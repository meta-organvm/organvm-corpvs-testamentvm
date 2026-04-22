#!/usr/bin/env python3
"""Vacuum Radiation Engine for ORGANVM prompt-atoms.

Every completed atom is a collapse event that radiates vacuums in all directions.
This script:
  1. Scans DONE atoms for implied adjacent work
  2. Scans OPEN atoms being closed for required vacuum emissions
  3. Generates new OPEN atoms for detected vacuums
  4. Tags generated atoms with 'produced': ['vacuum-radiation']

Vacuum detection axes:
  - ADJACENT:    same domain, related capability
  - INVERSE:     opposite action (create→maintain, deploy→monitor, build→test)
  - ENABLING:    what does this completion unlock?
  - DEPENDENT:   what depends on this and is now unblocked?
  - COUNTERPART: governance pair (code→test, feature→docs, deploy→monitor)
  - CROSS-DOMAIN: implications in other universes

Usage:
    python3 vacuum_radiation.py [--dry-run] [--from-done] [--limit N]

    --from-done    Scan DONE atoms (batch mode)
    --limit N      Process only N atoms (default: all)
    --dry-run      Show what would be generated without writing
"""

from __future__ import annotations

import json
import re
import sys
from collections import Counter
from datetime import datetime
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
ATOMS_PATH = SCRIPT_DIR / "prompt-atoms.json"

TODAY = datetime.now().strftime("%Y-%m-%d")
TIMESTAMP = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# ---------------------------------------------------------------------------
# Vacuum detection patterns
# ---------------------------------------------------------------------------

# Action → counterpart actions (inverse/complementary)
COUNTERPART_MAP = {
    # create/build → test, document, monitor
    r"\b(create|build|implement|scaffold|deploy)\b": [
        ("test", "Write tests for {summary}"),
        ("document", "Document {summary}"),
        ("monitor", "Add monitoring/observability for {summary}"),
    ],
    # fix/repair → verify, prevent, regression-test
    r"\b(fix|repair|patch|resolve)\b": [
        ("verify", "Verify fix: {summary}"),
        ("prevent", "Add guard/validation to prevent recurrence: {summary}"),
        ("regression-test", "Add regression test for {summary}"),
    ],
    # research/investigate → synthesize, publish, apply
    r"\b(research|investigate|analyze|audit)\b": [
        ("synthesize", "Synthesize findings from: {summary}"),
        ("publish", "Publish/share findings from: {summary}"),
        ("apply", "Apply findings to codebase: {summary}"),
    ],
    # configure/setup → validate, document, automate
    r"\b(configure|setup|install|provision)\b": [
        ("validate", "Validate configuration: {summary}"),
        ("automate", "Automate setup process: {summary}"),
    ],
    # remove/delete/uninstall → verify, update-refs, clean-deps
    r"\b(remove|delete|uninstall|deprecate)\b": [
        ("verify-removal", "Verify complete removal: {summary}"),
        ("update-refs", "Update references after removal: {summary}"),
        ("clean-deps", "Clean orphaned dependencies after: {summary}"),
    ],
    # design/architect/plan → implement, validate-design, review
    r"\b(design|architect|plan|spec)\b": [
        ("implement", "Implement: {summary}"),
        ("validate-design", "Validate design against requirements: {summary}"),
    ],
}

# Universe → cross-domain implications
CROSS_DOMAIN_MAP = {
    "security": ["enforcement", "personal"],
    "organ-i": ["organ-ii", "meta"],
    "organ-ii": ["organ-iii", "organ-v"],
    "organ-iii": ["employment", "financial"],
    "organ-iv": ["meta", "UNIVERSAL"],
    "organ-v": ["organ-vii", "UNIVERSAL"],
    "meta": ["UNIVERSAL", "persistence"],
    "personal": ["employment", "health"],
    "employment": ["organ-iii", "personal"],
}


def generate_counterpart_vacuums(atom: dict) -> list[dict]:
    """Generate vacuum atoms from counterpart actions."""
    content = atom.get("content", "")
    summary = atom.get("summary", content[:120])
    universes = atom.get("universes", [])
    vacuums = []

    for pattern, counterparts in COUNTERPART_MAP.items():
        if re.search(pattern, content, re.I):
            for action_type, template in counterparts:
                vacuum_summary = template.format(summary=summary[:80])
                vacuums.append({
                    "type": "directive",
                    "content": vacuum_summary,
                    "summary": vacuum_summary,
                    "universes": universes,
                    "vacuum_axis": f"counterpart-{action_type}",
                    "source_atom": atom["atom_id"],
                })

    return vacuums


