# Communication

Use ASD-STE100 Simplified Technical English for user-facing prose, code
identifiers and text, comments, documentation, commit messages, pull requests,
and review comments.
Adapt the standard to software engineering. Preserve technical precision,
valid syntax, and established code conventions.

## User questions

When user input is needed, call `AskUserQuestion` to collect the answer.
Keep questions short and provide clear choices when useful.
Ask a small set of related questions at a time. Do not embed questions in long
explanations.
When providing choices, put the recommended option first and label it
"(Recommended)". Briefly explain why. If no option has a clear advantage, do not
invent a recommendation.
Wait for the answer before work that depends on it. Do not treat a missing
answer as approval.
If the tool is unavailable or cannot collect the input, ask a short, separate
question in prose and wait for the answer.

## Comments

- Add comments only when needed to understand or safely change the code.
- Do not record research steps or progress in code comments. Preserve technical
  reasons needed to understand or safely change the code.
- Apply these rules even when existing comments use a different style.
- You may remove unnecessary or incorrect comments in code you are working on.

# Git branch names

Follow repository branch naming rules. Otherwise, use `<type>/<short-description>`
with lowercase, hyphen-separated words and type `feat`, `fix`, `docs`,
`refactor`, `test`, or `chore`.

# Pull requests

For PRs you create, keep the description short with exactly two sections:

- `## What`: State what changed.
- `## Why`: State why the change is needed.

Keep both sections concise and relevant. End the description with
`Created with Claude.`

If additional details help the reviewer, add a short PR comment with relevant
validation steps, results, or other necessary information. Omit routine logs
and unrelated details.
