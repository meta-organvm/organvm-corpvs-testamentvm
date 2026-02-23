#!/usr/bin/env python3
"""Propagate metrics from system-metrics.json into whitelisted documentation files.

Reads the canonical system-metrics.json and updates hardcoded metric values
in markdown files via pattern matching. Patterns include surrounding context
words to avoid replacing unrelated numbers.

Usage:
    python3 scripts/propagate-metrics.py                    # corpus-only (default)
    python3 scripts/propagate-metrics.py --dry-run          # preview only
    python3 scripts/propagate-metrics.py --verbose          # show every match
    python3 scripts/propagate-metrics.py --file X.md        # single file only
    python3 scripts/propagate-metrics.py --cross-repo       # all targets from manifest
    python3 scripts/propagate-metrics.py --cross-repo --dry-run  # preview cross-repo
"""

import argparse
import json
import re
import shutil
import sys
from dataclasses import dataclass, field
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
DEFAULT_METRICS = ROOT / "system-metrics.json"
DEFAULT_TARGETS = ROOT / "metrics-targets.yaml"

# ── Whitelist ────────────────────────────────────────────────
# Only these files are ever touched. Everything else is sacred.

WHITELIST_GLOBS = [
    "README.md",
    "CLAUDE.md",
    "applications/*.md",
    "applications/shared/*.md",
    "docs/applications/*.md",
    "docs/applications/cover-letters/*.md",
    "docs/essays/09-ai-conductor-methodology.md",
    "docs/operations/*.md",
]


def resolve_whitelist(root: Path) -> list[Path]:
    """Expand whitelist globs into concrete file paths."""
    files = []
    for pattern in WHITELIST_GLOBS:
        files.extend(sorted(root.glob(pattern)))
    # Deduplicate while preserving order
    seen = set()
    result = []
    for f in files:
        if f not in seen:
            seen.add(f)
            result.append(f)
    return result


def resolve_globs(root: Path, globs: list[str]) -> list[Path]:
    """Expand arbitrary glob list relative to root, deduplicated."""
    files = []
    for pattern in globs:
        files.extend(sorted(root.glob(pattern)))
    seen = set()
    result = []
    for f in files:
        if f not in seen:
            seen.add(f)
            result.append(f)
    return result


def expand_path(raw: str) -> Path:
    """Expand ~ and resolve a path string from the manifest."""
    return Path(raw).expanduser().resolve()


def load_manifest(manifest_path: Path) -> dict:
    """Load metrics-targets.yaml."""
    with open(manifest_path) as f:
        return yaml.safe_load(f)


def transform_for_portfolio(canonical: dict, portfolio_path: Path) -> dict:
    """Merge canonical metrics into the portfolio's existing schema.

    The portfolio uses a different JSON shape (registry.*, essays.total, etc.)
    than the canonical computed/manual structure. This preserves the portfolio's
    extra fields (sprint_history, engagement_baseline, etc.) while updating
    the metrics fields from canonical.
    """
    # Load existing portfolio data to preserve non-canonical fields
    if portfolio_path.exists():
        with open(portfolio_path) as f:
            portfolio = json.load(f)
    else:
        portfolio = {}

    c = canonical["computed"]

    # Update generated timestamp
    portfolio["generated"] = canonical["generated"]

    # Update registry section from canonical computed
    reg = portfolio.get("registry", {})
    reg["total_repos"] = c["total_repos"]
    reg["total_organs"] = c["total_organs"]
    reg["operational_organs"] = c["operational_organs"]
    reg["implementation_status"] = c["implementation_status"]
    reg["ci_coverage"] = c["ci_workflows"]
    reg["dependency_edges"] = c["dependency_edges"]

    # Update per-organ data
    organs = reg.get("organs", {})
    for organ_key, info in c.get("per_organ", {}).items():
        if organ_key in organs:
            organs[organ_key]["total_repos"] = info["repos"]
        else:
            organs[organ_key] = {
                "name": info["name"],
                "total_repos": info["repos"],
            }
    reg["organs"] = organs
    portfolio["registry"] = reg

    # Update essay count
    essays = portfolio.get("essays", {})
    essays["total"] = c.get("published_essays", essays.get("total", 0))
    portfolio["essays"] = essays

    return portfolio


