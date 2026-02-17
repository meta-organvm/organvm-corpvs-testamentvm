#!/usr/bin/env python3
"""Essay Auto-Deploy — push ready essays from docs/essays/ to public-process.

Scans docs/essays/ for files with complete Jekyll frontmatter (layout, title,
date), compares against files already in organvm-v-logos/public-process/_posts/,
and deploys new essays via the GitHub API.

Usage:
    python3 scripts/essay-deploy.py                   # dry-run (default)
    python3 scripts/essay-deploy.py --deploy          # actually push
    python3 scripts/essay-deploy.py --deploy --verbose
"""

import argparse
import base64
import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ESSAYS_DIR = ROOT / "docs" / "essays"
TARGET_REPO = "organvm-v-logos/public-process"
TARGET_DIR = "_posts"


def parse_frontmatter(path: Path) -> dict | None:
    """Extract YAML frontmatter from a markdown file.

    Returns dict with keys or None if frontmatter is missing/incomplete.
    """
    text = path.read_text(encoding="utf-8")
    match = re.match(r"^---\n(.*?)\n---", text, re.DOTALL)
    if not match:
        return None

    fm = {}
    for line in match.group(1).splitlines():
        # Simple key: value parsing (handles quoted and unquoted values)
        m = re.match(r'^(\w[\w_-]*)\s*:\s*(.+)$', line)
        if m:
            key = m.group(1).strip()
            val = m.group(2).strip().strip('"').strip("'")
            fm[key] = val
    return fm


def is_ready(fm: dict) -> bool:
    """Check if frontmatter has the minimum fields for deployment."""
    return all(k in fm for k in ("layout", "title", "date"))


def target_filename(fm: dict, source: Path) -> str:
    """Generate the Jekyll _posts/ filename: YYYY-MM-DD-slug.md."""
    date = fm["date"]
    # Extract slug from source filename (strip leading number prefix)
    stem = source.stem
    # Pattern: NN-slug or NNN-slug
    m = re.match(r"^\d+-(.+)$", stem)
    slug = m.group(1) if m else stem
    return f"{date}-{slug}.md"


def fetch_remote_files() -> set[str]:
    """List files in the remote _posts/ directory via GitHub API."""
    result = subprocess.run(
        ["gh", "api",
         f"repos/{TARGET_REPO}/git/trees/HEAD?recursive=1",
         "--jq", '.tree[] | select(.path | startswith("_posts/")) | .path'],
        capture_output=True, text=True, timeout=30,
    )
    if result.returncode != 0:
        print(f"WARNING: Could not list remote _posts/: {result.stderr.strip()}")
        return set()

    files = set()
    for line in result.stdout.strip().splitlines():
        if line:
            # Extract just the filename from _posts/YYYY-MM-DD-slug.md
            files.add(line.split("/")[-1])
    return files


def push_essay(source: Path, filename: str, verbose: bool = False) -> bool:
    """Push a single essay to the remote _posts/ directory via gh api PUT."""
    content = source.read_bytes()
    b64 = base64.b64encode(content).decode("ascii")

    payload = json.dumps({
        "message": f"essay: deploy {filename}",
        "content": b64,
    })

    endpoint = f"repos/{TARGET_REPO}/contents/{TARGET_DIR}/{filename}"
    result = subprocess.run(
        ["gh", "api", endpoint, "--method", "PUT", "--input", "-"],
        input=payload, capture_output=True, text=True, timeout=30,
    )

    if result.returncode == 0:
        if verbose:
            print(f"  OK: {filename}")
        return True

    # Check if file already exists (409 or SHA mismatch)
    if "sha" in result.stderr.lower() or result.returncode == 409:
        if verbose:
            print(f"  SKIP (already exists): {filename}")
        return False

    print(f"  ERROR deploying {filename}: {result.stderr.strip()}")
    return False


def main():
    parser = argparse.ArgumentParser(
        description="Deploy ready essays from docs/essays/ to public-process _posts/"
    )
    parser.add_argument(
        "--deploy", action="store_true",
        help="Actually push essays (default is dry-run)"
    )
    parser.add_argument(
        "--verbose", "-v", action="store_true",
        help="Show detailed output"
    )
    args = parser.parse_args()

    mode = "DEPLOY" if args.deploy else "DRY-RUN"
    print(f"Essay Auto-Deploy [{mode}]")
    print("=" * 40)

    # Scan local essays
    if not ESSAYS_DIR.is_dir():
        print(f"ERROR: Essays directory not found: {ESSAYS_DIR}")
        sys.exit(1)

    local_essays = sorted(ESSAYS_DIR.glob("*.md"))
    print(f"Local essays found: {len(local_essays)}")

    # Parse and filter ready essays
    ready = []
    for path in local_essays:
        fm = parse_frontmatter(path)
        if fm and is_ready(fm):
            ready.append((path, fm))
        elif args.verbose:
            print(f"  SKIP (incomplete frontmatter): {path.name}")

    print(f"Ready to deploy: {len(ready)}")

    # Fetch remote state
    remote_files = fetch_remote_files()
    print(f"Remote _posts/ files: {len(remote_files)}")

    # Find undeployed essays
    to_deploy = []
    for path, fm in ready:
        filename = target_filename(fm, path)
        if filename not in remote_files:
            to_deploy.append((path, fm, filename))
        elif args.verbose:
            print(f"  Already deployed: {filename}")

    print(f"\nUndeployed essays: {len(to_deploy)}")

    if not to_deploy:
        print("Nothing to deploy.")
        return 0

    # List what would be / will be deployed
    for path, fm, filename in to_deploy:
        title = fm.get("title", path.stem)
        print(f"  {filename} — \"{title}\"")

    if not args.deploy:
        print(f"\nDry-run complete. Use --deploy to push {len(to_deploy)} essay(s).")
        return 0

    # Deploy
    print(f"\nDeploying {len(to_deploy)} essay(s)...")
    deployed = 0
    for path, fm, filename in to_deploy:
        if push_essay(path, filename, verbose=args.verbose):
            deployed += 1

    print(f"\nDeployed: {deployed}/{len(to_deploy)}")
    return 0 if deployed == len(to_deploy) else 1


if __name__ == "__main__":
    sys.exit(main())
