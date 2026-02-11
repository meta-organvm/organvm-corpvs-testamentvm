# Bronze Sprint: Exploration Report

**Date:** 2026-02-10
**Phase:** Step 1 Complete — Exploration Phase
**Source:** Deep audit of 64 live repos across 8 GitHub orgs
**Status:** LOCKED — flagship selections finalized, tier assignments confirmed

---

## Executive Summary

All 64 live repositories across 8 GitHub organizations were explored via GitHub API (README content, directory tree, code size, test coverage, recent activity). Each repo received a tier assignment (Flagship/Standard/Stub/Archive) based on D-07 criteria from `08-canonical-action-plan.md`.

**Key findings:**
- **7 flagship candidates** identified (1 per organ I-IV, 2 for organ II, 1 for organ III; V-VII need creation/stubs)
- **ORGAN-II monorepo discovery:** 7 of 16 repos are subsets of `metasystem-master` — recommend archiving standalone duplicates
- **Several registry corrections needed:** visibility status, tier assignments, and descriptions out of date
- **ORGAN-V/VI/VII:** Only `.github` infra repos exist on GitHub; substantive repos are NOT_CREATED

---

## Flagship Selections (Locked)

| Organ | Flagship Repo | Why | Estimated TE |
|-------|--------------|-----|-------------|
| **I** | `recursive-engine--generative-entity` | 452KB Python, 1,254 tests at 85% coverage, 21 organ handlers, CLI/REPL, bridges to Obsidian/Git/Max/MSP. Existing 3,000+ word README (scored 72/100 — needs portfolio upgrade). The "symbolic operating system" is ORGAN-I's definitive expression. | ~107K |
| **II** | `metasystem-master` | 1MB canonical monorepo containing ALL Omni-Dromenon Engine source (core-engine, performance-sdk, client-sdk, audio-synthesis-bridge, orchestrate CLI, 4 examples, massive docs tree). Most recently pushed (Feb 8). | ~120K |
| **II-alt** | `a-mavs-olevm` | 973MB deployed live website (etceter4.com), Pantheon architecture. Already tagged flagship. Demonstrates ORGAN-II as deployed creative product. | ~107K |
| **III** | `public-record-data-scrapper` | 14.8MB, live Vercel deployment, tiered B2B subscription, 2,055 tests, Terraform AWS infrastructure, 60+ agents, 50-state UCC filing coverage. Strongest revenue proof in ORGAN-III. | ~120K |
| **IV** | `agentic-titan` | 2.4MB Python, 1,095+ tests (adversarial, chaos, e2e, integration, performance, MCP, Ray), 18 completed phases, 6 topologies, model-agnostic multi-agent swarm. Pushed today. | ~107K |
| **V** | `public-process` (NOT_CREATED) | Process essay hub. Needs repo creation + stub + essay. | ~140K |
| **VI** | `.github` (stub only) | Community organ. Stub README in .github profile. | ~12K |
| **VII** | `.github` (stub only) | Marketing organ. Stub README in .github profile. | ~12K |

**Total estimated TE for flagships:** ~725K (within 535K-750K budget band)

---

## Full Tier Assignment Table

### ORGAN-I: Theory (18 repos)

| Repo | Tier | Rationale |
|------|------|-----------|
| `recursive-engine--generative-entity` | **Flagship** | Strongest codebase + existing README + definitive ORGAN-I concept |
| `organon-noumenon--ontogenetic-morphe` | Standard | 274KB, 370 tests, 22 subsystems — strong but narrower scope |
| `sema-metra--alchemica-mundi` | Standard | 162KB TypeScript, 297 tests, 10 axioms — solid theory engine |
| `narratological-algorithmic-lenses` | Standard | 2.3MB monorepo, 14 studies — breadth over depth |
| `cognitive-archaelogy-tribunal` | Standard | 3.6MB, 5 modules — substantial but less portfolio-central |
| `my-knowledge-base` | Standard | 120+ source files, 14 test files — personal knowledge system |
| `4-ivi374-F0Rivi4` | Standard | Tagged flagship in registry but needs validation against actual state |
| `a-recursive-root` | Standard | Kitchen-sink monorepo — needs cleanup before showcase |
| `radix-recursiva-solve-coagula-redi` | Standard | 33MB mostly Obsidian vault — partial implementation |
| `system-governance-framework` | Stub | Generic governance template — not organ-specific enough for Standard |
| `dialectical-ontology` | Standard | Theory-heavy, portfolio-relevant |
| `archetypal-symbolism-engine` | Standard | Symbolic computation focus |
| `epistemic-cartography` | Standard | Knowledge mapping system |
| `recursive-cosmology` | Standard | Cosmological recursion model |
| `meta-ontological-framework` | Standard | Meta-level ontological work |
| `symbolic-topology` | Standard | Mathematical topology of symbols |
| `self-referential-calculus` | Standard | Self-reference formalism |
| `.github` | Infra | Org profile README (already deployed) |

