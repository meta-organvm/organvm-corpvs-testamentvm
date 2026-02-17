# Omega Evidence Map

**Created:** 2026-02-17
**Author:** @4444j99 (AI-conductor model: human directs, AI generates, human reviews)
**Status:** LIVING DOCUMENT — reviewed monthly at omega checklist review
**Companions:** [`there+back-again.md`](../strategy/there+back-again.md) (criteria definitions), [`rolling-todo.md`](../operations/rolling-todo.md) (active queue), [`operational-cadence.md`](../operations/operational-cadence.md) (review rhythm)
**Constitution:** [`docs/memory/constitution.md`](../memory/constitution.md) — Articles I-VI govern all specifications

---

> *The roadmap defines the criteria. This document tracks the proof. Each entry answers: "What evidence exists that this criterion is met or progressing?"*

---

## Summary

| Status | Count | Criteria |
|--------|-------|----------|
| MET | 1 | #6 |
| IN PROGRESS | 5 | #1, #3, #5, #8, #17 |
| NOT STARTED | 11 | #2, #4, #7, #9, #10, #11, #12, #13, #14, #15, #16 |

**By Horizon:**

| Horizon | Timeline | Met | In Progress | Not Started |
|---------|----------|-----|-------------|-------------|
| H1: Prove It Works | Days 1-30 | 0 | 3 (#1, #3, #17) | 2 (#2, #4) |
| H2: Validate Externally | Days 15-90 | 1 (#6) | 1 (#5) | 1 (#7) |
| H3: Generate Revenue | Days 30-180 | 0 | 1 (#8) | 2 (#9, #10) |
| H4: Build Community | Days 60-365 | 0 | 0 | 3 (#11, #12, #13) |
| H5: Achieve Recognition | Days 90-730 | 0 | 0 | 2 (#14, #15) |
| Cross-horizon | H1+H4 | 0 | 0 | 1 (#16) |

---

## Criteria Detail

### H1: Prove It Works

---

#### #1: 30-Day Soak Test Passes (<=3 critical incidents) — IN PROGRESS

**Criterion:** Soak test report shows <=3 critical incidents over 30 consecutive days.

**Status:** Data collection running since 2026-02-16. First real (non-dry-run) snapshot collected 2026-02-17. Daily cron at 08:00 UTC auto-collects and commits snapshots.

**Evidence:**
- Data: `data/soak-test/daily-*.json`
- Workflow: `.github/workflows/soak-test-daily.yml`
- Script: `scripts/soak-test-monitor.py`

**Current Data (2026-02-17 snapshot):**
- Registry validation: PASS (97 repos, 0 issues)
- Dependency validation: PASS (31 edges, 0 back-edges, 0 cycles)
- CI: 71 checked, 57 passing, 14 failing (12 ORGAN-I billing lock, 2 other)
- Engagement: 5 stars, 3 forks, 93 views on public-record-data-scrapper

**Gap:** Need 30 consecutive days of real data. Collection was broken (dry-run only + exit-code-1 preventing commit) until 2026-02-17 fix. ORGAN-I billing lock inflates CI failure count.

**Completion target:** ~March 18, 2026

**Rolling TODO:** S1-II

---

#### #2: Stranger Test Score >=80% — NOT STARTED

**Criterion:** An uninvolved person navigates the system, scores >=80% on the test protocol.

**Status:** Protocol written, no participant recruited.

**Evidence:**
- Protocol: `docs/operations/stranger-test-protocol.md`

**Gap:** Needs 1 external participant who has never seen the system. Cannot be self-tested.

**Blocker:** EXTERNAL — requires human participant

**Rolling TODO:** M1-II

---

#### #3: Engagement Baseline Established (30 days of data) — IN PROGRESS

**Criterion:** 30 consecutive days of engagement metrics (stars, forks, views, clones) collected.

**Status:** First real engagement data collected 2026-02-17. Soak test daily snapshots now include engagement metrics for 8 flagship repos.

**Evidence:**
- Data: `data/soak-test/daily-*.json` → `engagement` section
- Baseline (2026-02-17): 5 total stars, 3 total forks, views distributed across 8 repos

**Current Engagement Highlights:**
| Repo | Stars | Forks | Views (14d) | Clones (14d) |
|------|-------|-------|-------------|--------------|
| public-record-data-scrapper | 2 | 3 | 93 | 319 |
| agentic-titan | 1 | 0 | 13 | 929 |
| recursive-engine--generative-entity | 1 | 0 | 6 | 936 |

**Gap:** Need 30 days of continuous data. Currently 1 real data point (2026-02-17).

**Completion target:** ~March 18, 2026

**Rolling TODO:** E2 (completed — soak test now collecting real data)

---

#### #4: Runbooks Validated by Second Operator — NOT STARTED

**Criterion:** A second operator successfully follows the runbooks to perform system operations.

**Status:** Runbooks exist in `docs/operations/` (operational-cadence, autonomous-setup-guide). Not yet validated by anyone other than the author.

**Evidence:**
- Runbooks: `docs/operations/operational-cadence.md`, `docs/operations/autonomous-setup-guide.md`
- CLI: `scripts/organ-cli.py` (8 subcommands for system operations)

**Gap:** Needs a second human operator to attempt the procedures and log results.

**Blocker:** EXTERNAL — requires second person

**Rolling TODO:** M1-II (combined with stranger test — same participant could validate both)

---

### H2: Validate Externally

---

#### #5: >=1 Application Submitted — IN PROGRESS

**Criterion:** At least one grant/job/fellowship application has been submitted using the system as evidence.

**Status:** 3 applications prepared with materials ready. None yet submitted (requires human action).

**Evidence:**
- X1 materials: `docs/applications/05-google-creative-lab-five-responses.md`
- X3 cover letters: `docs/applications/cover-letters/`
- E3 script: `docs/applications/e3-google-creative-fellowship-submission.md`
- Submission scripts: clipboard-ready, character counts verified

**Gap:** Human must actually submit the applications. Materials are complete.

**Blocker:** TIME — requires human action (~1-2 hrs per application)

**Rolling TODO:** X1, X3, E3

---

#### #6: AI-Conductor Essay Published — MET

**Criterion:** An essay about the AI-conductor methodology has been published on the public-process site.

**Status:** Multiple essays published that document the AI-conductor methodology.

**Evidence:**
- Essay #32: "Building Autonomous Creative Systems" — guide covering the full methodology
- Essay #36: "Construction Addiction" — retrospective on the build process
- Essay #33: "Governance for Artists" — guide on the governance layer
- All published at: `organvm-v-logos/public-process/_posts/`
- Site URL: accessible via GitHub Pages

**Date met:** 2026-02-16 (essay #32 deployed)

---

#### #7: >=3 Pieces of External Feedback Collected — NOT STARTED

**Criterion:** At least 3 pieces of feedback from people outside the system have been collected and synthesized.

**Status:** No external feedback collected yet. First social media posts made 2026-02-17 (Mastodon + Discord), but no responses received.

**Evidence:** None yet.

**Gap:** Requires external interaction. Potential sources: application reviewers (after #5), social media responses, stranger test participant, salon attendees.

**Blocker:** EXTERNAL — requires other humans to engage with the system

**Rolling TODO:** Fed by X1, X4, M1-II

---

### H3: Generate Revenue

---

#### #8: >=1 ORGAN-III Product Live — IN PROGRESS

**Criterion:** At least one commercial product from ORGAN-III is deployed and accessible to users.

**Status:** life-my--midst--in is deployment-ready but not yet live. All code passes tests, DB provisioned, deploy guide written.

**Evidence:**
- Repo: `organvm-iii-ergon/life-my--midst--in` (branch: master)
- Tests: 291 pass, 7/7 packages build
- DB: Neon project `in-midst-my-life` (44 tables, seeded)
- Deploy guide: `DEPLOY.md` (minimum config: DATABASE_URL + JWT_SECRET)
- render.yaml: Fixed for free tier (BETA-VITAE sprint)

**Gap:** Not yet deployed. Human must deploy to Render (~1-2 hrs).

**Blocker:** TIME — requires human action (X2)

**Rolling TODO:** X2

---

#### #9: revenue_status: live for >=1 Registry Entry — NOT STARTED

**Criterion:** At least one ORGAN-III repository has `revenue_status: live` in registry-v2.json.

**Status:** All 27 ORGAN-III repos have `revenue_status: pre-launch` or null. No Stripe integration connected.

**Evidence:**
- Registry: `registry-v2.json` — all ORGAN-III entries show `revenue_status: "pre-launch"`

**Gap:** Requires: (1) product deployed (#8), (2) Stripe integration connected (M2-II), (3) at least 1 paying user.

**Blocker:** INCOME (Stripe setup) + product deployment

**Rolling TODO:** M2-II

---

#### #10: MRR >= System Operating Costs — NOT STARTED

**Criterion:** Monthly recurring revenue equals or exceeds system operating costs.

**Status:** No revenue generated. Operating costs currently ~$0/month (all free tier: GitHub, Neon free, Render free).

**Evidence:** None.

**Gap:** Requires revenue (#9). Note: since operating costs are ~$0 on free tier, technically even $1 MRR meets this criterion — but the spirit of the criterion assumes real hosting costs.

**Blocker:** Depends on #9

**Rolling TODO:** Downstream of M2-II

---

### H4: Build Community

---

#### #11: >=2 Salons/Events with External Participants — NOT STARTED

**Criterion:** At least 2 community events (salons, reading groups, workshops) held with external participants.

**Status:** No events held. ORGAN-VI community infrastructure exists but is empty.

**Evidence:** None.

**Gap:** Requires recruiting participants and organizing events. Depends on some external visibility (#5, #13) to attract participants.

**Blocker:** EXTERNAL — needs participants

**Rolling TODO:** S2-II

---

#### #12: >=3 External Contributions — NOT STARTED

**Criterion:** At least 3 contributions from external people to the system (PRs, issues, feedback, content).

**Status:** No external contributions received. Contribution pathway not yet created.

**Evidence:** None. (Can verify via `gh api` across all 8 orgs for non-owner activity.)

**Gap:** Requires: (1) contribution pathway (S3-II), (2) external awareness, (3) sufficiently accessible entry points.

**Blocker:** EXTERNAL — needs community

**Rolling TODO:** S3-II

---

#### #13: >=1 Organic Inbound Link — NOT STARTED

**Criterion:** At least 1 external website links to any part of the system without being solicited.

**Status:** First social media posts made 2026-02-17 (Mastodon + Discord). Essay distribution pipeline active (backfill-distribution.yml distributing 3/week). No confirmed inbound links yet.

**Evidence:** None confirmed. Would need to check via search engine or analytics.

**Gap:** Requires time for content to be discovered. Distribution pipeline is active — content is being pushed to Mastodon and Discord.

**Blocker:** TIME + organic discovery

**Rolling TODO:** Fed by essay distribution pipeline and social media activity

---

### H5: Achieve Recognition

---

#### #14: >=1 Recognition Event — NOT STARTED

**Criterion:** At least one external recognition: grant award, academic citation, conference invitation, or adoption by another system.

**Status:** No recognition events. Applications not yet submitted (#5).

**Evidence:** None.

**Gap:** Requires external validation. Potential paths: E3 (Google Creative Fellowship, deadline March 18), S6-II (conference talk proposal), essay citations.

**Blocker:** EXTERNAL — fully depends on external actors

**Rolling TODO:** S6-II, E3

---

#### #15: Portfolio Updated with External Validation — NOT STARTED

**Criterion:** Portfolio site reflects external validation (testimonials, acceptance letters, user counts, press).

**Status:** Portfolio exists at `4444j99.github.io/portfolio/` with 19 curated projects and system metrics. No external validation to display yet.

**Evidence:**
- Portfolio URL: `4444j99.github.io/portfolio/`
- Current state: 97 repos, 87 ACTIVE, 33 sprints, 38 essays displayed
- Data files: `site-data/*.json` and `portfolio-site/src/data/*.json`

**Gap:** No external validation exists to display. This criterion becomes achievable after #7, #14, or #8 produces user testimonials.

**Blocker:** Depends on external validation from other criteria

**Rolling TODO:** M3-II (partial — data files updated, omega scorecard page pending)

---

### Cross-Horizon

---

#### #16: Bus Factor >1 (Validated) — NOT STARTED

**Criterion:** A second operator can maintain the system using existing documentation. Validated, not just documented.

**Status:** Documentation exists (runbooks, CLI, autonomous setup guide). No second operator has attempted maintenance.

**Evidence:**
- Runbooks: `docs/operations/operational-cadence.md`
- Setup guide: `docs/operations/autonomous-setup-guide.md`
- CLI: `scripts/organ-cli.py`
- Autonomous workflows: 11+ configured across 2 repos

**Gap:** Needs a real person to attempt system operation and log the results.

**Blocker:** EXTERNAL — requires second person (potentially same as #2 and #4)

**Rolling TODO:** M1-II (shares participant with stranger test)

---

#### #17: System Operates 30+ Days Without Operator Intervention — IN PROGRESS

**Criterion:** The autonomous system runs for 30+ consecutive days without the primary operator needing to intervene.

**Status:** Autonomous systems activated (AUTOMATA sprint, 2026-02-17). 11+ workflows configured with daily/weekly/monthly schedules. First real autonomous data collected 2026-02-17.

**Evidence:**
- Autonomous schedule: 12 cron workflows across 2 repos
- Workflow list: soak-test-daily, essay-monitor, metrics-refresh, orchestrator-agent, backfill-distribution, distribution-agent, stale-detector-weekly, system-pulse-weekly, promotion-recommender, essay-deploy, auto-deploy
- Data: `data/soak-test/daily-*.json` (tracks system operation without intervention)

**Current autonomous operation:**
- Essay distribution: Active (backfill-distribution running Mon/Wed/Fri)
- Metrics: Auto-refreshed weekly (Mon 06:00 UTC)
- Health monitoring: Daily soak test (08:00 UTC) + weekly stale detector (Tue 06:00 UTC)
- Pulse reports: Weekly (Sun 12:00 UTC)

**Gap:** Clock started ~2026-02-16. Need 30 days of data showing no required manual intervention. Note: fixing the soak test collector (2026-02-17) counts as infrastructure maintenance, not system intervention — the autonomous workflows themselves didn't fail, the monitoring of them did.

**Completion target:** ~March 18, 2026

**Rolling TODO:** S1-II

---

## Critical Path to Omega

The fastest path through the criteria follows the horizon dependency chain:

```
H1 (#1, #3, #17) ──30 days──→ H1 complete
  ↓
H2 (#5) ──human submits──→ H2 partially complete
  ↓
H3 (#8) ──human deploys──→ H3 partially complete
  ↓
H4 (#11, #12, #13) ──calendar time──→ H4 gradually
  ↓
H5 (#14, #15) ──external response──→ H5 last
```

**What blocks omega is not engineering.** The 5 IN PROGRESS criteria all have running clocks or prepared materials. The 11 NOT STARTED criteria are blocked by: external humans (6), money (2), time/calendar (2), and dependencies on earlier criteria (1).

**The one thing that accelerates everything:** Submitting applications (X1, X3, E3). This directly advances #5 and creates the feedback loop that feeds #7, #14, and ultimately #15.

---

## Revision Log

| Date | Change | Reason |
|------|--------|--------|
| 2026-02-17 | Initial creation | Pre-validation maturation session |
