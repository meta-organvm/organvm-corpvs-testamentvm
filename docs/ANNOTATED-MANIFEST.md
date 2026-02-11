# Exhaustive Annotated Manifest: `ingesting-organ-document-structure/`

**Directory:** `/Users/4jp/Workspace/organvm-pactvm/ingesting-organ-document-structure`
**Total files:** 6 root files (README.md, LICENSE, CLAUDE.md, registry-v2.json, .gitignore, DIRECTORY.md) + docs/ subdirectories (genesis/4, planning/5, strategy/3, implementation/4, evaluation/4, standards/2, agents/2, archive/4, memory/1, specs/2, validation-runs/~45 files) + .config/3 + .github/4 + .github-template/(~25 templates + ~14 generated) + scripts/1 = ~120 content files
**Total size:** ~2.0 MB of documentation + templates (no runtime source code; 1 Python generator script)
**File types:** 50+ Markdown (.md), 4 JSON (.json), 2 Bash (.env/.env.local), 1 Python (.py), 7 YAML (.yml, generated), 1 text (.txt), 1 license (.txt), 6 log files (.log), 6 prompt files (.txt), 4 archived versions
**CLI validation artifacts:** `docs/validation-runs/codex-cli/` (23 files), `docs/validation-runs/gemini-cli/` (10 files), `docs/validation-runs/github-copilot-cli/` (12 files)
**Git status:** Untracked (directory exists within `organvm-pactvm` but the parent is not committed)
**Last updated:** 2026-02-10

---

## I. SYSTEM OVERVIEW

This directory is a **complete planning, evaluation, and implementation corpus** for an eight-organ creative-institutional system ("ORGAN I–VII + Meta"). It describes the architecture, governance, documentation standards, deployment automation, public narrative strategy, and independent cross-AI validation for coordinating ~44 GitHub repositories (42 unique; 14 local repos pending migration) across 8 GitHub organizations (7 organ orgs + 1 meta-org).

The system is designed to:
1. Protect distinct modes of work (theory, art, commerce, community) from collapsing into each other
2. Present the entire meta-system as a portfolio asset for grant funding, AI hiring, and residencies
3. Launch via a **tiered "Bronze" path** (5 flagships + registry + essay first) rather than all-at-once

**Current state (post-reconciliation):**
- Phase -1 (org architecture + config files): **DONE** — `.config/organvm.env`, `.config/organvm.config.json`, `.config/organvm.env.local` created
- TE conversion: **DONE** — 278 edits across 15 files by 4 parallel AI agents
- Budget reconciliation: **DONE** — all docs agree on ~4.4M TE Phase 1, ~6.5M TE total
- Independent AI cross-validation: **DONE** — 3 models × 2 runs, consensus: Bronze tier, registry hardening, 10% coordination tax
- Org rename/creation on GitHub: **NOT STARTED** — human must rename 3 orgs + create 5 new (4 organs + meta-organvm)
- Phase 0 corpus refinement: **NOT STARTED** — blocked on org rename

**Owner:** @4444j99 / @4444J99
**Launch:** Criteria-driven (per D-08 in `08-canonical-action-plan.md`)
**Total TE budget:** ~6.5M TE across 4 sprints (see TE methodology in CLAUDE.md; see `roadmap-there-and-back-again.md` for canonical timeline)
**Strategic pivot:** "Bronze" tier is the canonical launch path — "5 Perfect Repos > 44 Mediocre Repos" (post-cross-validation consensus)

---

## II. DOCUMENT-BY-DOCUMENT MANIFEST

### Layer 0: Genesis Documents (Conversational Source Material)

---

#### `00-a-system-genesis-transcript.md`
- **Size:** ~397 KB (largest file in directory)
- **Format:** Multi-turn Q&A transcript (ChatGPT-style export)
- **Role:** FOUNDATIONAL SOURCE — the original conversational genesis of the entire system
- **Content spans 6 Q&A exchanges:**
  1. **Q1:** "Ingest & digest ORGAN_i-vii___sub-ORGANS" — Initial charter analysis
     - Produces a table of all 8 organs + 3 backplanes
     - Identifies 3 pathologies the system prevents (art corrupted by commerce, theory compromised by scale, community colonized by metrics)
     - Flags 3 structural vulnerabilities (orchestration single-point failure, public process permeability, personal maintenance collapse)
     - Proposes 3 actionable decisions and 4 recommended next steps
  2. **Q2:** "Does it work as organizational framework + local workspace + GitHub orgs?" — Multi-level scalability analysis
     - Maps organ framework to local filesystem (`~/workspace/ORGAN_*/`)
     - Maps organ framework to GitHub organizations with permission model
     - Identifies integration tension: organs are governance units, not file containers
     - Recommends hybrid structure: GitHub as source of truth, local as working cache
  3. **Q3:** "Detail the promotion/graduation protocol" — State machine design
     - Defines 5 states: LOCAL → CANDIDATE → PUBLIC_PROCESS → GRADUATED → ARCHIVED
     - Each state has: location, duration, permissions, criteria, operational triggers
     - Includes promotion proposal template format
     - Defines orchestration gate mechanics (decision matrix, artifacts required)
  4. *(Continues with further refinements — file is ~500+ lines of analysis)*

- **Key annotations:**
  - This is the intellectual bedrock. All other documents derive from concepts introduced here.
  - The 8-organ model: I (Theory), II (Art), III (Commerce), IV (Orchestration), V (Public Process), VI (Community), VII (Marketing)
  - 3 backplanes: Admin/Legal/Financial, Archival/Memory/Versioning, Personal Maintenance
  - Contains the original vulnerability analysis not repeated elsewhere
  - The Q&A format means it includes both the analytical output AND the reasoning process

---

#### `00-b-local-remote-structure-transcript.md`
- **Size:** ~151 KB (second largest)
- **Format:** Multi-turn Q&A transcript
- **Role:** OPERATIONAL TRANSLATION — converts the abstract organ model into concrete filesystem/GitHub/CI tooling
- **Content spans 4+ Q&A exchanges:**
  1. **Q1:** Audio-transcribed request for local↔remote mirroring — produces ontology layers (ROOT → REALM → ORG_UNIT → REPO_UNIT → WORKSPACE_UNIT → ARTIFACT_UNIT) with 5 invariants
  2. **Environment variable contract:** `WORLD_ROOT`, `AUDIT_ROOT`, `REALMS`, `VCS_HOST`, `ORG_POLICY`
  3. **AI-handoff prompt pack:** 5-phase prompt chain (PROMPT 0–4) for terminal agents to audit `$HOME`, propose topology, generate migration plan, execute with gating
  4. **Q2:** "Design first for Claude, then Codex, then Gemini, then Copilot" — 4 tool-specific prompt adaptations
     - Claude variant: tight plan/stop/resume cycle, `.md` artifacts
     - Codex variant: two-man rule for destructive ops, task-based phases
     - Gemini variant: extensions-first approach, function declarations
     - Copilot variant: workspace/task framework, inline mode directives

- **Key annotations:**
  - Contains the only cross-tool prompt engineering in the corpus
  - The ontology layers (ROOT/REALM/ORG_UNIT/REPO_UNIT) are the naming standard all other documents reference
  - Introduces the "Russian doll" nesting metaphor that shapes the directory design
  - The directory template (`$WORLD_ROOT/realm/<realm_id>/org/<org_unit_id>/repo/<repo_unit_id>/`) is the canonical path formula
  - Includes the critical insight: "repo-inside-repo is prohibited unless declared submodule"

---

#### `00-c-master-summary.md`
- **Size:** ~16 KB
- **Format:** Structured markdown (standalone document, not Q&A)
- **Role:** EXECUTIVE SUMMARY — the "read this first" document for Phase 1 execution
- **Content:**
  - Strategic context: why Phase 1 (documentation audit) is make-or-break
  - 3 critical decisions with analysis:
    1. Personal account consolidation (Archive vs. Mirror — recommends Archive)
    2. Local repos public/private classification (per-organ visibility matrix)
    3. Empty/skeleton repos (populate 4, archive 4, merge 1 — decision matrix per repo)
  - Phase 1 structure: 6 subtasks across Sprints 1–2, ~4.4M TE total
  - Sprint 1: planning (~1.5M TE) — framework, audit, templates, checklists, risk map, setup
  - Sprint 2: execution (~2.4M TE) — README writing per organ, migration, validation
  - Success metrics: 18 checkboxes across documentation, metadata, decisions, QA
  - Effort allocation table by organ (ORGAN-I: ~850K TE, ORGAN-II: ~1,110K TE, etc.)
  - Portfolio positioning guidance for AI hiring, grants, residencies
  - Timeline: Feb 10–23, 2026
  - Common pitfalls (5) and critical success factors (5)

- **Key annotations:**
  - This is the operational entry point — designed to be read in 30 minutes
  - Contains the only explicit timeline with specific dates (Feb 10–23)
  - The decision matrices here are definitive (not repeated in later docs)
  - "Each README is a mini-portfolio piece, not just documentation" — core philosophy
  - References documents 01–05 as sequential outputs

---

#### `00-d-organ-system-audit.md`
- **Size:** ~22 KB
- **Format:** Structured markdown with tables
- **Role:** CURRENT STATE AUDIT — comprehensive inventory of existing GitHub repos mapped to organs
- **Content (8 parts):**
  1. **Executive summary:** 47 remote repos across 4 orgs + 1 personal account; "idea-rich but architecturally orphaned"
  2. **ORGAN-I audit:** 9 repos in organvm-i-theoria org — healthy but repos read as "finished products" when charter says they should "permit incompleteness"
  3. **ORGAN-II audit:** 8 repos in organvm-ii-poiesis — underdeveloped, most repos are shells, no completed art projects
  4. **ORGAN-III audit:** 12 repos in organvm-iii-ergon — healthy commercial engine, needs contract/governance docs
  5. **ORGAN-IV audit:** 3 repos — "not yet a distinct operational function," scattered across theory repos
  6. **ORGAN-V audit:** 5 repos — thin, `life-my--midst--in` is a catch-all, no structured visibility
  7. **ORGAN-VI audit:** 2 repos — not operational, no community infrastructure
  8. **ORGAN-VII audit:** 2 repos — not operational, no marketing systematization
  - **Part 2:** Organization structure assessment with tree diagrams for all 4 orgs
  - **Part 3:** Local workspace recommendation (`~/Workspace/ORGAN_*/` + `BACKPLANE/`)
  - **Part 4:** GitHub restructuring implementation plan (5 steps across 3 weeks)
  - **Part 5:** Promotion workflow with git commands (LOCAL → CANDIDATE → GRADUATED)
  - **Part 6:** Monthly audit checklist + quarterly system review
  - **Part 7:** Immediate action items (this week, next 2 weeks, by end of March)
  - **Part 8:** Expected outcome (7 guarantees) + 5 refinement questions

- **Key annotations:**
  - Date: 2025-02-02 — predates the v2 documents by ~1 year
  - Contains the most detailed per-repo status tables (repo name, org, visibility, status, type)
  - The naming pattern analysis ("Good" vs "Unclear") is only found here
  - Current org breakdown: 4444JPP (17 repos), organvm-i-theoria (16), organvm-ii-poiesis (13), organvm-iii-ergon (11)
  - The 5 refinement questions at the end were likely answered in subsequent documents

---

### Layer 1: Phase 1 Planning Documents (01–05)

These 5 documents form a sequential planning toolkit. Each is self-contained but references adjacent documents.

---

