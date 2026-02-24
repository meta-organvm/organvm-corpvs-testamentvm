#!/usr/bin/env python3
"""Calculate system-wide metrics from registry-v2.json, sprint specs, and essays.

Thin wrapper around organvm_engine.metrics.calculator — delegates core computation
to the engine while adding corpus-specific features (sprint counts, essay API, etc.).

Usage:
    python3 scripts/calculate-metrics.py
    python3 scripts/calculate-metrics.py --registry registry-v2.json --output system-metrics.json
    python3 scripts/calculate-metrics.py --skip-essays   # offline mode
"""

import argparse
import json
import os
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

from organvm_engine.metrics.calculator import (
    compute_metrics,
    count_words,
    format_word_count,
    write_metrics,
)

ROOT = Path(__file__).resolve().parent.parent
DEFAULT_REGISTRY = ROOT / "registry-v2.json"
DEFAULT_OUTPUT = ROOT / "system-metrics.json"
SPRINTS_DIR = ROOT / "docs" / "specs" / "sprints"


def count_sprint_specs(sprints_dir: Path) -> tuple[int, list[str]]:
    """Count .md files in specs/sprints/ and return sorted names."""
    if not sprints_dir.is_dir():
        return 0, []
    specs = sorted(f.stem for f in sprints_dir.glob("*.md"))
    return len(specs), specs


def fetch_essay_count(skip: bool = False) -> int:
    """Get essay count from public-process _posts/ via gh API."""
    if skip:
        return -1  # sentinel: caller should preserve existing value

    try:
        result = subprocess.run(
            ["gh", "api",
             "repos/organvm-v-logos/public-process/git/trees/HEAD?recursive=1",
             "--jq", '[.tree[] | select(.path | startswith("_posts/"))] | length'],
            capture_output=True, text=True, timeout=15,
        )
        if result.returncode == 0 and result.stdout.strip().isdigit():
            return int(result.stdout.strip())
    except (subprocess.TimeoutExpired, FileNotFoundError):
        pass

    print("  WARNING: Could not fetch essay count from GitHub API", file=sys.stderr)
    return -1


def load_existing_essay_count(output_path: Path) -> int:
    """Fallback: read essay count from existing metrics if API was skipped."""
    if not output_path.exists():
        return 29  # known good default

    try:
        with open(output_path) as f:
            existing = json.load(f)
        return existing.get("computed", {}).get("published_essays", 29)
    except (json.JSONDecodeError, KeyError):
        return 29


def main() -> None:
    parser = argparse.ArgumentParser(description="Calculate system metrics")
    parser.add_argument("--registry", default=str(DEFAULT_REGISTRY),
                        help="Path to registry-v2.json")
    parser.add_argument("--output", default=str(DEFAULT_OUTPUT),
                        help="Path for JSON metrics output")
    parser.add_argument("--skip-essays", action="store_true",
                        help="Skip GitHub API call for essay count")
    parser.add_argument("--workspace", default=None,
                        help="Workspace root for word counting (default: ~/Workspace)")
    parser.add_argument("--skip-words", action="store_true",
                        help="Skip word counting")
    args = parser.parse_args()

    registry_path = Path(args.registry)
    output_path = Path(args.output)

    # Load registry
    with open(registry_path) as f:
        registry = json.load(f)

    # Core metrics from engine
    workspace_raw = args.workspace or os.environ.get("ORGANVM_WORKSPACE_DIR")
    workspace = (
        Path(workspace_raw).expanduser().resolve() if workspace_raw
        else Path.home() / "Workspace"
    )

    workspace_arg = workspace if (not args.skip_words and workspace.is_dir()) else None
    computed = compute_metrics(registry, workspace=workspace_arg)

    # Corpus-specific: sprint specs
    sprint_count, sprint_names = count_sprint_specs(SPRINTS_DIR)
    computed["sprints_completed"] = sprint_count
    computed["sprint_names"] = sprint_names

    # Corpus-specific: essay count via GitHub API
    essay_count = fetch_essay_count(skip=args.skip_essays)
    if essay_count == -1:
        essay_count = load_existing_essay_count(output_path)
        print(f"  Using existing essay count: {essay_count}")
    computed["published_essays"] = essay_count

    # Write via engine
    write_metrics(computed, output_path)

    # Summary
    c = computed
    print(f"Metrics written to {output_path}")
    print(f"  Repos: {c['total_repos']} ({c['active_repos']} ACTIVE)")
    print(f"  Organs: {c['operational_organs']}/{c['total_organs']} operational")
    print(f"  CI: {c['ci_workflows']}")
    print(f"  Dependencies: {c['dependency_edges']} edges")
    print(f"  Essays: {c.get('published_essays', '?')}")
    print(f"  Sprints: {c.get('sprints_completed', '?')}")
    if "word_counts" in c:
        wc = c["word_counts"]
        tw, tw_num, tw_short = format_word_count(wc["total"])
        print(f"  Words: {tw_short} (readmes={wc['readmes']:,}, essays={wc['essays']:,}, "
              f"corpus={wc['corpus']:,}, profiles={wc['org_profiles']:,})")


if __name__ == "__main__":
    main()
