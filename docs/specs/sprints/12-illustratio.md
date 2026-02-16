# Sprint 12: ILLUSTRATIO — Portfolio CMYK Redesign and Billing Remediation

**Date:** 2026-02-14
**Status:** COMPLETE
**Duration:** ~6 hours
**Category:** Portfolio & Presentation

## Objective
Redesign the portfolio site with a distinctive visual identity and resolve the GitHub Actions billing overrun on organvm-i-theoria (48,880 minutes).

## Delivered
- CMYK color scheme deployed (Jost font + cyan/magenta/yellow)
- p5.js generative sketches added to 9 portfolio pages
- Puter.js LLM consultation page created
- 17 cron workflows disabled across ORGAN-I (14) and ORGAN-III (3)
- Stale portfolio data fixed

## Key Decisions
- Chose CMYK color scheme (print-inspired, distinctive from typical tech portfolios)
- Used p5.js for generative visuals on every page rather than static illustrations
- Disabled cron workflows rather than upgrading the billing plan

## Metrics Delta
- Portfolio pages with p5.js: 0 → 9
- Cron workflows disabled: 0 → 17
- Estimated billing minutes saved: ~16,000+/month

## Lessons
GitHub Actions billing spirals quickly with cron workflows across many repos (14 crons x 19 repos). Astro frontmatter follows ESM rules: `import` statements must precede all executable code — import order causes subtle build failures.
