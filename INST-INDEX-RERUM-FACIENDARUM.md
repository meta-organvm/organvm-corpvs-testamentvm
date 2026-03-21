# INST — Index Rerum Faciendarum

**Status:** ACTIVE
**Created:** 2026-03-20
**Authority:** META — System-wide governance instrument
**Purpose:** Universal hanging index of things to be done — the canonical gap between what the system IS and what it NEEDS TO BE.

> *Index Rerum Faciendarum* — after the classical scholarly apparatus: *Index Locorum* (places), *Index Nominum* (names), *Index Rerum* (things). The gerundive *faciendarum* transforms reference into obligation: not things that exist, but things that must be made to exist.

### The Four Indices

This document is the first of a four-part classical index apparatus for ORGANVM:

| Index | Latin | Purpose | Status |
|-------|-------|---------|--------|
| **Index Rerum Faciendarum** | *Things to be done* | Universal work registry — the gap between IS and NEEDS TO BE | **THIS DOCUMENT** |
| **Index Locorum** | *Index of places* | Canonical map of where everything lives — repos, directories, files, URLs, infrastructure endpoints, deployment targets | IRF-IDX-001 |
| **Index Nominum** | *Index of names* | Registry of all named entities — organs, repos, tools, agents, personas, regimes, orders, specifications, dissertations, people | IRF-IDX-002 |
| **Index Rerum** | *Index of things* | Ontological inventory of what exists — every artifact, its type, its state, its relationships, its provenance | IRF-IDX-003 |

Together, the four indices constitute a complete scholarly apparatus for the system: where things are (Locorum), what they're called (Nominum), what they are (Rerum), and what remains to be done (Rerum Faciendarum). The first three are reference instruments; this one is a governance instrument.

---

## How to Use This Document

This is a **living governance instrument**, not a snapshot. Every session that produces or discovers work items should update this index. The auditor (`vigiles_engine/auditor.py`) and the omega scorecard (`organvm omega status`) are the primary automated consumers.

**Update protocol:**
1. When a session closes, add completed items to `## Completed` with session ID and date.
2. When new work is discovered, add to the appropriate organ section with priority and source.
3. When work is blocked, move to `## Blocked` with blocking reason.
4. When work becomes irrelevant, move to `## Archived` with reason.

**Priority tiers:**
- **P0 — NOW**: Human-gated or zero-cost unblocking actions. Do today.
- **P1 — SOON**: Next-session work. Clear path, no blockers.
- **P2 — GROWTH**: Extends existing capability. No deadline pressure.
- **P3 — HORIZON**: Future work. Requires design or prerequisites.

---

## System-Wide

### Governance & Standards

| ID | Priority | Action | Owner | Source | Blocker |
|----|----------|--------|-------|--------|---------|
| IRF-SYS-001 | P1 | Consolidate universal standards into a single CONSTITUTION.md — naming conventions, required files, required processes, design standards | Agent | S14, Memory | None |
| IRF-SYS-002 | P2 | Deploy standard GitHub Actions workflow template across GRADUATED repos | Agent | Wants list | Need template designed first |
| IRF-SYS-003 | P2 | Seed.yaml coverage: 72/117 → 117/117 | Agent | CLAUDE.md | Incremental |
| IRF-SYS-004 | P1 | Descent Protocol remaining 22% — repos missing descriptions/topics on GitHub | Agent | S11 | None |
| IRF-SYS-005 | P2 | World Root Phase 2-4 — repo migration per `~/Workspace/Organizing-Local-Remote-Structure.md` | Human | Memory | Phase 1 audit complete, execution not started |
| IRF-SYS-006 | P1 | Audit global gitignore for remaining overly-broad patterns — `/.config` and `lib/` fixed, but other language-template patterns may still clash across 117 repos | Agent | S26 | None |
| IRF-SYS-007 | P2 | Deploy Dependabot auto-merge + grouping to remaining high-traffic repos (portfolio already has grouping; growth-auditor, ORGAN-I/II flagships need it) | Agent | S26 | Template now exists from S26 |
| IRF-SYS-008 | P2 | ESLint 9→10 migration — blocked on eslint-plugin-react support. Monitor `eslint-plugin-react` releases for v8+ with ESLint 10 compatibility | Agent | S26 | eslint-plugin-react@7.37.5 incompatible |
| IRF-SYS-009 | P1 | Gmail notification hygiene — create filter for `from:notifications@github.com subject:"chore(deps)"` to skip inbox, label `github/dependabot` | Human | S26 | None |

### Skills & Automation

| ID | Priority | Action | Owner | Source | Blocker |
|----|----------|--------|-------|--------|---------|
| IRF-SKL-001 | P2 | Map 142 skills to design-process phases for auto-triggering | Agent | Wants list | Needs phase taxonomy designed |
| IRF-SKL-002 | P2 | Implement hook-based triggering for "universal standards" tier skills | Agent | Wants list | Depends on IRF-SKL-001 |
| IRF-SKL-003 | P2 | Skills governance metadata enrichment — continue from S17 baseline | Agent | S17 | None |

### The Index Apparatus

| ID | Priority | Action | Owner | Source | Blocker |
|----|----------|--------|-------|--------|---------|
| IRF-IDX-001 | P1 | Build INST-INDEX-LOCORUM.md — canonical map of where everything lives: repos (117), directories, key files, URLs, infrastructure endpoints (Cloudflare, GitHub orgs, D1 databases), deployment targets, MCP servers | Agent | This session | Pattern: INST-INDEX-RERUM-FACIENDARUM.md |
| IRF-IDX-002 | P1 | Build INST-INDEX-NOMINUM.md — registry of all named entities: 8 organs, 117 repos, CLI tools (organvm, alchemia, ontologia), agent personas (Architect/QA Lead/Operator/Auditor), 22 regimes, 8 Watcher Orders, 18 SPECs, 64+ SOPs, 3 dissertations (D-001/D-002/D-003), 8 faculties, named protocols (Testament, Descent, Membrane, Styx), people (Chris, the Provost) | Agent | This session | Data exists across registry-v2.json, seed.yaml files, governance docs |
| IRF-IDX-003 | P1 | Build INST-INDEX-RERUM.md — ontological inventory of what exists: every artifact type (YAML spec, Python module, Markdown research, SVG visual, YAML regime, test file, dissertation chapter), its state (implemented/specified/planned), relationships (produces/consumes, depends-on, references), provenance (which session, which commit) | Agent | This session | Ontologia UID system exists for entity identity |

### Monitoring & Auditing

