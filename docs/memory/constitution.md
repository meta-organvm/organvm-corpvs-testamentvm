# organvm Project Constitution

**Version:** 1.0.0 | **Ratified:** 2026-02-10 | **Last Amended:** 2026-02-10
**Source:** `CLAUDE.md` Key Invariants (lines 28-34) + `08-canonical-action-plan.md` §2 stable consensus

## Core Principles (Articles I-VI)

### I. Registry as Single Source of Truth
All repo state lives in `registry-v2.json`. The registry is never wrong; if reality and registry disagree, update the registry or fix reality. No document, workflow, or agent may claim authoritative repo state outside the registry.

### II. Unidirectional Dependencies
Flow is I->II->III only. No back-edges: ORGAN-III cannot depend on ORGAN-II; ORGAN-II cannot depend on ORGAN-III. ORGAN-IV orchestrates; ORGAN-V documents; ORGAN-VII amplifies. Dependency violations are structural failures, not style issues.

### III. All Eight Organs Visible at Launch
Each organ has at least one representative at launch — flagship (fully documented) or stub (purpose, status, and link to parent org). The eight-organ system must be visible in its entirety; individual organs may launch at different completeness tiers per Amendment A. "Visible" means a grant reviewer navigating all 8 orgs encounters evidence of each organ's existence and purpose, not that every repo is complete.

### IV. Documentation Precedes Deployment
No Phase N+1 until Phase N is complete. Documentation is the deliverable, not an afterthought. Every README is written before the feature it documents is promoted.

### V. Portfolio-Quality Documentation
Every README is a portfolio piece, written for grant reviewers and hiring managers, not just developers. The "Stranger Test" applies: a grant reviewer seeing this for the first time should be convinced.

### VI. Promotion State Machine
Repos follow: LOCAL -> CANDIDATE -> PUBLIC_PROCESS -> GRADUATED -> ARCHIVED. This governs cross-organ promotion. Repo documentation status uses a separate vocabulary: ACTIVE/DEPLOYED/SKELETON/EMPTY. No state may be skipped.

## Amendments (Post-Cross-Validation Consensus)

### Amendment A: Bronze Tier Launch Path
*Source: SC-2, D-08 in `08-canonical-action-plan.md`*

The Bronze Sprint produces the Minimum Viable Launch: 5 flagships (one per organ I-V) + stubs for VI-VII + hardened registry + process essay. Completion is criteria-driven (D-08 success criteria), not time-boxed. "5 Perfect Repos > 44 Mediocre Repos."

### Amendment B: Coordination Overhead Budget
*Source: SC-3, B7 in `06-evaluation-to-growth-analysis.md`*

Budget 10% of phase TE as explicit line item for reconciling parallel AI streams. Coordination overhead is real and must not be hidden inside task estimates.

### Amendment C: Registry Schema Completeness
*Source: SC-1 in `08-canonical-action-plan.md`*

`registry-v2.json` must include `dependencies[]`, `promotion_status`, `tier`, and `last_validated` fields before Phase 2. Schema evolves iteratively during Bronze (fields added as workflows need them, locked after majority of flagships are drafted).

### Amendment D: AI Non-Determinism Acknowledgment
*Source: Meta-finding in `THREE_CLI_COMPARISON_ANALYSIS.md`*

Same inputs produce different strategic outputs across AI models and across time. All AI-generated deliverables require human review. Budget estimates use scenario banding (ranges), not point estimates, to reflect this variance.

## Quality Gates

### Registry Gate
Does this deliverable update `registry-v2.json`? Is the schema satisfied? Are all required fields populated with verified (not aspirational) data?

### Portfolio Gate
Does this README or essay pass the "Stranger Test" (D-08, Copilot validation §7)? Would a grant reviewer seeing this for the first time be convinced? Score >=90/100 on the `01` rubric for flagships.

### Dependency Gate
Does this deliverable respect the I->II->III flow? No back-edges? Cross-references follow the dependency direction?

### Completeness Gate
Are all TBD markers resolved? 0 broken links? No placeholder content in shipped deliverables?

## Governance

This constitution supersedes ad-hoc decision-making for the organvm project. All specifications (`docs/specs/`) and planning documents must be validated against these articles, amendments, and gates before execution.

Amendments require: (1) documented rationale with source citation, (2) human approval by @4444j99, (3) propagation to all affected documents per the E2G coherence review pattern established in `09-corpus-coherence-review.md`.
