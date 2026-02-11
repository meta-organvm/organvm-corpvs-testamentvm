# Implementation Sprint Specs: Phase 3 Priority Repos

**Goal:** Elevate 5 priority repos from current state to target state (Days 45-75)
**Updated:** 2026-02-11

These specs define the minimum viable implementation for each repo to close the gap between documentation (which exists) and working code. Each spec follows the AI-conductor model: AI generates the scaffolding and boilerplate, human reviews for accuracy and architectural soundness.

---

## 1. call-function--ontological (ORGAN-I)

**Org:** organvm-i-theoria
**Current:** SKELETON (has Python directory structure: core/, application/, tools/)
**Target:** PROTOTYPE
**Portfolio relevance:** CRITICAL — AI/ontology intersection, strongest evidence for AI engineering roles
**Dependency:** organvm-i-theoria/organon-noumenon--ontogenetic-morphe

### What Exists
- README (4,233 words) describing the 12-concept ontological function-calling framework
- Directory structure: `core/`, `application/`, `tools/`
- No meaningful implementation code

### What "PROTOTYPE" Means
A working demonstration of the 12-concept architecture that can:
1. Parse a function call through the ontological lens (Heideggerian Dasein, Aristotelian four causes, Peircean semiotics)
2. Ground at least 3 of the 12 concepts as executable Python
3. Include a CLI that demonstrates concept application to a sample function-calling scenario
4. Pass basic tests proving the grounding logic works

### Implementation Spec

```
call-function--ontological/
├── core/
│   ├── __init__.py
│   ├── ontology.py          # 12-concept definitions as dataclasses
│   ├── grounding.py         # Maps function calls → ontological categories
│   ├── four_causes.py       # Aristotelian: material, formal, efficient, final
│   ├── dasein.py            # Heideggerian: being-in-the-world context for tool use
│   └── semiotics.py         # Peircean: sign-object-interpretant for parameter types
├── application/
│   ├── __init__.py
│   ├── analyzer.py          # Takes a function signature → ontological analysis
│   └── grounding_report.py  # Generates human-readable grounding report
├── tools/
│   ├── __init__.py
│   └── cli.py               # CLI entry point: `python -m tools.cli analyze <function>`
├── tests/
│   ├── test_ontology.py     # 12 concepts instantiate correctly
│   ├── test_grounding.py    # Known function calls map to expected categories
│   ├── test_four_causes.py  # Aristotelian analysis produces valid output
│   └── test_cli.py          # CLI runs without error on sample input
├── examples/
│   └── sample_analysis.py   # Demo: analyze a real OpenAI function-calling schema
├── pyproject.toml
└── ci-python.yml → .github/workflows/
```

### Key Design Decisions
- Pure Python, no ML dependencies (consistent with RE:GE philosophy)
- Concepts are dataclasses with `validate()` methods
- Grounding is deterministic (no LLM inference) — the framework categorizes, it doesn't generate
- Compatible with OpenAI function-calling JSON schema as input format
- Tests target 70%+ coverage on core/

### TE Budget
~88K TE (README POPULATE equivalent — code structure exists, need implementation)

### Success Criteria
- [ ] `python -m tools.cli analyze examples/openai_schema.json` produces ontological report
- [ ] 20+ tests passing
- [ ] CI workflow runs green
- [ ] At least 3 of 12 concepts fully implemented with tests

---

## 2. example-ai-collaboration (ORGAN-II)

**Org:** organvm-ii-poiesis
**Current:** SKELETON (README + docs only, no code)
**Target:** PROTOTYPE
**Portfolio relevance:** HIGH — Most relevant 2026 topic for grants and hiring
**Dependencies:** None

### What Exists
- README (4,172 words) describing the AI-conductor model as artistic practice
- No implementation code

### What "PROTOTYPE" Means
A working demonstration of the AI-conductor collaboration model that:
1. Tracks human-AI attribution across a creative session
2. Generates a process document showing who contributed what
3. Demonstrates at least one collaboration workflow (e.g., text generation with human editing)
4. Includes exportable collaboration logs

### Implementation Spec

```
example-ai-collaboration/
├── src/
│   ├── __init__.py
│   ├── session.py            # CollaborationSession: tracks turns, attributions
│   ├── attribution.py        # Attribution model: human_authored, ai_generated, co_created
│   ├── conductor.py          # AIConductor: manages prompt→response→review cycles
│   ├── export.py             # Export session to markdown process document
│   └── metrics.py            # Session metrics: human/AI ratio, edit distance, etc.
├── workflows/
│   ├── __init__.py
│   ├── text_generation.py    # Workflow: iterative text generation with human review
│   └── code_generation.py    # Workflow: code generation with human refinement
├── examples/
│   ├── demo_text_session.py  # Run a simulated text collaboration session
│   └── demo_code_session.py  # Run a simulated code collaboration session
├── tests/
│   ├── test_session.py       # Session lifecycle: create, add turns, close
│   ├── test_attribution.py   # Attribution categories assigned correctly
│   ├── test_export.py        # Export produces valid markdown
│   └── test_metrics.py       # Metrics calculate correctly
├── docs/
│   └── process-template.md   # Template for exported process documents
├── pyproject.toml
└── ci-python.yml → .github/workflows/
```

