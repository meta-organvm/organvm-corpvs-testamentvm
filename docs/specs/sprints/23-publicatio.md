# Sprint 23: PUBLICATIO

**Date:** 2026-02-16
**Focus:** Essay publication
**Status:** COMPLETE

## Problem

29 essays deployed to public-process, but the catalog identified gaps: 1 complete undeployed draft (`14-promotions-in-practice.md`), 4 planned-but-never-written essays from `public-process-map-v2.md`, and new essays aligned with omega horizons. The essay corpus was stale — last batch deployed 2026-02-13, and application targets (particularly Together AI, HuggingFace, Eyebeam, Processing Foundation) benefit from fresh evidence of documentation ability and creative-institutional thinking.

## Solution

Deploy 1 existing draft + write and deploy 3 new essays = 4 publications (29→33 essays).

### Essay selection rationale:
- **Promotions in Practice** (existing draft): Complete, ~2,500 words, governance-as-practice angle. Ready to deploy.
- **How to Think About Autonomous Systems** (new): Guide/teaching essay. Demonstrates teaching ability for Together AI and HuggingFace applications. Maps five mental models from five years of building the eight-organ system.
- **Why the Organ Model Separates Commerce from Theory** (new): Philosophical essay. Demonstrates systems thinking for residency applications (Eyebeam, Google Creative). Addresses the most common question about the system's architecture.
- **Governance Frameworks for Artists** (new): Practical guide. Directly targets Processing Foundation and Eyebeam. Translates institutional governance patterns for creative practitioners.

## Deliverables

### 1. Deployed: "Promotions in Practice" (existing draft)
- Source: `docs/essays/14-promotions-in-practice.md`
- Deployed to: `_posts/2026-02-16-promotions-in-practice.md`
- ~2,500 words, governance-practice category
- Front matter updated to match deployed format (layout, author, date quotes)
- Fixed stale "PRODUCTION" references to "ACTIVE" (VERITAS alignment)

### 2. Written + Deployed: "How to Think About Autonomous Systems"
- Source: `docs/essays/30-how-to-think-about-autonomous-systems.md`
- Deployed to: `_posts/2026-02-16-how-to-think-about-autonomous-systems.md`
- ~3,200 words, guide category
- Five mental models: dependency graph as architecture, state machines over ad hoc, constraints generate, observability not optional, human as appellate court
- Common failure modes section

### 3. Written + Deployed: "Why the Organ Model Separates Commerce from Theory"
- Source: `docs/essays/31-why-the-organ-model-separates-commerce-from-theory.md`
- Deployed to: `_posts/2026-02-16-why-the-organ-model-separates-commerce-from-theory.md`
- ~3,100 words, meta-system category
- Three reasons (commercial pressure corrupts theory, different quality models, enables promotion pipeline)
- Historical precedent (Bell Labs, universities)

### 4. Written + Deployed: "Governance Frameworks for Artists"
- Source: `docs/essays/32-governance-frameworks-for-artists.md`
- Deployed to: `_posts/2026-02-16-governance-frameworks-for-artists.md`
- ~3,000 words, guide category
- Four patterns (registry, state machine, dependency graph, audit trail)
- Three starting points by effort level
- Addresses four common objections

### 5. Overlap resolution
- `21-promotion-pipeline.md` confirmed as already deployed (`2026-02-13-the-promotion-pipeline.md`) — not a gap

### 6. Metrics propagation
- `calculate-metrics.py`: essays 29→33, sprints 22→23
- `propagate-metrics.py`: 27 replacements across 18 files

## Metrics

| Metric | Before | After |
|--------|--------|-------|
| Deployed essays | 29 | 33 |
| Essay drafts in corpus | 6 | 9 |
| Total word count (est.) | ~386K+ | ~398K+ |
| Files updated by propagation | — | 18 |
| Replacements | — | 27 |

## Remaining from catalog (not addressed this sprint)

These items from the PUBLICATIO catalog description were deferred:
- "constraint-alchemy-workshop" essay (planned, never written)
- "performance-platform-methodology" essay (planned, never written)
- 30-day soak test report (omega H1 — not yet at 30 days)
- First application experience retrospective (omega H2 — no submissions yet)
- ORGAN-III product development journal (omega H3 — future sprint)

## Verification

- `gh api repos/organvm-v-logos/public-process/contents/_posts --jq 'length'` returns 33
- All 4 new files accessible via GitHub API
- `calculate-metrics.py` reports 33 essays
- `propagate-metrics.py` reports 0 stale values after propagation