| ID | Priority | Action | Owner | Source | Blocker |
|----|----------|--------|-------|--------|---------|
| IRF-MON-001 | P2 | Deploy vigiles-aeternae watcher orders as scheduled monitoring agents (cron/Actions) | Agent | Wants list, S12 | Code exists, deployment config needed |
| IRF-MON-002 | P2 | Connect auditor findings to omega scorecard — watchers report on criteria health | Agent | Wants list | None |
| IRF-MON-003 | P3 | Continuous auditor mode — IRA running on schedule, not just on-demand | Agent | Wants list | Needs deployment infrastructure |

---

## META — Corpus (organvm-corpvs-testamentvm)

| ID | Priority | Action | Owner | Source | Blocker |
|----|----------|--------|-------|--------|---------|
| IRF-CRP-001 | P1 | Omega scorecard: advance from 4/17 toward next achievable criteria | Agent | S13 | None |
| IRF-CRP-002 | P2 | Registry-v2.json maintenance — keep in sync as repos evolve | Agent | S3-7 | Ongoing |
| IRF-CRP-003 | P2 | Testament Protocol — verify chain integrity after recent sessions | Agent | S7 | None |

---

## META — Praxis Perpetua (SGO)

### Research Corpus (COMPLETE)

All 7 research prompts from INQ-2026-004 are delivered:

| Prompt | Document | Lines | Session |
|--------|----------|-------|---------|
| 1 — Intellectual genealogy | `research/intellectual-genealogy/` | ~800 | S8 |
| 2 — Aesthetic movements | `research/aesthetic-movements/` | ~800 | S9 |
| 3 — Solo auteur to studio | `research/solo-auteur-to-studio/` | ~800 | S10 |
| 4 — Trash and church | `research/trash-and-church/` | ~800 | S16 |
| 5 — Radical authenticity | `research/radical-authenticity/` | 800 + 427 | S20 |
| 6 — Alchemy as structure | `research/alchemical-system-lifecycle/` | 801 | S21 |
| 7 — System as genre | `research/system-as-genre/` | 715 | S22 |

### Dissertations

| ID | Priority | Action | Owner | Source | Blocker |
|----|----------|--------|-------|--------|---------|
| IRF-SGO-001 | P1 | D-003 spec review: work through GitHub issues #17-#24 (8 issues) | Agent | S18 | None |
| IRF-SGO-002 | P2 | Write first dissertation chapter — convert research corpus into D-003 Ch 1 | Agent | S4, S8-22 | 170K+ words of research available |
| IRF-SGO-003 | P2 | D-001 needs: 3+ months v2 outcome data, retrospective comparison, MPI test | Human | inquiry-log.yaml | Time-gated (need outcome data) |
| IRF-SGO-004 | P2 | D-002 needs: second instantiation, human baseline, expanded panel, longitudinal data | Agent+Human | inquiry-log.yaml | Partially time-gated |
| ~~IRF-SGO-005~~ | ~~P2~~ | ~~Add governance YAMLs to praxis-perpetua~~ — **DONE** (charter, defense-protocol, faculty-registry, senate-config all on disk + 4 new governance declarations 2026-03-21) | Agent | Memory | Completed S25 |
| IRF-SGO-006 | P3 | Build defense.py, publish.py, senate.py — SGO defense orchestration scripts | Agent | SGO spec | Depends on IRA code maturity |

### SGO Infrastructure (EXISTS)

Verified on disk 2026-03-20:
- `governance/charter.yaml` — constitutional document
- `governance/defense-protocol.yaml` — formal defense rules
- `governance/faculty-registry.yaml` — faculty definitions + rubrics
- `governance/senate-config.yaml` — panel composition rules
- `commissions/inquiry-log.yaml` — active research commissions
- `defenses/records/` + `defenses/transcripts/` — ready for use
- `publications/arxiv/` + `publications/journal/` + `publications/distilled/` — publication pipeline directories

---

## META — Vigiles Aeternae (IMPLEMENTED)

Verified on disk 2026-03-20 — full Python package:

**Source:** `src/vigiles_engine/` — 10 modules:
`auditor.py`, `orders.py`, `regime.py`, `consensus.py`, `divergence.py`, `chronicle.py`, `phaethon.py`, `reporter.py`, `cli.py`, `__init__.py`

**Data:** 22 regime YAMLs in `regimes/`, 8 Watcher Order YAMLs in `orders/`

**Tests:** 8 test files (test_auditor, test_orders, test_regime, test_consensus, test_divergence, test_chronicle, test_phaethon, test_reporter)

| ID | Priority | Action | Owner | Source | Blocker |
|----|----------|--------|-------|--------|---------|
| IRF-VIG-001 | P2 | Deploy as scheduled monitoring (cron or GitHub Actions) | Agent | S12 | Deployment config needed |
| IRF-VIG-002 | P2 | Integrate audit reports with system-dashboard | Agent | S12 | None |

---

## META — Trivium / Dialectica Universalis (IMPLEMENTED)

Verified on disk 2026-03-20:

**Spec:** `specs/SPEC-018.md`, `SPEC-018--dialect-taxonomy.md`, `SPEC-018--risk-register.md`

**Engine:** `organvm-engine/src/organvm_engine/trivium/` — 10 source files:
`dialects.py`, `taxonomy.py`, `detector.py`, `translator.py`, `synthesis.py`, `sources.py`, `content.py`, `edges.py`, `kinship.py`, `__init__.py`

**Tests:** 13 test files in `organvm-engine/tests/test_trivium_*.py`

**Plan:** `.claude/plans/2026-03-20-trivium-dialectica-universalis.md`

| ID | Priority | Action | Owner | Source | Blocker |
|----|----------|--------|-------|--------|---------|
| IRF-TRV-001 | P2 | Verify all tests pass, integrate into CI | Agent | Wants list | None |
| IRF-TRV-002 | P3 | Testament integration — add `trivium` to MODULE_SOURCES with PHILOSOPHICAL modality | Agent | Plan file | None |

---

## META — Testament Protocol (IMPLEMENTED)

Verified on disk 2026-03-20:

**Engine:** `organvm-engine/src/organvm_engine/testament/` — `pipeline.py`, `sources.py`, `manifest.py`, `network.py`, `aesthetic.py`, `catalog.py` + 6 renderers (sonic, statistical, social, html, prose, svg)

**Artifacts:** 30+ per-repo SVGs in `testament/artifacts/repos/`, sonic params, social pulse, self-portrait

**Network:** `network-map.yaml` with 3 lenses

| ID | Priority | Action | Owner | Source | Blocker |
|----|----------|--------|-------|--------|---------|
| IRF-TST-001 | P2 | Verify chain integrity post-22-session burst | Agent | S7 | None |

---

## ORGAN-II — Object Lessons

