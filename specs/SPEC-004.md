# SPEC-004: Logical Specification

```
Document ID:      SPEC-004
Title:            Logical Specification
Version:          1.1
Status:           RATIFIED (G3 review incorporated)
Layer:            L2 — Constitutional Logic
Authoritative:    Governance Behavior
Parent Specs:     SPEC-000 (System Manifesto), SPEC-003 (Invariant Register)
Date Ratified:    2026-03-19
Grounding:        post-flood/specs/SPEC-004/grounding.md
Risk Register:    post-flood/specs/SPEC-004/risk-register.md
Inventory:        post-flood/specs/SPEC-004/inventory.md
Bibliography:     post-flood/specs/bibliography.bib
Principal Author: https://orcid.org/0009-0008-2007-3596
```

---

## 1. Promotion Statechart

The promotion state machine governs the lifecycle of every registered repository. This section replaces the flat `TRANSITIONS` dict in `governance/state_machine.py` with a Harel statechart specification (Harel 1987) that serves as the single, canonical behavioral specification. The statechart is loaded from `governance-rules.json`; the engine executes it. This resolves the AX-000-005 DRIFT problem identified in SPEC-003's inventory: two sources of truth for the same behavioral specification, diverging in expressiveness and disconnected in implementation.

### 1.1 Top-Level States

The statechart contains six top-level states. INCUBATOR, CANDIDATE, and PUBLIC_PROCESS contain internal structure (OR-decomposition, AND-decomposition, or both). LOCAL, GRADUATED, and ARCHIVED are atomic.

```
PROMOTION_STATECHART
├── INCUBATOR  [timed, OR-decomposed]
├── LOCAL      [atomic]
├── CANDIDATE  [AND-decomposed]
├── PUBLIC_PROCESS  [OR-decomposed]
├── GRADUATED  [atomic, terminal except ARCHIVED]
└── ARCHIVED   [atomic, absorbing]
```

### 1.2 INCUBATOR: OR-Decomposition with Clock Guard

*Constitutional authority note:* INCUBATOR is a pre-constitutional state defined in `governance-rules.json` and `state_machine.py` but not explicitly named in SPEC-000's promotion description. Its constitutional authority derives from AX-000-004 (Constitutional Governance — every component requires authorization) and the governance-rules.json `state_machine.transitions` section. A Conservative Refinement to SPEC-000 should formalize INCUBATOR in the promotion sequence.

INCUBATOR repos have a 14-day TTL (governance-rules.json TTL rule, derives from AX-000-004). The internal structure tracks progress toward graduation.

```
INCUBATOR [OR]
├── INCUBATOR.initializing     ← default entry
├── INCUBATOR.configuring      ← seed.yaml + schema defined
└── INCUBATOR.ready            ← epistemic boundary + DAG edges declared
```

**Clock:** `clk_incubator` resets on entry to INCUBATOR. Guard `clk_incubator > 14` triggers mandatory transition to LOCAL or ARCHIVED (see Section 3, TIMED-001).

### 1.3 CANDIDATE: AND-Decomposition for Parallel Readiness

The three promotion prerequisites -- CI workflow, platinum status, and active implementation -- are independent, concurrent requirements. An AND-decomposed statechart models this with three parallel regions, replacing the ad-hoc multi-field guard logic currently scattered across `governance/rules.py` and `governance/audit.py`.

```
CANDIDATE [AND]
├── Region_CI:           {pending, configured}
├── Region_Platinum:     {pending, certified}
└── Region_Impl:         {pending, active}
```

The composite state CANDIDATE is exitable (transition to PUBLIC_PROCESS enabled) when all three regions are in their terminal sub-state: `Region_CI = configured AND Region_Platinum = certified AND Region_Impl = active`.

**History state:** H* (deep history). When a repo is demoted from PUBLIC_PROCESS back to CANDIDATE, re-entry via H* preserves which regions were already satisfied. A repo demoted because it lost CI configuration re-enters with Region_Platinum and Region_Impl preserved, needing only to re-satisfy Region_CI. This eliminates redundant re-evaluation.

### 1.4 PUBLIC_PROCESS: OR-Decomposition with Soak Test

```
PUBLIC_PROCESS [OR]
├── PUBLIC_PROCESS.review        ← default entry; governance audit in progress
├── PUBLIC_PROCESS.soak_testing  ← 30-day stability observation
└── PUBLIC_PROCESS.ready         ← soak complete, all criteria met
```