#### `01-readme-audit-framework.md`
- **Size:** ~6.7 KB
- **Format:** Structured methodology document
- **Role:** SCORING RUBRIC — defines what "comprehensive README" means quantitatively
- **Content (5 parts):**
  1. **Scoring rubric (0–100):** 4 dimensions × 20 points each
     - Existence & Accessibility (0–20): exists, title, ToC, formatting
     - Content Completeness (0–40): problem statement, installation, examples, dependencies, contributing
     - Accuracy & Currency (0–20): valid links, working code, current docs, last update
     - Portfolio Relevance (0–20): why exists, system connection, value prop, evidence
  2. **Score interpretation:** 90–100 (production-ready) → 0–39 (complete rewrite)
  3. **Organ-specific definitions:** Per-organ README requirements with minimum sections and common gaps
     - ORGAN-I: 3,000+ words, 8 required sections
     - ORGAN-II: 2,500+ words + working demos, 9 sections
     - ORGAN-III: 2,000+ words + metrics, 9 sections
     - ORGAN-IV through VII: governance/publishing/participation/strategy focused
  4. **Template instructions:** 8-step process for using templates
  5. **Quality checklist:** 10 must-have items, 6 common mistakes

- **Key annotations:**
  - The 0–100 scoring rubric is the only quantitative evaluation framework in the corpus
  - "Portfolio Relevance" as 20% of the score signals that documentation is portfolio-first
  - Each organ-specific definition includes "portfolio language" — pre-written positioning phrases
  - References Document 03 for templates and Document 04 for validation

---

#### `02-repo-inventory-audit.md`
- **Size:** ~7.7 KB
- **Format:** Structured tables
- **Role:** FULL INVENTORY — every repo numbered, scored, and actionable
- **Content:**
  - **58 total repos** (44 published + 14 local) organized by organ
  - Per-repo columns: #, name, status (✅/⚠️/❌/🔘), current score (0–100), effort estimate (TE), decision (REWRITE/REVISE/POPULATE/ARCHIVE/MERGE)
  - **ORGAN-I:** 10 repos, ~850K TE total, avg 55–70/100, all need REWRITE or REVISE
  - **ORGAN-II:** 13 repos, ~1,110K TE total, avg 0–65/100, mix of REWRITE/POPULATE/ARCHIVE/MERGE
  - **ORGAN-III:** 13 repos (incl. new commerce--meta), ~1.1M TE total, avg 15–70/100
  - **ORGAN-IV:** 3 repos, ~210K TE total
  - **ORGAN-V:** 1 repo, ~90K TE total
  - **ORGAN-VI:** 2 repos, ~120K TE total (new, TBD)
  - **ORGAN-VII:** 3 repos, ~170K TE total
  - **Local repos:** 14 repos, ~790K TE total, all audit needed
  - **Summary table:** 59 repos, ~4.4M TE total budget
  - **3 strategic decisions** repeated with recommendations

- **Key annotations:**
  - This is the operational task list — designed to be printed and checked off
  - TE budgets reflect AI-conductor model: AI generates volume, human reviews (~15 min/repo)
  - 14 local repos are placeholders (`[local-theory-1]` etc.) — not yet identified by name
  - New repo creation: `commerce--meta` (ORGAN-III governance hub, ~110K TE)
  - GitHub org names appear: `organvm-iv-taxis`, `organvm-v-logos`, `organvm-vi-koinonia`, `organvm-vii-kerygma`

---

#### `03-per-organ-readme-templates.md`
- **Size:** ~8.9 KB
- **Format:** 7 copy-paste-ready Markdown templates inside fenced code blocks
- **Role:** TEMPLATE LIBRARY — ready-to-use templates for all organ types
- **Content:**
  - Each template includes YAML frontmatter (title, organ, status, last_updated, author)
  - **ORGAN-I template:** 12 sections — Problem Statement → Core Concepts → Related Work → Installation → Examples → Downstream → Validation → Roadmap → Cross-References → Contributing → License → Author
  - **ORGAN-II template:** 12 sections — Artistic Purpose → Conceptual Approach → Technical Overview → Installation → Quick Start → Working Examples → Theory Implemented → Portfolio & Exhibition → Contributing → Related Work → License → Author
  - **ORGAN-III template:** 15 sections — Product Overview → Value Prop → Business Model → Target Users → Getting Started → Technical Architecture → Features → Case Study → Metrics → Support → Pricing → ToS → License → Contributing → Author
  - **ORGAN-IV template:** 8 sections — Purpose → Registry Overview → Governance → Key Concepts → How It Works → Example → Contributing → Author
  - **ORGAN-V template:** 8 sections — Purpose → Publishing Guidelines → Essay Structure → Essay Index → RSS → Newsletter → Contributing → Author
  - **ORGAN-VI template:** 8 sections — Purpose → Participation → Guidelines → Archive → Access → Contributing → Channels → Author
  - **ORGAN-VII template:** 10 sections — Overview → Audience → Channels → Content Types → Calendar → Templates (3) → Metrics → Analytics → Contributing → Author
  - Expected review times per AI-generated draft: ORGAN-I/III (15–20 min), ORGAN-II (20–30 min), others (10–15 min)

- **Key annotations:**
  - Templates are deliberately verbose — "customize, don't skip sections"
  - ORGAN-III is the most commercially detailed (pricing, ToS, SLA sections)
  - ORGAN-II uniquely requires demos/videos/images
  - Templates include `[bracketed instructions]` to be replaced

---

#### `04-per-organ-validation-checklists.md`
- **Size:** ~7.0 KB
- **Format:** Checkbox-based checklists per organ
- **Role:** QA PROCESS — used during peer review before committing READMEs
- **Content:**
  - **7 organ-specific checklists** with 3–4 validation categories each:
    - Content Completeness (5–9 checks per organ)
    - Accuracy & Clarity (6 checks)
    - Portfolio Relevance (4 checks)
    - Link Validation (4 checks)
    - Working Examples & Demos (ORGAN-II only, 6 checks)
    - Business Documentation / Technical Documentation / Governance (ORGAN-III, 11 checks)
  - **Per-organ "READY FOR LAUNCH" criteria** — conditions that must all be true
  - **Peer review process:** 6-step workflow (draft → review → feedback → revise → sign-off → commit)
  - **Red flags list:** 7 items that send README back for revision

- **Key annotations:**
  - ORGAN-II has the most stringent requirements (portfolio infrastructure must be complete)
  - ORGAN-III validation includes "Metrics current (within 30 days)" — a living document requirement
  - The peer review process is designed for solo operation (self-review fallback)

---

#### `05-risk-map-and-sequencing.md`
- **Size:** ~12 KB
- **Format:** Structured risk analysis + daily schedule
- **Role:** RISK MANAGEMENT + EXECUTION CALENDAR — what can go wrong and optimal daily order
- **Content (5 parts):**
  1. **Dependency map:** Foundation layer (Sprint 1 must complete before Sprint 2), within-organ dependencies, critical path
  2. **Risk assessment (7 risks):**
     - R1: Documentation burden overwhelming (60%, 5–10 day slip) — use templates, batch similar repos
     - R2: Code examples don't work (40%) — test everything
     - R3: Dependencies incomplete (low) — audit catches these
     - R4: Strategic decisions delayed (medium) — default to "Archive"
     - R5: Peer review bottleneck (medium) — self-review fallback
     - R6: Empty repo decision changes (low) — stick with decision
     - R7: Sprint 2 schedule slips (medium) — ~95K TE contingency buffer
  3. **Optimal sequencing:** Daily breakdown Mon–Sun with specific repos and TE budgets
  4. **Detailed failure scenarios (5):** Scenario A–E with problem, timeline, action, impact, prevention
  5. **Go/No-Go gates (3):**
     - Friday Feb 14 EOD (Sprint 1 gate)
     - Wednesday Feb 19 (Mid-Sprint 2 check)
     - Sunday Feb 23 EOD (Launch gate)
  - **Contingency timeline:** If slips occur, Phase 2 shifts proportionally

- **Key annotations:**
  - The daily breakdown is the most granular schedule in the corpus (per-day, per-organ, per-TE-budget)
  - Critical path insight: ORGAN-II portfolio infrastructure is the bottleneck
  - ORGAN-I and ORGAN-III can run in parallel (no dependencies between them)
  - ORGAN-IV should be done LAST (incorporates findings from all others)
  - The 3 go/no-go gates are the enforcement mechanism for the "complete before moving forward" philosophy

---

### Layer 2: Execution & Strategy Documents

---

#### `phase-1-execution-index.md`
- **Size:** ~12 KB
- **Format:** Document index with reading guide
- **Role:** NAVIGATION GUIDE — "how to use these 6 documents" meta-document
- **Content:**
  - Per-document summary (00–05): what it is, when to read it, what it contains, reading time, action items
  - **Sprint 1 workflow:** Read 00 → make decisions → read 01–02 → skim 03 → create task list → print 04 → read 05 → check go/no-go
  - **Sprint 2 workflow:** Follow daily plan (Doc 05) → write with templates (Doc 03) → review with checklists (Doc 04)
  - **Cross-reference table:** "If you need X, go to document Y"
  - **Success criteria:** 12 checkboxes for Phase 1 completion
  - **FAQ:** 6 common questions (solo vs team, word count minimums, stuck on README, etc.)
  - **Phase 2 preview:** Micro-Validation per Organ (Sprint 3, ~1.0M TE)
  - **Print recommendations:** 4 documents to print for wall reference

- **Key annotations:**
  - Total reading time for all planning documents: ~3 hours
  - Total preparation TE (Sprint 1): ~1.5M TE
  - Total execution TE (Sprint 2): ~2.4M TE (AI generation + human review + validation)
  - This document exists because the corpus is large enough to need a guide to the guide
  - "If any criterion incomplete: Phase 1 extends until complete. Don't move to Phase 2 with partial documentation."

---

#### `parallel-launch-strategy.md`
- **Size:** ~15 KB
- **Format:** Strategic overview + research-backed positioning
- **Role:** STRATEGIC RATIONALE — why parallel launch, and how to position the meta-system for external audiences
- **Content:**
  - **Why parallel:** Sequential launch delays full system visibility by 4+ weeks; parallel makes complete system visible day 1
  - **2026 landscape research:** Meta-system documentation valued by AI labs, grants, residencies
  - **Practitioner precedents:** Julian Oliver, Nicky Case, Hundred Rabbits (updated per `08-canonical-action-plan.md` §7)
  - **3 application strategies:**
    1. AI Systems Engineering (Anthropic, OpenAI, Runway) — lead with registry.json + orchestration
    2. Grant Funding (Knight, Mellon, NEA) — lead with ORGAN-V essays + organizational capacity (NSF CA deprioritized per `08` §6)
    3. Residencies (Eyebeam, Somerset House, Processing) — lead with all 8 organs as unified ecosystem
  - **3-phase implementation summary:** Phase 1 (~4.4M TE docs) → Phase 2 (~1.0M TE validation) → Phase 3 (~1.1M TE integration) = ~6.5M TE total across 4 sprints
  - **Meta-system as portfolio:** Detailed framing for hiring managers, grant reviewers, residency evaluators
  - **Timeline:** 4-week overview (Feb 10 → Mar 3 → ongoing)
  - **5 critical success factors:** documentation-first, phase isolation, all-or-nothing launch, ORGAN-V as narrative, visible decisions

- **Key annotations:**
  - This is the most externally-oriented document — written as if presenting the strategy to a stakeholder
  - The practitioner references (Oliver, Case, Hundred Rabbits — updated per `08` §7) provide art-world legitimacy at current portfolio scale
  - Contains specific application language for each target type (cover letter text, interview talking points)
  - The canonical effort estimate is ~6.5M TE across 4 sprints (see `roadmap-there-and-back-again.md`)
  - "All 8 organs must launch simultaneously, not piecemeal" — the core strategic constraint

---

### Layer 3: v2 Implementation Documents (Current Active Versions)

