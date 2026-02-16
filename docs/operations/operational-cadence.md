# Operational Cadence — Post-Construction Rhythm

**Created:** 2026-02-16
**Author:** @4444j99 (AI-conductor model: human directs, AI generates, human reviews)
**Status:** ACTIVE — Living document, updated as cadence evolves
**Companions:** [`minimum-viable-operations.md`](./minimum-viable-operations.md) (maintenance), [`key-workflows.md`](./key-workflows.md) (procedures)
**Governs:** Daily/weekly/monthly creative work rhythm (not maintenance — see MVO for that)
**Constitution:** [`docs/memory/constitution.md`](../memory/constitution.md) — Articles I-VI govern all specifications

---

> *The MVO tells a second operator how to keep the system alive. This document tells the primary operator how to use the system for what it was built for: making things, shipping things, and showing things to other people.*

---

## How to Read This Document

This is a **playbook, not a philosophy paper.** It has six parts:

- **Part I** — Weekly template (what to do each day)
- **Part II** — Monthly cycles (what to do each week of the month)
- **Part III** — Content cadence (what to publish and when)
- **Part IV** — Immediate priorities (exact steps for this week and this month)
- **Part V** — What you're not considering (honest guardrails)
- **Part VI** — Anti-patterns (what NOT to do)
- **Appendix** — Quick reference card

Parts I–III are **durable templates** — they survive beyond the first month and define steady-state rhythm. Part IV is **concrete NOW** — specific actions with URLs, commands, and deadlines that expire. Part V is **therapy** — the uncomfortable truths that prevent construction addiction from consuming the creative work the system was built to protect.

---

## PART I: THE WEEK — Default Weekly Template

The weekly template rotates organ focus by day. This prevents context-switching within a single day and ensures all 8 organs receive regular attention. The rotation is weighted toward the highest-impact horizons: H2 (validate externally) and H3 (generate revenue).

### Monday — ORGAN-I / ORGAN-II (Theory + Creative Work)

**Cognitive mode:** Deep focus. Generative. No external communication.

| Block | Time | Activity |
|-------|------|----------|
| Morning | 90 min | Deep work: theory writing (ORGAN-I) or creative project (ORGAN-II) |
| Midday | 30 min | Shallow ops: check email, review Dependabot PRs, triage GitHub notifications |
| Afternoon | 60–90 min | Continue deep work, or read/research for the week's theory topic |
| Evening | 5 min | Soak test snapshot: `python3 scripts/soak-test-monitor.py collect` + brief reflection |

**Monday deliverables:** Progress on one theory artifact (framework draft, algorithm spec, ontology revision) or one creative artifact (generative sketch, performance concept, composition).

**Why Monday:** Theory and creative work require the freshest cognitive energy. Starting the week with generative work prevents the Monday trap of "catch up on operational tasks" — a trap that turns into an entire week of maintenance.

### Tuesday — ORGAN-III (Product Development)

**Cognitive mode:** Engineering. Ship things. Measure things.

| Block | Time | Activity |
|-------|------|----------|
| Morning | 90 min | Deep work: feature development on the active ORGAN-III product |
| Midday | 30 min | Shallow ops: check CI, review product analytics if live, respond to user issues |
| Afternoon | 60–90 min | Continue feature work, or write product-related documentation |
| Evening | 5 min | Soak test snapshot + git commit any product progress |

**Tuesday deliverables:** One feature increment, one bug fix, or one deployment step on the active ORGAN-III product. Shipping trumps perfecting.

**Why Tuesday:** Product work needs sustained focus but a different kind than Monday's generative mode. Tuesday is pragmatic — write code, deploy it, test it with real users. The transition from Monday's theory/art to Tuesday's product work exercises the organ separation: ORGAN-I insights might inspire ORGAN-III features, but the dependency is I→III (unidirectional), never III→I.

### Wednesday — ORGAN-V / ORGAN-VII (Content + Distribution)

**Cognitive mode:** External-facing. Communication. Writing for an audience.

| Block | Time | Activity |
|-------|------|----------|
| Morning | 90 min | Deep work: essay writing or editing (ORGAN-V) |
| Midday | 30 min | Social media posting (ORGAN-VII): Mastodon thread, LinkedIn share, Discord announcement |
| Afternoon | 60 min | Distribution follow-up: respond to comments, share others' work, engage |
| Evening | 5 min | Soak test snapshot |

**Wednesday deliverables:** Essay progress (minimum 500 words toward next essay), social media posts across 2+ platforms.

**Why Wednesday:** The automated distribution-agent runs Wednesdays at 10:00 UTC. Aligning manual content work with the automated distribution cycle means both human and machine are pushing content outward on the same day. This creates a "publication day" rhythm.

