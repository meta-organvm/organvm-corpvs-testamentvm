# SPEC-024: Cyclic Dispatch Protocol

```
Document ID:      SPEC-024
Title:            Cyclic Dispatch Protocol
Version:          1.0
Status:           DRAFT
Layer:            L5 — Swarm Governance
Authoritative:    Session Lifecycle & Agent Dispatch
Parent Specs:     SPEC-013 (Agent Swarm Topology), SPEC-014 (Resource & Compute Constraints)
Date Drafted:     2026-04-05
Principal Author: https://orcid.org/0009-0008-2007-3596
```

---

## 1. Ontological Purpose

The Cyclic Dispatch Protocol prevents premature engineering collapse — the failure mode where abstract ideas are degraded through rough handling before they have been fully explored in their potential state. The default condition of an idea upon entry is idealized. Every touch degrades it. The protocol delays that degradation by inserting four careful phases between intention and realization.

This protocol is the OUTER loop of the ORGANVM agent lifecycle. It governs session-to-session flow. The Conductor lifecycle (FRAME→SHAPE→BUILD→PROVE) is the INNER loop governing within-session execution. The Agent lifecycle (SPAWN→CLAIM→OPERATE→RELEASE→DEBRIEF, per SPEC-013/014) is the per-task loop governing individual agent work.

```
Cyclic Dispatch (outer, session-to-session):
  RELEASE → CATCH → HANDOFF → FORTIFY → [cycle]
                       ↓
Conductor (inner, within-session):
  FRAME → SHAPE → BUILD → PROVE
                       ↓
Agent Lifecycle (per-task):
  SPAWN → CLAIM → OPERATE → RELEASE → DEBRIEF
```

Three nested cycles, each with its own state machine, each with hard phase gates.

## 2. The Four Phases

### FABRICA-001: RELEASE

The human enters an intention into the system. The intention may be abstract, visionary, or underspecified. It arrives as natural language through any projection surface (CLI, MCP, dashboard, voice transcription, or scheduled prompt).

The intention is persisted as a **RelayPacket** — a timestamped, content-addressed seed object. A RelayPacket is not a plan. It is pre-expansion, pre-clarification. It captures the idealized form before any handling.

**Entry**: Human prompt or scheduled trigger.
**Exit**: RelayPacket persisted. Auto-transition to CATCH.

### FABRICA-002: CATCH

The system expands the possibility space. The RelayPacket triggers multiverse expansion: the generating agent produces 2–5 **ApproachVectors**, each a distinct interpretation of the intention. Each vector declares a thesis, target organ(s), estimated scope, and suggested agent types.

The human and AI brainstorm together. The human clarifies — not reduces. Clarification sharpens boundaries without collapsing possibilities. When one or more vectors are selected, they become **RelayIntents** — structured objects with enough specificity to generate plans.

**Rule**: Do not jump to the first solution. The multiverse spray exists to prevent premature convergence.

**Entry**: RelayPacket exists in CATCH phase.
**Exit**: At least one RelayIntent with an assigned organ, scope, and agent type. Transition to HANDOFF.

### FABRICA-003: HANDOFF

Each RelayIntent generates an exhaustive plan. The plan is atomized into tasks via the existing atoms pipeline. Each task is dispatched to the appropriate agent backend based on capability matching, scope compatibility, and resource capacity.

Agent backends include but are not limited to: GitHub Copilot (code implementation via issue assignment), Jules (multi-file refactors via issue assignment), GitHub Actions (process automation via workflow dispatch), Claude Code subagents (complex reasoning in worktree isolation), macOS LaunchAgents (recurring/scheduled tasks via plist generation), and the Human operator (review and judgment via issue creation).

The dispatch protocol decides which agent type receives which task. The routing table is a data structure, not a hardcoded decision tree — it can be extended as new agent backends become available.

**Goal**: Plan so deeply that the engineering feels mechanical. The bureaucracy is the product — it is the thing that gets studied and improved.

**Entry**: At least one RelayIntent in HANDOFF phase.
**Exit**: All dispatches resolved (draft artifacts returned) or timed out. Transition to FORTIFY.

### FABRICA-004: FORTIFY

Draft artifacts return from agents. The human reviews, strengthens, and corrects. Fortified artifacts become proper PRs and merge into the mainline. This is not a rubber stamp — FORTIFY is where human judgment is applied to machine output.

**Exit routes**:
- → **COMPLETE**: All artifacts approved. Cycle done. New RELEASE required.
- → **CATCH**: Review revealed questions the original multiverse spray did not consider. Re-expand.
- → **HANDOFF**: Approach was correct but execution was incomplete. Re-dispatch with adjusted scope.

