# Sprint 33: OPERATIO

**Date:** 2026-02-17
**Focus:** Autonomous operations batch — TODO housekeeping, essay auto-deploy, CLI tooling, health dashboard
**Status:** COMPLETE

## Problem

Four operational gaps after SENSORIA (Sprint 32): (1) rolling-todo.md was stale with unrecorded SENSORIA completions, (2) the essay lifecycle still had one manual step (git push from docs/essays/ to public-process/_posts/), (3) common operations required remembering individual script names, (4) no visual health dashboard existed for soak test trends.

**AP-1 context:** This work was executed as a batch in weekly-rhythm mode (not a named sprint), bundling four catalog items: INSTRUMENTUM (#58), AUTOMATIA (#59), OBSERVATIO (#60), plus TODO housekeeping.

## Solution

Four-part batch: (D) governance housekeeping, (A) essay auto-deploy pipeline, (C) unified CLI tool, (B) static HTML health dashboard.

## Deliverables

### 1. TODO Housekeeping (Option D)

- Marked M4-II as COMPLETED (seed.yaml 44%→100%, Sprint 32 SENSORIA)
- Marked E2 as COMPLETED (soak test configured without --dry-run, first cron 2026-02-18)
- Added M7-II: 3 repos archived on GitHub but ACTIVE in registry
- Added M8-II: 5 ghost repos (registry entries with no GitHub remote)
- Updated provenance summary (24→26 items, 2→4 completed)

### 2. Essay Auto-Deploy Pipeline (Option A — AUTOMATIA #59)

- New `scripts/essay-deploy.py` — scans docs/essays/ for ready essays (complete frontmatter: layout, title, date), compares against remote _posts/ via gh API, pushes undeployed essays via `gh api PUT`
- Modes: dry-run (default) and --deploy
- New `.github/workflows/essay-deploy.yml` — triggers on push to main when `docs/essays/*.md` changes, plus workflow_dispatch
- Uses CROSS_ORG_TOKEN for cross-org push to organvm-v-logos/public-process
- Closes the last manual step in the essay lifecycle: author → detect → distribute is now fully autonomous

### 3. CLI Tooling (Option C — INSTRUMENTUM #58)

- New `scripts/organ-cli.py` — unified entry point with 8 subcommands:
  - `registry show <repo>` — pretty-print a registry entry
  - `registry validate` — validate schema (required fields, status enums, ORGAN-III fields, back-edge detection)
  - `registry update <repo> <field> <value>` — update field with validation
  - `metrics refresh` — run calculate-metrics + propagate-metrics pipeline
  - `invoke <ID>` — wrapper around invoke.py
  - `soak status` — latest snapshot + VIGILIA progress bar
  - `deploy essay [--dry-run]` — wrapper around essay-deploy.py
  - `pulse` — generate system pulse report
- stdlib-only (json, argparse, subprocess, pathlib)
- Registry validator checks: required fields, implementation_status enum, ORGAN-III revenue fields, dependency back-edges, count consistency

### 4. Health Dashboard (Option B — OBSERVATIO #60)

- New `scripts/generate-dashboard.py` — reads soak-test snapshots + system-metrics.json, generates self-contained HTML
- Inline SVG charts (no external JS dependencies)
- CMYK color scheme (Jost font, matching portfolio site)
- Sections: VIGILIA progress bar, system overview stats, validation status, organ distribution, CI stability trends, engagement trends
- Responsive design (works on mobile)
- Integrated into `system-pulse-weekly.yml` — dashboard regenerated every Sunday alongside pulse report

## Metrics Delta

| Metric | Before | After |
|--------|--------|-------|
| Sprint count | 32 | 33 |
| Rolling TODO completed items | 2 | 4 |
| Rolling TODO total items | 24 | 26 |
| Manual essay pipeline steps | 1 (git push) | 0 (fully autonomous) |
| CLI entry points | ~10 individual scripts | 1 unified CLI + scripts |
| Dashboard | None | data/dashboard/index.html |
| Autonomous workflows (corpvs) | 4 | 5 (+ essay-deploy) |

## Files Created

| File | Purpose |
|------|---------|
| `scripts/essay-deploy.py` | Detect + deploy essays to public-process |
| `scripts/organ-cli.py` | Unified CLI for common operations |
| `scripts/generate-dashboard.py` | Generate static HTML health dashboard |
| `.github/workflows/essay-deploy.yml` | Auto-trigger essay deployment on push |
| `data/dashboard/index.html` | Generated dashboard output |
| `docs/specs/sprints/33-operatio.md` | This sprint spec |

## Files Modified

| File | Change |
|------|--------|
| `docs/operations/rolling-todo.md` | M4-II + E2 completed, M7-II + M8-II added |
| `.github/workflows/system-pulse-weekly.yml` | Added dashboard generation step |
| `system-metrics.json` | sprints 32→33, added 33-operatio |
| `docs/strategy/sprint-catalog.md` | Added OPERATIO completion entries |
