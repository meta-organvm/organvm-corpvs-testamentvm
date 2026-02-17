# E2G-II Action Items — Prioritized

**Source:** `docs/evaluation/e2g-post-construction-review.md`
**Generated:** 2026-02-16
**Sprint context:** Post-BETA-VITAE (Sprint 27), post-construction system review
**Predecessor:** `docs/evaluation/e2g-action-items.md` (E2G-I, all P0/P1/P2 resolved)

---

## Priority Legend

- **P0 (CRITICAL):** Must do before any more internal sprints. These are the hermetic seal breakers.
- **P1 (HIGH):** Fix within the next 2 sprints. These strengthen external engagement.
- **P2 (MEDIUM):** Fix within the next 5 sprints. These improve system quality.
- **P3 (STRATEGIC):** Plan over the next month. These build long-term credibility.

---

## P0 — CRITICAL (Break the Hermetic Seal)

These are **human actions**, not sprint tasks. They cannot be automated or delegated to AI. They require opening a browser, filling out forms, and clicking "submit."

- [ ] **X1.** Submit Google Creative Lab Five application
  - Status: READY (materials at `docs/applications/05-google-creative-lab-five-responses.md`)
  - URL: https://www.creativelab5.com/
  - Time: ~1 hour
  - Omega criteria advanced: #5 (application submitted), feeds #7 (external feedback)
  - Finding: W1-II, SP1-II, LC3-II

- [ ] **X2.** Deploy life-my--midst--in to production hosting
  - Status: READY (DEPLOY.md written, Render Blueprint at repo root, 291 tests pass, 44 tables seeded on Neon)
  - Action: Click Render "Deploy" button or `render deploy` from life-my--midst--in repo root
  - Time: ~1-2 hours (deploy + verify)
  - Omega criteria advanced: #8 (product live)
  - Finding: W1-II, LC4-II, SP4-II

- [ ] **X3.** Submit 2 highest-fit job applications
  - Targets: Together AI Lead DX (6/10) and HuggingFace Dev Advocate (5/10)
  - Status: READY (cover letters at `docs/applications/cover-letters/`)
  - Time: ~2 hours
  - Omega criteria advanced: #5 (applications submitted), feeds #7 (external feedback)
  - Finding: W1-II, W6-II, ET3-II

- [ ] **X4.** Make first social media post
  - Platform: Mastodon or LinkedIn (whichever has an existing account)
  - Content: Link to AI-conductor essay with 2-3 sentence intro
  - Time: ~15 minutes
  - Omega criteria advanced: Feeds #7, #13 (inbound links)
  - Finding: W1-II, BS5-II, LC1-II

---

## P1 — HIGH (Strengthen External Engagement, Next 2 Sprints)

- [ ] **E1.** Refresh operational cadence Part IV with current priorities
  - Replace stale Week 1-4 actions with actual current state
  - Update beta candidate reference: public-record-data-scrapper → life-my--midst--in
  - Remove stale AI-conductor essay deployment action (already deployed 2026-02-11)
  - Update fit scores and priority queue to match current qualification assessment
  - Files: `docs/operations/operational-cadence.md` Part IV
  - Finding: W3-II
  - **Sprint:** 28 RECOGNITIO (this sprint)

- [ ] **E2.** Enable non-dry-run soak test monitoring
  - Current state: `data/soak-test/daily-2026-02-16.json` has `dry_run: true`, 0 CI checks, 0 engagement
  - Action: Configure soak-test-monitor.py for real data collection (GitHub API engagement tracking)
  - Omega criteria advanced: #1, #3, #17 (all passive — just need real data flowing)
  - Finding: W4-II

- [ ] **E3.** Submit Google Creative Fellowship application
  - Deadline: **March 18, 2026** (31 days from now)
  - Status: Materials ready, portfolio live
  - URL: https://creativefellowship.google/
  - Omega criteria advanced: #5, feeds #14 (recognition)
  - Finding: W6-II

- [ ] **E4.** Deploy essay drafts #34 and #35 if not already deployed
  - Current state: Drafts at `docs/essays/34-*.md` and `35-*.md`; public-process has 35 _posts/ files — verify alignment
  - Action: Confirm deployment or execute standard essay workflow
  - Finding: W5-II

