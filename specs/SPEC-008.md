# SPEC-008: Evolution & Migration Law

```
Document ID:      SPEC-008
Title:            Evolution & Migration Law
Version:          1.0
Status:           RATIFIED
Layer:            L3A — Structural Architecture
Authoritative:    System Evolution
Parent Specs:     SPEC-000 (System Manifesto), SPEC-003 (Invariant Register), SPEC-005 (Rulebook)
Date Ratified:    2026-03-19
Grounding:        post-flood/specs/SPEC-008/grounding.md
Risk Register:    post-flood/specs/SPEC-008/risk-register.md
Bibliography:     post-flood/specs/bibliography.bib
Principal Author: https://orcid.org/0009-0008-2007-3596
```

---

## 1. Three Change Modes

ORGANVM is an E-type system (Lehman 1980): embedded in the real world, co-evolving with its environment, subject to feedback loops where governance affects what gets built and what gets built affects governance. Every preceding specification assumes a stable system during specification. SPEC-008 breaks this assumption. Its subject is change itself: how the system evolves within its current paradigm, how it migrates between paradigms, and how the rules governing evolution are themselves subject to governed revision (AX-000-005).

Three change modes are defined, corresponding to Kuhn's (1962) normal science / crisis / revolution distinction applied to constitutional architecture.

### EVOL-001: Conservative Refinement

**Definition:** Adding detail within the current constitutional paradigm. The existing organ structure, axiom set, invariant register, and governance rules remain unchanged. All change is puzzle-solving within the established paradigm.

**Examples:** Promoting a repo from CANDIDATE to PUBLIC_PROCESS. Adding a new field to a registry entry. Extending a governance audit check. Refining a quality attribute scenario in SPEC-006. Adding detail to an existing signal class contract in SPEC-007.

**Authorization:** Standard promotion workflow — the state machine's guard conditions (SPEC-004).

**Migration artifact:** None required. Conservative refinements are backward-compatible by definition.

**Temporal constraint:** No cooldown. Conservative refinements can be applied continuously.

**Four-dimensional classification (Mens & Demeyer 2008):**

| Dimension | Value |
|-----------|-------|
| **Temporal** | Unrestricted; no cooldown or sequencing constraint |
| **Object of change** | Fine-grained: individual registry fields, repo metadata, governance audit checks |
| **System properties** | Availability preserved; no global lock; concurrent refinements permitted |
| **Change support** | Automated (metrics refresh, CI) through semi-automated (promotion requiring human sign-off) |

**Lehman's laws served:** Law I (Continuing Change — the system changes to remain satisfactory), Law VI (Continuing Growth — functional content grows), Law VII (Declining Quality — quality defenses maintain standards).

**Traces to:** SPEC-004 LOG-001 through LOG-014 (all promotion transitions), SPEC-005 RULE-018 (Promotion Integrity).

### EVOL-002: Constrained Extension

**Definition:** Adding scope without changing constitutional foundations. The paradigm's boundaries expand, but its core commitments (axioms, constitutional topology, fundamental invariants) remain intact.

**Examples:** Introducing a new organ dictum. Defining a new signal class (SIG-015+). Adding a new invariant to the register (INV-NNN-NNN). Extending the seed.yaml schema with a `contracts` section (SPEC-007 INTF-005). Adding a new governance rule (RULE-019+). Introducing a new entity type at an extension point (SPEC-001 Section 9).

**Authorization:** Requires:
1. **Impact analysis:** Which existing contracts, governance rules, and invariants are affected? The `organvm governance impact` command provides tooling.
2. **Adversarial review:** By a different agent or model than the proposer.
3. **Creator sign-off:** The human principal approves.

**Migration artifact:** An **Impact Assessment** documenting which downstream specs, governance rules, and repo contracts are affected, with explicit disposition for each:

| Disposition | Meaning |
|-------------|---------|
| **Compatible** | Existing artifact works unchanged with the extension |
| **Requires update** | Existing artifact must be modified; modification is backward-compatible |
| **Unaffected** | Existing artifact is outside the extension's scope |

**Temporal constraint:** 7-day review window between proposal and enactment.

**Four-dimensional classification:**

