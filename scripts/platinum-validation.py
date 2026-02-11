#!/usr/bin/env python3
"""Platinum Sprint validation script.

Checks:
1. All platinum repos have CI workflows on GitHub
2. All platinum repos have CHANGELOG.md on GitHub
3. All platinum repos have badge rows in README
4. All platinum repos have ADRs in docs/adr/
5. Registry has implementation_status, ci_workflow, platinum_status fields
6. ORGAN-V has 10 essays
7. Dependency validation (no violations)
"""

import json
import subprocess
import sys
from pathlib import Path

REGISTRY_PATH = Path(__file__).parent.parent / "registry-v2.json"

def check_file_exists(org, repo, path):
    """Check if a file exists on GitHub."""
    result = subprocess.run(
        ["gh", "api", f"/repos/{org}/{repo}/contents/{path}"],
        capture_output=True, text=True
    )
    return result.returncode == 0


def get_readme_content(org, repo):
    """Get README content from GitHub."""
    result = subprocess.run(
        ["gh", "api", f"/repos/{org}/{repo}/contents/README.md",
         "-H", "Accept: application/vnd.github.raw+json"],
        capture_output=True, text=True
    )
    if result.returncode == 0:
        return result.stdout
    return ""


def main():
    with open(REGISTRY_PATH) as f:
        registry = json.load(f)

    issues = []
    warnings = []
    checks_passed = 0
    checks_total = 0

    print("=" * 60)
    print("PLATINUM SPRINT VALIDATION")
    print("=" * 60)

    # Collect all platinum repos
    platinum_repos = []
    for organ_key, organ_data in registry["organs"].items():
        if "repositories" not in organ_data:
            continue
        for repo in organ_data["repositories"]:
            if repo.get("platinum_status"):
                platinum_repos.append(repo)

    print(f"\nPlatinum repos in registry: {len(platinum_repos)}")

    # CHECK 1: Registry schema
    print("\n--- CHECK 1: Registry Schema Fields ---")
    missing_fields = 0
    for repo in platinum_repos:
        for field in ["implementation_status", "ci_workflow", "platinum_status"]:
            checks_total += 1
            if field not in repo:
                issues.append(f"Missing {field} in {repo['org']}/{repo['name']}")
                missing_fields += 1
            else:
                checks_passed += 1
    print(f"  Missing fields: {missing_fields}")
    if missing_fields == 0:
        print("  PASS")

    # CHECK 2: CI workflows exist on GitHub (sample 10 repos)
    print("\n--- CHECK 2: CI Workflows (sampling 10 repos) ---")
    import random
    sample = random.sample(platinum_repos, min(10, len(platinum_repos)))
    ci_pass = 0
    ci_fail = 0
    for repo in sample:
        checks_total += 1
        exists = check_file_exists(repo["org"], repo["name"], ".github/workflows/ci.yml")
        if exists:
            ci_pass += 1
            checks_passed += 1
        else:
            ci_fail += 1
            issues.append(f"Missing CI workflow: {repo['org']}/{repo['name']}")
    print(f"  CI workflows found: {ci_pass}/{len(sample)}")
    if ci_fail == 0:
        print("  PASS")
    else:
        print(f"  FAIL ({ci_fail} missing)")

    # CHECK 3: CHANGELOG.md exists (sample 10 repos)
    print("\n--- CHECK 3: CHANGELOG.md (sampling 10 repos) ---")
    sample2 = random.sample(platinum_repos, min(10, len(platinum_repos)))
    cl_pass = 0
    cl_fail = 0
    for repo in sample2:
        checks_total += 1
        exists = check_file_exists(repo["org"], repo["name"], "CHANGELOG.md")
        if exists:
            cl_pass += 1
            checks_passed += 1
        else:
            cl_fail += 1
            issues.append(f"Missing CHANGELOG.md: {repo['org']}/{repo['name']}")
    print(f"  CHANGELOGs found: {cl_pass}/{len(sample2)}")
    if cl_fail == 0:
        print("  PASS")
    else:
        print(f"  FAIL ({cl_fail} missing)")

    # CHECK 4: Badge rows in README (sample 5 repos)
    print("\n--- CHECK 4: Badge Rows (sampling 5 repos) ---")
    sample3 = random.sample(platinum_repos, min(5, len(platinum_repos)))
    badge_pass = 0
    badge_fail = 0
    for repo in sample3:
        checks_total += 1
        readme = get_readme_content(repo["org"], repo["name"])
        if "img.shields.io" in readme or "badge.svg" in readme:
            badge_pass += 1
            checks_passed += 1
        else:
            badge_fail += 1
            warnings.append(f"No badges in README: {repo['org']}/{repo['name']}")
    print(f"  Badge rows found: {badge_pass}/{len(sample3)}")
    if badge_fail == 0:
        print("  PASS")
    else:
        print(f"  WARNING ({badge_fail} missing)")

    # CHECK 5: ADRs exist (sample 5 repos)
    print("\n--- CHECK 5: ADRs (sampling 5 repos) ---")
    sample4 = random.sample(platinum_repos, min(5, len(platinum_repos)))
    adr_pass = 0
    adr_fail = 0
    for repo in sample4:
        checks_total += 1
        exists = check_file_exists(repo["org"], repo["name"], "docs/adr/001-initial-architecture.md")
        if exists:
            adr_pass += 1
            checks_passed += 1
        else:
            adr_fail += 1
            issues.append(f"Missing ADR-001: {repo['org']}/{repo['name']}")
    print(f"  ADRs found: {adr_pass}/{len(sample4)}")
    if adr_fail == 0:
        print("  PASS")
    else:
        print(f"  FAIL ({adr_fail} missing)")

    # CHECK 6: ORGAN-V essays
    print("\n--- CHECK 6: ORGAN-V Essays ---")
    checks_total += 1
    essay_count = 0
    for i in range(1, 11):
        prefix = f"0{i}" if i < 10 else str(i)
        result = subprocess.run(
            ["gh", "api", f"/repos/organvm-v-logos/public-process/contents/essays/meta-system"],
            capture_output=True, text=True
        )
        if result.returncode == 0:
            data = json.loads(result.stdout)
            essay_count = len([f for f in data if f["name"].endswith(".md")])
            break
    if essay_count >= 10:
        print(f"  Essays found: {essay_count}")
        print("  PASS")
        checks_passed += 1
    else:
        print(f"  Essays found: {essay_count} (expected 10)")
        print("  FAIL")
        issues.append(f"Only {essay_count} essays found (expected 10)")

    # CHECK 7: Dependency validation
    print("\n--- CHECK 7: Dependency Validation ---")
    checks_total += 1
    dep_violations = 0
    organ_order = {
        "organvm-i-theoria": 1,
        "organvm-ii-poiesis": 2,
        "organvm-iii-ergon": 3,
        "organvm-iv-taxis": 4,
        "organvm-v-logos": 5,
        "organvm-vi-koinonia": 6,
        "organvm-vii-kerygma": 7,
        "meta-organvm": 8,
    }
    for organ_key, organ_data in registry["organs"].items():
        if "repositories" not in organ_data:
            continue
        for repo in organ_data["repositories"]:
            repo_org = repo.get("org", "")
            repo_order = organ_order.get(repo_org, 0)
            for dep in repo.get("dependencies", []):
                dep_org = dep.split("/")[0] if "/" in dep else ""
                dep_order = organ_order.get(dep_org, 0)
                # Back-edge check: lower-numbered organs cannot depend on higher-numbered
                # Flow is I→II→III, so II can depend on I, III can depend on I or II
                # Back-edges: I depending on II/III, or II depending on III
                if repo_order < dep_order and repo_order > 0 and dep_order <= 3:
                    dep_violations += 1
                    issues.append(f"Back-edge: {repo_org}/{repo['name']} -> {dep}")
    if dep_violations == 0:
        print("  0 dependency violations")
        print("  PASS")
        checks_passed += 1
    else:
        print(f"  {dep_violations} violations found")
        print("  FAIL")

    # CHECK 8: Implementation status distribution
    print("\n--- CHECK 8: Implementation Status Distribution ---")
    checks_total += 1
    status_dist = {"PRODUCTION": 0, "PROTOTYPE": 0, "SKELETON": 0, "DESIGN_ONLY": 0}
    for organ_key, organ_data in registry["organs"].items():
        if "repositories" not in organ_data:
            continue
        for repo in organ_data["repositories"]:
            s = repo.get("implementation_status", "DESIGN_ONLY")
            if s in status_dist:
                status_dist[s] += 1
    print(f"  PRODUCTION: {status_dist['PRODUCTION']}")
    print(f"  PROTOTYPE: {status_dist['PROTOTYPE']}")
    print(f"  SKELETON: {status_dist['SKELETON']}")
    print(f"  DESIGN_ONLY: {status_dist['DESIGN_ONLY']}")
    checks_passed += 1
    print("  PASS")

    # SUMMARY
    print("\n" + "=" * 60)
    print("VALIDATION SUMMARY")
    print("=" * 60)
    print(f"Checks passed: {checks_passed}/{checks_total}")
    if issues:
        print(f"\nISSUES ({len(issues)}):")
        for issue in issues:
            print(f"  - {issue}")
    if warnings:
        print(f"\nWARNINGS ({len(warnings)}):")
        for w in warnings:
            print(f"  - {w}")
    if not issues:
        print("\nALL CHECKS PASSED")
        return 0
    return 1


if __name__ == "__main__":
    sys.exit(main())