**Entry**: All dispatches resolved or timed out.
**Exit**: Human verdict on all draft artifacts.

## 3. Phase Transitions

```
RELEASE → CATCH         (always — every packet must be caught)
CATCH → HANDOFF         (when ≥1 vector selected as RelayIntent)
HANDOFF → FORTIFY       (when all dispatches resolved or timed out)
FORTIFY → COMPLETE      (all artifacts approved and merged)
FORTIFY → CATCH         (review revealed new questions)
FORTIFY → HANDOFF       (approach correct, execution incomplete)
COMPLETE → RELEASE      (new cycle)
```

No phase may be skipped. RELEASE must always precede CATCH. CATCH must always precede HANDOFF. The only backward transitions originate from FORTIFY.

## 4. Data Objects

Four data objects compose the protocol's state:

| Object | Created At | Purpose |
|--------|-----------|---------|
| **RelayPacket** | RELEASE | The seed — raw intention, source, timestamp, content-addressed ID |
| **ApproachVector** | CATCH | One interpretation of the intention — thesis, target organs, scope, agent types |
| **RelayIntent** | CATCH (selection) | A selected vector ready for planning and dispatch |
| **DispatchRecord** | HANDOFF | Tracks where a task was sent, its status, and what came back |

Objects are append-only. Status changes are recorded as new events, not mutations. The full lifecycle of a RelayPacket is reconstructable from the event log.

## 5. Persistence

All protocol state persists as JSONL append-only logs at `~/.organvm/fabrica/`. This follows the pattern established by the claims registry (`~/.organvm/claims.jsonl`, per SPEC-014). One truth source. CLI, MCP, and dashboard are read projections.

## 6. The Satellite Principle

The protocol functions as a satellite — a single entry point that hovers above the substrate of all other modules. The human enters the system through the protocol, not through individual repos or directories. The protocol wires together existing modules (dispatch, coordination, atoms, irf, plans, session) into the four-phase cycle. It is a composition layer, not a new system.

Three projections surface the protocol:
- **CLI**: `organvm fabrica <subcommand>`
- **MCP**: Tools prefixed `organvm_fabrica_*` available in any Claude Code session
- **Dashboard**: Route `/fabrica/` in the system dashboard

## 7. The Heartbeat

If the protocol does not pulse, it dies. A daemon (macOS LaunchAgent) runs on the Atomic Clock cadence. Each pulse:

1. Scans for active RelayIntents
2. Checks dispatch statuses via appropriate interfaces (gh CLI, git branch inspection, issue status)
3. Updates DispatchRecord statuses
4. Transitions RelayIntents to FORTIFY when all dispatches resolve
5. Alerts when drafts are ready for human review

The heartbeat is the mechanism that prevents forgetting. Any CLI command that is not also scheduled on the heartbeat is already dead.

## 8. Agent Routing

The routing table maps task characteristics to agent backends. Routing considers:

1. **Explicit hint**: If a task declares an `agent_hint`, honor it.
2. **Capability matching**: Match task type (code_implementation, process_automation, complex_reasoning, etc.) to backend capabilities.
3. **Scope compatibility**: Cross-organ tasks cannot be dispatched to single-repo backends (e.g., Copilot).
4. **Resource capacity**: Reuse the ResourceWeight vocabulary from SPEC-014. The 16GB M3 has a budget of ~6 concurrent weight units.

Agent personas (optional, not first-pass): agents may receive not just a task but a disposition — context that shapes how they approach the work.

## 9. Relationship to Existing Specifications

| Spec | Relationship |
|------|-------------|
| SPEC-013 (Agent Swarm Topology) | Defines the agent classes dispatched by this protocol |
| SPEC-014 (Resource & Compute Constraints) | Provides ResourceWeight vocabulary and capacity budgeting used by routing |
| SPEC-015 (Escalation & Attention Policy) | Governs what happens when dispatches fail or timeout |
| SPEC-016 (Epistemic Routing) | Determines which context is injected when agents receive tasks |
| SPEC-017 (Agent Authority Matrix) | Constrains what each agent backend may modify |

## 10. Implementation

The protocol is implemented as `organvm_engine.fabrica` — a Python module in organvm-engine that composes existing modules:

- `coordination.lifecycle` — phase transition patterns, JSONL event log, ActiveRecordMixin
- `coordination.claims` — capacity budgeting, handle pools
- `dispatch.router` — event routing, DispatchReceipt
- `atoms.pipeline` — task atomization
- `irf` — IRFItem parsing for task sourcing
- `plans` — plan generation and indexing

The CLI entry point is `organvm fabrica`. The MCP tools are exposed via organvm-mcp-server. The dashboard route is `/fabrica/`.
