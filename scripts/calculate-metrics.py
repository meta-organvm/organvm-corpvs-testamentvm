#!/usr/bin/env python3
"""Calculate system-wide metrics from registry-v2.json, sprint specs, and essays.

Computes all derivable metrics and writes system-metrics.json.
The 'manual' section is preserved across runs — edit it by hand for
values that can't be auto-computed (word counts, code file counts, etc.).

Usage:
    python3 scripts/calculate-metrics.py
    python3 scripts/calculate-metrics.py --registry registry-v2.json --output system-metrics.json
    python3 scripts/calculate-metrics.py --skip-essays   # offline mode
"""

import argparse
import json
import os
import re
import subprocess
import sys
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DEFAULT_REGISTRY = ROOT / "registry-v2.json"
DEFAULT_OUTPUT = ROOT / "system-metrics.json"
SPRINTS_DIR = ROOT / "docs" / "specs" / "sprints"

# Organ directory mappings (mirrors organ_config.py for standalone use)
ORGAN_DIRS = {
    "ORGAN-I": "organvm-i-theoria",
    "ORGAN-II": "organvm-ii-poiesis",
    "ORGAN-III": "organvm-iii-ergon",
    "ORGAN-IV": "organvm-iv-taxis",
    "ORGAN-V": "organvm-v-logos",
    "ORGAN-VI": "organvm-vi-koinonia",
    "ORGAN-VII": "organvm-vii-kerygma",
    "META-ORGANVM": "meta-organvm",
    "PERSONAL": "4444J99",
}


def compute_registry_metrics(registry: dict) -> dict:
    """Derive all metrics from registry-v2.json."""
    organs = registry.get("organs", {})
    all_repos = []
    per_organ = {}

    for organ_key, organ_data in organs.items():
        repos = organ_data.get("repositories", [])
        all_repos.extend(repos)
        per_organ[organ_key] = {
            "name": organ_data.get("name", organ_key),
            "repos": len(repos),
        }

    status_dist = defaultdict(int)
    ci_count = 0
    dep_count = 0

    for repo in all_repos:
        status_dist[repo.get("implementation_status", "UNKNOWN")] += 1
        if repo.get("ci_workflow"):
            ci_count += 1
        dep_count += len(repo.get("dependencies", []))

    operational = sum(
        1 for o in organs.values()
        if o.get("launch_status") == "OPERATIONAL"
    )

    return {
        "total_repos": len(all_repos),
        "active_repos": status_dist.get("ACTIVE", 0),
        "archived_repos": status_dist.get("ARCHIVED", 0),
        "total_organs": len(organs),
        "operational_organs": operational,
        "ci_workflows": ci_count,
        "dependency_edges": dep_count,
        "per_organ": per_organ,
        "implementation_status": dict(sorted(status_dist.items())),
    }


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


def _strip_frontmatter(text: str) -> str:
    """Strip YAML frontmatter from markdown text."""
    if text.startswith("---"):
        end = text.find("---", 3)
        if end != -1:
            text = text[end + 3:]
    return text


def _count_file_words(path: Path) -> int:
    """Count words in a file, stripping frontmatter and HTML tags."""
    try:
        text = path.read_text(errors="replace")
    except OSError:
        return 0
    text = _strip_frontmatter(text)
    text = re.sub(r"<[^>]+>", " ", text)
    return len(text.split())


def count_words_local(workspace: Path) -> dict:
    """Count words across the workspace by walking the filesystem."""
    readme_words = 0
    for organ_dir_name in ORGAN_DIRS.values():
        organ_dir = workspace / organ_dir_name
        if not organ_dir.is_dir():
            continue
        for entry in sorted(organ_dir.iterdir()):
            if not entry.is_dir():
                continue
            readme = entry / "README.md"
            if readme.is_file():
                readme_words += _count_file_words(readme)

    essay_words = 0
    essays_dir = workspace / "organvm-v-logos" / "public-process" / "_posts"
    if essays_dir.is_dir():
        for md in sorted(essays_dir.glob("*.md")):
            essay_words += _count_file_words(md)

    corpus_words = 0
    corpus_dir = workspace / "meta-organvm" / "organvm-corpvs-testamentvm" / "docs"
    if corpus_dir.is_dir():
        for md in sorted(corpus_dir.rglob("*.md")):
            corpus_words += _count_file_words(md)

    profile_words = 0
    for organ_dir_name in ORGAN_DIRS.values():
        profile = workspace / organ_dir_name / ".github" / "profile" / "README.md"
        if profile.is_file():
            profile_words += _count_file_words(profile)

    total = readme_words + essay_words + corpus_words + profile_words
    return {
        "readmes": readme_words,
        "essays": essay_words,
        "corpus": corpus_words,
        "org_profiles": profile_words,
        "total": total,
    }