| Dimension | Value |
|-----------|-------|
| **Temporal** | 7-day review window; no more than 3 concurrent constrained extensions (EVOL-010 capacity constraint) |
| **Object of change** | Medium-grained: governance dictums, signal classes, invariants, schema fields |
| **System properties** | Availability preserved; extension operates alongside existing rules during review |
| **Change support** | Semi-automated: impact analysis tooling exists; review and sign-off are manual |

**Lehman's laws served:** Law II (Increasing Complexity — constrained extensions add scope; the review requirement prevents unmanaged complexity growth).

**Traces to:** SPEC-000 Section 9 (Conservative Refinement and Constrained Extension processes), SPEC-001 Section 9 (Leaf Extension and Intermediate Revision).

### EVOL-003: Breaking Revision

**Definition:** Changes requiring migration because the old and new paradigms are potentially incommensurable (Kuhn 1962). Concepts in the old system may have no equivalent in the new one. The flood — the dissolution of 52 repos into 8 organs — was a breaking revision.

**Examples:** Amending an axiom. Restructuring the organ topology. Replacing a fundamental invariant. Introducing a new constitutional era. Weakening a signal class postcondition in ways that break existing consumers. Changing the promotion state machine's top-level state topology.

**Authorization:** The full SPEC-000 Section 9 process:
1. Evidence citation demonstrating the current paradigm is insufficient or incorrect.
2. Change classification as Breaking Revision.
3. New grounding narrative addressing the change.
4. Adversarial review by a different agent or model.
5. Human spot-check of cited sources.
6. Explicit creator sign-off.
7. Review of all downstream specs for consistency.

**Migration artifact:** A **Migration Record** (constitutional artifact with the same authority as a SPEC document). The record is never overwritten, only versioned (per AX-000-007). Contents:

| Section | Content |
|---------|---------|
| **Source paradigm** | Which constitutional version is being departed from |
| **Target paradigm** | Which constitutional version is being adopted |
| **Mapping table** | For each concept in the source paradigm: mapped (equivalent exists), transformed (equivalent exists with modification), dissolved (no equivalent, entity archived), no equivalent (concept absent in target) |
| **Incommensurable concepts** | Explicit enumeration of concepts existing in one paradigm but not the other, with disposition protocols |
| **LIMINAL roster** | Entities entering the LIMINAL holding state pending reclassification |
| **Rollback protocol** | How to revert to the source paradigm if the migration fails |
| **Parallel operation window** | Period during which both paradigms operate simultaneously, with conflict resolution rules |

**Temporal constraint:** No more than 1 concurrent breaking revision (EVOL-010 capacity constraint). The parallel operation window defines the migration duration.

**Four-dimensional classification:**

| Dimension | Value |
|-----------|-------|
| **Temporal** | Unbounded duration; limited to 1 concurrent; parallel operation window defined per migration |
| **Object of change** | Coarse-grained to constitutional: axioms, organ topology, fundamental invariants, SPEC documents |
| **System properties** | Availability maintained through parallel operation; safety maintained through rollback protocol |
| **Change support** | Manual: constitutional revision is a human-governed process |

**Lehman's laws served:** Law I (Continuing Change — sometimes change requires paradigm shift), Law VIII (Feedback System — era transitions are multi-level feedback events).

**Traces to:** SPEC-000 Section 9 (Breaking Revision process), AX-000-005 (Evolutionary Recursivity), AX-000-006 (Topological Plasticity), AX-000-007 (Alchemical Inheritance — prior structural artifacts inform new constructions).

---

## 2. Migration Records

### EVOL-004: Migration Record as Constitutional Artifact

The Migration Record is a constitutional artifact with the same authority as a SPEC document. It is the structured memory of paradigm transition — the document that ensures no future era loses access to the reasoning behind structural change.

The post-flood corpus (`post-flood/`) is the system's first Migration Record, created retroactively. The flood was a breaking revision executed before constitutional governance existed; the post-flood corpus documents the transition after the fact. Future breaking revisions will produce Migration Records prospectively.

### EVOL-005: Incommensurable Concept Handling

When the source and target paradigms are incommensurable (Kuhn 1962), three categories of concept require explicit handling:

