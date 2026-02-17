# ADR-008: Essay Dating and Future-Date Correction

## Status

Accepted

## Date

2026-02-13

## Context

During the VERITAS sprint (Sprint 11), an audit of the 29 published essays at that time discovered that 9 essays had **future dates** — dates that had not yet occurred at the time the essays were published. This happened because the AI-conductor workflow sometimes assigned dates based on when content was *written or planned* rather than when it was *published*.

For a system that claims to "build in public" (ORGAN-V's core mission), publishing essays with incorrect dates undermines credibility. A reader seeing an essay dated February 16 that was actually published on February 11 would question the integrity of the entire publication record.

The problem was compounded by Jekyll's date-based URL scheme: `/_posts/YYYY-MM-DD-slug.md` → `/YYYY/MM/DD/slug/`. Changing a date means changing the URL, which breaks any existing links.

## Decision

**Policy**: An essay's date is its **publication date** — the date it was deployed to the public-process Jekyll site and became accessible via URL. Not the date it was written, planned, or drafted.

**VERITAS correction**: All 9 future-dated essays were corrected to their actual publication date. This was a one-time breaking change to URLs, accepted as necessary to establish the policy.

**Enforcement**: The `essay-deploy.py` script (created in Sprint 33 OPERATIO) deploys essays with the date embedded in the filename. The essay-monitor workflow detects new essays by scanning `_posts/` — the filename date is the publication date by construction.

**Exception**: Essays may be backdated to the same day they were written if they are published within the same calendar day. Multi-day drafting uses the publication date, not the start date.

## Consequences

### Positive

- **Credibility**: Every essay date is verifiable against git history
- **Consistency**: One rule, no ambiguity — date = publication date
- **URL stability going forward**: Once published, an essay's date (and URL) never changes
- **Automated enforcement**: The deploy pipeline sets dates at publication time

### Negative

- **9 URLs broke**: Existing links to the corrected essays became 404s. No redirect mechanism was implemented.
- **Historical inaccuracy**: Some essays were genuinely written on their original dates — the correction erased that provenance
- **Rigid policy**: If an essay is accidentally published a day early, the date cannot be corrected without breaking the URL

## References

- VERITAS sprint: `docs/specs/sprints/11-veritas.md`
- Essay deploy pipeline: `scripts/essay-deploy.py`
- Essay monitor: `essay-monitor.yml` in orchestration-start-here
- Honesty essay deployed during VERITAS as companion piece
