# Agent instructions

Version-controlled instructions and configuration for Codex and Claude Code.
Add other agents when there is a concrete need.

## Layout

| Path | Purpose |
| --- | --- |
| `AGENTS.md` | Instructions for agents that maintain this repository |
| `codex/` | Reusable Codex instructions and configuration notes |
| `claude/` | Reusable Claude Code instructions and setup notes |

Keep each agent's files in its own directory. Add shared instructions only when
two or more agents need the same content.

## Use

Start with [Codex setup](codex/README.md) or
[Claude Code setup](claude/README.md). Files in this repository are source files.
Cloning this repository does not install them into an agent's user configuration.

Keep credentials, authentication files, session history, and machine-specific
state outside this repository.

## Apply shared settings

Install [uv](https://docs.astral.sh/uv/getting-started/installation/) and Python
3.11 or later. From this repository, run these commands after a pull:

```sh
./scripts/apply-settings --dry-run
./scripts/apply-settings
```

The command merges Claude and Codex settings and installs the Claude output
style. It uses `CLAUDE_CONFIG_DIR` (default `~/.claude`) and `CODEX_HOME`
(default `~/.codex`). Use `--claude-dir PATH` and `--codex-home PATH` to select
other directories. It does not install the instruction files.

Repository values replace matching local values. Nested objects and TOML tables
merge recursively; arrays replace the existing array. Unrelated local keys stay.
Removing a key from this repository does not remove its installed value.
TOML comments and formatting are preserved. Changed JSON files use two-space
indentation. The output style file is replaced as a whole.

Dry-run output lists changed keys and paths without displaying values or writing
target files. The first run can download the pinned TOML parser through uv.
All inputs are parsed before writes start. Each changed existing file gets a
private `.backup-*` file beside it. Each replacement is atomic, but the complete
set of files is not one transaction. Existing symbolic links are followed and
preserved; backups are placed beside their resolved targets.

Close agents that can write settings before applying changes. Repeated runs make
no changes when the installed values already match. Restart the agents after
applying changes. To restore a file, copy its backup over the resolved target.

Run the merge tests with:

```sh
uv run --with tomlkit==0.13.3 python -m unittest discover -s tests -v
```
