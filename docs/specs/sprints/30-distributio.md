# Sprint 30: DISTRIBUTIO

**Date:** 2026-02-17
**Focus:** Autonomous essay distribution pipeline
**Status:** COMPLETE

## Problem

The organ system has 35 published essays and an active distribution pipeline (Mastodon + Discord secrets live since 2026-02-11), but the pipeline only handles *new* essays detected within a 7-day lookback window. All 35 existing essays — published Feb 10-16 — are past the window and will never be automatically distributed. The omega scorecard is 1/17 (only #6 met), and criterion #13 (organic inbound link) requires content to actually reach external audiences.

Additionally, the essay-monitor creates issues with slug-derived titles (e.g., "Ai Conductor Methodology" instead of the actual frontmatter title), and distribute-content posts link to GitHub issues rather than the essay URL on the public-process site.

**AP-1 override:** User explicitly chose to override the "no new named sprints until X1-X4" rule. This sprint creates external surface area that directly enables X4 (first social post) and advances #13.

## Solution

Build a backfill workflow that drip-feeds the essay backlog at 3/week cadence (Mon/Wed/Fri 14:00 UTC), completing in ~12 weeks. Enhance the essay-monitor to extract Jekyll frontmatter for rich metadata. Enhance distribute-content to use essay excerpts, proper URLs, and tag-derived hashtags instead of generic posts.

## Deliverables

### 1. Backfill distribution workflow (`backfill-distribution.yml`)
- NEW workflow in orchestration-start-here
- Cron: Mon/Wed/Fri 14:00 UTC + `workflow_dispatch`
- Inline Python: fetches all essays from public-process `_posts/`, parses YAML frontmatter, checks existing issues (paginated, both open + closed), creates 1 issue per run for the oldest undistributed essay
- Issue body includes structured fields: Title, Date, URL, Excerpt, Tags, Category, Reading Time, Source
- Labels: `essay-detected`, `ready-to-distribute`, `backfill`
- Exits cleanly when all essays are tracked ("Backfill complete!")
- **Impact:** 35 essays distributed over ~12 weeks at sustainable 3/week cadence

### 2. Enhanced essay-monitor (`essay-monitor.yml`)
- MODIFIED workflow in orchestration-start-here
- Now fetches raw essay content via GitHub API to read Jekyll frontmatter
- Uses frontmatter `title` instead of filename-derived slug
- Issue body includes Excerpt, Tags, Category, Reading Time fields (same format as backfill)
- Paginated duplicate detection (handles >100 issues)
- **Impact:** New essays get rich metadata from day one — same quality as backfilled essays

### 3. Enhanced distribute-content (`distribute-content.yml`)
- MODIFIED workflow in orchestration-start-here
- Metadata extraction: parses `**Excerpt:**`, `**Tags:**`, `**URL:**`, `**Category:**`, `**Reading Time:**` from structured issue body, with fallback to old format
- Mastodon: posts with essay excerpt (not title), essay URL (not issue URL), tag-derived hashtags (e.g., `ai-conductor` -> `#aiconductor`) plus constant `#organvm #buildinginpublic`
- Discord: rich embed with category as footer, reading_time appended
- Security: all `github.event.*` data passed via `env:` block, Mastodon and Discord posting moved into Python to eliminate shell interpolation of untrusted data
- LinkedIn and Ghost steps converted to same safe Python pattern
- Auto-close + `distributed` label preserved (already existed)
- **Impact:** Social posts are now well-crafted, linking to the essay site with proper excerpts and hashtags

### 4. Sprint spec (`docs/specs/sprints/30-distributio.md`)
- This document

### 5. Documentation updates
- `rolling-todo.md`: note DISTRIBUTIO progress on X4
- `sprint-catalog.md`: mark catalog item 24 DISTRIBUTIO as COMPLETE

## Autonomous Schedule After Sprint

```
EXISTING (unchanged):
  Daily 08:00 UTC  soak-test-daily.yml (health data)
  Daily 09:00 UTC  essay-monitor.yml (detect new essays) [ENHANCED]
  Mon 06:00 UTC    metrics-refresh.yml (calculate + propagate)
  Mon 07:00 UTC    orchestrator-agent.yml (system graph)
  Wed 10:00 UTC    distribution-agent.yml (POSSE audit)
  Sun 12:00 UTC    system-pulse-weekly.yml (status report)
  1st 08:00 UTC    promotion-recommender.yml (evaluations)
  On push master   auto-deploy.yml (life-my--midst--in)

NEW:
  Mon 14:00 UTC    backfill-distribution.yml (1 essay)
  Wed 14:00 UTC    backfill-distribution.yml (1 essay)
  Fri 14:00 UTC    backfill-distribution.yml (1 essay)
```

**Backfill timeline:** 35 essays / 3 per week = ~12 weeks (~May 2026). After that, the cron continues but exits immediately. The essay-monitor handles any new essays.

## Metrics Delta

| Metric | Before | After |
|--------|--------|-------|
| Sprint count | 29 | 30 |
| Autonomous cron workflows | 9 | 10 (+backfill-distribution) |
| Essay distribution coverage | 0/35 (0%) | Climbing 3/week toward 35/35 |
| Social media posts (autonomous) | 0 | 3/week scheduled |
| Omega #13 progress | NOT MET | IN PROGRESS (surface area created) |

## Files Changed

| File | Repo | Action |
|------|------|--------|
| `.github/workflows/backfill-distribution.yml` | orchestration-start-here | Created |
| `.github/workflows/essay-monitor.yml` | orchestration-start-here | Modified |
| `.github/workflows/distribute-content.yml` | orchestration-start-here | Modified |
| `docs/specs/sprints/30-distributio.md` | corpvs-testamentvm | Created |
| `docs/operations/rolling-todo.md` | corpvs-testamentvm | Modified |
| `docs/strategy/sprint-catalog.md` | corpvs-testamentvm | Modified |