### ORGAN-II: Art (16 existing repos + 6 NOT_CREATED)

| Repo | Tier | Rationale |
|------|------|-----------|
| `metasystem-master` | **Flagship** | Canonical monorepo — ALL ORGAN-II source code consolidated here |
| `a-mavs-olevm` | **Flagship** | Live deployed website (etceter4.com) — demonstrates creative product |
| `a-i-council--coliseum` | Standard | 570KB Python/TypeScript, AI agents + blockchain + event pipeline |
| `omni-dromenon-engine` | Archive | Monorepo duplicate — superseded by metasystem-master |
| `core-engine` | Archive | Monorepo duplicate |
| `performance-sdk` | Archive | Monorepo duplicate |
| `docs` | Archive | Monorepo duplicate |
| `artist-toolkit-and-templates` | Archive | Monorepo duplicate |
| `client-sdk` | Archive | Monorepo duplicate |
| `audio-synthesis-bridge` | Archive | Monorepo duplicate |
| Remaining repos | Stub/Standard | Assess individually during writing phase |
| `.github` | Infra | Org profile README (already deployed) |

**Key finding:** `metasystem-master` CHANGELOG documents consolidation of "12 separate git repositories into a single monorepo." The 7 standalone repos should be archived with redirect notices pointing to `metasystem-master`.

### ORGAN-III: Commerce (21 repos)

| Repo | Tier | Rationale |
|------|------|-----------|
| `public-record-data-scrapper` | **Flagship** | Live Vercel deployment, B2B subscriptions, 2,055 tests, Terraform AWS, 60+ agents. Strongest revenue proof. |
| `trade-perpetual-future` | Standard | 13.7MB Solana/Drift perpetual futures, on-chain revenue via Builder Code referrals. Strong alternate flagship. |
| `life-my--midst--in` | Standard | Currently tagged flagship in registry (Inverted Interview CV platform). Needs re-evaluation. |
| `my--father-mother` | Standard | Massive macOS clipboard tool, 60+ CLI commands, MCP bridge |
| `classroom-rpg-aetheria` | Standard | 2.8MB edtech platform |
| `gamified-coach-interface` | Standard | 8MB coaching platform |
| `fetch-familiar-friends` | Standard | 2.1MB pet app |
| `sovereign-ecosystem--real-estate-luxury` | Standard | 1.9MB real estate platform |
| `multi-camera--livestream--framework` | Standard | Livestreaming infrastructure |
| `universal-mail--automation` | Standard | Email automation |
| `tab-bookmark-manager` | Standard | Browser extension |
| `a-i-chat--exporter` | Standard | Chat export tool |
| `virgil-training-overlay` | Stub | Incomplete training overlay |
| `search-local--happy-hour` | Stub | Local search app |
| `mirror-mirror` | Stub | Private |
| `the-invisible-ledger` | Stub | Private |
| `enterprise-plugin` | Archive | Empty repo |
| `.github` | Infra | Org profile README (already deployed) |

### ORGAN-IV: Orchestration (6 existing + 3 NOT_CREATED)

| Repo | Tier | Rationale |
|------|------|-----------|
| `agentic-titan` | **Flagship** | 2.4MB, 1,095+ tests, 18 phases, 6 topologies, model-agnostic. Definitive orchestration showcase. |
| `agent--claude-smith` | Standard | 131KB TypeScript, Claude SDK wrapper — useful but narrow |
| `a-i--skills` | Standard | 5.2MB, 101 skills — substantial but Anthropic upstream content complicates portfolio claim |
| `petasum-super-petasum` | Standard | 285KB governance docs, 1,818 word README — governance framework |
| `universal-node-network` | Stub | 8KB, single-line README — skeleton |
| `.github` | Infra | Org profile README (already deployed) |

