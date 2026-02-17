#!/usr/bin/env python3
"""Governance ID lookup tool — resolves short codes from concordance.md.

Parses docs/operations/concordance.md and returns context for any governance
ID across the six namespaces: TODO items, omega criteria, horizons,
anti-patterns, E2G-II findings, and sprints.

Usage:
    python3 scripts/invoke.py X1                  # lookup single ID
    python3 scripts/invoke.py X1 E3 AP-2          # lookup multiple IDs
    python3 scripts/invoke.py --namespace todo     # list all TODO items
    python3 scripts/invoke.py --namespace omega    # list all omega criteria
    python3 scripts/invoke.py --tag INCOME         # filter by constraint tag
    python3 scripts/invoke.py --tag READY          # filter by constraint tag
    python3 scripts/invoke.py --search "stranger"  # full-text search
    python3 scripts/invoke.py --list               # list namespaces and counts
"""

import argparse
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CONCORDANCE = ROOT / "docs" / "operations" / "concordance.md"

# ── Namespace detection ──────────────────────────────────────────────────

# Maps a regex pattern → namespace name
ID_PATTERNS = [
    (re.compile(r"^X\d+$", re.IGNORECASE), "todo"),
    (re.compile(r"^E\d+$", re.IGNORECASE), "todo"),
    (re.compile(r"^M\d+-II$", re.IGNORECASE), "todo"),
    (re.compile(r"^S\d+-II$", re.IGNORECASE), "todo"),
    (re.compile(r"^G\d+$", re.IGNORECASE), "todo"),
    (re.compile(r"^#?\d{1,2}$"), "omega"),
    (re.compile(r"^H[1-5]$", re.IGNORECASE), "horizon"),
    (re.compile(r"^AP-\d+$", re.IGNORECASE), "anti-pattern"),
    (re.compile(r"^(?:W|SP|BS|LC|BL|ET|LO)\d+-II$", re.IGNORECASE), "e2g-ii"),
    # Sprint: two-digit number or a sprint name (lowercase alpha)
    (re.compile(r"^\d{2}$"), "sprint"),
    (re.compile(r"^[A-Z][-A-Z]+$", re.IGNORECASE), "sprint"),
]

# Sections in concordance.md → namespace
SECTION_NAMESPACE = {
    "TODO Items": "todo",
    "P0": "todo",
    "P1": "todo",
    "P2": "todo",
    "P3": "todo",
    "Setup Guide Items": "todo",
    "Omega Criteria": "omega",
    "Horizons": "horizon",
    "Anti-Patterns": "anti-pattern",
    "E2G-II Findings": "e2g-ii",
    "Warnings (W)": "e2g-ii",
    "Shatter Points (SP)": "e2g-ii",
    "Blind Spots (BS)": "e2g-ii",
    "Latent Contradictions (LC)": "e2g-ii",
    "Bright Lines (BL)": "e2g-ii",
    "Other (ET, LO)": "e2g-ii",
    "Sprints": "sprint",
    "Cross-Reference": "xref",
}

NAMESPACE_NAMES = {
    "todo": "TODO Items",
    "omega": "Omega Criteria",
    "horizon": "Horizons",
    "anti-pattern": "Anti-Patterns",
    "e2g-ii": "E2G-II Findings",
    "sprint": "Sprints",
    "xref": "Cross-Reference: Omega ← TODO",
}


# ── Markdown table parser ────────────────────────────────────────────────


def parse_table(lines: list[str]) -> list[dict]:
    """Parse a markdown table (header + separator + rows) into list of dicts."""
    if len(lines) < 3:
        return []
    headers = [h.strip() for h in lines[0].strip().strip("|").split("|")]
    rows = []
    for line in lines[2:]:  # skip header + separator
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) == len(headers):
            rows.append(dict(zip(headers, cells)))
    return rows


