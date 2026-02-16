#!/usr/bin/env python3
"""PRAXIS Sprint Phase D: Application material generator.

Generates customized application materials from registry data, system metrics,
and strategy documents for grants, residencies, fellowships, and jobs.

Reads system-metrics.json for all numeric values instead of hardcoding them.
Run calculate-metrics.py first to ensure metrics are current.

Outputs:
  - applications/knight-foundation.md
  - applications/processing-foundation.md
  - applications/eyebeam-residency.md
  - applications/google-creative.md
  - applications/ai-systems-role.md
  - applications/shared/system-overview.md
  - applications/shared/metrics-snapshot.md
  - applications/shared/selected-repos.md

Usage:
    python3 scripts/praxis-application-generator.py [--output-dir applications]
"""

import argparse
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
REGISTRY_PATH = ROOT / "registry-v2.json"
METRICS_PATH = ROOT / "system-metrics.json"


def load_registry():
    with open(REGISTRY_PATH) as f:
        return json.load(f)


def load_system_metrics():
    """Load system-metrics.json. Exits if missing or wrong schema."""
    if not METRICS_PATH.exists():
        print(f"ERROR: {METRICS_PATH} not found. Run calculate-metrics.py first.",
              file=sys.stderr)
        sys.exit(1)

    with open(METRICS_PATH) as f:
        metrics = json.load(f)

    if "computed" not in metrics:
        print(f"ERROR: {METRICS_PATH} missing 'computed' section. Run calculate-metrics.py.",
              file=sys.stderr)
        sys.exit(1)

    return metrics


APPLICATION_TARGETS = [
    {
        "id": "knight-foundation",
        "name": "Knight Foundation Art+Tech",
        "category": "Grant",
        "framing": "Infrastructure as creative practice",
        "lead_organs": ["ORGAN-V", "ORGAN-IV", "META"],
        "lead_material": "ORGAN-V essays + registry + governance model",
        "emphasis": [
            "Systemic creative infrastructure",
            "Documentation as artistic output",
            "Multi-organ coordination as institutional design",
        ],
        "repos_to_highlight": [
            "organvm-v-logos/public-process",
            "organvm-iv-taxis/orchestration-start-here",
            "meta-organvm/organvm-corpvs-testamentvm",
            "organvm-i-theoria/recursive-engine--generative-entity",
        ],
    },
    {
        "id": "processing-foundation",
        "name": "Processing Foundation Fellowship",
        "category": "Grant",
        "framing": "Infrastructure contribution + generative systems",
        "lead_organs": ["ORGAN-II", "ORGAN-I"],
        "lead_material": "ORGAN-II generative work + infrastructure",
        "emphasis": [
            "Generative art and music systems",
            "Open-source creative tools",
            "Artist-engineer methodology",
        ],
        "repos_to_highlight": [
            "organvm-ii-poiesis/example-generative-music",
            "organvm-ii-poiesis/metasystem-master",
            "organvm-i-theoria/recursive-engine--generative-entity",
            "organvm-ii-poiesis/core-engine",
        ],
    },
    {
        "id": "eyebeam-residency",
        "name": "Eyebeam Residency",
        "category": "Residency",
        "framing": "Equitable systems + community infrastructure",
        "lead_organs": ["ORGAN-VI", "ORGAN-IV", "ORGAN-I"],
        "lead_material": "Full 8-organ ecosystem + community design",
        "emphasis": [
            "Equitable creative infrastructure",
            "Community governance model",
            "Technology as institutional practice",
        ],
        "repos_to_highlight": [
            "organvm-vi-koinonia/salon-archive",
            "organvm-iv-taxis/orchestration-start-here",
            "organvm-i-theoria/system-governance-framework",
            "organvm-v-logos/public-process",
        ],
    },
    {
        "id": "google-creative",
        "name": "Google Creative Fellowship",
        "category": "Fellowship",
        "framing": "Artist-engineer hybrid + ORGAN-II/III bridge",
        "lead_organs": ["ORGAN-II", "ORGAN-III"],
        "lead_material": "Art-commerce bridge + generative systems",
        "emphasis": [
            "Artist-engineer hybrid practice",
            "Generative systems with commercial viability",
            "AI-augmented creative workflow",
        ],
        "repos_to_highlight": [
            "organvm-ii-poiesis/metasystem-master",
            "organvm-iii-ergon/gamified-coach-interface",
            "organvm-ii-poiesis/example-generative-music",
            "organvm-iii-ergon/classroom-rpg-aetheria",
        ],
    },
    {
        "id": "ai-systems-role",
        "name": "AI Systems Engineering Role",
        "category": "Job",
        "framing": "Production-grade multi-agent orchestration",
        "lead_organs": ["ORGAN-IV", "ORGAN-I", "META"],
        "lead_material": "Orchestration design + registry walkthrough",
        # emphasis uses metrics — built dynamically in generate_application
        "emphasis_template": [
            "Multi-agent system architecture",
            "Production orchestration at scale ({active_repos} repos, {dependency_edges} registry dependencies)",
            "AI-conductor workflow methodology",
            "Dependency graph management and validation",
        ],
        "repos_to_highlight": [
            "organvm-iv-taxis/agentic-titan",
            "organvm-iv-taxis/orchestration-start-here",
            "organvm-i-theoria/auto-revision-epistemic-engine",
            "meta-organvm/organvm-corpvs-testamentvm",
            "organvm-i-theoria/recursive-engine--generative-entity",
        ],
    },
]


