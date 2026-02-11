---
title: "Recursive Engines at Scale: How We Formalized Narrative as Algorithm"
date: 2026-02-11
author: 4444j99
category: theory-implementation
organ: ORGAN-I
status: draft
excerpt: >
  How a symbolic operating system for myth, identity, and ritual became a
  1,254-test, 85%-coverage Python codebase — and what that teaches us about
  formalizing narrative principles as executable systems.
portfolio_relevance: HIGH
related_repos:
  - organvm-i-theoria/recursive-engine--generative-entity
  - organvm-i-theoria/narratological-algorithmic-lenses
reading_time: 14
target_word_count: 4000
---

# Recursive Engines at Scale: How We Formalized Narrative as Algorithm

## The Problem: Narrative Is Everywhere, but Nowhere Computable

Every software system tells a story. User flows are plot arcs. State machines are character development. Error handling is conflict resolution. But we treat these observations as metaphors rather than engineering principles.

What if narrative structure — the formal kind, from Aristotle's *Poetics* through Propp's *Morphology of the Folktale* to McKee's *Story* — could be encoded as executable rules? Not as an AI that "writes stories" (the market is saturated with those), but as a symbolic operating system where narrative principles govern how systems organize, evolve, and maintain coherence.

That's what ORGAN-I's recursive-engine does. And the journey from "interesting idea" to "1,254 tests passing" taught us more about the relationship between formalism and creativity than any amount of theorizing could.

## What RE:GE Actually Is

RE:GE — Recursive Engine: Generative Entity — is a symbolic operating system written in pure Python. It implements 21 organ handlers that process symbolic values through a ritual syntax DSL. In plainer terms:

**It's a system where myths, identities, rituals, and recursive structures are first-class computational objects.**

Each "organ" in the engine handles a different aspect of symbolic processing:

- **Myth organs** encode narrative archetypes as transformation rules. A hero's journey isn't a template; it's a function that takes an entity state and returns a transformed state.
- **Identity organs** manage how entities maintain coherence across transformations. When a character "changes," what persists? The identity organs formalize this.
- **Ritual organs** define sequences of operations that must execute in order, with pre-conditions and post-conditions — essentially, ceremonies as transactions.
- **Recursive organs** handle self-reference: entities that describe themselves, systems that modify their own rules, narratives that contain narratives.

The engine processes these through what we call the "ritual syntax DSL" — a domain-specific language for declaring symbolic operations:

```
INVOKE myth.hero_journey ON entity:protagonist
  WITH threshold: 0.7
  BINDING outcome TO identity.transform
  WHEN condition.readiness EXCEEDS threshold
```

This isn't pseudo-code. It's the actual syntax the engine parses and executes.

## From Theory to 1,254 Tests

The hardest part of building RE:GE wasn't the theory. It was the testing.

When your system's purpose is to formalize narrative — something humans experience as intuition, emotion, and aesthetic judgment — how do you write assertions? What does "correct" mean for a myth transformation?

We solved this through three testing strategies:

### 1. Structural Invariants

Regardless of what a transformation *means*, certain structural properties must hold. An identity transformation must preserve entity type. A ritual must execute all steps or none (transactionality). A recursive invocation must terminate (halting guarantee within bounded depth).

These gave us ~400 tests that verify the engine doesn't violate its own rules, independent of any particular narrative content.

### 2. Reference Implementations

We encoded known narrative structures — Propp's 31 functions, Campbell's monomyth stages, Aristotle's six elements — as test cases. If the engine claims to implement Propp's "Villainy" function, we can verify it produces the correct state transition for a known input.

This gave us ~500 tests that verify fidelity to established narrative theory.

### 3. Round-Trip Consistency

If we serialize an entity to the ritual syntax DSL and then parse it back, we should get the same entity. If we apply a transformation and then its inverse (where one exists), we should return to the original state.

This gave us ~350 tests that verify the engine's internal consistency.

The result: 1,254 tests, 85% line coverage, with the remaining 15% being edge cases in the DSL parser that we're still formalizing.

## What Narratological Algorithmic Lenses Adds