| ID | Priority | Action | Owner | Source | Blocker |
|----|----------|--------|-------|--------|---------|
| IRF-OBJ-001 | P0 | `npx wrangler pages secret put COLLABORATOR_PASSWORD` | Human | S19 | None |
| IRF-OBJ-002 | P0 | Share `https://object-lessons.pages.dev` with Chris | Human | S19 | None |
| IRF-OBJ-003 | P1 | Replace YouTube ID placeholders for 4 V1 episodes | Human | S19 | Need to look up IDs |
| IRF-OBJ-004 | P1 | Acquire `objectlessons.film` domain, point to Cloudflare Pages | Human | S19 | Domain availability |
| IRF-OBJ-005 | P1 | Add film stills/thumbnails to `public/images/` | Human | S19 | Need source images |
| IRF-OBJ-006 | P2 | Expand film database 253 → 302+ (omitted Tier 3 films) | Agent | S19 | None |
| IRF-OBJ-007 | P2 | Connect GitHub repo to Cloudflare Pages for auto-deploy on push | Agent | S19 | None |

---

## ORGAN-IV — Skills (a-i--skills)

| ID | Priority | Action | Owner | Source | Blocker |
|----|----------|--------|-------|--------|---------|
| IRF-SKL-001 | P2 | Map 142 skills to design-process phases | Agent | Wants list | Phase taxonomy needed |
| IRF-SKL-002 | P2 | Auto-trigger universal standards skills on push | Agent | Wants list | Depends on IRF-SKL-001 |

---

## ORGAN-VII — Kerygma (Distribution)

| ID | Priority | Action | Owner | Source | Blocker |
|----|----------|--------|-------|--------|---------|
| IRF-KER-001 | P3 | Build POSSE syndication pipeline — auto-post changes to socials | Agent | Wants list | ORGAN-VII repos exist but no automation |
| IRF-KER-002 | P3 | Connect Testament events to social distribution | Agent | Wants list | Depends on IRF-KER-001 |

---

## PERSONAL — Portfolio

| ID | Priority | Action | Owner | Source | Blocker |
|----|----------|--------|-------|--------|---------|
| IRF-PRT-002 | P2 | Re-evaluate security allowlist (h3, fast-xml-parser) by 2026-04-03 — GitHub issue #66 | Human | S24 | Time-gated |

---

## PERSONAL — Application Pipeline

| ID | Priority | Action | Owner | Source | Blocker |
|----|----------|--------|-------|--------|---------|
| IRF-APP-001 | P2 | Collect 3+ months v2 outcome data for D-001 | Human | inquiry-log.yaml | Time-gated |

---

## Generative Visuals

| ID | Priority | Action | Owner | Source | Blocker |
|----|----------|--------|-------|--------|---------|
| IRF-GEN-001 | P2 | Design generative art pipeline reading `organ-aesthetic.yaml` → per-organ visual identity | Agent | Wants list | Needs design spec |
| IRF-GEN-002 | P2 | Extend OG image generator pattern (S19) to system-wide use | Agent | S19 | Pattern exists in object-lessons |
| IRF-GEN-003 | P3 | Per-repo visual signatures derived from code characteristics | Agent | Wants list | Needs algorithm design |

---

## IRA / Evaluative Authority

Verified on disk 2026-03-20:

**Code:** `application-pipeline/scripts/diagnose_ira.py` — pure-stdlib ICC, Cohen's kappa, Fleiss kappa with Landis & Koch bands.
**Tests:** `tests/test_diagnose_ira.py`, `tests/test_math_proofs.py`, `tests/test_standards.py`
**Supporting:** `scripts/generate_ratings.py`, `scripts/standards.py`

| ID | Priority | Action | Owner | Source | Blocker |
|----|----------|--------|-------|--------|---------|
| IRF-IRA-001 | P2 | Second instantiation: deploy authority against ORGAN-IV (Taxis) | Agent | inquiry-log.yaml | None |
| IRF-IRA-002 | P2 | Human baseline: 3 expert engineers rate the pipeline; compare ICC | Human | inquiry-log.yaml | Need human raters |
| IRF-IRA-003 | P3 | Expand panel to 7 raters across 3 providers | Agent | inquiry-log.yaml | Depends on IRF-IRA-001 |

---

## Session Triage Findings (This Session — 2026-03-20)

Items discovered during the 22-session triage and filesystem verification that don't fit existing sections:

### Cross-Organ Architecture

| ID | Priority | Action | Owner | Source | Blocker |
|----|----------|--------|-------|--------|---------|
| IRF-ARC-001 | P1 | Persist this session's 22-session ledger as a canonical session archive (not just conversation memory) | Agent | This session | None |
| IRF-ARC-002 | P2 | Build session-to-IRF pipeline — every session close should check for new IRF items | Agent | This session | Needs hook or SOP |
| IRF-ARC-003 | P2 | Cross-session dependency map — which sessions' outputs feed into which other sessions | Agent | This session (S4→S8-10, S16, S18, S20-22 chain identified) | None |
| IRF-ARC-004 | P2 | Resolve old org alias remotes — local repos may still reference ivviiviivvi, omni-dromenon-machina, labores-profani-crux | Agent | Memory | Need per-repo audit |
| IRF-ARC-005 | P2 | Unarchive blocked repos on GitHub — 8 repos across 3 orgs can't push (see Memory: Archived repos) | Human | Memory | Need GitHub settings access |
| IRF-ARC-006 | P2 | Protected branch repos — 5 repos need PR + review approval, can't direct-push | Human | Memory | GitHub branch protection rules |

### Blockchain & Provenance

| ID | Priority | Action | Owner | Source | Blocker |
|----|----------|--------|-------|--------|---------|
| IRF-BLK-001 | P3 | Evaluate: publish Testament hash-chain attestations to external blockchain (Ethereum/Solana) for public verifiability | Agent | Wants list | Design decision needed: local chain sufficient vs. external attestation |
| IRF-BLK-002 | P2 | Connect Testament events to change tracking — every commit, promotion, governance change gets a chain entry | Agent | Wants list | Testament engine exists, needs event wiring |

### Documentation Gaps Identified

| ID | Priority | Action | Owner | Source | Blocker |
|----|----------|--------|-------|--------|---------|
| IRF-DOC-001 | P2 | Document the Vigiles Aeternae Python API — no public documentation beyond code | Agent | Filesystem verification | None |
| IRF-DOC-002 | P2 | Document the Trivium engine API — 10 modules, no usage guide | Agent | Filesystem verification | None |
| IRF-DOC-003 | P2 | Document IRA diagnostic tooling — diagnose_ira.py usage, rubric format, ratings format | Agent | Filesystem verification | None |
| IRF-DOC-004 | P1 | Verify all Vigiles tests pass: `pytest tests/` in vigiles-aeternae repo | Agent | Filesystem verification (.pytest_cache exists, tests may have drifted) | None |
| IRF-DOC-005 | P1 | Verify all Trivium tests pass: `pytest organvm-engine/tests/test_trivium_*.py` | Agent | Filesystem verification (13 test files exist) | None |