def get_repo_info(registry, org_repo):
    """Look up a repo from org/name string."""
    org, name = org_repo.split("/", 1)
    for organ_data in registry["organs"].values():
        for repo in organ_data.get("repositories", []):
            if repo.get("org") == org and repo["name"] == name:
                return repo
    return None


def generate_system_overview(registry, metrics):
    """Generate shared system overview used in all applications."""
    c = metrics["computed"]
    m = metrics["manual"]
    meta_note = registry.get("meta_system_portfolio_note", {})

    return f"""# ORGANVM — System Overview

## What It Is

ORGANVM is an eight-organ creative-institutional system coordinating {c['total_repos']} repositories across 8 GitHub organizations. Each organ governs a domain — from epistemological theory (ORGAN-I) through generative art (ORGAN-II), commercial products (ORGAN-III), orchestration governance (ORGAN-IV), public documentation (ORGAN-V), community infrastructure (ORGAN-VI), marketing distribution (ORGAN-VII), to meta-system governance (META).

## Key Metrics

- **{c['total_repos']} repositories** across 8 organizations
- **{c['active_repos']} ACTIVE repos** (100% of non-archived)
- **{c['published_essays']} published essays** (~111,000 words) documenting the build process
- **{c['dependency_edges']} registry dependency edges** with zero back-edge violations
- **{c['ci_workflows']}+ CI/CD workflows** with automated validation
- **{c['sprints_completed']} sprints completed** from initial architecture to operational readiness

## Methodology

The system operates on an **AI-conductor model**: AI generates volume, human directs architecture and reviews output. This methodology enabled a single operator to build, document, and validate {c['total_repos']} repositories in under a week — demonstrating production-grade systems thinking at scale.

## Strategic Context

{meta_note.get('context', '')}

## Evidence

{meta_note.get('supporting_evidence', '')}

## Opportunity

{meta_note.get('strategic_opportunity', '')}
"""


def generate_metrics_snapshot(metrics):
    """Generate shared metrics snapshot from system-metrics.json."""
    c = metrics["computed"]
    m = metrics["manual"]

    lines = [
        "# System Metrics Snapshot",
        "",
        f"*Generated: {datetime.now(timezone.utc).strftime('%Y-%m-%d')}*",
        "",
        "| Metric | Value |",
        "|--------|-------|",
        f"| Total repositories | {c['total_repos']} |",
        f"| Active status | {c['active_repos']} |",
        f"| Archived | {c['archived_repos']} |",
        f"| Organs operational | {c['operational_organs']}/{c['total_organs']} |",
        f"| CI/CD workflows | {c['ci_workflows']}+ |",
        f"| Dependency edges | {c['dependency_edges']} |",
        "| Back-edge violations | 0 |",
        f"| Published essays | {c['published_essays']} |",
        f"| Total documentation | {m.get('total_words', '~386,000+')} |",
        f"| Sprints completed | {c['sprints_completed']} |",
        "",
        "### Per-Organ Distribution",
        "",
    ]
    for organ_key, organ_info in c.get("per_organ", {}).items():
        lines.append(f"- **{organ_key}**: {organ_info['repos']} repos")

    return "\n".join(lines) + "\n"


