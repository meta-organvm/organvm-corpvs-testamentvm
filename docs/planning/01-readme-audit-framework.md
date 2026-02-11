# 01: README AUDIT FRAMEWORK

**Purpose:** Define comprehensive README methodology + templates per organ type  
**Duration:** Subtask 1.1 (~88K TE)
**Output:** Framework + 7 templates + scoring rubric  

---

## Part 1: Scoring Methodology (0-100)

### README Quality Score Rubric

**Existence & Accessibility (0-20 points)**
- README exists in root directory (5 points)
- Clear title + one-line description (5 points)  
- Navigation/table of contents present (5 points)
- Clean formatting + readable layout (5 points)

**Content Completeness (0-40 points)**
- Problem statement clearly explained (10 points)
- Installation/setup instructions complete (10 points)
- 2+ working examples included (10 points)
- All dependencies documented (5 points)
- Contributing guidelines present (5 points)

**Accuracy & Currency (0-20 points)**
- All links valid (no 404s) (5 points)
- Code examples actually work (5 points)
- Documentation matches current code (5 points)
- Last update date visible (5 points)

**Portfolio Relevance (0-20 points)**
- Why this repo exists clearly stated (5 points)
- Connection to larger system shown (5 points)
- Key features or value proposition listed (5 points)
- Metrics, use cases, or impact evidence (5 points)

### Score Interpretation

- 90-100: Production-ready, minimal revision needed
- 75-89: Good foundation, focused additions needed
- 60-74: Partial documentation, substantial revision needed
- 40-59: Minimal documentation, major overhaul needed
- 0-39: Missing/outdated, complete rewrite needed

---

## Part 2: Organ-Specific Definitions

### ORGAN-I (Theory) — 3,000+ words target (AI-generated, human-reviewed)

**Sections must include:**
1. Problem statement (what intellectual gap?)
2. Conceptual overview (3-5 core ideas)
3. Related work (academic/artistic precedent)
4. Examples (runnable code if applicable)
5. Downstream usage (which ORGAN-II repos implement this?)
6. Roadmap (future directions)
7. Cross-references (links to other theory repos)
8. Author/contact info

**Common gaps:** Vague problem statements, no downstream examples, missing related work, non-functional code

**Portfolio language:** "Contributes epistemological framework for autonomous creative systems"

---

### ORGAN-II (Art) — 2,500+ words + working demos target (AI-generated, human-reviewed)

**Sections must include:**
1. Artistic purpose (what does it create?)
2. Conceptual approach (design rationale + aesthetics)
3. Technical overview (how it works, high-level)
4. Installation instructions (how to run it)
5. Working demos (video/images/interactive)
6. Theory implemented (ORGAN-I repos it builds on)
7. Portfolio/exhibition history (where shown?)
8. Contributing (how others extend it)
9. Author/contact info

**Common gaps:** No working demos, weak theory connection, missing portfolio, hard to actually run

**Portfolio language:** "Demonstrates theory from ORGAN-I in creative practice; exhibited at..."

---

### ORGAN-III (Commerce) — 2,000+ words + governance + metrics target (AI-generated, human-reviewed)

**Sections must include:**
1. Product overview (what does it do?)
2. User value (why is this valuable?)
3. Business model (revenue, pricing, SLAs)
4. Technical architecture (system design)
5. Getting started (path from interest to use)
6. Case study (how it was built)
7. Metrics (users, revenue, growth)
8. Support/governance (issue resolution, terms)
9. Author/contact info

**Common gaps:** Vague value prop, no metrics, no governance, unclear architecture

**Portfolio language:** "Generated $X revenue from X customers; demonstrates theory application at scale"

---

### ORGAN-IV (Orchestration) — Governance-focused

**Sections must include:**
1. Orchestration purpose (what does this coordinate?)
2. Registry overview (link + contents)
3. Governance rules (promotion + dependency)
4. How it works (high-level flow)
5. Key concepts (promotion, dependency, validation)
6. Examples ("here's how Theory→Art happens")
7. Contributing (propose governance changes)
8. Author/contact info

**Common gaps:** Too technical, no examples, registry unclear

**Portfolio language:** "Demonstrates governance-first design for autonomous systems coordination"

---

### ORGAN-V (Public) — Publishing-focused

**Sections must include:**
1. Publication purpose (what is this?)
2. Publishing guidelines (how to submit essays)
3. Essay structure (format, frontmatter)
4. Essay index (all published content)
5. RSS/newsletter (how to subscribe)
6. Contributing (guest essays process)
7. Archive (where to find older content)
8. Author/contact info

---

### ORGAN-VI (Community) — Participation-focused

**Sections must include:**
1. Community purpose (why this space?)
2. Participation model (how to join?)
3. Community guidelines (expected behavior)
4. Archive structure (what's recorded?)
5. Access model (invitation management)
6. Contributing (member participation)
7. Author/contact info

---

### ORGAN-VII (Marketing) — Strategy-focused

**Sections must include:**
1. Distribution strategy (platforms, cadence)
2. Audience target (who are we reaching?)
3. Content types (formats used)
4. Metrics (how do we track success?)
5. Channels (Mastodon, LinkedIn, newsletter)
6. Publishing calendar (when content goes out)
7. Templates (announcement formats)
8. Author/contact info

---

## Part 3: Template Instructions

**For each repo:**
1. Copy organ-specific template (Document 03)
2. Fill in sections with repo-specific content
3. Customize examples to this repo
4. Add working code samples (if applicable)
5. Include 2+ concrete examples
6. Link to upstream + downstream repos
7. Peer-review for accuracy + clarity
8. Validate all links before commit

**Expected review time per AI-generated draft:**
- ORGAN-I/III: 15-20 minutes (verify accuracy of complex topics)
- ORGAN-II: 20-30 minutes (verify examples + portfolio links)
- ORGAN-IV/V/VI/VII: 10-15 minutes (lighter review)

---

## Part 4: Quality Checklist

**Every README must:**
- [ ] Have clear title + tagline
- [ ] Explain why it exists (problem statement)
- [ ] Include installation instructions
- [ ] Have 2+ working examples
- [ ] Link to related repos (upstream + downstream)
- [ ] Include author/contact info
- [ ] Have all links validated
- [ ] Be reviewed by someone other than author
- [ ] Be written in plain language (not jargon-heavy)
- [ ] Include portfolio language (external visibility)

---

## Part 5: Common Mistakes (AI-Conductor Model)

1. **Accepting AI output uncritically** — AI generates fluent prose but may hallucinate examples, miss project-specific context, or use generic phrasing. Review every draft for accuracy.
2. **"Good enough" READMEs** — No. External evaluators see them. AI can hit word count easily; the risk is generic quality, not insufficient quantity.
3. **Non-working code examples** — AI-generated code examples may not run. Test everything before publishing.
4. **Missing cross-references** — AI may generate plausible-sounding but incorrect cross-repo links. Verify every link.
5. **Vague problem statements** — AI defaults to "interesting framework" boilerplate. Ensure each README has a specific, distinctive problem statement.
6. **No portfolio infrastructure** — showcase + archive critical for ORGAN-II. AI can draft structure but human must curate actual works.

---

**Framework Status:** Complete  
**Next:** Document 02 (Repo Inventory Audit)