- [ ] **E5.** Write "Construction Addiction" essay
  - The meta-narrative of a system that diagnosed its own compulsive building and then must overcome it
  - This converts the SP2-II shatter point into a narrative strength
  - Target: Essay #36 for bi-weekly cadence
  - Finding: SP2-II, BL3-II

---

## P2 — MEDIUM (System Quality, Next 5 Sprints)

- [ ] **M1-II.** Recruit and run first stranger test
  - Protocol at `docs/operations/stranger-test-protocol.md`
  - Target: 1 participant, 5 tasks, scoring rubric
  - Omega criteria advanced: #2, #4, #16
  - Recommended sprint: 30 PEREGRINUS
  - Finding: BS2-II

- [ ] **M2-II.** Add payment integration to life-my--midst--in
  - Stack: Stripe (mock fallback already in codebase)
  - Action: Connect real Stripe test keys, verify checkout flow
  - Omega criteria advanced: #9 (revenue_status: live), #10 (MRR)
  - Recommended sprint: 31 MERCATURA
  - Finding: LO3-II

- [ ] **M3-II.** Refresh portfolio with post-construction evidence
  - Update 4444j99.github.io/portfolio/ with: life-my--midst--in as live product, 28 sprints, 35 essays, omega scorecard
  - Omega criteria advanced: #15
  - Recommended sprint: 32 RENOVATIO
  - Finding: ET2-II

- [ ] **M4-II.** Improve seed.yaml coverage from 44% to 60%+
  - Current: 38/86 repos, Organs V/VI/VII at 0%
  - Priority: Organ V (public-process), Organ VI (4 repos), Organ VII (4 repos) — 10 repos
  - Finding: Concordia sprint deferred item
  - Recommended sprint: Catalog item 58 INSTRUMENTUM or new sprint

- [ ] **M5-II.** Set up monitoring/alerting for life-my--midst--in
  - Sentry error tracking, basic uptime monitoring
  - Required before claiming "product live" credibly
  - Finding: Sprint 27 deferred item

- [ ] **M6-II.** CI restructure (carried from E2G-I M4, still P3→P2)
  - Current state: `continue-on-error: true` on lint/mypy, silent pass on no tests
  - Option: make CI fail when no tests exist, require explicit `skip_tests: true`
  - 17 disabled cron workflows remain disabled (Sprint 12 ILLUSTRATIO)
  - Finding: E2G-I M4, E2G-I ET3

---

## P3 — STRATEGIC (1+ Month)

- [ ] **S1-II.** Complete 30-day soak test and generate report
  - Clock started 2026-02-16; completes ~March 18, 2026
  - Action: Run `python3 scripts/soak-test-monitor.py report --days 30`
  - Omega criteria advanced: #1, #17
  - Finding: W4-II

- [ ] **S2-II.** Host first salon (ORGAN-VI community event)
  - Target: 1 small event with ≥2 external participants
  - Omega criteria advanced: #11 (partial — need 2 total)
  - Recommended sprint: 33 CONVIVIUM
  - Finding: Omega criteria #11

- [ ] **S3-II.** Create contribution pathway for external contributors
  - CONTRIBUTING.md templates, good-first-issue labels, onboarding documentation
  - Omega criteria advanced: #12 (external contributions)
  - Recommended sprint: Catalog item 47 HOSPITIUM
  - Finding: Omega criteria #12

- [ ] **S4-II.** Write 2 planned essays (from Sprint 23 PUBLICATIO backlog)
  - "constraint-alchemy-workshop" (planned for Wed Mar 4, 2026)
  - "performance-platform-methodology" (planned for Wed Mar 18, 2026)
  - Maintain bi-weekly essay cadence
  - Finding: Sprint 23 deferred item

- [ ] **S5-II.** Investigate universal-mail--automation as second product candidate
  - Sprint 25 INSPECTIO recommended INVESTIGATE status
  - Assess for second beta product after life-my--midst--in
  - Finding: Sprint 25 deferred item

