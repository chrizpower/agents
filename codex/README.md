# Codex

This directory contains reusable Codex instructions. The initial baseline covers
communication and structured user questions. Add other instructions and
configuration as requirements become clear.

## Files

| Source | Intended destination | Purpose |
| --- | --- | --- |
| `AGENTS.md` | `$CODEX_HOME/AGENTS.md` | User-level instructions |
| [config.toml](config.toml) | `$CODEX_HOME/config.toml` | Reusable configuration baseline |

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

The supplied [config.toml](config.toml) enables structured questions in Default
mode. Other settings use the applicable configuration or runtime defaults.
Install `AGENTS.md` separately for the communication rules.
Keep credentials and machine-specific settings outside this file.

Merge the file into your existing configuration, preserving other settings.
For a new setup, run these commands from the repository root:

```sh
mkdir -p "${CODEX_HOME:-$HOME/.codex}"
cp -i codex/config.toml "${CODEX_HOME:-$HOME/.codex}/config.toml"
```

For versions that support structured questions in Default mode, enable
`default_mode_request_user_input` under `[features]` in your local
`config.toml`. Check support and status with `codex features list`; the local
CLI currently marks this feature as under development. The flag enables tool
availability. The instructions direct when to ask questions, subject to runtime
restrictions.

After applying the instructions, start a new interactive session in Default
mode. Ask Codex to collect a preference with the question tool. Check that the
question interface opens and that Codex uses your answer. Documentation checks
do not verify this interactive behavior.
