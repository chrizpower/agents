# Claude Code

This directory contains reusable Claude Code communication instructions,
including rules for code comments and structured user questions.

## Files

| Source | Intended destination | Purpose |
| --- | --- | --- |
| `CLAUDE.md` | `~/.claude/CLAUDE.md` | User-level instructions |

The root [AGENTS.md](../AGENTS.md) governs maintenance of this repository.

## Apply instructions

1. Compare [CLAUDE.md](CLAUDE.md) with `~/.claude/CLAUDE.md`.
2. Merge the required instructions. Preserve existing rules that you still need.
3. Start a new interactive Claude Code session. Use `/memory` to check the loaded
   instruction files.
4. Ask Claude to collect a decision with `AskUserQuestion`. Check that it opens
   the question interface and waits for your answer.

Claude Code provides the `AskUserQuestion` tool for decisions and clarification.
These instructions direct Claude to call that tool when user input is needed;
they do not require a separate ask mode or feature flag. The tool must be
available in the session. If it is unavailable, the instructions require a
plain-text question.

See the official [instruction guide](https://code.claude.com/docs/en/memory)
and [question tool reference](https://code.claude.com/docs/en/tools-reference#askuserquestion-tool-behavior).
