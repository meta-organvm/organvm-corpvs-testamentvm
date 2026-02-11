# ORGAN System Audit: Repository Mapping & Reorganization Strategy

**Date:** 2025-02-02  
**Status:** Prescriptive (ready for implementation)

---

## EXECUTIVE SUMMARY

**Current State:**
- 47 remote repositories across 4 GitHub organizations + 1 personal account
- No explicit ORGAN-based organization (repos exist in semantic chaos)
- ~70% public, ~30% private
- Heavy theory/tooling; light commerce; no community infrastructure yet
- Staging repos exist (ORG-IV/V/VI/VII) but not populated

**Key Finding:** 
Your remote repos are **idea-rich but architecturally orphaned**. They express the work (ORGAN I–VII) but lack the **governance layer** (ORGAN IV) that routes them. Local workspace should mirror this, with explicit promotion protocols.

---

## PART 1: REMOTE REPOSITORY AUDIT BY ORGAN

### ORGAN I: Conceptual / Symbolic Engine (Theory)

**Current Repos:**

| Repo | Org | Visibility | Status | Type |
|------|-----|-----------|--------|------|
| organon-noumenon--ontogenetic-morphe | 4444J99 | Public | Active | Pure Python theory |
| recursive-engine--generative-entity | 4444J99 | Public | Active | Symbolic OS framework |
| auto-revision-epistemic-engine | organvm-i-theoria | Public | Active | Self-governing orchestration (v4.2) |
| call-function--ontological | 4444J99 | Public | Active | Naming/metadata convention |
| narratological-algorithmic-lenses | 4444J99 | Public | Active | Narrative formalism + algorithms |
| cognitive-archaelogy-tribunal | organvm-i-theoria | Public | Active | System archaeology & knowledge reconstruction |
| a-i-council--coliseum | organvm-i-theoria | Public | Active | Decentralized debate framework |
| system-governance-framework | organvm-i-theoria | Public | Active | Autonomous governance theory |
| radix-recursiva-solve-coagula-redi | organvm-i-theoria | Public | Active | Alchemical transformation theory |

**Status:** ✓ Healthy population. These repos represent **unfinished symbolic work** that should mostly stay public (ORGAN V) after graduation, not jump to commerce.

**Issue:** `recursive-engine--generative-entity` and `organon-noumenon--ontogenetic-morphe` are presented as finished products (public repos with READMEs), but they read like **foundational theory in development**. Per ORGAN I charter, they should:
- Permit incompleteness and obscurity
- Not optimize for legibility
- Stay upstream of public process

**Recommendation:** These should remain **public but not promoted**. If they graduate to ORGAN V (public process), clearly mark them as "unfinished foundational work" in metadata.

---

### ORGAN II: Art / Experience / Enactment (Performance, Temporal, Experiential)

**Current Repos:**

| Repo | Org | Visibility | Status | Type |
|------|-----|-----------|--------|------|
| multi-camera--livestream--framework | organvm-iii-ergon | Public | Active | 4K live streaming + Dante sync |
| my-block-warfare | 4444J99 | Public | Active | TurfSynth AR (location-based experience) |
| example-generative-visual | organvm-ii-poiesis | Public | Empty | Placeholder for performance examples |
| example-generative-music | organvm-ii-poiesis | Public | Has code | Generative music composition |
| example-theatre-dialogue | organvm-ii-poiesis | Public | Empty | Dialogue/performance example |
| artist-toolkit-and-templates | organvm-ii-poiesis | Public | Empty | Artist templates |
| metasystem-master | organvm-ii-poiesis | Public | Active | Exhibition/presentation framework |
| performance-sdk | organvm-ii-poiesis | Public | Active | SDK for temporal performances |

**Status:** ⚠ **Underdeveloped.** Theory-heavy, but art production is light. The `organvm-ii-poiesis` org exists but most repos are shells.

**Issue:** 
- No active performance/art projects with release documentation
- Toolkits exist but no examples of their use in actual works
- `my-block-warfare` is the only concrete experiential project
- No archival of past performances

**Recommendation:** 
1. Populate `organvm-ii-poiesis` with **actual completed works** (past performances, installations, scores)
2. Create promotion strategy for theory (ORGAN I) → experiential (ORGAN II)
3. Archive completed projects separately (keep active work in main org)

---

### ORGAN III: Commerce / Applied Labor / Survival Surface

**Current Repos:**

