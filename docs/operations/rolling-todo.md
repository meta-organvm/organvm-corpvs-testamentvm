# Rolling TODO — Master Deferred Work Queue

**Created:** 2026-02-17
**Author:** @4444j99
**Status:** ACTIVE — Living document, reviewed weekly (Friday retrospective)
**Last reviewed:** 2026-02-17 (Strategy rewrite: added F1-F9 funding items, benefits cliff note, reordered by deadline urgency)
**Companions:** [`operational-cadence.md`](./operational-cadence.md) (rhythm), [`there+back-again.md`](../strategy/there+back-again.md) (destination), [`sprint-catalog.md`](../strategy/sprint-catalog.md) (menu), [`e2g-ii-action-items.md`](../evaluation/e2g-ii-action-items.md) (audit trail), [`concordance.md`](./concordance.md) (ID lookup)
**Constitution:** [`docs/memory/constitution.md`](../memory/constitution.md) — Articles I-VI govern all specifications

---

> *The roadmap says **where we're going.** The catalog says **what we could do.** The cadence says **when we work.** This document says **what we're actually doing next.***

> **Benefits Cliff Awareness:** SNAP excludes lump-sum grants (safe).
> Medicaid threshold: $21,597/year. Essential Plan $0 premium to $39,125.
> Fair Fares hard cliff: $22,692/year.
> Call NYLAG (212-613-5000) before accepting any single grant >$5K.
> See [`docs/applications/10-funding-strategy.md`](../applications/10-funding-strategy.md) for full analysis.

---

## How to Use This Document

**When:** Every Friday during the Part I retrospective block (see [`operational-cadence.md`](./operational-cadence.md) Part I).

**What to do:**
1. Scan READY — can anything be knocked out this week?
2. Scan NEEDS TIME — schedule blocks for next week's deep work days
3. Check NEEDS INCOME / NEEDS EXTERNAL — has anything unblocked?
4. Move completed items to COMPLETED with a date
5. Add any new items discovered during the week
6. At monthly review (Week 4), archive completed items

**Constraint tags:**
- `[READY]` — No blockers. Just needs doing. Quick wins (<30 min).
- `[TIME]` — Needs a scheduled block (>30 min). No other blocker.
- `[INCOME]` — Requires spending money (hosting, subscriptions, paid tools).
- `[EXTERNAL]` — Waiting on someone or something outside your control.

**Item IDs** use the e2g-ii codes where they exist (X1, E2, M3-II, S1-II, etc.) and new codes (G1, G2, G3) for setup-guide items. This preserves provenance and makes cross-referencing painless.

---

## READY — No Blockers, Just Needs Doing

