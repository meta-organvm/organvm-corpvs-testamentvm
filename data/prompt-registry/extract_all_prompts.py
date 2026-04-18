#!/usr/bin/env python3
"""Extract every user prompt from ALL Claude Code sessions into a structured registry.

Reads JSONL files from ~/.claude/projects/*/ (the authoritative source for all sessions).
Parses each human message with full metadata and outputs:
1. A JSON registry (prompt-registry.json) — machine-readable, full metadata
2. A markdown registry (INST-INDEX-PROMPTORUM.md) — human-readable, grouped views
"""

import json
import os
import re
from datetime import datetime
from pathlib import Path

PROJECTS_DIR = Path.home() / ".claude" / "projects"
CHATGPT_EXPORT = Path.home() / "Workspace/meta-organvm/intake/data-2026-02-16-00-20-00-batch-0000/conversations.json"
CODEX_HISTORY = Path.home() / ".codex" / "history.jsonl"
REGISTRY_DIR = Path(__file__).parent
OUTPUT_JSON = REGISTRY_DIR / "prompt-registry.json"
OUTPUT_MD = REGISTRY_DIR / "INST-INDEX-PROMPTORUM.md"


def extract_project_path(dir_name: str) -> str:
    """Convert project directory name back to a readable path."""
    # Format: -Users-4jp-Workspace-meta-organvm → /Users/4jp/Workspace/meta-organvm
    return "/" + dir_name.replace("-", "/").lstrip("/")


def parse_jsonl_session(filepath: Path, project_dir: str) -> list[dict]:
    """Parse a JSONL session file and extract all human messages."""
    prompts = []
    project_path = extract_project_path(project_dir)

    try:
        with open(filepath, "r", encoding="utf-8") as f:
            lines = f.readlines()
    except (OSError, UnicodeDecodeError):
        return []

    prompt_num = 0
    for line_text in lines:
        line_text = line_text.strip()
        if not line_text:
            continue

        try:
            entry = json.loads(line_text)
        except json.JSONDecodeError:
            continue

        # Look for user messages
        if entry.get("type") != "user":
            continue

        # Skip sidechain/meta messages
        if entry.get("isSidechain") or entry.get("isMeta"):
            continue

        # Extract content
        content_parts = entry.get("message", {}).get("content", [])
        if isinstance(content_parts, str):
            raw_content = content_parts
        elif isinstance(content_parts, list):
            text_parts = []
            for part in content_parts:
                if isinstance(part, dict) and part.get("type") == "text":
                    text_parts.append(part.get("text", ""))
                elif isinstance(part, str):
                    text_parts.append(part)
            raw_content = "\n".join(text_parts)
        else:
            continue

        if not raw_content or not raw_content.strip():
            continue

        # Skip system-generated messages (local-command-caveat wrappers)
        if "<local-command-caveat>" in raw_content and len(raw_content) < 200:
            continue
        if "<local-command-stdout>" in raw_content and len(raw_content) < 200:
            continue
        if raw_content.strip().startswith("<command-name>") and len(raw_content) < 200:
            # Extract slash command
            cmd_match = re.search(r"<command-name>([^<]+)</command-name>", raw_content)
            if cmd_match:
                raw_content = f"/{cmd_match.group(1)}"
            else:
                continue

        prompt_num += 1

        # Get timestamp (ISO string format: 2026-04-16T12:35:26.621Z)
        timestamp_raw = entry.get("timestamp", "")
        if isinstance(timestamp_raw, str) and timestamp_raw:
            try:
                dt = datetime.fromisoformat(timestamp_raw.replace("Z", "+00:00"))
                timestamp_str = dt.strftime("%Y-%m-%d %H:%M:%S")
                date_str = dt.strftime("%Y-%m-%d")
            except ValueError:
                timestamp_str = timestamp_raw
                date_str = timestamp_raw[:10] if len(timestamp_raw) >= 10 else ""
        elif isinstance(timestamp_raw, (int, float)) and timestamp_raw > 0:
            dt = datetime.fromtimestamp(timestamp_raw / 1000)
            timestamp_str = dt.strftime("%Y-%m-%d %H:%M:%S")
            date_str = dt.strftime("%Y-%m-%d")
        else:
            timestamp_str = ""
            date_str = ""

        # Classify
        categories = classify_prompt(raw_content)

        # Summary (first 150 chars, single line)
        summary = raw_content[:150].replace("\n", " ").strip()
        if len(raw_content) > 150:
            summary += "..."

        session_id = filepath.stem  # UUID from filename

        prompts.append({
            "session_id": session_id,
            "project_dir": project_dir,
            "project_path": project_path,
            "prompt_number": prompt_num,
            "timestamp": timestamp_str,
            "date": date_str,
            "content": raw_content,
            "summary": summary,
            "categories": categories,
            "status": "UNREVIEWED",
            "content_length": len(raw_content),
            "source": "claude-code",
        })

    return prompts