---

#### `implementation-package-v2.md`
- **Size:** ~23 KB
- **Format:** Comprehensive implementation plan
- **Role:** MASTER IMPLEMENTATION PLAN — the definitive "how to build this" document
- **Content:**
  - **Strategic context:** 2026 funding landscape shift (meta-system documentation valued)
  - **5 design documents described:** registry-v2.json, orchestration-system-v2.md, github-actions-spec.md, public-process-map-v2.md, this document
  - **3 application strategies** (detailed — identical to parallel-launch-strategy but with more implementation detail)
  - **Phase 1 (Sprints 1–2, ~4.4M TE):** 8 subtasks with effort breakdowns
    - 1.1: README audit template (~88K TE)
    - 1.2: Personal account & org audit (~88K TE)
    - 1.3: ORGAN-I READMEs (~850K TE)
    - 1.4: ORGAN-II READMEs (~1,110K TE)
    - 1.5: ORGAN-III READMEs (~1.1M TE)
    - 1.6: ORGAN-IV/V/VI/VII READMEs (~590K TE)
    - 1.7: GitHub org About sections (~105K TE)
    - 1.8: 14 local repos migration prep (~400K TE)
  - **Phase 2 (Sprint 3, ~1.0M TE):** Micro-validation process per organ with 5-step validation
  - **Phase 3 (Sprint 4, ~1.1M TE):** 5 subtasks — dependency validation (~88K TE), workflow deployment (~275K TE), essays (~600K TE), health check (~88K TE), launch coordination (~88K TE)
  - **Phase 1 detailed checklist:** Per-organ README requirements (checkbox format)
  - **Portfolio positioning summary:** Pre-written text for hiring, grants, residencies
  - **5 implementation risks + mitigations**
  - **Success metrics:** Launch day (8 items) + first 30 days (6 items)

- **Key annotations:**
  - Version 2.0 supersedes `archive/IMPLEMENTATION-PACKAGE.md`
  - This is the most actionable document — it has specific subtask numbers, TE estimates, and checklists
  - Phase 2 introduces "LOCKED" status per organ — a formal state machine for deployment readiness
  - Phase 3 subtask 3.2 (workflow deployment, ~275K TE) is the single largest task
  - Contains both the strategic WHY and the tactical HOW

---

#### `orchestration-system-v2.md`
- **Size:** ~17 KB
- **Format:** Governance design document
- **Role:** GOVERNANCE SPECIFICATION — how ORGAN-IV coordinates all 8 organs in parallel
- **Content:**
  - **Parallel vs. sequential comparison:** Why simultaneous launch
  - **Architecture diagram:** All 8 organs + connection model (ASCII tree)
  - **5 governance rules:**
    1. Simultaneous operational status (all or nothing)
    2. Documentation-first validation (4-step: README → micro → cross-organ → meta-docs)
    3. Registry as single source of truth (authoritative for all state)
    4. Meta-system documentation as portfolio asset (not overhead)
    5. Parallel organ dependencies (unidirectional flow: I→II→III, documented by V, amplified by VII)
  - **Promotion criteria (post-launch):** Theory→Art, Art→Commerce, All→Public Process, Public→Marketing — with example walkthrough
  - **Orchestration rules:** ORGAN-IV visibility, ORGAN-V explains ORGAN-IV, health checks across all organs
  - **Dependency model:** Intra-organ + cross-organ dependency graph with "no back-edges" rule
  - **Monthly audit specification:** Per-organ check items (ASCII pseudocode)
  - **Meta-system as strategic asset:** Framing for AI hiring, grants, residencies
  - **Registry as narrative device:** JSON structure tells a story about system organization
  - **Parallel launch checklist:** Phase 1/2/3 + Day 1 items
  - **Success metrics:** Launch (6 items) + first month (5 items)

- **Key annotations:**
  - Version 2.0 supersedes `archive/orchestration-system.md`
  - The "no back-edges" dependency rule is critical: ORGAN-III cannot depend on ORGAN-II output
  - Contains the only ASCII dependency flow diagram in the corpus
  - The promotion criteria section describes ongoing post-launch operations (not just deployment)
  - "Registry is never wrong" — the single most important invariant

---

#### `public-process-map-v2.md`
- **Size:** ~21 KB
- **Format:** Content strategy + infrastructure specification
- **Role:** ORGAN-V BLUEPRINT — how the public narrative layer works
- **Content:**
  - **2 content streams:** Meta-system essays (about the system) + product/process documentation (from organs I/II/III)
  - **Directory structure:** `public-process/` with essays/, marginalia/, case-studies/, guides/, data/, _site/, .github/workflows/
  - **5 flagship meta-system essays (detailed outlines):**
    1. "How We Orchestrate Eight Organs" (5,000 words, Day 1)
    2. "Governance as Creative Practice" (4,000 words, Day 3)
    3. "Meta-System as Portfolio Asset" (3,500 words, Week 2)
    4. "Building in Public" (3,000 words, Week 2)
    5. "Five Years of Autonomous Creative Systems" (4,500 words, Month 1)
  - **Subsidiary content:** 2 theory deep-dives, 2 art process docs, 2 commerce retrospectives
  - **12-week content calendar** (table format)
  - **Publishing infrastructure:** Jekyll static site, GitHub Pages, Atom RSS, newsletter (Substack/Ghost)
  - **Essay anatomy:** YAML frontmatter specification with all required fields
  - **RSS feed:** Full Atom 1.0 XML template
  - **Newsletter template:** Markdown format
  - **POSSE distribution:** Per-platform strategy (Mastodon, LinkedIn, Discord, Twitter) with example posts
  - **Engagement metrics:** JSON schema for tracking (views, stars, discussions, impressions, reactions)
  - **Monthly analytics report:** Auto-generated template
  - **3 automation workflows:** publish-essay.yml, generate-changelog.yml, distribute-to-channels.yml
  - **Guest contributor guidelines:** 5-step process
  - **Launch week checklist:** Days 1–7
  - **90-day success metrics:** Publishing (4), engagement (4), external application (3), audience (3)

- **Key annotations:**
  - Version 2.0 supersedes `archive/public-process-map.md`
  - The most detailed content strategy in the corpus — includes actual essay outlines with "reading hooks"
  - The POSSE (Publish Own Site, Syndicate Everywhere) model is the distribution philosophy
  - Engagement metrics schema is surprisingly detailed (per-platform, per-essay)
  - "Portfolio relevance" is a field in the essay frontmatter — every essay is tagged for external positioning
  - The 5 flagship essays total ~20,000 words — AI-generated, human-directed

---

#### `registry-v2.json`
- **Size:** ~27 KB
- **Format:** JSON data file
- **Role:** SINGLE SOURCE OF TRUTH — the canonical registry of all repos, organs, and relationships
- **Content:**
  - **Top-level metadata:** version 2.0, parallel deployment model, launch date 2026-02-10, summary stats
  - **`meta_system_portfolio_note`:** Strategic positioning context, supporting evidence (practitioner examples), strategic opportunity statement
  - **7 organ definitions** with per-organ:
    - Name, description, launch status, completion %, visibility, portfolio angle, repository count
    - Per-repository: name, org, status, public/private, description, documentation_status, portfolio_relevance
    - ORGAN-III repos additionally have: type (SaaS/B2B/B2C/internal), revenue status
    - ORGAN-V repo has: `launch_content` array (5 essay titles)
    - ORGAN-VI repos have: type (invitation-only)
  - **Repo inventory:**
    - ORGAN-I: 10 repos in organvm-i-theoria org
    - ORGAN-II: 13 repos in organvm-ii-poiesis org
    - ORGAN-III: 12 repos in organvm-iii-ergon org
    - ORGAN-IV: 3 repos (orchestration-start-here in organvm-iv-taxis, 2 in organvm-i-theoria)
    - ORGAN-V: 1 repo (public-process in organvm-v-logos)
    - ORGAN-VI: 2 repos in organvm-vi-koinonia
    - ORGAN-VII: 3 repos in organvm-vii-kerygma
  - **`local_repos_migration`:** 14 repos distributed across 6 organs
  - **`parallel_launch_implications`:** 4 advantages, 3 challenges, 1 mitigation
  - **`documentation_audit_status`:** Per-organ documentation needs
  - **`portfolio_positioning`:** Pre-written angles for hiring, grants, residencies
  - **`launch_checklist`:** Phase 1/2/3 items with TE budgets

- **Key annotations:**
  - This is the machine-readable companion to orchestration-system-v2.md
  - Every repo has a `documentation_status` field — the TODO list for Phase 1
  - `portfolio_relevance` values: CRITICAL, HIGH, MEDIUM, OPTIONAL, INTERNAL
  - 8 GitHub organizations: organvm-i-theoria, organvm-ii-poiesis, organvm-iii-ergon, organvm-iv-taxis, organvm-v-logos, organvm-vi-koinonia, organvm-vii-kerygma
  - 44 total repos across these orgs (+ 14 local = 58; document says 60 — slight discrepancy with audit doc which counts some repos differently)
  - All organ launch statuses are "OPERATIONAL" and completion "100%" — these are TARGET states, not current reality

---

#### `github-actions-spec.md`
- **Size:** ~25 KB
- **Format:** Technical specification with YAML + Python code
- **Role:** CI/CD SPECIFICATION — the 5 core GitHub Actions workflows
- **Content:**
  - **Architecture pattern:** Data-driven workflows (trigger → read registry → apply rules → execute → update)
  - **5 reusable composite actions:** fetch-registry, validate-against-rules, notify-organs, update-dependencies, log-event
  - **Workflow 1: validate-dependencies** — PR-triggered, <2 min, checks circular deps/downward flow/transitive depth
    - Full YAML with Python validation script
    - `.meta/dependencies.json` schema per repo
    - Branch protection integration
  - **Workflow 2: monthly-organ-audit** — Cron (1st of month), ~15 min, full system health check
    - Full YAML + Python audit script (`organ-audit.py`, ~60 lines)
    - Creates GitHub issue with report
    - Pushes metrics to registry audit_history
  - **Workflow 3: promote-repo** — Issue label triggered, <5 min
    - Parses promotion type from labels
    - Validates against governance criteria
    - Creates destination repo via `gh` CLI
    - Links in registry, opens cross-repo issues
    - Full YAML (~80 lines)
  - **Workflow 4: publish-process** — Issue label triggered, on-demand
    - Extracts content from source repo (README, docs, git log, CHANGELOG)
    - Generates essay outline
    - Creates draft PR in ORGAN-V repo
  - **Workflow 5: distribute-content** — Issue label triggered, on-demand
    - Extracts YAML frontmatter
    - Posts to Mastodon, adds to newsletter queue, notifies Discord
    - Tracks analytics
  - **Deployment checklist:** Pre/during/post deployment items
  - **Maintenance & monitoring:** Dashboard, alert thresholds
  - **Implementation order:** Sprint 2 (validate + pilot) → Sprint 3 (all repos + audit + promote) → Sprint 4 (publish + distribute)
  - **Success metrics:** 6 items

- **Key annotations:**
  - This is the only document with executable code (Python + YAML)
  - Version 1.0 — unchanged between v1 and v2 (noted in parallel-launch-strategy)
  - The validate-dependencies workflow is deployed to ALL repos (template distribution)
  - Uses `ORCHESTRATION_PAT` secret for cross-org operations
  - The audit script includes cycle detection (`find_cycles` function referenced but not fully implemented)
  - The POSSE distribution workflow uses Mastodon API + Discord webhook
  - Total workflow deployment: 5 workflows across ~44 repos (+ 14 local repos pending migration)

---

### Layer 3b: Execution Roadmap

---