### Verification Debts (from this session's corrections)

| ID | Priority | Action | Owner | Source | Blocker |
|----|----------|--------|-------|--------|---------|
| IRF-VER-001 | P1 | Run full test suite across all META repos: engine, vigiles, trivium, alchemia, ontologia, mcp-server, dashboard | Agent | This session (claimed "complete" without running tests) | None |
| IRF-VER-002 | P1 | Verify praxis-perpetua research directory paths match the ledger (some paths in session transcripts may differ from actual disk) | Agent | This session | None |
| IRF-VER-003 | P2 | Audit all 22 session commits for unpushed branches or stale feature branches | Agent | This session | None |

---

## SGO Research Programme — Implementation Manifest

**Source:** 12 SGO papers + 3 TRP reviews across 4 research phases (INQ-2026-004)
**Added:** 2026-03-20
**Total tasks:** 71 (3 DONE, 68 OPEN)
**Manifest location:** `~/Workspace/intake/research-adventures-2026-03/IMPLEMENTATION-MANIFEST.md`

These tasks represent every actionable design recommendation extracted from the SGO research programme. Each traces to specific paper sections via the source field. Categories: GOVERNANCE, MEASUREMENT, NAMING, ARCHITECTURE, TOOLING, PROCESS.

### P0 — Foundational (must precede other research programme work)

| ID | Priority | Action | Category | Effort | Source | Status | Dependencies |
|----|----------|--------|----------|--------|--------|--------|--------------|
| IRF-RES-001 | P0 | Make the Governance Trilemma choice explicit — document ORGANVM's implicit choice of Consistent + Measurable over Complete; create machine-readable registry of governance blind spots | GOVERNANCE | M | SYN-02 SS5.5 R1; TRP-SYN-02 POV-3 | DONE | None |
| IRF-RES-002 | P0 | Classify all governance rules as syntactic or semantic — audit every rule in governance-rules.json, seed.yaml schemas, and CI checks; maintain classification as machine-readable annotation | GOVERNANCE | M | RP-02 SS4.5 I1, SS5.2; SYN-02 SS4.1 | DONE | None |
| IRF-RES-003 | P0 | Define "readiness" construct independently of its operationalization — convene expert panel to define full domain of "repository readiness" independently of metrics that measure it | MEASUREMENT | M | RP-07 SS7 I1; SYN-02 SS4.4; SYN-04 SS4.1 | OPEN | None |
| IRF-RES-004 | P0 | Conduct factor analysis on the omega scorecard — perform EFA on all indicators across repo population; determine single vs. multiple latent factors | MEASUREMENT | L | RP-07 SS6.2, SS6.3; SYN-02 SS5.5 R2 | OPEN | IRF-RES-003 |
| IRF-RES-005 | P0 | Implement the naming convention validator (double-hyphen linter) — automated validator enforcing double-hyphen convention in CI as syntactic governance check | NAMING | M | RP-04 SS5.1 P6; SYN-03 SS6.4; RP-02 SS4.5 I2 | DONE | None |
| IRF-RES-006 | P0 | Build a controlled vocabulary registry for domain terms — machine-readable mapping of canonical terms to synonyms; validate new names against vocabulary in CI | NAMING | M | RP-04 SS5.1 P4; SYN-03 SS6.4 | OPEN | IRF-RES-005 |
| IRF-RES-007 | P0 | Make incompleteness visible in all governance verdicts — every automated verdict must include explicit scope statement listing unverified semantic properties | GOVERNANCE | M | RP-02 SS5.5; SYN-02 SS5.5 R1 | OPEN | IRF-RES-002 |
| IRF-RES-008 | P0 | Formalize the IRA panel protocol — strengthen IRA panel as Tarskian escape; provide explicit guidance on semantic properties that automated checks cannot assess | GOVERNANCE | M | RP-02 SS6.3; SYN-02 SS4.5, SS5.3, SS5.5 R5 | OPEN | IRF-RES-002 |
| IRF-RES-009 | P0 | Implement seed.yaml semantic accuracy tracking — maintain machine-readable registry of properties not covered by seed.yaml validation; track gap between declared and actual behavior | GOVERNANCE | L | RP-02 SS6.2, SS6.4; SYN-02 SS5.4 | OPEN | IRF-RES-002 |
| IRF-RES-010 | P0 | Separate self-maintenance from self-improvement in governance — build two distinct operational modes with architectural enforcement of the boundary | ARCHITECTURE | L | RP-02 SS5.7, SS6.4 | OPEN | IRF-RES-002, IRF-RES-008 |
| IRF-RES-011 | P0 | Establish the hybrid topology principle as architectural law — codify inter-organ hierarchical flow and intra-organ rhizomatic connectivity as compression/search principle | ARCHITECTURE | S | RP-03 SS6.1-6.4; SYN-02 SS4.2 | OPEN | None |
| IRF-RES-012 | P0 | Design governance artifacts as boundary objects — redesign seed.yaml, CLAUDE.md, and governance-rules.json as boundary objects accommodating human, machine, and AI interpretive communities | ARCHITECTURE | M | RP-05 SS4.3, SS7.1; SYN-02 SS4.3; SYN-03 SS5.1-5.3 | OPEN | None |
| IRF-RES-013 | P0 | Implement temporal staging for governance validation — ensure governance always validates previous state using current state, never current state using itself | GOVERNANCE | S | RP-02 SS5.1, SS6.1; SYN-02 SS4.1, SS5.2 | OPEN | None |
| IRF-RES-014 | P0 | Implement context-specific governance norms — differentiate thresholds by organ, programming language, and project type; use expert-determined context-specific norms | MEASUREMENT | L | RP-07 SS5.5, SS7 I4; SYN-02 SS5.5 R3; SYN-04 SS5.2 | OPEN | IRF-RES-003, IRF-RES-004 |

### P1 — Important (high-impact, clear value; after P0 foundations)