| Repo | Org | Visibility | Status | Type |
|------|-----|-----------|--------|------|
| classroom-rpg-aetheria | organvm-iii-ergon | Public | Active | Educational game/coach interface |
| gamified-coach-interface | organvm-iii-ergon | Public | Active | Learning/coaching UI system |
| fetch-familiar-friends | organvm-iii-ergon | Public | Active | Pet calendar + social tracker |
| search-local--happy-hour | organvm-iii-ergon | Public | Active | Local search interface |
| sovereign-ecosystem--real-estate-luxury | organvm-iii-ergon | Public | Active | Real estate SaaS platform |
| trade-perpetual-future | organvm-iii-ergon | Public | Active | Crypto perpetual futures trading |
| universal-mail--automation | organvm-iii-ergon | Public | Active | Email automation tooling |
| public-record-data-scrapper | organvm-iii-ergon | Public | Active | Public records extraction (TypeScript) |
| enterprise-plugin | organvm-iii-ergon | Private | Empty | Private enterprise work |
| mirror-mirror | organvm-iii-ergon | Private | Active | Private commercial tool |
| the-invisible-ledger | organvm-iii-ergon | Private | Active | Private financial/ledger system |
| a-i--skills | 4444J99 | Public | Active | AI skills/training repo |

**Status:** ✓ **Healthy population.** This is your commercial engine. Mix of public tools and private client work.

**Issue:**
- No clear contract/client tracking linked to private repos
- Public ORGAN III repos (trade-perpetual, real-estate) lack client/revenue context
- No archival of completed client projects
- Missing: payment tracking, scope docs, IP clarification

**Recommendation:**
1. Create `backplane/admin/contracts/` with links to private repos
2. For each active ORGAN III project, document:
   - Client (or self-funded if public)
   - Contract status & dates
   - Payment terms
   - IP ownership
3. Archive completed client work (frozen) in separate location
4. Keep private repos private; don't expose client info

---

### ORGAN IV: Orchestration (Governance / Flow Control)

**Current Repos:**

| Repo | Org | Visibility | Status | Type |
|------|-----|-----------|--------|------|
| ORG-IV-orchestration-staging | (local workspace) | N/A | Empty | Placeholder |
| auto-revision-epistemic-engine | organvm-i-theoria | Public | Active | Self-orchestrating system (partial) |
| cognitive-archaelogy-tribunal | organvm-i-theoria | Public | Active | System archaeology tool |
| system-governance-framework | organvm-i-theoria | Public | Active | Governance theory |

**Status:** ⚠ **Underdeveloped.** Orchestration is **not yet a distinct operational function**. It's scattered:
- Auto-Rev-Epistemic-Engine describes an orchestration philosophy
- Cognitive-Archaeology-Tribunal is a tool for understanding current state
- System-Governance-Framework is theory, not operational practice

**Issue:** You lack a **single source of truth for routing decisions**. The ORGAN system defines boundaries, but there's no exec organ that implements them.

**Recommendation:**
1. Create formal `organ-iv-orchestration` repo (public or private) with:
   - Decision log (what promoted, when, why)
   - Dependency graph (which repos feed which)
   - Graduation criteria per organ
   - Archival index (where old work lives)
   - Promotion proposal template
2. Use this repo as the **routing hub** for the entire system
3. Make it the source of truth for permission matrix

---

### ORGAN V: Public Process / Building in Light

**Current Repos:**

| Repo | Org | Visibility | Status | Type |
|------|-----|-----------|--------|------|
| ORG-V-public-process-staging | (local workspace) | N/A | Empty | Placeholder |
| life-my--midst--in | 4444J99 | Public | Active | Personal system/journal (mixed content) |
| intake | 4444J99 | Public | Empty | Placeholder |
| for-the-record | 4444J99 | Public | Empty | Placeholder |
| a-i-chat--exporter | organvm-i-theoria | Public | Active | AI conversation export tool |
| .github (organvm-i-theoria) | organvm-i-theoria | Public | Active | Org docs & community health |

**Status:** ⚠ **Thin.** You have a few public process repos, but no systematic **visibility into thinking**.

**Issue:**
- `life-my--midst--in` is a catch-all (mixed code, journal, systems)
- No structured place for essays, marginalia, or process documentation
- Intake is empty (was meant to be inbox?)
- No visible research threads or annotation work

**Recommendation:**
1. Create `organ-v-public` repo with sections:
   - `essays/` — longer-form thinking (600+ words)
   - `marginalia/` — annotations on existing work
   - `process/` — research notes, methodology docs
   - `notebooks/` — exploratory sketches (executable if applicable)
   - `rehearsal-traces/` — documentation of works-in-progress
