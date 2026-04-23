# ADR-017: Multi-Agent Architecture Paradigm

**Status:** Accepted
**Date:** 2026-04-23
**Source atom:** `prompt-1dd4e88daf85`
**Deciders:** System architect (human)

## Context

ORGANVM operates as an AI-conductor system where one human directs multiple AI agents.
The August 2025 architectural synthesis (prompt-1dd4e88daf85) proposed a modular synthesis
paradigm for multi-agent systems, drawing from modular synthesizer design. This ADR
captures the architectural decisions that emerged from that analysis and their
application to the current ORGANVM agent fleet.

## Decision

### 1. Orchestration Model: State Machine, Not Rigid DAG

ORGANVM workflows are state machines that support both linear and cyclical execution.

- **Linear workflows** (standard patches): Well-defined tasks follow the
  FRAME -> SHAPE -> BUILD -> PROVE pipeline sequentially.
- **Adaptive workflows** (experimental patches): Open-ended problems allow dynamic
  agent routing with cycle support (e.g., BUILD -> SHAPE back-transition for reshaping).

**Circuit breakers are mandatory.** Every potential loop must have provably correct
termination conditions. Maximum iteration counts and timeout budgets prevent infinite
agent cycling.

### 2. Collaboration Pattern: Hierarchical with Blackboard

ORGANVM uses hierarchical orchestration (human as conductor, Claude as strategic layer,
Codex/Gemini/OpenCode as tactical layer) combined with a blackboard pattern (shared
filesystem, git repos, and MCP servers as the communication substrate).

- **Hierarchical orchestration** governs task decomposition and delegation.
- **Blackboard collaboration** occurs through shared git repositories and the atom
  registry, where agents read from and write to common substrates.

### 3. Agent Role Enforcement

Each agent in the fleet has a single, well-defined purpose. Role confusion (where a
generalist LLM bleeds outside its designated function) is mitigated by:

- Constrained system prompts per agent (CLAUDE.md, AGENTS.md)
- Validation logic in the conductor layer
- Dispatch protocol that routes work to the correct cognitive class

| Agent | Role | Cognitive Class |
|-------|------|-----------------|
| Claude | Strategic: architecture, audit, governance, debugging | Strategic |
| Codex | Mechanical: scaffolding, boilerplate, test stubs | Mechanical |
| Gemini | Tactical: content generation, research velocity | Tactical |
| OpenCode | Mechanical: well-scoped infrastructure tasks | Mechanical |
| Perplexity | Research: web research, source discovery | Research |

### 4. Budget-Aware Scheduling

Cost optimization follows the CFO Agent pattern:

- **Dynamic model routing:** Tasks are dispatched to the cheapest capable agent.
  Claude handles only strategic work; mechanical tasks go to the bench.
- **Response caching:** Semantic and exact-match caching in the conductor layer
  prevents redundant API calls.
- **Token accounting:** Every session tracks token consumption against work produced.

### 5. Tiered Memory Architecture

The system uses a hybrid memory model:

| Layer | Technology | Role |
|-------|-----------|------|
| Hot state | MCP servers, filesystem, working memory | Active collaboration substrate |
| Warm state | Git repositories, CLAUDE.md, session archives | Persistent shared context |
| Cold state | Atom registry, fossil record, raw archives | Immutable audit trail |

### 6. Safety and Governance

- **Guardrails:** PreToolUse hooks in Claude's settings.json enforce outbound operation
  constraints. No agent can perform destructive operations without conductor approval.
- **Human-in-the-loop:** High-stakes actions (production deployments, data deletion,
  financial operations) require explicit human confirmation.
- **Traceability:** All agent actions are logged in session archives for accountability.
  The conductor cross-verification protocol validates dispatched agent work.

## Consequences

### Positive

- Clear separation of strategic vs. mechanical work reduces cost
- Modular agent design allows fleet expansion without architecture changes
- Circuit breaker requirement prevents runaway agent loops
- Blackboard pattern enables emergent cross-agent collaboration

### Negative

- Dispatch overhead adds latency to task initiation
- Role enforcement requires ongoing prompt engineering
- Multi-agent coordination complexity grows with fleet size

### Risks

- Agent role drift if system prompts are not regularly audited
- Blackboard contention if multiple agents write to the same files simultaneously
- Budget model accuracy depends on consistent token-to-value tracking

## Related

- ADR-006: AI Conductor Methodology
- ADR-010: Cross-Org Dispatch
- Dispatch Protocol in CLAUDE.md (global)
