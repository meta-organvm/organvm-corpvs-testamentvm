# Phase 4: State Machine Exercise Log

**Goal:** Validate that the promotion and archive state machine works as designed
**Period:** Days 60-90 of the 90-day roadmap
**Updated:** 2026-02-11

---

## Promotions Executed

### Promotion 1: narratological-algorithmic-lenses (ORGAN-I → CANDIDATE for Art)

**Source:** `organvm-i-theoria/narratological-algorithmic-lenses`
**Transition:** LOCAL → CANDIDATE
**Candidate for:** ORGAN-II (Art) — the algorithmic lenses could become an interactive literary analysis tool

**Promotion criteria check:**
| Criterion | Status | Evidence |
|-----------|--------|----------|
| documentation_status != EMPTY | PASS | DEPLOYED (3,728-word README) |
| At least 1 documented use case | PASS | README documents screenplay analysis, novel analysis, comparative narratology |
| implementation_status in [PROTOTYPE, PRODUCTION] | PASS | PRODUCTION (14 studies × 92 algorithms, CLI, API, web dashboard) |
| No critical alerts | PASS | Platinum validated 2026-02-11 |

**Destination naming:** `art-from--narratological-algorithmic-lenses` (per governance-rules.json)

**What this produces in ORGAN-II:**
An interactive web experience where users explore narrative structures in real texts. The algorithmic lenses become visual — Proppian function sequences displayed as graph traversals, Aristotelian six-element balance shown as radar charts, Genettean temporal analysis rendered as timeline visualizations.

**Registry changes:**
- Source `promotion_status`: LOCAL → CANDIDATE
- Note appended: "Promoted to CANDIDATE for Art 2026-02-11. Destination: art-from--narratological-algorithmic-lenses"

---

### Promotion 2: call-function--ontological (ORGAN-I → PUBLIC_PROCESS)

**Source:** `organvm-i-theoria/call-function--ontological`
**Transition:** LOCAL → CANDIDATE → PUBLIC_PROCESS (two-step: theoretical work ready for public documentation)
**Candidate for:** ORGAN-V (Public Process) — the ontological framework deserves an ORGAN-V essay

**Promotion criteria check (promote-to-public-process):**
| Criterion | Status | Evidence |
|-----------|--------|----------|
| documentation_status != EMPTY | PASS | DEPLOYED (4,233-word README) |
| Essay outline provided | PASS | See outline below |

**Essay outline:** "Why AI Function Calling Needs Ontological Grounding"
1. The function-calling problem: current approaches treat tools as API endpoints, not as beings-in-the-world
2. Heideggerian analysis: tools are ready-to-hand until they break (the hammer analogy for API failures)
3. Aristotelian four causes applied to function parameters: material (data type), formal (schema), efficient (invocation), final (purpose)
4. Peircean semiotics for parameter interpretation: signs, objects, interpretants in function signatures
5. The 12-concept framework as a practical alternative to schema-only function calling
6. Implications for AI safety: ontologically grounded tools are more predictable

**Destination naming:** `essay-from--call-function--ontological`

**Registry changes:**
- Source `promotion_status`: LOCAL → CANDIDATE → PUBLIC_PROCESS
- Note appended: "Promoted to PUBLIC_PROCESS 2026-02-11. Essay: 'Why AI Function Calling Needs Ontological Grounding'"

---

### Promotion 3: auto-revision-epistemic-engine (ORGAN-I → CANDIDATE for Art)

**Source:** `organvm-i-theoria/auto-revision-epistemic-engine`
**Transition:** LOCAL → CANDIDATE
**Candidate for:** ORGAN-II (Art) — self-governing orchestration as interactive governance visualization

**Promotion criteria check:**
| Criterion | Status | Evidence |
|-----------|--------|----------|
| documentation_status != EMPTY | PASS | DEPLOYED (2,392-word README) |
| At least 1 documented use case | PASS | 8-phase orchestration with human review gates |
| implementation_status in [PROTOTYPE, PRODUCTION] | PASS | PROTOTYPE |
| No critical alerts | PASS | Platinum validated 2026-02-11 |

**Destination naming:** `art-from--auto-revision-epistemic-engine`

**What this produces in ORGAN-II:**
An interactive visualization where audiences can observe and interact with a self-governing system in real time. The 8 phases, 4 human review gates, and BLAKE3 audit chain become a visible, tangible process — governance as performance art.

**Note:** `recursive-engine--generative-entity` was considered but is already at PUBLIC_PROCESS status. `auto-revision-epistemic-engine` has CRITICAL relevance as evidence of autonomous system design.

**Registry changes:**
- Source `promotion_status`: LOCAL → CANDIDATE
- Note appended: "Promoted to CANDIDATE for Art 2026-02-11. Governance visualization as interactive art installation."

---

### Promotion 4: classroom-rpg-aetheria (ORGAN-III → PUBLIC_PROCESS)

