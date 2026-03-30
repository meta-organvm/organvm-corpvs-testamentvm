# Signal Closure Cascade — Lex Necessitatis Enforcement

**Date:** 2026-03-28
**Authority:** AX-6 (Signal Closure), Amendment F, LIQ-008
**Scope:** System-wide — all organs, 4 phases, April grant deadlines
**Status:** READY — pickup point for next session

---

## Context

AX-6 (Signal Closure / Lex Necessitatis) was ratified 2026-03-27. The entailment matrix in `governance-rules.json` defines minimum organ-to-organ signal connectivity. An initial audit against current seed.yaml contracts reveals massive structural violations: the interface organs (V, VI, VII) are disconnected from the production core (I, II, III).

Three forces converge:
1. **AX-6 obligations** — constitutional violations demand immediate remedy
2. **April grant cascade** — NLnet (April 1), Creative Capital (April 2), Sovereign Tech (April 6), ZKM (April 12)
3. **Active client revenue** — Maddie pricing unsent (IRF-APP-031, P1 BLOCKING)

The deduction: grant applications ARE signal closure compliance. The consulting case study IS the ORGAN-V output. The announcement IS the ORGAN-VII output. One action satisfies multiple entailment edges.

---

## Phase 1 — GROUND (2026-03-28)

### 1.1 Send Maddie Pricing
- **IRF:** IRF-APP-031 (P1 BLOCKING)
- **Action:** Send $1K deposit + $200/month retainer pricing
- **Owner:** Human
- **Cost:** Text message
- **Unblocks:** First revenue into ORGAN-III

### 1.2 Signal Closure Audit → IRF-VAC Entries
- **Action:** For each active organ, validate entailment_flows matrix against actual seed.yaml produces/consumes edges
- **Violations found (2026-03-27 preliminary audit):**

| Source | Target | Entailed Signal | Status |
|--------|--------|----------------|--------|
| ORGAN-III (consulting) | ORGAN-V | process-documentation | **MISSING** — no produces edge from any active ORGAN-III repo to ORGAN-V |
| ORGAN-III (consulting) | ORGAN-VII | distribution-signal | **MISSING** — kerygma-pipeline has zero consumes from ORGAN-III |
| ORGAN-III (consulting) | ORGAN-VI | community-growth | **MISSING** — community-hub has zero consumes from ORGAN-III |
| ORGAN-III (consulting) | ORGAN-I | research-feedback | **MISSING** — no feedback edge from consulting to Theoria |
| ORGAN-I (SGO program) | ORGAN-VII | distribution | **MISSING** — no distribution signal declared |
| ORGAN-I (SGO program) | ORGAN-V | public-discourse | **PARTIAL** — arXiv pending, no essay-pipeline connection |
| ORGAN-III (institutional) | ORGAN-V | process-documentation | **MISSING** — no public process for fiscal sponsorship work |
| ORGAN-III (institutional) | ORGAN-VII | distribution | **MISSING** — no announcement channel for institutional strategy |

- **Output:** Create IRF-VAC-xxx entries for each violation. Zero-cost fills (seed.yaml edge additions) executed immediately.

### 1.3 Wire Interface Organs (Zero-Cost Fills)
- **Action:** Update seed.yaml in these repos to add missing produces/consumes edges:
  - `sovereign-systems--elevate-align/seed.yaml` — add produces to V, VII, VI, I
  - `kerygma-pipeline/seed.yaml` — add consumes from ORGAN-III, ORGAN-I, ORGAN-II
  - `essay-pipeline/seed.yaml` — add consumes from ORGAN-III, ORGAN-I
  - `community-hub/seed.yaml` — add consumes from ORGAN-III, ORGAN-II
  - `public-process/seed.yaml` — verify consumes edges exist
- **Validation:** `organvm seed validate` after each batch

### 1.4 Create `organvm` GitHub Org
- **IRF:** IRF-LIQ-001 (P0)
- **Owner:** Human (web UI)
- **Unblocks:** Liquid constitutional order migration

---

## Phase 2 — APPLICATIONS (2026-03-28 → April 2)

### 2.1 NLnet NGI0 Commons
- **Deadline:** April 1 (3 days)
- **Narrative:** ORGANVM as open-source governance infrastructure — signal closure as fundable architecture
- **Key evidence:** AX-6 (machine-readable governance), entailment matrix, 127 repos under constitutional law
- **Materials location:** `meta-organvm/aerarium--res-publica/applications/nlnet/`
- **References:** Full institutional strategy in `aerarium--res-publica/strategy/`

