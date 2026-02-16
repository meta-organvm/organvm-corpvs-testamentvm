# ORGAN-III Beta Product Brief — life-my--midst--in

**Created:** 2026-02-16
**Sprint:** 25-INSPECTIO
**Author:** @4444j99 (AI-conductor model: human directs, AI generates, human reviews)
**Purpose:** 1-page product brief for the recommended first beta product
**Companion:** [`organ-iii-beta-assessment.md`](./organ-iii-beta-assessment.md) (full assessment of top 5 candidates)
**Referenced by:** [`operational-cadence.md`](../operations/operational-cadence.md) Part IV, Days 4-5

---

## Target User Persona

**Primary: The Portfolio Professional** — Mid-career creative technologists, developers, designers, and researchers who apply to competitive positions (tech companies, fellowships, residencies, grants). They are tired of maintaining multiple resume versions and want their professional identity to speak for itself. They value authenticity over optimization and want employers to see the real person, not a keyword-stuffed PDF.

**Secondary: The Hiring Manager** — Technical leads and hiring managers at companies that value cultural fit alongside skills. They visit a candidate's link and experience the "Inverted Interview" — answering questions about their role and team culture before seeing a curated presentation of the candidate tailored to their context.

---

## Core Value Proposition

**Your professional identity, curated by context — not by you.** Instead of maintaining 10 resume versions, you maintain one identity ledger. When an employer visits your link, they describe what they're looking for, and the system assembles the right presentation of you using 16 identity masks and compatibility scoring.

---

## MVP Feature Set (Beta Launch)

1. **Identity Ledger** — Create and manage a comprehensive professional identity with skills, experiences, values, and career narrative across 8 temporal epochs
2. **Inverted Interview Flow** — Employer-facing questionnaire that captures role requirements and culture preferences before revealing the candidate profile
3. **Mask-Based Presentation** — Automated selection from 16 identity masks (cognitive, expressive, operational) based on the employer's responses, producing a contextually relevant profile view
4. **Compatibility Score** — 5-factor analysis (Skill Match 30%, Values Alignment 25%, Growth Fit 20%, Sustainability 15%, Compensation 10%) displayed to both candidate and employer
5. **Multi-Format Export** — PDF resume, JSON-LD (semantic web), and shareable link for each mask configuration

---

## Tech Stack and Deployment Plan

| Component | Technology | Deployment |
|-----------|-----------|------------|
| Frontend | Next.js 16, React 19, TypeScript 5.3, Tailwind CSS | Vercel (free tier, then Pro at scale) |
| API | Fastify 5, Node.js 22+ | Railway or Render (starter plan ~$7/month) |
| Database | PostgreSQL with pgvector | Railway managed Postgres (~$5/month) or Neon (free tier) |
| Cache/Queue | Redis | Railway Redis (~$5/month) or Upstash (free tier) |
| Orchestrator | Node.js worker service | Railway (same deployment, separate process) |
| Domain | Custom domain (TBD) | ~$12/year via Cloudflare or Namecheap |
| SSL | Auto via deployment platform | Included |
| Monitoring | Prometheus + Grafana (already configured) | Self-hosted on same infra or Grafana Cloud free |

**Total hosting cost for beta:** ~$17–25/month (can start at ~$5/month with free tiers)

**Deployment approach:** Docker Compose for local development → Railway for staging + production (simplest path given existing configs). Vercel for frontend if SSR performance matters. The repo already has Railway, Render, Vercel, and K8s configs — choose one, not all.

---

## Revenue Model and Pricing Hypothesis

**Model:** Freemium with premium tiers

| Tier | Price | Features |
|------|-------|----------|
| **Free** | $0/month | 1 identity ledger, 3 masks, basic compatibility score, PDF export, shareable link |
| **Professional** | $12/month | All 16 masks, full compatibility scoring, JSON-LD export, Hunter Protocol (autonomous job search), custom domain for profile |
| **Team/Institution** | $29/user/month | Everything in Professional + employer dashboard, consultation credits, W3C Verifiable Credentials, API access |

