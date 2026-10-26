# Repository instructions

## Purpose

Maintain reusable agent instructions and configuration. Current scope: Codex.
Keep agent-specific files in their agent directory. Add other agents when
requested.

## Communication

Use ASD-STE100 Simplified Technical English for all communication and development
work.
Adapt the standard to software engineering terminology.
Preserve technical precision over strict ASD-STE100 compliance.

### User communication

Apply the style to all user-facing prose.

### Code

Apply the style to code identifiers, comments, and text in code.
Preserve valid syntax and established code conventions.

#### Comments

- Do not add comments to code that explains itself.
- Do not record research activity or findings in code comments.
- Add a comment only when it is needed to understand the code.
- Follow these rules instead of existing comment patterns, which can contain
  bad examples.
- You may delete unnecessary or incorrect comments in code you are working on.

### Artifacts

Apply the style to documentation, commit messages, pull request titles and
descriptions, and review comments.

## Changes

- Keep instructions short, explicit, and relevant to their scope.
- Keep repository maintenance rules here and reusable Codex rules in `codex/`.
- Check current official documentation before changing configuration behavior.
- Keep setup notes consistent with the files they describe.
- Keep secrets and local runtime state out of version control.
- Do not read or write `AI.md`. Exclude it from searches and Git operations.

## Validation

For documentation changes, check relative links and run `rtk git diff --check`.
For configuration changes, also validate syntax and the documented behavior
with the relevant agent when available. Report any behavior that was not tested.
