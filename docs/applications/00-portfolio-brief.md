# Portfolio Brief: The Eight-Organ System

**For:** All application tracks (AI roles, grants, residencies)
**Updated:** 2026-02-11
**Status:** LAUNCHED — all 8 organs OPERATIONAL

---

## One-Paragraph Summary

I designed and implemented an eight-organ orchestration system that coordinates 78 repositories across 8 GitHub organizations — spanning theory, generative art, commercial products, governance, public process, community, and marketing. The system includes a machine-readable registry, automated dependency validation, a formal promotion state machine (LOCAL -> CANDIDATE -> PUBLIC_PROCESS -> GRADUATED -> ARCHIVED), and 5 GitHub Actions workflows for autonomous governance. It is fully documented at ~289K words and validated by automated scripts that check every repository for CI/CD, documentation, dependency integrity, and constitutional compliance.

---

## System at a Glance

| Dimension | Value |
|-----------|-------|
| Total repositories | 78 (+ 2 planned) |
| GitHub organizations | 8 |
| Documentation | ~289,000 words |
| CI/CD coverage | 65 repos with workflows |
| Validation scripts | 5 automated, all passing |
| Meta-system essays | 10 published (~40K words) |
| Dependency edges | 31, all validated |
| Back-edge violations | 0 |
| Circular dependencies | 0 |
| Implementation status | 29 PRODUCTION, 10 PROTOTYPE, 21 SKELETON, 20 DESIGN_ONLY |

---

## The Eight Organs

| # | Organ | Domain | Repos | What It Demonstrates |
|---|-------|--------|-------|----------------------|
| I | Theoria | Theory & epistemology | 18 | Intellectual depth, foundational thinking, recursive systems |
| II | Poiesis | Generative art & performance | 21 | Creative systems design, artistic infrastructure |
| III | Ergon | Commerce & products | 21 | Product-market thinking, revenue generation, deployment |
| IV | Taxis | Orchestration & governance | 9 | Systems architecture, governance design, organizational capacity |
| V | Logos | Public process & essays | 2 | Transparency, thought leadership, building in public |
| VI | Koinonia | Community | 3 | Collaborative infrastructure, community contribution |
| VII | Kerygma | Marketing & distribution | 4 | Audience building, POSSE automation, content strategy |
| VIII | Meta | Umbrella coordination | 2 | Cross-system integration, meta-documentation |

---

## Key Technical Achievements

### Orchestration Architecture
- **Central registry** (`registry-v2.json`): Single source of truth for all 78 repos — status, dependencies, documentation, tier, promotion state
- **Dependency validation**: Automated checks enforce no back-edges in I->II->III chain, no circular dependencies, transitive depth <= 4
- **Promotion state machine**: Formal governance pipeline (LOCAL -> CANDIDATE -> PUBLIC_PROCESS -> GRADUATED -> ARCHIVED) with automated workflows

### Automation Stack
- **5 GitHub Actions workflows**: validate-dependencies, monthly-organ-audit, promote-repo, publish-process, distribute-content
- **Organ audit script**: Full system health check across all 8 organs with Markdown report + JSON metrics
- **POSSE distribution**: Automated content distribution to Mastodon, Discord, newsletter

### Flagship Projects
- **recursive-engine--generative-entity** (ORGAN-I): Symbolic operating system — 1,254 tests, 85% coverage, 21 organ handlers
- **agentic-titan** (ORGAN-IV): Multi-agent orchestration framework — 1,095 tests, 18 development phases
- **metasystem-master** (ORGAN-II): Generative art meta-system, the creative engine connecting theory to practice
- **public-record-data-scrapper** (ORGAN-III): Civic tech data pipeline, deployed and serving users

---

## Positioning by Track

### AI Engineering Roles
**Lead with:** ORGAN-IV orchestration, registry design, governance trade-offs, agentic-titan (1,095 tests). **Demonstrates:** Production-ready systems thinking, architectural reasoning, autonomous system design, test-driven development at scale.

### Grant Funding
**Lead with:** ORGAN-V essays + registry as evidence of long-term organizational capacity. **Demonstrates:** Digital sustainability, infrastructure that enables ongoing work (not project-based), transparent governance, community contribution model.

### Residencies & Fellowships
**Lead with:** Governance as creative practice, all 8 organs as unified artistic infrastructure. **Demonstrates:** Systemic artistic practice, artist-engineer hybrid identity, documentation as artistic output, equitable systems design.

---

## Evidence Links

| Asset | URL |
|-------|-----|
| Central Registry | `github.com/meta-organvm/organvm-corpvs-testamentvm/registry-v2.json` |
| Orchestration Hub | `github.com/organvm-iv-taxis/orchestration-start-here` |
| Public Process | `github.com/organvm-v-logos/public-process` |
| Governance Spec | `github.com/meta-organvm/organvm-corpvs-testamentvm/docs/implementation/orchestration-system-v2.md` |
| CI/CD Spec | `github.com/meta-organvm/organvm-corpvs-testamentvm/docs/implementation/github-actions-spec.md` |

---

## Artist-Engineer Identity

The eight-organ system is proof that "artist" and "engineer" are not separate roles. AI roles see the systems thinking. Grants see the organizational capacity. Residencies see the systemic artistic practice. Same evidence, different framings. The system *is* the portfolio.
