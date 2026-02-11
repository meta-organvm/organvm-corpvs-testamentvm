# Three-Run Comparison Report

**Date:** 2026-02-09  
**Scope:** Compare three macro run sets and synthesize a canonical baseline

## 1. Run Inventory And Provenance

Compared run sets:
- **Run A:** `gemini-cli`
- **Run B:** `github-copilot-cli`
- **Run C:** `codex-cli/runs/20260209-135130`

Core comparable files:
- `codex_validation_response.md`
- `gemini_validation_response.md`
- `copilot_validation_response.md`
- `validation_synthesis.md`

Non-overlapping files:
- Only in Run A: `06-EVALUATION-TO-GROWTH-ANALYSIS.md`, `07-CROSS-AI-LOGIC-CHECK-PROMPTS.md`, `07-CROSS-AI-LOGIC-CHECK-RESULTS.md`
- Only in Run B: `analysis_differences_report.md`
- Only in Run C: run artifacts (`*.raw.md`, prompt runtime files, logs, manifests, provenance)

Integrity check:
- Run A and Run B are byte-identical on all four core comparable files.
- Run C differs from Run A/B on all four core comparable files.

## 2. High-Level Result

Short answer to the confusion: prior analysis compared only **Run A vs Run B**.  
This report compares **A vs B vs C**.

## 3. Agreement Classes

### 3.1 Stable Consensus (3/3)

1. **Registry schema is a blocker for automation.**
- A/B: `gemini-cli/validation_synthesis.md:11`, `gemini-cli/validation_synthesis.md:15`
- C: `codex-cli/runs/20260209-135130/codex_validation_response.md:4`, `codex-cli/runs/20260209-135130/codex_validation_response.md:20`

2. **Tiered launch (Bronze/Silver/Gold) is required; all-at-once is not viable.**
- A/B: `gemini-cli/07-CROSS-AI-LOGIC-CHECK-RESULTS.md:18`
- C: `codex-cli/runs/20260209-135130/07-CROSS-AI-LOGIC-CHECK-RESULTS.md:11`, `codex-cli/runs/20260209-135130/07-CROSS-AI-LOGIC-CHECK-RESULTS.md:16`

3. **Coordination overhead must be explicit.**
- A/B: `gemini-cli/validation_synthesis.md:23`, `gemini-cli/validation_synthesis.md:27`
- C: `codex-cli/runs/20260209-135130/validation_synthesis.md:12`, `codex-cli/runs/20260209-135130/validation_synthesis.md:47`

4. **README strategy must be tiered, not uniform.**
- A/B: `gemini-cli/07-CROSS-AI-LOGIC-CHECK-RESULTS.md:46`, `gemini-cli/copilot_validation_response.md:260`
- C: `codex-cli/runs/20260209-135130/validation_synthesis.md:15`, `codex-cli/runs/20260209-135130/copilot_validation_response.md:32`

### 3.2 Pairwise Consensus (2/3)

1. **Two-phase registry approach (schema first, population during writing).**
- A/B explicit: `gemini-cli/validation_synthesis.md:97`, `gemini-cli/validation_synthesis.md:149`
- C partial alignment: schema-first appears strongly (`codex-cli/runs/20260209-135130/codex_validation_response.md:74`), population-during-writing appears indirectly via sequencing (`codex-cli/runs/20260209-135130/copilot_validation_response.md:45`)

2. **Human review fatigue is a material execution risk.**
- A/B explicit: `gemini-cli/validation_synthesis.md:203`, `gemini-cli/validation_synthesis.md:206`
- C present in execution response: `codex-cli/runs/20260209-135130/copilot_validation_response.md:58`

## 4. Divergences Introduced In Run C

## 4.1 Technical Response Drift (Codex prompt)

### Topic: Budget realism and correction policy
- A/B Codex response:
  - Bronze estimate called optimistic and adjusted upward (`~1.6M`): `gemini-cli/codex_validation_response.md:207`, `gemini-cli/codex_validation_response.md:211`
  - Recommended **not** formally updating planning docs for correction propagation: `gemini-cli/codex_validation_response.md:276`
- C Codex response:
  - Bronze `~1.5M` treated as plausible: `codex-cli/runs/20260209-135130/codex_validation_response.md:51`
  - Recommended formal propagation of 13% correction to Phases 2-3: `codex-cli/runs/20260209-135130/codex_validation_response.md:62`

### Impact
- This is a **hard recommendation reversal** in policy (note-risk vs formal-propagate).

## 4.2 Strategic Response Drift (Gemini prompt)

### Topic: Hiring posture for meta-documentation
- A/B Gemini response:
  - Documentation alone is too abstract for AI hiring: `gemini-cli/gemini_validation_response.md:24`, `gemini-cli/gemini_validation_response.md:72`