**Clock:** `clk_soak` resets on entry to `PUBLIC_PROCESS.soak_testing`. Any instability event (failing CI, critical audit finding) resets `clk_soak` to zero. Transition to `PUBLIC_PROCESS.ready` requires `clk_soak >= 30` (see Section 3, TIMED-002).

### 1.5 Transitions Table

Each transition carries a LOG identifier for traceability, a source state, a target state, a guard condition, and generated events.

| ID | Source | Target | Guard | Events Generated |
|----|--------|--------|-------|-----------------|
| LOG-001 | INCUBATOR.ready | LOCAL | `schema_defined AND dag_edges_declared AND clk_incubator <= 14` | `promotion_changed(repo, LOCAL)` |
| LOG-002 | INCUBATOR.* | ARCHIVED | `clk_incubator > 14 AND NOT ready` | `ttl_eviction(repo)` |
| LOG-003 | LOCAL | CANDIDATE | `seed_yaml_valid` | `promotion_changed(repo, CANDIDATE)` |
| LOG-004 | LOCAL | ARCHIVED | `operator_decision` | `archived(repo)` |
| LOG-005 | CANDIDATE [all regions terminal] | PUBLIC_PROCESS.review | `Region_CI = configured AND Region_Platinum = certified AND Region_Impl = active` | `promotion_changed(repo, PUBLIC_PROCESS)` |
| LOG-006 | CANDIDATE | LOCAL | `demotion_justified` | `demotion(repo, LOCAL)` |
| LOG-007 | CANDIDATE | ARCHIVED | `operator_decision` | `archived(repo)` |
| LOG-008 | PUBLIC_PROCESS.review | PUBLIC_PROCESS.soak_testing | `governance_audit_passed AND no_critical_findings` | `soak_started(repo)` |
| LOG-009 | PUBLIC_PROCESS.soak_testing | PUBLIC_PROCESS.ready | `clk_soak >= 30 AND ci_stable` | `soak_complete(repo)` |
| LOG-010 | PUBLIC_PROCESS.soak_testing | PUBLIC_PROCESS.review | `instability_detected` | `soak_reset(repo)` |
| LOG-011 | PUBLIC_PROCESS.ready | GRADUATED | `omega_criteria_met AND no_critical_findings` | `promotion_changed(repo, GRADUATED)` |
| LOG-012 | PUBLIC_PROCESS | CANDIDATE [H*] | `demotion_justified` | `demotion(repo, CANDIDATE)` |
| LOG-013 | PUBLIC_PROCESS | ARCHIVED | `operator_decision` | `archived(repo)` |
| LOG-014 | GRADUATED | ARCHIVED | `operator_decision OR dissolution_protocol` | `archived(repo)` |

### 1.6 Broadcast Events

State transitions generate broadcast events visible to all parallel regions within the statechart and to external listeners registered through `seed.yaml` event subscriptions. The current `emit_promotion_event()` function in `state_machine.py` is a partial implementation of this broadcast; the statechart formalization makes broadcast a structural consequence of transition semantics rather than an ad-hoc function call.

Event routing follows the `produces`/`consumes` edges declared in `seed.yaml`. When a repo transitions to GRADUATED, its downstream dependents receive a `promotion_changed` event, which may trigger re-evaluation of their own guard conditions (e.g., a dependency requirement that all upstream repos be at least PUBLIC_PROCESS).

---

## 2. Temporal Properties

Governance invariants are expressed as linear temporal logic (LTL) formulas (Pnueli 1977) over execution traces of the promotion statechart. Each formula carries a TEMP identifier, a natural-language statement, and a formal LTL expression. The variables range over repositories (r), states (s), and events (e).

### TEMP-001: Dependency Acyclicity (Safety)

**Statement:** The dependency graph must never contain a cycle.

**LTL:**
```
G(not exists(r : Repo) . reachable(r, r, G_dep))
```

where `reachable(a, b, G)` is the transitive closure of edges in graph G. This captures cycles of ALL lengths (not just mutual 2-cycles). A→B→C→A is detected because `reachable(A, A, G_dep)` holds via the path A→B→C→A.

**Classification:** Safety property. "Nothing bad happens." Enforced structurally by `validate_dag_invariant()` (topological sort) on every registry load. The LTL formulation enables trace-based verification: has any observed sequence of dependency-edge additions ever created a cycle, even transiently?

**Traces to:** AX-000-004 (Constitutional Governance), AX-000-008 (Multiplex Flow Governance — dependency layer acyclicity), INV-000-001 (Dependency Acyclicity).

