# ADR-012: Billing Guardrails

## Status

Accepted

## Date

2026-02-14

## Context

On 2026-02-14, the `organvm-i-theoria` GitHub organization exceeded its GitHub Actions minutes allocation by a significant margin — 48,880 minutes consumed. This triggered a billing lock that prevented all CI workflows from running across all 20 ORGAN-I repositories.

**Root cause analysis:**
- ORGAN-I had 14 cron-triggered workflows running daily or weekly across 20 repos
- Several of these were computationally expensive (ML training, large test suites)
- The free-tier GitHub Actions allocation (2,000 minutes/month for free orgs) was insufficient
- Additionally, batch operations during ORGAN-II and ORGAN-III sprints (pushing changes to many repos simultaneously) triggered CI runs that consumed minutes in bursts

**Immediate impact:**
- All ORGAN-I CI became non-functional
- The soak test recorded ORGAN-I as perpetually failing — degrading signal quality
- No code changes could be validated via CI for any ORGAN-I repo

## Decision

### Immediate Response (Sprint 12 ILLUSTRATIO)

Disabled 17 cron workflows across the system:
- **14 in ORGAN-I**: All scheduled workflows (daily/weekly) disabled
- **3 in ORGAN-III**: Non-essential crons disabled (anon-hookup-now news.yml, fetch-familiar-friends codeql.yml, life-my--midst--in performance.yml)

Workflows were disabled by removing `schedule:` triggers from the YAML files, preserving `push:` and `pull_request:` triggers so CI still runs on code changes.

### Ongoing Policy

1. **No new cron workflows** without explicit billing impact assessment
2. **Push-triggered CI only** as the default — cron schedules require justification
3. **Soak test acknowledges billing lock**: ORGAN-I failures are classified as "known external condition" in soak test analysis
4. **Free-tier awareness**: All 8 orgs use GitHub Free — 2,000 minutes/month per org is the hard constraint
5. **Batch operation awareness**: When pushing to many repos (e.g., seed.yaml deployment), stagger pushes or accept the burst CI cost

### Future Mitigation

When income allows (rolling-todo G-items), options include:
- GitHub Team plan ($4/user/month) for orgs that need cron workflows
- Self-hosted runners for compute-heavy jobs
- Selective cron re-enablement with conservative schedules (weekly, not daily)

## Consequences

### Positive

- **Bleeding stopped**: No further billing overruns after disabling crons
- **Signal clarity**: Non-ORGAN-I CI is clean — failures represent real issues, not billing artifacts
- **Policy established**: Future cron additions require explicit justification
- **Cost awareness**: The team (currently just one person) is now attuned to CI minutes as a resource

### Negative

- **ORGAN-I is degraded**: No scheduled CI means regressions in ORGAN-I repos may go undetected between pushes
- **Soak test noise**: ORGAN-I perpetually shows as "failing" in soak data — requires manual filtering in analysis
- **Capability loss**: Useful workflows (security scanning, dependency updates, performance monitoring) are disabled
- **External dependency**: Resolving the billing lock requires either payment or GitHub support — outside the system's autonomous control

## References

- ILLUSTRATIO sprint: `docs/specs/sprints/12-illustratio.md`
- Billing lock discovery: Sprint 12 investigation
- Disabled workflows: 14 ORGAN-I crons + 3 ORGAN-III crons (17 total)
- Soak test handling: `scripts/soak-test-monitor.py` (ORGAN-I filter)
- Rolling TODO: M6-II (CI restructure) in `docs/operations/rolling-todo.md`
