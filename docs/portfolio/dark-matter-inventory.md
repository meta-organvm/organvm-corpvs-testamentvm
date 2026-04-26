# 72h Dark-Matter Inventory

**Window:** 2026-04-23 → 2026-04-25
**Created:** 2026-04-25
**Source session:** S-modular-synthesis-portfolio-unification
**Authoritative atom counter:** `data/done-id-counter.json` `next_id = 480` (DONE-001..479 allocated)
**IRF range claimed:** IRF-PRT-050..074 (25 items, additive only per universal rule #3)

## Purpose

Capture work that was discussed/decided/promised in the 72h window but never received an IRF row, atom, or memory-level record. User signaled: *"there's a lot of stuff that I could tell that you're not tracking."*

## Method

1. Read all 10 session memories in window (project_session_2026-04-23* through project_session_2026-04-25_catch_all_titan_keeper.md)
2. Cross-reference against fossil-record.jsonl + IRF + git log
3. Extract items present in narrative but absent from canonical registries

## Stale-claim correction

The MEMORY.md atom counts ("47,299 unified atoms" / "24,599 triaged" / "14,898 OPEN" from `project_prompt_atomization_pipeline.md` and `project_prompt_triage_complete.md`) are pre-2026-04-23 pipeline state and have NOT been updated. The system uses DONE-NNN entries (via `done-id-counter.json`) and IRF-XXX-NNN entries (via INST-INDEX-RERUM-FACIENDARUM.md) as the authoritative work-completion + work-pending registries.

## Inventory (25 items)

| IRF ID | Item | Source session | Status notes |
|--------|------|----------------|--------------|
| IRF-PRT-050 | Spiral V5→V5.10 series (12 commits, no DONE row, no IRF entry) | `project_session_2026-04-25_v5_materia_physics.md` | Pushed to main; needs subatomic decompose to claim DONE-N range |
| IRF-PRT-051 | Jessica — no `collaborator_jessica.md`, undefined relationship/context | All session memories | Stub written 2026-04-25; full memory pending user-supplied context |
| IRF-PRT-052 | Maddie awaiting visual approval — no SLA, no escalation if >3 days silent | `project_session_2026-04-25_chakra_stars.md` | Open thread; needs polite re-ping discipline |
| IRF-PRT-053 | CF_ANALYTICS_TOKEN env var missing — Cloudflare Pages dashboard token unset | `project_session_2026-04-23_spiral_lightening.md` | Blocker mentioned, never IRF-rowed |
| IRF-PRT-054 | GH#52 CI auto-deploy broken Apr 19+ — root cause unresolved | `project_session_2026-04-25_chakra_stars.md` | Workaround active (wrangler pages deploy local); needs CLOUDFLARE_API_TOKEN rotation |
| IRF-PRT-055 | GH#3 elevatealign.com DNS — GoDaddy parking page still live | `project_artifact_handoff_elevate_align.md` | Needs Maddie+Anthony coordination, no calendar block |
| IRF-PRT-056 | Application Pipeline (28d no submission) — flagged Apr 23, no follow-up | `project_session_2026-04-23.md` | Status unknown if still stuck |
| IRF-PRT-057 | Becka McKay email send authorization — drafted, never sent (NOW PERMANENTLY CLOSED) | `project_becka_mckay_thread.md` | Closed 2026-04-25 by user; resolved as ARCHIVED, no further action |
| IRF-PRT-058 | Rob v6 strategy doc revisions — pending Rob reply, no re-ping discipline | `project_artifact_hokage_v6_refresh.md` | Open thread |
| IRF-PRT-059 | Rob 70-more-constellation profiles — homework handed off, no followup mechanism | `project_session_2026-04-25_evening_cross_pollination.md` | PRT-046 opened but no closure protocol |
| IRF-PRT-060 | Kit API key (PRT-030) — gates Hokage L2 deploy | `project_session_2026-04-25_engine_infra_landing.md` | 60s user action, no escalation if delayed |
| IRF-PRT-061 | hokagechess.com domain registration — verified AVAILABLE 2026-04-25 | `project_session_2026-04-25_handoff_relay.md` | P0 blocker, no owner assigned, time-decay risk |
| IRF-PRT-062 | Hokage OG image generation (PRT-036) — `/og.png` 1200×630 deferred | `project_session_2026-04-25_engine_infra_landing.md` | Never escalated |
| IRF-PRT-063 | Hokage mobile responsiveness QA (PRT-037) — flagged, not scoped | `project_session_2026-04-25_engine_infra_landing.md` | ~70%+ YouTube traffic mobile per Rob |
| IRF-PRT-064 | Hokage Character Sheet onboarding (PRT-039) — sketch exists, never specced | `project_session_2026-04-25_engine_infra_landing.md` | 6 chess stats sketch awaiting wireframe |
| IRF-PRT-065 | Filter affiliate URLs (GH#49) — waiting on Maddie filter-info | `project_artifact_handoff_elevate_align.md` | Open since Apr 23, no SLA |
| IRF-PRT-066 | Lambda/cost optimization decision — scope unclear, no owner | `project_session_2026-04-25_hokage_chess_pde.md` | Hokage context, undecided |
| IRF-PRT-067 | Portfolio-site CI honesty repair (DONE-479) — no session memory written | `project_artifact_catch_all_relay_2026-04-25.md` | Work shipped via relay reception but continuity record missing |
| IRF-PRT-068 | Stale-propagation root cause — diagnosed but `organvm relay draft` CLI unbuilt | `project_session_2026-04-25_catch_all_titan_keeper.md` | Stream Τ owns the build |
| IRF-PRT-069 | Titan-keeper architecture — SPEC ONLY; 5 follow-up CLIs unbuilt | `~/.claude/plans/2026-04-25-titan-keeper-architecture.md` | Chronos / Hermes / persona-router / PreToolUse keeper-guard / ID-claim primitive |
| IRF-PRT-070 | Scott Lefler iMessage decision packet — drafted, awaiting send authorization | `project_scott_lefler_verification_20260425.md` | User decision pending |
| IRF-PRT-071 | MEMORY.md local:remote sync violations — pattern not prevented despite recurrence | `project_session_2026-04-25_evening_cross_pollination.md` | Per universal rule #2 enforcement gap |
| IRF-PRT-072 | DONE-475/476 collision incident — counter protocol documented but NOT enforced by hook | `project_session_2026-04-25_catch_all_titan_keeper.md` | Pre-commit hook is part of Stream Τ |
| IRF-PRT-073 | Registry schema ambiguities — `organ` field, `status` vs `promotion_status` — no formal spec | `project_session_2026-04-25_handoff_relay.md` | Conservative defaults chosen without formal spec |
| IRF-PRT-074 | Persons-index meta-pattern — humans named but never indexed (Jessica + future) | All session memories | Process gap: any named human should auto-trigger collaborator memory creation |

## Subatomic-decomposition candidates (for Stream Ω)

Top-5 densest sessions, with predicted sub-atom counts (totals 38):

| Session memory | Predicted sub-atoms |
|----------------|---------------------|
| `project_session_2026-04-25_v5_materia_physics.md` | 11 (V5.0 nested solar systems, V5.1 physics-driven orbits, V5.2 transparent vessel, V5.3 boundary containment, V5.4 99% volumetric fill, V5.5 raycast inside-test, V5.6 phase-particle physics, V5.7 vessel removal, V5.8 spring-bound 600-particle physics, V5.9 bouncing-substrate, V5.10 bloom kill + normal blending) |
| `project_session_2026-04-25_engine_infra_landing.md` | 8 (landing-engine plan, ChatGPT multi-part adapter, Claude multi-part mirror, hanging-items plan, resolve-bootstrap, chatgpt_exporter_to_bundle, spiral landing-engine slice 1, hokage landing-engine slice 3) |
| `project_session_2026-04-23.md` | 7 (ChatGPT export pipeline, Claude/Copilot/Gemini dedup, 11,979 task prioritization rubric, Trinity dispatch protocol, Gmail OAuth refresh, 224+ email triage SOP, CI fixes) |
| `project_session_2026-04-25_hokage_chess_pde.md` | 6 (market-gap synthesis, course design SOP, trademark risk matrix, price ladder design, PDE 4-modes formalization, 49-file repo merge) |
| `project_session_2026-04-25_handoff_relay.md` | 6 (PDE skill scaffold, spiral mobile viewport tuning, hokage seed.yaml + Rob 30-day playbook, registry registration, OG metadata layout enhancement, 51-plan chezmoi sync) |

## Tooling gaps (Stream Τ targets)

5 CLIs do not exist; their absence is what allowed this dark matter to accumulate:

1. `organvm sessions audit --since <duration>` — would surface session memories without IRF backing
2. `organvm subatomic decompose <session-id>` — would propose sub-atom boundaries by narrative breaks + commit counts
3. `organvm memory triangulate <window>` — would cross-check items across atoms / IRF / git / GH
4. `organvm relay draft <relay-file>` — would validate sister relays against current disk state
5. `organvm atoms pipeline --verify` — would ensure every DONE-N has matching commit + handoff + memory

Plus:
- Pre-commit hook for `done-id-counter.json` collision guard (prevents DONE-475/476-class incidents)
- Session-boundary detector (catches multi-session work conflated as one memory)

## Verification

- [ ] All 25 IRF-PRT-050..074 rows appear in INST-INDEX-RERUM-FACIENDARUM.md
- [ ] After Stream Τ ships, `organvm memory triangulate --since 72h` returns 0 single-location entries (excluding the 25 in this inventory, which are now triple-referenced)
- [ ] Stream Ω closes the 38 subatomic-decompose candidates as DONE-N entries

## Cross-references

- Plan: `~/.claude/plans/okay-so-now-harmonic-kettle.md`
- Sister docs: `parameter-matrix.md`, `framework-stack.md`
- IRF source: `~/Workspace/organvm/organvm-corpvs-testamentvm/INST-INDEX-RERUM-FACIENDARUM.md`
