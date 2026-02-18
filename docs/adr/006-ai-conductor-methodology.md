# ADR-006: AI-Conductor Methodology

## Status

Accepted

## Date

2026-02-09

## Context

Building institutional-scale documentation (97 repos, ~404K+ words, 41 essays) as a solo operator is infeasible with traditional human-writes-everything workflows. The project needed a methodology that:

1. Enables one person to produce volume equivalent to a small team
2. Maintains consistent quality across hundreds of documents
3. Preserves human strategic judgment on positioning, accuracy, and voice
4. Uses a measurable effort model (not subjective "hours" estimates)

The key insight: LLMs excel at volume generation but lack strategic judgment. Humans excel at judgment but cannot match LLM throughput. The optimal split is human-directs, AI-generates, human-reviews.

## Decision

The **AI-Conductor model** divides labor:

- **Human (conductor)**: Sets direction, defines templates, reviews output, ensures accuracy, handles strategic positioning
- **AI (orchestra)**: Generates volume — READMEs, essays, boilerplate, CI workflows, validation scripts
- **Human (final pass)**: Reviews AI output for hallucinations, generic phrasing, incorrect cross-references, and strategic misalignment

Effort is measured in **TE (Tokens Expended)**, not human-hours:

| Task Type | TE Budget |
|-----------|-----------|
| README REWRITE | ~72K TE |
| README POPULATE | ~88K TE |
| Essay (4,000–5,000 words) | ~120K TE |
| Validation Pass (per repo) | ~15K TE |
| GitHub Actions Workflow | ~55K TE |

Total system budget: ~6.5M TE across Phases 1–3.

**AI-specific quality risks** are explicitly tracked:
- Hallucinated code examples (AI invents functions that don't exist)
- Generic boilerplate phrasing ("leverage synergies" language)
- Incorrect cross-references (linking to wrong documents)
- Missing project-specific context (writing about the project as if it were generic)

## Consequences

### Positive

- **Solo scalability**: One person produced ~404K+ words of documentation in under 10 days
- **Measurable effort**: TE budgets enable predictable planning and resource allocation
- **Consistent templates**: AI-generated docs follow the same structure, reducing reader cognitive load
- **Rapid iteration**: 2–3 revision cycles per document, each taking minutes not hours
- **33 sprints completed** using this model — the methodology itself has been battle-tested

### Negative

- **Review burden shifts**: The human bottleneck moves from writing to reviewing — reviewing 50 READMEs still takes real time
- **Voice consistency risk**: AI-generated text can feel homogeneous; human editorial passes are needed to inject authentic voice
- **Hallucination management**: Every factual claim in AI-generated text must be verified against source material
- **TE budgets are approximate**: Actual token usage varies with model, context length, and revision depth
- **Methodology is non-standard**: Job applications and grant proposals must explain why "AI wrote this" is a feature, not a liability

## References

- TE budget model: `docs/implementation/implementation-package-v2.md`
- Constitution Article III (Quality): `docs/memory/constitution.md`
- Essay on methodology: `2026-02-11-ai-conductor-methodology.md` in public-process
- CLAUDE.md "AI-Conductor Workflow Model" section
