# ORGAN-III Beta Product Assessment

**Created:** 2026-02-16
**Sprint:** 25-INSPECTIO
**Author:** @4444j99 (AI-conductor model: human directs, AI generates, human reviews)
**Purpose:** Structured assessment of the 5 highest-code-substance ORGAN-III repos to select a beta product candidate
**Companion:** [`organ-iii-beta-brief.md`](./organ-iii-beta-brief.md) (product brief for recommended candidate)

---

> **Context:** Revenue is $0. H3 (generate revenue) is the most underdeveloped omega horizon. 24 sprints of documentation/infrastructure are complete. This assessment is the first step toward actually shipping a product. It evaluates the top 5 ORGAN-III repos by code substance and recommends one for beta development.

---

## Summary Comparison Table

| Dimension | life-my--midst--in | universal-mail--automation | public-record-data-scrapper | classroom-rpg-aetheria | fetch-familiar-friends |
|-----------|-------------------|---------------------------|----------------------------|----------------------|----------------------|
| **Files** | ~1,694 (monorepo) | ~1,272 (incl. venv) | ~497 | ~211 | ~188 (130 src) |
| **Stack** | Next.js 16 + Fastify 5 + PostgreSQL | Python 3 + Gmail/IMAP/Outlook APIs | React 19 + Vite 7 + Express 5 + PostgreSQL | React 19 + Vite 7 + Firebase + GitHub Spark | React 18 + Vite 7 + Supabase + Stripe |
| **Tests** | 75%+ coverage (Vitest + Playwright) | None (manual validation) | Vitest + Playwright E2E (5 browsers) | Vitest configured | Vitest configured |
| **Deploy** | Docker, Helm, K8s, Railway, Render, Vercel | None (CLI tool) | Dockerfile, docker-compose, K8s, Vercel | None | GitHub Pages |
| **CI/CD** | 6 workflows | None | 12 workflows | Unknown | 17 workflows |
| **UI** | Full web dashboard | CLI only | Full web dashboard + investor pitch | Full web app (sandbox demo) | Full web app |
| **Revenue model** | Freemium (B2C + B2B) | Subscription | Subscription (B2B) | Subscription (B2B) | Freemium (two-tier Stripe) |
| **Time to beta** | **1–2 weeks** | 2–3 months | 3–4 weeks | 6–8 weeks | 4–6 weeks |
| **Recommendation** | **BUILD** | DEFER | INVESTIGATE | DEFER | DEFER |

---

## 1. life-my--midst--in (1,694 files)

### What it does
Interactive CV/resume system implementing the "Inverted Interview" paradigm: employers visit a candidate's profile link, answer questions about role and culture, and the system assembles a role-curated identity presentation from a comprehensive identity ledger using 16 identity masks across 3 ontological categories.

### Tech stack
- **Frontend:** Next.js 16, React 19, TypeScript 5.3, Tailwind CSS (port 3000)
- **Backend API:** Fastify 5, Node.js 22+, TypeScript 5.3 (port 3001)
- **Orchestrator/Workers:** Node.js, Redis queue, 10 agent roles (port 3002)
- **Database:** PostgreSQL with pgvector, 21 migrations
- **Build:** Turborepo, pnpm workspaces — 3 apps (web, api, orchestrator), 4 packages (schema, core, content-model, design-system)

### Code substance
~90K+ files across the monorepo (includes node_modules). Architecture follows hexagonal pattern (ports & adapters) with schema-first design (Zod schemas as canonical source of truth). Code quality standards enforced: max 1,200 LOC/file, max 200 LOC/function, max cyclomatic complexity 10.

Key directories: `apps/web/`, `apps/api/` (21 SQL migrations, seeds, OpenAPI spec), `apps/orchestrator/` (task queue, webhooks, agent execution), `packages/schema/` (identity, profile, mask, epoch, narrative), `packages/core/` (mask matching, DID/VC crypto), `packages/content-model/` (narrative generation, role families, compatibility analyzer), `packages/design-system/`.

### Feature completeness
**Feature-complete.** 68+ commits, zero open issues.
- Inverted Interview flow with role/culture questionnaire
- 16-mask identity system with 3 ontological categories
- 10 role families with optimized professional mappings
- 8 temporal epochs for career progression tracking
- Compatibility scoring engine (5-factor: Skill 30%, Values 25%, Growth 20%, Sustainability 15%, Compensation 10%)
- Multi-format export (JSON-LD, PDF, W3C Verifiable Credentials)
- Hunter Protocol autonomous job search
- DID/VC verification with cryptographic signing