def copy_json_targets(manifest: dict, metrics: dict, dry_run: bool) -> int:
    """Process json_copies from manifest. Returns number of copies made."""
    copies = manifest.get("json_copies", [])
    count = 0
    for entry in copies:
        dest = expand_path(entry["dest"])
        transform = entry.get("transform")
        note = entry.get("note", "")

        if transform == "portfolio":
            data = transform_for_portfolio(metrics, dest)
        else:
            data = metrics

        if dry_run:
            print(f"  [JSON COPY] → {dest}")
            if note:
                print(f"    ({note})")
        else:
            dest.parent.mkdir(parents=True, exist_ok=True)
            with open(dest, "w") as f:
                json.dump(data, f, indent=2)
                f.write("\n")
            print(f"  Copied → {dest}")

        count += 1
    return count


def resolve_cross_repo_files(manifest: dict) -> list[Path]:
    """Resolve all markdown targets from manifest into file paths."""
    all_files = []
    for target in manifest.get("markdown_targets", []):
        raw_root = target.get("root", ".")
        if raw_root == ".":
            root = ROOT
        else:
            root = expand_path(raw_root)

        whitelist = target.get("whitelist", [])
        files = resolve_globs(root, whitelist)
        all_files.extend(files)

    # Deduplicate
    seen = set()
    result = []
    for f in all_files:
        if f not in seen:
            seen.add(f)
            result.append(f)
    return result


# ── Metric Patterns ──────────────────────────────────────────
# Each entry: (metric_key, list of (regex_pattern, replacement_template))
#
# Patterns must include surrounding context to avoid false positives.
# replacement_template uses {value} for the metric value.
# Some patterns use {value_plus} for "77+" style formatting.

@dataclass
class Replacement:
    file: Path
    line_num: int
    old_text: str
    new_text: str
    metric: str
    pattern_desc: str


