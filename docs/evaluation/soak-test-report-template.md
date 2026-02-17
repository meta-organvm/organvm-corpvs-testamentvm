# Soak Test Report — 30-Day Autonomous Operation Assessment

**Test Period:** [START_DATE] to [END_DATE]
**Collection Schedule:** Daily at 08:00 UTC via `soak-test-daily.yml`
**Data Location:** `data/soak-test/YYYY-MM-DD.json`
**Report Generated:** [REPORT_DATE]
**Author:** [AUTHOR]

---

## Executive Summary

**Overall Verdict:** [PASS / CONDITIONAL PASS / FAIL]

| Metric | Result | Notes |
|--------|--------|-------|
| Days of data collected | /30 | |
| Registry validation pass rate | % | |
| Dependency graph valid (all days) | Yes/No | |
| CI pass rate (non-billing) | % | |
| Incidents (critical) | | |
| Incidents (warning) | | |
| Autonomous operation gaps | | Days requiring manual intervention |

---

## 1. Test Parameters

- **Start date:** [DATE] (first real data collection after dry-run fix)
- **End date:** [DATE] (30th day of collection)
- **Collection method:** `scripts/soak-test-monitor.py collect`
- **Report method:** `scripts/soak-test-monitor.py report --days 30`
- **Total repos monitored:** 97 (87 ACTIVE, 10 ARCHIVED)
- **Known conditions:**
  - ORGAN-I repos (~20) expected to fail CI due to billing lock (external dependency)
  - 17 cron workflows disabled (billing guardrails, see ADR-012)

---

## 2. Registry Stability

| Day | Validation Result | Changes | Notes |
|-----|------------------|---------|-------|
| 1 | | | |
| ... | | | |
| 30 | | | |

**Summary:**
- Total validation passes: /30
- Registry changes during test period: [count]
- Schema violations: [count]

---

## 3. Dependency Graph Integrity

| Check | Result | Details |
|-------|--------|---------|
| DAG validation (no cycles) | | |
| Back-edge check | | |
| Maximum depth | | |
| Edge count | /31 declared | |

**Summary:** [DAG remained stable / changes detected / violations found]

---

## 4. CI Health Trend

### Daily Pass Rate (Non-ORGAN-I)

| Day | Total Workflows | Passing | Failing | Skipped | Pass Rate |
|-----|----------------|---------|---------|---------|-----------|
| 1 | | | | | % |
| ... | | | | | % |
| 30 | | | | | % |

### Breakdown by Organ

| Organ | Repos | Workflows | Avg Pass Rate | Trend |
|-------|-------|-----------|---------------|-------|
| ORGAN-I | 20 | | N/A (billing lock) | N/A |
| ORGAN-II | 30 | | % | ↑↓→ |
| ORGAN-III | 27 | | % | ↑↓→ |
| ORGAN-IV | 7 | | % | ↑↓→ |
| ORGAN-V | 2 | | % | ↑↓→ |
| ORGAN-VI | 4 | | % | ↑↓→ |
| ORGAN-VII | 4 | | % | ↑↓→ |
| Meta | 3 | | % | ↑↓→ |

### CI Fixes Applied During Test Period

| Date | Repo | Fix | Impact |
|------|------|-----|--------|
| | | | |

---

## 5. Engagement Baseline

### Stars & Forks (30-day delta)

| Metric | Start | End | Delta |
|--------|-------|-----|-------|
| Total stars (all repos) | | | |
| Total forks (all repos) | | | |
| Top repo by stars | | | |

### Traffic (where available)

| Metric | 30-day Total | Weekly Average |
|--------|-------------|----------------|
| Unique visitors | | |
| Unique cloners | | |
| Page views | | |

### Distribution Pipeline Activity

| Metric | Count |
|--------|-------|
| Essays distributed (Mastodon + Discord) | |
| Distribution issues created | |
| Backfill distributions triggered | |

---

## 6. Incidents

### Critical (system down or data loss risk)

| # | Date | Description | Resolution | Time to Resolve |
|---|------|-------------|------------|-----------------|
| | | | | |

### Warning (degraded but functional)

| # | Date | Description | Resolution | Time to Resolve |
|---|------|-------------|------------|-----------------|
| | | | | |

### Informational (noted, no action required)

| # | Date | Description | Notes |
|---|------|-------------|-------|
| | | | |

---

## 7. Autonomous Operation Assessment

**Key question:** Did the system operate for 30+ days without human intervention?

| Dimension | Assessment |
|-----------|-----------|
| Daily soak test ran every day | Yes/No (missed: [dates]) |
| Weekly metrics refresh ran | Yes/No |
| Weekly system pulse generated | Yes/No |
| Essay distribution pipeline functional | Yes/No |
| Stale detector ran and reported | Yes/No |
| Manual interventions required | [count] |

**Manual interventions log:**

| Date | Action | Why | Avoidable? |
|------|--------|-----|-----------|
| | | | |

---

## 8. Omega Criteria Assessment

| # | Criterion | Verdict | Evidence |
|---|-----------|---------|----------|
| #1 | System runs autonomously for 30+ days | | [days of clean operation] |
| #3 | All 8 organs operational | | [organ status summary] |
| #17 | Autonomous operation verified | | [intervention count, pipeline success rate] |

---

## 9. Recommendations

### Before Claiming Omega Readiness

1. [Recommendation 1]
2. [Recommendation 2]
3. [Recommendation 3]

### For Next 30-Day Cycle

1. [Improvement 1]
2. [Improvement 2]

### Known Issues to Accept

1. ORGAN-I billing lock — external dependency, cannot be resolved autonomously
2. [Other known conditions]

---

## Appendix: Data Files

| File | Description |
|------|-------------|
| `data/soak-test/YYYY-MM-DD.json` | Daily snapshots (30 files) |
| `scripts/soak-test-monitor.py` | Collection and analysis script |
| `.github/workflows/soak-test-daily.yml` | Collection workflow |

---

*Template created: 2026-02-17. Fill in data when 30-day collection completes (~March 18, 2026). Run `python3 scripts/soak-test-monitor.py report --days 30` to generate raw data for each section.*