### TEMP-002: Promotion Resolution (Bounded Liveness)

**Statement:** Every promotion request must eventually be resolved -- the repo advances, is demoted, or the request is withdrawn.

**LTL:**
```
G(promotion_requested(r) -> F(promoted(r) OR demoted(r) OR request_withdrawn(r)))
```

**Classification:** Liveness property. "Something good eventually happens." Without this property, the system permits indefinite limbo -- a repo in CANDIDATE that is never reviewed, never promoted, and never demoted. The property does not specify a time bound (see TIMED-003 for calendar-bounded variants); it asserts that resolution must occur in finite time.

**Traces to:** AX-000-004 (Constitutional Governance).

### TEMP-003: No State Skipping (Safety)

**Statement:** Every promotion must traverse the state machine's defined transitions. No state may be bypassed.

**LTL:**
```
G(in_state(r, s1) AND next_state(r, s2) -> valid_transition(s1, s2))
```

**Classification:** Safety property. `valid_transition(s1, s2)` is true if and only if the pair (s1, s2) appears in the transitions table (Section 1.5). This prevents direct jumps from LOCAL to PUBLIC_PROCESS (bypassing CANDIDATE) or from CANDIDATE to GRADUATED (bypassing PUBLIC_PROCESS).

**Traces to:** RR-5 (Promotion Integrity), INV-000-004 (Constitutional Supremacy).

### TEMP-004: Guard Satisfaction (Safety)

**Statement:** No transition may fire unless all its guard conditions are satisfied.

**LTL:**
```
G(transition_fires(r, LOG-n) -> guard_satisfied(r, LOG-n))
```

**Classification:** Safety property. This is the formal expression of the gap between topological legality (the current `check_transition()` function) and semantic legality (the guard conditions in the transitions table). A transition that is topologically valid but whose guard is unsatisfied must not fire.

**Traces to:** SPEC-000 Section 4 (promotion_criteria).

### TEMP-005: Staleness Eviction (Bounded Liveness)

**Statement:** Every repo must show activity within 90 days. Inactivity beyond this threshold must result in review or archival within 30 days.

**LTL:**
```
G(days_since_activity(r) > 90 -> F_within(30, reviewed(r) OR archived(r)))
```

**Classification:** Safety-liveness hybrid. The 90-day threshold is a safety condition (the bad state of staleness should not persist); the 30-day response window is a bounded liveness condition (remediation must occur within a fixed interval). `F_within(k, phi)` is syntactic sugar for the timed-automata formalization in Section 3.

**Traces to:** governance-rules.json TTL rule (derives from AX-000-004), AX-000-004 (Constitutional Governance).

### TEMP-006: Constitutional Supremacy (Safety)

**Statement:** No organ dictum may contradict a system axiom. No repo rule may contradict an organ dictum.

**LTL:**
```
G(forall d : Dictum, a : Axiom . NOT contradicts(d, a))
G(forall rr : RepoRule, od : OrganDictum . NOT contradicts(rr, od))
```

**Classification:** Safety property. The predicate `contradicts(x, y)` determines whether a lower-level rule's effect violates a higher-level rule's intent. The predicate's formal definition is a governance design problem (deferred to SPEC-005's defeasibility framework); LTL provides the temporal frame requiring the predicate to hold at all times.

**Traces to:** INV-000-004 (Constitutional Supremacy), AX-000-004 (Constitutional Governance).

### TEMP-007: Identity Persistence (Safety)

**Statement:** No entity's canonical UID may be destroyed. Entities may be archived, dissolved, merged, or split, but their identity must be preserved.

**LTL:**
```
G(exists_entity(uid) -> G(identity_record_exists(uid)))
```

**Classification:** Safety property. Once an entity has existed (`exists_entity(uid)` becomes true), its identity record must remain forever (`G` nested within `G`). The entity's state may change (ACTIVE to ARCHIVED), but the record persists.

**Traces to:** INV-000-003 (Identity Persistence), AX-000-007 (Alchemical Inheritance).

---

## 3. Timed Constraints

Clock-based constraints formalize the temporal dimension that plain statecharts and LTL lack. Following Alur and Dill (1994), each constraint specifies a clock variable, its reset conditions, and the guard expression that governs transitions. ORGANVM's temporal constraints are calendar-based (discrete days), not continuous real-valued -- a coarser granularity than Alur and Dill's theory supports, but the conceptual framework (clocks, guards, resets) applies directly.