def parse_concordance(path: Path) -> dict:
    """Parse concordance.md into a dict of {namespace: [entries]}."""
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()

    namespaces: dict[str, list[dict]] = {
        "todo": [],
        "omega": [],
        "horizon": [],
        "anti-pattern": [],
        "e2g-ii": [],
        "sprint": [],
        "xref": [],
    }

    current_ns = None
    table_lines: list[str] = []
    in_table = False

    for line in lines:
        # Detect section headers
        if line.startswith("## ") or line.startswith("### "):
            # Flush any pending table
            if in_table and table_lines and current_ns:
                namespaces[current_ns].extend(parse_table(table_lines))
                table_lines = []
                in_table = False

            heading = line.lstrip("#").strip()
            # Remove markdown link syntax from heading
            heading = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", heading)
            # Match heading to namespace
            for prefix, ns in SECTION_NAMESPACE.items():
                if heading.startswith(prefix):
                    current_ns = ns
                    break

        # Detect table start (line starting with |)
        if line.strip().startswith("|") and current_ns:
            if not in_table:
                in_table = True
                table_lines = []
            table_lines.append(line)
        elif in_table:
            # End of table
            if table_lines and current_ns:
                namespaces[current_ns].extend(parse_table(table_lines))
            table_lines = []
            in_table = False

    # Flush final table
    if in_table and table_lines and current_ns:
        namespaces[current_ns].extend(parse_table(table_lines))

    return namespaces


# ── ID detection ─────────────────────────────────────────────────────────


def detect_namespace(id_str: str) -> str | None:
    """Detect which namespace an ID belongs to."""
    for pattern, ns in ID_PATTERNS:
        if pattern.match(id_str):
            # Disambiguate bare numbers: 1-17 = omega, 18+ = sprint
            if ns == "omega" and not id_str.startswith("#"):
                try:
                    num = int(id_str)
                    if num > 17:
                        return "sprint"
                except ValueError:
                    pass
            return ns
    return None


def normalize_id(id_str: str) -> str:
    """Normalize an ID for matching (strip leading #, uppercase)."""
    return id_str.lstrip("#").upper()


def get_entry_id(entry: dict) -> str:
    """Extract the ID field from an entry dict (first column that looks like an ID)."""
    for key in ("ID", "#", "id"):
        if key in entry:
            return entry[key].strip()
    # Fall back to first column
    first_key = next(iter(entry), None)
    if first_key:
        return entry[first_key].strip()
    return ""


# ── Lookup ───────────────────────────────────────────────────────────────


def lookup_id(namespaces: dict, id_str: str) -> list[dict]:
    """Find all entries matching an ID across namespaces."""
    ns = detect_namespace(id_str)
    norm = normalize_id(id_str)
    results = []

    search_spaces = [namespaces[ns]] if ns and ns in namespaces else namespaces.values()

    for entries in search_spaces:
        for entry in entries:
            entry_id = get_entry_id(entry)
            entry_norm = normalize_id(entry_id)
            if entry_norm == norm:
                results.append(entry)
            # Also match sprint names (e.g., "AUTOMATA" matches sprint #29)
            elif ns == "sprint" and "Name" in entry:
                if entry["Name"].upper() == norm:
                    results.append(entry)

    return results


def filter_by_namespace(namespaces: dict, ns: str) -> list[dict]:
    """Return all entries in a given namespace."""
    ns_lower = ns.lower()
    # Allow aliases
    aliases = {
        "todos": "todo",
        "horizons": "horizon",
        "anti-patterns": "anti-pattern",
        "antipattern": "anti-pattern",
        "antipatterns": "anti-pattern",
        "e2g": "e2g-ii",
        "findings": "e2g-ii",
        "sprints": "sprint",
        "criteria": "omega",
        "cross-reference": "xref",
        "xref": "xref",
    }
    resolved = aliases.get(ns_lower, ns_lower)
    return namespaces.get(resolved, [])


def filter_by_tag(namespaces: dict, tag: str) -> list[dict]:
    """Filter TODO items by constraint tag (READY, TIME, INCOME, EXTERNAL)."""
    tag_upper = tag.upper()
    results = []
    for entry in namespaces.get("todo", []):
        constraint = entry.get("Constraint", "")
        if tag_upper in constraint.upper():
            results.append(entry)
    return results


def search_text(namespaces: dict, query: str) -> list[dict]:
    """Full-text search across all entries."""
    query_lower = query.lower()
    results = []
    for ns_name, entries in namespaces.items():
        for entry in entries:
            text = " ".join(str(v) for v in entry.values()).lower()
            if query_lower in text:
                results.append({"_namespace": ns_name, **entry})
    return results


# ── Formatting ───────────────────────────────────────────────────────────


