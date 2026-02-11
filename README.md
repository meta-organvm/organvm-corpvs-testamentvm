# Eight-Organ System: Planning & Governance Corpus

[![License: CC BY-SA 4.0](https://img.shields.io/badge/License-CC%20BY--SA%204.0-lightgrey?style=flat-square)](LICENSE)
[![Status: LAUNCHED](https://img.shields.io/badge/Status-LAUNCHED-2e7d32?style=flat-square)](#current-status)
[![Organs: 8](https://img.shields.io/badge/Organs-8-1a237e?style=flat-square)](#the-eight-organ-model)
[![Repos: 77](https://img.shields.io/badge/Repos-77-2e7d32?style=flat-square)](#the-eight-organ-model)
[![Docs: ~270K words](https://img.shields.io/badge/Docs-~270K%20words-6a1b9a?style=flat-square)](#current-status)

> Complete planning, audit, and implementation corpus for an eight-organ creative-institutional system coordinating 77 GitHub repositories across 8 organizations (7 organs + 1 meta). The system is **live** — all organs are operational.

This is **not a source code repository**. It is the authoritative planning and governance corpus for the organvm system — a framework that protects distinct modes of work (theory, art, commerce, community) from collapsing into each other, while presenting the meta-system itself as a portfolio asset. The system launched on 2026-02-11 with 72 documented repositories (~270K words), 5 meta-system essays, and automated governance via GitHub Actions.

---

## Quick Navigation

| If you want to... | Read this |
|-------------------|-----------|
| Understand the whole system in 30 minutes | [`00-c-master-summary.md`](docs/genesis/00-c-master-summary.md) |
| See the strategic rationale | [`parallel-launch-strategy.md`](docs/strategy/parallel-launch-strategy.md) |
| Know what repos exist and their status | [`registry-v2.json`](registry-v2.json) |
| See the execution plan | [`implementation-package-v2.md`](docs/implementation/implementation-package-v2.md) |
| Understand governance rules | [`orchestration-system-v2.md`](docs/implementation/orchestration-system-v2.md) |
| See the canonical timeline | [`roadmap-there-and-back-again.md`](docs/strategy/roadmap-there-and-back-again.md) |
| Read the meta-system essays | [public-process on GitHub Pages](https://organvm-v-logos.github.io/public-process/) |
| See the orchestration hub | [orchestration-start-here](https://github.com/organvm-iv-taxis/orchestration-start-here) |
| See every file annotated | [`ANNOTATED-MANIFEST.md`](docs/ANNOTATED-MANIFEST.md) |

---

## Document Architecture

The corpus is organized in layers, each building on the previous:

```
Layer 0: Genesis (docs/genesis/)
  00-a (Q&A transcript) → 00-b (local/remote structure) → 00-c (master summary) → 00-d (system audit)

Layer 1: Phase 1 Planning (docs/planning/)
  01 (scoring rubric) → 02 (inventory) → 03 (templates) → 04 (checklists) → 05 (risk map)

Layer 2: Execution & Strategy (docs/strategy/)
  phase-1-execution-index → parallel-launch-strategy → roadmap-there-and-back-again

Layer 3: v2 Active Documents (docs/implementation/)
  implementation-package-v2 → orchestration-system-v2 → public-process-map-v2 → registry-v2.json → github-actions-spec

Layer 4: Evaluation & Cross-Validation (docs/evaluation/)
  06 (evaluation) → 07 (prompts + results) → 08 (canonical action plan) → 09 (corpus coherence review)

Layer 5: Standards & Configuration (docs/standards/ + .config/)
  10-repository-standards → 11-specification-driven-development → organvm.env → organvm.config.json

Archive: v1 predecessors (docs/archive/, frozen, superseded by v2)
```

The full cross-document dependency map and per-file annotations are in [`ANNOTATED-MANIFEST.md`](docs/ANNOTATED-MANIFEST.md).

For a concise directory map, see [`DIRECTORY.md`](DIRECTORY.md).

---

## Current Status

**The system is LAUNCHED.** All 8 organs are operational as of 2026-02-11.

| Milestone | Status |
|-----------|--------|
| Phase -1: Org architecture + config files | **DONE** (2026-02-09) |
| Phase -1: GitHub orgs live + repo transfers | **DONE** (2026-02-10) |
| Bronze Sprint: 7 flagship READMEs | **DONE** (2026-02-10) |
| Silver Sprint: 58 repo READMEs (~202K words) | **DONE** (2026-02-10) |
| Gold Sprint: Essays, health files, workflows, descriptions | **DONE** (2026-02-10) |
| Phase 2: Micro-validation (all 8 organs locked) | **DONE** (2026-02-10) |
| Phase 3: GitHub Actions, POSSE, branch protection | **DONE** (2026-02-10) |
| Launch: 9/9 criteria met | **DONE** (2026-02-11) |
| Gap-Fill Sprint: Uniform quality across all repos | **DONE** (2026-02-11) |

### Launch Metrics

| Metric | Value |
|--------|-------|
| Repos on GitHub | 77 |
| Documented repos (2,000+ word READMEs) | 72 |
| Total documentation | ~270,000 words |
| Flagship repos | 7 |
| Standard repos | 57 |
| Meta-system essays | 5 (21,625 words) |
| GitHub Actions workflows | 5 |
| Dependency edges validated | 31 (0 violations) |
| POSSE channels | Mastodon + Discord |
| GitHub Pages | [public-process](https://organvm-v-logos.github.io/public-process/) |

---

## The Eight-Organ Model

| Organ | Domain | GitHub Org | Repos | Flagships | Portfolio Angle |
|-------|--------|-----------|-------|-----------|-----------------|
| I | Theory (epistemology, recursion, ontology) | [`organvm-i-theoria`](https://github.com/organvm-i-theoria) | 18 | recursive-engine | Intellectual foundations |
| II | Art (generative, performance, experiential) | [`organvm-ii-poiesis`](https://github.com/organvm-ii-poiesis) | 27 | metasystem-master, a-mavs-olevm | Creative practice |
| III | Commerce (SaaS, B2B, B2C products) | [`organvm-iii-ergon`](https://github.com/organvm-iii-ergon) | 21 | public-record-data-scrapper | Deployed products |
| IV | Orchestration (governance, routing) | [`organvm-iv-taxis`](https://github.com/organvm-iv-taxis) | 9 | orchestration-start-here, agentic-titan | System architecture |
| V | Public Process (essays, building in public) | [`organvm-v-logos`](https://github.com/organvm-v-logos) | 2 | public-process | Transparent methodology |
| VI | Community (salons, reading groups) | [`organvm-vi-koinonia`](https://github.com/organvm-vi-koinonia) | 3 | — | Relational infrastructure |
| VII | Marketing (POSSE distribution, announcements) | [`organvm-vii-kerygma`](https://github.com/organvm-vii-kerygma) | 4 | — | External communication |
| VIII | Meta (umbrella org) | [`meta-organvm`](https://github.com/meta-organvm) | 1 | — | System-level coordination |

The organ model prevents three pathologies: art corrupted by commerce, theory compromised by scale, and community colonized by metrics. Each organ has its own GitHub organization, governance rules, and documentation standards.

Dependencies flow unidirectionally: **I → II → III**. ORGAN-III cannot depend on ORGAN-II. All organs are documented by V and amplified by VII.

---

## How to Use This Corpus

### For Human Readers

1. **Start with** [`00-c-master-summary.md`](docs/genesis/00-c-master-summary.md) for a 30-minute overview of the system's design
2. **Browse** [`registry-v2.json`](registry-v2.json) to see all 77 repos with their status, tiers, and documentation state
3. **Read the essays** at [public-process](https://organvm-v-logos.github.io/public-process/) for the meta-system narrative
4. **Reference** the numbered documents (`01`–`05`) in [`docs/planning/`](docs/planning/) for the original planning methodology

### For AI Agents

- **Claude Code:** Read [`CLAUDE.md`](CLAUDE.md) first — it provides full project context, key invariants, and document architecture
- **Gemini:** Read [`docs/agents/GEMINI.md`](docs/agents/GEMINI.md) for Gemini-specific onboarding
- **Any agent:** Read [`docs/agents/AGENTS.md`](docs/agents/AGENTS.md) for universal agent guidelines (commit style, testing, security)
- **Full file inventory:** [`docs/ANNOTATED-MANIFEST.md`](docs/ANNOTATED-MANIFEST.md) provides exhaustive per-file annotations

### Key Invariants

1. `registry-v2.json` is the single source of truth for all repo state
2. No back-edges in the dependency graph (I → II → III only)
3. All 8 organs are represented at launch
4. Documentation precedes deployment
5. Every README is a portfolio piece
6. Promotion is a state machine: LOCAL → CANDIDATE → PUBLIC_PROCESS → GRADUATED → ARCHIVED

---

## License

This work is licensed under the [Creative Commons Attribution-ShareAlike 4.0 International License](LICENSE) (CC BY-SA 4.0).

You are free to share and adapt this material for any purpose, including commercial, as long as you give appropriate credit and distribute derivative works under the same license.

---

## Author

**@4444j99** / **@4444J99**

This corpus operates on an AI-conductor model: human directs, AI generates volume, human reviews and refines. The meta-system — and the process of building it — is itself the primary portfolio artifact.