### 2.2 Creative Capital
- **Deadline:** April 2 (opens for submission)
- **IRF:** IRF-APP-015 (P0 — ADVANCED to drafting 2026-03-25)
- **Narrative:** Eight-organ model as creative practice — consulting-to-research pipeline demonstrates art-commerce-theory cycle
- **Key evidence:** I→II→III flow, SGO research program (13 works, 500K words), signal closure showing practice generates theory
- **Materials:** Resume (batch-03, PDF), cover letter (alchemized), profile JSON (3-length statements/bios/samples)
- **Materials location:** `4444J99/application-pipeline/` + `aerarium--res-publica/applications/`

### 2.3 Maddie Case Study (ORGAN-V Output)
- **Action:** Write building-in-public essay on solo-practitioner consulting model
- **Satisfies:** ORGAN-III → ORGAN-V entailment (AX-6)
- **Double duty:** Becomes grant evidence for Creative Capital AND NLnet
- **Target location:** `organvm-v-logos/public-process/essays/` or `organvm-v-logos/essay-pipeline/`

### 2.4 Distribution Signal (ORGAN-VII Output)
- **Action:** Announce consulting launch + signal closure architecture via POSSE pipeline
- **Satisfies:** ORGAN-III → ORGAN-VII entailment (AX-6)
- **Double duty:** Social proof for grant reviewers
- **Target:** `organvm-vii-kerygma/kerygma-pipeline/` dispatch

---

## Phase 3 — INFRASTRUCTURE (April 2-6)

### 3.1 Build `validate_signal_closure` Validator
- **Location:** `organvm-engine/src/organvm_engine/governance/dictums.py`
- **Interface:** `organvm governance audit --signal-closure`
- **Logic:** Read entailment_flows from governance-rules.json, discover active repos per organ via registry, check seed.yaml produces edges against required targets, emit violations as audit findings
- **Tests:** `organvm-engine/tests/test_governance_signal_closure.py`
- **References:** AX-6 validator field = `validate_signal_closure`

### 3.2 Client Pillar Spec
- **IRF:** IRF-APP-018 (P1)
- **Action:** Formalize contracts, SOPs, intake-to-delivery workflow, proposal/invoice standards
- **Location:** `organvm-iii-ergon/consult-consul--console/docs/`
- **Critical gaps (from memory):**
  - No standardized contract/legal templates
  - No SOP documents for client lifecycle
  - No proposal/invoice standards
  - No formalized intake-to-delivery workflow
  - No client scoring/qualification rubric

### 3.3 Sovereign Tech Fellowship
- **Deadline:** April 6
- **Narrative:** Digital sovereignty through solo-practitioner orchestration at enterprise scale
- **Materials location:** `aerarium--res-publica/applications/sovereign-tech/`

---

## Phase 4 — FLYWHEEL (April 7+)

### 4.1 ZKM Rauschenberg Residency
- **Deadline:** April 12
- **Narrative:** Poiesis evidence — generative art + performance systems

### 4.2 SGO arXiv Submissions
- **IRF:** IRF-SGO-001 (P1) + related items
- **Action:** Submit research works, satisfying I→V→VII entailment chain
- **13 works, 500K+ words already written

### 4.3 Three Companion Indices
- **IRF:** IRF-IDX-001, 002, 003 (all P1)
- **Plan exists:** `2026-03-21-companion-indices-construction-plan.md`
- **Action:** Build Index Locorum, Nominum, Rerum

### 4.4 Omega #9 Push
- **IRF:** IRF-CRP-001 (P1), IRF-HRM-006 (P2)
- **Action:** Stranger-ready polish — closest unmet criterion (8/19 → 9/19)

---

## Pickup Protocol

When resuming this plan:

1. Check which Phase 1 items are complete (human-gated items may have been done between sessions)
2. Read `aerarium--res-publica/` for current grant application state
3. Verify NLnet deadline proximity — if <24h, go directly to 2.1
4. Run `organvm governance audit` (if validator exists) or manual seed.yaml audit
5. Check IRF for any new P0 items added since 2026-03-28

## Related IRF Items

P0: IRF-SYS-009, IRF-LIQ-001, IRF-APP-015, IRF-OSS-017
P1 BLOCKING: IRF-APP-031
P1: IRF-APP-003, IRF-APP-005, IRF-APP-017, IRF-APP-018, IRF-APP-021, IRF-APP-022
P1: IRF-CRP-001, IRF-CRP-005, IRF-MON-006, IRF-MON-008
P1: IRF-SGO-001, IRF-SGO-008
P1: IRF-IDX-001, IRF-IDX-002, IRF-IDX-003
P1: IRF-LIQ-002, IRF-LIQ-003, IRF-LIQ-004, IRF-LIQ-009, IRF-LIQ-010