2. Systematize release: move things into ORGAN V as they stabilize locally
3. Link to upstream theory (ORGAN I) and downstream projects (II, III, VI)

---

### ORGAN VI: Community / Reciprocal Continuity

**Current Repos:**

| Repo | Org | Visibility | Status | Type |
|------|-----|-----------|--------|------|
| ORG-VI-community-staging | (local workspace) | N/A | Empty | Placeholder |
| collective-persona-operations | organvm-i-theoria | Public | Empty | Multi-agent identity (theory, not community) |

**Status:** ✗ **Not operational.** No community infrastructure exists.

**Issue:**
- No gated community space
- No reading groups, salons, or forums documented
- No archival of community conversations

**Recommendation:**
1. **Determine first:** Is community infrastructure urgent, or does it wait?
   - Per ORGAN VI charter, this is for **people who've already demonstrated sustained interest**
   - Don't build it yet if you don't have that audience
2. When ready, create:
   - Private Discord/forum (not GitHub, but document access rules here)
   - Archive of conversations (anonymized if needed)
   - Reading list / shared references
3. Gate access explicitly in ORGAN IV docs

---

### ORGAN VII: Marketing / Attention Routing

**Current Repos:**

| Repo | Org | Visibility | Status | Type |
|------|-----|-----------|--------|------|
| ORG-VII-marketing-staging | (local workspace) | N/A | Empty | Placeholder |
| domus-semper-palingenesis | 4444J99 | Public | Active | Dotfiles (not marketing) |

**Status:** ✗ **Not operational.** Marketing is not systematized.

**Issue:**
- You have 47 repos but no centralized announcement strategy
- No marketing automation, templates, or calendar
- Announcement logic lives in your head, not documented

**Recommendation:**
1. Create `organ-vii-marketing` repo (private or internal) with:
   - `templates/` — announcement templates (blog, social, release notes)
   - `calendar/` — release schedule for next 3–6 months
   - `automation/` — GitHub Actions, RSS feeds, social posting rules
   - `policy/` — what gets announced, when, where, to whom
2. Automate via GitHub Actions + social APIs
3. Keep it mechanical and detached (per ORGAN VII charter)

---

## PART 2: ORGANIZATION STRUCTURE ASSESSMENT

### **Current GitHub Orgs:**

```
4444J99 (Personal)
├── 17 repos (mostly theory, some tools, mix public/private)
├── Naming convention inconsistent
└── No clear ORGAN alignment

organvm-i-theoria (Org)
├── 16 repos (theory + tools, mostly public)
├── Positioned as ORGAN I symbolic engine
├── Staging repos exist but empty
└── Strong naming: a--, recursive--, auto--, etc.

organvm-ii-poiesis (Org)
├── 13 repos (art/experience framework + examples)
├── Positioned as ORGAN II experiential system
├── Most are shells or examples (underpopulated)
└── Missing: actual completed art projects

organvm-iii-ergon (Org)
├── 11 repos (all ORGAN III: commerce + tools)
├── Private repos for active commercial work
├── Well-structured, actively maintained
└── Healthy population
```

### **Current Naming Patterns:**

**Good:** `linguistic-atomization-framework`, `recursive-engine--generative-entity`, `call-function--ontological`, `multi-camera--livestream--framework`

**Unclear:** `4444JPP`, `etceter4`, `intake`, `for-the-record`, `life-my--midst--in`, `your-fit-tailored`

**Recommendation:** Rename unclear repos to follow pattern: `[organ]-[type]--[specific-name]`

---

## PART 3: LOCAL WORKSPACE RECOMMENDATION

Since your local workspace structure isn't yet materialized, here's the exact directory structure to implement:

