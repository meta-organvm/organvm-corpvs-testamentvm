# Autonomous Systems Setup Guide

**Created:** 2026-02-17
**Sprint:** AUTOMATA (#29)
**Purpose:** One-time human setup to enable fully autonomous operation

---

## Overview

The AUTOMATA sprint built the autonomous pipeline:

```
Content Generation → Distribution → Social Presence → Health Monitoring
       ↑                                                       |
       └── System Pulse (metrics, soak test) ←─────────────────┘
```

This pipeline requires one-time secret configuration to activate. Once configured, the system operates without human intervention.

## Prerequisites

- GitHub CLI (`gh`) authenticated with org admin access
- Access to 1Password for org-wide tokens

## 1. CROSS_ORG_TOKEN (Required — may already exist)

**Where:** `organvm-iv-taxis/orchestration-start-here` repo secrets
**Used by:** essay-monitor, distribute-content, soak-test-daily, system-pulse-weekly, metrics-refresh

This token enables cross-org GitHub API calls. It may already be configured from the SYNCHRONIUM sprint.

```bash
# Verify it exists
gh secret list --repo organvm-iv-taxis/orchestration-start-here | grep CROSS_ORG_TOKEN

# If missing, set from your gh auth token
gh secret set CROSS_ORG_TOKEN \
  --repo organvm-iv-taxis/orchestration-start-here \
  --body "$(gh auth token)"
```

Also needed in corpvs-testamentvm for soak test and metrics workflows:

```bash
gh secret set CROSS_ORG_TOKEN \
  --repo meta-organvm/organvm-corpvs-testamentvm \
  --body "$(gh auth token)"
```

## 2. Mastodon (Social Distribution)

**Where:** `organvm-iv-taxis/orchestration-start-here` repo secrets
**Used by:** distribute-content.yml

### Steps

1. Create a Mastodon account at [mastodon.social](https://mastodon.social) (or your preferred instance)
2. Go to **Preferences → Development → New Application**
3. Name: `organvm-distributor`
4. Scopes: `write:statuses`
5. Save and copy the **Access Token**

```bash
gh secret set MASTODON_TOKEN \
  --repo organvm-iv-taxis/orchestration-start-here \
  --body "YOUR_ACCESS_TOKEN"

# Optional: set instance if not mastodon.social
gh variable set MASTODON_INSTANCE \
  --repo organvm-iv-taxis/orchestration-start-here \
  --body "https://mastodon.social"
```

## 3. Discord (Notifications)

**Where:** `organvm-iv-taxis/orchestration-start-here` repo secrets
**Used by:** distribute-content.yml

### Steps

1. Create a Discord server (or use existing)
2. Go to **Server Settings → Integrations → Webhooks → New Webhook**
3. Name: `organvm-updates`
4. Choose the channel for updates
5. Copy the **Webhook URL**

```bash
gh secret set DISCORD_WEBHOOK \
  --repo organvm-iv-taxis/orchestration-start-here \
  --body "https://discord.com/api/webhooks/YOUR_WEBHOOK_URL"
```

## 4. Render Deploy Hook (Auto-Deploy)

**Where:** `organvm-iii-ergon/life-my--midst--in` repo secrets
**Used by:** auto-deploy.yml

### Steps

1. Log into [Render Dashboard](https://dashboard.render.com)
2. Navigate to the life-my--midst--in service
3. Go to **Settings → Deploy Hook**
4. Copy the deploy hook URL

```bash
gh secret set RENDER_DEPLOY_HOOK \
  --repo organvm-iii-ergon/life-my--midst--in \
  --body "https://api.render.com/deploy/srv-xxx?key=yyy"
```

## 5. LinkedIn (Optional — Social Distribution)

**Where:** `organvm-iv-taxis/orchestration-start-here` repo secrets
**Used by:** distribute-content.yml

### Steps

1. Create a LinkedIn developer app at [linkedin.com/developers](https://www.linkedin.com/developers/)
2. Request `w_member_social` scope
3. Generate an access token (OAuth 2.0 flow)
4. Note your LinkedIn Person ID

```bash
gh secret set LINKEDIN_TOKEN \
  --repo organvm-iv-taxis/orchestration-start-here \
  --body "YOUR_ACCESS_TOKEN"

gh variable set LINKEDIN_PERSON_ID \
  --repo organvm-iv-taxis/orchestration-start-here \
  --body "YOUR_PERSON_ID"
```

**Note:** LinkedIn tokens expire after 60 days. You'll need to refresh periodically or set up token rotation.

## 6. Ghost Newsletter (Optional — Email Distribution)

**Where:** `organvm-iv-taxis/orchestration-start-here` repo secrets
**Used by:** distribute-content.yml

### Steps

1. Set up a Ghost instance (self-hosted or Ghost Pro)
2. Go to **Settings → Integrations → Add Custom Integration**
3. Name: `organvm-distributor`
4. Copy the **Admin API Key** (format: `key_id:secret`)

```bash
gh secret set GHOST_ADMIN_KEY \
  --repo organvm-iv-taxis/orchestration-start-here \
  --body "KEY_ID:SECRET"

gh variable set GHOST_URL \
  --repo organvm-iv-taxis/orchestration-start-here \
  --body "https://your-ghost-site.com"
```

## Verification

After setting up secrets, verify the autonomous loop:

```bash
# 1. Trigger soak test manually
gh workflow run soak-test-daily.yml --repo meta-organvm/organvm-corpvs-testamentvm

# 2. Trigger essay monitor manually
gh workflow run "Essay Monitor" --repo organvm-iv-taxis/orchestration-start-here

# 3. Trigger metrics refresh manually
gh workflow run metrics-refresh.yml --repo meta-organvm/organvm-corpvs-testamentvm

# 4. Trigger system pulse manually
gh workflow run system-pulse-weekly.yml --repo meta-organvm/organvm-corpvs-testamentvm

# 5. Check workflow runs
gh run list --repo meta-organvm/organvm-corpvs-testamentvm --limit 5
gh run list --repo organvm-iv-taxis/orchestration-start-here --limit 5
```

## Autonomous Schedule (Once Configured)

| Time (UTC) | Workflow | Repo | Frequency |
|------------|----------|------|-----------|
| 06:00 Mon | metrics-refresh | corpvs-testamentvm | Weekly |
| 07:00 Mon | orchestrator-agent | orchestration-start-here | Weekly |
| 08:00 daily | soak-test-daily | corpvs-testamentvm | Daily |
| 09:00 daily | essay-monitor | orchestration-start-here | Daily |
| 10:00 Wed | distribution-agent | orchestration-start-here | Weekly |
| 12:00 Sun | system-pulse-weekly | corpvs-testamentvm | Weekly |
| 08:00 1st | promotion-recommender | orchestration-start-here | Monthly |
| on push | auto-deploy | life-my--midst--in | On push |

**Human involvement after setup: none.**
