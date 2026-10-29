# Repository instructions

## Purpose

Maintain reusable agent instructions and configuration for Codex and Claude Code.
Keep agent-specific files in their agent directory. Add other agents when
requested.

## Agent instructions

Read and follow the instructions for the agent in use:

- Codex: [codex/AGENTS.md](codex/AGENTS.md).
- Claude Code: [claude/CLAUDE.md](claude/CLAUDE.md).

## Changes

- Keep instructions short, explicit, and relevant to their scope.
- Keep repository maintenance rules here and reusable agent rules in `codex/`
  and `claude/`.
- Check current official documentation before changing configuration behavior.
- Keep setup notes consistent with the files they describe.
- Keep secrets and local runtime state out of version control.

## Validation

For documentation changes, check relative links and run `rtk git diff --check`.
For configuration changes, also validate syntax and the documented behavior
with the relevant agent when available. Report any behavior that was not tested.