| ID | Priority | Action | Category | Effort | Source | Status | Dependencies |
|----|----------|--------|----------|--------|--------|--------|--------------|
| IRF-RES-015 | P1 | Implement IRT-based scoring for governance checks — fit 2PL IRT model to pass/fail data; weight checks by information content; assign to promotion levels by empirical difficulty | MEASUREMENT | L | RP-07 SS5.1-5.4, SS6.3; SYN-02 SS4.4 | OPEN | IRF-RES-004 |
| IRF-RES-016 | P1 | Implement Goodhart monitoring system — track correlation between governance metrics and external outcomes over time; implement periodic metric rotation; track IRT discrimination parameters | MEASUREMENT | L | RP-07 SS7 I7; SYN-02 SS5.4, SS5.5 R4; SYN-04 SS5.3 | OPEN | IRF-RES-015 |
| IRF-RES-017 | P1 | Report governance scores with confidence intervals — use CTT formula SEM = sigma_X * sqrt(1 - r_XX); acknowledge uncertainty near promotion thresholds | MEASUREMENT | M | RP-07 SS6.4, SS7; SYN-02 SS4.4 | OPEN | IRF-RES-004 |
| IRF-RES-018 | P1 | Build a Governance Trilemma Audit instrument — formal audit methodology to test actual behavior against declared trilemma position | GOVERNANCE | M | SYN-02 SS6; TRP-SYN-02 POV-1 E2 | OPEN | IRF-RES-001 |
| IRF-RES-019 | P1 | Create a Practitioner's Decision Matrix for trilemma positions — table mapping governance contexts to recommended trilemma positions with specific guidance | GOVERNANCE | S | TRP-SYN-02 POV-3; SYN-02 SS6 | OPEN | IRF-RES-001 |
| IRF-RES-020 | P1 | Implement OPP-based governance architecture — design explicit obligatory passage points at every critical juncture; document the OPP map | ARCHITECTURE | L | RP-05 SS7.3; SYN-02 SS4.3 | OPEN | IRF-RES-002 |
| IRF-RES-021 | P1 | Build the stigmergic infrastructure layer — invest in rich, persistent, searchable stigmergic substrates; extend registry and dashboard | TOOLING | L | RP-03 SS6.4 H5, SS7.2-7.3 | OPEN | IRF-RES-011 |
| IRF-RES-022 | P1 | Implement namespace governance proportional to scale — formalize who can create top-level names, rules for naming within each namespace, dispute resolution | NAMING | S | RP-04 SS5.1 P3, P6; SYN-03 SS6.5 | OPEN | IRF-RES-005, IRF-RES-006 |
| IRF-RES-023 | P1 | Track naming debt and implement naming health metrics — detect and track names that no longer accurately describe what they name; implement periodic naming audits | NAMING | M | RP-04 SS5.3; SYN-03 SS3.4, SS6.2 | OPEN | IRF-RES-005 |
| IRF-RES-024 | P1 | Formalize the distinction between designed and emergent hierarchy — monitor flat domains for hub-and-spoke emergence; track centrality distribution over time | ARCHITECTURE | M | RP-03 SS4.4; SYN-02 SS2.2 | OPEN | IRF-RES-011 |
| IRF-RES-025 | P1 | Build relational quality metrics (not just entity-level) — supplement entity-level metrics with network-level metrics for dependency health, test quality, documentation adequacy | MEASUREMENT | L | SYN-04 SS5.1 | OPEN | IRF-RES-004 |
| IRF-RES-026 | P1 | Record network configuration alongside every assessment score — accompany every governance score with tool versions, checks applied, dependency network state, development context | MEASUREMENT | M | SYN-04 SS5.2 | OPEN | IRF-RES-014 |
| IRF-RES-027 | P1 | Implement Guttman scale validation for the promotion pipeline — scalogram analysis, compute coefficient of reproducibility; identify hard/soft/structural violations | MEASUREMENT | M | RP-07 SS4.1, SS6.3; SYN-02 SS5.2 | OPEN | IRF-RES-004 |
| IRF-RES-028 | P1 | Implement criterion validation for governance scores — correlate with external outcomes; compute concurrent and predictive validity coefficients | MEASUREMENT | L | RP-07 SS4.4, SS6.3, SS7 I5 | OPEN | IRF-RES-015 |
| IRF-RES-029 | P1 | Adopt VSM recursive structure for organs — align each organ with Beer's five subsystems; map VSM subsystems to trilemma properties | ARCHITECTURE | L | SYN-02 SS4.6, SS5.5 R6; TRP-SYN-02 POV-1 | OPEN | IRF-RES-010, IRF-RES-011 |
| IRF-RES-030 | P1 | Design system prompts as enrollment contracts, not command lists — redesign CLAUDE.md files to define role, establish relationship, specify conditions of productive collaboration | PROCESS | M | RP-05 SS7.1 | OPEN | IRF-RES-012 |
| IRF-RES-031 | P1 | Implement mediator visibility in AI-generated outputs — transparent attribution, confidence/uncertainty indication, visible translation traces, challenge mechanisms | PROCESS | M | RP-05 SS7.2 | OPEN | None |
| IRF-RES-032 | P1 | Build governance-as-type-system framework — use Curry-Howard framing to classify governance rules by type-theoretic strength; map to Chomsky hierarchy | GOVERNANCE | L | RP-02 SS4.4, SS4.5 I5; RP-06 SS7.4 | OPEN | IRF-RES-002 |
| IRF-RES-033 | P1 | Implement over/under-approximation strategy per governance rule — for each semantic rule, explicitly choose conservative or liberal approximation direction; document error rate | GOVERNANCE | M | RP-02 SS4.3, SS5.4 | OPEN | IRF-RES-002 |
| IRF-RES-034 | P1 | Implement language-game specification for naming contexts — when designing naming conventions, specify where name appears, who reads it, what must be understood from name alone | NAMING | S | RP-04 SS5.1 P7 | OPEN | IRF-RES-005 |
| IRF-RES-035 | P1 | Design for translation drift in governance rules — monitor for excessive interpretation drift between human understanding and AI interpretation; build feedback loops | GOVERNANCE | M | SYN-02 SS4.3, SS5.5 R7; RP-05 SS7.1 | OPEN | IRF-RES-012 |
| IRF-RES-036 | P1 | Implement the four-phase design audit — for each organ, verify coverage across Naming, Structuring, Computing, and Reflecting phases; identify gaps | GOVERNANCE | M | CAPSTONE SS11.6 | OPEN | IRF-RES-001 |
| IRF-RES-037 | P1 | Build item analysis for governance checks — compute pass rate and point-biserial correlation for each check; remove or redesign non-discriminating checks | MEASUREMENT | M | RP-07 SS6.3 S1 | OPEN | IRF-RES-004 |
| IRF-RES-038 | P1 | Design assessment criteria for constitutive value, not just diagnostic value — optimize checks for encouraging desirable practices alongside distinguishing quality levels | MEASUREMENT | M | SYN-04 SS5.4 | OPEN | IRF-RES-003, IRF-RES-015 |
| IRF-RES-039 | P1 | Implement schema contracts as syntactic categories — treat seed.yaml contracts as formal syntactic category; implement schema validation as type-checking in Curry-Howard sense | TOOLING | L | SYN-01 SS6; CAPSTONE SS10.2 | OPEN | IRF-RES-009 |
| IRF-RES-040 | P1 | Implement external case study of the Governance Trilemma — apply framework to at least one governance system not designed by the author (Linux kernel, GDPR, Kubernetes) | PROCESS | M | TRP-SYN-02 A4 (all POVs) | OPEN | IRF-RES-001 |
| IRF-RES-041 | P1 | Calibrate formality claims in SYN-02 — replace "formal theorem" language with "structural argument"; engage with mechanism design as partial counterexamples; add Formalization Roadmap | PROCESS | M | TRP-SYN-02 A1, A2, A3 | OPEN | None |
| IRF-RES-042 | P1 | Address the small-N problem for psychometric calibration — develop simplified approaches for 117 repos: classical reliability, Bayesian methods, repeated measures over time | MEASUREMENT | M | TRP-SYN-02 POV-3 C3, A8 | OPEN | IRF-RES-004 |
| IRF-RES-043 | P1 | Implement panarchy-aware design for phase transitions — build structures that can transition between hierarchical and rhizomatic phases; innovation sandboxes, periodic reorganization | ARCHITECTURE | L | RP-03 SS4.5, SS6.4 H3 | OPEN | IRF-RES-011 |