### Deployment readiness
**Production-grade.** Docker Compose (dev + prod), Kubernetes manifests (Helm charts, ingress, RBAC, PDB), Railway.yaml, Vercel.json, Render.yaml. Prometheus monitoring with alert rules, Grafana dashboards, k6 load testing scripts. Environment templates for dev/prod/integration.

### Test coverage
**75%+ statement/branch/function/line coverage** (Vitest thresholds). Unit tests (Vitest), integration tests with dedicated database URLs, E2E tests (Playwright). Pre-commit hooks via Husky enforce lint + test pass.

### User-facing state
Full web dashboard with CompatibilityDashboard and MaskEditor components. OpenAPI spec for API documentation. JSON-LD and PDF export. Responsive UI with Tailwind CSS.

### Revenue model fit
**Clear freemium path:** Free profile creation + basic masks; premium for Hunter Protocol, VC export, advanced mask customization. B2B angle: employer consultation credits for compatibility reports. Institutional licensing for universities/corporate recruiting.

### Environment/secrets needed
PostgreSQL, Redis. Well-documented `.env.example` files for dev, prod, and integration environments. No embedded secrets.

### CI/CD
6 workflows: ci-cd (main pipeline), test (isolated runner), deploy (multi-platform), performance (k6), release (semantic versioning + changelog), security (dependency scan + SAST).

### Time to beta estimate
**1–2 weeks.** Code complete and feature-locked. Remaining: seed production data (2–3 days), configure production secrets (1 day), domain/SSL (1 day), staging test cycle (3–5 days), go-live checklist (2–3 days).

### Recommendation: **BUILD**
This is the clear winner. Feature-complete, production-grade, comprehensive deployment infra, tested, documented. The only ORGAN-III repo that could be live within 2 weeks. The "Inverted Interview" paradigm is novel enough to differentiate in the market, and the mask system provides a clear value proposition for premium features.

---

## 2. universal-mail--automation (1,272 files)

### What it does
Multi-provider email automation system for inbox triage using shared categorization rules and Eisenhower priority tiers across Gmail API, Microsoft Graph (Outlook), generic IMAP, and macOS Mail.app (AppleScript).

### Tech stack
- **Language:** Python 3 (no pyproject.toml — bare pip install)
- **APIs:** Gmail API (OAuth), Microsoft Graph (Azure AD), IMAP, AppleScript
- **Auth:** 1Password CLI integration for credential management
- **Architecture:** Abstract base class pattern — `core/rules.py` → `providers/*.py` → `core/state.py`

### Code substance
~1,272 files total (heavily inflated by `.venv/` dependencies). Actual source code is in `core/` (rules.py, state.py, models.py, config.py), `providers/` (base.py, gmail.py, imap.py, mailapp.py, outlook.py), `auth/` (onepassword.py), plus root-level CLI scripts (cli.py, auto_drain.py, bulk_sweeper.py). Shallow 3-level directory structure.

### Feature completeness
Feature-complete as a CLI tool: multi-provider triage, 28 categories, Eisenhower priority routing, VIP detection, time-based escalation, dry-run mode, crash recovery via StateManager, reporting commands (summary, pending, vip, escalate, health).

### Deployment readiness
**None.** No Dockerfile, docker-compose, cloud deployment configs. Designed as a local CLI tool with launchd scheduling. Not a web service.

### Test coverage
**None.** No test suite. AGENTS.md explicitly states: "No unit test suite; validation via small queries and log review."

### User-facing state
CLI only. No web UI. Users interact via command-line arguments (`python3 cli.py label --provider gmail --tier-routing`).

### Revenue model fit
**Weak for SaaS.** The tool solves a real problem (multi-account email triage) but the path from CLI tool to paid SaaS is long: would need a web interface, multi-tenant architecture, user auth, and hosted infrastructure. The 1Password dependency complicates deployment for others.

### Environment/secrets needed
1Password integration required (GMAIL_OAUTH_OP_REF, GMAIL_TOKEN_OP_REF, OUTLOOK_CLIENT_ID). No `.env.example` — uses 1Password environment files.

