# ADR-011: Soak Test Design

## Status

Accepted

## Date

2026-02-16

## Context

The omega roadmap requires criterion #1 ("System runs autonomously for 30+ days") and #17 ("Autonomous operation verified") before the system can claim maturity. These criteria require *evidence* — not a one-time check, but sustained operation data over a meaningful time window.

The system needed a testing approach that:
1. Runs daily without human intervention
2. Collects data across all 4 system dimensions (registry, dependencies, CI, engagement)
3. Produces a 30-day dataset suitable for trend analysis
4. Does not interfere with normal system operation (non-invasive observation)

An earlier version of the soak test used `exit 1` on any validation failure, which caused the GitHub Actions workflow to show as "failed" — creating noise in the CI health data it was supposed to be measuring. This was counterproductive.

## Decision

### Architecture

The soak test is implemented as `scripts/soak-test-monitor.py` with two subcommands:
- **`collect`**: Runs daily (08:00 UTC via `soak-test-daily.yml`), collects a snapshot and appends it to `data/soak-test/YYYY-MM-DD.json`
- **`report`**: Analyzes the accumulated snapshots and generates a summary with pass/fail verdicts

### Data Collection (per daily snapshot)

1. **Registry validation**: Runs `praxis-validate.py` — checks schema, required fields, status enums
2. **Dependency graph**: Validates DAG properties — no cycles, no back-edges, maximum depth within bounds
3. **CI health**: Queries `gh api` for latest workflow run per repo — records pass/fail/skipped
4. **Engagement metrics**: Stars, forks, views, clones via GitHub API (where available)

### Key Design Decisions

- **Always exit 0**: The soak test workflow always succeeds. Failures are recorded in the JSON data, not as workflow exit codes. This prevents the soak test from polluting its own CI health data.
- **30-day window**: Chosen to span a full billing cycle, capture weekly and monthly patterns, and provide enough data points (30) for meaningful trend analysis.
- **Append-only**: Each daily snapshot is a separate file. No overwriting, no compaction. The full history is preserved.
- **ORGAN-I billing lock acknowledged**: ORGAN-I repos fail CI due to a billing issue external to the system. The soak test records this as a known condition, not an incident.

## Consequences

### Positive

- **Non-invasive**: The soak test observes but does not modify any system state
- **Self-documenting**: Each snapshot is a complete system health record with timestamp
- **Automated**: Runs daily without human intervention — the core requirement for autonomy claims
- **Evidence-grade**: 30 daily snapshots constitute auditable evidence for omega criteria
- **Trend-friendly**: Time-series data enables "is the system improving or degrading?" analysis

### Negative

- **API rate consumption**: Daily queries across 97 repos consume GitHub API quota. Mitigated by using a single PAT with adequate rate limits.
- **Stale on weekends**: The system changes slowly on weekends but the soak test still runs — some snapshots may be identical to the previous day
- **No alerting**: The soak test collects data but does not alert on anomalies. A separate system-pulse-weekly.yml generates reports, but real-time alerting doesn't exist.
- **ORGAN-I noise**: ~20 repos perpetually fail CI due to billing lock — this is expected noise that must be filtered in analysis

## References

- Monitor script: `scripts/soak-test-monitor.py`
- Daily workflow: `.github/workflows/soak-test-daily.yml`
- Report template: `docs/evaluation/soak-test-report-template.md` (created for analysis)
- Omega criteria: `docs/strategy/there+back-again.md` (#1, #17)
- Pre-validation maturation: Fixed dry-run→real data (2026-02-17)
