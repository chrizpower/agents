# Codex

This directory contains reusable Codex instructions. The initial baseline covers
communication. Add other instructions and configuration as requirements become
clear.

## Files

| Source | Intended destination | Purpose |
| --- | --- | --- |
| `AGENTS.md` | `$CODEX_HOME/AGENTS.md` | User-level instructions |

`CODEX_HOME` defaults to `~/.codex`. The root [AGENTS.md](../AGENTS.md) governs
maintenance of this repository.

## Apply instructions

1. Compare [AGENTS.md](AGENTS.md) with the file in your Codex home directory.
2. Merge the required instructions into that file. Preserve existing rules that
   you still need.
3. Check for `AGENTS.override.md` in the same directory. Codex reads that file
   instead of `AGENTS.md` when the override is non-empty.
4. Start a new Codex session and ask it to list the instruction sources and
   summarize the communication rules.

Project instructions can be added in each project's `AGENTS.md`. Codex combines
global and project instructions, with more specific directory guidance taking
precedence. See the official [instruction discovery guide](https://learn.chatgpt.com/docs/agent-configuration/agents-md).

## Configuration settings

Codex stores user settings in `$CODEX_HOME/config.toml`. Trusted projects can
also provide `.codex/config.toml`. See the official
[configuration guide](https://learn.chatgpt.com/docs/config-file/config-basic).

This repository does not define configuration settings yet. When settings are
added, document their purpose, destination, and validation here. Keep credentials
and machine-specific settings outside the reusable configuration.