**Concepts present in the source but absent in the target.** Repos, entities, or categories without a place in the new structure enter a LIMINAL holding state. LIMINAL is not ARCHIVED (which implies completion) but explicitly transitional: LIMINAL entities must be reclassified, merged, or archived within a defined timeframe.

| Disposition | Protocol | Deadline |
|-------------|----------|----------|
| **Reclassify** | Assign to a target-paradigm category with documented justification | Before parallel operation window closes |
| **Merge** | Combine with another LIMINAL entity into a target-paradigm entity | Before parallel operation window closes |
| **Archive** | Enter ARCHIVED with LINEAGE_TRACE (SIG-014) recording the dissolution | Before parallel operation window closes |

**Concepts present in the target but absent in the source.** New categories, invariants, or governance mechanisms have no historical data. Their initial state is bootstrapped from approximate-mapped source data, with explicit acknowledgment that the mapping is approximate. Per AX-000-007 (Alchemical Inheritance), the old material is prima materia for the new paradigm — transformative inheritance, not preservative.

**Concepts present in both but with changed meaning.** The mapping table records the semantic delta: what the concept meant in the source paradigm, what it means in the target paradigm, and how existing data should be reinterpreted.

### EVOL-006: Rollback Protocol

Every breaking revision must include a rollback protocol — a governed process for reverting to the source paradigm if the migration fails. The protocol specifies:

1. **Rollback trigger conditions:** What constitutes migration failure (invariant violations exceeding threshold, critical governance findings unresolable under the new paradigm, human principal declaring rollback).
2. **Rollback procedure:** How to restore the source paradigm's constitutional artifacts, registry state, and governance rules.
3. **LIMINAL entity disposition on rollback:** LIMINAL entities return to their source-paradigm classification. Entities created under the target paradigm that have no source equivalent enter LIMINAL under the restored source paradigm.
4. **Rollback deadline:** The window during which rollback remains feasible. After the parallel operation window closes and the target paradigm becomes authoritative, rollback requires a new breaking revision.

---

## 3. Lehman's Laws as Constitutional Constraints

ORGANVM codifies Lehman's (1980) eight laws of software evolution as standing constraints on system evolution. These are empirical observations about how E-type systems actually evolve — the system can no more opt out of them than a physical system can opt out of thermodynamics. The evolution law's role is to ensure governance aligns with these dynamics.

### EVOL-007: Complexity Budget (Law II)

**Law II — Increasing Complexity:** Entropy grows with each modification unless actively managed.

Each organ has a complexity budget: maximum repo count, maximum dependency fan-out per repo, and maximum cross-organ edge count. Growth beyond these thresholds is not blocked but triggers governance review — active complexity management rather than passive accumulation.

| Budget Parameter | Initial Value | Trigger |
|------------------|---------------|---------|
| **Max repos per organ** | 30 | Exceeding triggers Constrained Extension (EVOL-002) review |
| **Max dependency fan-out per repo** | 8 | Exceeding triggers architectural review |
| **Max cross-organ edges per organ** | 15 | Exceeding triggers structural interrogation |

Current baseline: ORGAN-III has 28 repos and 28 modules (the most structurally complex organ). These values provide the empirical baseline for setting initial budgets.

**Enforcement:** `organvm governance audit` checks budget compliance. Exceeding a budget parameter generates a warning-level finding; sustained exceedance (2 consecutive audit cycles) escalates to critical.

**Traces to:** Law II (Increasing Complexity), ARCH-011 (organ-level near-decomposability — complexity threatens decomposition quality).

### EVOL-008: Capacity Planning (Law IV)

**Law IV — Conservation of Organizational Stability:** Resource changes do not linearly affect development rate because organizational dynamics absorb the increase.

The system's evolution rate is bounded by constitutional review capacity (the human principal's attention), not by implementation capacity (agent sessions). Adding more agent sessions does not proportionally increase throughput because the human operator remains the bottleneck for constitutional decisions, governance reviews, and promotion sign-offs.