def format_word_count(total: int) -> tuple[str, int, str]:
    """Format word count into display strings."""
    return f"~{total:,}+", total, f"{total // 1000}K+"


def load_manual_section(output_path: Path) -> dict:
    """Load the manual section from the existing metrics file, if any."""
    default_manual = {
        "_note": "Edit these by hand. calculate-metrics.py preserves this section.",
        "total_words": "~404,000+",
        "total_words_numeric": 404000,
        "total_words_short": "404K+",
        "code_files": 3586,
        "test_files": 736,
        "repos_with_tests": 56,
    }

    if not output_path.exists():
        return default_manual

    try:
        with open(output_path) as f:
            existing = json.load(f)
        return existing.get("manual", default_manual)
    except (json.JSONDecodeError, KeyError):
        return default_manual


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


def main():
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

    # Compute metrics from three sources
    reg_metrics = compute_registry_metrics(registry)
    sprint_count, sprint_names = count_sprint_specs(SPRINTS_DIR)
    essay_count = fetch_essay_count(skip=args.skip_essays)

    if essay_count == -1:
        essay_count = load_existing_essay_count(output_path)
        print(f"  Using existing essay count: {essay_count}")

    # Word counting
    word_counts = None
    if not args.skip_words:
        workspace_raw = args.workspace or os.environ.get("ORGANVM_WORKSPACE_DIR")
        if workspace_raw:
            workspace = Path(workspace_raw).expanduser().resolve()
        else:
            workspace = Path.home() / "Workspace"

        if workspace.is_dir():
            word_counts = count_words_local(workspace)
            tw, tw_num, tw_short = format_word_count(word_counts["total"])
        else:
            print(f"  WARNING: Workspace {workspace} not found, skipping word count",
                  file=sys.stderr)

    # Load manual section (preserved across runs)
    manual = load_manual_section(output_path)

    # Migrate word count fields from manual when auto-computed
    if word_counts is not None:
        for key in ("total_words", "total_words_numeric", "total_words_short"):
            manual.pop(key, None)

    # Build computed section
    computed = {
        **reg_metrics,
        "published_essays": essay_count,
        "sprints_completed": sprint_count,
        "sprint_names": sprint_names,
    }

    if word_counts is not None:
        computed["word_counts"] = word_counts
        tw, tw_num, tw_short = format_word_count(word_counts["total"])
        computed["total_words"] = tw
        computed["total_words_numeric"] = tw_num
        computed["total_words_short"] = tw_short

    # Assemble output
    metrics = {
        "schema_version": "1.0",
        "generated": datetime.now(timezone.utc).isoformat(),
        "computed": computed,
        "manual": manual,
    }

    with open(output_path, "w") as f:
        json.dump(metrics, f, indent=2)
        f.write("\n")

    # Summary
    c = metrics["computed"]
    print(f"Metrics written to {output_path}")
    print(f"  Repos: {c['total_repos']} ({c['active_repos']} ACTIVE, {c['archived_repos']} ARCHIVED)")
    print(f"  Organs: {c['operational_organs']}/{c['total_organs']} operational")
    print(f"  CI: {c['ci_workflows']}")
    print(f"  Dependencies: {c['dependency_edges']} edges")
    print(f"  Essays: {c['published_essays']}")
    print(f"  Sprints: {c['sprints_completed']}")
    if word_counts is not None:
        wc = word_counts
        print(f"  Words: {tw_short} (readmes={wc['readmes']:,}, essays={wc['essays']:,}, "
              f"corpus={wc['corpus']:,}, profiles={wc['org_profiles']:,})")


if __name__ == "__main__":
    main()
