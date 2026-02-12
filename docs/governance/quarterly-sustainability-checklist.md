# Quarterly Sustainability Checklist

**Purpose:** Minimal viable audit for solo operator maintenance of 79 repos across 8 orgs
**Cadence:** Quarterly (Q2 2026 is first execution)
**Estimated effort:** 1-2 hours per quarter
**Source:** Doc 11 Priority 4 recommendation; simplified from `orchestration-system-v2.md` monthly spec

---

## Pre-Audit

- [ ] Note the date and quarter (e.g., "Q2 2026 — 2026-04-15")
- [ ] Confirm `registry-v2.json` is the working copy (not stale)

## 1. Registry Currency Check

- [ ] Run `python scripts/v3-registry-reconciliation.py` — confirm 0 missing repos, 0 extra repos
- [ ] Check for new repos created on GitHub not in registry: `gh api orgs/ORGNAME/repos --jq '.[].name'` for each org
- [ ] Verify `total_repos` count matches actual registry entries
- [ ] Spot-check 3 random repos: does GitHub description match registry description?

## 2. Broken Link Sweep

- [ ] Run `python scripts/v1-v2-link-tbd-audit.py` — note any new broken links
- [ ] Fix broken system links (highest priority)
- [ ] Triage external broken links (may be temporary outages)

## 3. Dependency Validation

- [ ] Run `python scripts/v4-dependency-validation.py` — confirm 0 violations
- [ ] Check for new dependencies added since last quarter

## 4. Constitution Gate Check

- [ ] Run `python scripts/v5-v6-constitution-organ-checks.py` — all 8 organs should PASS
- [ ] If any organ fails, investigate and fix before proceeding

## 5. CI Workflow Health

- [ ] Check GitHub Actions status for flagship repos (8 repos): any failed runs?
- [ ] Verify `monthly-organ-audit.yml` has run at least once since last quarter
- [ ] Check for GitHub Actions deprecation warnings (Node.js version, action versions)

## 6. Content Freshness

- [ ] Are any essays outdated by project changes? (e.g., if a repo was archived that an essay references)
- [ ] Are flagship README word counts still ≥ 3,000? (spot-check 2-3)
- [ ] Has any flagship repo's code changed significantly without README update?

## 7. Promotion Obligation Status

- [ ] Query registry for `promotion_obligations` with `status: "PENDING"`:
  ```
  python3 -c "import json; [print(f'{r[\"org\"]}/{r[\"name\"]}: {o}') for org in json.load(open('registry-v2.json'))['organs'].values() for r in org['repositories'] for o in r.get('promotion_obligations', []) if o['status'] == 'PENDING']"
  ```
- [ ] For each PENDING obligation: is it still relevant? Should it be started, deferred, or cancelled?

## 8. Implementation Status Drift

- [ ] Count SKELETON + DESIGN_ONLY repos: has the number decreased since last quarter?
- [ ] Have any PRODUCTION repos degraded (dependencies outdated, tests failing)?
- [ ] Are the 5 highest-portfolio-relevance SKELETON repos making progress?

## Post-Audit

- [ ] Update `last_validated` dates in registry for any repos checked in detail
- [ ] Record audit results (pass/fail per section) in a dated entry below
- [ ] If critical issues found, create tracking items (registry notes or GitHub issues)

---

## Audit Log

| Quarter | Date | Operator | Result | Notes |
|---------|------|----------|--------|-------|
| Q2 2026 | TBD | @4444j99 | — | First quarterly audit |

---

## Scope Boundary

This checklist is intentionally minimal. It replaces the full monthly audit specification in `orchestration-system-v2.md` with a quarterly cadence appropriate for solo operation. If the project gains contributors, revisit the monthly spec.

Items explicitly excluded from this checklist (defer to when relevant):
- POSSE distribution metrics (no audience to measure yet)
- Community engagement tracking (ORGAN-VI not yet active)
- Framework extraction progress (deferred per D-06)
- Security audit of dependencies (add when code repos mature)