| Constraint | Limit | Rationale |
|------------|-------|-----------|
| **Max concurrent Constrained Extensions** (EVOL-002) | 3 | Each requires human review; more than 3 creates review queue congestion |
| **Max concurrent Breaking Revisions** (EVOL-003) | 1 | Constitutional change requires full attention; concurrent revisions risk incoherence |
| **Conservative Refinements** (EVOL-001) | Unlimited | No constitutional review required |

**Traces to:** Law IV (Conservation of Organizational Stability), ARCH-021 (organizational constriction risk).

### EVOL-009: Growth Governance (Law VI)

**Law VI — Continuing Growth:** Functional content must grow to maintain user satisfaction, because the environment's demands grow and a static system fails to meet them.

SPEC-008 distinguishes two growth types:

| Growth Type | Definition | Governance |
|-------------|-----------|------------|
| **Organic growth** | New repos arising from genuine functional need — a new product, a new infrastructure component, a new creative domain | Standard promotion pathway (EVOL-001) |
| **Proliferative growth** | New repos arising from naming ambiguity, scope confusion, or agent-induced fragmentation — the pre-flood pattern | Triggers excavation audit (`organvm governance excavate`) and potential consolidation |

The flood was a response to proliferative growth. The evolution law prevents recurrence by requiring that new repo creation satisfy a justification test: does this repo serve a function not already served by an existing repo? If the answer is unclear, the repo enters INCUBATOR (14-day TTL) for evaluation.

**Traces to:** Law VI (Continuing Growth), SPEC-004 TIMED-001 (INCUBATOR TTL).

### EVOL-010: Feedback Loop Inventory (Law VIII)

**Law VIII — Feedback System:** E-type evolution is fundamentally a multi-level, multi-loop, multi-agent feedback process.

SPEC-008 requires an enumerated inventory of all system feedback loops, classified by McGinnis's (2011) IAD levels:

| Level | Feedback Loop | Health Metrics |
|-------|---------------|---------------|
| **Operational** | CI pipeline (test → fix → test) | Latency: minutes. Accuracy: binary (pass/fail). Coverage: per-repo. |
| **Operational** | Metrics refresh (compute → propagate → display) | Latency: seconds. Accuracy: schema-validated. Coverage: system-wide. |
| **Operational** | Session debrief (work → reflect → extract → archive) | Latency: per-session. Accuracy: heuristic. Coverage: per-agent. |
| **Collective-choice** | Governance audit (scan → find → report → remediate) | Latency: on-demand. Accuracy: rule-based. Coverage: registry-wide. |
| **Collective-choice** | Promotion cycle (request → evaluate → transition → broadcast) | Latency: days-weeks. Accuracy: guard-based. Coverage: per-repo. |
| **Collective-choice** | Organism gate evaluation (measure → gate → state → display) | Latency: on-demand. Accuracy: threshold-based. Coverage: per-organ. |
| **Constitutional** | Omega scorecard (criterion → evaluate → aggregate → report) | Latency: daily. Accuracy: binary per criterion. Coverage: system-wide. |
| **Constitutional** | SPEC revision (evidence → propose → review → ratify) | Latency: days-weeks. Accuracy: judgment. Coverage: per-spec. |
| **Constitutional** | Era transition (accumulate → declare → draft → migrate → stabilize) | Latency: months-years. Accuracy: judgment. Coverage: system-wide. |

The inventory is a living document maintained alongside `governance-rules.json`. A feedback loop that degrades (latency increases, accuracy decreases, coverage shrinks) triggers a governance finding, treating feedback health as a system invariant subject to the same monitoring as dependency acyclicity or identity persistence.

**Traces to:** Law VIII (Feedback System), INV-000-005 (Observability — feedback loops are diagnostic instruments).

---

## 4. Era Transition Protocol

The most consequential application of the evolution law is the definition of era transitions — the governed process for paradigmatic constitutional change.

### EVOL-011: Era Definition

ORGANVM's current constitutional topology is Era 1: 8 organs, the first axiom set (AX-000-001 through AX-000-009), the first SPEC corpus (SPEC-000 through SPEC-008), the first governance-rules.json. An era is a constitutional epoch — a period during which a specific constitutional topology holds (ONT-021 ERA in SPEC-001).

### EVOL-012: Anomaly Threshold