### TIMED-001: INCUBATOR TTL

**Clock:** `clk_incubator`
**Reset:** On entry to INCUBATOR state.
**Guard:** `clk_incubator > 14 -> MUST transition(INCUBATOR, LOCAL) OR transition(INCUBATOR, ARCHIVED)`
**Reset condition:** Clock is never reset while in INCUBATOR -- it counts continuously from entry.
**Granularity:** Days (discrete).

**Semantics:** An INCUBATOR repo has 14 calendar days to graduate to LOCAL or be archived. Expiration without graduation triggers a mandatory transition. The guard is an obligation, not a permission: the system must act when the clock exceeds 14.

**Traces to:** governance-rules.json TTL rule (derives from AX-000-004), LOG-001, LOG-002.

### TIMED-002: Soak Test Duration

**Clock:** `clk_soak`
**Reset:** On entry to `PUBLIC_PROCESS.soak_testing`. Additionally reset to zero on any instability event (failing CI run, critical audit finding, unresolved regression).
**Guard:** `clk_soak >= 30 -> MAY transition(PUBLIC_PROCESS.soak_testing, PUBLIC_PROCESS.ready)`
**Granularity:** Days (discrete, continuous counting -- no pauses).

**Semantics:** The soak test requires 30 continuous days of stability. Any instability resets the clock. The guard is a permission, not an obligation: reaching 30 days enables the transition but does not require it -- additional review may be warranted.

**Traces to:** Omega criterion #1 (soak test), LOG-008, LOG-009, LOG-010.

### TIMED-003: Staleness Detection

**Clock:** `clk_activity(r)` -- per-repository.
**Reset:** On any qualifying activity event (commit, CI run, registry update, governance action).
**Guard:** `clk_activity(r) > 90 -> TRIGGERS staleness_warning(r)`
**Escalation guard:** `clk_activity(r) > 120 -> MUST reviewed(r) OR archived(r)`
**Granularity:** Days (discrete).

