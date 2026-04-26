# Portfolio Unification Framework Stack

**Created:** 2026-04-25
**Source session:** S-modular-synthesis-portfolio-unification
**Layer status:** PDE shipped, MSP shipped, DIWS designed (v2.2) NOT YET BUILT, Synthesis layer NEW

## Purpose

Document the 4-layer composition that lets a single user run N concurrent product-domains while computing combinatorial overlaps across them. The user's framing: *"logic + meta + metaphysics computed to absurdity."*

## Stack Diagram

```
┌─────────────────────────────────────────────────────────────────┐
│                    PORTFOLIO MATRIX (user layer)                │
│  Scott Lefler / Jessica / Maddie / Rob / + (4+ concurrent)      │
└────────────────────────────┬────────────────────────────────────┘
                             │
        ┌────────────────────┴────────────────────┐
        │  Portfolio Operator (DIWS v2 + v2.1)    │
        │  - pull (Phase 0)  [engine reuse]       │
        │  - push (v2)       [cross-domain flow]  │
        │  - Phase 0.5: portfolio-gap-audit.sh    │
        │    (the "stretching rack")              │
        └────────────────────┬────────────────────┘
                             │
    ┌────────────────────────┼────────────────────────┐
    │                        │                        │
    ▼                        ▼                        ▼
┌─────────────────┐  ┌─────────────────┐  ┌──────────────────┐
│  DIWS Instance  │  │  DIWS Instance  │  │  DIWS Instance   │
│  (Chess domain) │  │ (Wellness dom.) │  │ (Education dom.) │
│                 │  │                 │  │                  │
│ Phase 0 (audit) │  │ Phase 0 (audit) │  │ Phase 0 (audit)  │
│ Layers 1–8      │  │ Layers 1–8      │  │ Layers 1–8       │
│ + 4 operators   │  │ + 4 operators   │  │ + 4 operators    │
└────────┬────────┘  └────────┬────────┘  └────────┬─────────┘
         │                    │                    │
         │ (substrate filled) │                    │
         ▼                    ▼                    ▼
    ┌────────────────────────────────────┐
    │   PDE Instance N                   │
    │   - Phase 1: IDENTIFY (agents)     │
    │   - Phase 2: MAP (constraints)     │
    │   - Phase 3: ENCODE (types/tests)  │
    │   - Phase 4: EXPRESS (4 modes)     │
    │   - Phase 5: DEPLOY (density)      │
    │   Composition matrix → blends      │
    │   logos / ethos / pathos / kairos  │
    └────────┬───────────────────────────┘
             │
             ▼
    ┌────────────────────────────────────┐
    │   Modular Synthesis Patcher (MSP)  │
    │   Combines multiple PDE outputs    │
    │   across portfolio via primitives: │
    │                                    │
    │   - Oscillators (PDE instances)    │
    │   - Filters (mode blenders)        │
    │   - Modulators (operators)         │
    │   - Feedback (autopoietic loop)    │
    │                                    │
    │   Signals: logos/ethos/pathos      │
    │   Control: phase gates, operators  │
    └────────┬───────────────────────────┘
             │
             ▼
    ┌────────────────────────────────────┐
    │   UNIFIED PORTFOLIO OUTPUT         │
    │   - shared engines surfaced        │
    │   - cross-pollination artifacts    │
    │   - meta-skill extractions         │
    │   - n-way combination products     │
    └────────────────────────────────────┘
```

## Layer specifications

### Layer 0 — DIWS (Domain Ideal-Whole Substrate)

**Status:** DESIGNED v2.2, NOT BUILT (gating dependency)
**Path:** `~/Workspace/a-i--skills/skills/project-management/domain-ideal-whole-substrate/`
**Plan:** `~/.claude/plans/2026-04-25-domain-ideal-whole-substrate-design.md`

**8 strata** (every domain loads identically):

| # | Layer | Question | Output |
|---|-------|----------|--------|
| 1 | Ontology | What is the domain made of? | `domain-ontology.md` |
| 2 | Lineage | How did it become what it is? | `domain-lineage.md` |
| 3 | Constellation | Who is doing it well? | `domain-constellation.yaml` (75-person file) |
| 4 | Gap-map | Where is unexploited terrain? | `domain-gap-map.md` |
| 5 | Practitioner agents | Who serves the work? | `domain-agent-fleet.yaml` |
| 6 | Production stack | What does shipping require? | `domain-production-stack.md` |
| 7 | Internal magnet | What flows IN? | `domain-attractor.md` |
| 8 | External contribution | What flows OUT? | `domain-contribution-charter.md` |

**4 operators** (fire simultaneously per Tenet Protocol):

1. **Selfish-altruistic loop** — single-engagement self-cycle
2. **Magnetic membrane** — single-domain in/out flow
3. **Portfolio Operator** (v2 + v2.1) — cross-portfolio bidirectional pull/push
4. **Reflexive Operator** (v2.2) — build + study-of-build co-arise

**Phase 0 + 0.5** (pre-instantiation):