### P2 — Enhancement (deepens theoretical alignment and operational sophistication)

| ID | Priority | Action | Category | Effort | Source | Status | Dependencies |
|----|----------|--------|----------|--------|--------|--------|--------------|
| IRF-RES-044 | P2 | Build adaptive governance assessment — IRT-enabled adaptive testing; evaluate repos with checks selected based on estimated quality level | MEASUREMENT | L | RP-07 SS7 I6 | OPEN | IRF-RES-015 |
| IRF-RES-045 | P2 | Implement measurement invariance testing across organs — multi-group CFA and DIF analysis across organs, languages, and project types | MEASUREMENT | XL | RP-07 SS5.5, SS6.3; SYN-02 SS5.5 R3 | OPEN | IRF-RES-015, IRF-RES-014 |
| IRF-RES-046 | P2 | Build a rhizomaticity index for organizational monitoring — implement R(G) function tracking clustering coefficient, path length, power-law exponent, centrality inequality, modularity | TOOLING | L | RP-03 SS2.4 | OPEN | IRF-RES-021 |
| IRF-RES-047 | P2 | Implement sense-preservation checks for aliases — when multiple names point to same referent, validate that naming system preserves sense distinctions | NAMING | S | RP-04 SS5.1 P2 | OPEN | IRF-RES-006 |
| IRF-RES-048 | P2 | Implement type-token naming discipline — enforce visual distinction between types and tokens, schemas and records, conventions and applications | NAMING | S | RP-04 SS5.1 P5 | OPEN | IRF-RES-005 |
| IRF-RES-049 | P2 | Build the dynamic trilemma navigation model — governance lifecycle model mapping expected trajectory of trilemma choices as system scales | GOVERNANCE | M | TRP-SYN-02 POV-1 E1 | OPEN | IRF-RES-018 |
| IRF-RES-050 | P2 | Map the inter-organ trilemma coordination problem — map how one organ's incompleteness interacts with another's inconsistency; identify failure modes at inter-organ interfaces | GOVERNANCE | M | TRP-SYN-02 POV-1 E3 | OPEN | IRF-RES-018 |
| IRF-RES-051 | P2 | Implement the Willard strategy for restricted self-verification — restrict governance expressiveness so it cannot construct self-referential rules | GOVERNANCE | L | RP-02 SS7 | OPEN | IRF-RES-010 |
| IRF-RES-052 | P2 | Implement abstract interpretation for semantic governance approximation — explicit soundness/completeness tradeoffs for undecidable governance rules | TOOLING | L | RP-02 SS4.3 | OPEN | IRF-RES-033 |
| IRF-RES-053 | P2 | Design strange loop stability analysis — identify all strange loops in governance architecture; characterize stability as convergent vs. divergent | GOVERNANCE | M | RP-02 SS5.6 | OPEN | IRF-RES-013 |
| IRF-RES-054 | P2 | Explore consequential validity monitoring — build feedback loops tracking downstream effects of assessment decisions on production outcomes | MEASUREMENT | L | SYN-04 SS5.3; RP-07 SS7 I7 | OPEN | IRF-RES-016 |
| IRF-RES-055 | P2 | Implement multi-level interpretation naming — ensure naming conventions provide shallow interpretability (novice) and deep interpretability (expert) | NAMING | S | SYN-03 SS6.3 | OPEN | IRF-RES-005 |
| IRF-RES-056 | P2 | Build the ontological commitment registry — maintain registry of every naming decision that constitutes an ontological commitment; review periodically | NAMING | S | RP-04 SS5.1 P1; SYN-03 SS5.4 | OPEN | IRF-RES-006 |
| IRF-RES-057 | P2 | Implement names-as-infrastructure breakdown detection — automated detection for reference failures, collisions, semantic drift, abstraction mismatches | NAMING | M | SYN-03 SS2.2, SS6.4 | OPEN | IRF-RES-005, IRF-RES-006 |
| IRF-RES-058 | P2 | Design for ontological pluralism in quality assessment — accept "quality" is constituted differently in different network configurations; produce quality profiles | MEASUREMENT | L | SYN-04 SS5.5 | OPEN | IRF-RES-014, IRF-RES-045 |
| IRF-RES-059 | P2 | Build a formalization roadmap for the Governance Trilemma — specify what fully formal version would require: formal definitions, conditions, proof | GOVERNANCE | M | TRP-SYN-02 A3 | OPEN | IRF-RES-041 |
| IRF-RES-060 | P2 | Build governance rule classification by Chomsky level — classify every rule as regular, context-free, context-sensitive, or unrestricted; map decidability implications | GOVERNANCE | M | RP-06 SS7.4; TRP-RP-06 POV-3 E4 | OPEN | IRF-RES-002, IRF-RES-032 |
| IRF-RES-061 | P2 | Implement alignment-as-translation framework for AI interactions — reframe AI alignment as ongoing network stabilization; classify misalignment types by translation-failure moment | PROCESS | M | RP-05 SS5.5; CAPSTONE SS12.5 | OPEN | IRF-RES-030 |
| IRF-RES-062 | P2 | Build the test information function for governance assessment — compute I(theta) across all governance checks; identify under-measured regions of quality continuum | MEASUREMENT | M | RP-07 SS5.4 | OPEN | IRF-RES-015 |
| IRF-RES-063 | P2 | Implement Dunbar-aware team sizing for organs — keep active participants below cognitive limit; design for future scaling with hierarchical compression thresholds | ARCHITECTURE | S | RP-03 SS4.1, SS6.4 H6 | OPEN | None |
| IRF-RES-064 | P2 | Implement SEM-based relational quality model — use structural equation modeling to specify quality as network of related constructs; test fit against observed data | MEASUREMENT | XL | SYN-04 SS5.1 | OPEN | IRF-RES-004, IRF-RES-015 |
| IRF-RES-065 | P2 | Scope-narrow the SYN-01 claims per TRP review — narrow to "the architecture of compositional formal meaning"; engage with philosophy of unification; provide honest DisCoCat assessment | PROCESS | M | TRP-SYN-01 Priorities 1-3 | OPEN | None |
| IRF-RES-066 | P2 | Address RP-06 Type 1 correspondence weakness — provide concrete worked example encoding {a^n b^n c^n} as System F typing problem, or acknowledge encoding is conjectural | PROCESS | M | TRP-RP-06 A2 | OPEN | None |
| IRF-RES-067 | P2 | Propose MCS type-theoretic conjecture — propose concrete conjecture for type-theoretic characterization of mildly context-sensitive languages; document as open problem | ARCHITECTURE | L | RP-06 SS2.5, SS6.2; TRP-RP-06 A6 | OPEN | None |
| IRF-RES-068 | P2 | Design assessment for constitutive rather than just detection value — accept CI checks are mediators that constitute quality; design checks whose constitutive effects encourage beneficial practices | MEASUREMENT | S | SYN-04 SS4.2-4.3, SS5.4 | OPEN | IRF-RES-038 |
| IRF-RES-069 | P2 | Implement names-stable-under-change principle — names should refer to what is stable (function/domain), not what is volatile (org-chart position); audit existing names | NAMING | S | SYN-03 SS6.2 | OPEN | IRF-RES-005 |
| IRF-RES-070 | P2 | Build the compression/search ratio monitoring tool — monitor ratio of hierarchical compression to rhizomatic search per domain; alert on mismatches | TOOLING | M | RP-03 SS3.3, SS6.4 H1 | OPEN | IRF-RES-046 |
| IRF-RES-071 | P2 | Build explicit typological coverage in RP-06 — expand linguistic examples to include polysynthetic, free word-order, and sign languages; acknowledge non-generativist frameworks | PROCESS | M | TRP-RP-06 A3, A4 | OPEN | None |

