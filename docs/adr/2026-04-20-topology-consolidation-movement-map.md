# ADR: Topology Consolidation Movement Map (2026-04-20)

**Decision**: Consolidate 8-org workspace structure + home root sprawl into minimal flat-pool topology.
**Rationale**: Numbered organ orgs are scaffold superseded by SPEC-025 (flat primitive pool). Sprawling root is anti-pattern to evolving/elevating/minimizing.

---

## PHASE PRE (Before — 2026-04-20 ~12:00)

### ~/Workspace/ (top-level)
```
~/Workspace/
├── organvm-i-theoria/           # Organ I superproject (18 repos inside)
├── organvm-ii-poiesis/          # Organ II superproject (10 repos inside)
├── organvm-iii-ergon/           # Organ III superproject (12 repos inside)
├── organvm-iv-taxis/            # Organ IV superproject (31 repos inside)
├── organvm-v-logos/             # Organ V superproject (7 repos inside)
├── organvm-vi-koinonia/         # Organ VI superproject (7 repos inside)
├── organvm-vii-kerygma/         # Organ VII superproject (8 repos inside)
├── meta-organvm/                # Meta superproject (16 repos inside)
├── 4444J99/                     # Personal superproject (8 repos)
├── a-i--skills/                 # Standalone (stub, not git repo)
├── alchemia-ingestvm/           # Data staging directory
├── blender-mcp/                 # Standalone git repo
├── dwv/                         # Standalone directory
├── fastmcp/                     # Standalone git repo
├── gemini-cli-blender-extension/ # Standalone git repo
├── intake/                      # Unsorted inbound
├── k6-contrib/                  # Standalone git repo
├── openai-agents-contrib/       # Standalone git repo
├── python-sdk/                  # Standalone git repo
├── CLAUDE.md                    # Workspace guidance
├── AGENTS.md                    # Agent guidance
├── GEMINI.md                    # Gemini guidance
├── INSTANCE.toml                # Workspace instance descriptor
├── workspace-manifest.json      # Manifest
├── export-*.md (6 files)        # Session exports (loose)
├── 2026-*.txt (2 files)         # Session logs (loose)
├── session-ses_2969.md          # Session file (loose)
├── sync_interlinked_landing_pages.sh  # Loose script
└── text-based--relevance.md     # Loose doc
```

### ~/ Home Root
```
~/
├── domus-semper-palingenesis/    # Chezmoi source (13GB)
├── system-system--system/       # Git repo (45MB) — system governance
├── system-system--system--monad/ # Git worktree (2.1MB) — theoretical research
├── sovereign--ground/           # Git repo (4.3MB) — structural investigation
├── chaos--incarnate/            # INSTANCE.toml only — world plane concept
├── i--me--mine/                 # INSTANCE.toml only — world plane concept
├── mort--proto-intre-post/      # Empty directory
├── is--_not/                    # Empty directory
├── Projects/                    # Empty scaffold (Active/, Archive/)
├── nltk_data/                   # Python NLP data (4.5MB)
├── Calendar/                    # Calendar data (8K)
├── System/                      # Logs directory
├── Workspace/                   # (see above)
├── AGENTS.md                    # Deployed by chezmoi
├── CLAUDE.md                    # Deployed by chezmoi
├── GEMINI.md                    # Deployed by chezmoi
├── .claude.json                 # Claude config (chezmoi managed)
├── seed.yaml                    # Home-level seed contract
├── task_review_report_2026_04_13.md  # Loose report
├── 2026-04-05-*.txt             # Session export
├── 2026-04-18-*.txt (2 files)   # Session exports
├── 2026-04-18-*.md              # Session export
└── [standard macOS: Applications, Desktop, Documents, Downloads, Library, Movies, Music, Pictures, Public]
```

---

## PHASE POST (After — 2026-04-20 ~12:15)

