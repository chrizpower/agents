# Pi setup

[AGENTS.md](AGENTS.md) contains reusable Pi instructions. It keeps the shared
communication, project convention, comment, branch naming, and PR rules.
Question tools and subagent support depend on the tools and extensions available
in the session.

## Use

Copy or link `pi/AGENTS.md` to `~/.pi/agent/AGENTS.md`. If `PI_CODING_AGENT_DIR`
is set, use that directory instead. Preserve any existing local instructions
before replacing the destination. An `AGENTS.override.md` in that directory
takes precedence.

Run `/reload` in an existing Pi session after changing instructions, or start a
new session. The repository's `scripts/apply-settings` does not install Pi files.

See the official [configuration documentation](https://github.com/earendil-works/pi/blob/main/packages/coding-agent/docs/configuration.md)
and [extension documentation](https://github.com/earendil-works/pi/blob/main/packages/coding-agent/docs/extensions.md).