### Thursday — ORGAN-III Continued + Applications/Outreach

**Cognitive mode:** Mixed. Product work morning, external communication afternoon.

| Block | Time | Activity |
|-------|------|----------|
| Morning | 90 min | ORGAN-III product work (continuation from Tuesday) |
| Midday | 30 min | Shallow ops: email, notifications, scheduling |
| Afternoon | 60–90 min | Application work: drafting, submitting, or following up on applications and outreach |
| Evening | 5 min | Soak test snapshot |

**Thursday deliverables:** Product progress plus one application-related action (submit, draft, follow up, or research a new target).

**Why Thursday:** Applications require a different cognitive register than product development — less "build the thing" and more "explain why the thing matters." Splitting the day between these modes ensures neither stagnates. Thursday afternoon is also good for email outreach and networking because people process email before the weekend.

### Friday — System Health + Omega Review + Planning

**Cognitive mode:** Reflective. Strategic. Maintenance.

| Block | Time | Activity |
|-------|------|----------|
| Morning | 60 min | Weekly system review: check all workflow runs, merge Dependabot PRs, review soak test data |
| Midday | 30 min | Omega checklist review: which of the 17 criteria advanced this week? |
| Afternoon | 60 min | Plan next week: choose Monday's theory/art topic, Tuesday's product task, Wednesday's essay target |
| Evening | 15 min | Weekly reflection: what worked, what didn't, what's blocked. Commit soak test data. |

**Friday deliverables:** All workflow runs verified green. Next week planned. Weekly soak test data committed. One sentence per omega criterion on whether it advanced.

**Why Friday:** Friday is natural review-and-plan territory. It prevents the "what should I work on Monday?" uncertainty that leads to doomscrolling or infrastructure tinkering. The omega checklist review keeps long-term goals visible without dominating the creative week.

### Daily Anchors (Every Day)

These three micro-habits anchor every day regardless of organ focus:

1. **Morning (first 5 min):** Check overnight workflow runs. If anything is red, triage before starting deep work. Most days: everything is green, move on.
   ```bash
   gh run list --repo organvm-iv-taxis/orchestration-start-here --limit 5 --json status,name --jq '.[] | "\(.name): \(.status)"'
   ```

2. **Midday (30 min):** Shallow task batch — email, GitHub notifications, social media responses, Dependabot PRs. Do not let these bleed into deep work blocks. If a notification requires deep work, schedule it for the appropriate day.

3. **Evening (5 min):** Soak test snapshot + one-sentence reflection. The snapshot is automated if cron is configured; the reflection is for you.
   ```bash
   python3 scripts/soak-test-monitor.py collect
   ```

### Weekend

**Do not work on the system.** The system is designed to be autonomous. If it can't survive a weekend without you, that's a bug to fix, not a schedule to fill. Use weekends for:
- Reading that informs ORGAN-I theory (books, papers, not GitHub repos)
- Creative input (attending performances, visiting exhibitions, listening to music)
- Rest

If something breaks over the weekend, the emergency procedures (`emergency-procedures.md`) will be there Monday morning. Nothing in this system is urgent enough to sacrifice rest.

---

## PART II: THE MONTH — 30-Day Cycles

Each month follows a four-week rhythm. The weeks are themed, not rigid — if a product feature needs an extra day, borrow from the content sprint, not the other way around. Product and applications are higher-priority than content during the validation phase (H1-H2).

### Week 1: Product Sprint

**Focus:** ORGAN-III feature development. Ship something.

- Monday-Tuesday: Full product development (2 deep work days)
- Wednesday: Product update essay (ORGAN-V: "what I shipped this month")
- Thursday: Continue product work + one application action
- Friday: System review + week 2 planning

**Week 1 target:** One deployable feature increment or one beta milestone reached.

### Week 2: Content Sprint

**Focus:** ORGAN-V essays and ORGAN-VII distribution. Publish something.

- Monday: Theory deep-dive writing (ORGAN-I → V pipeline)
- Tuesday: Essay editing and finalization
- Wednesday: Publish + distribute. Deploy essay to public-process, post social threads
- Thursday: Application follow-up + catch-up on any product tasks
- Friday: System review + week 3 planning

**Week 2 target:** One essay published. Social media posts distributed across platforms.

### Week 3: Outreach Sprint

**Focus:** External engagement. Applications, stranger test recruitment, salon planning.

- Monday: Creative/theory work (maintain the generative rhythm)
- Tuesday: Application drafting or submission (ORGAN-III products are portfolio evidence here)
- Wednesday: Distribution + community engagement (ORGAN-VI planning, ORGAN-VII posting)
- Thursday: Stranger test recruitment, salon scheduling, conference proposal drafting
- Friday: System review + week 4 planning