```
~/Workspace/
├── ORGAN_I_theory/
│   ├── grammars/
│   ├── ontologies/
│   ├── symbolic-systems/
│   └── [active theory sketches, Python notebooks, unfinished papers]
│
├── ORGAN_II_art/
│   ├── performances/
│   ├── installations/
│   ├── generative-systems/
│   └── [actual art projects with scores, code, documentation]
│
├── ORGAN_III_commerce/
│   ├── client-a/ (private)
│   ├── client-b/ (private)
│   ├── tools/ (reusable, potentially public)
│   ├── [active contracts, scope docs, code]
│   └── [PRIVATE: client info, contracts, invoices]
│
├── ORGAN_IV_orchestration/
│   ├── decision-log/
│   ├── dependency-graph/
│   ├── graduation-criteria/
│   ├── archival-index/
│   ├── promotion-proposals/
│   └── [governance & routing docs]
│
├── ORGAN_V_public/
│   ├── essays/
│   ├── marginalia/
│   ├── process-notes/
│   ├── notebooks/
│   └── [visible thinking, unresolved but legible]
│
├── ORGAN_VI_community/
│   ├── reading-group-notes/
│   ├── salon-archives/
│   └── [PRIVATE: gated community space]
│
├── ORGAN_VII_marketing/
│   ├── templates/
│   ├── calendar/
│   ├── automation/
│   └── [mechanical routing logic]
│
├── BACKPLANE/
│   ├── admin/
│   │   ├── contracts/ (PRIVATE)
│   │   ├── accounting/ (PRIVATE)
│   │   └── legal/ (PRIVATE)
│   ├── archival/
│   │   ├── 2024/ [frozen completed work]
│   │   ├── 2025/ [ongoing]
│   │   └── index.md
│   └── personal/ (PRIVATE)
│       └── [infrastructure health checks, not tracked]
│
└── .organ-metadata.json [schema for all work]
```

---

## PART 4: GitHub Organization Restructuring (Implementation Plan)

### **Step 1: Rename & Consolidate (Week 1)**

**Rename** to clarify ORGAN alignment:

```
4444J99 (Personal Account)
├── Rename unclear repos:
│   ├── life-my--midst--in → org-v-personal-system-journal
│   ├── for-the-record → [ARCHIVE or DELETE if empty]
│   ├── intake → org-v-inbox
│   └── a-i--skills → org-iii-ai-training-services (if commercial)
│
└── Maintain theory repos as-is (they're clear)

organvm-i-theoria (Org) → STAYS AS-IS (good naming)

organvm-ii-poiesis (Org)
├── Populate with actual completed art projects
├── Keep examples (they serve as templates)
└── Add: `completed-works-archive/` for finished performances

organvm-iii-ergon (Org) → STAYS AS-IS (healthy)
```

### **Step 2: Create ORGAN IV Infrastructure (Week 1)**

Create **`organ-iv-orchestration`** repo in `organvm-i-theoria` org:

```
organ-iv-orchestration/
├── README.md [charter excerpt + decision protocol]
├── decision-log.md [routing decisions over time]
├── dependency-graph.json [repo relationships]
├── graduation-criteria/
│   ├── organ-i.md
│   ├── organ-ii.md
│   ├── organ-iii.md
│   └── etc.
├── promotion-template.md [template for proposals]
├── archival-index/
│   ├── 2024.md [completed work from 2024]
│   └── 2025.md [current year]
├── permission-matrix.md [who sees what]
└── .organ-metadata.json [schema definition]
```

### **Step 3: Create ORGAN V Infrastructure (Week 2)**

Create **`organ-v-public-process`** repo in `organvm-i-theoria` org:

```
organ-v-public-process/
├── essays/
│   ├── 2025-01-temporal-systems.md [unresolved thinking]
│   └── [500+ word pieces]
├── marginalia/
│   ├── [annotations on other work]
│   └── [reading notes, critique]
├── process-documentation/
│   ├── methodology-sketches/
│   └── research-threads/
├── notebooks/
│   ├── [executable Python/JS notebooks]
│   └── [exploratory code & output]
├── rehearsal-traces/
│   └── [documentation of works-in-progress]
└── README.md [invitation to think alongside]
```

### **Step 4: Archive & Freeze (Week 2–3)**

For each repo that's **completed** (not actively developed):
1. Create tag: `archived-[date]`
2. Move to `archive/[year]/` branch (or separate archive repo)
3. Mark read-only in GitHub settings
4. Add entry to `organ-iv-orchestration/archival-index/[year].md`

Example: Completed art project
```
git checkout -b archive/2024/org-ii-performance-ritual-june
git push origin archive/2024/org-ii-performance-ritual-june
[mark repo read-only in GitHub]
[add entry to archival-index]
```

### **Step 5: Populate Missing Organs (Ongoing)**

| Organ | Action | Deadline |
|-------|--------|----------|
| I (Theory) | Review ORGAN I repos; move unfinished theory to CANDIDATE state | End of Feb |
| II (Art) | Add 3–5 completed art projects to organvm-ii-poiesis | End of Mar |
| III (Commerce) | Document all active contracts in backplane/admin | Ongoing |
| IV (Orchestration) | Create decision-log with retroactive entries for past promotions | End of Feb |
| V (Public) | Seed with 5–10 essays/process docs; establish release cadence (monthly?) | Ongoing |
| VI (Community) | Skip for now; revisit when you have engaged audience | N/A |
| VII (Marketing) | Create templates and calendar; automate announcements | End of Mar |