### ~/Workspace/ (top-level)
```
~/Workspace/
├── organvm/                     # ALL system repos, flat (104 repos)
├── 4444J99/                     # Personal repos (unchanged)
├── meta-organvm → organvm/      # SYMLINK (backward compat for env vars)
├── a-i--skills → organvm/a-i--skills  # SYMLINK (backward compat for skill paths)
├── alchemia-ingestvm/           # Data staging directory (unchanged)
├── intake/                      # Unsorted inbound (augmented)
├── .archive/                    # Archived superproject shells
├── CLAUDE.md                    # (unchanged)
├── AGENTS.md                    # (unchanged)
├── GEMINI.md                    # (unchanged)
├── INSTANCE.toml                # (unchanged)
└── workspace-manifest.json      # (unchanged)
```

### ~/ Home Root
```
~/
├── domus-semper-palingenesis/    # Chezmoi source (unchanged)
├── System/                      # Logs directory (unchanged)
├── Workspace/                   # (see above)
├── AGENTS.md                    # Deployed by chezmoi (unchanged)
├── CLAUDE.md                    # Deployed by chezmoi (unchanged)
├── GEMINI.md                    # Deployed by chezmoi (unchanged)
├── .claude.json                 # Claude config (unchanged)
├── seed.yaml                    # Home-level seed (unchanged)
└── [standard macOS: Applications, Desktop, Documents, Downloads, Library, Movies, Music, Pictures, Public]
```

---

## MOVEMENT KEY

### Repos: Organ Superprojects → ~/Workspace/organvm/

| Previous Location | Current Location | Count |
|-------------------|-----------------|-------|
| `~/Workspace/organvm-i-theoria/<repo>/` | `~/Workspace/organvm/<repo>/` | 17 repos |
| `~/Workspace/organvm-ii-poiesis/<repo>/` | `~/Workspace/organvm/<repo>/` | 9 repos |
| `~/Workspace/organvm-iii-ergon/<repo>/` | `~/Workspace/organvm/<repo>/` | 11 repos |
| `~/Workspace/organvm-iv-taxis/<repo>/` | `~/Workspace/organvm/<repo>/` | 30 repos |
| `~/Workspace/organvm-v-logos/<repo>/` | `~/Workspace/organvm/<repo>/` | 6 repos |
| `~/Workspace/organvm-vi-koinonia/<repo>/` | `~/Workspace/organvm/<repo>/` | 6 repos |
| `~/Workspace/organvm-vii-kerygma/<repo>/` | `~/Workspace/organvm/<repo>/` | 6 repos |
| `~/Workspace/meta-organvm/<repo>/` | `~/Workspace/organvm/<repo>/` | 14 repos |
| **Total from organ superprojects** | | **~99 repos** |

### Repos: Standalone → ~/Workspace/organvm/

| Previous Location | Current Location |
|-------------------|-----------------|
| `~/Workspace/blender-mcp/` | `~/Workspace/organvm/blender-mcp/` |
| `~/Workspace/fastmcp/` | `~/Workspace/organvm/fastmcp/` |
| `~/Workspace/k6-contrib/` | `~/Workspace/organvm/k6-contrib/` |
| `~/Workspace/openai-agents-contrib/` | `~/Workspace/organvm/openai-agents-contrib/` |
| `~/Workspace/python-sdk/` | `~/Workspace/organvm/python-sdk/` |
| `~/Workspace/gemini-cli-blender-extension/` | `~/Workspace/organvm/gemini-cli-blender-extension/` |

### Repos: Home Root → ~/Workspace/organvm/

| Previous Location | Current Location |
|-------------------|-----------------|
| `~/system-system--system/` | `~/Workspace/organvm/system-system--system/` |
| `~/system-system--system--monad/` | `~/Workspace/organvm/system-system--system--monad/` |
| `~/sovereign--ground/` | `~/Workspace/organvm/sovereign--ground/` |

### Superproject Shells → Archive