**Week 3 target:** One application submitted or advanced. One external engagement initiated (stranger test recruit, salon invite, conference proposal).

### Week 4: Review + Maintenance

**Focus:** System health, omega checklist, portfolio update.

- Monday: Creative work (keep the Monday generative habit even during review week)
- Tuesday: Portfolio site update — refresh project data, add recent work
- Wednesday: Monthly omega checklist review — all 17 criteria, current status
- Thursday: System audit — run `organ-audit.py`, review soak test trends, check billing
- Friday: Month retrospective + next month planning

**Week 4 target:** Monthly omega checklist reviewed with evidence links updated. Portfolio site refreshed. Soak test data committed. Audit passing.

### Monthly Deliverables (Minimum Viable)

Every 30-day cycle should produce, at minimum:

| Deliverable | Quantity | Horizon |
|-------------|----------|---------|
| Essays published | 2 (one every 2 weeks) | H2/H5 |
| Applications submitted or advanced | 1 | H2 |
| ORGAN-III feature shipped | 1 increment | H3 |
| Omega checklist reviewed | 1 review | All |
| Soak test data committed | 30 daily snapshots | H1 |
| Social media posts | 12-20 (3-5/week) | H4/H5 |
| Portfolio site updated | 1 refresh | H2/H5 |

These are **floors, not ceilings.** If you're shipping more, great. If you're consistently missing these, something is wrong with the schedule or the scope — adjust the cadence, not the sleep.

---

## PART III: CONTENT CADENCE

### Essay Publishing Rhythm

The construction sprints produced 29 essays in 3 days. That pace is unsustainable and unnecessary. Steady-state essay cadence:

| Frequency | Type | Effort | Source |
|-----------|------|--------|--------|
| Every 2 weeks | Meta-system essay | ~4 hours total (draft + edit + deploy) | ORGAN-V |
| Monthly | Theory deep-dive | ~6 hours total | ORGAN-I → ORGAN-V pipeline |
| Monthly | Product update / retrospective | ~2 hours total | ORGAN-III → ORGAN-V pipeline |
| As completed | Application post-mortem | ~1 hour | ORGAN-V (after each decision) |

**Annual target:** 24-30 essays (2/month average). This is a sustainable pace that keeps ORGAN-V active without starving ORGAN-I/II/III of creative energy.

### Social Media Schedule

The distribution-agent workflow runs weekly on Wednesday. Manual social posting should complement it:

**Mastodon (2-3 posts/week):**
- 1 essay thread (when publishing, typically Wednesday)
- 1-2 process notes (brief observations, in-progress screenshots, questions)
- Boost/reply to relevant posts in your community

**LinkedIn (1-2 posts/week):**
- 1 essay share (article format, Wednesday or Thursday)
- 1 industry reflection (Friday or weekend, if moved to engage)

**Discord (1-2 posts/week):**
- 1 essay announcement in relevant channels
- Ad hoc community engagement (replies, discussions)

**Timing guidance:**
- Mastodon: mornings (European audience is active early)
- LinkedIn: Tuesday-Thursday, 8-10 AM or 12-1 PM local time
- Discord: no optimal time — asynchronous by design

**Social media is not the work.** It is distribution of the work. If you're spending more than 30 minutes/day on social media, something is wrong. The posts should write themselves from the creative work you're already doing — a screenshot of code you wrote, a sentence from the essay you're editing, a link to the thing you shipped.

### Portfolio Site Refresh

The portfolio site (`4444j99.github.io/portfolio/`) should be updated monthly during Week 4's review cycle. Updates:

- Add any new projects or significant features shipped
- Update project status descriptions if they've changed
- Refresh metrics if they've moved meaningfully
- Ensure all links resolve

Do not redesign the portfolio. The CMYK + Jost + p5.js design from the ILLUSTRATIO Sprint is sufficient. The portfolio becomes stronger through *content* (more shipped projects to show), not through *design iterations*.

### Content Pipeline

The content pipeline flows from creative work to published artifact:

```
ORGAN-I (theory work, Monday)
    ↓ promotes to
ORGAN-V essay draft (Wednesday)
    ↓ deploys to
public-process _posts/ (next Wednesday)
    ↓ distributes via
ORGAN-VII social (same Wednesday)
    ↓ automated by
distribution-agent (Wednesday 10:00 UTC)
```

Similarly for ORGAN-III:

```
ORGAN-III (product work, Tuesday/Thursday)
    ↓ retrospective becomes
ORGAN-V product update essay (Week 2)
    ↓ deploys to
public-process _posts/
    ↓ distributes via
social + distribution-agent
```