**Pricing rationale:** LinkedIn Premium is $30/month and offers far less identity curation. Resume builder tools (Resumake, Zety, Novoresume) charge $8–25/month for template-based PDF generation. The mask-based contextual presentation is a genuine differentiator worth a premium over static resume builders.

**Revenue target:** 50 paying users at $12/month = $600 MRR. This exceeds typical indie SaaS operating costs (~$50–100/month) and meets omega criterion #10 (MRR ≥ operating costs).

---

## Gap Analysis: Built vs. Needed for Beta

| Feature | Status | Gap |
|---------|--------|-----|
| Identity ledger CRUD | Built | None — working |
| Mask system (16 masks, 3 categories) | Built | None — working |
| Inverted Interview flow | Built | None — working |
| Compatibility scoring | Built | None — working |
| Role family mapping (10 families) | Built | None — working |
| Temporal epoch tracking | Built | None — working |
| PDF export | Built | None — working |
| JSON-LD export | Built | None — working |
| W3C Verifiable Credentials | Built | None — working |
| Hunter Protocol (job search) | Built | None — working |
| DID verification | Built | None — working |
| Database migrations (21) | Built | Need to run against production DB |
| Seed data | Exists | Need production seed profiles (demo data) |
| User authentication | **Gap** | Need auth provider (Auth0, Clerk, or Supabase Auth) |
| Payment processing | **Gap** | Need Stripe integration for premium features |
| Landing page / marketing site | **Gap** | Need public-facing page explaining the product |
| User onboarding flow | **Gap** | Need guided setup for new users creating their identity |
| Analytics / usage tracking | **Gap** | Need basic analytics (PostHog free tier or Plausible) |

**Summary:** Core product is complete. Gaps are standard SaaS plumbing (auth, payments, marketing, onboarding) — not product features. This is ~2 weeks of work for an experienced developer using the AI-conductor model.

---

## Timeline to Beta (in weeks)

| Week | Focus | Deliverables |
|------|-------|-------------|
| **Week 1** | Infrastructure + Auth | Production database provisioned, auth provider integrated (Clerk or Supabase Auth), staging deployment on Railway, demo seed data loaded |
| **Week 2** | Payments + Polish | Stripe integration (free/pro tier gate), landing page, user onboarding flow, basic analytics, production deployment |
| **Week 3** | Beta launch + feedback | Announce to first 10 users, collect feedback, fix critical bugs, iterate on onboarding |

**Total: 3 weeks to public beta** (conservative). Could compress to 2 weeks with aggressive scoping.

---

## First 10 Users (Where to Find Them)

1. **Personal network** (3–5 users) — Fellow creative technologists, developers, and designers who are actively job-seeking or portfolio-building. Direct outreach via existing contacts.

2. **Public-process readers** (2–3 users) — The 33 essays on public-process describe the system in detail. Readers who've engaged with the building-in-public content are natural early adopters. Announce via ORGAN-VII distribution (Mastodon thread, LinkedIn post).

3. **Mastodon/Fediverse tech community** (2–3 users) — Post the beta announcement on Mastodon with the "Inverted Interview" hook. The fediverse tech community values novel approaches to professional identity and is disproportionately composed of creative technologists (the target persona).

4. **Application reviewers** (1–2 users) — If any of the submitted applications result in conversations, mention the product as evidence of shipping capability. Hiring managers who review your application are literally the target user on the employer side.

**User recruitment strategy:** Do not attempt to scale beyond 10 users in the first month. The goal is qualitative feedback on the core interaction (does the Inverted Interview actually help employers understand candidates better?), not growth metrics. Growth comes after product-market fit is validated.

---

*This brief answers the 8 questions specified in the operational cadence Part IV, Days 4-5. Development begins on the next Tuesday product day per the weekly rotation.*