An era transition is triggered when accumulated anomalies — governance audit findings unresolable within the current paradigm, omega scorecard criteria unsatisfiable by the current architecture, structural tensions that constrained extension cannot accommodate — exceed the estimated migration cost.

The migration cost is estimated from three sources of increasing returns (North 1990):

| Cost Source | Estimation Method | Current Scale |
|-------------|-------------------|---------------|
| **Learning effects** | Session transcript volume referencing current structure; agent context depth | 1,367 sessions, 3.5GB across 3 agents |
| **Coordination effects** | Count of cross-referencing artifacts (seed.yaml files, governance dictums, organ_config.py entries) | 112 seed.yaml files, 18 governance dictums, 3 hardcoded topology references |
| **Adaptive expectations** | External touchpoints (GitHub organizations, portfolio URLs, pitch decks, stakeholder portal) | 3 GitHub orgs, 83 pitch decks, 1 stakeholder portal |

Breaking revisions are justified only when the cost of continuing within the current paradigm (anomaly burden) exceeds the cost of migrating to a new paradigm (learning + coordination + expectation adjustment).

### EVOL-013: Era Transition Protocol

The following protocol governs transitions between constitutional eras:

**Phase 1 — Anomaly accumulation.** Governance audit, omega scorecard regression, or structural interrogation produces findings unresolable within the current paradigm. Findings are documented with explicit classification: *within-paradigm* (addressable by EVOL-001/002) versus *paradigm-straining* (requiring EVOL-003).

**Phase 2 — Crisis declaration.** The human principal declares constitutional crisis, freezing EVOL-002 (Constrained Extension) and EVOL-003 (Breaking Revision) operations. EVOL-001 (Conservative Refinement) continues to maintain system health during the crisis.

**Phase 3 — Paradigm drafting.** A new constitutional framework is proposed: revised axioms, revised organ topology (if applicable), revised invariants, revised governance rules. The draft operates as a candidate paradigm — it has no authority until enacted.

**Phase 4 — Migration Record authoring.** The mapping between old and new paradigms is exhaustively documented per EVOL-004/005. Incommensurable concepts are enumerated. LIMINAL roster is defined. Rollback protocol is specified per EVOL-006.

**Phase 5 — Parallel operation.** Both paradigms operate simultaneously for a defined window. Conflict resolution:
- Newly initiated work follows the new paradigm.
- Already-started work completes under the old paradigm.
- If old and new paradigms produce contradictory governance findings for the same entity, the old-paradigm finding takes precedence for already-started work; the new-paradigm finding takes precedence for newly initiated work.

**Phase 6 — Cutover.** At the end of the parallel operation window, the new paradigm becomes authoritative. LIMINAL entities are reclassified or archived per EVOL-005. The old paradigm is archived as a historical version (per AX-000-007, never discarded).

**Phase 7 — Post-transition stabilization.** A soak-like period during which the new paradigm is monitored for unforeseen anomalies. Expedited rollback remains available during stabilization. Stabilization ends when the omega scorecard under the new paradigm matches or exceeds the pre-crisis score under the old paradigm.

**Self-reference:** The era transition protocol is itself subject to governed evolution (AX-000-005). Future eras may amend this protocol — but the amendment must follow the current era's protocol for breaking revision. This is the recursion that AX-000-005 demands.

**Traces to:** Kuhn 1962 (normal science / crisis / revolution), North 1990 (path dependence and migration cost), AX-000-006 (Topological Plasticity), SPEC-000 Section 9 (amendment process).

---

## 5. Contestation Disclosures

### 5.1 Kuhn's Incommensurability Applied to Constitutional Revision

**Status:** ADAPTED (risk register).

Kuhn's incommensurability thesis was formulated for scientific paradigms — frameworks of theory, method, and exemplar that define entire fields of inquiry. Applying it to a software system's constitutional architecture is a significant extension. The justification is structural: ORGANVM's constitutional paradigm (axioms, invariants, organ topology, governance rules) defines what counts as a valid system component, what counts as a valid change, and what counts as a valid outcome. When the paradigm shifts, these definitions change. The extension is acknowledged: ORGANVM does not claim to be a science, and its paradigm shifts lack the sociological dynamics of scientific revolutions (there is no community of competing researchers). What is preserved from Kuhn is the formal structure of the normal/revolutionary distinction and the practical consequence of incommensurability for migration planning.

