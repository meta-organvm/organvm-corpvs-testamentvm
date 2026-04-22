#!/usr/bin/env python3
"""Reclassify non-actionable UNREVIEWED atoms in prompt-atoms.json.

Closes atoms whose type is inherently non-actionable:
  question       -> CLOSED-QUESTION
  command        -> CLOSED-COMMAND
  emotional      -> CLOSED-SIGNAL
  data           -> CLOSED-DATA
  implicit-signal -> CLOSED-SIGNAL

Actionable types left as UNREVIEWED:
  directive, governance-rule, constraint, correction
"""

import json
import sys
from collections import Counter
from pathlib import Path

RECLASSIFY_MAP: dict[str, str] = {
    "question": "CLOSED-QUESTION",
    "command": "CLOSED-COMMAND",
    "emotional": "CLOSED-SIGNAL",
    "data": "CLOSED-DATA",
    "implicit-signal": "CLOSED-SIGNAL",
}

def main() -> None:
    src = Path(__file__).resolve().parent / "prompt-atoms.json"

    if not src.exists():
        print(f"FATAL: {src} not found", file=sys.stderr)
        sys.exit(1)

    print(f"Loading {src} ...")
    with src.open("r", encoding="utf-8") as f:
        atoms: list[dict] = json.load(f)

    print(f"Loaded {len(atoms)} atoms.")

    reclassified: Counter[str] = Counter()
    for atom in atoms:
        if atom.get("status") != "UNREVIEWED":
            continue
        new_status = RECLASSIFY_MAP.get(atom.get("type", ""))
        if new_status is None:
            continue
        atom["status"] = new_status
        reclassified[atom["type"]] += 1

    total_changed = sum(reclassified.values())
    if total_changed == 0:
        print("No atoms matched reclassification criteria. Nothing written.")
        sys.exit(0)

    print(f"\nReclassified {total_changed} atoms:")
    for typ, count in sorted(reclassified.items(), key=lambda x: -x[1]):
        print(f"  {typ:20s} -> {RECLASSIFY_MAP[typ]:20s}  ({count})")

    # Write back — compact JSON (no indent) to keep file size reasonable
    print(f"\nWriting {src} ...")
    with src.open("w", encoding="utf-8") as f:
        json.dump(atoms, f, ensure_ascii=False, separators=(",", ":"))
        f.write("\n")

    print(f"Written. File size: {src.stat().st_size / (1024 * 1024):.1f} MB")

    # Final status distribution
    status_dist: Counter[str] = Counter(a.get("status") for a in atoms)
    print("\nNew status distribution:")
    for status, count in sorted(status_dist.items(), key=lambda x: -x[1]):
        print(f"  {status:20s}  {count}")

if __name__ == "__main__":
    main()