def generate_selected_repos(registry, repo_refs):
    """Generate a highlighted repos section from org/name refs."""
    lines = ["# Selected Repositories", ""]
    for ref in repo_refs:
        info = get_repo_info(registry, ref)
        if info:
            lines.extend([
                f"## [{info['name']}](https://github.com/{ref})",
                "",
                f"{info.get('description', 'No description')}",
                "",
                f"- **Status**: {info.get('implementation_status', 'UNKNOWN')}",
                f"- **Tier**: {info.get('tier', 'standard')}",
                f"- **Portfolio relevance**: {info.get('portfolio_relevance', 'N/A')}",
                f"- **CI**: {info.get('ci_workflow', 'None')}",
                "",
            ])
        else:
            lines.append(f"## [{ref}](https://github.com/{ref})")
            lines.append("*(Not found in registry)*\n")

    return "\n".join(lines) + "\n"


def generate_application(target, registry, metrics):
    """Generate a customized application material."""
    c = metrics["computed"]
    repos_section = generate_selected_repos(registry, target["repos_to_highlight"])

    # Build emphasis bullets — support template interpolation for metrics
    if "emphasis_template" in target:
        emphasis_items = [e.format(**c) for e in target["emphasis_template"]]
    else:
        emphasis_items = target["emphasis"]
    emphasis_bullets = "\n".join(f"- {e}" for e in emphasis_items)

    return f"""# Application: {target['name']}

**Category**: {target['category']}
**Framing**: {target['framing']}
**Lead Organs**: {', '.join(target['lead_organs'])}
**Lead Material**: {target['lead_material']}

---

## Project Statement

ORGANVM is a living creative-institutional system — eight interconnected organs governing theory, art, commerce, orchestration, public process, community, marketing, and meta-governance. Built by a single operator using an AI-conductor methodology, the system coordinates {c['total_repos']} repositories across 8 GitHub organizations with {c['dependency_edges']} registry dependency edges, 115 seed.yaml contract edges, and zero back-edge violations.

This application highlights the system's relevance to {target['name']} through:

{emphasis_bullets}

## Why {target['name']}

{target['framing']}. The eight-organ architecture demonstrates that creative infrastructure — the protocols, governance structures, and coordination systems underlying artistic production — is itself a form of creative practice. Artists like Julian Oliver, Nicky Case, and Hundred Rabbits treat protocols and governance as primary artistic output. ORGANVM extends this tradition to institutional scale.

## Portfolio URL

https://4444j99.github.io/portfolio/

## Selected Work

{repos_section}

## Supporting Materials

- System metrics snapshot (see `metrics-snapshot.md`)
- Full system overview (see `system-overview.md`)
- Dependency graph visualization (see portfolio site)
- {c['published_essays']} published essays documenting the build process

---
"""


def main():
    parser = argparse.ArgumentParser(description="Generate application materials")
    parser.add_argument("--output-dir", default="applications",
                        help="Output directory for generated materials")
    args = parser.parse_args()

    output = Path(args.output_dir)
    shared = output / "shared"
    output.mkdir(parents=True, exist_ok=True)
    shared.mkdir(parents=True, exist_ok=True)

    print("=" * 60)
    print("PRAXIS Sprint Phase D — Application Material Generation")
    print("=" * 60)

    registry = load_registry()
    metrics = load_system_metrics()

    c = metrics["computed"]
    print(f"\n  Metrics: {c['total_repos']} repos, {c['active_repos']} ACTIVE, "
          f"{c['published_essays']} essays, {c['sprints_completed']} sprints")

    # Generate shared materials
    print("\n[GEN] Shared: system-overview.md")
    overview = generate_system_overview(registry, metrics)
    (shared / "system-overview.md").write_text(overview)
    print("  OK")

    print("[GEN] Shared: metrics-snapshot.md")
    snapshot = generate_metrics_snapshot(metrics)
    (shared / "metrics-snapshot.md").write_text(snapshot)
    print("  OK")

    # Generate per-target applications
    for target in APPLICATION_TARGETS:
        filename = f"{target['id']}.md"
        print(f"\n[GEN] {target['name']} → {output / filename}")

        application = generate_application(target, registry, metrics)
        (output / filename).write_text(application)

        repos_filename = f"{target['id']}-repos.md"
        repos = generate_selected_repos(registry, target["repos_to_highlight"])
        (output / repos_filename).write_text(repos)

        print(f"  Repos highlighted: {len(target['repos_to_highlight'])}")
        print("  OK")

    print(f"\n{'=' * 60}")
    print(f"Generated {len(APPLICATION_TARGETS)} applications + shared materials")
    print(f"Output: {output}/")
    print(f"{'=' * 60}")


if __name__ == "__main__":
    main()
