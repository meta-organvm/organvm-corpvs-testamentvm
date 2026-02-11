# ORGAN-IV: Orchestration System

**Status:** Design Document (Ready to Implement)  
**Version:** 1.0  
**Created:** 2026-02-03  
**Owner:** ORGAN-IV (to be established)

---

## Executive Summary

The Orchestration System governs workflow across all seven organs. It defines:
1. **Promotion criteria** — What qualifies a repo to graduate from one organ to another
2. **Dependency rules** — Cross-organ dependency tracking and validation
3. **Routing logic** — How work flows between organs
4. **Health checks** — Automated validation of system coherence

This document is the data layer for ORGAN-IV automation. Once implemented, all GitHub Actions workflows reference these rules.

---

## Table of Contents

1. [Core Concepts](#core-concepts)
2. [Promotion Criteria](#promotion-criteria)
3. [Dependency Rules](#dependency-rules)
4. [Routing Logic](#routing-logic)
5. [Health Checks & Monitoring](#health-checks--monitoring)
6. [Implementation Architecture](#implementation-architecture)

---

## Core Concepts

### Repo Lifecycle States

Every repo exists in one of these states:

```
IDEATION → SCAFFOLDING → ACTIVE → MATURE → ARCHIVED
```

**IDEATION**  
- Hypothesis stage, minimal code  
- Belongs to: ORGAN-I (Theory)  
- Requirements: README with problem statement  
- Can promote to: SCAFFOLDING (upon initial architecture design)  

**SCAFFOLDING**  
- Framework exists, examples incomplete  
- Belongs to: ORGAN-II (Art), or ORGAN-I (Theory)  
- Requirements: API documented, at least 1 working example  
- Can promote to: ACTIVE (upon working implementation with tests)  

**ACTIVE**  
- In production or regular use  
- Belongs to: ORGAN-II (Art), ORGAN-III (Commerce), ORGAN-V (Public Process)  
- Requirements: Tests pass, docs current, 30+ days updated  
- Can promote to: MATURE (upon 1+ year stability, significant usage)  

**MATURE**  
- Proven, stable, widely adopted  
- Belongs to: ORGAN-III (Commerce), ORGAN-V (Public Process)  
- Requirements: SLA-level reliability, comprehensive docs, community adoption  
- Can promote to: ARCHIVED (when sunset planned)  

**ARCHIVED**  
- End-of-life, read-only  
- Requirements: Migration path documented  
- Never promotes; can only be deleted after 6-month read-only period

### Organ Classification

Repos **primarily belong to one organ**, but can **cross-participate** in others (modeled in registry as multi-organ relationships).

**Primary organ assignment criteria:**

| Organ | Primary Type | Graduation Condition |
|-------|---|---|
| ORGAN-I (Theory) | Epistemological framework | Generalized beyond single implementation |
| ORGAN-II (Art) | Artistic system, experience, performance | Demonstrated in exhibition/performance context |
| ORGAN-III (Commerce) | Revenue product, B2B/B2C/B2B2C | Live paying customers or measurable revenue |
| ORGAN-IV (Orchestration) | Cross-organ tooling, governance, automation | Proven effective across 2+ other organs |
| ORGAN-V (Public Process) | Essays, marginalia, changelog, process docs | Published and receiving audience engagement |
| ORGAN-VI (Community) | Community infrastructure, membership, shared resources | 3+ active community members using it regularly |
| ORGAN-VII (Marketing) | Content distribution, POSSE, audience amplification | Measurable audience growth or engagement metrics |

---

## Promotion Criteria

### Theory → Art Promotion

**Condition:** A Theory framework is implemented as a concrete Art system.

**Criteria (all required):**
- [ ] Framework has been used to generate at least 1 working artwork
- [ ] Artwork demonstrates novel aesthetic or interaction model
- [ ] Code is published with example project
- [ ] GitHub repo tagged with both `ORGAN-I` and `ORGAN-II` topics
- [ ] PR opened linking theory repo to art repo (relationship documented in registry)

**Outcome:** Theory repo gains "implemented-in" cross-reference; Art repo gains "implements" cross-reference.

**Example:**
- `auto-revision-epistemic-engine` (ORGAN-I) → implemented in generative music system (ORGAN-II)
- Registry updated with bidirectional link

---

### Art → Commerce Promotion

**Condition:** An Art system is packaged as a revenue product.

**Criteria (all required):**
- [ ] System has 3+ documented use cases or examples
- [ ] Pricing model defined (if B2B/B2C) or integration path (if embedded)
- [ ] API/integration documented with >500 words of docs
- [ ] At least 1 paying customer or active deployment
- [ ] GitHub repo has commerce topic added
- [ ] Governance doc created (contract, pricing, SLA, if applicable)
- [ ] README updated with commercial terms and support model

**Outcome:** Art repo gains "commercialized" status; Commerce repo gains "derived-from" cross-reference.

**Example:**
- `core-engine` (ORGAN-II) + `metasystem-master` (ORGAN-II) → `classroom-rpg-aetheria` (ORGAN-III)

---

### Theory → Commerce Promotion (Direct)

**Condition:** A Theory framework is directly commercialized without intermediate Art step.

**Criteria (all required):**
- [ ] Framework has clear B2B/B2C application  
- [ ] Minimum viable product exists (not just theory)
- [ ] All Theory promotion criteria met
- [ ] At least 1 paying customer or funded development
- [ ] Commercial terms documented in private governance repo

**Outcome:** Commerce repo tagged with both `ORGAN-I` and `ORGAN-III` topics; dual cross-reference recorded.

**Example:**
- `call-function--ontological` (ORGAN-I) → potential direct commercialization as API service

---

### Art/Theory → Public Process Promotion

**Condition:** Development process, methodology, or learnings are documented publicly.

**Criteria (all required):**
- [ ] Essay or process document written (minimum 2,000 words)
- [ ] Document linked to source code repo
- [ ] Published in ORGAN-V public process repo
- [ ] Includes methodology, decisions, and learnings
- [ ] Receives engagement (comments, shares, citations)

**Outcome:** Source repo gains "documented-in" cross-reference; ORGAN-V repo gains "documents" cross-reference.

**Example:**
- `narratological-algorithmic-lenses` → "How We Formalized Narrative as Algorithm" essay

---

### Public Process → Marketing Promotion

**Condition:** Public process document is amplified for audience reach.

**Criteria (all required):**
- [ ] Essay published in ORGAN-V with engagement metrics
- [ ] POSSE checklist completed (cross-posted to 3+ platforms)
- [ ] Newsletter included or standalone announcement sent
- [ ] Social media amplification documented
- [ ] Minimum 50 engaged readers or equivalent metrics

**Outcome:** Document gains "distributed" status; ORGAN-VII repo records amplification details.

---

### Multi-Organ Participation

**Rules:**

1. **A repo can belong to 2 organs maximum** (except ORGAN-IV which is overhead)
   - Example: `multi-camera--livestream--framework` = ORGAN-II + ORGAN-III

2. **Primary organ is the dominant use case**
   - `multi-camera--livestream--framework` is primarily ORGAN-III (commerce product), secondarily ORGAN-II (performance platform)

3. **Cross-participation documented in registry**
   - Relationship type: "cross_organ_participation"
   - Governance: Secondary organ inherits primary organ's promotion rules

4. **Decision rule: If unsure, assign to primary revenue/impact organ**
   - Theory always primary if theoretical contribution is novel
   - Commerce always primary if revenue-generating

---

## Dependency Rules

### Dependency Graph Validation

Every repo declares its dependencies. The system validates:

```
dependency_graph = {
  repo_name: {
    depends_on: [list of upstream repos/organs],
    consumed_by: [list of downstream repos/organs],
    transitive_depth: N,  # How many hops to reach ORGAN-I
    integrity_check: PASS/WARN/FAIL
  }
}
```

### Validation Rules

1. **No Circular Dependencies**
   - If A depends on B, B cannot depend on A
   - Exception: ORGAN-IV can depend on any repo (for orchestration)
   - Automated check: Monthly GitHub Actions workflow

2. **Upward Dependencies Only**
   - ORGAN-I (Theory) depends on nothing
   - ORGAN-II (Art) can depend on ORGAN-I or other ORGAN-II
   - ORGAN-III (Commerce) can depend on ORGAN-I, ORGAN-II, or other ORGAN-III
   - ORGAN-V/VI/VII depend on any organ (they're meta-organs)
   - Automated check: Every commit via pre-push hook

3. **Depth Limits**
   - Max transitive depth: 4 hops (to keep systems modular)
   - Warning at 3 hops; error at 4+
   - Exception: ORGAN-IV orchestration workflows can traverse entire graph

4. **Breaking Change Protocol**
   - If ORGAN-I repo makes breaking change:
     - All ORGAN-II repos must be updated within 30 days
     - All ORGAN-III repos must be updated within 60 days
   - GitHub issue opened in each dependent repo
   - Orchestration system tracks compliance

### Dependency Declaration Format

Each repo has a `.meta/dependencies.json` file:

```json
{
  "repo_name": "my-awesome-engine",
  "organ": "ORGAN-I",
  "status": "ACTIVE",
  "dependencies": {
    "internal": {
      "depends_on": [
        {
          "repo": "recursive-engine--generative-entity",
          "organ": "ORGAN-I",
          "type": "hard",
          "reason": "Core algorithm"
        }
      ],
      "consumed_by": [
        {
          "repo": "generative-art-system",
          "organ": "ORGAN-II",
          "type": "hard"
        }
      ]
    },
    "external": {
      "depends_on": [
        {
          "package": "numpy",
          "version": ">=1.21.0"
        }
      ]
    }
  }
}
```

---

## Routing Logic

### Work Routing Between Organs

#### Theory → Art Pipeline

```
ORGAN-I (Hypothesis)
    ↓ [meets implementation criteria]
ORGAN-II (Artistic Implementation)
    ↓ [meets commercialization criteria]
ORGAN-III (Commercial Product)
```

**Automated routing:**
1. Theory repo tagged with `ready-for-art` label
2. Orchestration system notifies ORGAN-II maintainers
3. Art repo created with prefix matching theory repo name
4. Cross-references established automatically
5. Dependency tracking updated

#### Commerce → Public Process Pipeline

```
ORGAN-III (Deployed Product)
    ↓ [meets documentation criteria]
ORGAN-V (Public Process Essay)
    ↓ [meets distribution criteria]
ORGAN-VII (Marketing Amplification)
```

**Automated routing:**
1. Commerce repo tagged with `publishable-process` label
2. Issue opened in ORGAN-V repo for essay assignment
3. After publication, essay tagged with `ready-to-distribute`
4. ORGAN-VII workflow triggers POSSE distribution
5. Engagement metrics tracked

#### Cross-Organ Contribution Flow

```
Community Member
    ↓ [proposes improvement]
Primary Organ Repo
    ↓ [if accepted and promoted]
Secondary Organ(s)
    ↓ [amplified in]
ORGAN-VII Marketing
```

**Automated routing:**
1. PR opened in any repo with `cross-organ-impact` label
2. Orchestration validates against all dependent repos
3. If approved, automatically pings secondary organs
4. On merge, dependency graph updated
5. Marketing queue updated if impact is significant

---

## Health Checks & Monitoring

### Monthly Organ Health Audit

**Automated via GitHub Actions:** `monthly-organ-audit.yml`

Checks per organ:

**ORGAN-I (Theory)**
- [ ] All repos have updated README with problem statement
- [ ] All repos have at least 1 example or test
- [ ] No circular dependencies detected
- [ ] Cross-organ references are current
- [ ] Promotion candidates identified (ready-for-art)

**ORGAN-II (Art)**
- [ ] All repos have working example (not SKELETON)
- [ ] All repos link to parent theory (if applicable)
- [ ] All repos have demo or visualization
- [ ] Portfolio repo populated with 3+ completed works
- [ ] Promotion candidates identified (ready-for-commerce)

**ORGAN-III (Commerce)**
- [ ] All repos have SLA documentation (public or private)
- [ ] All repos have update within 60 days
- [ ] Revenue tracking sheet current
- [ ] No undocumented private repos
- [ ] Customer agreement templates updated
- [ ] Candidates for ORGAN-V process documentation identified

**ORGAN-IV (Orchestration)**
- [ ] Central registry updated
- [ ] Governance rules documentation current
- [ ] All 46 repos mapped to organs
- [ ] Dependency graph valid (no circles, correct depth)
- [ ] All GitHub Actions workflows passing
- [ ] Automation runbooks current

**ORGAN-V (Public Process)**
- [ ] 2+ essays published in past 30 days
- [ ] Each essay linked to source repo
- [ ] Engagement metrics tracked
- [ ] Newsletter/RSS generated
- [ ] Candidates for ORGAN-VII amplification identified

**ORGAN-VI (Community)**
- [ ] Discord/forum active (if applicable)
- [ ] Community guidelines current
- [ ] Member count and engagement tracked
- [ ] Contribution workflows documented

**ORGAN-VII (Marketing)**
- [ ] 3+ POSSE campaigns completed in past 30 days
- [ ] Social metrics tracked
- [ ] Audience growth metrics analyzed
- [ ] Upcoming content calendar updated
- [ ] Newsletter subscriber count tracked

### Alert Conditions

**CRITICAL (immediate action required):**
- Circular dependency detected
- Private repo without governance doc
- ORGAN-III product without customer tracking
- Public repo with secrets exposed

**WARNING (address within 2 weeks):**
- Repo exceeds 60 days without update
- SKELETON repo with no examples
- ORGAN-V essay without linked source
- Marketing queue exceeds 3 weeks backlog

**INFO (review at monthly audit):**
- New repos awaiting organ assignment
- Completed promotions to record
- Cross-organ relationships to document

---

## Implementation Architecture

### Where ORGAN-IV Lives

**Recommended:** Create new org `4444J99-orchestration` with:

```
orchestration-start-here/
├── README.md (overview, getting started)
├── registry.json (this document's data structure)
├── governance-rules.json (Promotion criteria as code)
├── dependency-manifest.json (All 46 repos' dependencies)
├── .github/
│   └── workflows/
│       ├── monthly-organ-audit.yml
│       ├── validate-dependencies.yml
│       ├── promote-repo.yml
│       ├── publish-process.yml
│       └── distribute-content.yml
├── docs/
│   ├── promotion-process.md
│   ├── dependency-rules.md
│   ├── routing-logic.md
│   └── runbooks/
│       ├── how-to-promote-art-to-commerce.md
│       ├── how-to-publish-process.md
│       └── how-to-trigger-marketing-campaign.md
└── schemas/
    ├── repo-metadata.schema.json
    ├── dependency.schema.json
    └── promotion-criteria.schema.json
```

### Data Flow

```
Central Registry (registry.json)
    ↓ [read by all workflows]
GitHub Actions Workflows
    ↓ [validate against rules]
Governance Rules Engine (governance-rules.json)
    ↓ [determine routing]
Cross-Organ Dispatch System
    ↓ [push notifications/PRs]
Individual Organ Repos
    ↓ [update dependencies]
Monthly Audit (validate entire graph)
```

### Key Workflows (to be detailed in next document)

1. **validate-dependencies.yml** — Run on every PR across all repos; block merge if dependency rules violated
2. **monthly-organ-audit.yml** — Full system health check; generate report
3. **promote-repo.yml** — Triggered by label/comment; handles organ transitions
4. **publish-process.yml** — Triggered from ORGAN-III → automates ORGAN-V essay creation
5. **distribute-content.yml** — Triggered from ORGAN-V → POSSE/newsletter distribution

---

## Implementation Sequence

### Phase 1: Foundation (Week 1)
1. Create `orchestration-start-here` repo
2. Commit registry.json and this governance document
3. Create .github/workflows directory structure
4. Tag all existing repos with organ topics in GitHub

### Phase 2: Validation (Week 2)
1. Implement validate-dependencies.yml workflow
2. Test on all 46 repos (will find current violations)
3. Document any dependency conflicts found
4. Create runbooks for resolving violations

### Phase 3: Automation (Week 3-4)
1. Implement promotion, publishing, and distribution workflows
2. Test end-to-end: Theory → Art → Commerce → Process → Marketing
3. Run full monthly audit
4. Document and deploy

### Phase 4: Continuous Operation (Ongoing)
1. Monthly audit becomes scheduled task
2. New repos automatically onboarded to system
3. Promotion requests flow through automated pipeline
4. Cross-organ collaboration facilitated by clear routing

---

## Maintenance & Evolution

### Updating Governance Rules

**Process:**
1. Propose change as GitHub issue in orchestration repo
2. Comment period: 1 week
3. Vote among organ maintainers (simple majority)
4. Update governance-rules.json
5. Workflows automatically read new version on next run

### Handling Exceptions

**One-time exceptions** (e.g., "this theory repo will never be commercialized"):
1. Document in repo's `.meta/metadata.json`
2. Reference in orchestration audit log
3. Workflow honors exception via `ignore_rule: [list]`

**Systematic exceptions** (e.g., "private repos don't need cross-references"):
1. Propose new rule
2. Update governance document
3. Commit and merge

---

## Appendix: Example Governance Rules (JSON)

```json
{
  "version": "1.0",
  "rules": {
    "theory_to_art": {
      "name": "Theory can be implemented in Art",
      "conditions": [
        "depends_on: ORGAN-I repo",
        "has: working example or artwork",
        "has: public GitHub repo",
        "status: ACTIVE",
        "updated_within_days: 60"
      ],
      "action": "promote_to_art",
      "blockers": [
        "circular dependency detected",
        "dependent repos fail tests",
        "documentation outdated"
      ]
    },
    "art_to_commerce": {
      "name": "Art can be commercialized",
      "conditions": [
        "depends_on: ORGAN-I or ORGAN-II repos",
        "has: 3+ documented use cases",
        "has: API documentation (500+ words)",
        "has: paying customer OR active deployment",
        "status: ACTIVE",
        "updated_within_days: 30"
      ],
      "action": "promote_to_commerce",
      "blockers": [
        "circular dependency",
        "governance doc missing",
        "tests failing"
      ]
    },
    "no_circular_dependencies": {
      "name": "Dependency graph must be acyclic",
      "validation": "graph_analysis.check_no_cycles()",
      "applies_to": ["all"],
      "severity": "CRITICAL",
      "auto_block_merge": true
    }
  }
}
```

---

## Status & Next Steps

**This document is complete** and ready for implementation.

**Next steps:**
1. Review with community/stakeholders
2. Create orchestration-start-here repo
3. Implement Phase 1 foundation tasks
4. Begin GitHub Actions development (see next document)

---

**Owner:** You (@4444j99)  
**Maintainer:** (to be assigned)  
**Last Updated:** 2026-02-03  
**Review Schedule:** Quarterly or upon major system change