### Cross-Cutting Concerns (from SGO research programme)

These are not discrete tasks but organizing principles that cross-cut the entire programme:

| ID | Concern | Description | Scope |
|----|---------|-------------|-------|
| IRF-RES-CC1 | Syntactic/semantic boundary | All governance automation must respect the Rice boundary — every check is either syntactic (decidable) or semantic (undecidable, requiring human judgment) | All organs, CI, governance |
| IRF-RES-CC2 | Governance Trilemma universality | The trilemma applies at every level: system, organ, repo, and governance tool; each level makes its own choice; choices must be coordinated | META, ORGAN-IV, all organs |
| IRF-RES-CC3 | Naming as infrastructure | Every naming decision is an ontological commitment that shapes organizational topology; naming debt compounds; naming governance = API design rigor | All repos, conventions, docs |
| IRF-RES-CC4 | Measurement constitutes its object | CI checks, governance scores, and quality metrics constitute quality, not merely detect it; assessment design must optimize constitutive alongside diagnostic value | All CI, scoring, governance |
| IRF-RES-CC5 | Human-in-the-loop is structurally necessary | Human judgment at the semantic boundary responds to impossibility results (Godel, Tarski, Rice, Goodhart), not a stopgap; the human is the incompleteness response | IRA panel, promotion, AI design |

### Implementation Sequence (from manifest)

| Phase | Weeks | Focus | Key Tasks |
|-------|-------|-------|-----------|
| A: Foundations | 1-4 | Structural preconditions | IRF-RES-001(DONE), 002(DONE), 011, 013, 005(DONE), 006, 012, 007 |
| B: Measurement Foundations | 3-8 | Psychometric infrastructure | IRF-RES-003, 004, 014, 037, 027, 017 |
| C: Governance Hardening | 6-12 | Impossibility-aware governance | IRF-RES-008, 009, 010, 018, 019, 020, 032, 033 |
| D: Naming and Architecture | 8-14 | Naming infrastructure, org topology | IRF-RES-022, 023, 034, 024, 021, 029, 043 |
| E: Advanced Measurement | 12-20 | Psychometric calibration | IRF-RES-015, 042, 028, 016, 025, 026 |
| F: Research Revisions | 4-16 | Paper revisions per TRP reviews | IRF-RES-041, 040, 065, 066, 071 |
| G: Enhancements | 16+ | P2 tasks as capacity allows | IRF-RES-044, 046, 049, 054, 060 (prioritized) |

---

## Completed (from 22-session cataloguing, 2026-03-20)

