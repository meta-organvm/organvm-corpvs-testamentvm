#!/usr/bin/env python3
"""Calculate system-wide metrics from registry-v2.json.

Standalone metrics calculator used by the monthly-organ-audit workflow.
Can also be run independently for ad-hoc metrics.

Usage:
    python3 scripts/calculate-metrics.py \
        --registry registry-v2.json \
        --output metrics.json
"""

import argparse
import json
import sys
from collections import defaultdict
from datetime import datetime, timezone


def main():
    parser = argparse.ArgumentParser(description="Calculate system metrics")
    parser.add_argument("--registry", required=True, help="Path to registry-v2.json")
    parser.add_argument("--output", required=True, help="Path for JSON metrics output")
    args = parser.parse_args()

    with open(args.registry) as f:
        registry = json.load(f)

    organs = registry.get("organs", {})
    all_repos = []
    for organ_data in organs.values():
        all_repos.extend(organ_data.get("repositories", []))

    operational = sum(
        1 for o in organs.values()
        if o.get("launch_status") == "OPERATIONAL"
    )

    status_dist = defaultdict(int)
    tier_dist = defaultdict(int)
    promotion_dist = defaultdict(int)
    ci_count = 0
    platinum_count = 0
    doc_status_dist = defaultdict(int)

    for repo in all_repos:
        status_dist[repo.get("implementation_status", "UNKNOWN")] += 1
        tier_dist[repo.get("tier", "unknown")] += 1
        promotion_dist[repo.get("promotion_status", "UNKNOWN")] += 1
        doc_status_dist[repo.get("documentation_status", "UNKNOWN")] += 1
        if repo.get("ci_workflow"):
            ci_count += 1
        if repo.get("platinum_status"):
            platinum_count += 1

    # Dependency stats
    dep_count = sum(
        len(repo.get("dependencies", []))
        for repo in all_repos
    )

    metrics = {
        "audit_date": datetime.now(timezone.utc).isoformat(),
        "total_repos": len(all_repos),
        "total_organs": len(organs),
        "operational_organs": operational,
        "completion": round(operational / max(len(organs), 1) * 100, 1),
        "implementation_status": dict(status_dist),
        "tier_distribution": dict(tier_dist),
        "promotion_status": dict(promotion_dist),
        "documentation_status": dict(doc_status_dist),
        "ci_coverage": ci_count,
        "platinum_repos": platinum_count,
        "total_dependencies": dep_count,
        "critical_alerts": 0,
        "warnings": 0,
    }

    with open(args.output, "w") as f:
        json.dump(metrics, f, indent=2)
        f.write("\n")

    print(f"Metrics written to {args.output}")
    print(f"  Repos: {metrics['total_repos']}")
    print(f"  Organs: {metrics['operational_organs']}/{metrics['total_organs']} operational")
    print(f"  CI: {ci_count}/{len(all_repos)}")
    print(f"  Platinum: {platinum_count}")


if __name__ == "__main__":
    main()
