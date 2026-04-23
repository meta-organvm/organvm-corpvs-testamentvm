# UAKS v1 Architecture Specification

**Status:** Draft
**Date:** 2026-04-23
**Source atom:** `prompt-34a0d9036d16`
**Implementation repo:** `meta-organvm/atomic-substrata`
**Schema repo:** `meta-organvm/schema-definitions`

## 1. System Identity

**UAKS** (Universal Atomistic Knowledge System) is the core knowledge infrastructure
for ORGANVM. It atomizes human-language material and technical source code into
self-contained, content-addressed units with full provenance, typed relations, and
governed validation states.

The system serves as the substrate beneath all ORGANVM organs -- every piece of
knowledge, code, policy, requirement, and creative artifact is decomposed into atoms
that can be retrieved, assembled, traced, and governed independently.

## 2. Core Principles

1. **Content addressing.** Every atom is identified by its content hash. Same content
   produces the same hash, always.
2. **Immutable objects, mutable metadata.** Content is never modified after creation.
   Logical changes create new content-addressed objects linked by SUPERSEDES relations.
3. **Dual refineries.** Text and code are processed by specialized pipelines that share
   a common governance framework.
4. **Hybrid storage.** Graph, vector, CAS, and raw archive stores serve complementary
   roles -- no single store is authoritative for all operations.
5. **Provenance completeness.** Every verified atom traces to a registered source.

## 3. Source Intake Model

The system accepts four source families.

| Source Family | Examples |
|---------------|----------|
| Raw text | Notes, specs, requirements, essays, policy docs |
| Conversational text | Transcripts, chat logs, meeting notes |
| Technical source | Code files, scripts, configuration, schemas |
| Binary or rich artifacts | PDFs, images, diagrams, archives |

### 3.1 Source Object Schema

Each source receives immutable registration metadata before refinement. The full
schema is defined in `schema-definitions/schemas/uaks-source-object.schema.json`.

Key fields: `sourceId`, `sourceType`, `origin`, `ingestedAt`, `checksum` (SHA-256),
`mimeType`, `authorRef`, `rightsClass`, `rawArchiveRef`.

## 4. Atom Families

### 4.1 TextAtom

Self-contained units of human-language meaning. Schema defined in
`schema-definitions/schemas/uaks-text-atom.schema.json`.

**Atom classes:** claim, definition, requirement, policy, observation, question,
instruction, narrative, evidence, annotation, summary, hypothesis.

**Text kinds:** technical, academic, conversational, legal, editorial, creative,
operational.

### 4.2 CodeAtom

Meaningful units of technical source with dependency graphs. Schema defined in
`schema-definitions/schemas/uaks-code-atom.schema.json`.

**Code kinds:** function, class, module, config, query, schema, test, script,
interface, type_definition, migration, workflow.

## 5. Refinery Architecture

Two refineries operate under one governance framework.

### 5.1 Text Refinery Stages

| Stage | Function |
|-------|----------|
| Segmentation | Structural splitting into candidate spans |
| Extraction | Entities, claims, relations, temporal cues |
| Distillation | Convert segments into self-contained units |
| Typing | Assign atom class and text kind |
| Linking | Attach evidence, entities, parents, contradictions |
| Validation | Atomicity, clarity, provenance check |

### 5.2 Code Refinery Stages

| Stage | Function |
|-------|----------|
| Parse | AST construction |
| Symbol extraction | Functions, classes, modules, configs, queries |
| Boundary determination | Determine meaningful code atom spans |
| Dependency analysis | Imports, calls, dataflow, interfaces |
| Technical typing | Assign code kind, runtime, side-effect profile |
| Bridge linking | Connect to tests, docs, rules, interfaces |
| Validation | Parse validity, span integrity, hash binding |

## 6. Storage Architecture

UAKS v1 is explicitly hybrid. No single store is authoritative for all operations.

### 6.1 Layer Roles

| Layer | Primary Role | What It Should Not Do |
|-------|-------------|----------------------|
| Graph | Explicit logic and relation substrate | Not sole semantic retrieval engine |
| Vector | Similarity and latent concept retrieval | Not define truth or replace graph logic |
| CAS | Immutable content persistence | Not be user-facing ontology |
| Raw Source Archive | Forensic source preservation | Not serve as primary query substrate |
| GraphQL API | Unified typed access layer | Not become the storage engine itself |

### 6.2 Adoption Matrix

All five components are mandatory for v1: Graph (critical), Vector (high),
CAS (critical), Raw Source Archive (critical), GraphQL API (high, treated as mandatory).

### 6.3 Failure-If-Absent Analysis

| Missing Component | Likely Failure |
|-------------------|----------------|
| Graph absent | No robust code-policy mapping, weak dependency reasoning |
| Vector absent | Retrieval becomes brittle and keyword-bound |
| CAS absent | No precise content identity, weak technical reproducibility |
| Raw archive absent | Provenance collapses, reprocessing impossible |
| GraphQL absent | Fragmented interfaces, inconsistent access semantics |

## 7. Retrieval Model

Retrieval is hybrid and score-based:

```
R(a, q) = w1 * semantic(a,q)
         + w2 * graph(a,q)
         + w3 * temporal(a,q)
         + w4 * validation(a)
         + w5 * utility(a)
         + w6 * centrality(a)
```

- For TextAtom: semantic and evidence relations dominate.
- For CodeAtom: dependency, symbol, interface, and business-rule relations receive
  more weight.

## 8. Assembly Model