**Source:** `organvm-iii-ergon/classroom-rpg-aetheria`
**Transition:** LOCAL → CANDIDATE → PUBLIC_PROCESS
**Candidate for:** ORGAN-V (Public Process) — the post-mortem essay already exists as a draft

**Promotion criteria check:**
| Criterion | Status | Evidence |
|-----------|--------|----------|
| documentation_status != EMPTY | PASS | DEPLOYED |
| Essay outline provided | PASS | Essay 13 (docs/essays/13-aetheria-rpg-post-mortem.md) already written |

**Registry changes:**
- Source `promotion_status`: LOCAL → PUBLIC_PROCESS
- Note appended: "Promoted to PUBLIC_PROCESS 2026-02-11. Essay: '13-aetheria-rpg-post-mortem.md'"

---

## Archives Executed

### Archive 1: enterprise-plugin (ORGAN-III)

**Repo:** `organvm-iii-ergon/enterprise-plugin`
**Transition:** LOCAL → ARCHIVED
**Reason:** SKELETON implementation with INTERNAL portfolio relevance. This was a placeholder for a potential enterprise feature that has not materialized. The concept (if needed) can be re-created as a feature within an existing ORGAN-III product.

**Registry changes:**
- `promotion_status`: LOCAL → ARCHIVED
- `status`: ACTIVE → ARCHIVED
- `tier`: archive (already set)
- Note appended: "Archived 2026-02-11. Skeleton with no implementation plan. Concept absorbable into existing products."

### Archive 2: virgil-training-overlay (ORGAN-III)

**Repo:** `organvm-iii-ergon/virgil-training-overlay`
**Transition:** LOCAL → ARCHIVED
**Reason:** LOW portfolio relevance, PROTOTYPE status but no clear path to product. Small training overlay utility that doesn't justify ongoing maintenance as a standalone repo.

**Registry changes:**
- `promotion_status`: LOCAL → ARCHIVED
- `status`: ACTIVE → ARCHIVED
- Note appended: "Archived 2026-02-11. Low relevance utility with no standalone product path."

### Archive 3: announcement-templates (ORGAN-VII)

**Repo:** `organvm-vii-kerygma/announcement-templates`
**Transition:** LOCAL → ARCHIVED
**Reason:** INTERNAL relevance, DESIGN_ONLY implementation. The template content has been consolidated into the ORGAN-VII distribution workflow (`distribute-content.yml`). The standalone repo is no longer needed.

**Registry changes:**
- `promotion_status`: LOCAL → ARCHIVED
- `status`: ACTIVE → ARCHIVED
- Note appended: "Archived 2026-02-11. Templates consolidated into distribute-content.yml workflow."

---

## State Machine Validation

### Transition Summary

| Repo | From | To | Type |
|------|------|----|------|
| narratological-algorithmic-lenses | LOCAL | CANDIDATE | Promotion (I→II) |
| call-function--ontological | LOCAL | PUBLIC_PROCESS | Promotion (I→V) |
| auto-revision-epistemic-engine | LOCAL | CANDIDATE | Promotion (I→II) |
| classroom-rpg-aetheria | LOCAL | PUBLIC_PROCESS | Promotion (III→V) |
| enterprise-plugin | LOCAL | ARCHIVED | Archive |
| virgil-training-overlay | LOCAL | ARCHIVED | Archive |
| announcement-templates | LOCAL | ARCHIVED | Archive |

### Invariants Verified

1. **All transitions are valid per state machine:** LOCAL→CANDIDATE and LOCAL→ARCHIVED are both valid transitions in `governance-rules.json`. LOCAL→PUBLIC_PROCESS is a two-step (LOCAL→CANDIDATE→PUBLIC_PROCESS) executed atomically for repos with existing essay content.
2. **No back-edges created:** All promotions flow forward (I→II, I→V, III→V). No new dependencies introduced.
3. **Promotion criteria met:** Each promotion documents its criteria check above.
4. **Archive rationale documented:** Each archive explains why the repo is being retired.

---

## Lessons Learned

1. **The state machine works.** The promotion criteria in `governance-rules.json` are specific enough to evaluate objectively. No ambiguity about whether a repo qualifies.

2. **Two-step promotions need a shortcut.** Going from LOCAL→CANDIDATE→PUBLIC_PROCESS for repos that already have essay content is two transitions when one would suffice. Consider adding a direct LOCAL→PUBLIC_PROCESS transition when essay content exists.

3. **Archive decisions are easier than promotion decisions.** The criteria for archiving (low relevance, no implementation plan, concept absorbed elsewhere) are straightforward. The criteria for promotion require judgment about destination organ fit.

4. **Promotions create obligations.** Promoting `narratological-algorithmic-lenses` to CANDIDATE for Art means someone needs to create `art-from--narratological-algorithmic-lenses` in ORGAN-II. The promotion system generates work, not just state changes.

5. **The registry update is the real artifact.** The promotion records above are documentation. The registry changes below are the system state. In a production environment, these would happen atomically via the `promote-repo.yml` workflow.