### CI/CD
**None.** No `.github/workflows/` directory.

### Time to beta estimate
**2–3 months.** Would need: web UI (4–6 weeks), multi-tenant backend (2–3 weeks), user auth (1 week), deployment infrastructure (1 week), test suite (1 week), CI/CD (days). Essentially a rewrite as a web service.

### Recommendation: **DEFER**
Solid engineering for a personal tool, but fundamentally a CLI utility, not a product. Converting to SaaS would require rebuilding most of the user-facing layer. The effort-to-revenue ratio is unfavorable compared to repos that already have web UIs.

---

## 3. public-record-data-scrapper (497 files)

### What it does
UCC/MCA lead generation intelligence platform that scrapes public filing records across US states, enriches business data with ML and external APIs, and presents actionable intelligence through a web dashboard for sales teams.

### Tech stack
- **Frontend:** React 19, TypeScript ~5.9, Vite 7, Tailwind CSS 4, Radix UI, Recharts, D3
- **Backend:** Express 5, PostgreSQL, Redis (BullMQ for job queues), Puppeteer (web scraping)
- **Auth:** Auth0 (planned Phase 4), JWT
- **Monitoring:** Sentry, Prometheus
- **Build:** npm workspaces (monorepo with apps/* and packages/*)

### Code substance
~497 files. Comprehensive frontend with data visualization dashboards (D3, Recharts), form handling (React Hook Form + Zod), and component library (Radix UI). Backend includes state-specific UCC scrapers (Texas, Florida, California documented), data enrichment pipeline, and job queue. Has an investor pitch video (5-min, 1080p) and dedicated access page.

### Feature completeness
**Partial.** The UI is functional with mock data (`VITE_USE_MOCK_DATA=true` default). Core features: prospect dashboard, data visualization, filtering. Missing: real data pipeline connected (scraper → database → frontend), ML enrichment active, multi-state scraper coverage beyond 3 states. Phased implementation plan documented (Phase 1–5).

### Deployment readiness
**Good.** Dockerfile, docker-compose.yml, Kubernetes manifests, Vercel deployment (already configured at `public-record-data-scrapper.vercel.app`). 12 GitHub workflows. DEPLOYMENT_READY.md describes auto-deployment via Vercel.

### Test coverage
**Good framework, uncertain coverage.** Vitest configured with coverage. Playwright E2E configured for 5 browsers (Chromium, Firefox, WebKit, Mobile Chrome, Mobile Safari) with screenshot-on-failure and trace recording. Actual test file count and coverage metrics not confirmed.

### User-facing state
Full web dashboard operational with mock data. Investor pitch video and access page exist. Currently deployed on Vercel (mock mode). A user could interact with the demo today.

### Revenue model fit
**Strong B2B subscription.** Target: MCA lenders, commercial brokers, sales teams needing UCC filing intelligence. Clear value proposition: automated lead generation from public records. The market exists (UCC filing data is used extensively in commercial lending).

### Environment/secrets needed
Extensive (245-line `.env.example`): PostgreSQL, Redis, UCC API keys, state portal credentials (Texas SOS), ML API keys, Stripe/payment (not yet configured), Auth0, AWS (secrets management), Sentry, various external data enrichment APIs (SEC EDGAR, OSHA, USPTO, Census, SAM.gov, D&B, Clearbit, ZoomInfo).

### CI/CD
**Comprehensive.** 12 GitHub workflows. Branch-protected (requires PRs). Build verified (9.2s build time per DEPLOYMENT_READY.md).

### Time to beta estimate
**3–4 weeks.** Mock data mode works now. Remaining: connect at least 1 real state scraper (Texas — credentials documented), wire database, basic auth (can start with simple JWT before Auth0), deploy to production Vercel. The gap is data pipeline, not UI.

### Recommendation: **INVESTIGATE**
Strong product-market fit (B2B lead gen is a real market with paying customers). The Vercel deployment exists. But: the mock data dependency means there's no real product yet — it's a sophisticated demo. The scraper legal/compliance landscape for state UCC portals needs investigation before committing development time. If the legal path is clear, this is the #2 candidate after life-my--midst--in.

---

## 4. classroom-rpg-aetheria (211 files)

### What it does
Educational gamification platform that transforms classroom assignments into RPG quests, using AI-powered feedback and a thematic identity system to increase student engagement (targeting the 40% dropout rate problem).

### Tech stack
- **Frontend:** React 19, TypeScript strict, Vite 7.3, Tailwind CSS 4, Radix UI (21 primitives), Framer Motion, Three.js (3D via @react-three/fiber + drei)
- **Backend:** Firebase 12.8, GitHub Spark (LLM integration via `window.spark.llm()`)
- **Data:** Recharts, D3 for visualization
- **Forms:** React Hook Form + Zod validation
- **Monitoring:** Sentry, web-vitals

### Code substance
~211 files. Comprehensive React component library with 43 production dependencies. Core data model: Realm (course container), Quest (assignment state machine: locked → available → in_progress → completed/failed), UserProfile (XP, level, artifacts), Submission (AI-generated feedback), KnowledgeCrystal (AI study guides), Artifact (collectible rewards). Theme system with 4 variants (Fantasy/Cyberpunk/Medieval/Modern). Sandbox demo mode via `?sandbox=true` URL parameter.

### Feature completeness
**Moderate.** Quest system, character creation, progress tracking, achievement system functional. AI integration for feedback generation implemented. 4-theme system complete. Sandbox mode with pre-populated demo data works. Missing: actual classroom deployment and teacher onboarding flow.

### Deployment readiness
**Weak.** No Dockerfile, docker-compose, K8s, Railway, Vercel, Render, or Netlify configs found. Depends on GitHub Spark for LLM features, which limits deployment targets. Firebase provides backend but no self-hosted option documented.

### Test coverage
Vitest configured with Testing Library (React, DOM, jest-dom, user-event). jsdom environment. Coverage not verified. 25-minute portfolio presentation video exists (Python-generated, 45 scenes).

### User-facing state
Full web app with sandbox demo mode. Interactive UI with 3D elements, animations, and gamification. User can explore via `?sandbox=true`. Polished visual experience.

### Revenue model fit
**Challenging B2B (EdTech).** Target: schools/districts. EdTech sales cycles are long (6–12 months), require pilot programs, and face procurement bureaucracy. The product needs a teacher champion, district buy-in, and often compliance with student privacy regulations (FERPA, COPPA). GitHub Spark dependency adds vendor lock-in concerns for institutional buyers.

### Environment/secrets needed
Firebase credentials, GitHub Spark access, AI provider keys. Not fully documented (no `.env.example` found in investigation).

### CI/CD
Not confirmed (`.github/workflows/` existence uncertain from agent investigation).

### Time to beta estimate
**6–8 weeks.** Needs: deployment infrastructure (2 weeks), teacher onboarding flow (1–2 weeks), remove GitHub Spark dependency or document it (1 week), actual classroom pilot coordination (2–3 weeks). The EdTech market also requires longer validation cycles.

### Recommendation: **DEFER**
Impressive demo with sophisticated UX, but the EdTech market is notoriously hard for indie developers. Long sales cycles, compliance requirements, and the GitHub Spark dependency make this a poor first-revenue candidate. Better suited as a second product after establishing revenue from a simpler B2C or B2B product.

---

## 5. fetch-familiar-friends (188 files)

### What it does
Personalized dog calendar app ("Attend Our Familiar Friends" / "DogTale Daily") with AI-powered content generation, social community features, health tracking, virtual pet companion, AR camera, telemedicine consultations, and premium subscription tiers.

### Tech stack
- **Frontend:** React 18.2, Vite 7.3.1, Tailwind CSS 3.3.3, Framer Motion, Lucide React
- **Backend:** Supabase (database, auth, real-time)
- **Payments:** Stripe (two-tier: PREMIUM_PRICE_ID, LUXURY_PRICE_ID)
- **AI:** Claude API (primary), OpenAI (secondary), HuggingFace (fallback)
- **Testing:** Vitest with happy-dom, Testing Library

### Code substance
~188 files total, 130 source files in `src/`. Version 0.2.0 (active development). Feature flags for gradual rollout: social, AI chat, health tracking, virtual pet (all enabled). Extensive planning documentation (BLINDSPOTS_ANALYSIS.md, COMPREHENSIVE_ROADMAP.md, CRITICAL_ANALYSIS.md, ChatPRD/).

### Feature completeness
**Ambitious scope, early implementation.** README describes: personalized daily content, care tracking, social hub with activity feed, quests (XP gamification), friends list, nearby users map, professional coaching, 24/7 telemedicine, AR camera filters, virtual pet companion, memorial services, premium tiers. At v0.2.0, likely many features are planned but not yet built. The feature list reads more like a roadmap than a shipped product.

### Deployment readiness
**Minimal.** GitHub Pages deployment workflow exists (deploy-pages.yml). No Docker, K8s, or cloud platform configs. Supabase provides managed backend, which simplifies deployment for the database layer.

### Test coverage
Vitest configured with v8 coverage provider, happy-dom environment, setup file at `src/test/setup.js`. Testing Library present. Actual test coverage and test file count not verified.

### User-facing state
Full web app with React components. Feature flags suggest modular UI. Daily calendar view, social features, AI chat interface likely present. Quality of implementation unclear at v0.2.0.

### Revenue model fit
**B2C freemium with Stripe.** Two-tier subscription (Premium + Luxury) already architected with Stripe price IDs in env config. Pet owner market is large but highly competitive (many dog apps exist). Differentiation unclear — "AI-powered personalized calendar" is novel but the feature sprawl (telemedicine, AR camera, coaching) suggests unfocused value proposition.

### Environment/secrets needed
Well-documented `.env.example` (56 lines): Supabase URL + anon key, AI provider keys (3 providers), Stripe keys (2 tiers), Pet image API URLs, feature flags.

### CI/CD
**Comprehensive.** 17 GitHub Actions workflows: ci, code-quality, codeql, accessibility, docs-validation, security-scan, performance, pr-automation, project-automation, stale, release, release-drafter, deploy-pages, label, node.js. (Note: performance.yml disabled per ILLUSTRATIO Sprint billing fix.)

### Time to beta estimate
**4–6 weeks.** Has Stripe already architected. Needs: feature pruning to MVP (1 week of decision-making), implement core calendar + AI features (2–3 weeks), Supabase auth + database setup (1 week), deploy beyond GitHub Pages (1 week). The feature sprawl is the main risk — trying to ship everything at v0.2.0 would take months.

### Recommendation: **DEFER**
Has Stripe integration architected (unique advantage) and comprehensive CI/CD, but v0.2.0 status and extreme feature sprawl (calendar + social + gamification + telemedicine + AR + virtual pets + coaching + memorial services) suggest the product vision isn't focused enough for a fast beta. The B2C pet market is also crowded. Better to focus on a product with clearer differentiation and more complete implementation.

---

## Final Ranking

| Rank | Repo | Recommendation | Rationale |
|------|------|---------------|-----------|
| **1** | **life-my--midst--in** | **BUILD** | Feature-complete, production-grade infra, 1–2 weeks to live. Novel "Inverted Interview" paradigm with clear monetization path. |
| 2 | public-record-data-scrapper | INVESTIGATE | Strong B2B market fit, Vercel deployed (demo), but needs real data pipeline + legal review of scraping. 3–4 weeks. |
| 3 | fetch-familiar-friends | DEFER | Stripe already designed, good CI/CD, but v0.2.0 + extreme feature sprawl + crowded B2C market. 4–6 weeks after pruning. |
| 4 | classroom-rpg-aetheria | DEFER | Impressive demo but EdTech market is hard for indie devs. Long sales cycles, compliance burden, GitHub Spark lock-in. |
| 5 | universal-mail--automation | DEFER | Solid CLI tool but not a product. No UI, no tests, no deployment. Would be a ground-up SaaS rebuild. |

---

## Recommended Path

**Primary:** Build `life-my--midst--in` as the first ORGAN-III beta product. It is the only repo that could generate revenue within 30 days. Begin Tuesday product work immediately.

**Secondary (month 2):** Investigate `public-record-data-scrapper` for B2B revenue. The UCC lead gen market has real paying customers. If legal review clears the scraping approach, this becomes the second product candidate.

**Deferred:** The remaining 3 repos are better served by continued creative development (Tuesday/Thursday product time) rather than beta launch pressure. They can mature into beta candidates once the first product is generating revenue.

---

*This assessment was generated at Sprint 25: INSPECTIO. See [`organ-iii-beta-brief.md`](./organ-iii-beta-brief.md) for the detailed product brief for the recommended candidate.*