The pipeline is designed so that creative work is **upstream** and content is a **natural byproduct.** You should never be "looking for things to write about." The writing comes from the doing.

---

## PART IV: IMMEDIATE PRIORITIES

This section contains time-bound actions that expire. It should be updated at each monthly review.

**Current as of:** 2026-02-16 (Checkpoint Alpha)

### THIS WEEK (Feb 17-21, 2026)

These actions are ordered by ROI. Do them in this order. Do not rearrange to do the comfortable thing first.

#### Day 1 (Monday, Feb 17): Submit Google Creative Lab Five

This is the single highest-ROI action available right now. All materials are prepared. The application portal is open. Zero applications have been submitted. Every day of delay is a day of zero external feedback.

**Steps:**
1. Open: https://www.creativelab5.com/
2. Review your prepared responses: `docs/applications/05-google-creative-lab-five-responses.md`
3. Confirm portfolio URL resolves: https://4444j99.github.io/portfolio/
4. Submit the application form (browser — not automatable)
5. Update the tracker:
   ```bash
   cd ~/Workspace/meta-organvm/organvm-corpvs-testamentvm
   # Edit docs/applications/04-application-tracker.md — change status to SUBMITTED
   git add docs/applications/04-application-tracker.md
   git commit -m "chore: mark Google Creative Lab Five as submitted"
   git push origin main
   ```

**Time:** ~1 hour
**Omega criteria advanced:** #5 (application submitted), feeds H2

#### Day 1 (Monday, Feb 17): Deploy AI-conductor Essay

The essay is drafted at `docs/essays/09-ai-conductor-methodology.md`. It needs to be formatted as a Jekyll post and deployed to ORGAN-V.

**Steps:**
1. Copy to public-process with Jekyll frontmatter:
   ```bash
   cd ~/Workspace/organvm-v-logos/public-process
   # Create the post file with proper Jekyll frontmatter
   # Date: 2026-02-17 (today's publish date)
   # Slug: ai-conductor-methodology
   ```
2. Follow the "Publish an Essay" workflow in `key-workflows.md`
3. Verify essay-monitor picks it up (or trigger manually):
   ```bash
   gh workflow run essay-monitor.yml --repo organvm-iv-taxis/orchestration-start-here
   ```

**Time:** ~30 min
**Omega criteria advanced:** #6 (AI-conductor essay published), feeds H2 + H5

#### Day 2 (Tuesday, Feb 18): Submit 3 Job Applications

All cover letters are drafted. All materials are ready. The portal URLs are in the application tracker. This is form-filling and uploading, not creative work.

**Highest fit-score targets:**
1. **Anthropic FDE, Custom Agents** (fit: 9/10)
   - URL: https://job-boards.greenhouse.io/anthropic/jobs/5074695008
   - Cover letter: `docs/applications/cover-letters/anthropic-fde-custom-agents.md`
2. **Together AI Lead DX** (fit: 9/10)
   - URL: https://job-boards.greenhouse.io/togetherai/jobs/4903661007
   - Cover letter: `docs/applications/cover-letters/together-ai-lead-dx-documentation.md`
3. **HuggingFace Dev Advocate** (fit: 8/10)
   - URL: https://apply.workable.com/huggingface/j/4C12FB7880
   - Cover letter: `docs/applications/cover-letters/huggingface-dev-advocate-hub-enterprise.md`

