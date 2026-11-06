# Communication

Use ASD-STE100 Simplified Technical English for user-facing prose, code
identifiers and text, comments, documentation, commit messages, pull requests,
and review comments.
Adapt the standard to software engineering. Preserve technical precision,
valid syntax, and required interfaces.

## Prose

Start with the answer, result, or required action. Include the context needed to
understand it and the detail needed to act or assess the result. Keep each point
once. Use established technical terms and explain unfamiliar terms when needed.

When the user says an explanation is unclear, explain it again in plain language.
Add the missing context and use a concrete example when useful.

## User questions

When input is needed, use `AskUserQuestion` if available and permitted by the
runtime. If it cannot collect the input, ask a separate prose question.

Keep questions short and group only related questions. Provide choices when
useful. Put a clearly recommended option first, label it "(Recommended)", and
briefly explain why. If no option has a clear advantage, omit the recommendation.
Wait for required answers before dependent work. Continue independent work.
Do not treat a missing answer as approval. Use the runtime approval process for
permission requests.

## Comments

Add comments only when needed to understand or safely change the code. Explain
technical reasons, not research steps or progress. Apply these rules to comments
you change, even when nearby comments use a different style. Remove unnecessary
or incorrect comments within the task's scope.

# Project conventions

Read applicable repository instructions before making changes. Treat existing
code and documentation as potentially outdated or inconsistent. Distinguish
explicit requirements from incidental patterns. Repetition alone does not
justify a pattern.

Follow conventions that support correctness, clear responsibilities, and
testability. Before reusing a pattern, check for concrete problems such as
duplicated logic, unnecessary coupling, or abstractions that add complexity.
Preserve required behavior and interfaces unless the task calls for changing
them. Keep improvements within the task's scope and explain material departures
from existing patterns.

If an explicit repository rule conflicts with these goals, state the conflict.
Resolve it using applicable instructions and task requirements. If the decision
remains unclear, ask the user before dependent changes.

Use the project's validation commands and check their results. Report failures
and checks not run. Prefer automated checks for mechanical rules; use review
for judgment calls.

# Git branch names

Use `<type>/<short-description>` for branch names
with lowercase, hyphen-separated words and type `feat`, `fix`, `docs`,
`refactor`, `test`, or `chore`.

# Pull requests

Use `<type>: <short-description>` for PR titles. Use type `feat`, `fix`, `docs`,
`refactor`, `test`, or `chore`. Start the description with an imperative verb,
use sentence case, and omit the final period. Describe the final change.

For PRs you create, keep the description short with exactly two sections:

- `## What`: State what changed.
- `## Why`: State why the change is needed.

When a work ticket is known, include its ID and link in the PR's `## Why`
section. Use a closing keyword such as `Closes` only when the PR fully resolves
the ticket and the tracker supports it. Otherwise, use `Refs`.

End the description with
`Created by an 🤖.`

If additional details help the reviewer, add a short PR comment with relevant
validation steps, results, or other necessary information. Omit routine logs
and unrelated details.

End every PR comment with `Comment by an 🤖.`
