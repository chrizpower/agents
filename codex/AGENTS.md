# Communication

Use ASD-STE100 Simplified Technical English for user-facing prose, code
identifiers and text, comments, documentation, commit messages, pull requests,
and review comments.
Adapt the standard to software engineering. Preserve technical precision,
valid syntax, and established code conventions.

## User questions

When user input is needed, use an available structured question tool that the
runtime permits, such as `request_user_input` or `request_user_input_async`.
Apply this rule in Default mode too. Keep questions short and provide clear
choices when useful. Ask a small set of related questions at a time. Do not
embed questions in long explanations.
When providing choices, put the recommended option first and label it
"(Recommended)". Briefly explain why. If no option has a clear advantage, do not
invent a recommendation.
Wait for required answers before work that depends on them. Continue independent
work when possible. Do not treat a missing answer as approval. If no permitted
question tool can collect the input, ask a short, separate question in prose.
Use the runtime approval process for permission requests.

## Comments

- Add comments only when needed to understand or safely change the code.
- Do not record research steps or progress in code comments. Preserve technical
  reasons needed to understand or safely change the code.
- Apply these rules even when existing comments use a different style.
- You may remove unnecessary or incorrect comments in code you are working on.

# Subagent context

These rules apply only when delegation is already authorized. Preserve required
models, roles, reviews, budgets, and permissions.

Start new subagents without inherited conversation history by default. When the
spawn tool supports `fork_turns`, set it to `"none"`. Inherit history only when
the assignment needs it.

Give each subagent a short, self-contained brief with its objective, scope,
applicable instructions, constraints, required checks, and expected result.
Include relevant decisions from the conversation and exact source or evidence
pointers. Do not copy unrelated history or raw outputs.

# Git branch names

Follow repository branch naming rules. Otherwise, use `<type>/<short-description>`
with lowercase, hyphen-separated words and type `feat`, `fix`, `docs`,
`refactor`, `test`, or `chore`.

# Pull requests

For PRs you create, keep the description short with exactly two sections:

- `## What`: State what changed.
- `## Why`: State why the change is needed.

Keep both sections concise and relevant. End the description with
`Created with an agent.`

If additional details help the reviewer, add a short PR comment with relevant
validation steps, results, or other necessary information. Omit routine logs
and unrelated details.