#### `roadmap-there-and-back-again.md`
- **Size:** ~22 KB
- **Format:** Phased execution plan with tables, code blocks, and checklists
- **Role:** CANONICAL TIMELINE — the master execution roadmap from Phase -1 through Phase 3
- **Content (5 phases):**
  1. **Phase -1: Org Architecture + Naming** — Identifies naming problems (cryptic orgs, 4 non-existent), proposes env-var-based templatable naming, details the consolidation strategy (rename 3 + create 4), and provides 8 execution steps
  2. **Phase 0: Corpus Refinement + Logic Check** — Updated execution pipeline with approval gates, 8 tasks (registry update, doc search-replace, repo reconciliation, orphan classification, task manifest generation)
  3. **Phase 1: Documentation Audit (~4.4M TE)** — AI parallel streams (Claude/Gemini/Codex/Copilot), per-organ repo tables with current scores and actions, GitHub org About sections, go/no-go gates
  4. **Phase 2: Micro-Validation (~1.0M TE)** — Per-organ TE budgets and key checks, "LOCKED" status gate
  5. **Phase 3: Integration + Launch (~1.1M TE)** — Dependency validation, 5 GitHub Actions workflows, 5 flagship essays, health check + social launch
  - **Verification section:** Phase -1 completion checklist (partially complete), launch day verification (9 criteria), critical files table

- **Key annotations:**
  - This is the definitive "what happens when" document — all other plans defer to it
  - Introduces the env-var architecture design (`.config/organvm.env` → `.config/organvm.env.local` → `.config/organvm.config.json`)
  - Contains the consolidation strategy decision: rename 3 existing orgs + create 4 new (not consolidate to personal)
  - Phase -1 status: config files created, org renames NOT YET DONE on GitHub
  - The only document that maps old org names (`ivviiviivvi`, `omni-dromenon-machina`, `labores-profani-crux`) to new names
  - Documents the discovery that ORGAN-I has 18 repos on GitHub vs 10 in registry (8 unaccounted)
  - Referenced in manifest header and CLAUDE.md as "canonical timeline"

---

### Configuration Files

---

#### `.config/organvm.env`
- **Size:** ~1.9 KB
- **Format:** Bash environment variable template
- **Role:** TEMPLATE CONFIG — the reusable org-naming template that ships with the framework
- **Content:**
  - `ORGAN_PREFIX` variable (default: `organvm`)
  - 7 suffix variables with Greek ontological names and etymological comments
  - 7 derived org name variables (`ORGAN_I_ORG` through `ORGAN_VII_ORG`)
  - `PERSONAL_ACCOUNT` variable for orphan classification
  - All variables use `${VAR:-default}` pattern for override flexibility

- **Key annotations:**
  - Created during Phase -1 (2026-02-09)
  - "The template is the product. Your instance is one configuration."
  - The suffix scheme: `i-theoria`, `ii-poiesis`, `iii-ergon`, `iv-taxis`, `v-logos`, `vi-koinonia`, `vii-kerygma`
  - Committed to repo (not gitignored) — it IS the shareable template

---

#### `.config/organvm.config.json`
- **Size:** ~1.5 KB
- **Format:** JSON configuration file
- **Role:** MACHINE-READABLE ORG MAP — consumed by registry, workflows, and scripts
- **Content:**
  - `organ_prefix` field (uses `${ORGAN_PREFIX}` template variable)
  - `orgs` object mapping `ORGAN-I` through `ORGAN-VII` to: suffix, env_var name, domain label, Greek etymology

- **Key annotations:**
  - Created during Phase -1 (2026-02-09)
  - Companion to `.config/organvm.env` — same data in JSON form for programmatic consumption
  - Used by `registry-v2.json` and GitHub Actions workflows for org name resolution
  - The `domain` field provides human-readable labels (Theory, Art, Commerce, Orchestration, Public, Community, Marketing)

---