### Key Design Decisions
- Pure Python — no API keys required for demo (uses mock LLM responses)
- Attribution is structural, not AI-detected — the system tracks what was generated vs. edited
- Export format is markdown — compatible with ORGAN-V documentation pipeline
- Session data is JSON-serializable for archival
- Simulated workflows demonstrate the pattern without requiring live API access

### TE Budget
~88K TE (README POPULATE)

### Success Criteria
- [ ] `python examples/demo_text_session.py` produces a collaboration log
- [ ] Export generates a readable markdown process document
- [ ] Attribution tracking correctly distinguishes human/AI/co-created content
- [ ] 15+ tests passing
- [ ] CI workflow runs green

---

## 3. example-interactive-installation (ORGAN-II)

**Org:** organvm-ii-poiesis
**Current:** SKELETON (README + docs only, no code)
**Target:** PROTOTYPE
**Portfolio relevance:** HIGH — Art residency portfolio piece
**Dependencies:** organvm-ii-poiesis/metasystem-master

### What Exists
- README (3,920 words) describing sensor-driven interactive installations
- No implementation code

### What "PROTOTYPE" Means
A working reference implementation that:
1. Simulates sensor input (depth camera, LIDAR, motion) without requiring hardware
2. Maps sensor data to visual/audio output parameters
3. Includes a basic visualization (even terminal-based) showing the mapping
4. Demonstrates the architecture pattern for installation artists

### Implementation Spec

```
example-interactive-installation/
├── src/
│   ├── __init__.py
│   ├── sensor_sim.py         # Simulated sensor input: depth, lidar, motion
│   ├── mapping.py            # Parameter mapping: sensor data → output parameters
│   ├── output.py             # Output abstraction: visual, audio, spatial
│   ├── engine.py             # Main loop: read sensors → map → render
│   └── config.py             # Installation configuration (YAML-based)
├── renderers/
│   ├── __init__.py
│   ├── terminal.py           # Terminal-based ASCII visualization
│   ├── json_stream.py        # JSON output for piping to external renderers
│   └── osc.py                # OSC protocol output (for Max/MSP, TouchDesigner)
├── presets/
│   ├── depth_field.yaml      # Preset: depth camera → particle field
│   ├── motion_trace.yaml     # Preset: motion tracking → trail visualization
│   └── spatial_audio.yaml    # Preset: LIDAR → spatial audio positioning
├── examples/
│   └── run_simulation.py     # Run with simulated sensors + terminal renderer
├── tests/
│   ├── test_sensor_sim.py    # Simulated sensors produce valid data
│   ├── test_mapping.py       # Mappings transform correctly
│   ├── test_engine.py        # Engine loop processes without error
│   └── test_config.py        # YAML configs parse correctly
├── pyproject.toml
└── ci-python.yml → .github/workflows/
```

### Key Design Decisions
- No hardware dependencies — everything runs with simulated sensors
- YAML-based configuration makes presets sharable and versionable
- OSC output enables integration with standard creative coding tools (Max/MSP, TouchDesigner, SuperCollider)
- Terminal renderer provides instant visual feedback without graphics dependencies
- Architecture mirrors real installation patterns: input → mapping → output pipeline

### TE Budget
~88K TE (README POPULATE)

### Success Criteria
- [ ] `python examples/run_simulation.py` runs with terminal visualization
- [ ] At least 2 presets work end-to-end
- [ ] OSC output sends valid messages (testable without receiver)
- [ ] 15+ tests passing
- [ ] CI workflow runs green

---

## 4. tab-bookmark-manager (ORGAN-III)

**Org:** organvm-iii-ergon
**Current:** PRODUCTION (has real code: backend/, extension/, ml-service/, docker-compose)
**Target:** DEPLOYED
**Portfolio relevance:** HIGH — Full-stack SaaS product
**Dependencies:** organvm-i-theoria/my-knowledge-base

### What Exists
- README (3,974 words)
- Real codebase: backend/ (API), extension/ (browser), ml-service/ (ML categorization)
- docker-compose.yml for local development
- CI workflow (ci-typescript.yml)

### What "DEPLOYED" Means
The application is accessible and demonstrable:
1. Docker Compose stack runs locally without manual configuration
2. Backend API responds to health checks
3. Browser extension builds without errors
4. ML service loads and categorizes sample bookmarks
5. A deployment target is configured (even if just documentation for self-hosting)

### Implementation Spec (Gap Analysis)