def parse_chatgpt_export(filepath: Path) -> list[dict]:
    """Parse a ChatGPT conversations.json export and extract all human messages."""
    prompts = []
    try:
        data = json.loads(filepath.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return []

    for conv in data:
        conv_name = conv.get("name", "untitled")
        conv_uuid = conv.get("uuid", "")
        messages = conv.get("chat_messages", [])

        prompt_num = 0
        for msg in messages:
            if msg.get("sender") != "human":
                continue

            text = msg.get("text") or ""
            if not text.strip():
                continue

            prompt_num += 1

            ts_raw = msg.get("created_at", "")
            if ts_raw:
                try:
                    dt = datetime.fromisoformat(ts_raw.replace("Z", "+00:00"))
                    timestamp_str = dt.strftime("%Y-%m-%d %H:%M:%S")
                    date_str = dt.strftime("%Y-%m-%d")
                except ValueError:
                    timestamp_str = ts_raw
                    date_str = ts_raw[:10]
            else:
                timestamp_str = ""
                date_str = ""

            summary = text[:150].replace("\n", " ").strip()
            if len(text) > 150:
                summary += "..."

            prompts.append({
                "session_id": conv_uuid,
                "project_dir": "chatgpt",
                "project_path": "ChatGPT",
                "prompt_number": prompt_num,
                "timestamp": timestamp_str,
                "date": date_str,
                "content": text,
                "summary": summary,
                "categories": classify_prompt(text),
                "status": "UNREVIEWED",
                "content_length": len(text),
                "source": "chatgpt",
                "conversation_name": conv_name,
            })

    return prompts


def parse_codex_history(filepath: Path) -> list[dict]:
    """Parse Codex history.jsonl and extract all user prompts."""
    prompts = []
    session_counters: dict[str, int] = {}

    try:
        with open(filepath, "r", encoding="utf-8") as f:
            lines = f.readlines()
    except OSError:
        return []

    for line_text in lines:
        line_text = line_text.strip()
        if not line_text:
            continue
        try:
            entry = json.loads(line_text)
        except json.JSONDecodeError:
            continue

        text = entry.get("text", "")
        if not text or not text.strip():
            continue

        session_id = entry.get("session_id", "unknown")
        session_counters[session_id] = session_counters.get(session_id, 0) + 1

        ts_raw = entry.get("ts", 0)
        if ts_raw:
            dt = datetime.fromtimestamp(ts_raw)
            timestamp_str = dt.strftime("%Y-%m-%d %H:%M:%S")
            date_str = dt.strftime("%Y-%m-%d")
        else:
            timestamp_str = ""
            date_str = ""

        summary = text[:150].replace("\n", " ").strip()
        if len(text) > 150:
            summary += "..."

        prompts.append({
            "session_id": session_id,
            "project_dir": "codex",
            "project_path": "Codex",
            "prompt_number": session_counters[session_id],
            "timestamp": timestamp_str,
            "date": date_str,
            "content": text,
            "summary": summary,
            "categories": classify_prompt(text),
            "status": "UNREVIEWED",
            "content_length": len(text),
            "source": "codex",
        })

    return prompts


def classify_prompt(content: str) -> list[str]:
    """Classify a prompt into categories."""
    categories = []
    lower = content.lower()

    if content.startswith("/"):
        categories.append("command")
        return categories

    # Close-out litany
    if "provide an overview of all that was" in lower or "are we certain, sisyphus" in lower:
        categories.append("close-out")
    if "commit[all] push[origin]" in lower:
        categories.append("close-out")
    if "(local):(remote)" in lower:
        categories.append("close-out")
    if "nothing will be lost" in lower:
        categories.append("close-out")

    # Governance rules
    if "vacuum" in lower and ("n/a" in lower or "none-knowledge" in lower):
        categories.append("governance")
    if "persistent memory must" in lower:
        categories.append("governance")
    if "every single thing you ingest" in lower:
        categories.append("governance")
    if "must be universally" in lower:
        categories.append("governance")

    # Directives
    directive_words = [
        r"\bsolve\b", r"\bbuild\b", r"\bcreate\b", r"\bimplement\b",
        r"\bfix\b", r"\bwrite\b", r"\bdesign\b", r"\bwe need to\b",
        r"\blet'?s\b", r"\bmake\b", r"\bensure\b", r"\bwire\b",
    ]
    for pat in directive_words:
        if re.search(pat, lower):
            categories.append("directive")
            break

    # Questions
    if content.rstrip().endswith("?") or re.match(r"^(what|why|how|is |does |did |can |where)", lower):
        categories.append("question")

    # Emotional
    if any(w in lower for w in ["fuck", "shit", "retard", "sick of", "frustrated", "idiot", "moron"]):
        categories.append("emotional")

    # Resume/carry-forward
    if "last session" in lower or "pick this back up" in lower or "continue" in lower:
        categories.append("carry-forward")

    # Pasted content (large blocks)
    if len(content) > 500 and content.count("\n") > 10:
        categories.append("pasted-content")

    # Personal
    if any(w in lower for w in ["becka", "housing", "employment", "income", "money"]):
        categories.append("personal")

    if not categories:
        categories.append("uncategorized")

    return list(set(categories))


def generate_markdown(all_prompts: list[dict]) -> str:
    """Generate the full markdown registry."""
    lines = []
    lines.append("# Index Promptorum — Complete Prompt Registry")
    lines.append("")
    lines.append(f"**Generated:** {datetime.now().isoformat()}")
    lines.append(f"**Total prompts:** {len(all_prompts)}")
    sessions = set(p["session_id"] for p in all_prompts)
    lines.append(f"**Total sessions:** {len(sessions)}")
    dates = [p["date"] for p in all_prompts if p["date"]]
    if dates:
        lines.append(f"**Date range:** {min(dates)} → {max(dates)}")
    lines.append("")
    lines.append("**Automation:** SessionEnd hook at `~/.claude/hooks/session-prompt-capture.sh`")
    lines.append("**Machine-readable:** `data/prompt-registry/prompt-registry.json`")
    lines.append("")

    # Category stats
    cat_counts: dict[str, int] = {}
    for p in all_prompts:
        for c in p["categories"]:
            cat_counts[c] = cat_counts.get(c, 0) + 1

    lines.append("## Statistics")
    lines.append("")
    lines.append("| Category | Count | % |")
    lines.append("|----------|-------|---|")
    for cat, count in sorted(cat_counts.items(), key=lambda x: -x[1]):
        pct = count / len(all_prompts) * 100
        lines.append(f"| {cat} | {count} | {pct:.1f}% |")
    lines.append("")

    # Status counts
    status_counts: dict[str, int] = {}
    for p in all_prompts:
        s = p["status"]
        status_counts[s] = status_counts.get(s, 0) + 1
    lines.append("| Status | Count |")
    lines.append("|--------|-------|")
    for s, count in sorted(status_counts.items()):
        lines.append(f"| {s} | {count} |")
    lines.append("")

    # Daily activity
    daily: dict[str, int] = {}
    for p in all_prompts:
        if p["date"]:
            daily[p["date"]] = daily.get(p["date"], 0) + 1

    lines.append("## Daily Activity")
    lines.append("")
    lines.append("| Date | Prompts |")
    lines.append("|------|---------|")
    for date in sorted(daily.keys()):
        lines.append(f"| {date} | {daily[date]} |")
    lines.append("")

    # Directives view (the implementation tracking board)
    directives = [p for p in all_prompts if "directive" in p["categories"]]
    lines.append("---")
    lines.append(f"## Directives — Implementation Tracking ({len(directives)})")
    lines.append("")
    lines.append("| ID | Date | Project | Status | Prompt |")
    lines.append("|----|------|---------|--------|--------|")
    for i, p in enumerate(directives, 1):
        proj = p["project_path"].split("/")[-1] if "/" in p["project_path"] else p["project_path"]
        summary = p["summary"][:80].replace("|", "\\|")
        lines.append(f"| D-{i:04d} | {p['date']} | {proj} | {p['status']} | {summary} |")
    lines.append("")

    # Governance rules view
    governance = [p for p in all_prompts if "governance" in p["categories"]]
    lines.append("---")
    lines.append(f"## Governance Rules ({len(governance)})")
    lines.append("")
    for p in governance:
        lines.append(f"- **[{p['date']}]** {p['summary']}")
    lines.append("")

    # By project directory
    lines.append("---")
    lines.append("## By Project Directory")
    lines.append("")
    by_proj: dict[str, list] = {}
    for p in all_prompts:
        by_proj.setdefault(p["project_path"], []).append(p)

    for proj in sorted(by_proj.keys()):
        prompts = by_proj[proj]
        lines.append(f"### `{proj}` ({len(prompts)} prompts)")
        lines.append("")
        for p in prompts[:10]:  # Show first 10 per project
            lines.append(f"- [{p['date']}] {p['summary']}")
        if len(prompts) > 10:
            lines.append(f"- ... and {len(prompts)-10} more")
        lines.append("")

    return "\n".join(lines)


def main():
    all_prompts = []

    # Walk ALL project directories
    for project_dir in sorted(PROJECTS_DIR.iterdir()):
        if not project_dir.is_dir():
            continue

        project_name = project_dir.name

        # Find all JSONL files (sessions)
        jsonl_files = sorted(project_dir.glob("*.jsonl"))
        for jsonl_file in jsonl_files:
            prompts = parse_jsonl_session(jsonl_file, project_name)
            all_prompts.extend(prompts)

    # ChatGPT export
    if CHATGPT_EXPORT.exists():
        chatgpt_prompts = parse_chatgpt_export(CHATGPT_EXPORT)
        all_prompts.extend(chatgpt_prompts)
        print(f"ChatGPT: {len(chatgpt_prompts)} prompts")

    # Codex history
    if CODEX_HISTORY.exists():
        codex_prompts = parse_codex_history(CODEX_HISTORY)
        all_prompts.extend(codex_prompts)
        print(f"Codex: {len(codex_prompts)} prompts")

    if not all_prompts:
        print("No prompts found.")
        return

    # Sort by timestamp
    all_prompts.sort(key=lambda p: p["timestamp"] or "0")

    # Assign sequential IDs
    for i, p in enumerate(all_prompts, 1):
        p["id"] = f"PRM-{i:05d}"

    # Write JSON
    OUTPUT_JSON.write_text(
        json.dumps(all_prompts, indent=2, ensure_ascii=False), encoding="utf-8"
    )
    print(f"JSON: {len(all_prompts)} prompts → {OUTPUT_JSON}")

    # Write Markdown
    md = generate_markdown(all_prompts)
    OUTPUT_MD.write_text(md, encoding="utf-8")
    print(f"Markdown: → {OUTPUT_MD}")

    # Stats
    cats = {}
    for p in all_prompts:
        for c in p["categories"]:
            cats[c] = cats.get(c, 0) + 1
    print(f"\nCategories:")
    for c, n in sorted(cats.items(), key=lambda x: -x[1]):
        print(f"  {c}: {n}")


if __name__ == "__main__":
    main()