def generate_cross_domain_vacuums(atom: dict) -> list[dict]:
    """Generate vacuum atoms from cross-domain implications."""
    universes = atom.get("universes", [])
    summary = atom.get("summary", atom.get("content", "")[:120])
    vacuums = []

    for u in universes:
        cross_domains = CROSS_DOMAIN_MAP.get(u, [])
        for target_domain in cross_domains:
            if target_domain not in universes:
                vacuum_summary = f"Cross-domain implication in {target_domain}: {summary[:80]}"
                vacuums.append({
                    "type": "implicit-signal",
                    "content": vacuum_summary,
                    "summary": vacuum_summary,
                    "universes": [target_domain] + [x for x in universes if x != u][:2],
                    "vacuum_axis": f"cross-domain-{u}-to-{target_domain}",
                    "source_atom": atom["atom_id"],
                })

    return vacuums


def deduplicate_vacuums(vacuums: list[dict], existing_content: set[str]) -> list[dict]:
    """Remove vacuum atoms that duplicate existing content."""
    unique = []
    seen = set()
    for v in vacuums:
        # Normalize for dedup
        key = v["summary"][:60].lower().strip()
        if key in seen or key in existing_content:
            continue
        seen.add(key)
        unique.append(v)
    return unique


def main() -> None:
    dry_run = "--dry-run" in sys.argv
    from_done = "--from-done" in sys.argv
    limit = None
    if "--limit" in sys.argv:
        idx = sys.argv.index("--limit")
        if idx + 1 < len(sys.argv):
            limit = int(sys.argv[idx + 1])

    if not ATOMS_PATH.exists():
        print(f"ERROR: {ATOMS_PATH} not found", file=sys.stderr)
        sys.exit(1)

    print(f"Loading {ATOMS_PATH}...")
    with open(ATOMS_PATH) as f:
        atoms = json.load(f)

    # Build existing content fingerprints for dedup
    existing_content = {
        a.get("summary", a.get("content", ""))[:60].lower().strip()
        for a in atoms
    }

    # Select source atoms
    if from_done:
        # Scan DONE atoms — only high-priority ones to avoid noise
        source_atoms = [
            a for a in atoms
            if a.get("status") == "DONE" and a.get("priority", 99) <= 1
        ]
        print(f"Scanning {len(source_atoms)} high-priority DONE atoms...")
    else:
        # Scan recently-closed atoms (today)
        source_atoms = [
            a for a in atoms
            if a.get("status") == "DONE"
            and a.get("date", "") == TODAY
        ]
        print(f"Scanning {len(source_atoms)} atoms closed today...")

    if limit:
        source_atoms = source_atoms[:limit]

    # Generate vacuums
    all_vacuums: list[dict] = []
    axis_counts: Counter[str] = Counter()

    for atom in source_atoms:
        counterparts = generate_counterpart_vacuums(atom)
        cross_domain = generate_cross_domain_vacuums(atom)
        for v in counterparts + cross_domain:
            axis_counts[v["vacuum_axis"]] += 1
        all_vacuums.extend(counterparts)
        all_vacuums.extend(cross_domain)

    print(f"Raw vacuums generated: {len(all_vacuums)}")

    # Deduplicate
    unique_vacuums = deduplicate_vacuums(all_vacuums, existing_content)
    print(f"After dedup: {len(unique_vacuums)}")

    if not unique_vacuums:
        print("No new vacuum atoms to create.")
        return

    # Find next atom ID
    max_id = 0
    for a in atoms:
        aid = a.get("atom_id", "")
        if aid.startswith("ATM-"):
            num = int(aid.split("-")[1])
            if num > max_id:
                max_id = num

    # Create new atoms
    new_atoms = []
    for i, v in enumerate(unique_vacuums):
        new_atoms.append({
            "atom_id": f"ATM-{max_id + 1 + i:06d}",
            "parent_prompt_id": f"VACUUM-{v['source_atom']}",
            "type": v["type"],
            "content": v["content"],
            "summary": v["summary"],
            "universes": v["universes"],
            "status": "OPEN",
            "produced": ["vacuum-radiation", v["vacuum_axis"]],
            "source": "vacuum-engine",
            "date": TODAY,
            "timestamp": TIMESTAMP,
            "response_summary": "",
        })

    print(f"\nNew vacuum atoms: {len(new_atoms)}")
    print("\nAxis distribution:")
    for axis, count in axis_counts.most_common(15):
        print(f"  {axis}: {count}")

    print(f"\nSample atoms:")
    for a in new_atoms[:10]:
        print(f"  {a['atom_id']} ({', '.join(a['universes'][:2])}) — {a['summary'][:100]}")

    if dry_run:
        print(f"\n[DRY RUN] Would create {len(new_atoms)} vacuum atoms.")
    else:
        atoms.extend(new_atoms)
        print(f"\nWriting {ATOMS_PATH} ({len(atoms)} total)...")
        with open(ATOMS_PATH, "w") as f:
            json.dump(atoms, f, indent=1)
        print("Done.")


if __name__ == "__main__":
    main()