```
What needs to happen (not a new file tree — code exists):

1. Docker Compose Validation
   - [ ] `docker-compose up` starts all 3 services cleanly
   - [ ] Backend health endpoint responds at /api/health
   - [ ] ML service health endpoint responds
   - [ ] Verify inter-service communication

2. Backend Fixes (if needed)
   - [ ] Environment variables documented in .env.example
   - [ ] Database migrations run on first start
   - [ ] Seed data available for demo mode

3. Extension Build
   - [ ] `npm run build` produces extension artifact
   - [ ] Extension manifest is valid for Chrome/Firefox
   - [ ] Extension connects to local backend

4. ML Service
   - [ ] Model loads on startup (or downloads on first run)
   - [ ] Categorization endpoint accepts bookmark JSON
   - [ ] Returns valid category predictions

5. Deployment Documentation
   - [ ] docs/deployment.md — self-hosting guide
   - [ ] docs/demo-mode.md — running the demo locally
   - [ ] .env.example with all required variables
```

### Key Design Decisions
- "Deployed" means locally demonstrable, not cloud-hosted (no hosting costs)
- Demo mode with seed data lets evaluators see the product without setup
- Self-hosting documentation is the deployment artifact
- No changes to architecture — just closing gaps between "code exists" and "code runs"

### TE Budget
~50K TE (README REVISE equivalent — code exists, needs polish and validation)

### Success Criteria
- [ ] `docker-compose up` → all services healthy within 60 seconds
- [ ] Backend API serves at least 3 endpoints
- [ ] Extension builds without errors
- [ ] ML service categorizes sample bookmarks
- [ ] Deployment docs exist and are accurate

---

## 5. the-actual-news (ORGAN-III)

**Org:** organvm-iii-ergon
**Current:** PRODUCTION (has real code: apps/, contracts/, services/, pnpm workspace)
**Target:** DEPLOYED
**Portfolio relevance:** HIGH — Civic tech product
**Dependencies:** None
**Type:** B2C

### What Exists
- README (3,739 words)
- Real codebase: apps/ (frontend), contracts/ (smart contracts), services/ (backend)
- pnpm workspace configuration
- CI workflow (ci-typescript.yml)

### What "DEPLOYED" Means
The application is accessible and demonstrable:
1. Development server starts and serves the frontend
2. Backend services respond to API calls
3. Smart contracts compile (even if not deployed to mainnet)
4. A demo mode exists that doesn't require blockchain infrastructure

### Implementation Spec (Gap Analysis)

```
What needs to happen:

1. Development Environment
   - [ ] `pnpm install` completes without errors
   - [ ] `pnpm dev` starts the development server
   - [ ] Frontend renders at localhost
   - [ ] Environment variables documented in .env.example

2. Backend Services
   - [ ] At least one service starts and responds to health checks
   - [ ] API documentation (even minimal) exists
   - [ ] Demo mode bypasses blockchain requirements

3. Smart Contracts
   - [ ] Contracts compile with `pnpm build:contracts` (or equivalent)
   - [ ] Basic contract tests pass
   - [ ] Local testnet configuration documented (Hardhat/Foundry)

4. Demo Mode
   - [ ] Frontend works with mock data (no live blockchain)
   - [ ] News verification flow demonstrable without real transactions
   - [ ] Screenshots or recording available for portfolio

5. Deployment Documentation
   - [ ] docs/local-development.md — getting started guide
   - [ ] docs/architecture.md — system component diagram
   - [ ] .env.example with all required variables
```

### Key Design Decisions
- "Deployed" means locally demonstrable with mock blockchain
- Civic tech narrative is strong for grants — the demo should tell the story
- No mainnet deployment required (gas costs, infrastructure)
- Demo mode is the primary artifact: prove the concept works

### TE Budget
~50K TE (README REVISE equivalent)

### Success Criteria
- [ ] `pnpm install && pnpm dev` starts the application
- [ ] Frontend renders with mock or demo data
- [ ] Smart contracts compile
- [ ] Local development docs exist and are accurate
- [ ] At least one end-to-end flow works in demo mode

---

## Priority Order

| # | Repo | Impact | Effort | Priority |
|---|------|--------|--------|----------|
| 1 | call-function--ontological | CRITICAL (AI roles) | HIGH (build from scratch) | **Week 7** |
| 2 | example-ai-collaboration | HIGH (2026 relevance) | HIGH (build from scratch) | **Week 7-8** |
| 3 | tab-bookmark-manager | HIGH (working product) | LOW (polish existing) | **Week 8** |
| 4 | the-actual-news | HIGH (civic tech) | MEDIUM (polish existing) | **Week 9** |
| 5 | example-interactive-installation | HIGH (residencies) | HIGH (build from scratch) | **Week 9-10** |

### Rationale
- **call-function--ontological** first: CRITICAL relevance for AI engineering applications (Phase 2 targets). Every day this is a skeleton weakens the Anthropic/OpenAI applications.
- **tab-bookmark-manager** and **the-actual-news** are lower effort (code exists, just needs validation and deployment docs). Good for quick wins mid-sprint.
- **example-interactive-installation** last: primarily supports residency applications, which have later deadlines (Spring/Summer 2026).

---

## Total TE Budget

| Repo | TE |
|------|-----|
| call-function--ontological | ~88K |
| example-ai-collaboration | ~88K |
| example-interactive-installation | ~88K |
| tab-bookmark-manager | ~50K |
| the-actual-news | ~50K |
| **Total** | **~364K TE** |

This is approximately 5.6% of the original 6.5M TE total project budget.