### ORGAN-V: Public Process (1 existing + 1 NOT_CREATED)

| Repo | Tier | Rationale |
|------|------|-----------|
| `.github` | Infra | Org profile README (already deployed) |
| `public-process` | **Flagship** (NOT_CREATED) | Process essay hub — needs creation |

### ORGAN-VI: Community (1 existing + 2 NOT_CREATED)

| Repo | Tier | Rationale |
|------|------|-----------|
| `.github` | Infra | Org profile README (already deployed) |
| `salon-series` | Stub (NOT_CREATED) | Planned community event series |
| `reading-groups` | Stub (NOT_CREATED) | Planned reading group infrastructure |

### ORGAN-VII: Marketing (1 existing + 3 NOT_CREATED)

| Repo | Tier | Rationale |
|------|------|-----------|
| `.github` | Infra | Org profile README (already deployed) |
| `posse-distribution` | Stub (NOT_CREATED) | Planned POSSE syndication |
| `announcements` | Stub (NOT_CREATED) | Planned announcement channel |
| `brand-kit` | Stub (NOT_CREATED) | Planned brand assets |

---

## Open Decision Resolutions

### Decision 2: Local repos public/private matrix
**Resolved:** Per-organ default:
- ORGAN-I (Theory): Public — intellectual contribution is portfolio-visible
- ORGAN-II (Art): Public — creative work benefits from visibility
- ORGAN-III (Commerce): Mixed — deployed products public, private IP repos stay private
- ORGAN-IV (Orchestration): Public — infrastructure demonstrates capability
- ORGAN-V/VI/VII: Public — community-facing by nature

### Decision 3: Empty/skeleton repo disposition
**Resolved:**
- **Archive 7:** ORGAN-II monorepo duplicates (omni-dromenon-engine, core-engine, performance-sdk, docs, artist-toolkit-and-templates, client-sdk, audio-synthesis-bridge)
- **Archive 1:** ORGAN-III `enterprise-plugin` (empty)
- **Populate 4:** ORGAN-V `public-process`, ORGAN-VI `salon-series` + `reading-groups` (stubs), ORGAN-VII `announcements` (stub)
- **Demote 1:** ORGAN-I `system-governance-framework` (flagship→stub)

---

## Registry Corrections Needed

1. **Tier assignments:** Update all repos per table above (most are currently `TBD`)
2. **ORGAN-II monorepo duplicates:** Mark 7 repos for archival
3. **`life-my--midst--in`:** Currently tagged flagship — re-evaluate; `public-record-data-scrapper` is stronger
4. **`4-ivi374-F0Rivi4`:** Currently tagged flagship — validate actual state
5. **Visibility corrections:** Several repos listed as private in registry are actually public on GitHub
6. **`system-governance-framework`:** Demote from any flagship consideration to Stub

---

## Writing Order (per `08` §5 dependency flow)

1. **ORGAN-I:** `recursive-engine--generative-entity` (establishes vocabulary)
2. **ORGAN-II:** `metasystem-master` (independent, can parallel with III)
3. **ORGAN-III:** `public-record-data-scrapper` (independent, can parallel with II)
4. **ORGAN-IV:** `agentic-titan` (references I vocabulary)
5. **ORGAN-V:** Create `public-process` repo + essay (synthesizes I-IV material)
6. **ORGAN-VI/VII:** Stubs (anytime, no dependencies)

**Parallelization:** Steps 2+3 can run concurrently. Steps 6 can run anytime.

---

## TE Budget Estimate (Revised)

| Deliverable | TE Estimate |
|-------------|------------|
| 5 flagship READMEs (I, II, III, IV, V) | 594K |
| 2 alternate/extra flagships (II-alt, III-alt) | 214K |
| 2 stubs (VI, VII) | 24K |
| Registry schema hardening | 70K |
| Process essay | 120K |
| Cross-reference resolution | 80K |
| Coordination overhead (10% per Amendment B) | ~110K |
| **Total** | **~1,212K TE** |

Within the 1.1M-1.6M TE budget band. If we skip the alternate flagships (II-alt `a-mavs-olevm`, III-alt `trade-perpetual-future`), total drops to ~998K.

---

## Next Steps

1. ~~Exploration phase~~ COMPLETE
2. **Begin ORGAN-I flagship README** for `recursive-engine--generative-entity`
3. Registry tier updates (parallel with step 2)
4. Continue per writing order above