---

## PART 5: Promotion Workflow (Git + GitHub Integration)

### **When promoting work locally → GitHub:**

```bash
# 1. Work in LOCAL state
~/Workspace/ORGAN_I_theory/grammar-sketch/
  # Edit, commit locally
  git init .
  git add .
  git commit -m "WIP: Grammar sketch v3"

# 2. Ready for review? → CANDIDATE state
# Create promotion proposal
~/Workspace/ORGAN_IV_orchestration/proposals/
  # File: org-i-theory-grammar-2025-02-proposal.md

# 3. Push to candidate branch
cd ~/Workspace/ORGAN_I_theory/grammar-sketch/
git remote add origin https://github.com/organvm-i-theoria/org-i-theory-grammar.git
git checkout -b branch/organ-i-candidate-grammar-2025-02
git push origin branch/organ-i-candidate-grammar-2025-02

# 4. GitHub issue links proposal
# Title: "Promote: grammar-sketch → PUBLIC_PROCESS / ARCHIVED / GRADUATED"
# Body: Links to proposal, graduation checklist

# 5. Orchestration approves
# Merge to main (if public) or to organ-specific branch

# 6. Tag promotion
git tag -a "org-i-theory-grammar-2025-02-promoted" -m "Promoted to ORGAN V"
git push origin --tags

# 7. Update archival index
# ~/Workspace/ORGAN_IV_orchestration/archival-index/2025.md
# - Entry: org-i-theory-grammar-sketch | PUBLIC_PROCESS | [link]
```

---

## PART 6: Key Metrics & Monitoring

### **Monthly Audit Checklist:**

- [ ] All LOCAL work is either in CANDIDATE or has explicit reason to stay LOCAL
- [ ] All CANDIDATE work is either promoted or has explicit hold reason
- [ ] All GRADUATED work is active (or marked for archival)
- [ ] Archival index is current
- [ ] No work is stuck in a state >3 months without decision
- [ ] Permission matrix (GitHub visibility) matches ORGAN assignments

### **Quarterly System Review:**

- [ ] Do the ORGAN boundaries still make sense?
- [ ] Is orchestration (ORGAN IV) actually working, or becoming bottleneck?
- [ ] Are backplane systems (admin, archival, personal) healthy?
- [ ] Has any organ become over/under-loaded?
- [ ] What patterns emerged in promotion decisions?

---

## PART 7: Immediate Action Items (Prioritized)

### **This Week (Feb 3–7):**
1. Create `organ-iv-orchestration` repo in `organvm-i-theoria`
2. Write decision-log with retrospective entries (what repos have you already promoted or archived?)
3. Create `organ-v-public-process` repo with 3 seed essays
4. Tag all **completed** projects with `archived-[date]`

### **Next 2 Weeks (Feb 10–21):**
1. Rename unclear repos (4444J99 account)
2. Populate `organvm-ii-poiesis` with 3 completed art projects
3. Create `backplane/admin/` structure with contract summary
4. Establish ORGAN VII marketing calendar + templates

### **By End of March:**
1. All active repos have `.organ-metadata.json`
2. All 47 repos are explicitly assigned to one ORGAN
3. Local workspace mirrors GitHub org structure
4. Graduation criteria are finalized for each organ

---

## PART 8: Expected Outcome

**After implementation, your system will:**

✓ Route work explicitly through orchestration (no leakage)  
✓ Make theory safe from audience optimization (ORGAN I protected)  
✓ Archive finished work systematically (nothing lost)  
✓ Gate community access properly (ORGAN VI when ready)  
✓ Keep commerce clean from art direction (III → IV → II, never direct)  
✓ Automate marketing without it colonizing creation (VII mechanical, not expressive)  
✓ Show public process without explaining everything (ORGAN V visible but unresolved)

---

## Questions for Refinement

1. **Do you have active ORGAN II (art) projects that should be in organvm-ii-poiesis?** If yes, list them.
2. **Is ORGAN VI (community) urgent, or can it wait?** Current read: you don't have a committed audience yet.
3. **For ORGAN III (commerce), which repos are actively billable?** Need this for contract documentation.
4. **Should local workspace exist locally at all, or live in GitHub?** (I assumed local mirrors GitHub, but could be ephemeral cache)
5. **Who enforces ORGAN IV decisions if you're away?** (Single point of failure if you're sole orchestrator)

---

**End of Audit**