### 5.2 Single-Operator Amendment Process

**Status:** ADAPTED (risk register).

Multi-stakeholder institutions (North 1990) have political processes for constitutional amendment — legislatures, courts, referenda. ORGANVM lacks this: the human operator is simultaneously legislator, executive, and governed subject. The amendment process defined in SPEC-000 Section 9 substitutes adversarial review by different agents/models for the political process that would exist in a multi-stakeholder system. This substitution provides structural review but not the diversity of interests that political processes represent.

### 5.3 Migration Cost Model

**Status:** NOVEL (risk register).

The three-source migration cost model (learning + coordination + expectations) synthesizes North's institutional economics into a threshold function for determining when breaking revision is justified. Each individual cost source is directly grounded in North's theory; the synthesis into a single threshold function is ORGANVM's novel contribution. The model is qualitative (costs are estimated and compared, not computed to precision); quantification is a future refinement.

### 5.4 Four-Dimensional Taxonomy as Prescriptive Framework

**Status:** ADAPTED (risk register).

Mens and Demeyer's (2008) four-dimensional taxonomy was developed for analyzing software evolution empirically — describing what changes occur. SPEC-008 inverts this into a prescriptive classification — specifying what changes are permitted. The inversion is justified because ORGANVM's governance is explicitly constitutional: it must specify what changes are permitted, not merely observe what changes occur. Each evolution operation (EVOL-001/002/003) is classified along all four dimensions, providing a complete operational specification.

---

## 6. Evolution Constraints

SPEC-008 may be amended through the following governed process only. As the specification governing system evolution, SPEC-008's own evolution constraints are the most self-referential in the corpus. Per AX-000-005, the rules for changing rules are themselves changeable, but only through governed processes.

### 6.1 Amendment Types

| Type | Definition | Requirements |
|------|-----------|-------------|
| **Conservative Refinement** | Adjusts budget thresholds (EVOL-007), refines the feedback loop inventory (EVOL-010), adds detail to migration protocols. Does not add new EVOL identifiers or change the three-mode structure. | Adversarial review + creator sign-off |
| **Constrained Extension** | Adds new evolution operations (new EVOL-NNN identifiers), new budget parameters, or new feedback loops to the inventory. Must preserve the three-mode structure (conservative/constrained/breaking). | Adversarial review + impact assessment on all upstream specs (SPEC-000 through SPEC-007) + creator sign-off |
| **Mode Restructuring** | Changes the three-mode structure (e.g., adding a fourth mode, merging two modes, changing mode boundaries). | New grounding narrative + adversarial review + human spot-check + review of all specs + creator sign-off |
| **Breaking Revision** | Changes the era transition protocol (EVOL-013), changes the migration cost model (EVOL-012), or modifies the Lehman Law enforcement mechanisms in ways that weaken constitutional constraints. | Full SPEC-000 Section 9 process (this is itself a breaking revision requiring a Migration Record) |

### 6.2 Permanent Identifiers

EVOL identifiers (EVOL-001 through EVOL-013) are permanent. Removed items have their identifiers retired, not reassigned.

### 6.3 Versioning

The original SPEC-008 is never overwritten. Amendments are versioned: SPEC-008-v1.1, v1.2, etc.

---

## 7. Traceability

### 7.1 Upward Traceability (to SPEC-000)

