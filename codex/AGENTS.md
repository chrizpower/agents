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