def format_entry(entry: dict, indent: int = 0) -> str:
    """Format a single entry for display."""
    prefix = " " * indent
    lines = []
    # Filter out internal keys
    for key, value in entry.items():
        if key.startswith("_"):
            continue
        if value and value != "—":
            lines.append(f"{prefix}{key}: {value}")
    return "\n".join(lines)


def format_entries(entries: list[dict], title: str = "") -> str:
    """Format a list of entries for display."""
    if not entries:
        return "  (no results)"
    parts = []
    if title:
        parts.append(f"\n{title}")
        parts.append("─" * max(len(title), 40))
    for entry in entries:
        parts.append(format_entry(entry, indent=2))
        parts.append("")
    return "\n".join(parts)


def format_namespace_list(namespaces: dict) -> str:
    """Format the list of namespaces with counts."""
    lines = ["\nNamespaces in concordance.md:", "─" * 40]
    total = 0
    for ns, name in NAMESPACE_NAMES.items():
        count = len(namespaces.get(ns, []))
        total += count
        lines.append(f"  {ns:<15} {name:<35} {count:>3} entries")
    lines.append("─" * 40)
    lines.append(f"  {'TOTAL':<15} {'':35} {total:>3} entries")
    return "\n".join(lines)


# ── CLI ──────────────────────────────────────────────────────────────────


def main():
    parser = argparse.ArgumentParser(
        description="Governance ID lookup — resolves short codes from concordance.md",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""examples:
  %(prog)s X1                  lookup single ID
  %(prog)s X1 E3 AP-2          lookup multiple IDs
  %(prog)s --namespace todo     list all TODO items
  %(prog)s --namespace omega    list all omega criteria
  %(prog)s --tag INCOME         filter TODO items by constraint
  %(prog)s --search "stranger"  full-text search
  %(prog)s --list               list namespaces and counts""",
    )
    parser.add_argument(
        "ids",
        nargs="*",
        metavar="ID",
        help="one or more governance IDs to look up (e.g., X1, #8, AP-3, H2, W1-II, 29)",
    )
    parser.add_argument(
        "--namespace", "-n",
        metavar="NS",
        help="list all entries in a namespace (todo, omega, horizon, anti-pattern, e2g-ii, sprint, xref)",
    )
    parser.add_argument(
        "--tag", "-t",
        metavar="TAG",
        help="filter TODO items by constraint tag (READY, TIME, INCOME, EXTERNAL)",
    )
    parser.add_argument(
        "--search", "-s",
        metavar="QUERY",
        help="full-text search across all definitions",
    )
    parser.add_argument(
        "--list", "-l",
        action="store_true",
        help="list all namespaces with entry counts",
    )
    parser.add_argument(
        "--concordance",
        type=Path,
        default=CONCORDANCE,
        help=f"path to concordance.md (default: {CONCORDANCE.relative_to(ROOT)})",
    )

    args = parser.parse_args()

    if not args.concordance.exists():
        print(f"Error: concordance not found at {args.concordance}", file=sys.stderr)
        sys.exit(1)

    if not (args.ids or args.namespace or args.tag or args.search or args.list):
        parser.print_help()
        sys.exit(0)

    namespaces = parse_concordance(args.concordance)

    # --list: show namespace summary
    if args.list:
        print(format_namespace_list(namespaces))
        return

    # --namespace: show all entries in a namespace
    if args.namespace:
        entries = filter_by_namespace(namespaces, args.namespace)
        ns_label = NAMESPACE_NAMES.get(args.namespace.lower(), args.namespace)
        print(format_entries(entries, title=ns_label))
        return

    # --tag: filter TODOs by constraint
    if args.tag:
        entries = filter_by_tag(namespaces, args.tag)
        print(format_entries(entries, title=f"TODO items tagged [{args.tag.upper()}]"))
        return

    # --search: full-text search
    if args.search:
        entries = search_text(namespaces, args.search)
        print(format_entries(entries, title=f'Search results for "{args.search}"'))
        return

    # Positional IDs: look up each one
    for id_str in args.ids:
        results = lookup_id(namespaces, id_str)
        ns = detect_namespace(id_str) or "unknown"
        ns_label = NAMESPACE_NAMES.get(ns, ns)
        if results:
            print(format_entries(results, title=f"{id_str} ({ns_label})"))
        else:
            print(f"\n{id_str}: not found in concordance.md")
            print(f"  Detected namespace: {ns_label}")
            print()


if __name__ == "__main__":
    main()