**Semantics:** Two-stage temporal constraint. The 90-day threshold triggers a warning (TEMP-005's bounded liveness begins). At 120 days (90 + 30-day response window), remediation becomes mandatory. This formalizes the `F_within(30, ...)` construct from TEMP-005 as a concrete clock guard.

**Traces to:** governance-rules.json TTL rule (derives from AX-000-004), audit_thresholds.warning.stale_repo_days.

### TIMED-004: Promotion Request Timeout

**Clock:** `clk_request(r)` -- per-repository, per-request.
**Reset:** On filing of a promotion request.
**Guard:** `clk_request(r) > 60 -> TRIGGERS request_stale_warning(r)`
**Escalation guard:** `clk_request(r) > 90 -> request_withdrawn(r) OR reviewed(r)`
**Granularity:** Days (discrete).

**Semantics:** Operationalizes TEMP-002 (Promotion Resolution). A promotion request open for more than 60 days generates a warning; more than 90 days requires explicit resolution (withdrawal or review). This prevents indefinite limbo in the CANDIDATE or PUBLIC_PROCESS states.

**Traces to:** TEMP-002 (Promotion Resolution).

---

## 4. Conformance Checking

Conformance checking (van der Aalst 2016) provides the verification layer: comparing actual system behavior, as recorded in event logs, against the specification defined in Sections 1-3. The methodology detects deviations between intended and observed governance behavior.

### 4.1 Event Log Sources

ORGANVM produces three event log sources suitable for conformance checking:

| Source | Format | Content | Conformance-Ready |
|--------|--------|---------|-------------------|
| `claims.jsonl` | Append-only JSONL | Agent session punch-in/out, operations performed, timestamps | YES |
| `ontologia/events.jsonl` | Append-only JSONL | Entity lifecycle events: creation, state change, hierarchy modification | YES |
| Git commit history | Git log (implicit) | Every modification to registry, governance rules, seed files, code | PARTIAL -- requires extraction into standardized event format |
| Promotion history | Registry `note` field | State transition history | NO -- freetext, not structured events |

**Implementation prerequisite:** Promotion state transitions must be recorded as structured events in `ontologia/events.jsonl` (entity_uid, from_state, to_state, timestamp, agent_handle, guard_evaluation_result). The current freetext `note` field is insufficient for conformance analysis.

### 4.2 Alignment Methodology

Van der Aalst's alignment technique maps each observed trace (sequence of promotion events for a repository) to the closest trace permitted by the statechart model. The alignment identifies four deviation types, each with a governance interpretation:

| Deviation | Alignment Type | Governance Interpretation |
|-----------|---------------|--------------------------|
| Observed event matches model | Synchronous move | System behaving as specified |
| Event observed that model does not permit | Log move (insertion) | Unauthorized transition -- governance violation |
| Model transition not observed | Model move (skip) | Skipped state -- bypassed required intermediate stage |
| Observed event fills structural slot but matches no model event | Substitution | Variant -- transition type not in specification |

### 4.3 Quality Metrics

Two quality dimensions evaluate conformance:

**Fitness** measures how well observed traces can be reproduced by the statechart model. Fitness = 1.0 means every observed promotion sequence is a valid trace of the model. Low fitness indicates governance violations (the system is executing transitions the model forbids).

**Precision** measures how tightly the model constrains behavior. Precision = 1.0 means the model permits only traces that have been observed. Low precision indicates over-specification (the model allows transitions that never occur in practice). For ORGANVM, moderate precision is expected: demotion paths (LOG-006, LOG-012) and dissolution (LOG-014) may be rarely exercised during active development. The precision gap is informative, not alarming.

### 4.4 Organizational Mining

Van der Aalst's organizational perspective analyzes who performs which governance operations. Applied to ORGANVM's multi-agent environment, organizational mining on `claims.jsonl` reveals:

- Which agents trigger promotions vs. which create governance drift
- Whether certain agents systematically skip guard-condition verification
- Agent-specific behavioral patterns across sessions

This is an empirical complement to the normative specification, not a replacement. The statechart defines what should happen; organizational mining reveals what does happen and who does it.

---

## 5. Contestation Disclosures

### 5.1 Statechart Complexity vs. System Scale

**Status:** ADAPTED (risk register claim #6)

The full Harel statechart formalism (AND-decomposition, OR-decomposition, history states, broadcast) was designed for avionics and embedded systems with combinatorial state spaces. ORGANVM has 6 top-level states and 14 transitions. The overhead of the full formalism may exceed the complexity it manages at current scale.

**Mitigation:** The formalism is applied selectively. CANDIDATE receives AND-decomposition because three independent readiness dimensions genuinely compose in parallel. PUBLIC_PROCESS receives OR-decomposition because the soak test is a sequential sub-process. LOCAL, GRADUATED, and ARCHIVED remain atomic. The formalism is used where it resolves concrete problems (the AX-000-005 DRIFT, scattered guard logic, lost sub-state on demotion), not applied uniformly for theoretical completeness.

### 5.2 Pi-Calculus Applicability

**Status:** ADAPTED (risk register claim #2)

ORGANVM's current inter-organ communication is unidirectional broadcast (fire-and-forget), not the bidirectional synchronization that pi-calculus natively models. A CCS-like fragment (Milner's earlier, simpler calculus without mobility) suffices for the current architecture.

**Scope:** The pi-calculus is held in reserve for future extensions where dynamic subscription, channel mobility, or bidirectional synchronization become operationally necessary. SPEC-004 does not impose pi-calculus semantics on the current design.

### 5.3 Discrete vs. Continuous Time

**Status:** ADAPTED (risk register claim #4)

Alur and Dill's timed automata use continuous real-valued clocks. ORGANVM's temporal constraints are calendar-based (discrete days). The region construction -- Alur and Dill's central technical result for making continuous-time verification decidable -- is more powerful than ORGANVM currently needs. The theory guarantees that even when finer-grained temporal constraints are introduced (hourly CI checks, real-time soak monitoring), the verification machinery remains decidable.

---

## 6. Evolution Constraints

SPEC-004 may be amended through the following governed process only. This process is self-contained -- it does not depend on any downstream spec for its authority.

### 6.1 Amendment Types

| Type | Definition | Requirements |
|------|-----------|-------------|
| **Conservative Refinement** | Adds sub-states, guards, or temporal properties without changing the top-level state topology. | Adversarial review + creator sign-off |
| **Constrained Extension** | Adds new top-level states or new transition types. Must preserve all existing temporal properties (TEMP-001 through TEMP-007). | Adversarial review + impact assessment on SPEC-005 (Rulebook) and SPEC-003 (Invariant Register) + creator sign-off |
| **Breaking Revision** | Removes states, removes transitions, or changes guard semantics in ways that invalidate existing temporal properties. | New grounding narrative + adversarial review + human spot-check of cited sources + review of all downstream specs + creator sign-off |

### 6.2 Permanent Identifiers

LOG identifiers (LOG-001 through LOG-014) and TEMP identifiers (TEMP-001 through TEMP-007) and TIMED identifiers (TIMED-001 through TIMED-004) are permanent. Removed items have their identifiers retired, not reassigned.

### 6.3 Versioning

The original SPEC-004 is never overwritten. Amendments are versioned: SPEC-004-v1.1, v1.2, etc.

---

## 7. Traceability

### 7.1 Upward Traceability (to SPEC-000)

| SPEC-000 Element | SPEC-004 Grounding |
|------------------|--------------------|
| AX-000-001 (Ontological Primacy) | TEMP-007 -- entities must exist before behavioral rules apply |
| AX-000-002 (Organizational Closure) | Section 1.6 -- broadcast events propagate within the constitutive process network |
| AX-000-004 (Constitutional Governance) | TEMP-003, TEMP-004 -- no transition without valid path and satisfied guards |
| AX-000-005 (Evolutionary Recursivity) | Section 6 -- the statechart itself evolves through governed revision |
| AX-000-007 (Alchemical Inheritance) | TEMP-007 -- identity records persist through archival and dissolution |
| AX-000-008 (Multiplex Flow Governance) | Section 1.6 -- broadcast events are a distinct flow type from dependencies |
| INV-000-001 (Dependency Acyclicity) | TEMP-001 -- formalized as LTL safety property |
| INV-000-002 (Governance Reachability) | LOG-001 through LOG-014 -- every state is reachable from a governed transition |
| INV-000-003 (Identity Persistence) | TEMP-007 -- formalized as LTL safety property |
| INV-000-004 (Constitutional Supremacy) | TEMP-006 -- formalized as LTL safety property |
| INV-000-005 (Observability) | Section 4 -- conformance checking makes behavioral gaps observable |

### 7.2 Lateral Traceability

| Peer Spec | Connection |
|-----------|-----------|
| SPEC-001 (Ontology Charter) | Statechart states correspond to State (PRIM-005) values of REPO entities (ONT-006) |
| SPEC-002 (Primitive Register) | Transitions are Events (PRIM-004); guards are Constraints (PRIM-006); statechart states are States (PRIM-005) |
| SPEC-003 (Invariant Register) | TEMP-001 through TEMP-007 formalize invariants declared in SPEC-003 |
| SPEC-005 (Rulebook) | Guards reference rules decomposed and classified in SPEC-005 |

### 7.3 Downward Traceability (to implementation)

| SPEC-004 Element | Current Code Location | Alignment |
|------------------|-----------------------|-----------|
| Statechart (Section 1) | `governance/state_machine.py` TRANSITIONS dict | CONFLICT -- flat dict, no hierarchy/parallelism/guards |
| Transitions table (Section 1.5) | `governance-rules.json` state_machine section | DRIFT -- contains transitions but engine ignores it |
| Guard conditions | `governance-rules.json` promotion_criteria | DRIFT -- criteria exist but not attached to transitions |
| Broadcast events | `state_machine.py` emit_promotion_event() | PARTIAL -- manual invocation, not structural |
| LTL properties (Section 2) | English prose in governance-rules.json + scattered conditionals | DRIFT -- not machine-checkable |
| Timed constraints (Section 3) | `governance/audit.py` TTL checks | PARTIAL -- checks exist but not formalized as clock automata |
| Conformance checking (Section 4) | Not implemented | MISSING |
| Event log (structured promotions) | Registry `note` field (freetext) | DRIFT -- not structured events |

### 7.4 Academic Lineage

| SPEC-004 Element | Traditions | Key Sources |
|------------------|-----------|-------------|
| Promotion statechart | Hierarchical reactive systems | Harel 1987 |
| LTL temporal properties | Temporal logic of programs | Pnueli 1977 |
| Timed constraints | Real-time verification | Alur & Dill 1994 |
| Conformance checking | Process mining | van der Aalst 2016 |
| Inter-organ communication model | Process algebra | Milner 1999 (reserved for future) |

Full grounding narrative: `post-flood/specs/SPEC-004/grounding.md` (4,224 words)
Full risk register: `post-flood/specs/SPEC-004/risk-register.md` (6 classified claims)
Current state inventory: `post-flood/specs/SPEC-004/inventory.md` (4 component assessments)
Full bibliography: `post-flood/specs/bibliography.bib`