| Previous Location | Current Location |
|-------------------|-----------------|
| `~/Workspace/organvm-i-theoria/` (shell + non-repo data) | `~/Workspace/.archive/superprojects-20260420-120747/organvm-i-theoria/` |
| `~/Workspace/organvm-ii-poiesis/` (shell) | `~/Workspace/.archive/superprojects-20260420-120747/organvm-ii-poiesis/` |
| `~/Workspace/organvm-iii-ergon/` (shell) | `~/Workspace/.archive/superprojects-20260420-120747/organvm-iii-ergon/` |
| `~/Workspace/organvm-iv-taxis/` (shell) | `~/Workspace/.archive/superprojects-20260420-120747/organvm-iv-taxis/` |
| `~/Workspace/organvm-v-logos/` (shell) | `~/Workspace/.archive/superprojects-20260420-120747/organvm-v-logos/` |
| `~/Workspace/organvm-vi-koinonia/` (shell) | `~/Workspace/.archive/superprojects-20260420-120747/organvm-vi-koinonia/` |
| `~/Workspace/organvm-vii-kerygma/` (shell) | `~/Workspace/.archive/superprojects-20260420-120747/organvm-vii-kerygma/` |
| `~/Workspace/meta-organvm/` (shell) | `~/Workspace/.archive/superprojects-20260420-120747/meta-organvm/` |

**Note**: Superproject shells contain .git history, .gitmodules, CLAUDE.md, AGENTS.md, and NON-REPO data (conversation-corpus-site 9.4GB, post-flood/, loose session files). All repos inside were extracted first.

### Home Root Concepts → ~/Workspace/intake/

| Previous Location | Current Location |
|-------------------|-----------------|
| `~/chaos--incarnate/` (INSTANCE.toml) | `~/Workspace/intake/chaos--incarnate/` |
| `~/i--me--mine/` (INSTANCE.toml) | `~/Workspace/intake/i--me--mine/` |
| `~/Calendar/` | `~/Workspace/intake/Calendar/` |
| `~/task_review_report_2026_04_13.md` | `~/Workspace/intake/task_review_report_2026_04_13.md` |
| `~/2026-04-05-*.txt` | `~/Workspace/intake/2026-04-05-*.txt` |
| `~/2026-04-18-*.txt` (2 files) | `~/Workspace/intake/2026-04-18-*.txt` |
| `~/2026-04-18-*.md` | `~/Workspace/intake/2026-04-18-*.md` |

### Home Root → DELETED

| Previous Location | Reason |
|-------------------|--------|
| `~/mort--proto-intre-post/` | Empty directory — no content to preserve |
| `~/is--_not/` | Empty directory — no content to preserve |
| `~/Projects/` | Empty scaffold (Active/, Archive/) — no content |

### Home Root → Relocated

| Previous Location | Current Location | Reason |
|-------------------|-----------------|--------|
| `~/nltk_data/` | `~/.local/share/nltk_data/` | XDG compliance — data belongs in XDG_DATA_HOME |

### Workspace Loose Files → ~/Workspace/intake/workspace-cleanup/

| Previous Location | Current Location |
|-------------------|-----------------|
| `~/Workspace/export-2026-04-07-1544.md` | `~/Workspace/intake/workspace-cleanup/20260420-120747/export-2026-04-07-1544.md` |
| `~/Workspace/export-governed-sequences.md` | `~/Workspace/intake/workspace-cleanup/20260420-120747/export-governed-sequences.md` |
| `~/Workspace/export-workspace-interaction.md` | `~/Workspace/intake/workspace-cleanup/20260420-120747/export-workspace-interaction.md` |
| `~/Workspace/export-reality-existence.md` | `~/Workspace/intake/workspace-cleanup/20260420-120747/export-reality-existence.md` |
| `~/Workspace/export-fortify-postmortem.md` | `~/Workspace/intake/workspace-cleanup/20260420-120747/export-fortify-postmortem.md` |
| `~/Workspace/export-origin-inventory.md` | `~/Workspace/intake/workspace-cleanup/20260420-120747/export-origin-inventory.md` |
| `~/Workspace/sync_interlinked_landing_pages.sh` | `~/Workspace/intake/workspace-cleanup/20260420-120747/sync_interlinked_landing_pages.sh` |
| `~/Workspace/text-based--relevance.md` | `~/Workspace/intake/workspace-cleanup/20260420-120747/text-based--relevance.md` |
| `~/Workspace/session-ses_2969.md` | `~/Workspace/intake/workspace-cleanup/20260420-120747/session-ses_2969.md` |
| `~/Workspace/2026-04-16-*.txt` | `~/Workspace/intake/workspace-cleanup/20260420-120747/2026-04-16-*.txt` |
| `~/Workspace/2026-04-07-*.txt` | `~/Workspace/intake/workspace-cleanup/20260420-120747/2026-04-07-*.txt` |

