# Team Structure and Permission Model

**Status:** Active
**Scope:** All ORGANVM GitHub organizations
**Source atom:** `prompt-380062cff468`
**Last updated:** 2026-04-23

## Identity and Scope

This document defines the team topology, permission model, and code ownership conventions
for ORGANVM GitHub organizations. While authored originally for `ivviiviivvi` (ORGAN-I),
the patterns apply to all eight organ organizations with org-specific slug substitution.

**Environment binding:** Each org has its own `ORG_SLUG` value.

| Organ | ORG_SLUG |
|-------|----------|
| I | `ivviiviivvi` (or `organvm-i-theoria`) |
| II | `omni-dromenon-machina` (or `organvm-ii-poiesis`) |
| III | `labores-profani-crux` (or `organvm-iii-ergon`) |
| IV | TBD |
| V | TBD |
| VI | TBD |
| VII | TBD |
| Meta | `meta-organvm` |

## Teams and Intent

### Leadership (team slug: `leadership`)

**Purpose:** Organization administrators and final decision makers.
**Baseline access:** Administrative access to all repositories.
**Operational note:** Not intended for routine code review routing. Control-plane
governance and emergency access only.

### Engineering (team slug: `engineering`)

**Purpose:** All engineering contributors; parent team for engineering sub-teams.
**Baseline access:** Write access to code repositories by default, with CODEOWNERS
routing to sub-teams by path.

### Engineering Sub-Teams (parent: `engineering`)

| Team | Slug | Purpose |
|------|------|---------|
| Frontend | `frontend` | Frontend code and UI |
| Backend | `backend` | Backend services and APIs |
| DevOps | `devops` | Infrastructure, CI/CD, deployment |
| Security | `security` | Security review and vulnerability management |

### Product (team slug: `product`)

**Purpose:** Product management.
**Baseline access:** Read access to code repositories; triage access to issues and
discussions where enabled.

### Design (team slug: `design`)

**Purpose:** Design and UX.
**Baseline access:** Read access to code repositories; write access to design-specific
repositories (brand assets, design systems, UI kits).

### Contractors (team slug: `contractors`)

**Purpose:** External contributors with minimal access.
**Baseline access:** Read-only by default; time-limited membership; escalation via
per-repository grant when necessary.

## Permission Model

Repository permissions use GitHub's standard levels: `pull`, `triage`, `push`, `maintain`, `admin`.

### Default Policy

| Team | Permission Level | Scope |
|------|-----------------|-------|
| Leadership | `admin` | All repositories |
| Engineering (parent) | `push` | Engineering-owned repositories only |
| Frontend/Backend/DevOps/Security | `push` | Owned repositories; optionally `maintain` on managed repos |
| Product | `pull` on code; `triage` on issue repos | Selective |
| Design | `pull` on code; `push` on design repos | Selective |
| Contractors | `pull` only | Never `admin`; no broad org-wide grants |

## CODEOWNERS Integration

CODEOWNERS supports users and teams via `@org/team-name`. Teams referenced in
CODEOWNERS must have explicit write access to the repository for valid review routing.

### Recommended CODEOWNERS Pattern

```
# Default: engineering team reviews everything
* @<ORG_SLUG>/engineering

# Path-specific routing
/src/frontend/ @<ORG_SLUG>/frontend
/src/backend/  @<ORG_SLUG>/backend
/infra/        @<ORG_SLUG>/devops
/security/     @<ORG_SLUG>/security
/docs/         @<ORG_SLUG>/product @<ORG_SLUG>/design
/design/       @<ORG_SLUG>/design
```

**Operational rule:** CODEOWNERS matching is evaluated bottom-to-top and stops at the
first match, so more specific paths must be lower in the file than broad globs.

## Team Management Workflows (GitHub CLI)

### List teams

```bash
gh api "orgs/$ORG_SLUG/teams" --paginate --jq '.[] | .slug'
```

### Create top-level teams (idempotent)

Check before creating:

```bash
# Check existence
gh api "orgs/$ORG_SLUG/teams/engineering" --silent >/dev/null

# Create if absent
gh api "orgs/$ORG_SLUG/teams" -X POST \
  -f name="engineering" \
  -f privacy="closed" \
  -f description="All engineering staff"
```

### Create child team under engineering

```bash
ENGINEERING_ID="$(gh api "orgs/$ORG_SLUG/teams/engineering" --jq '.id')"
gh api "orgs/$ORG_SLUG/teams" -X POST \
  -f name="frontend" \
  -f privacy="closed" \
  -f description="Frontend developers" \
  -F parent_team_id="$ENGINEERING_ID"
```

### Grant repository access to a team

```bash
REPO_OWNER="$ORG_SLUG"
REPO_NAME="example-repo"
TEAM_SLUG="frontend"
PERMISSION="push"

gh api -X PUT "orgs/$ORG_SLUG/teams/$TEAM_SLUG/repos/$REPO_OWNER/$REPO_NAME" \
  -f permission="$PERMISSION"
```

### Remove repository from a team

```bash
gh api -X DELETE "orgs/$ORG_SLUG/teams/$TEAM_SLUG/repos/$REPO_OWNER/$REPO_NAME"
```

### Manage team membership

```bash
# Add user
TEAM_SLUG="contractors"
USERNAME="someuser"
gh api -X PUT "orgs/$ORG_SLUG/teams/$TEAM_SLUG/memberships/$USERNAME" \
  -f role="member"

# Remove user
gh api -X DELETE "orgs/$ORG_SLUG/teams/$TEAM_SLUG/memberships/$USERNAME"
```

## Audit Checklist

- [ ] Team topology exists and children correctly nested under `engineering`
- [ ] Each team has minimum necessary repository grants only
- [ ] CODEOWNERS references only teams with explicit write access
- [ ] Contractor memberships have explicit end dates and removal schedule
- [ ] No orphan teams (teams with zero members and zero repo grants)
- [ ] Admin access limited to `leadership` team only

## ORGANVM-Specific Considerations

Given the single-operator nature of ORGANVM (one human + AI agents), the team
structure above serves as a governance template for:

1. **Agent identity separation:** Different AI agents (Claude, Codex, Gemini) can be
   mapped to different team roles when GitHub Apps are introduced.
2. **Future collaborator onboarding:** The contractor team provides a minimal-access
   path for external contributors.
3. **Audit compliance:** The structure satisfies GitHub Business governance requirements
   for org-level rulesets and CODEOWNERS enforcement.