| ID | What | Session | Date |
|----|------|---------|------|
| DONE-001 | Application pipeline v2 with clearance gates | S1-2 | 2026-03-20 |
| DONE-002 | Testament Protocol — hash-linked event chain with flock | S3, S5-7 | 2026-03-20 |
| DONE-003 | 7/7 research prompts delivered (170K+ words) | S8-10, S16, S20-22 | 2026-03-20 |
| DONE-004 | Descent Protocol 22%→78% | S11 | 2026-03-20 |
| DONE-005 | Vigiles Aeternae — 22 regimes, 8 orders, full Python engine | S12 | 2026-03-20 |
| DONE-006 | Omega scorecard amendment | S13 | 2026-03-20 |
| DONE-007 | Dotfiles/chezmoi/PAT fix/permissions | S14 | 2026-03-20 |
| DONE-008 | Portfolio — 496 tests, 0 vulns, CI/CD | S15 | 2026-03-20 |
| DONE-009 | Skills 105→142 with governance metadata | S17 | 2026-03-20 |
| DONE-010 | D-003 dissertation design spec | S18 | 2026-03-20 |
| DONE-011 | Object Lessons website — deployed to Cloudflare | S19 | 2026-03-20 |
| DONE-012 | Trivium / Dialectica — SPEC-018 + engine module + 13 tests | Prior sessions | Pre-2026-03-20 |
| DONE-013 | IRA diagnostic code — ICC/kappa/consensus computation | Prior sessions | Pre-2026-03-20 |
| DONE-014 | 22-session triage, cataloguing, and filesystem verification | This session (S23) | 2026-03-20 |
| DONE-015 | Index Rerum Faciendarum — universal work registry created | This session (S23) | 2026-03-20 |
| DONE-016 | Wants-vs-sessions tracking with corrected completion states | This session (S23) | 2026-03-20 |
| DONE-017 | SGO Research: Governance Trilemma Declaration (IRF-RES-001) | Research programme | 2026-03-20 |
| DONE-018 | SGO Research: Syntactic-Semantic Boundary Classification (IRF-RES-002) | Research programme | 2026-03-20 |
| DONE-019 | SGO Research: Naming Convention Spec (IRF-RES-005) | Research programme | 2026-03-20 |
| DONE-020 | Portfolio Lighthouse CI fix — programmatic API, 3-trigger system, security remediation (IRF-PRT-001) | S24 | 2026-03-21 |
| DONE-021 | SGO Research: Research Pipeline SOP | Research programme | 2026-03-21 |
| DONE-022 | SGO Research: Research Registry | Research programme | 2026-03-21 |
| DONE-023 | SGO Research: Session Retrospective | Research programme | 2026-03-21 |
| DONE-024 | praxis-perpetua CI remediation — fixed broken-link checker (SIGPIPE, cross-repo links, session artifacts), added permissions block, made link check informational | S25 | 2026-03-21 |
| DONE-025 | praxis-perpetua dependency bumps — actions/checkout v4→v6, actions/stale v9→v10, Dependabot PRs #14/#15 absorbed and closed | S25 | 2026-03-21 |
| DONE-026 | Security: redacted leaked Render API token from session logs (secret scanning alert #1), resolved alert | S25 | 2026-03-21 |
| DONE-027 | Security: dismissed code scanning alert #1 (missing permissions — fixed in CI workflow) | S25 | 2026-03-21 |
| DONE-028 | Closed GitHub issues #1 (research taxonomy — superseded by SGO registry), #2 (ingestion cleanup — source files deleted), #26 (org checkout bump) | S25 | 2026-03-21 |
| DONE-029 | Merged PR #27 (Copilot autofix — 4 quality corrections to session retrospective) | S25 | 2026-03-21 |
| DONE-030 | Org-level ci-minimal.yml bumped to actions/checkout@v6 (in .github repo, feat/canonical-readme-standards branch) | S25 | 2026-03-21 |
| DONE-031 | Research corpus status taxonomy applied — 66 files updated to `status: reference-activated` frontmatter | S25 | 2026-03-21 |
| DONE-032 | Gmail notification triage — 201 emails → 3 actionable items, all resolved | S26 (gmail-triage) | 2026-03-21 |
| DONE-033 | victoroff-group a11y remediation — 4 Gemini review issues (h1 overlap, disclosure clipping, badge version, meta-viewport rule), 40/40 Playwright | S26 | 2026-03-21 |
| DONE-034 | growth-auditor security — PDF endpoint rate limiting (10 req/hr/IP), Codex P1 finding | S26 | 2026-03-21 |
| DONE-035 | growth-auditor infra — `.config/` restored (vitest/playwright/eslint), 3 missing lib modules created (schemas/config/env), tests 196→346 | S26 | 2026-03-21 |
| DONE-036 | Global gitignore fix — `/.config` removed, `lib/`→`/lib/` scoped, chezmoi-deployed system-wide | S26 | 2026-03-21 |
| DONE-037 | Dependabot auto-merge + grouping on stakeholder-portal, organvm-engine, praxis-perpetua (partial IRF-SYS-002) | S26 | 2026-03-21 |
| DONE-038 | stakeholder-portal Next.js 16.2.1 + eslint-config-next sync — PR #27, 265/265 tests, lint clean | S26 | 2026-03-21 |
| DONE-039 | Community reply to m13v on agentic-titan#20 (multi-agent orchestration evaluation) | S26 | 2026-03-21 |
| DONE-040 | Security PR merged — organvm-corpvs-testamentvm#269 (npm_and_yarn low severity) | S26 | 2026-03-21 |

---

## Blocked

*None currently.*

---

## Archived

*None currently.*

---

## Statistics

- **Total active items:** 123 (119 prior + 4 new from S26)
- **P0 (NOW):** 13
- **P1 (SOON):** 43 (41 prior + 2 new: IRF-SYS-006, IRF-SYS-009)
- **P2 (GROWTH):** 58 (56 prior + 2 new: IRF-SYS-007, IRF-SYS-008)
- **P3 (HORIZON):** 9
- **Completed:** 40 (31 prior + 9 from S26)
- **Blocked:** 0

### By Domain

| Domain | Active | Completed | Total |
|--------|--------|-----------|-------|
| SYS (System-wide) | 9 | 0 | 9 |
| IDX (Index apparatus) | 3 | 1 | 4 |
| SKL (Skills) | 3 | 1 | 4 |
| MON (Monitoring) | 3 | 0 | 3 |
| CRP (Corpus) | 3 | 0 | 3 |
| SGO (Studium) | 6 | 3 | 9 |
| VIG (Vigiles) | 2 | 1 | 3 |
| TRV (Trivium) | 2 | 1 | 3 |
| TST (Testament) | 1 | 1 | 2 |
| OBJ (Object Lessons) | 7 | 1 | 8 |
| KER (Kerygma) | 2 | 0 | 2 |
| PRT (Portfolio) | 1 | 2 | 3 |
| APP (Application) | 1 | 1 | 2 |
| GEN (Generative) | 3 | 0 | 3 |
| IRA (Authority) | 3 | 1 | 4 |
| ARC (Architecture) | 6 | 0 | 6 |
| BLK (Blockchain) | 2 | 0 | 2 |
| DOC (Documentation) | 5 | 0 | 5 |
| VER (Verification) | 3 | 3 | 6 |
| RES (Research Programme) | 68 | 9 | 77 |
| **TOTAL** | **128** | **23** | **151** |

### Research Programme Breakdown

| Category | P0 | P1 | P2 | Total | DONE |
|----------|----|----|----|----|------|
| GOVERNANCE | 5 | 7 | 5 | 17 | 2 |
| MEASUREMENT | 3 | 8 | 7 | 18 | 0 |
| NAMING | 1 | 3 | 6 | 10 | 1 |
| ARCHITECTURE | 3 | 4 | 2 | 9 | 0 |
| TOOLING | 0 | 2 | 3 | 5 | 0 |
| PROCESS | 0 | 5 | 3 | 8 | 0 |
| **Total** | **12** | **29** | **26** | **67** | **3** |

*Note: 3 additional completed research programme items (Research Pipeline SOP, Research Registry, Session Retrospective) are process deliverables not in the 71-task manifest.*

### Effort Distribution (Research Programme)

| Effort | Count |
|--------|-------|
| S (hours) | 13 |
| M (days) | 30 |
| L (weeks) | 22 |
| XL (months) | 3 |

---

*Last updated: 2026-03-20 — Session: SGO research programme implementation manifest integration (71 tasks added; 3 DONE, 68 OPEN)*
*Next update: After any session that produces or discovers work items*
