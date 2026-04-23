# Governance-as-Code: Repository Rulesets

**Status:** Active
**Date:** 2026-04-23
**Source atom:** `prompt-a337b84aac10`
**Research ref:** `praxis-perpetua/research/2025-11-github-business-playbook.md`

## Purpose

The ORGANVM system constitution exists as documents (CLAUDE.md files, governance-rules.json,
seed.yaml contracts). This specification defines how to enforce those documents as
non-negotiable policy using GitHub org-level repository rulesets.

## Org-Level Ruleset: Constitutional Compliance

This ruleset applies to all repositories across all ORGANVM GitHub organizations.

### Ruleset Definition

```yaml
name: "Constitutional Compliance"
target: all_repositories
enforcement: active

rules:
  # Prevent destructive history rewriting
  block_force_pushes: true

  # Enforce linear history for clean audit trails
  require_linear_history: true

  # All commits must be signed (SSH or GPG)
  require_signed_commits: true

  # No direct pushes to main -- PRs required
  require_pull_request:
    required_approving_review_count: 0  # Solo operator, self-merge permitted
    dismiss_stale_reviews: true
    require_code_owner_approval: false  # Enable when team structure is populated
    require_last_push_approval: false
```

### Implementation Commands

```bash
# For each ORGANVM org, create the ruleset via GitHub CLI
ORG_SLUG="meta-organvm"  # Repeat for each org

# Create the ruleset
gh api "orgs/$ORG_SLUG/rulesets" -X POST \
  --input - <<'EOF'
{
  "name": "Constitutional Compliance",
  "target": "branch",
  "enforcement": "active",
  "conditions": {
    "ref_name": {
      "include": ["~DEFAULT_BRANCH"],
      "exclude": []
    }
  },
  "rules": [
    { "type": "deletion" },
    { "type": "non_fast_forward" },
    { "type": "required_linear_history" },
    {
      "type": "pull_request",
      "parameters": {
        "required_approving_review_count": 0,
        "dismiss_stale_reviews_on_push": true,
        "require_code_owner_review": false,
        "require_last_push_approval": false
      }
    }
  ],
  "bypass_actors": [
    {
      "actor_type": "OrganizationAdmin",
      "bypass_mode": "always"
    }
  ]
}
EOF
```

## Reusable Workflows

The second pillar of governance-as-code: all repos share a single CI/CD pipeline via
GitHub reusable workflows stored in each org's `.github` repository.

### Standard Workflow Template

```yaml
# .github/workflows/standard-ci.yml (in org .github repo)
name: Standard CI
on:
  workflow_call:
    inputs:
      language:
        type: string
        required: true
      test_command:
        type: string
        default: "pytest tests/ -v"

jobs:
  lint:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Lint
        run: |
          if [ "${{ inputs.language }}" = "python" ]; then
            pip install ruff
            ruff check src/
          elif [ "${{ inputs.language }}" = "typescript" ]; then
            npm ci
            npm run typecheck
          fi

  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Test
        run: ${{ inputs.test_command }}

  seed-validate:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Validate seed.yaml
        run: |
          if [ -f seed.yaml ]; then
            python3 -c "import yaml; yaml.safe_load(open('seed.yaml'))"
          fi
```

### Consumer Workflow

Individual repos call the shared workflow:

```yaml
# .github/workflows/ci.yml (in each repo)
name: CI
on: [push, pull_request]

jobs:
  ci:
    uses: <ORG_SLUG>/.github/.github/workflows/standard-ci.yml@main
    with:
      language: python
      test_command: "pytest tests/ -v"
```

## Identity Model: GitHub Apps for Automation

When the system scales beyond single-operator, automation should use GitHub Apps
(not personal access tokens) for:

- Bot commits from CI/CD pipelines
- Automated PR creation by agents
- Webhook-driven dispatch

### Decision Needed

**Human decision required:** Whether to create a dedicated GitHub App for the ORGANVM
conductor vs. continuing with PAT-based authentication. The App model provides:
- Per-installation token scoping (limits blast radius)
- Distinct bot identity in git history
- Rate limit isolation from human account

The PAT model is simpler but bundles all automation under one identity.

## Phased Rollout

| Phase | Action | Organs |
|-------|--------|--------|
| 1 | Create Constitutional Compliance ruleset | meta-organvm |
| 2 | Deploy reusable workflow to `.github` repo | meta-organvm |
| 3 | Roll out rulesets to all organ orgs | I through VII |
| 4 | Migrate repos to reusable workflow calls | All active repos |
| 5 | Evaluate GitHub App vs PAT for automation | System-wide |
