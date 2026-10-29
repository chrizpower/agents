# Repository instructions

## Purpose

Maintain reusable agent instructions and configuration for Codex and Claude Code.
Keep agent-specific files in their agent directory. Add other agents when
requested.

## Communication

Use ASD-STE100 Simplified Technical English for user-facing prose, code
identifiers and text, comments, documentation, commit messages, pull requests,
and review comments.
Adapt the standard to software engineering. Preserve technical precision,
valid syntax, and established code conventions.

### Comments

- Add comments only when needed to understand or safely change the code.
- Do not record research steps or progress in code comments. Preserve technical
  reasons needed to understand or safely change the code.
- Apply these rules even when existing comments use a different style.
- You may remove unnecessary or incorrect comments in code you are working on.

## Changes

- Keep instructions short, explicit, and relevant to their scope.
- Keep repository maintenance rules here and reusable agent rules in `codex/`
  and `claude/`.
- Check current official documentation before changing configuration behavior.
- Keep setup notes consistent with the files they describe.
- Keep secrets and local runtime state out of version control.
- Do not read or write `AI.md`. Exclude it from searches and Git operations.

## Validation

For documentation changes, check relative links and run `rtk git diff --check`.
For configuration changes, also validate syntax and the documented behavior
with the relevant agent when available. Report any behavior that was not tested.