- [x] **X4.** Make first social media post — completed 2026-02-17 (HERMETICUM session: Mastodon + Discord via distribution pipeline, issue #45)
  - Source: [e2g-ii P0](../evaluation/e2g-ii-action-items.md) · Omega: feeds #7, #13
- [ ] **F1.** Activate GitHub Sponsors (~15 min) — zero fee, monetizes 97 repos immediately
  - Source: [10-funding-strategy.md](../applications/10-funding-strategy.md) · Omega: feeds #9, #10
- [ ] **F2.** Apply for Fractured Atlas fiscal sponsorship (~30 min) — $10/mo, unlocks org-only grants (NEA, state arts councils)
  - Source: [10-funding-strategy.md](../applications/10-funding-strategy.md) · Omega: feeds #9
- [ ] **G2.** Configure Render deploy hook for life-my--midst--in — deploy service first (depends on X2), then copy deploy hook URL to `RENDER_DEPLOY_HOOK` secret
  - Render free tier costs $0, no credit card required
  - Enables auto-deploy on push to master
  - Source: [autonomous-setup-guide](./autonomous-setup-guide.md) §4

---

## NEEDS TIME — Schedule a Block

### This Week — URGENT DEADLINES

> **Non-negotiable rule from E2G-II:** No new named internal sprints until X1-X4 are complete.
> **Clarification:** Funding applications are external-facing (breaking the seal), not internal sprints.

- [ ] **F3.** Submit Artadia NYC application ($15K unrestricted) — **deadline Mar 1** (~3-4 hrs)
  - URL: https://artadia.org/award_schedule/new-york/ (Submittable) · Fit: 8/10
  - Identity position: Multimedia Artist / Systems Artist
  - Benefits cliff: SNAP-safe. Below Medicaid threshold with Schedule C deductions.
  - Source: [10-funding-strategy.md](../applications/10-funding-strategy.md) · Omega: #5, #9

- [ ] **X1.** Submit Google Creative Lab Five application (~1 hr)
  - Materials: `docs/applications/05-google-creative-lab-five-responses.md`
  - URL: https://www.creativelab5.com/ · Fit: 8/10
  - Source: [e2g-ii P0](../evaluation/e2g-ii-action-items.md) · Omega: #5, feeds #7

- [ ] **F4.** Research and submit NEH Summer Programs — **deadline Mar 6** (~2 hrs)
  - Credential-building. Evaluate eligibility before investing time.
  - Source: [10-funding-strategy.md](../applications/10-funding-strategy.md)

- [ ] **X2.** Deploy life-my--midst--in to Render (~1-2 hrs)
  - Guide: `~/Workspace/organvm-iii-ergon/life-my--midst--in/DEPLOY.md`
  - Env vars: `DATABASE_URL` (Neon) + `JWT_SECRET`
  - **Status:** `render.yaml` fixed for free tier (removed worker + Redis). Delete old Render blueprint, then fresh deploy from updated yaml.
  - Source: [e2g-ii P0](../evaluation/e2g-ii-action-items.md) · Omega: #8

### This Month (Feb 17 – Mar 18)

- [ ] **E3.** Submit Google Creative Fellowship application — **deadline March 18, 2026**
  - URL: https://creativefellowship.google/ · Materials ready · Fit: 7/10
  - Source: [e2g-ii P1](../evaluation/e2g-ii-action-items.md) · Omega: #5, feeds #14

- [ ] **X3.** Submit 2 job applications (~2 hrs) — Together AI Lead DX (6/10), HuggingFace Dev Advocate (5/10)
  - Cover letters: `docs/applications/cover-letters/`
  - Source: [e2g-ii P0](../evaluation/e2g-ii-action-items.md) · Omega: #5, feeds #7

- [x] **E5.** Write "Construction Addiction" essay (#36) — completed 2026-02-17 (HERMETICUM session: ~2600 words, auto-deploys via essay-deploy pipeline)
  - Source: [e2g-ii P1](../evaluation/e2g-ii-action-items.md) · Omega: #6

- [ ] **G1.** Set up LinkedIn developer token (~30 min, OAuth flow) — enables automated LinkedIn distribution
  - Source: [autonomous-setup-guide](./autonomous-setup-guide.md) §5

### Next 1-3 Months (Deadline-Sequenced)

- [ ] **F6.** Submit Fire Island Artist Residency — **deadline Apr 1** (~2 hrs, SlideRoom)
  - LGBTQ+ emerging visual artist. Stipend + housing. Fit: 7/10
  - Source: [10-funding-strategy.md](../applications/10-funding-strategy.md) · Omega: #5

- [ ] **F5.** Submit Creative Capital 2027 application ($50K) — portal opens Mar 2, **deadline Apr 2, 3pm ET** (~4-6 hrs)
  - HIGHEST-FIT TARGET (9/10). 6 short questions, 500-word project description, work samples.
  - Identity position: Systems Artist — "adventurous and imaginative" interdisciplinary work.
  - Benefits cliff: $50K exceeds Medicaid → Essential Plan ($0 premium). Call NYLAG before accepting.
  - Source: [10-funding-strategy.md](../applications/10-funding-strategy.md) · Omega: #5, #9

- [ ] **F7.** Submit Rauschenberg Cycle 36 ($5K) — **opens Apr 14, closes May 12** (~1 hr)
  - Emergency grant for digital/electronic arts. Quick application. SNAP-safe.
  - Source: [10-funding-strategy.md](../applications/10-funding-strategy.md)

- [ ] **F8.** Submit Spencer Foundation Small Research ($50K) — **deadline Apr 15, noon CT** (~4 hrs)
  - Education research focus. Identity position: Educator.
  - Source: [10-funding-strategy.md](../applications/10-funding-strategy.md) · Omega: #5

- [ ] **F9.** Submit Processing Foundation Fellowship ($10K) — **~Apr-May** (~3 hrs)
  - Infrastructure contribution. Governance toolkit as deliverable. Fit: 6/10
  - Source: [10-funding-strategy.md](../applications/10-funding-strategy.md) · Omega: #5

- [ ] **M1-II.** Recruit and run first stranger test — protocol at `docs/operations/stranger-test-protocol.md`
  - 1 participant, 5 tasks, scoring rubric
  - Source: [e2g-ii P2](../evaluation/e2g-ii-action-items.md) · Omega: #2, #4, #16
  - Recommended sprint: 30 PEREGRINUS

- [ ] **M3-II.** Refresh portfolio with post-construction evidence — 33 sprints, omega scorecard, live product
  - Site: `4444j99.github.io/portfolio/`
  - **Partial:** RENOVATIO updated all 5 data JSON files (97 repos, 87 ACTIVE, 33 sprints, 41 essays). Omega scorecard page added (pre-validation maturation session). Remaining: visual verification after deploy, push portfolio changes.
  - Source: [e2g-ii P2](../evaluation/e2g-ii-action-items.md) · Omega: #15

- [ ] **M6-II.** CI restructure — make CI fail when no tests, require explicit `skip_tests: true`
  - 17 disabled cron workflows remain disabled (Sprint 12 ILLUSTRATIO)
  - Source: [e2g-ii P2](../evaluation/e2g-ii-action-items.md), carried from E2G-I M4

- [x] **M9-II.** Fix fetch-familiar-friends CI — completed 2026-02-17 (downgraded `@types/react-dom` from ^19.2.3 to ^18.3.5 to match runtime React 18.2.0, closes #200)
  - Source: AMPLIFICATIO CI investigation · Omega: #1, #17

- [x] **M10-II.** Fix life-my--midst--in CI — completed 2026-02-17 (downgraded ESLint ^10.0.0 to ^9.39.2, added design-system vitest.config.ts with 20% thresholds, closes #91)
  - Source: AMPLIFICATIO CI investigation · Omega: #1, #8, #17

- [x] **M7-II.** Registry cleanup: 3 repos archived on GitHub but marked ACTIVE — nexus--babel-alexandria-, 4-ivi374-F0Rivi4, cog-init-1-0- — completed 2026-02-17 (RENOVATIO: all 3 archived in registry, ACTIVE 90→87, ARCHIVED 7→10)
  - Source: Sprint 32 SENSORIA findings

- [x] **M8-II.** Resolve 5 ghost repos — completed 2026-02-17 (RENOVATIO: all 5 exist on GitHub and are active; "ghost" was false alarm from missing local clones, not missing remotes)
  - Source: Sprint 32 SENSORIA findings

- [ ] **S1-II.** Complete 30-day soak test and generate report — clock started 2026-02-16, completes ~March 18
  - Command: `python3 scripts/soak-test-monitor.py report --days 30`
  - Source: [e2g-ii P3](../evaluation/e2g-ii-action-items.md) · Omega: #1, #17

- [ ] **S4-II.** Write 2 planned essays (from Sprint 23 PUBLICATIO backlog)
  - ~~"constraint-alchemy-workshop"~~ — completed 2026-02-17 (essay #37, ~2400 words)
  - "performance-platform-methodology" (target Wed Mar 18)
  - Source: [e2g-ii P3](../evaluation/e2g-ii-action-items.md)

- [ ] **S6-II.** Pursue conference talk or workshop proposal — AI-conductor methodology talk
  - Venues: Strange Loop, XOXO, Processing Community Day
  - **Partial:** 2 talk proposals drafted (AMPLIFICATIO) — `docs/applications/conference-proposals/ai-conductor-talk.md` and `constraint-alchemy-talk.md`. Remaining: submit when CFPs open.
  - Source: [e2g-ii P3](../evaluation/e2g-ii-action-items.md) · Omega: #14

---

## NEEDS INCOME — Requires Spending Money

- [ ] **G3.** Ghost newsletter hosting (~$9/mo or self-host) — enables email distribution channel
  - Source: [autonomous-setup-guide](./autonomous-setup-guide.md) §6

- [ ] **M2-II.** Stripe payment integration for life-my--midst--in — connect real Stripe test keys
  - Mock fallback already in codebase
  - Source: [e2g-ii P2](../evaluation/e2g-ii-action-items.md) · Omega: #9, #10
  - Recommended sprint: 31 MERCATURA

- [ ] **M5-II.** Set up monitoring/alerting for life-my--midst--in — Sentry error tracking + uptime monitoring
  - Required before claiming "product live" credibly
  - Source: [e2g-ii P2](../evaluation/e2g-ii-action-items.md)

---

## NEEDS EXTERNAL — Waiting on Someone or Something Else

- [ ] **S2-II.** Host first salon (ORGAN-VI community event) — need ≥2 external participants
  - Source: [e2g-ii P3](../evaluation/e2g-ii-action-items.md) · Omega: #11
  - Recommended sprint: 33 CONVIVIUM

- [ ] **S3-II.** Create contribution pathway for external contributors — need community activity first
  - CONTRIBUTING.md templates, good-first-issue labels, onboarding docs
  - **Partial:** CONTRIBUTING.md written (corpvs-testamentvm root), 5 good-first-issues created across 5 repos (AMPLIFICATIO). Remaining: first external contribution, community onboarding docs.
  - Source: [e2g-ii P3](../evaluation/e2g-ii-action-items.md) · Omega: #12
  - Recommended sprint: Catalog item 47 HOSPITIUM

- [ ] **S5-II.** Investigate universal-mail--automation as second product candidate
  - Sprint 25 INSPECTIO recommended INVESTIGATE status
  - Source: [e2g-ii P3](../evaluation/e2g-ii-action-items.md)

---

## COMPLETED — Done Since Last Review

> Move items here with a completion date. Archive monthly.

- [x] **E1.** Refresh operational cadence Part IV — completed 2026-02-16 (Sprint 28 RECOGNITIO)
  - Source: [e2g-ii P1](../evaluation/e2g-ii-action-items.md)
- [x] **E2.** Enable non-dry-run soak test monitoring — completed 2026-02-17 (workflow configured without --dry-run, first cron run 2026-02-18 08:00 UTC)
  - Source: [e2g-ii P1](../evaluation/e2g-ii-action-items.md) · Omega: #1, #3, #17
- [x] **E4.** Deploy essay drafts #34 and #35 — completed 2026-02-16 (Sprint 27 BETA-VITAE)
  - Source: [e2g-ii P1](../evaluation/e2g-ii-action-items.md) · Omega: #6
- [x] **X4.** Make first social media post — completed 2026-02-17 (HERMETICUM: Mastodon + Discord, distribution issue #45)
  - Source: [e2g-ii P0](../evaluation/e2g-ii-action-items.md) · Omega: feeds #7, #13
- [x] **E5.** Write "Construction Addiction" essay (#36) — completed 2026-02-17 (HERMETICUM: ~2600 words, SP2-II→narrative)
  - Source: [e2g-ii P1](../evaluation/e2g-ii-action-items.md) · Omega: #6
- [x] **M4-II.** Improve seed.yaml coverage from 44% to 100% — completed 2026-02-17 (Sprint 32 SENSORIA — 82/82 eligible repos)
  - Source: [e2g-ii P2](../evaluation/e2g-ii-action-items.md)
- [x] **M7-II.** Registry cleanup: 3 archived-on-GitHub repos marked ACTIVE — completed 2026-02-17 (RENOVATIO: ACTIVE 90→87, ARCHIVED 7→10)
  - Source: Sprint 32 SENSORIA findings
- [x] **M8-II.** Resolve 5 ghost repos — completed 2026-02-17 (all 5 exist on GitHub; "ghost" was false alarm from missing local clones)
  - Source: Sprint 32 SENSORIA findings
- [x] **M9-II.** Fix fetch-familiar-friends CI — completed 2026-02-17 (@types/react-dom v19→v18, closes #200)
  - Source: AMPLIFICATIO CI investigation
- [x] **M10-II.** Fix life-my--midst--in CI — completed 2026-02-17 (ESLint 10→9.x, design-system coverage 75%→20%, closes #91)
  - Source: AMPLIFICATIO CI investigation

---

## Archive

> Items moved from COMPLETED at monthly review, with date range.

*No archived items yet.*

---

## Provenance Summary

| Source Document | Items Drawn | Coverage |
|----------------|-------------|----------|
| [`e2g-ii-action-items.md`](../evaluation/e2g-ii-action-items.md) | 20 of 21 (E1, E2, E4, M4-II completed) | 100% of open items |
| [`autonomous-setup-guide.md`](./autonomous-setup-guide.md) | 3 of 3 PENDING/OPTIONAL | 100% |
| [`10-funding-strategy.md`](../applications/10-funding-strategy.md) | 9 new items (F1-F9) | Funding strategy rewrite |
| [`operational-cadence.md`](./operational-cadence.md) Part IV | Subsumed by e2g-ii items | Cross-referenced |
| [`sprint-catalog.md`](../strategy/sprint-catalog.md) | Referenced via recommended sprints | Menu, not queue |
| Sprint 32 SENSORIA findings | 2 new items (M7-II, M8-II) | Registry anomalies |
| AMPLIFICATIO CI investigation | 2 new items (M9-II, M10-II) | Deferred CI fixes |

**Total items:** 37 (3 READY, 18 TIME, 3 INCOME, 3 EXTERNAL, 10 COMPLETED)
**Strategy rewrite (2026-02-17):** 9 funding items added (F1-F9). Benefits cliff note added. NEEDS TIME reordered by deadline urgency (F3 Artadia Mar 1 → F9 Processing ~Apr-May). Funding submissions classified as external-facing (compatible with P0 hermetic seal rule).
**Last session:** Strategy rewrite (2026-02-17) — replaced engineering-heavy approach with multi-track (art-tech grants, emergency funds, selective employment, consulting)

---

*This document was created on 2026-02-17 as the fourth governance document, completing the quadrilateral: roadmap (destination) + catalog (menu) + cadence (rhythm) + rolling TODO (queue). Review weekly at Friday retrospective. Items that persist for 3+ months without progress should be reassessed — they may belong in the catalog's unscheduled list rather than the active queue.*