def build_patterns(metrics: dict) -> list[tuple[str, re.Pattern, str, str]]:
    """Build (metric_name, compiled_regex, replacement_string, description) tuples.

    Design principle: patterns include enough surrounding context to prevent
    false positives. A bare ``\\d+ repos`` would match per-organ counts and
    table cells with unrelated numbers. Instead we anchor on contextual
    phrases like 'coordinating N repositories' or 'Total repositories | N'.
    """
    c = metrics["computed"]
    m = metrics["manual"]

    total_repos = c["total_repos"]
    active_repos = c["active_repos"]
    archived_repos = c["archived_repos"]
    essays = c["published_essays"]
    dep_edges = c["dependency_edges"]
    ci_workflows = c["ci_workflows"]
    sprints = c["sprints_completed"]
    total_words_numeric = str(m.get("total_words_numeric", 386000))
    # Format: "386,000"
    total_words_formatted = f"{int(total_words_numeric):,}"
    total_words_short = m.get("total_words_short", "386K+")
    # Extract just the number part for K pattern, e.g. "386"
    total_words_k = total_words_short.rstrip("K+")

    patterns = []

    def add(name, regex, replacement, desc):
        patterns.append((name, re.compile(regex), replacement, desc))

    # ── total_repos ──
    # Only match in specific contexts that clearly refer to the system total.
    # "N repositories across" is the most common prose pattern.
    add("total_repos",
        r"(\b)\d+( repositor(?:ies|y) across\b)",
        rf"\g<1>{total_repos}\2",
        "N repositories across")

    # "coordinating N repositories" / "coordinating N repos"
    add("total_repos",
        r"(coordinating )\d+( repo)",
        rf"\g<1>{total_repos}\2",
        "coordinating N repos")

    # "Total repositories | N" in markdown tables
    add("total_repos",
        r"(Total repositories \| )\d+",
        rf"\g<1>{total_repos}",
        "Table: Total repositories | N")

    # Badge: Repos-97
    add("total_repos",
        r"(Repos-)\d+",
        rf"\g<1>{total_repos}",
        "Badge: Repos-N")

    # "N-repo system" / "N-repo"
    add("total_repos",
        r"(\b)\d+(-repo system\b)",
        rf"\g<1>{total_repos}\2",
        "N-repo system")

    add("total_repos",
        r"(\b)\d+(-repo\b)",
        rf"\g<1>{total_repos}\2",
        "N-repo")

    # "across N repos" / "across N repositories"
    add("total_repos",
        r"(across )\d+( repo)",
        rf"\g<1>{total_repos}\2",
        "across N repos")

    # "organize N repositories" / "validate N repositories"
    add("total_repos",
        r"(organize )\d+( repositor)",
        rf"\g<1>{total_repos}\2",
        "organize N repositories")

    add("total_repos",
        r"(validate )\d+( repositor)",
        rf"\g<1>{total_repos}\2",
        "validate N repositories")

    # "checks across N repos" / "monitoring across N repos"
    add("total_repos",
        r"(across all )\d+( repos?\b)",
        rf"\g<1>{total_repos}\2",
        "across all N repos")

    # "N documented repositories"
    add("total_repos",
        r"(\b)\d+( documented repositor)",
        rf"\g<1>{total_repos}\2",
        "N documented repositories")

    # "N repository READMEs"
    add("total_repos",
        r"(\b)\d+( repository READMEs)",
        rf"\g<1>{total_repos}\2",
        "N repository READMEs")

    # ── active_repos ──
    add("active_repos",
        r"(\b)\d+( ACTIVE\b)",
        rf"\g<1>{active_repos}\2",
        "N ACTIVE")

    add("active_repos",
        r"(Active status \| )\d+",
        rf"\g<1>{active_repos}",
        "Table: Active status | N")

    add("active_repos",
        r"(\b)\d+( active repos?,)",
        rf"\g<1>{active_repos}\2",
        "N active repos,")

    add("active_repos",
        r"(\b)\d+( production-grade\b)",
        rf"\g<1>{active_repos}\2",
        "N production-grade")

    add("active_repos",
        r"(Production status \| )\d+",
        rf"\g<1>{active_repos}",
        "Table: Production status | N")

    # ── archived_repos ──
    add("archived_repos",
        r"(\b)\d+( ARCHIVED\b)",
        rf"\g<1>{archived_repos}\2",
        "N ARCHIVED")

    add("archived_repos",
        r"(Archived \| )\d+",
        rf"\g<1>{archived_repos}",
        "Table: Archived | N")

    # ── published_essays ──
    add("published_essays",
        r"(\b)\d+(\+? published essays?\b)",
        rf"\g<1>{essays}\2",
        "N published essays")

    add("published_essays",
        r"(\b)\d+(\+? meta-system essays?\b)",
        rf"\g<1>{essays}\2",
        "N meta-system essays")

    add("published_essays",
        r"(Published essays? \| )\d+",
        rf"\g<1>{essays}",
        "Table: Published essays | N")

    add("published_essays",
        r"(\b)\d+( essays explaining\b)",
        rf"\g<1>{essays}\2",
        "N essays explaining")

    add("published_essays",
        r"(\b)\d+( essays documenting\b)",
        rf"\g<1>{essays}\2",
        "N essays documenting")

    # ── dependency_edges ──
    add("dependency_edges",
        r"(\b)\d+( dependency edges?\b)",
        rf"\g<1>{dep_edges}\2",
        "N dependency edges")

    add("dependency_edges",
        r"(\b)\d+( tracked dependency\b)",
        rf"\g<1>{dep_edges}\2",
        "N tracked dependency")

    add("dependency_edges",
        r"(Dependency edges? \| )\d+",
        rf"\g<1>{dep_edges}",
        "Table: Dependency edges | N")

    add("dependency_edges",
        r"(\b)\d+( registry dependency edges?\b)",
        rf"\g<1>{dep_edges}\2",
        "N registry dependency edges")

    # ── ci_workflows ──
    # Only match "70+" / "77+" / "82+" style CI counts, not "5 CI/CD" (which
    # refers to 5 specific workflow files in the spec, not total system count).
    add("ci_workflows",
        r"(\b)\d+(\+ CI/CD workflows?\b)",
        rf"\g<1>{ci_workflows}\2",
        "N+ CI/CD workflows")

    add("ci_workflows",
        r"(CI/CD workflows? \| )\d+\+?",
        rf"\g<1>{ci_workflows}+",
        "Table: CI/CD workflows | N+")

    add("ci_workflows",
        r"(\b)\d+(\+ CI workflows?\b)",
        rf"\g<1>{ci_workflows}\2",
        "N+ CI workflows")

    add("ci_workflows",
        r"(\b)\d+(\+ CI/CD pipelines?\b)",
        rf"\g<1>{ci_workflows}\2",
        "N+ CI/CD pipelines")

    # ── sprints_completed ──
    add("sprints_completed",
        r"(\b)\d+( sprints completed\b)",
        rf"\g<1>{sprints}\2",
        "N sprints completed")

    add("sprints_completed",
        r"(Sprints completed \| )\d+",
        rf"\g<1>{sprints}",
        "Table: Sprints completed | N")

    # ── total_words (manual) ──
    # Only match system-level word counts (300K+ range), not essay/question
    # word counts which are in the hundreds or low thousands.
    # "~386,000+ words" — the tilde + 6-digit number pattern
    add("total_words",
        r"~\d{3},\d{3}\+?( words)",
        rf"~{total_words_formatted}+\1",
        "~NNN,NNN+ words")

    # "386,000 words" without tilde (bare, 6-digit)
    add("total_words",
        r"(?<!~)\b\d{3},\d{3}\+?( words)",
        rf"{total_words_formatted}+\1",
        "NNN,NNN words (bare)")

    # "386K+ words" / "~386K+ words" in prose
    add("total_words",
        r"~?\d{3}K\+?( words)",
        rf"~{total_words_short}\1",
        "~NNNK+ words")

    # Badge: Docs-~386K%2B%20words
    add("total_words",
        r"(Docs-)~?\d{3}K%2B(%20words)",
        rf"\g<1>~{total_words_k}K%2B\2",
        "Badge: Docs-~NNNK%2B words")

    # "| Documentation | ~386,000+ words |" table pattern
    add("total_words",
        r"(Documentation \| )~?\d{3},?\d{3}\+?( words)",
        rf"\g<1>~{total_words_formatted}+\2",
        "Table: Documentation | ~NNN,NNN+ words")

    return patterns