- [ ] **S6-II.** Pursue conference talk or workshop proposal
  - AI-conductor methodology as standalone talk
  - Target venues: Strange Loop, XOXO, Processing Community Day
  - Omega criteria advanced: #14 (recognition event)
  - Finding: E2G-I S4

---

## Cross-Reference: Finding → Action Item

| Finding | Code | Action Items |
|---------|------|-------------|
| Zero external contact | W1-II | X1, X2, X3, X4 |
| Construction addiction unbroken | W2-II, SP2-II | E5 (essay converts to narrative strength) |
| Operational cadence stale | W3-II | E1 |
| Soak test nominal only | W4-II | E2, S1-II |
| Essay drafts not deployed | W5-II | E4 |
| Application materials expiring | W6-II | X1, X3, E3 |
| Building in public but sealed | LC1-II | X4 (social media) |
| Construction addiction self-diagnosed | LC2-II | E5 |
| Ready but not submitted | LC3-II | X1, X3 |
| Beta-ready not deployed | LC4-II | X2 |
| Hermetic seal shatter point | SP1-II | X1, X2, X3, X4 (all P0) |
| Day-count acceleration | SP3-II | All P0 items (urgency) |
| Beta product decay risk | SP4-II | X2, M5-II |
| Self-assessment selection bias | BS2-II | M1-II (stranger test) |
| No social media presence | BS5-II | X4 |
| Omega scorecard as portfolio piece | BL1-II | M3-II (portfolio refresh) |
| Construction addiction essay value | BL3-II | E5 |

---

## E2G-I Action Items: Current Status

All E2G-I items referenced below for completeness:

| Item | E2G-I Priority | Status at E2G-II |
|------|---------------|------------------|
| Q1 (TODOs in apps) | P0 | **RESOLVED** — 0 TODOs remain |
| Q2 (revenue: active) | P0 | **RESOLVED** — split to revenue_model + revenue_status |
| Q3 (future-dated essays) | P0 | **RESOLVED** — all corrected |
| Q4 (portfolio URL) | P1 | **RESOLVED** |
| Q5 (jargon in apps) | P1 | **RESOLVED** |
| M1 (PRODUCTION→ACTIVE) | P2 | **RESOLVED** — 0 PRODUCTION in registry |
| M2 (vivify flagships) | P2 | **SUPERSEDED** — measurement error corrected |
| M3 (revenue_status field) | P2 | **RESOLVED** |
| M4 (CI restructure) | P2→P3 | **OPEN** — carried as M6-II |
| M5 (honesty essay) | P1 | **RESOLVED** — deployed |
| M6 (audience variants) | P2 | **RESOLVED** — 3 tracks, 9 bundles |
| S1 (30-day soak test) | P3 | **IN PROGRESS** — 1 day of 30, dry-run mode |
| S2 (stranger test) | P3 | **OPEN** — protocol ready, 0 conducted |
| S3 (submit application) | P3 | **OPEN** — 0 submitted, 9 ready |
| S4 (AI-conductor essay) | P3 | **RESOLVED** — deployed 2026-02-11 |
| S5 (engagement baseline) | P3 | **OPEN** — 0 engagement data |
| S6 (runbooks) | P3 | **RESOLVED** — 3 runbooks written |

**Summary: 11 RESOLVED, 1 SUPERSEDED, 4 OPEN (carried forward), 1 IN PROGRESS**

---

## Priority Action Sequence

The recommended execution order:

```
Day 1: X1 (submit Creative Lab Five) + X4 (first social post)
Day 1: X2 (deploy life-my--midst--in)
Day 2: X3 (submit 2 job apps)
Day 3: E1 (refresh operational cadence) — this sprint
Day 3: E2 (enable real soak test monitoring)
Week 2: E3 (submit Google Creative Fellowship)
Week 2: E5 (write "Construction Addiction" essay)
Week 3: M1-II (stranger test)
Week 4: M2-II (payment integration)
Month 2: S1-II (30-day soak report), S2-II (first salon)
```

**Non-negotiable rule:** No new named internal sprints until X1-X4 are complete.