Assemblies are stored as recipes, not documents. Schema defined in
`schema-definitions/schemas/uaks-assembly-recipe.schema.json`.

### 8.1 v1 Assembly Outputs

| Output Type | Inputs |
|-------------|--------|
| Technical specification | Text and code atoms + dependency graph |
| Rule-to-code trace report | Rule atoms + implementing code atoms |
| Impact analysis | Changed code atoms + dependents |
| Policy drift report | Changed text atoms + mismatched code atoms |
| Documentation synthesis | Code atoms + documentation atoms |

## 9. Governance Model

### 9.1 Validation States

| State | Meaning |
|-------|---------|
| `DRAFT` | Newly created, not reviewed |
| `DISTILLED` | Machine-produced and schema-conformant |
| `REVIEWED` | Human or trusted automated review completed |
| `VERIFIED` | Approved for production assembly |
| `DEPRECATED` | Retained but not active |
| `DISPUTED` | Integrity or truth in question |

Validation state transitions are recorded as validation events. Schema defined in
`schema-definitions/schemas/uaks-validation-event.schema.json`.

### 9.2 Review Policy

- TextAtoms expressing requirements, policies, or externally consequential claims
  must not be treated as production-grade until reviewed.
- CodeAtoms with high breaking-change risk, external side effects, or policy linkage
  must not auto-promote to verified without review.

### 9.3 Supersession Policy

Content changes create new content-addressed objects. Logical continuity is expressed
through `SUPERSEDES` relations and effective-time intervals.

## 10. Nonfunctional Requirements

| Requirement | Target |
|-------------|--------|
| Provenance completeness | 100% of verified atoms must trace to a source |
| Hash determinism | Same content must produce same hash |
| Graph consistency | No dangling verified relation edges |
| Retrieval hybridity | Queries must combine graph and vector criteria |
| Projection stability | Portal/workspace views must reconstruct exact requested state |
| Re-refinement ability | Sources must be reprocessable without loss |

## 11. v1 Exclusions

| Exclusion | Reason |
|-----------|--------|
| Full autonomous code rewriting loop | Too much operational risk in v1 |
| Distributed peer-to-peer storage network | Unnecessary for first internal architecture |
| Universal language/runtime support | Start with selected languages |
| Perfect policy-code trace completeness | Achieve partial but structurally correct linkage first |
| Full real-time live IDE mutation orchestration | Too complex for foundational release |

## 12. Recommended Launch Sequence

| Phase | Objective | Schema Artifacts |
|-------|-----------|-----------------|
| 1 | Core ontology, schemas, IDs, relations | `uaks-source-object.schema.json`, `uaks-text-atom.schema.json`, `uaks-code-atom.schema.json` |
| 2 | Raw archive + CAS + graph backbone | `uaks-validation-event.schema.json` |
| 3 | Text refinery | — |
| 4 | Code refinery | — |
| 5 | GraphQL interface | — |
| 6 | Retrieval and recipe engine | `uaks-assembly-recipe.schema.json` |
| 7 | Traceability and impact-analysis reports | — |
| 8 | Governance and operator workflows | — |

## 13. Artifact Inventory

### A. Schema Artifacts (Created)

| Artifact | File | Status |
|----------|------|--------|
| Source object schema | `schemas/uaks-source-object.schema.json` | Done |
| TextAtom schema | `schemas/uaks-text-atom.schema.json` | Done |
| CodeAtom schema | `schemas/uaks-code-atom.schema.json` | Done |
| Assembly recipe schema | `schemas/uaks-assembly-recipe.schema.json` | Done |
| Validation event schema | `schemas/uaks-validation-event.schema.json` | Done |

### B. Schema Artifacts (Pending)

| Artifact | Purpose |
|----------|---------|
| Entity schema catalog | Domain object definitions |
| Relation schema catalog | Typed edge definitions |
| Provenance schema | Transformation lineage records |
| Telemetry schema | Operational metrics and instrumentation |

### C. Implementation Modules (Existing Stubs in `atomic-substrata`)

| Module | Path | Status |
|--------|------|--------|
| Source Intake | `src/uaks/source_intake/` | Basic implementation |
| Text Refinery | `src/uaks/text_refinery/` | Stub |
| Code Refinery | `src/uaks/code_refinery/` | Stub |
| Graph Storage | `src/uaks/graph_storage/` | Exists |
| Vector Retrieval | `src/uaks/vector_retrieval/` | Exists |
| CAS | `src/uaks/content_addressable_storage/` | Exists |
| Assembly | `src/uaks/assembly/` | Exists |
| GraphQL | `src/uaks/graphql/` | Exists |
| Portal Projection | `src/uaks/portal_projection/` | Exists |
| Semantic Embeddings | `src/uaks/semantic_embeddings/` | Exists |
| Integrity Verification | `src/uaks/integrity_verification/` | Exists |

### D. Governance Artifacts (Pending -- Require Human Decision)

| Artifact | Purpose | Decision Needed |
|----------|---------|-----------------|
| Ontology charter | Defines atom families, classes, entities, and relation semantics | Which entity types are v1-canonical? |
| Naming convention standard | Standardizes identifiers, tags, and schema names | Prefix convention for each atom family |
| Data governance policy | Defines access, review, retention, and lifecycle rules | Retention period for deprecated atoms |
| Contradiction handling policy | How conflicts remain visible rather than flattened | Dispute resolution workflow |
| Security and rights policy | Permissions, sensitivity classes, archival controls | rightsClass enforcement mechanism |