While RE:GE is the engine, [narratological-algorithmic-lenses](https://github.com/organvm-i-theoria/narratological-algorithmic-lenses) is the analytical layer. It implements 14 narratological studies crossed with 92 algorithms — a systematic exploration of how narrative principles can be formalized.

Each "lens" pairs a narrative theory with an algorithmic approach:

| Narrative Theory | Algorithm Family | What It Analyzes |
|-----------------|-----------------|------------------|
| Propp's Morphology | Graph traversal | Function sequence patterns |
| Aristotle's Poetics | Constraint satisfaction | Six-element balance |
| Barthes's S/Z | Text classification | Code distribution in text |
| Genette's Narratology | Temporal logic | Anachrony and focalization |
| McKee's Story | Optimization | Scene-level value changes |

The lenses include a CLI, an API, and a web dashboard for running analyses against real texts. We've tested them against published screenplays and novels, verifying that the algorithmic analyses align with expert human readings.

This is where the theory-to-practice bridge becomes concrete: you can take a screenplay, run it through the Proppian lens, and see which of the 31 functions appear, in what order, with what deviations from the canonical sequence. It's not replacing human literary analysis — it's providing a computational complement.

## Why This Matters for AI Systems

The obvious question: why build a symbolic narrative engine in the age of large language models?

Three reasons:

### 1. Interpretability

LLMs generate narrative content, but they can't explain *why* a particular story choice was made. RE:GE can. Every transformation has a trace — which organ fired, what rule applied, what condition was met. When the system decides a character should face their threshold moment, you can inspect exactly why.

This isn't academic. As AI systems become more consequential, the ability to audit narrative decisions (why did the recommendation system frame this product story this way?) becomes critical.

### 2. Composability

RE:GE's organs are composable. You can build a myth organ on top of an identity organ on top of a recursive organ. You can swap organs in and out. You can run the same entity through different narrative frameworks and compare results.

LLMs don't compose this way. You can't take GPT's "understanding" of hero's journeys and cleanly separate it from its understanding of tragedy. In RE:GE, these are distinct, testable modules.

### 3. Governance Integration

Because RE:GE is part of the eight-organ system, its narrative operations are subject to the same governance that governs everything else. The dependency validation ensures RE:GE doesn't develop unauthorized dependencies. The promotion state machine controls when RE:GE concepts move from theory (ORGAN-I) to art (ORGAN-II). The monthly audit checks that RE:GE's tests still pass.

This means narrative computation exists within an institutional framework — not as an isolated experiment, but as governed infrastructure.

## Lessons Learned

### Formalism Enables, Not Constrains

The most common objection to formalizing narrative is that it kills creativity. Our experience is the opposite. Having 21 distinct organ types, each with formal interfaces and test suites, created more creative possibilities than working without structure.

When you know exactly what an identity transformation guarantees, you can safely compose it with a myth transformation and a ritual sequence. The formalism is what makes creative composition safe and predictable.

### Test-Driven Development Works for Abstract Systems

We were skeptical that TDD would work for a system whose purpose is "symbolic narrative processing." But structural invariants, reference implementations, and round-trip consistency gave us a testing strategy that's both rigorous and meaningful.

The key insight: you don't need to test whether the narrative is "good." You test whether the system's behavior is consistent, correct according to its declared rules, and faithful to the theoretical frameworks it claims to implement.

### Pure Python Was the Right Choice

No machine learning frameworks, no external dependencies for the core engine. Pure Python with standard library only. This was deliberate:

- **Auditability**: Anyone can read the code. No hidden model weights.
- **Testability**: No GPU required, no non-determinism from model inference.
- **Longevity**: No dependency on framework versions that might break.
- **Portability**: Runs anywhere Python runs.

For a system meant to be infrastructure — meant to last years, not sprints — minimizing dependencies was essential.

## Connection to the Eight-Organ System

RE:GE is the definitive ORGAN-I expression. It embodies the theoretical depth that feeds into everything else:

- **ORGAN-II (Art)** implements RE:GE concepts as generative installations and performances
- **ORGAN-III (Commerce)** packages RE:GE capabilities into products (the narratological analysis API)
- **ORGAN-V (Public Process)** documents the theory and methodology publicly
- **ORGAN-IV (Governance)** ensures RE:GE's development follows the promotion state machine

This is the I->II->III flow made concrete. Theory (formalized narrative) becomes art (generative systems) becomes commerce (analysis tools). The recursive engine recurses through the entire system.

## What's Next

Three active development tracks:

1. **DSL completion**: The ritual syntax language has ~30 keywords implemented out of a target ~50. The remaining keywords handle advanced recursive constructs and meta-narrative operations.

2. **External bridges**: Integration with Obsidian (for knowledge graph interop), Git (for version-controlled narrative state), and Max/MSP (for real-time performance systems).

3. **Benchmark suite**: A standardized set of narrative analysis benchmarks, comparable to how NLP has GLUE/SuperGLUE. This would allow comparing symbolic approaches (RE:GE) with neural approaches (LLMs) on identical narrative tasks.

The recursive engine continues to recurse.

---

*This essay is part of the [ORGAN-V Public Process](https://github.com/organvm-v-logos/public-process) — building in public, documenting everything.*

*Related repos: [recursive-engine--generative-entity](https://github.com/organvm-i-theoria/recursive-engine--generative-entity) | [narratological-algorithmic-lenses](https://github.com/organvm-i-theoria/narratological-algorithmic-lenses)*

*Discuss: Open an issue in the public-process repo.*