### Workspace Root Stub → Symlink

| Previous Location | Current Location | Type |
|-------------------|-----------------|------|
| `~/Workspace/a-i--skills/` (stub dir, not git) | `~/Workspace/a-i--skills → ~/Workspace/organvm/a-i--skills` | Symlink |

### Symlinks Created (backward compatibility)

| Symlink Path | Points To | Purpose |
|-------------|-----------|---------|
| `~/Workspace/meta-organvm` | `~/Workspace/organvm/` | `$ORGANVM_CORPUS_DIR` resolution |
| `~/Workspace/a-i--skills` | `~/Workspace/organvm/a-i--skills/` | Skill path resolution |

---

## .github COLLISION NOTE

6 per-organ `.github` repos could not move because `~/Workspace/organvm/.github/` was already occupied by the first one (from organvm-i-theoria). The remaining `.github` repos are in:
- `~/Workspace/.archive/superprojects-20260420-120747/organvm-ii-poiesis/.github/`
- `~/Workspace/.archive/superprojects-20260420-120747/organvm-iii-ergon/.github/`
- `~/Workspace/.archive/superprojects-20260420-120747/organvm-iv-taxis/.github/`
- `~/Workspace/.archive/superprojects-20260420-120747/organvm-v-logos/.github/`
- `~/Workspace/.archive/superprojects-20260420-120747/organvm-vi-koinonia/.github/`
- `~/Workspace/.archive/superprojects-20260420-120747/organvm-vii-kerygma/.github/`
- `~/Workspace/.archive/superprojects-20260420-120747/meta-organvm/.github/`

These contain per-organ org profiles and org-level configs. Post-consolidation, ONE unified `.github` repo is needed for the `organvm` org.

---

## WHAT DID NOT MOVE

| Location | Reason |
|----------|--------|
| `~/domus-semper-palingenesis/` | Chezmoi source — must be at ~/ |
| `~/System/` | System logs, state |
| `~/AGENTS.md`, `~/CLAUDE.md`, `~/GEMINI.md` | Deployed by chezmoi to ~/ |
| `~/.claude.json` | Claude config (chezmoi managed) |
| `~/seed.yaml` | Home-level seed contract |
| `~/Workspace/4444J99/` | Personal repos — unchanged |
| `~/Workspace/alchemia-ingestvm/` | Data staging dir (not a repo) |
| `~/Workspace/intake/` | Destination — augmented |
| `~/Workspace/CLAUDE.md`, `AGENTS.md`, `GEMINI.md` | Workspace guidance — unchanged |
| `~/Workspace/INSTANCE.toml` | Workspace instance descriptor |
| `~/Workspace/workspace-manifest.json` | Manifest |
| `~/Workspace/dwv/` | Previously moved to intake earlier in session |

---

## SUMMARY COUNTS

| Category | Count |
|----------|-------|
| Repos moved to `~/Workspace/organvm/` | **104** (99 from organs + 6 standalone + 3 from home root - 4 .github collisions) |
| Superproject shells archived | **8** |
| Home root directories cleaned | **8** (3 moved to organvm, 2 to intake, 3 deleted) |
| Loose files triaged to intake | **~15** |
| Symlinks created | **2** |
| Directories at ~/ removed | **5** (3 empty + 2 concept dirs to intake) |
| Net reduction in ~/ top-level dirs | **8 directories eliminated** |
| Net reduction in ~/Workspace/ top-level dirs | **~12 directories → 1 (organvm/) + symlinks** |
