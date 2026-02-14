# E2G Action Items — Prioritized

**Source:** `docs/evaluation/e2g-full-system-review.md`
**Generated:** 2026-02-13
**Sprint context:** Post-PRAXIS, pre-external submission

---

## Priority Legend

- **P0 (CRITICAL):** Must fix before any external submission. These are credibility-destroying if discovered.
- **P1 (HIGH):** Should fix within 1–2 days. These weaken claims but are survivable.
- **P2 (MEDIUM):** Fix within 1–2 weeks. These improve presentation and reduce risk.
- **P3 (STRATEGIC):** Plan and execute over 1+ month. These build long-term credibility.

---

## P0 — CRITICAL (Fix Before Submission)

- [ ] **Q1.** Fix TODO in all 5 application materials — replace `TODO — deploy portfolio site before submission` with actual portfolio URL (`https://4444j99.github.io/portfolio/`)
  - Files: `applications/knight-foundation.md:26`, `applications/eyebeam-residency.md:26`, `applications/google-creative.md:26`, `applications/processing-foundation.md:26`, `applications/ai-systems-role.md:27`
  - Finding: W5

- [ ] **Q2.** Change `revenue: active` to `revenue_model: [subscription|freemium|one-time]` for all ORGAN-III repos with zero actual revenue
  - File: `registry-v2.json` (9 entries with `"revenue": "active"`)
  - Finding: W3, LC4, SP3

- [ ] **Q3.** Redate 9 future-dated essays (2026-02-14 through 2026-02-22) to their actual creation date (2026-02-13)
  - Files: `system-metrics.json` essay timeline, public-process `_posts/` frontmatter
  - Finding: W4, SP2

## P1 — HIGH (Fix Within 1–2 Days)

- [ ] **Q4.** Add portfolio URL to application materials (in the Portfolio URL section and supporting materials)
  - Files: All 5 `applications/*.md`
  - Finding: W5

- [ ] **Q5.** Translate project-internal vocabulary in applications for external audiences
  - Replace "115 seed.yaml contract edges" with human-readable description
  - Replace "PRAXIS Sprint" references with accessible language
  - Define "AI-conductor methodology" on first use
  - Files: All 5 `applications/*.md`
  - Finding: PA4

- [ ] **M5.** Write an honest "How This Was Built" essay acknowledging AI role, compressed timeline, and current limitations
  - Target: `_posts/` in public-process
  - Finding: BS3, BS4, PA3

## P2 — MEDIUM (Fix Within 1–2 Weeks)

- [ ] **M1.** Rename `implementation_status: PRODUCTION` → `DOCUMENTED` across the entire system
  - Files: `registry-v2.json` (82 entries), `system-metrics.json`, all validation scripts, CLAUDE.md, application materials
  - Finding: LC3, SP1, ET2
  - Note: This is the single highest-impact vocabulary change. Discuss naming alternatives: `DOCUMENTED`, `MAINTAINED`, `ACTIVE`

- [ ] **M2.** Vivify top 4 non-SUBSTANTIAL flagships with real code and tests
  - `agentic-titan` (2 code files → working orchestration agent)
  - `public-process` (6 code files → search, navigation, build validation)
  - `auto-revision-epistemic-engine` (20 code files, 3 tests → expand test coverage)
  - `example-generative-music` (7 code files, 2 tests → working Web Audio demo)
  - Finding: W1, LC2

- [ ] **M3.** Add `revenue_status` field to ORGAN-III repo schema
  - Values: `pre-launch` | `beta` | `live`
  - Separates business model (what you plan to charge) from business state (whether anyone is paying)
  - File: `registry-v2.json`
  - Finding: W3, LC4

- [ ] **M4.** Restructure CI to distinguish "test suite passes" from "no tests found"
  - Option A: Fail CI on repos with no tests; require explicit `skip_tests: true`
  - Option B: Add CI tier labeling (FULL | LINT_ONLY | BUILD_ONLY)
  - Option C: Report CI coverage as "6 repos with test suites; 77 with linting/build"
  - Finding: W6, SP4, ET3

- [ ] **M6.** Create audience-specific application variants
  - Technical (AI labs): lead with registry, orchestration, CI, code substance
  - Humanities (grants): lead with essays, governance philosophy, naming etymology
  - Arts (residencies): lead with cross-domain integration, meta-system as artwork
  - Finding: ET4, PA4

## P3 — STRATEGIC (1+ Month)

- [ ] **S1.** Run the system for 30 days without intervention; document what breaks
  - Tests: autonomous workflow execution, CI stability, registry consistency
  - Deliverable: "30-Day Soak Test" report
  - Finding: LC5, SP5

- [ ] **S2.** Get one external person to navigate the system and document their experience
  - First external validation of the "Stranger Test" (Constitution Article V)
  - Deliverable: External usability report
  - Finding: BS1, BS2

- [ ] **S3.** Submit one actual application (Knight Foundation or Processing Foundation)
  - Converts portfolio asset into real-world feedback loop
  - Prerequisites: P0 items complete, M5 essay published
  - Finding: LO1

- [ ] **S4.** Publish AI-conductor methodology as standalone essay or talk proposal
  - Target venues: Strange Loop, XOXO, Processing Community Day, NeurIPS workshop
  - Exploits: BL3 (methodology has standalone value)
  - Finding: BL3

- [ ] **S5.** Establish 30-day engagement baseline
  - Metrics: GitHub stars, forks, page views (GitHub insights), essay reads (Jekyll analytics), RSS subscribers
  - Required for: credible "public process" claims
  - Finding: BS5

- [ ] **S6.** Write operational runbooks for a second operator
  - Document: minimum viable operation, key workflows, emergency procedures
  - Addresses: bus-factor critique for grant applications
  - Finding: SP5, ET1

---

## Cross-Reference: Finding → Action Item

| Finding | Code | Action Items |
|---------|------|-------------|
| Code substance gap | W1 | M2 |
| Promotion stagnation | W2 | (no direct action — natural over time) |
| Revenue claims | W3, LC4, SP3 | Q2, M3 |
| Essay dating | W4, SP2 | Q3 |
| Application TODOs | W5 | Q1, Q4 |
| CI hollow coverage | W6, SP4, ET3 | M4 |
| PRODUCTION semantics | LC3, SP1, ET2 | M1 |
| Documentation-before-deployment | LC1 | M5 (honest framing) |
| Single-operator risk | SP5, ET1 | S6 |
| No external validation | BS1, BS2 | S2 |
| No engagement data | BS5 | S5 |
| AI transparency | BS3, BS4 | M5 |
