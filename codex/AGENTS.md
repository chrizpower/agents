# Communication

Use ASD-STE100 Simplified Technical English for user-facing prose, code
identifiers and text, comments, documentation, commit messages, pull requests,
and review comments.
Adapt the standard to software engineering. Preserve technical precision,
valid syntax, and required interfaces.

## Claims and evidence

Check claims that affect decisions against relevant sources or observed results.
If verification is not possible, state the uncertainty. Distinguish an unverified
claim from a false claim.

## Prose

Start with the answer, result, or required action. Include the context needed to
understand it and the detail needed to act or assess the result. Keep each point
once. Use established technical terms and explain unfamiliar terms when needed.

When the user says an explanation is unclear, explain it again in plain language.
Add the missing context and use a concrete example when useful.

## User questions

Use the task and repository context to resolve routine, reversible choices.
Ask the user when an open decision materially affects scope, compatibility,
or the requested outcome.

When input is needed, use a structured question tool permitted by the runtime,
such as `request_user_input` or `request_user_input_async`, including in Default
mode. If no permitted tool can collect the input, ask a separate prose question.

Keep questions short and group only related questions. Provide choices when
useful. Only when one option has a clear advantage, put it first, label it
"(Recommended)", and briefly explain why.
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

Run the relevant project checks. When possible, verify the requested outcome
through its normal entry point. State what passed, what failed, and which part
of the requested outcome remains unverified. Prefer automated checks for
mechanical rules. Use review for judgment calls.

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

# Branches and pull requests

For branch names and PR titles, use type `feat`, `fix`, `docs`, `refactor`,
`test`, or `chore`.

- Branch names use `<type>/<short-description>` with lowercase, hyphen-separated words.
- PR titles use `<type>: <short-description>`. Describe the final change in
  sentence case. Start the text after `<type>:` with an imperative verb and
  omit the final period.

For PRs you create, keep the description short with exactly two sections:

- `## What`: State what changed.
- `## Why`: State why the change is needed.

When a work ticket is known, include its ID and link in the PR's `## Why`
section. Use a closing keyword such as `Closes` only when the PR fully resolves
the ticket and the tracker supports it. Otherwise, use `Refs`.

If additional details help the reviewer, add a short PR comment with relevant
validation steps, results, or other necessary information. Omit routine logs
and unrelated details.

Use `Created by an 🤖.` as the only signature in PR descriptions and
`Comment by an 🤖.` as the only signature in PR comments. Put the signature last.