- Phase 0: `audit-portfolio.sh` — globs `~/Workspace/` for engines (3-tier taxonomy: domain-engines, meta-engines, consultant-engines)
- Phase 0.5: `portfolio-gap-audit.sh` — **the stretching rack**; gap-map operator at portfolio scale, holes/fat report

### Layer 1 — PDE (Product-Domain Engine)

**Status:** SHIPPED 2026-04-25 (cf92479)
**Path:** `~/Workspace/a-i--skills/skills/project-management/product-domain-engine/SKILL.md`

**4 rhetorical modes** (independent output classes):

| Mode | Question | Outputs |
|------|----------|---------|
| Logos | What is structurally true? | Types, proofs, algorithms |
| Ethos | Why trust this? | Citations, scholarship, density |
| Pathos | Why does it matter? | Narrative, voice, community |
| Kairos | When is the moment? | Timing, zeitgeist alignment |

**5-phase protocol:**

1. IDENTIFY — agent census
2. MAP — domain structures
3. ENCODE — types, tests, schemas
4. EXPRESS — through 4 modes independently
5. DEPLOY — let density create gravity

**Known gaps:**

- **Tier-0 gap:** PDE cannot ingest DIWS substrate as input. N independent invocations, no portfolio-level composition matrix.
- **No holes/fat diagnostic:** mode-imbalance scoring exists but no formal stretching-rack equivalent.

### Layer 2 — MSP (Modular Synthesis Philosophy)

**Status:** SHIPPED
**Path:** `~/Workspace/a-i--skills/skills/creative/modular-synthesis-philosophy/SKILL.md`

**Synthesis-to-portfolio mapping:**

| Synthesis primitive | Portfolio architecture |
|---------------------|------------------------|
| Oscillator (signal generator) | Product instance, domain instantiation |
| Filter (signal processor) | Mode blender, composition matrix |
| Modulator (control system) | Portfolio operator, constraint engine |
| Mixer (combiner) | Cross-domain synthesis output |
| VCA (amplitude control) | Feature flag, resource gate |
| Feedback loop | Recursive observer, autopoietic loop |

**Patching patterns:**

- Series (linear): PDE 5-phase sequence
- Parallel (split & merge): multiple domains processed independently
- Feedback: autopoietic loop, reflexive operator
- Cross-modulation: cross-pollination between domain pairs

### Layer 3 — Synthesis (NEW)

**Status:** TO BE BUILT (parent plan Stream "Synthesis layer")
**Output target:** `<organvm-corpvs>/docs/portfolio/portfolio-synthesis.md`

**Method:**

For each combination of clients (pairs, triples, quads):
1. Load N DIWS instances simultaneously
2. Run `portfolio-gap-audit.sh` (the stretching rack) on the merged whole
3. Identify holes (under-developed in the merged domain) + fat (redundant in the merged domain)
4. Propose what unified product fills the hole

**Example** (Scott × Maddie × Rob = "design + wellness + chess pedagogy"):
→ Unified output: design-language-for-transformation-coaches (new product domain)

## Adjacent skills and their relationship

| Skill | Path | Overlap with stack |
|-------|------|--------------------|
| project-alchemy-orchestrator | `~/Workspace/a-i--skills/skills/project-management/project-alchemy-orchestrator/` | Earlier (governance / lifecycle stage); complementary |
| agent-swarm-orchestrator | `~/Workspace/a-i--skills/skills/tools/agent-swarm-orchestrator/` | Implementation layer for DIWS stratum 5 (agent fleet) |
| systemic-product-analyst | `~/Workspace/a-i--skills/skills/data/systemic-product-analyst/` | Upstream of PDE Phases 1-2 (diagnostic before formalization) |
| recursive-systems-architect | `~/Workspace/a-i--skills/skills/knowledge/recursive-systems-architect/` | Theoretical foundation for DIWS Reflexive Operator |

## Five named gaps (for follow-up plans)

1. **PDE Tier-0 (Load Substrate)** — extend PDE to take DIWS output as input
2. **Portfolio composition matrix** — extend DIWS v3 with `portfolio-composition-map.md`
3. **Stretching rack** — NEW DIWS Phase-0.5 operator: `portfolio-gap-audit.sh` (Stream Σ)
4. **MSP ↔ DIWS primitive map** — extend MSP with `references/diws-mapping.md`
5. **Portfolio meta-skill extractor** — NEW skill orchestrating DIWS pull → engine taxonomy promotion → consultant-engine registry

## Verification

- [ ] DIWS skill ships and runs `audit-portfolio.sh` end-to-end (Stream Σ closes)
- [ ] `portfolio-gap-audit.sh` produces holes/fat report with ≥1 entry per axis per project
- [ ] PDE invocation can chain after DIWS instantiation (Tier-0 added)
- [ ] Synthesis doc covers C(N,2) + C(N,3) + C(N,4) for portfolio of size N

## Cross-references

- Plan: `~/.claude/plans/okay-so-now-harmonic-kettle.md`
- DIWS plan: `~/.claude/plans/2026-04-25-domain-ideal-whole-substrate-design.md`
- Sister docs: `parameter-matrix.md`, `dark-matter-inventory.md`
