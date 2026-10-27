# Communication

Use ASD-STE100 Simplified Technical English for all communication and development
work.
Adapt the standard to software engineering terminology.
Preserve technical precision over strict ASD-STE100 compliance.

## User communication

Apply the style to all user-facing prose.

When user input is needed, call `AskUserQuestion` to collect the answer.
Keep questions short and provide clear choices when useful.
Wait for the answer before work that depends on it. Do not treat a missing
answer as approval.
If the tool is unavailable, ask the question in prose and wait for the answer.

## Code

Apply the style to code identifiers, comments, and text in code.
Preserve valid syntax and established code conventions.

### Comments

- Do not add comments to code that explains itself.
- Do not record research activity or findings in code comments.
- Add a comment only when it is needed to understand the code.
- Follow these rules instead of existing comment patterns, which can contain
  bad examples.
- You may delete unnecessary or incorrect comments in code you are working on.

## Artifacts

Apply the style to documentation, commit messages, pull request titles and
descriptions, and review comments.