| SPEC-000 Element | SPEC-008 Grounding |
|------------------|--------------------|
| AX-000-001 (Ontological Primacy) | EVOL-005 — incommensurable concepts must be ontologically classified before behavioral rules apply in the new paradigm |
| AX-000-002 (Organizational Closure) | EVOL-013 Phase 5 — parallel operation maintains constitutive processes during transition |
| AX-000-004 (Constitutional Governance) | EVOL-001/002/003 — every change mode has explicit authorization requirements |
| AX-000-005 (Evolutionary Recursivity) | Section 6 — SPEC-008 itself evolves through governed revision; EVOL-013 is self-referential |
| AX-000-006 (Topological Plasticity) | EVOL-011/012/013 — era transitions are the mechanism for governed topological mutation |
| AX-000-007 (Alchemical Inheritance) | EVOL-004 — Migration Records are constitutional artifacts preserving structural history; old paradigms archived, never discarded |
| AX-000-008 (Multiplex Flow Governance) | EVOL-012 — coordination effects count cross-referencing artifacts across all graph layers |
| INV-000-001 (Dependency Acyclicity) | EVOL-003 — breaking revisions must not create dependency cycles in the transition |
| INV-000-003 (Identity Persistence) | EVOL-005 — LIMINAL entities retain UIDs; no identity destruction during migration |
| INV-000-004 (Constitutional Supremacy) | EVOL-008 — capacity constraint ensures constitutional review is not overwhelmed |
| INV-000-005 (Observability) | EVOL-010 — feedback loop inventory as standing governance instrument |

### 7.2 Lateral Traceability

| Peer Spec | Connection |
|-----------|-----------|
| SPEC-001 (Ontology Charter) | ONT-021 (ERA) — the entity type for constitutional epochs; Section 9 — taxonomy evolution through extension points |
| SPEC-002 (Primitive Register) | Section 6 — primitive register evolution governed by SPEC-008's three modes |
| SPEC-003 (Invariant Register) | Section 6 — invariant addition/refinement governed by SPEC-008; EVOL-007 complexity budget is a standing constraint |
| SPEC-004 (Logical Specification) | Section 6 — statechart amendments governed by SPEC-008; EVOL-001 covers promotion transitions |
| SPEC-005 (Rulebook) | Section 7 — rule addition/retraction governed by SPEC-008; EVOL-002 covers new rule introduction |
| SPEC-006 (Architecture Document) | ARCH-034 — evolutionary capacity scenario depends on SPEC-008 protocols; ARCH-042 — layer dependency changes are breaking revisions |
| SPEC-007 (Interface Contract Spec) | INTF-001 — removing produces edge requires SPEC-008 migration protocol; INTF-003 — contract evolution across promotion follows EVOL-001 |

### 7.3 Downward Traceability (to implementation)

| SPEC-008 Element | Current Code Location | Alignment |
|------------------|-----------------------|-----------|
| Three change modes (Section 1) | SPEC-000 Section 9 (prose) | ALIGNED (procedural — modes defined in prose, not in code) |
| Migration Records (Section 2) | `post-flood/` (retroactive first record) | DRIFT — post-flood corpus is unstructured; no Migration Record schema |
| Complexity budget (EVOL-007) | Not implemented | MISSING — no automated budget check in governance audit |
| Capacity planning (EVOL-008) | Not implemented | MISSING — no concurrent-revision tracking |
| Growth governance (EVOL-009) | `governance/excavation.py` (detects proliferative patterns) | PARTIAL — excavation detects but does not enforce justification test |
| Feedback loop inventory (EVOL-010) | Distributed across engine, dashboard, MCP server | DRIFT — loops exist but are not inventoried as governed instruments |
| Era model (EVOL-011) | `organ_config.py` (hardcoded topology) | DRIFT — AX-000-006 conflict; era model requires data-driven topology |
| Migration cost model (EVOL-012) | Not implemented | MISSING — qualitative model not yet operationalized |
| Era transition protocol (EVOL-013) | Not implemented | MISSING — no automated support for parallel operation or cutover |

### 7.4 Academic Lineage

| SPEC-008 Element | Traditions | Key Sources |
|------------------|-----------|-------------|
| E-type classification, Laws I-VIII | Software evolution | Lehman 1980 |
| Four-dimensional change taxonomy | Software evolution | Mens & Demeyer 2008 |
| Path dependence, migration cost | Institutional economics | North 1990 |
| Normal/revolutionary distinction | Philosophy of science | Kuhn 1962 |
| Three change modes | Novel synthesis (grounded in above) | — |
| Migration cost model | Novel (synthesizes North's three increasing-returns sources) | — |

Full grounding narrative: `post-flood/specs/SPEC-008/grounding.md` (5,588 words)
Full risk register: `post-flood/specs/SPEC-008/risk-register.md` (6 classified claims)
Full bibliography: `post-flood/specs/bibliography.bib`