# ── Lines to skip ────────────────────────────────────────────
# Some lines in whitelisted files should not be updated because they
# describe historical state at a specific point in time.

SKIP_MARKERS = [
    # ── Historical sprint descriptions (README.md) ──
    "Sprint (",         # "Gap-Fill Sprint (2026-02-11):" — historical
    "Phase 1 (",        # "Phase 1 (2026-02-10):" — historical
    "Phase 2 (",        # "Phase 2 (2026-02-10):" — historical
    "Phase 3 (",        # "Phase 3 (2026-02-10):" — historical
    "Launch (",         # "Launch (2026-02-11):" — historical
    "Silver Sprint:",
    "Bronze Sprint",
    "Gold Sprint",
    "Platinum Sprint",
    "Previous:",        # "Previous: PRAXIS, CONVERGENCE, ..."
    "Pre-PRAXIS",       # historical baseline references
    "was pre-existing",
    # ── Dated lines that are point-in-time snapshots ──
    "Sprint (2026-02",  # "Exodus Sprint (2026-02-12):" etc.
    "**Phase",          # "**Phase 1 (2026-02-10):**" in README
    "**Launch",         # "**Launch (2026-02-11):**" in README
    # ── Before/after tables ──
    "| Total documentation |",  # has before|after columns in README
    "| Meta-system essays |",   # has before|after columns in README
    # ── TE budget tables (CLAUDE.md) ──
    "Per-Task TE",
    "README REWRITE",
    "README REVISE",
    "README POPULATE",
    "README EVALUATE",
    "README ARCHIVE",
    "Phase Budgets",
    # ── Specific workflow references (not system-wide CI counts) ──
    "5 CI/CD workflow specifications",  # CLAUDE.md line about github-actions-spec.md
    "5 governance",     # "5 governance automations" — specific count, not CI total
    # ── Historical dates embedded in sprint history sections ──
    "**Ignition Sprint",
    "**Propulsion Sprint",
    "**Ascension Sprint",
    "**Exodus Sprint",
    "**Perfection Sprint",
    "**Autonomy Sprint",
    "**Genesis Sprint",
    "**Alchemia Sprint",
    "**Convergence Sprint",
    "**Praxis Sprint",
    "**Veritas Sprint",
    "**Manifestatio Sprint",
    "**Illustratio Sprint",
    "**Synchronium Sprint",
    "**Concordia Sprint",
    "**Tripartitum Sprint",
    "**Submissio Sprint",
    "**Gap-Fill Sprint",
    # ── Essay-specific word counts (not system totals) ──
    "~4,500 words",     # essay draft word count
    "~170 words",       # question word count
    "~190 words",       # question word count
    "~85 words",        # question word count
    "(~111,000 words)", # essay corpus word count (subset)
    "(~111K words)",    # essay corpus word count (subset)
    "(~84K words)",     # essay corpus word count (subset)
    "(~129,000 words)", # essay corpus word count (subset, updated SENSORIA)
    "published essays", # essay count lines often have subset word counts
    "~202,000 words",   # Silver Sprint historical count
    "~270,000 words",   # historical total before current
    "(~84K words)",     # historical essay word count
    # ── Table rows with before/after columns ──
    "| ~270,000",       # before column in README table
    # ── Emergency procedures (specific operational counts, not system totals) ──
    ">5 repos",         # severity threshold, not system count
    "across 19 repos",  # ORGAN-I specific count
    "20 repos =",       # formula in prevention note
    "num_repos",        # formula variable
    # ── ai-conductor essay (specific sprint word counts, not system totals) ──
    "~202,000 words of README",  # Silver Sprint output count
    # ── Concordance sprint history table (point-in-time records) ──
    "| COMPLETED |",    # Sprint history rows contain historical metric snapshots
]