- C Gemini response:
  - Stronger endorsement for AI systems hiring signal from coordination complexity: `codex-cli/runs/20260209-135130/gemini_validation_response.md:16`, `codex-cli/runs/20260209-135130/gemini_validation_response.md:24`

### Impact
- This is a **strategic framing reversal** (caution-first vs endorsement-first).

## 4.3 Execution Response Drift (Copilot prompt)

### Topic: Bronze/Silver TE calibration
- A/B Copilot response:
  - Bronze `~1.1M`, disagrees with `~1.5M`: `gemini-cli/copilot_validation_response.md:141`
  - Silver `~2.1M`, disagrees with `~3.0M`: `gemini-cli/copilot_validation_response.md:154`
- C Copilot response:
  - Bronze `~1.5M` feasible with overhead, Silver `~3.0M` feasible with conditions: `codex-cli/runs/20260209-135130/copilot_validation_response.md:19`, `codex-cli/runs/20260209-135130/copilot_validation_response.md:20`

### Topic: Registry timing and essay timing
- A/B Copilot response:
  - Registry fix during writing: `gemini-cli/copilot_validation_response.md:367`
  - First ORGAN-V meta essay after Bronze complete: `gemini-cli/copilot_validation_response.md:384`, `gemini-cli/copilot_validation_response.md:396`
- C Copilot response:
  - Registry before first flagship publish: `codex-cli/runs/20260209-135130/copilot_validation_response.md:45`
  - Essay after 2-3 flagships (mid-Bronze): `codex-cli/runs/20260209-135130/copilot_validation_response.md:47`

### Impact
- This is a **sequencing policy shift** (later-locking vs earlier-locking).

## 5. Contradiction Matrix And Resolution

| Topic | Run A (`gemini-cli`) | Run B (`github-copilot-cli`) | Run C (`codex-cli`) | Conflict Type | Canonical Decision |
|---|---|---|---|---|---|
| Registry schema urgency | Blocker before automation | Same as A | Blocker with machine-first schema | Soft | Lock schema structure before automation; populate dynamic fields during README execution |
| Bronze budget | Mixed inside model outputs, synthesis favors Bronze-first | Same as A | Treats `~1.5M` as plausible | Hard | Plan Bronze as `1.5M` baseline with contingency band `1.1M-1.6M` |
| Silver budget | 4-5 sprint implication in synthesis | Same as A | `~3.0M` feasible if scope controlled | Soft | Keep Silver as conditional `2.1M-3.3M`, schedule against review throughput not TE alone |
| AI hiring narrative lead | Production-first caution | Same as A | More positive on meta-system as signal | Hard | Lead with deployed products + incidents; position meta-system as supporting systems-evidence |
| ORGAN-V essay timing | Process essay early; system essay later | Same as A | Essay after 2-3 flagships | Soft | Publish process essay immediately; publish system-level essay after Bronze core is demonstrably real |

## 6. Canonical Baseline (Decision Register)

1. **D-01 Registry:** adopt machine-first schema and CI linting immediately.  
Default: schema-first, data-population iterative.  
Evidence: `gemini-cli/validation_synthesis.md:97`, `codex-cli/runs/20260209-135130/codex_validation_response.md:74`.

2. **D-02 Launch Model:** execute Bronze first with tiered README depth.  
Default: `5 required + 2 stretch` flagships.  
Evidence: `gemini-cli/validation_synthesis.md:20`, `codex-cli/runs/20260209-135130/validation_synthesis.md:53`.

3. **D-03 Budgeting:** keep explicit coordination buffer as a first-class line item.  
Default: 10% coordination line item plus scenario banding for phase estimates.  
Evidence: `gemini-cli/validation_synthesis.md:27`, `codex-cli/runs/20260209-135130/validation_synthesis.md:12`.

4. **D-04 Narrative:** lead externally with shipped production evidence, not only architecture prose.  
Default: product case studies first, orchestration docs second.  
Evidence: `gemini-cli/gemini_validation_response.md:24`, `gemini-cli/gemini_validation_response.md:72`.

5. **D-05 Review Operations:** treat human review capacity as the pacing constraint.  
Default: batch reviews in small chunks and perform dedicated cross-reference pass.  
Evidence: `gemini-cli/validation_synthesis.md:206`, `gemini-cli/copilot_validation_response.md:186`.

## 7. What This Means For Your Original Question

Yes, now the comparison has been done correctly across all three macro runs:
- `gemini-cli` and `github-copilot-cli` act as one duplicated baseline set.
- `codex-cli` is the distinct rerun set.
- The final synthesis above isolates stable consensus from rerun-induced drift and resolves contradictions into one decision baseline.

## 8. Residual Unknowns / Validation Needed

1. Whether Run A and Run B are truly independent model executions or shared artifacts exported twice. Their byte-level identity suggests low independence.
2. Whether TE planning should be represented as single-point estimates or bounded scenarios in primary planning docs.
3. Whether the team wants strict Bronze = 5 or Bronze = 7 by policy; current material still mixes both.
