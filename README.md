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