def should_skip_line(line: str) -> bool:
    """Check if a line contains historical context that should not be updated."""
    for marker in SKIP_MARKERS:
        if marker in line:
            return True
    return False


# ── Core propagation ─────────────────────────────────────────

def update_file(filepath: Path, patterns, dry_run: bool, verbose: bool) -> list[Replacement]:
    """Apply metric patterns to a single file. Returns list of replacements."""
    replacements = []
    lines = filepath.read_text().splitlines(keepends=True)
    new_lines = []
    changed = False

    for i, line in enumerate(lines, 1):
        if should_skip_line(line):
            new_lines.append(line)
            continue

        new_line = line
        for metric_name, pattern, replacement, desc in patterns:
            match = pattern.search(new_line)
            if match:
                candidate = pattern.sub(replacement, new_line)
                if candidate != new_line:
                    replacements.append(Replacement(
                        file=filepath,
                        line_num=i,
                        old_text=new_line.rstrip('\n'),
                        new_text=candidate.rstrip('\n'),
                        metric=metric_name,
                        pattern_desc=desc,
                    ))
                    new_line = candidate
                    changed = True

        new_lines.append(new_line)

    if changed and not dry_run:
        filepath.write_text("".join(new_lines))

    return replacements


def _display_path(filepath: Path) -> str:
    """Show a file path relative to ROOT if inside it, else relative to home."""
    try:
        return str(filepath.relative_to(ROOT))
    except ValueError:
        try:
            return "~/" + str(filepath.relative_to(Path.home()))
        except ValueError:
            return str(filepath)


