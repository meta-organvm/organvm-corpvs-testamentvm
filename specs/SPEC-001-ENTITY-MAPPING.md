# SPEC-001 Entity Type Mapping

```
Document ID:      SPEC-001-ENTITY-MAPPING
Title:            Ontologia Entity Type Derivation from SPEC-000 Primitives
Version:          1.0
Status:           ACTIVE
Parent Specs:     SPEC-001 (Ontology Charter), SPEC-000 (System Manifesto)
Date:             2026-04-14
Refs:             #312
```

---

## Purpose

This document makes explicit the derivation chain from SPEC-000 primitives (Section 6)
through SPEC-001 stratified taxonomy (ONT-001 through ONT-028) to the ontologia
implementation entity types (the `EntityType` enum in `organvm-ontologia`).

SPEC-001 Section 7 reconciles four primitive formulations. SPEC-001 Section 9c lists
category paths. This document completes the wiring by stating, for each implemented
leaf type, which SPEC-000 primitive it instantiates and through which intermediate
ontological categories the derivation passes.

---

## Derivation Table

| Ontologia Leaf | ONT-### | SPEC-000 Primitive | Category Path | Derivation Rationale |
|----------------|---------|-------------------|---------------|---------------------|
| `ORGAN` | ONT-004 | **Entity** | Entity > Continuant > IndependentContinuant > ORGAN | An organizational unit with persistent identity (SPEC-000 Section 6: "a thing that exists with persistent identity"). Top-level containment boundary. |
| `REPO` | ONT-005 | **Entity** | Entity > Continuant > IndependentContinuant > REPO | A version-controlled repository bearing governance state. Independent continuant with its own identity, not a quality of another entity. |
| `MODULE` | ONT-006 | **Entity** | Entity > Continuant > IndependentContinuant > MODULE | An extractable sub-package within a repository. Finest-grained independent continuant tracked by the system. |
| `VARIABLE` | ONT-008 | **Value** | Entity > Continuant > SpecificallyDependentContinuant > VARIABLE | A named quality with temporal value history inhering in a bearer entity (SPEC-000 Section 6: "a datum attached to an entity"). |
| `METRIC` | ONT-009 | **Value** | Entity > Continuant > SpecificallyDependentContinuant > METRIC | A measured quality with thresholds and gate associations. Specializes VARIABLE with normative structure. Derived from Value as a constrained datum. |
| `DOCUMENT` | ONT-011 | **Entity** | Entity > Continuant > GenericallyDependentContinuant > DOCUMENT | An authored information content entity. Generically dependent: can migrate between bearers without identity loss. Not derived from Value (documents are not data attached to an entity) but from Entity (a thing with persistent identity that happens to depend on some bearer). |
| `SESSION` | ONT-015 | **Event** | Entity > Occurrent > Process > SESSION | A bounded agent work episode (SPEC-000 Section 6: "a state change with timestamp and causation"). Technically a Process (has duration), but its primitive ancestor is Event because sessions mark and record state changes. SPEC-001 Section 7 restores Process as a distinct concept from Stage-II. |

---

## SPEC-000 Primitive Coverage

How each of the 7 SPEC-000 primitives (Section 6) maps into the implemented ontologia types:

| SPEC-000 Primitive | Implemented As | Notes |
|-------------------|---------------|-------|
| **Entity** | ORGAN, REPO, MODULE, DOCUMENT | The primitive "Entity" is the root sortal (ONT-001). All leaf types are entities. ORGAN, REPO, MODULE are direct embodiments as independent things. DOCUMENT is a generically dependent entity. |
| **Value** | VARIABLE, METRIC | SPEC-001 Section 7: "Value is a property of SpecificallyDependentContinuants." VARIABLE is the general case; METRIC adds normative thresholds. |
| **Relation** | *(not a leaf EntityType)* | Relations are typed connections between entities (ONT-030 through ONT-037). Implemented as HierarchyEdge, LineageRecord, DependencyEdge in ontologia's structure layer, not as entity types. |
| **Event** | SESSION | SESSION is the only implemented occurrent. Future: StateTransition (ONT-018), SignalDispatch (ONT-019). |
| **State** | *(not a leaf EntityType)* | State is modeled through ONT-040 (PromotionState) and ONT-041 (OrganismState) as state machines, not as entity types. Tracked via LifecycleStatus enum and promotion_status fields. |
| **Constraint** | *(implementation debt)* | ONT-026 (CONSTRAINT) is ratified but not yet implemented as an EntityType. Currently encoded in governance-rules.json. Target: SPEC-003. |
| **Capability** | *(implementation debt)* | ONT-027 (Capability) is ratified but not yet implemented as an EntityType. Currently declared in seed.yaml produces/consumes. Target: Layer 3B. |

---

## Derivation Chain Diagram

```
SPEC-000 Section 6              SPEC-001 Stratified Taxonomy           Ontologia EntityType
(7 Primitives)                  (ONT-001 through ONT-028)              (7 Leaf Types)
──────────────────              ──────────────────────────              ──────────────────

Entity ─────────────── ONT-001 Entity
                         ├─ ONT-002 Continuant
                         │    ├─ ONT-003 IndependentContinuant
                         │    │    ├─ ONT-004 ──────────────── ORGAN
                         │    │    ├─ ONT-005 ──────────────── REPO
                         │    │    └─ ONT-006 ──────────────── MODULE
                         │    ├─ ONT-007 SpecificallyDependentCont.
Value ──────────────────►│    │    ├─ ONT-008 ──────────────── VARIABLE
                         │    │    └─ ONT-009 ──────────────── METRIC
                         │    └─ ONT-010 GenericallyDependentCont.
                         │         └─ ONT-011 ──────────────── DOCUMENT
                         ├─ ONT-013 Occurrent
Event ──────────────────►│    ├─ ONT-014 Process
                         │    │    └─ ONT-015 ──────────────── SESSION
                         │    ├─ ONT-017 Event (instantaneous)
State ──────────────────►│    │    └─ ONT-018 StateTransition ── (debt)
                         │    └─ ONT-020 TemporalRegion
                         └─ ONT-023 Abstract
Constraint ─────────────►     ├─ ONT-024 GovernanceObject
                              │    ├─ ONT-025 RULE ──────────── (debt)
                              │    └─ ONT-026 CONSTRAINT ────── (debt)
Capability ─────────────►     └─ ONT-027 Capability ─────────── (debt)

Relation ───────────────► ONT-030..037 (typed edges, not entity types)
```

---

## Implementation References

| File | Role |
|------|------|
| `organvm-ontologia/src/ontologia/entity/identity.py` | `EntityType` enum — the 7 leaf types |
| `organvm-engine/src/organvm_engine/ontology/taxonomy.py` | `CATEGORY_MAP` — maps leaf types to BFO-aligned categories |
| `specs/SPEC-000.md` Section 6 | Declares the 7 primitives |
| `specs/SPEC-001.md` Section 2 | Defines the full ONT-001 through ONT-028 stratified taxonomy |
| `specs/SPEC-001.md` Section 7 | Reconciles the 4 primitive formulations |
| `specs/SPEC-001.md` Section 9c | Lists category paths for implemented types |