**Steps per application:**
1. Open the portal URL
2. Fill required fields (name, email, location, work authorization)
3. Upload resume (from portfolio: https://4444j99.github.io/portfolio/resume/)
4. Paste or upload cover letter
5. Add project links from the relevant cover letter's "Lead projects" section
6. Submit
7. Update `04-application-tracker.md` with submission date and confirmation

**Time:** ~2-3 hours total
**Omega criteria advanced:** #5 (application submitted), feeds H2

#### Day 3 (Wednesday, Feb 19): First Social Media Push

The AI-conductor essay is now published (from Day 1). Distribute it.

**Mastodon thread (3-5 posts):**
- Post 1: Hook — what the AI-conductor model is and why it matters
- Post 2: The key insight — human directs, AI generates volume, human reviews
- Post 3: Evidence — 386K words in 7 days across 91 repositories
- Post 4: The honest part — what AI-conductor can't do (community, revenue, validation)
- Post 5: Link to the full essay on public-process

**LinkedIn (article post):**
- Share the essay with a 2-3 paragraph intro framing it for a professional audience
- Tag relevant topics: #AIMethodology #BuildingInPublic #DeveloperExperience

**Discord:**
- Post in relevant channels with a brief description + link

**Time:** ~1 hour
**Omega criteria advanced:** Feeds #7 (external feedback), H4 (distribution), H5 (methodological authority)

#### Days 4-5 (Thursday-Friday, Feb 20-21): Select ORGAN-III Beta Product

The omega roadmap identifies `public-record-data-scrapper` as the highest-readiness ORGAN-III product candidate. Assess it.

**Steps:**
1. Review the codebase:
   ```bash
   cd ~/Workspace/organvm-iii-ergon/public-record-data-scrapper
   # Assess: directory structure, tech stack, existing features, test coverage
   ```
2. Answer these questions:
   - What does it do today? (core feature)
   - Who is the target user? (specific audience)
   - What's the minimum to deploy a usable beta? (MVP scope)
   - What infrastructure is needed? (domain, hosting, payment processor)
   - How long to get to beta launch? (realistic, not optimistic)
3. Write a 1-page product brief (store in this corpus: `docs/implementation/organ-iii-beta-brief.md`):
   - Target user persona
   - Core value proposition (one sentence)
   - MVP feature set (3-5 features)
   - Tech stack and deployment plan
   - Revenue model and pricing hypothesis
   - Timeline to beta (in weeks, not sprints)

**Time:** ~4 hours across 2 days
**Omega criteria advanced:** Feeds #8 (product live), #9 (revenue status), H3

### THIS MONTH (Feb 17 - Mar 18, 2026)

The month is anchored to the **Google Creative Fellowship deadline: March 18, 2026.** This is the only hard deadline in the system right now and it structures everything.

**Week 1 (Feb 17-21): Submissions Blitz**
- Submit Google Creative Lab Five (Day 1)
- Deploy AI-conductor essay (Day 1)
- Submit 3 job applications (Day 2)
- First social media distribution (Day 3)
- Assess ORGAN-III beta product candidate (Days 4-5)

**Week 2 (Feb 24-28): Product Development Begins**
- Begin ORGAN-III beta development (based on Week 1 assessment)
- Submit 2 more job applications (Anthropic SE Claude Code, OpenAI Applied Evals)
- Draft 1 essay (choose from: product development journal, theory deep-dive, or system retrospective)
- Continue daily soak test snapshots

**Week 3 (Mar 3-7): Product + Fellowship**
- Continue ORGAN-III development
- Finalize Google Creative Fellowship application materials
- Publish Week 2's essay draft
- Recruit 1 stranger test participant (reach out via social/community channels)

**Week 4 (Mar 10-14): Fellowship Submission + First Review**
- Submit Google Creative Fellowship (deadline: March 18, but submit by March 14 to avoid last-minute issues)
- Continue ORGAN-III development
- First 30-day omega checklist review (Checkpoint Alpha was Feb 16; first review March 16-18)
- Generate first soak test report: `python3 scripts/soak-test-monitor.py report --days 30`

**Post-Month (Mar 15-18): Buffer**
- Final review of Google Creative Fellowship submission
- Submit by March 18 at 5:00 PM PST absolute latest
- Commit soak test 30-day report

### REPO/ORGAN PRIORITY ORDER

This is the durable priority stack. It answers "what should I work on?" when you have unscheduled time.

**URGENT (this week, Feb 17-21):**
- `organvm-v-logos/public-process` — deploy AI-conductor essay
- Application submissions (not repo work — browser + email)

**HIGH (weeks 1-4, Feb 17 - Mar 18):**
- `organvm-iii-ergon/public-record-data-scrapper` — beta product candidate
- `organvm-v-logos/public-process` — 2 more essays this month
- `4444J99/portfolio` — update with current state after submissions
- Google Creative Fellowship — deadline March 18

**MEDIUM (month 2, Mar 18 - Apr 18):**
- `organvm-i-theoria/recursive-engine--generative-entity` — theory work feeds essays
- `organvm-ii-poiesis/metasystem-master` — creative work feeds portfolio
- `organvm-vi-koinonia` repos — salon planning for H4

**LOW / PARKED (month 3+):**
- ORGAN-II SKELETON repos (5 repos: example-generative-music, example-choreographic-interface, client-sdk, example-theatre-dialogue, audio-synthesis-bridge) — these become relevant when you're making art, not during validation
- ORGAN-VII workflow improvements — distribution-agent is running; optimize later
- Registry schema evolution — schema v0.5 is sufficient
- Any repo not listed above — 91 repos is enough; don't add more

**Hard deadlines integrated:**

| Deadline | Target | Action Required |
|----------|--------|----------------|
| **Open (NOW)** | Google Creative Lab Five | Submit immediately |
| **March 18, 2026** | Google Creative Fellowship | Submit by March 14 |
| **Spring 2026 (TBA)** | Eyebeam Residency | Monitor for open call |
| **~April-May 2026** | Processing Foundation | Monitor for announcement |
| **June 20, 2026** | Knight Foundation | Verify eligibility first |
| **July 9, 2026** | NEA GAP 2 | Find fiscal sponsor if pursuing |

---

## PART V: WHAT YOU'RE NOT CONSIDERING

This section is written in second person because it is addressed to the primary operator. It names the blind spots. Read it once. Read it again in 30 days.

### 1. The Construction Addiction

You have completed 16 sprints in 7 days. Each sprint had a name, a metric, a commit message, and a sense of completion. The dopamine loop of "name a sprint → execute it → update metrics → admire the diff" is powerful and immediate. Creative work — writing theory, making art, shipping products — does not produce this loop. Theory takes months to mature. Art takes false starts. Products take market feedback cycles. None of them produce the clean commit message of "feat: complete VERITAS Sprint."

**The guardrail: NO NEW NAMED INFRASTRUCTURE SPRINTS FOR 30 DAYS.** If you find yourself wanting to name Sprint 17, stop. Open this document. Read Part VI. Then go work on the ORGAN-III product or submit an application.

This does not mean "never improve infrastructure." If a CI workflow breaks, fix it. If the registry has an error, correct it. But those are maintenance tasks (MVO scope), not sprints. The difference between maintenance and a sprint is narrative: maintenance is "fixing a broken thing," a sprint is "building a new thing and naming it." You do not need new things. You need to use what you built.

### 2. Application Submission Is the Highest-ROI Action

Right now, today, the materials are ready:
- 7 cover letters drafted
- 9 submission bundles prepared
- Portfolio site deployed
- Resume page live
- Google Creative Lab Five application literally just needs to be submitted

Submitting 3 applications takes 2-3 hours and produces real external feedback. The feedback is binary and unambiguous: interview or rejection, funded or not funded. Another infrastructure sprint produces more internal metrics that you review yourself. The marginal value of the 92nd repo documented is approximately zero. The marginal value of the first application submitted is enormous.

### 3. The Soak Test Is Passive

The soak test monitor runs daily. It collects data. It generates reports. It does not require your active attention. Do not confuse "monitoring the soak test" with "doing work." Checking soak test data for 5 minutes is monitoring. Spending an hour analyzing trends in a 3-day-old dataset is procrastination disguised as diligence.

Your active work should be on H2 (validate externally) and H3 (generate revenue). H1 (prove it works) is already running. Let it run.

### 4. Energy Asymmetry

Writing theory (ORGAN-I) and writing applications require completely different cognitive modes. Theory is generative, exploratory, slow-burning. Applications are persuasive, precise, deadline-driven. Product development (ORGAN-III) is engineering — build, test, deploy. Social media posting is performative — short, punchy, audience-aware.

Do not schedule theory writing and application submission on the same day. The context switch cost is enormous and the quality of both suffers. This is why the weekly template assigns organ domains to specific days. Respect the rotation even when it feels inefficient — the efficiency gain from sustained cognitive mode more than compensates.

### 5. The ORGAN-II SKELETON Repos Are a Trap

Five repos in ORGAN-II have `implementation_status: SKELETON`:
- `example-generative-music`
- `example-choreographic-interface`
- `client-sdk`
- `example-theatre-dialogue`
- `audio-synthesis-bridge`

These feel urgent because they are "incomplete." The completionist impulse says: "everything else is ACTIVE, these should be too." But they are ORGAN-II (art) repos — they become relevant when you are actually making art, not during the validation phase. Filling them with scaffold code to change their status to ACTIVE would be exactly the kind of dishonesty the VERITAS Sprint corrected.

Park them. They will be there when ORGAN-II creative work produces something that belongs in them. Their current state (SKELETON) is *honest.* Honest is more important than complete.

### 6. Portfolio Site Staleness

The portfolio site shows 19 curated projects and was last updated during the ILLUSTRATIO Sprint. It looks good. It works. No one has seen it yet because no applications have been submitted. The portfolio becomes more valuable through *new projects to show* (ship an ORGAN-III product, publish more essays) than through *design iterations* (new color scheme, different layout, fancier animations).

Update it monthly. Do not redesign it. The Jost + CMYK + p5.js design system is sufficient. Direct your design energy toward the ORGAN-III product, where design quality actually affects revenue.

### 7. Revenue Requires Product Work, Not Documentation

Every sprint so far has been documentation. Writing README files, deploying CI workflows, configuring governance, generating essays about the system. These are all documentation acts, even when they involve code (the scripts, the workflows).

Shipping a product requires a fundamentally different kind of work:
- Writing application code (not infrastructure code)
- Building user interfaces (not README templates)
- Deploying to a domain (not to GitHub Pages)
- Integrating payment processing (not CI badges)
- Finding users (not documenting potential users)

The ORGAN-III repos have `revenue_status: pre-launch` because no product work has been done. Documentation of the *plan* to do product work is not product work. The 30-60 day beta timeline in the omega roadmap starts when you write the first line of product code, not when you write the first line of the product brief.

### 8. The 12-Week Content Calendar Is Stale

The content calendar in `public-process-map-v2.md` was designed during the launch era. It lists specific essays for specific weeks — "2026-02-24: recursive-engines-at-scale," "2026-03-10: generative-systems-case-study." These dates are fictional and the essay topics were aspirational.

The new cadence (Part III of this document) replaces the old calendar with a sustainable rhythm: 1 essay every 2 weeks, content flowing naturally from creative work. Do not try to follow the old calendar. It was designed for a different phase.

---

## PART VI: ANTI-PATTERNS

These are the specific traps you are most likely to fall into, based on the pattern of the last 16 sprints. Each anti-pattern is named so you can reference it in weekly reflections.

### AP-1: Don't Start Another Named Sprint

If you find yourself drafting a Sprint 17 description, stop. The sprint framework served construction mode. Construction mode is over. Use the weekly template (Part I) instead. Sprints produce infrastructure; the weekly template produces creative work.

**Test:** "Am I building the system or using the system?" If building, stop. If using, continue.

### AP-2: Don't Update the Registry Unless Something Actually Changed

The registry should only be updated when empirical state changes — a repo is promoted, archived, created, or its actual capabilities change. Do not update the registry to "reflect plans" or "capture intent." The registry captures reality.

**Test:** "Did something change in the real world (GitHub), or am I updating paperwork?" If paperwork, stop.

### AP-3: Don't Write More Documentation About Writing Documentation

This corpus has ~386K words. It has a CLAUDE.md, a constitution, an annotated manifest, governance rules, an implementation package, a public process map, an orchestration system spec, a repository standards doc, an SDD methodology, 5 planning documents, and this operational cadence document. If you find yourself creating a new document to describe how existing documents relate to each other, the documentation has reached self-referential saturation.

**Test:** "Is this document for an external audience, or am I explaining the system to myself?" If the latter, you don't need a document — you need to go do the thing.

### AP-4: Don't Optimize Workflows That Are Already Passing

The CI workflows are green. The orchestrator runs weekly. The essay-monitor runs daily. The validation pipeline catches dependency violations. Do not spend time making these "better" unless they are failing. Working is the goal; optimal is a trap.

**Test:** "Is this workflow failing, or am I making it more elegant?" If elegant, stop.

### AP-5: Don't Redesign the Portfolio When No One Has Seen It Yet

The portfolio is designed. It's deployed. It uses a coherent design system. Submit it in an application. Get feedback from a real reviewer. Then redesign based on feedback, not based on your own aesthetic restlessness.

**Test:** "Has an external person given me feedback that motivates this change?" If not, stop.

### AP-6: Don't Add Repos to Fill Perceived Gaps

91 repositories is enough. The temptation to create `organvm-iii-ergon/new-product-idea` or `organvm-i-theoria/another-framework` is real. Each new repo adds maintenance burden (CI, README, registry entry, seed.yaml, topics) and dilutes focus. Create new repos only when you have working code that doesn't fit an existing repo.

**Test:** "Do I have code written that needs a home, or am I creating a home for code I haven't written?" If the latter, stop.

### AP-7: Don't Confuse Motion With Progress

Committing soak test data every day feels productive. Updating system-metrics.json feels productive. Reviewing workflow runs feels productive. These are maintenance activities with near-zero impact on the omega criteria. They keep the lights on but they don't move the needle.

Progress on omega looks like:
- An application submitted (H2 #5)
- An essay published (H2 #6)
- A product feature deployed (H3 #8)
- A stranger completing the navigation test (H1 #2)
- A real human reading your work and responding (H4 #12, #13)

**Test:** "Does this advance an omega criterion, or does it make my dashboard look better?" If dashboard, defer it to Friday review.

---

## APPENDIX: Quick Reference Card

*Designed to be printed, pinned, or kept in a terminal scratchpad.*

```
╔══════════════════════════════════════════════════════════════╗
║          OPERATIONAL CADENCE — QUICK REFERENCE              ║
╠══════════════════════════════════════════════════════════════╣
║                                                              ║
║  DAILY                                                       ║
║  □ Morning:  Check workflow runs (5 min)                     ║
║  □ Midday:   Shallow ops batch (30 min)                      ║
║  □ Evening:  Soak test snapshot (5 min)                      ║
║                                                              ║
║  WEEKLY ROTATION                                             ║
║  Mon: ORGAN-I/II (theory + creative)                         ║
║  Tue: ORGAN-III (product development)                        ║
║  Wed: ORGAN-V/VII (content + distribution)                   ║
║  Thu: ORGAN-III + applications/outreach                      ║
║  Fri: System health + omega review + plan next week          ║
║  Sat-Sun: REST. The system is autonomous.                    ║
║                                                              ║
║  MONTHLY CYCLE                                               ║
║  Week 1: Product sprint                                      ║
║  Week 2: Content sprint                                      ║
║  Week 3: Outreach sprint                                     ║
║  Week 4: Review + maintenance                                ║
║                                                              ║
║  MONTHLY MINIMUMS                                            ║
║  □ 2 essays published                                        ║
║  □ 1 application submitted                                   ║
║  □ 1 ORGAN-III feature shipped                               ║
║  □ 1 omega checklist review                                  ║
║  □ 30 soak test snapshots committed                          ║
║  □ Portfolio updated                                         ║
║                                                              ║
║  HORIZON STATUS (check monthly)                              ║
║  H1: Prove It Works     — Days 1-30   (soak test, stranger)  ║
║  H2: Validate Externally — Days 15-90 (apps, essays)         ║
║  H3: Generate Revenue   — Days 30-180 (product, payments)    ║
║  H4: Build Community    — Days 60-365 (salons, contributors) ║
║  H5: Achieve Recognition — Days 90-730 (grants, citations)   ║
║                                                              ║
║  HARD DEADLINES                                              ║
║  Mar 18: Google Creative Fellowship                          ║
║  Jun 20: Knight Foundation                                   ║
║  Jul  9: NEA GAP 2                                           ║
║                                                              ║
║  ANTI-PATTERN QUICK CHECK                                    ║
║  "Am I building the system or using it?"                     ║
║  "Did something actually change?"                            ║
║  "Has an external person motivated this?"                    ║
║  "Does this advance an omega criterion?"                     ║
║                                                              ║
║  COMMANDS                                                    ║
║  gh run list --repo organvm-iv-taxis/orchestration-start-    ║
║    here --limit 5                    # workflow status        ║
║  python3 scripts/soak-test-monitor.py collect  # snapshot    ║
║  python3 scripts/soak-test-monitor.py report   # 30-day rpt  ║
║  python3 scripts/organ-audit.py --registry registry-v2.json  ║
║    --governance governance-rules.json --output audit.md      ║
║                                                              ║
╚══════════════════════════════════════════════════════════════╝
```

---

## Omega Criteria Cross-Reference

For traceability, here is how this cadence document maps to the 17 omega criteria from the roadmap:

| # | Criterion | Where in This Cadence |
|---|-----------|----------------------|
| 1 | 30-day soak test | Daily anchor (evening snapshot), Friday review |
| 2 | Stranger test ≥80% | Week 3 outreach sprint, Part IV immediate priorities |
| 3 | Engagement baseline (30 days) | Passive — soak-test-monitor tracks this automatically |
| 4 | Runbooks validated | Week 3 outreach sprint (recruit second operator) |
| 5 | ≥1 application submitted | Part IV Day 1-2 (this week!), monthly minimum |
| 6 | AI-conductor essay published | Part IV Day 1 (this week!) |
| 7 | ≥3 external feedback | Accumulates from H2 submissions over months |
| 8 | ≥1 ORGAN-III product live | Tuesday product days, Week 1 product sprint |
| 9 | `revenue_status: live` | Follows from #8 after payment integration |
| 10 | MRR ≥ operating costs | Follows from #9 with user acquisition |
| 11 | ≥2 salons/events | Week 3 outreach sprint, MEDIUM priority (month 2+) |
| 12 | ≥3 external contributions | H4 — develops organically from H2/H3 visibility |
| 13 | ≥1 organic inbound link | H4 — develops organically from published content |
| 14 | ≥1 recognition event | H5 — harvest of H1-H4 |
| 15 | Portfolio updated with validation | Week 4 review (monthly portfolio refresh) |
| 16 | Bus factor >1 | Runbook validation + second operator recruitment |
| 17 | 30+ days without intervention | Soak test (already running) |

---

*This document was created at Checkpoint Alpha (2026-02-16), the transition point between construction and operation. It should be updated monthly during the Week 4 review cycle. When the document starts feeling obsolete, that's a good sign — it means the cadence has become internalized and the operator is living in the system, not reading instructions about how to live in the system.*
