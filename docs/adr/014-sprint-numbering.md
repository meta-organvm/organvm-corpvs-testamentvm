# ADR-014: Sprint Numbering and Catalog Reconciliation

## Status

Accepted

## Date

2026-02-16

## Context

The system uses two overlapping work-tracking mechanisms:
1. **Sprint specs** in `docs/specs/sprints/` — numbered sequentially (01-ignition through 33-operatio), representing work that was actually executed
2. **Sprint catalog** in `docs/strategy/sprint-catalog.md` — a menu of potential future work, numbered by catalog position, not execution order

During the CANON sprint (Sprint 24), a reconciliation audit discovered that catalog items 19-22 had **different names** than the sprints that were actually executed with those numbers:

| Number | Catalog Item | Executed Sprint |
|--------|-------------|----------------|
| 19 | MEMORIA | CONCORDIA |
| 20 | ANNOTATIO | TRIPARTITUM |
| 21 | DECISIO | SUBMISSIO |
| 22 | CANON (original) | METRICUM |

The confusion arose because the catalog was written before execution, and execution order diverged from the catalog's suggested sequence. Some catalog items (MEMORIA, ANNOTATIO) were combined into TRIPARTITUM; others (DECISIO, original CANON) were deferred; and new sprints emerged that weren't in the catalog at all.

## Decision

### Sprint Numbering: Execution Order Is Canonical

Sprint numbers in `docs/specs/sprints/` reflect **execution order**, not catalog position. The spec files are the source of truth:

- `01-ignition.md` through `33-operatio.md` — continuous numbering, no gaps
- A sprint's number is assigned when it begins execution, not when it's planned
- Sprint names are Latin (following the system's naming convention) and chosen for semantic relevance to the work

### Catalog Reconciliation Rules

1. Catalog items that were executed under different names get a note linking to the actual sprint spec
2. Catalog items that were never executed are marked `[UNSCHEDULED]` — they remain available for future work
3. Catalog items that were combined into a larger sprint (e.g., MEMORIA + ANNOTATIO → TRIPARTITUM) get cross-references
4. New sprints not in the original catalog are added to the catalog retroactively with their execution number

### Naming Convention

Sprint names follow the pattern: `NN-latin-name` where:
- `NN` is zero-padded execution order (01, 02, ... 33)
- `latin-name` is a Latin word describing the sprint's purpose
- The name is chosen at sprint start, not predetermined by the catalog

## Consequences

### Positive

- **No numbering conflicts**: Execution order is unambiguous — sprint 19 is always CONCORDIA
- **Catalog remains useful**: As a menu of potential future work, not a rigid execution plan
- **Historical accuracy**: The spec files form an accurate chronological record of what was actually done
- **Continuous sequence**: No gaps in numbering — every number from 01 to 33 maps to exactly one sprint

### Negative

- **Catalog drift**: The catalog's numbering diverges from execution numbering — readers must understand they're different sequences
- **Naming overhead**: Each sprint needs a unique Latin name chosen at start time — this occasionally delays sprint initiation
- **Retrospective catalog updates**: After each sprint, the catalog must be updated to reflect what actually happened — an administrative task
- **DECISIO still pending**: The catalog item for writing ADRs (DECISIO) was never executed as a named sprint — the work is being done in sessions like AMPLIFICATIO instead

## References

- Sprint specs: `docs/specs/sprints/01-ignition.md` through `docs/specs/sprints/33-operatio.md`
- Sprint catalog: `docs/strategy/sprint-catalog.md`
- CANON reconciliation: `docs/specs/sprints/24-canon.md`
- Concordance: `docs/operations/concordance.md` (sprint namespace)