def print_summary(all_replacements: list[Replacement], verbose: bool):
    """Print grouped-by-file change report."""
    if not all_replacements:
        print("\nNo changes needed — all files are current.")
        return

    # Group by file
    by_file: dict[Path, list[Replacement]] = {}
    for r in all_replacements:
        by_file.setdefault(r.file, []).append(r)

    # Group by metric
    by_metric: dict[str, int] = {}
    for r in all_replacements:
        by_metric[r.metric] = by_metric.get(r.metric, 0) + 1

    print(f"\n{'─' * 60}")
    print(f"  {len(all_replacements)} replacement(s) across {len(by_file)} file(s)")
    print(f"{'─' * 60}")

    for filepath, reps in sorted(by_file.items()):
        rel = _display_path(filepath)
        print(f"\n  {rel} ({len(reps)} change{'s' if len(reps) != 1 else ''})")
        for r in reps:
            if verbose:
                print(f"    L{r.line_num} [{r.metric}] {r.pattern_desc}")
                print(f"      - {r.old_text.strip()[:100]}")
                print(f"      + {r.new_text.strip()[:100]}")
            else:
                print(f"    L{r.line_num}: {r.metric} ({r.pattern_desc})")

    print(f"\n  By metric:")
    for metric, count in sorted(by_metric.items()):
        print(f"    {metric}: {count}")


def main():
    parser = argparse.ArgumentParser(description="Propagate metrics to documentation")
    parser.add_argument("--metrics", default=str(DEFAULT_METRICS),
                        help="Path to system-metrics.json")
    parser.add_argument("--dry-run", action="store_true",
                        help="Preview changes without writing")
    parser.add_argument("--verbose", action="store_true",
                        help="Show old/new text for every match")
    parser.add_argument("--file", type=str, default=None,
                        help="Process only this file (relative to repo root)")
    parser.add_argument("--cross-repo", action="store_true",
                        help="Read metrics-targets.yaml and propagate to all registered consumers")
    parser.add_argument("--targets", default=None,
                        help="Path to metrics-targets.yaml (default: repo root)")
    args = parser.parse_args()

    # Load metrics
    metrics_path = Path(args.metrics)
    if not metrics_path.exists():
        print(f"ERROR: {metrics_path} not found. Run calculate-metrics.py first.",
              file=sys.stderr)
        sys.exit(1)

    with open(metrics_path) as f:
        metrics = json.load(f)

    if "computed" not in metrics:
        print(f"ERROR: {metrics_path} missing 'computed' section. Wrong schema?",
              file=sys.stderr)
        sys.exit(1)

    # Build patterns
    patterns = build_patterns(metrics)

    # ── Cross-repo mode ──
    if args.cross_repo:
        manifest_path = Path(args.targets) if args.targets else DEFAULT_TARGETS
        if not manifest_path.exists():
            print(f"ERROR: {manifest_path} not found.", file=sys.stderr)
            sys.exit(1)

        manifest = load_manifest(manifest_path)
        mode = "DRY RUN (cross-repo)" if args.dry_run else "PROPAGATING (cross-repo)"

        # 1. JSON copies
        json_count = copy_json_targets(manifest, metrics, args.dry_run)
        print(f"[{mode}] {json_count} JSON copy target(s)")

        # 2. Markdown targets from manifest
        files = resolve_cross_repo_files(manifest)
        print(f"[{mode}] {len(files)} markdown file(s), {len(patterns)} patterns")

        all_replacements = []
        for filepath in files:
            reps = update_file(filepath, patterns, args.dry_run, args.verbose)
            all_replacements.extend(reps)

        print_summary(all_replacements, args.verbose)

        if args.dry_run and all_replacements:
            print(f"\n  Run without --dry-run to apply these changes.")
        return

    # ── Single-file or corpus-only mode ──
    if args.file:
        target = ROOT / args.file
        if not target.exists():
            print(f"ERROR: {target} not found.", file=sys.stderr)
            sys.exit(1)
        files = [target]
    else:
        files = resolve_whitelist(ROOT)

    if not files:
        print("No target files found.")
        return

    mode = "DRY RUN" if args.dry_run else "PROPAGATING"
    print(f"[{mode}] {len(files)} file(s), {len(patterns)} patterns")

    # Process files
    all_replacements = []
    for filepath in files:
        reps = update_file(filepath, patterns, args.dry_run, args.verbose)
        all_replacements.extend(reps)

    print_summary(all_replacements, args.verbose)

    if args.dry_run and all_replacements:
        print(f"\n  Run without --dry-run to apply these changes.")


if __name__ == "__main__":
    main()