#### `.config/organvm.env.local`
- **Size:** ~537 B
- **Format:** Bash environment variable overrides
- **Role:** INSTANCE CONFIG — the user's specific org-name configuration (gitignored)
- **Content:**
  - Sets `ORGAN_PREFIX="organvm"` (user's rendering, with 'u')
  - Sets `PERSONAL_ACCOUNT="4444J99"`
  - Comment block showing the 7 resolved org names

- **Key annotations:**
  - Created during Phase -1 (2026-02-09)
  - **Gitignored** — this file contains instance-specific values, not committed
  - The distinction between `organvm` (template/framework name) and `organvm` (user's org prefix) is intentional
  - Resolves to: `organvm-i-theoria`, `organvm-ii-poiesis`, `organvm-iii-ergon`, `organvm-iv-taxis`, `organvm-v-logos`, `organvm-vi-koinonia`, `organvm-vii-kerygma`

---

### Template Infrastructure (Phase 0)

---

#### `.github-template/`
- **Role:** TEMPLATE DIRECTORY — contains all org-level GitHub configuration templates and generated output
- **Subdirectories:**
  - `profile/` — org profile README template (contains `{{VAR}}` placeholders)
  - `minimal-core/.github/` — community health file templates (CONTRIBUTING, SECURITY, CODE_OF_CONDUCT, etc.)
  - `generated/` — per-org generated output (template-config.yml and profile-README.md files)

---

#### `.github-template/profile/README.md`
- **Size:** ~1.2 KB
- **Format:** Markdown template with `{{VAR}}` placeholders
- **Role:** ORG PROFILE TEMPLATE — the source template for each org's `.github/profile/README.md`
- **Content:** Org display name, etymology, tagline, description, repos placeholder, 8-org table, footer
- **Placeholders:** `{{ORG_DISPLAY_NAME}}`, `{{ORGAN_ETYMOLOGY}}`, `{{ORGAN_TAGLINE}}`, `{{ORGAN_DESCRIPTION}}`, `{{ORG_NAME}}`, `{{TAXIS_ORG}}`
- **Key annotations:** Not used directly — `scripts/generate-github-configs.py` produces fully-resolved copies per org in `generated/`

---

#### `.github-template/meta-profile/README.md`
- **Size:** ~1.5 KB
- **Format:** Markdown template with `{{VAR}}` placeholders
- **Role:** META-ORG PROFILE TEMPLATE — the source template for the `meta-organvm/.github/profile/README.md`
- **Content:** Meta-org overview, eight-organ system summary, org table (all 8 orgs), footer
- **Key annotations:** Separate from the organ profile template because the meta-org has unique content (system overview rather than organ-specific). Generated via `scripts/generate-github-configs.py`.

---

#### `.github-template/minimal-core/.github/`
- **Format:** Markdown templates with `{{VAR}}` placeholders
- **Role:** COMMUNITY HEALTH TEMPLATES — org-level defaults for all repos within an org
- **Files:**
  - `CONTRIBUTING.md` — contribution guidelines template
  - `SECURITY.md` — security reporting policy template
  - `CODE_OF_CONDUCT.md` — Contributor Covenant v2.1 template
  - `FUNDING.yml` — sponsorship configuration (commented out by default)
  - `PULL_REQUEST_TEMPLATE.md` — PR checklist template
  - `ISSUE_TEMPLATE/bug_report.yml` — structured bug report form
  - `ISSUE_TEMPLATE/feature_request.yml` — structured feature request form
- **Placeholders:** `{{ORG_DISPLAY_NAME}}`, `{{ORG_NAME}}`, `{{TAXIS_ORG}}`, `{{CONDUCT_EMAIL}}`, `{{SUPPORT_EMAIL}}`, `{{SECURITY_EMAIL}}`
- **Key annotations:** These templates are copied to each org's `.github` repo and placeholders resolved during setup

---

#### `.github-template/generated/`
- **Format:** Generated YAML configs + Markdown profile READMEs
- **Role:** GENERATED OUTPUT — per-org resolved files produced by `scripts/generate-github-configs.py`
- **Files (per org, ×7 template-configs + ×8 profile-READMEs):**
  - `{org_name}.template-config.yml` — fully-resolved YAML config for `setup_template.py` (7 organ orgs)
  - `{org_name}.profile-README.md` — fully-resolved profile README (7 organ orgs + 1 meta-org = 8 total; no `{{VAR}}` placeholders remain)
- **Key annotations:** These files are regenerated on each script run. Do not edit manually.

---

#### `scripts/generate-github-configs.py`
- **Size:** ~7 KB
- **Format:** Python 3 script
- **Role:** TEMPLATE GENERATOR — reads `organvm.config.json` + `organvm.env.local` and produces per-org YAML configs and profile READMEs
- **Usage:** `python scripts/generate-github-configs.py [--organ ORGAN-I] [--dry-run] [--no-profile-readmes]`
- **Inputs:** `.config/organvm.config.json` (organ definitions), `.config/organvm.env.local` (resolved prefix)
- **Outputs:** 7 `*.template-config.yml` + 8 `*.profile-README.md` files (7 organ + 1 meta) in `.github-template/generated/`
- **Key annotations:** Created during Phase 0 (2026-02-10). Resolves `${ORGAN_PREFIX}` and `${PERSONAL_ACCOUNT}` from env.local, env vars, or CLI args.

---

### Layer 4: Evaluation & Cross-Validation

---

#### `06-evaluation-to-growth-analysis.md`
- **Size:** ~37 KB
- **Format:** Structured evaluation with coded findings (C1-C7, R1-R6, B1-B7, S1-S4, E1-E7)
- **Role:** INDEPENDENT EVALUATION — comprehensive critique, reinforcement, and growth analysis of the entire corpus
- **Content (4 phases):**
  1. **Post-Conversion Status Summary:** Scorecard of TE conversion (278 edits, 15 files), org architecture, budget reconciliation
  2. **Phase 1 — Evaluation:**
     - 7 Critiques: C1 (Phantom 16 repos), C2 (TE budget variance), C3 (timeline impossibility), C4 (hidden dependencies), C5 (portfolio paradox), C6 (governance without software), C7 (systematic ~13% optimism)
     - 6 Reinforcements: R1 (org architecture sound), R2 (documentation-first wise), R3 (TE model grounded), R4 (registry-as-truth elegant), R5 (tiered launch pragmatic), R6 (AI-conductor proof — the conversion itself)
     - 7 Blind Spots: B1 (human review bottleneck), B2 (code quality assumption), B3 (no rollback plan), B4 (community chicken-and-egg), B5 (marketing without audience), B6 (archive debt), B7 (coordination overhead ~5-10%)
     - 4 Shatter Points: S1 (if READMEs take 2x), S2 (if code doesn't work), S3 (if GitHub Actions fail across 7 orgs), S4 (if no one reads ORGAN-V)
  3. **Phase 2 — Growth:** 7 Execution recommendations (E1-E7)
  4. **Post-reconciliation additions:** C7, R6, B7, E7 discovered during the TE conversion process

- **Key annotations:**
  - Post-TE-conversion revision (2026-02-09) — includes findings discovered during the reconciliation itself
  - The coded finding system (C/R/B/S/E + number) is referenced throughout subsequent documents
  - C1 (Phantom 16 repos) and C7 (systematic 13% optimism) are the most impactful findings
  - R6 (AI-conductor proof) is strategically significant — the TE conversion is itself evidence the model works
  - This document is the input that drives `07-cross-ai-logic-check-prompts.md`

---

#### `07-cross-ai-logic-check-prompts.md`
- **Size:** ~22 KB
- **Format:** Three structured prompts with document attachment lists
- **Role:** VALIDATION FRAMEWORK — the exact prompts used to cross-validate the corpus via Codex, Gemini, and Copilot
- **Content:**
  - **Post-reconciliation note:** Reflects reconciled state (all TE budgets reference `02` sums)
  - **Prompt 1 (Codex — Technical Feasibility):** 6 attached documents, focuses on registry schema, GitHub Actions viability, env-var architecture
  - **Prompt 2 (Gemini — Strategic Reasoning):** 6 attached documents, focuses on portfolio positioning, grant strategy, Bronze/Silver/Gold approach
  - **Prompt 3 (Copilot — Execution Feasibility):** 6 attached documents, focuses on flagship selection, writing effort estimation, cross-references, templates
  - Each prompt includes: ordered document list, context summary, completed-so-far status, evaluation findings to validate, structured output format (AGREE/DISAGREE/ADD)

- **Key annotations:**
  - The three prompts partition the evaluation space: technical (machine correctness), strategic (positioning), execution (throughput)
  - Each prompt attaches a different subset of the corpus (~6 docs each, with `06` common to all three)
  - The AGREE/DISAGREE/ADD output format enables structured cross-comparison
  - These prompts were executed twice: Run A/B (gemini-cli + github-copilot-cli, identical) and Run C (codex-cli, different responses)
  - **Superseded by:** `08-canonical-action-plan.md` (for action items and D-register resolutions)

---

#### `07-cross-ai-logic-check-results.md`
- **Size:** ~4.7 KB
- **Format:** Executive synthesis with tables
- **Role:** EXECUTIVE VERDICT — the synthesized findings from all three AI validations
- **Content:**
  - **Executive Summary:** Architecture sound; sequential execution plan and binary launch gate unanimously rejected
  - **Verdict:** "The Eight-Organ model is sound. The All-at-Once execution is not."
  - **4 Consensus Findings:** Registry schema blocking, binary launch is critical risk, coordination overhead real (~10%), org architecture solid
  - **3 Key Disagreements + Resolutions:** Launch order (hybrid: fix registry → ORGAN-V → flagships), registry source (manual Phase 1, automate Phase 3), portfolio asset (lead with narrative, prove with code, sustain with automation)
  - **Detailed Findings per model:** Codex (pass/fail/critical add), Gemini (pass/fail/critical pivot), Copilot (pass/fail/critical fix)
  - **Action Plan ("The Bronze Sprint"):** Phase 0 (fix registry, prune, secrets), Phase 1 (essay 1 + 5 flagship READMEs), Phase 2 (deploy validate-dependencies)
  - **Revised Metrics:** ~1.5M TE Bronze + 10% overhead, 2 sprints

- **Key annotations:**
  - "5 Perfect Repos > 44 Mediocre Repos" — the Bronze philosophy
  - Supersedes previous risk assessments in `05` and `06`
  - The 5 flagship repos identified: orchestration-start-here (IV), public-process (V), auto-revision-epistemic-engine (I), core-engine (II), classroom-rpg-aetheria (III)
  - Critical strategic pivot: "Don't just document the system; document the process of building the system"
  - **Superseded by:** `08-canonical-action-plan.md` (the Bronze Sprint action plan is replaced; flagship selection is now exploration-first)

---

#### `08-canonical-action-plan.md`
- **Size:** ~24 KB
- **Format:** Structured decision document with resolved registers, consensus findings, and execution plan
- **Role:** CANONICAL ACTION PLAN — resolves all contradictions from the cross-validation cycle into the executable Bronze Sprint plan
- **Content (9 sections):**
  1. **Resolved Decisions (D-01 through D-08):** Each D-register states the contradiction, resolution, and reasoning with source citations
     - D-01: Budget correction → scenario banding (not single numbers or notes)
     - D-02: Flagship selection → deferred to exploration (not pre-selected from registry)
     - D-03: Bronze TE baseline → band 1.1M–1.6M TE
     - D-04: Narrative lead → meta-system first (AI-conductor methodology)
     - D-05: Sequencing → iterative (registry, essay, and READMEs in parallel)
     - D-06: Framework productization → yes, Phase 2
     - D-07: Tiered classification → criteria defined, assignments deferred to exploration
     - D-08: Timeline → success criteria, not sprint count
  2. **Stable Consensus (8 items):** Registry broken, Bronze is MVL, coordination overhead, TE realistic, process essay priority, human review constraint, two-pass cross-references, tiered templates
  3. **Bronze Sprint Definition:** Scope, TE budget band, success criteria (7 checkboxes)
  4. **Tiered Repo Classification:** Framework only (Flagship/Standard/Stub/Archive criteria), assignments deferred
  5. **Sequencing:** Iterative execution pattern, writing order respecting dependency flow (I→II/III→IV/V)
  6. **What NOT to Do:** 8 rejected items with sources
  7. **Unique Insights Worth Preserving:** Per-model insights from Codex, Gemini, Copilot, and cross-run comparison
  8. **Supersedes:** Table of which documents this plan updates or replaces
  9. **Provenance:** Run metadata, decision authority, synthesis agent

- **Key annotations:**
  - This is the CANONICAL document for Bronze Sprint execution — all D-registers resolved by human decision
  - Replaces `07-cross-ai-logic-check-results.md` action plan and partial aspects of `05` and `implementation-package-v2.md`
  - Key departures from cross-validation recommendations: exploration-first (not pre-selected flagships), iterative sequencing (not infrastructure-first), criteria-driven timeline (not fixed sprints), meta-system narrative lead (not production-first)
  - Source intelligence: 3 AI models × 2 runs = 6,004+ lines of validation analysis synthesized
  - The document itself is evidence of the AI-conductor model: multiple AI systems generate analysis, a coordinating AI synthesizes, and the human decides

---

### Layer 5: Cross-AI Comparison Reports

*Note: These comparison reports were previously duplicated at the repository root. The root copies have been deleted; the authoritative copies now live within their respective `docs/validation-runs/` subdirectories.*

---

#### `validation-runs/github-copilot-cli/THREE_CLI_COMPARISON_ANALYSIS.md`
- **Size:** ~36 KB (797 lines)
- **Format:** Comprehensive comparative analysis with tables, code references, and contradiction matrix
- **Role:** AUTHORITATIVE META-ANALYSIS — the definitive comparison of all three CLI validation runs
- **Content:**
  - **Executive Summary:** Critical correction — Run A/B are byte-identical, Run C is a separate rerun with different responses
  - **Directory structure overview:** validation-runs/codex-cli (22 files, 1,513 lines), validation-runs/gemini-cli (10 files, ~2,200 lines), validation-runs/github-copilot-cli (12 files, ~2,200 lines)
  - **Universal Consensus (5 items):** Registry broken, Bronze tier is MVL, coordination overhead real, TE budgets realistic, AI-conductor essay highest priority
  - **5 Major Divergences between Run A/B and Run C:** Budget correction policy, AI hiring narrative, Bronze/Silver estimates, registry/essay timing, framework productization
  - **Contradiction matrix** with canonical decisions
  - **Discovery: AI Model Non-Determinism** — same prompts, ~5.5 hours apart, different strategic recommendations

- **Key annotations:**
  - This is the PRIMARY DOCUMENT for understanding the cross-validation results
  - Documents the discovery that AI validation is non-deterministic for strategic recommendations while core technical findings remain stable
  - Contains full provenance data (tool versions, model pins, timestamps)
  - 6,004+ lines of validation analysis synthesized across three environments and two runs

---

#### `validation-runs/gemini-cli/gemini_vs_copilot_comparison.md`
- **Size:** ~3.5 KB
- **Format:** Two-way comparison with tables
- **Role:** PAIRWISE COMPARISON — Gemini CLI vs GitHub Copilot CLI synthesis comparison
- **Content:**
  - **Shared Foundations:** Binary gate fatal, Bronze is the way, registry bottleneck, 10% coordination tax
  - **Key Divergences:** Gemini prioritizes infrastructure fixes (registry schema), Copilot prioritizes AI-conductor essay (narrative leverage)
  - **Complementary Insights:** Gemini = system integrity lens, Copilot = narrative integrity lens
  - **Integrated Action Plan:** Merge both perspectives

- **Key annotations:**
  - Gemini focuses on "the framework (why)" — `organvm` as reusable toolkit
  - Copilot focuses on "the products (what)" — 12 deployed commerce products as evidence
  - Gemini flags API rate limits + secret management sprawl; Copilot flags human review fatigue

---

#### `validation-runs/codex-cli/runs/20260209-135130/three_run_comparison_report.md`
- **Size:** ~8.9 KB
- **Format:** Technical comparison with provenance, agreement classes, contradiction matrix, and decision register
- **Role:** THREE-WAY TECHNICAL COMPARISON — structured A vs B vs C analysis with canonical decisions
- **Content:**
  - **Run Inventory:** Run A (gemini-cli), Run B (github-copilot-cli), Run C (codex-cli/runs/20260209-135130)
  - **Integrity check:** A/B byte-identical on core files; C differs on all comparable files
  - **Agreement Classes:** Stable consensus (3/3), pairwise consensus (2/3), divergences (Run C only)
  - **Contradiction Matrix:** Hard conflicts and soft conflicts with resolutions
  - **5 Canonical Decision Registers (D-01 through D-05):** Formalized decisions from cross-run synthesis

- **Key annotations:**
  - The most technically rigorous comparison document (citation-level references to specific files and line numbers)
  - Establishes the baseline: A/B = same run, C = different run
  - D-01 through D-05 are the formal decision outputs of the cross-validation process

---

#### `validation-runs/gemini-cli/triptych_comparison_report.md`
- **Size:** ~4.2 KB
- **Format:** Strategic synthesis with characterization table
- **Role:** STRATEGIC TRIPTYCH — three-way persona comparison (Codex, Gemini, Copilot)
- **Content:**
  - **Meta-analysis of environments:** Gemini = structural integrity, Copilot = narrative & execution, Codex = machine correctness
  - **Triptych Consensus (4 universal invariants):** Registry broken, all-at-once impossible, coordination overhead real, AI-conductor essay high-value
  - **Divergences by persona lens**

- **Key annotations:**
  - The characterization — Codex as "rigorous engineer," Copilot as "product manager," Gemini as "architect" — provides useful mental models for interpreting each AI's output
  - All three converge on the same 4 invariants despite different analytical lenses

---

### AI Agent Documentation

---

#### `AGENTS.md`
- **Size:** ~2.5 KB
- **Format:** Structured agent guidelines
- **Role:** AGENT ONBOARDING — repository guidelines for any AI agent working in this corpus
- **Content:**
  - Project structure overview (documentation corpus, not application code)
  - Build/test commands: `rg --files`, JSON validation (`jq`, `python3 -m json.tool`), placeholder search
  - Coding style: clear Markdown, descriptive headings, follow existing filename patterns
  - Testing: documentation QA via scoring rubric, link/example accuracy, registry consistency
  - Commit guidelines: Conventional Commits, scoped to one document set
  - Security: no secrets, local overrides in `.env.local` only, `archive/` immutable

- **Key annotations:**
  - References global policy at `/Users/4jp/AGENTS.md`
  - Designed for any AI agent (not Claude-specific — contrast with `CLAUDE.md`)
  - The repo naming convention `[organ]-[type]--[specific-name]` (double-dash separator) is documented here

---

#### `GEMINI.md`
- **Size:** ~4.1 KB
- **Format:** Gemini-specific project context
- **Role:** GEMINI ONBOARDING — context document for Google Gemini AI agent
- **Content:**
  - Project overview with organ model table (8 organs + etymologies)
  - 6 key invariants (registry as truth, unidirectional deps, parallel launch, documentation-first, portfolio READMEs, promotion state machine)
  - Project structure by layer (Genesis, Planning, Strategy, v2 Active, Archive)
  - Critical files list and useful commands
  - AI-conductor workflow notes

- **Key annotations:**
  - Mirrors `CLAUDE.md` structure but shorter and Gemini-oriented
  - Contains a typo: `ποποίησις` (should be `ποίησις`) in the ORGAN-II etymology
  - References `ANNOTATED-MANIFEST.md` for complete corpus breakdown

---

### Layer 6: CLI Validation Artifacts

These three directories contain the raw inputs, outputs, and meta-analysis from two validation runs. Run A/B (gemini-cli + github-copilot-cli) are byte-identical copies of the first run. Run C (codex-cli) is a later rerun (~5.5 hours after) with different model responses, revealing AI non-determinism.

---

#### `validation-runs/codex-cli/` (22 files in `runs/20260209-135130/` + 1 root pointer)

**Run metadata:** Run ID `20260209-135130`, UTC 2026-02-09T19:15:05Z. Tools: codex-cli 0.98.0, gemini 0.27.3, gh copilot 0.0.361. Models: gpt-5 (Codex/Copilot), gemini-3-pro-preview (Gemini).

##### `validation-runs/codex-cli/LATEST_RUN.txt` (~21 B)
- Pointer file containing the path to the active run directory (`runs/20260209-135130/`)

##### `validation-runs/codex-cli/runs/20260209-135130/run-config.json` (~608 B)
- Machine-readable run metadata: run_id, timestamp, workspace path, source prompt file, model pins per AI system, command invocations for each CLI tool

##### `validation-runs/codex-cli/runs/20260209-135130/input-manifest.json` (~3.3 KB)
- SHA256 integrity hashes and file sizes for all input documents shared across 3 models, plus per-model context docs. Ensures input consistency and enables detection of input-drift in future comparisons.

##### `validation-runs/codex-cli/runs/20260209-135130/provenance.md` (~1 KB)
- Human-readable provenance record: tool versions, model pins, run timestamp, and 4 command notes (config override, extension constraints, token isolation, MCP disabling)

##### `validation-runs/codex-cli/runs/20260209-135130/codex_prompt.txt` (~5.4 KB)
- The exact prompt sent to Codex for technical feasibility validation (Prompt 1 from `07-cross-ai-logic-check-prompts.md`)

##### `validation-runs/codex-cli/runs/20260209-135130/codex_prompt_runtime.txt` (~5.5 KB)
- Codex prompt with runtime context injected (workspace path, timestamp, resolved variable values)

##### `validation-runs/codex-cli/runs/20260209-135130/codex_validation_response.raw.md` (~8.8 KB)
- Raw, unedited output from Codex (gpt-5). Preserved for reproducibility and diff comparison.

##### `validation-runs/codex-cli/runs/20260209-135130/codex_validation_response.md` (~8.8 KB)
- Cleaned Codex validation response: technical feasibility assessment using AGREE/DISAGREE/ADD format. Covers registry schema requirements, GitHub Actions viability, env-var architecture. Emphasizes schema-first approach before population.

##### `validation-runs/codex-cli/runs/20260209-135130/codex.stderr.log` (~34 KB)
- Codex CLI stderr output including tool call traces. Largest log file — includes internal reasoning and function call metadata.

##### `validation-runs/codex-cli/runs/20260209-135130/codex.stdout.log` (~8.8 KB)
- Codex CLI stdout output (the rendered response as displayed to user)

##### `validation-runs/codex-cli/runs/20260209-135130/gemini_prompt.txt` (~5.9 KB)
- The exact prompt sent to Gemini for strategic reasoning validation (Prompt 2)

##### `validation-runs/codex-cli/runs/20260209-135130/gemini_prompt_runtime.txt` (~6.0 KB)
- Gemini prompt with runtime context injected

##### `validation-runs/codex-cli/runs/20260209-135130/gemini_validation_response.raw.md` (~6.4 KB)
- Raw, unedited output from Gemini (gemini-3-pro-preview)

##### `validation-runs/codex-cli/runs/20260209-135130/gemini_validation_response.md` (~6.4 KB)
- Cleaned Gemini validation response: strategic advisory on portfolio positioning, grant strategy, narrative framing. Recommends curating planning docs into a "System Design Journal" and framing architecture as "Simulating Organizational Scale in Solo Practice."

##### `validation-runs/codex-cli/runs/20260209-135130/gemini.stderr.log` (~311 B)
- Gemini CLI stderr output (minimal — clean run)

##### `validation-runs/codex-cli/runs/20260209-135130/copilot_prompt.txt` (~6.4 KB)
- The exact prompt sent to Copilot for execution feasibility validation (Prompt 3)

##### `validation-runs/codex-cli/runs/20260209-135130/copilot_prompt_runtime.txt` (~6.6 KB)
- Copilot prompt with runtime context injected

##### `validation-runs/codex-cli/runs/20260209-135130/copilot_validation_response.raw.md` (~4.1 KB)
- Raw, unedited output from Copilot (gpt-5 via gh copilot)

##### `validation-runs/codex-cli/runs/20260209-135130/copilot_validation_response.md` (~3.7 KB)
- Cleaned Copilot validation response: execution-focused analysis covering flagship selection (7 repos), Bronze tier TE estimation (~1.5M tokens), cross-reference validation, template applicability. Recommends registry hardening before first flagship publish.

##### `validation-runs/codex-cli/runs/20260209-135130/copilot.stderr.log` (~258 B)
- Copilot CLI stderr output (minimal — clean run)

##### `validation-runs/codex-cli/runs/20260209-135130/validation_synthesis.md` (~2.9 KB)
- Cross-model synthesis for Run C: 3 consensus areas (tiered launch, coordination overhead, adaptive templates), 3 tension points (narrative-first vs infrastructure-first, numeric correction aggressiveness, README deployment timing). Includes "Additions Introduced by This Run" and "Meta-Findings."

##### `validation-runs/codex-cli/runs/20260209-135130/07-CROSS-AI-LOGIC-CHECK-RESULTS.md` (~1.6 KB)
- Executive summary for Run C: confirms architecture validity, rejects all-at-once execution, documents stable consensus and model-specific strengths (Codex=schema clarity, Gemini=strategic framing, Copilot=throughput optimization). "Practical Next Actions" section.

##### `validation-runs/codex-cli/runs/20260209-135130/three_run_comparison_report.md` (~8.9 KB)
- Three-way comparison (A vs B vs C): run provenance, integrity check (A/B identical, C different), agreement classes (3/3, 2/3, C-only), contradiction matrix with hard/soft conflicts, 5 canonical decision registers (D-01 through D-05).

---

#### `validation-runs/gemini-cli/` (10 files — Run A, the "master" first validation run)

**Run metadata:** First validation run (~13:51 UTC on 2026-02-09). Models not explicitly recorded but responses are larger and more detailed than Run C.

##### `validation-runs/gemini-cli/06-EVALUATION-TO-GROWTH-ANALYSIS.md` (~37 KB)
- Copy of `06-evaluation-to-growth-analysis.md` (now in docs/evaluation/), included as input context for the validation run.

##### `validation-runs/gemini-cli/07-CROSS-AI-LOGIC-CHECK-PROMPTS.md` (~22 KB)
- Copy of `07-cross-ai-logic-check-prompts.md` (now in docs/evaluation/), included as input context.

##### `validation-runs/gemini-cli/07-CROSS-AI-LOGIC-CHECK-RESULTS.md` (~4.7 KB)
- Executive synthesis from Run A. Content matches `07-cross-ai-logic-check-results.md` (now in docs/evaluation/). Contains the original "Bronze Sprint" action plan.

##### `validation-runs/gemini-cli/codex_validation_response.md` (~15 KB)
- Codex technical validation from Run A. Larger and more detailed than Run C's version (15 KB vs 8.8 KB). Covers the same AGREE/DISAGREE/ADD structure but with more elaboration.

##### `validation-runs/gemini-cli/gemini_validation_response.md` (~22 KB)
- Gemini strategic validation from Run A. The most detailed strategic assessment (22 KB). Covers portfolio positioning, grant strategy, practitioner positioning, Bronze/Silver/Gold approach.

##### `validation-runs/gemini-cli/copilot_validation_response.md` (~24 KB)
- Copilot execution validation from Run A. The most detailed execution analysis (24 KB). Covers flagship selection, TE estimation, cross-reference validation, template applicability, sequencing recommendations.

##### `validation-runs/gemini-cli/validation_synthesis.md` (~13.5 KB)
- Comprehensive cross-model synthesis from Run A. Significantly more detailed than Run C's version (13.5 KB vs 2.9 KB). Sections: consensus findings, key disagreements, unique insights, action conflicts, meta-findings.

##### `validation-runs/gemini-cli/analysis_differences_report.md` (~4.8 KB)
- Perspective comparison: Technical vs Strategic vs Execution lenses. Identifies key areas of disagreement between models, unique insights per model (blind spot detection), and impact assessment on the action plan.

##### `validation-runs/gemini-cli/gemini_vs_copilot_comparison.md` (~3.5 KB)
- Two-way comparison of Gemini and Copilot syntheses. Authoritative copy (root duplicate deleted).

##### `validation-runs/gemini-cli/triptych_comparison_report.md` (~4.2 KB)
- Three-way triptych synthesis. Authoritative copy (root duplicate deleted).

---

#### `validation-runs/github-copilot-cli/` (12 files — Run B, byte-identical to Run A core + 2 unique files)

**Run metadata:** Same validation run as gemini-cli (Run A/B). All 10 shared files are byte-identical to gemini-cli versions.

##### `validation-runs/github-copilot-cli/06-EVALUATION-TO-GROWTH-ANALYSIS.md` (~37 KB)
- Copy of `06-evaluation-to-growth-analysis.md` (now in docs/evaluation/). Byte-identical to gemini-cli version.

##### `validation-runs/github-copilot-cli/07-CROSS-AI-LOGIC-CHECK-PROMPTS.md` (~22 KB)
- Copy of `07-cross-ai-logic-check-prompts.md` (now in docs/evaluation/). Byte-identical to gemini-cli version.

##### `validation-runs/github-copilot-cli/07-CROSS-AI-LOGIC-CHECK-RESULTS.md` (~4.7 KB)
- Copy of `07-cross-ai-logic-check-results.md` (now in docs/evaluation/). Byte-identical to gemini-cli version.

##### `validation-runs/github-copilot-cli/codex_validation_response.md` (~15 KB)
- Codex technical validation. Byte-identical to gemini-cli version.

##### `validation-runs/github-copilot-cli/gemini_validation_response.md` (~22 KB)
- Gemini strategic validation. Byte-identical to gemini-cli version.

##### `validation-runs/github-copilot-cli/copilot_validation_response.md` (~24 KB)
- Copilot execution validation. Byte-identical to gemini-cli version.

##### `validation-runs/github-copilot-cli/validation_synthesis.md` (~13.5 KB)
- Cross-model synthesis. Byte-identical to gemini-cli version.

##### `validation-runs/github-copilot-cli/analysis_differences_report.md` (~4.8 KB)
- Perspective comparison. Byte-identical to gemini-cli version.

##### `validation-runs/github-copilot-cli/gemini_vs_copilot_comparison.md` (~3.5 KB)
- Two-way comparison. Byte-identical to gemini-cli version (root duplicate deleted).

##### `validation-runs/github-copilot-cli/triptych_comparison_report.md` (~4.2 KB)
- Triptych synthesis. Byte-identical to gemini-cli version (root duplicate deleted).

##### `validation-runs/github-copilot-cli/THREE_CLI_COMPARISON_ANALYSIS.md` (~36 KB) — **UNIQUE to this directory**
- Comprehensive 3-CLI meta-analysis (797 lines). The authoritative synthesis documenting AI model non-determinism and canonical decisions (root duplicate deleted).

##### `validation-runs/github-copilot-cli/00-MANIFEST-AND-INDEX.md` (~12.5 KB) — **UNIQUE to this directory**
- Copilot-generated manifest of its own directory: file inventory (11 documents, ~180 KB), key findings summary, reading order recommendations, relationship to sibling directories, provenance data, actionable outputs, and document status table. Self-referential meta-documentation.

---

### Layer 7: Archive (Previous Versions)

All in `archive/` subdirectory. These are v1 predecessors superseded by v2 documents.

---

#### `archive/registry.json` (~27 KB)
- v1 registry, pre-parallel-launch model
- Superseded by `registry-v2.json`

#### `archive/IMPLEMENTATION-PACKAGE.md` (~15 KB)
- v1 implementation plan (sequential launch)
- Superseded by `implementation-package-v2.md`

#### `archive/public-process-map.md` (~22 KB)
- v1 public process specification
- Superseded by `public-process-map-v2.md`

#### `archive/orchestration-system.md` (~18 KB)
- v1 orchestration governance (sequential model)
- Superseded by `orchestration-system-v2.md`

---

### Layer 8: Repository Standards & Community Health

---

#### `README.md`
- **Size:** ~5 KB (136 lines)
- **Format:** Structured markdown
- **Role:** CORPUS ENTRY POINT — the first file visitors see on GitHub
- **Content:** Project overview, eight-organ model summary, quick-start reading order, document architecture overview, links to key documents
- **Key annotations:** Points readers to `ANNOTATED-MANIFEST.md` for detailed breakdown and `00-c-master-summary.md` for executive summary

---

#### `10-repository-standards.md`
- **Size:** ~12 KB (346 lines)
- **Format:** Structured standards document with numbered sections
- **Role:** REPOSITORY STANDARDS — defines naming conventions, licensing, community health files, CI/CD, and branch protection for all 44+ repos
- **Content:** 7 sections covering repo naming patterns, license selection (CC BY-SA 4.0 for docs, MIT for code), README requirements, community health files, GitHub Actions standards, branch protection rules, and tiered compliance (Bronze/Silver/Gold)
- **Key annotations:** Extends the Phase 1 planning toolkit (numbered 10 to continue the 01–05 sequence). References `01-readme-audit-framework.md` for scoring rubric and `registry-v2.json` for repo inventory.

---

#### `11-specification-driven-development.md`
- **Size:** ~13 KB (~280 lines)
- **Format:** Structured methodology document with numbered sections
- **Role:** SDD METHODOLOGY — adapts Specification-Driven Development from code generation to documentation/governance deliverables
- **Content:** 7 sections: Purpose & Scope, Documentation Power Inversion, Three Commands (Adapted), Project Constitution, Specification Workflow, Tier-Aware Specifications, Precedence & Integration. Maps speckit concepts (features, user stories, functional requirements, tests) to organvm equivalents (deliverables, stakeholder scenarios, documentation requirements, quality gates).
- **Key annotations:** Derived from the `speckit` skill. Introduces the concept of "specifications drive documentation" (not vice versa). Defines when to use SDD vs. existing templates (`03`) — SDD for multi-deliverable sprints and cross-cutting work, templates for individual READMEs. References `memory/constitution.md` for quality gates and `specs/` for deliverable specifications.

---

#### `memory/constitution.md`
- **Size:** ~3 KB (~65 lines)
- **Format:** Structured constitutional document
- **Role:** PROJECT CONSTITUTION — immutable architectural principles governing all specifications and quality gates
- **Content:** 6 core articles (from CLAUDE.md Key Invariants), 4 amendments (from `08-canonical-action-plan.md` §2 stable consensus), 4 quality gates (Registry, Portfolio, Dependency, Completeness), governance rules for amendments.
- **Key annotations:** Referenced by `11-specification-driven-development.md` §4. Articles map directly to CLAUDE.md invariants 1–6. Amendments capture post-cross-validation additions (Bronze tier, coordination overhead, schema completeness, AI non-determinism). Quality gates are validated during `/speckit.plan` and before declaring deliverables complete.

---

#### `specs/bronze-sprint/spec.md`
- **Size:** ~7 KB (~130 lines)
- **Format:** Feature specification (adapted from speckit spec template)
- **Role:** BRONZE SPRINT SPECIFICATION — formal requirements and success criteria for the Minimum Viable Launch
- **Content:** 4 user stories (P1: Flagship READMEs, P2: Registry Schema Hardening, P3: Process Essay, P4: Cross-Reference Resolution), edge cases, 10 functional requirements (FR-001 through FR-010), key entities, 7 measurable success criteria (SC-001 through SC-007) mapped directly from `08-canonical-action-plan.md` D-08.
- **Key annotations:** First application of the SDD methodology to the organvm corpus. TE budget band: 1.1M–1.6M TE. Success criteria are identical to D-08 checkboxes — Bronze is complete when all 7 are satisfied.

---

#### `specs/bronze-sprint/checklists/requirements.md`
- **Size:** ~2 KB (~45 lines)
- **Format:** Checkbox-based validation checklist
- **Role:** BRONZE SPRINT VALIDATION — quality checklist for declaring Bronze complete
- **Content:** 5 sections: Flagship READMEs (12 checks), Registry Schema (8 checks), Process Essay (4 checks), Cross-References (3 checks), Constitution Compliance (6 checks).
- **Key annotations:** Companion to `specs/bronze-sprint/spec.md`. Every checkbox corresponds to a requirement or success criterion in the spec. Use alongside `04-per-organ-validation-checklists.md` for organ-specific validation.

---

#### `LICENSE`
- **Size:** ~14 KB (428 lines)
- **Format:** Plain text legal document
- **Role:** LICENSE — Creative Commons Attribution-ShareAlike 4.0 International (CC BY-SA 4.0)
- **Content:** Standard CC BY-SA 4.0 legalcode as published by Creative Commons
- **Key annotations:** Applies to this documentation corpus. Individual code repos may use different licenses (see `10-repository-standards.md` §2.3).

---

#### `.github/CONTRIBUTING.md`
- **Size:** ~1.5 KB
- **Format:** Structured markdown
- **Role:** CONTRIBUTING GUIDE — how to contribute corrections, suggestions, and editorial changes
- **Content:** Scope (documentation-only), correction process, suggestion process, editorial standards, commit message conventions, review process

---

#### `.github/SECURITY.md`
- **Size:** ~0.8 KB
- **Format:** Structured markdown
- **Role:** SECURITY POLICY — scoped to documentation-only repository (no deployed code)
- **Content:** Scope statement, reporting process for accidentally committed secrets, out-of-scope items

---

#### `.github/CODE_OF_CONDUCT.md`
- **Size:** ~3.2 KB
- **Format:** Contributor Covenant v2.1
- **Role:** CODE OF CONDUCT — community behavior standards
- **Content:** Standard Contributor Covenant v2.1 as published at contributor-covenant.org

---

#### `.github/PULL_REQUEST_TEMPLATE.md`
- **Size:** ~0.5 KB
- **Format:** GitHub PR template with checkboxes
- **Role:** PR TEMPLATE — checklist for documentation change pull requests
- **Content:** Summary section, documents changed section, 6-item checklist (cross-references, registry schema, archive immutability, manifest listing, naming conventions, portfolio language)

---

## III. CROSS-DOCUMENT DEPENDENCY MAP

```
00-a (Genesis Q&A) [docs/genesis/]
  ├─→ 00-b (Local/Remote Structure Q&A) [docs/genesis/]
  ├─→ 00-d (System Audit) [docs/genesis/]
  │     ├─→ registry-v2.json (machine-readable audit data) [root]
  │     └─→ orchestration-system-v2.md (governance rules) [docs/implementation/]
  └─→ 00-c (Master Summary) [docs/genesis/]
        ├─→ 01 (Scoring Framework) [docs/planning/]
        ├─→ 02 (Inventory Audit) [docs/planning/]
        ├─→ 03 (README Templates) [docs/planning/]
        ├─→ 04 (Validation Checklists) [docs/planning/]
        ├─→ 05 (Risk Map & Sequencing) [docs/planning/]
        └─→ phase-1-execution-index (Navigation Guide) [docs/strategy/]

parallel-launch-strategy (Strategic Rationale) [docs/strategy/]
  ├─→ implementation-package-v2 (How to Build) [docs/implementation/]
  ├─→ orchestration-system-v2 (How to Govern) [docs/implementation/]
  ├─→ public-process-map-v2 (How to Narrate) [docs/implementation/]
  ├─→ github-actions-spec (How to Automate) [docs/implementation/]
  └─→ registry-v2.json (What Exists) [root]

roadmap-there-and-back-again.md (Canonical Timeline) [docs/strategy/]
  ├─→ .config/organvm.env (Template Config)
  ├─→ .config/organvm.config.json (Machine-Readable Config)
  └─→ .config/organvm.env.local (Instance Config, gitignored)

06-evaluation-to-growth-analysis (Independent Evaluation) [docs/evaluation/]
  ├─→ 07-cross-ai-logic-check-prompts (Validation Prompts) [docs/evaluation/]
  │     └─→ validation-runs/{codex,gemini,github-copilot}-cli/ (Raw Validation Runs) [docs/]
  ├─→ 07-cross-ai-logic-check-results (Executive Synthesis) [docs/evaluation/]
  ├─→ THREE_CLI_COMPARISON_ANALYSIS (Authoritative Meta-Analysis) [docs/validation-runs/github-copilot-cli/]
  │     ├─→ gemini_vs_copilot_comparison (Two-Way Comparison) [docs/validation-runs/gemini-cli/]
  │     ├─→ three_run_comparison_report (Three-Way Technical Comparison) [docs/validation-runs/codex-cli/]
  │     └─→ triptych_comparison_report (Strategic Triptych) [docs/validation-runs/gemini-cli/]
  └─→ 08-canonical-action-plan (Resolves all D-registers → Bronze Sprint) [docs/evaluation/]
        └─→ 11-specification-driven-development (SDD Methodology) [docs/standards/]
              ├─→ memory/constitution.md (Project Constitution) [docs/]
              └─→ specs/bronze-sprint/ (Bronze Sprint Specification) [docs/]
                    ├─→ spec.md (Requirements & Success Criteria)
                    └─→ checklists/requirements.md (Validation Checklist)
```

---

## IV. READING ORDER (Recommended)

### Core Corpus
1. **00-c-master-summary.md** — Start here (30 min) [docs/genesis/]
2. **parallel-launch-strategy.md** — Strategic context (30 min) [docs/strategy/]
3. **00-d-organ-system-audit.md** — Current state understanding (20 min) [docs/genesis/]
4. **registry-v2.json** — Machine-readable truth (skim) [root]
5. **implementation-package-v2.md** — Execution plan (30 min) [docs/implementation/]
6. **orchestration-system-v2.md** — Governance rules (20 min) [docs/implementation/]
7. **roadmap-there-and-back-again.md** — Canonical timeline and Phase -1 details (20 min) [docs/strategy/]
8. **01 through 05** — Phase 1 planning details (as needed) [docs/planning/]
9. **public-process-map-v2.md** — Content strategy (20 min) [docs/implementation/]
10. **github-actions-spec.md** — Automation (reference only) [docs/implementation/]
11. **00-a and 00-b** — Deep genesis context (optional, 60+ min each) [docs/genesis/]

### Evaluation & Cross-Validation Layer
12. **06-evaluation-to-growth-analysis.md** — Independent evaluation (30 min) [docs/evaluation/]
13. **07-cross-ai-logic-check-results.md** — Executive verdict (10 min) [docs/evaluation/]
14. **08-canonical-action-plan.md** — Canonical action plan resolving all D-registers (20 min) [docs/evaluation/] **← START HERE for Bronze Sprint**
15. **THREE_CLI_COMPARISON_ANALYSIS.md** — Authoritative meta-analysis (30 min) [docs/validation-runs/github-copilot-cli/]
16. **three_run_comparison_report.md**, **triptych_comparison_report.md**, **gemini_vs_copilot_comparison.md** — Supporting comparisons (as needed) [docs/validation-runs/]
17. **07-cross-ai-logic-check-prompts.md** — Validation framework (reference only) [docs/evaluation/]

### SDD & Specification Layer (Bronze Sprint execution)
18. **11-specification-driven-development.md** — SDD methodology adapted for documentation (15 min) [docs/standards/]
19. **memory/constitution.md** — Project constitution: articles, amendments, quality gates (5 min) [docs/memory/]
20. **specs/bronze-sprint/spec.md** — Bronze Sprint feature specification (10 min) [docs/specs/] **← START HERE for Bronze execution**
21. **specs/bronze-sprint/checklists/requirements.md** — Bronze validation checklist (reference during QA) [docs/specs/]

### Configuration & Agent Docs (reference as needed)
22. **.config/organvm.env**, **.config/organvm.config.json**, **.config/organvm.env.local** — Org naming configuration
23. **AGENTS.md**, **GEMINI.md** — AI agent onboarding docs [docs/agents/]
24. **validation-runs/codex-cli/**, **validation-runs/gemini-cli/**, **validation-runs/github-copilot-cli/** — Raw CLI validation artifacts [docs/]

---

## V. NOTABLE PATTERNS & OBSERVATIONS

1. **Versioning discipline:** Clear v1→v2 transition with archive/ preservation; v2 = parallel launch model
2. **Redundancy by design:** Key decisions repeated across 3–4 documents for different reading contexts (executive summary, operational plan, governance spec, registry)
3. **No source code:** This is entirely planning/governance documentation — the actual repos live elsewhere
4. **Portfolio-first philosophy:** Every document frames documentation as an external-facing portfolio asset, not internal overhead
5. **AI-conductor model:** Designed for human direction with AI-parallel execution streams; human reviews AI-generated output
6. **Date context:** Documents reference Feb 2026 launch; the audit (00-d) is dated Feb 2025 — suggesting ~1 year of iterative planning
7. **Scope ambition:** 44 registered repos (42 unique), 8 orgs (8 organs + meta), 14 local migrations, 5 GitHub Actions workflows, 5 flagship essays, newsletter, RSS, POSSE distribution — within ~6.5M TE across 4 sprints
8. **The meta-system IS the work:** The documents consistently argue that orchestration/governance documentation is itself the primary artistic and professional output
9. **Cross-AI validation as methodology:** The corpus includes a complete cross-validation cycle (3 AI models × 2 runs) with provenance tracking, SHA256 integrity hashes, and non-determinism analysis — itself a portfolio piece
10. **Multi-agent layering:** Each AI agent type has its own context doc (`CLAUDE.md`, `GEMINI.md`, `AGENTS.md`) — the corpus is designed to be worked on by multiple AI systems simultaneously
11. **Env-var-first architecture:** The org naming system (`.config/organvm.env` → `.config/organvm.env.local` → `.config/organvm.config.json`) makes the entire eight-organ framework forkable — "the template is the product, your instance is one configuration"

---

## VI. QUICK REFERENCE TABLE

| File | Location | Size | Layer | Role | Read Priority |
|------|----------|------|-------|------|---------------|
| `00-a-system-genesis-transcript.md` | docs/genesis/ | 397 KB | Genesis | Foundational source | Optional |
| `00-b-local-remote-structure-transcript.md` | docs/genesis/ | 151 KB | Genesis | Operational translation | Optional |
| `00-c-master-summary.md` | docs/genesis/ | 18 KB | Genesis | Executive summary | **1st** |
| `00-d-organ-system-audit.md` | docs/genesis/ | 22 KB | Genesis | Current state audit | 3rd |
| `01-readme-audit-framework.md` | docs/planning/ | 7.4 KB | Phase 1 | Scoring rubric | As needed |
| `02-repo-inventory-audit.md` | docs/planning/ | 8.5 KB | Phase 1 | Full inventory | As needed |
| `03-per-organ-readme-templates.md` | docs/planning/ | 9.4 KB | Phase 1 | Template library | As needed |
| `04-per-organ-validation-checklists.md` | docs/planning/ | 7.5 KB | Phase 1 | QA checklists | As needed |
| `05-risk-map-and-sequencing.md` | docs/planning/ | 13 KB | Phase 1 | Risk map + calendar | As needed |
| `phase-1-execution-index.md` | docs/strategy/ | 12 KB | Execution | Navigation guide | 2nd (after 00-c) |
| `parallel-launch-strategy.md` | docs/strategy/ | 15 KB | Strategy | Strategic rationale | 2nd |
| `implementation-package-v2.md` | docs/implementation/ | 24 KB | v2 Active | Master implementation plan | 5th |
| `orchestration-system-v2.md` | docs/implementation/ | 19 KB | v2 Active | Governance specification | 6th |
| `public-process-map-v2.md` | docs/implementation/ | 21 KB | v2 Active | ORGAN-V blueprint | 9th |
| `registry-v2.json` | root | 29 KB | v2 Active | Single source of truth | 4th (skim) |
| `github-actions-spec.md` | docs/implementation/ | 26 KB | v2 Active | CI/CD specification | Reference only |
| `roadmap-there-and-back-again.md` | docs/strategy/ | 22 KB | Execution | Canonical timeline | 7th |
| `organvm.env` | .config/ | 1.9 KB | Config | Template org config | Reference |
| `organvm.config.json` | .config/ | 1.5 KB | Config | Machine-readable org map | Reference |
| `organvm.env.local` | .config/ | 537 B | Config | Instance config (gitignored) | Reference |
| `profile/README.md` | .github-template/ | 1.2 KB | Template | Org profile README template | Reference |
| `minimal-core/.github/` | .github-template/ | ~10 files | Template | Community health file templates | Reference |
| `generated/` | .github-template/ | 15 files | Generated | Per-org YAML configs + profile READMEs | Reference |
| `generate-github-configs.py` | scripts/ | ~7 KB | Script | Template generator (YAML + profile READMEs) | Reference |
| `06-evaluation-to-growth-analysis.md` | docs/evaluation/ | 37 KB | Evaluation | Independent evaluation | 12th |
| `07-cross-ai-logic-check-prompts.md` | docs/evaluation/ | 22 KB | Evaluation | Validation prompts | Reference |
| `07-cross-ai-logic-check-results.md` | docs/evaluation/ | 4.7 KB | Evaluation | Executive verdict | 13th |
| `08-canonical-action-plan.md` | docs/evaluation/ | 24 KB | Evaluation | Canonical action plan | **14th** |
| `THREE_CLI_COMPARISON_ANALYSIS.md` | docs/validation-runs/github-copilot-cli/ | 36 KB | Comparison | Authoritative meta-analysis | 15th |
| `gemini_vs_copilot_comparison.md` | docs/validation-runs/gemini-cli/ | 3.5 KB | Comparison | Two-way comparison | As needed |
| `three_run_comparison_report.md` | docs/validation-runs/codex-cli/ | 8.9 KB | Comparison | Three-way technical comparison | As needed |
| `triptych_comparison_report.md` | docs/validation-runs/gemini-cli/ | 4.2 KB | Comparison | Strategic triptych | As needed |
| `AGENTS.md` | docs/agents/ | 2.5 KB | Agent Docs | Agent onboarding guidelines | Reference |
| `GEMINI.md` | docs/agents/ | 4.1 KB | Agent Docs | Gemini-specific context | Reference |
| `CLAUDE.md` | root | 8.7 KB | Agent Docs | Claude-specific context | Reference |
| `validation-runs/codex-cli/` | docs/ | 23 files | CLI Artifacts | Run C validation (gpt-5, gemini-3-pro) | Reference |
| `validation-runs/gemini-cli/` | docs/ | 10 files | CLI Artifacts | Run A validation (master copies) | Reference |
| `validation-runs/github-copilot-cli/` | docs/ | 12 files | CLI Artifacts | Run B validation (= Run A + extras) | Reference |
| `README.md` | root | 5 KB | Standards | Corpus entry point | **1st (visitors)** |
| `DIRECTORY.md` | root | — | Standards | Concise corpus directory map | Reference |
| `10-repository-standards.md` | docs/standards/ | 12 KB | Phase 1 | Repository standards | 10th |
| `11-specification-driven-development.md` | docs/standards/ | 13 KB | Phase 1 | SDD methodology | 11th |
| `memory/constitution.md` | docs/ | 3 KB | Constitution | Project principles & gates | Reference |
| `specs/bronze-sprint/spec.md` | docs/ | 7 KB | Specs | Bronze Sprint specification | **Bronze start** |
| `specs/bronze-sprint/checklists/requirements.md` | docs/ | 2 KB | Specs | Bronze validation checklist | Bronze QA |
| `LICENSE` | root | 14 KB | Standards | CC BY-SA 4.0 | Reference |
| `.github/CONTRIBUTING.md` | root | 1.5 KB | Standards | Contributing guide | Reference |
| `.github/SECURITY.md` | root | 0.8 KB | Standards | Security policy | Reference |
| `.github/CODE_OF_CONDUCT.md` | root | 3.2 KB | Standards | Code of conduct | Reference |
| `.github/PULL_REQUEST_TEMPLATE.md` | root | 0.5 KB | Standards | PR template | Reference |
| `archive/registry.json` | docs/ | 27 KB | Archive | v1 registry | Superseded |
| `archive/IMPLEMENTATION-PACKAGE.md` | docs/ | 15 KB | Archive | v1 implementation | Superseded |
| `archive/public-process-map.md` | docs/ | 22 KB | Archive | v1 public process | Superseded |
| `archive/orchestration-system.md` | docs/ | 18 KB | Archive | v1 orchestration | Superseded |

---

## VII. KEY INVARIANTS (Cross-Document)

These rules appear in multiple documents and are never contradicted:

1. **Registry is single source of truth** — all state lives in `registry-v2.json`
2. **No back-edges in dependency graph** — ORGAN-III cannot depend on ORGAN-II; flow is I→II→III only
3. **Repo-inside-repo is prohibited** unless declared as a git submodule
4. **All 8 organs represented at launch** — each organ has at least one flagship repo
5. **Documentation precedes deployment** — no Phase 2 until Phase 1 is complete
6. **Every README is a portfolio piece** — not just internal documentation
7. **Promotion is a state machine** — LOCAL → CANDIDATE → PUBLIC_PROCESS → GRADUATED → ARCHIVED

### Post-Cross-Validation Additions (consensus from 3 AI models × 2 runs)

8. **Bronze tier is the canonical launch path** — 5 flagship repos + registry + essay first, not all 44 at once. "5 Perfect Repos > 44 Mediocre Repos." The all-at-once binary launch gate was unanimously rejected by all 3 AI validators.
9. **Coordination overhead (~10%) must be budgeted** — managing parallel AI streams requires explicit budget allocation (finding B7, validated by all 3 models)
10. **Registry schema must be hardened before execution** — current `registry-v2.json` is missing `dependencies[]`, `promotion_status`, `tier`, and `last_validated` fields required by GitHub Actions workflows
11. **AI validation is non-deterministic for strategy** — same prompts run ~5.5 hours apart produced different strategic recommendations while core technical findings remained stable (documented in `validation-runs/github-copilot-cli/THREE_CLI_COMPARISON_ANALYSIS.md`)

*Invariants 1–6 are formalized as Articles I–VI in `memory/constitution.md`. Invariants 8–11 are formalized as Amendments A–D. The constitution also defines 4 quality gates (Registry, Portfolio, Dependency, Completeness) enforced by the SDD methodology in `11-specification-driven-development.md`.*
