# ADR-003: Organ Naming Scheme and Greek Suffixes

## Status

Accepted

## Date

2026-02-09

## Context

The eight-organ system required a naming convention for GitHub organizations that would be:
1. Immediately parseable by machines (CI scripts, registry queries, templating)
2. Semantically meaningful to humans reading a repo list
3. Unique enough to avoid collision with existing GitHub org names
4. Systematically derivable from a single configuration change (for forking the entire system)

Early options included English domain names (`organvm-theory`, `organvm-art`, `organvm-commerce`), sequential numbering (`organvm-1`, `organvm-2`), and the ultimately chosen Greek ontological suffixes.

## Decision

Each organ's GitHub organization name follows the pattern `${ORGAN_PREFIX}-${roman_numeral}-${greek_suffix}`, where the Greek suffix is drawn from the organ's functional domain in classical philosophy:

| Organ | Suffix | Greek | Meaning |
|-------|--------|-------|---------|
| I | `i-theoria` | θεωρία | contemplation, theory |
| II | `ii-poiesis` | ποίησις | making, artistic creation |
| III | `iii-ergon` | ἔργον | work, deed, product |
| IV | `iv-taxis` | τάξις | arrangement, order, governance |
| V | `v-logos` | λόγος | word, speech, reason |
| VI | `vi-koinonia` | κοινωνία | communion, fellowship |
| VII | `vii-kerygma` | κήρυγμα | proclamation, announcement |
| Meta | `meta-organvm` | μετά | beyond, about, self-referential |

The naming scheme is **env-var-driven** for templating:
- `.config/organvm.env` provides shell-sourceable defaults
- `.config/organvm.env.local` (gitignored) contains instance-specific overrides
- `.config/organvm.config.json` provides machine-readable mappings

Changing `ORGAN_PREFIX` in one place derives all 8 org names automatically.

## Consequences

### Positive

- Roman numerals encode the dependency hierarchy (I→II→III) directly in the name
- Greek suffixes communicate organ purpose to anyone reading a GitHub org list
- Env-var templating means the entire naming scheme can be forked by changing one variable
- No collision risk — `organvm-i-theoria` is unique on GitHub
- Org names double as documentation — the suffix teaches the reader what the organ does

### Negative

- Greek names are less accessible to non-English/non-European readers
- Longer org names make CLI commands more verbose (`gh repo list organvm-ii-poiesis`)
- The Roman numeral embedding creates a perceived hierarchy that may not always apply (ORGAN-VII is not "less important" than ORGAN-I)
- Requires explanation in onboarding docs — not self-evident to newcomers

## References

- Configuration: `.config/organvm.env`, `.config/organvm.config.json`
- Repository standards: `docs/standards/10-repository-standards.md`
- Phase -1 implementation: Sprint 01 IGNITION (`docs/specs/sprints/01-ignition.md`)
