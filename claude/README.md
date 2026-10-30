# Claude Code

This directory contains reusable Claude Code communication instructions,
including rules for code comments and structured user questions.

## Files

| Source | Intended destination | Purpose |
| --- | --- | --- |
| `CLAUDE.md` | `~/.claude/CLAUDE.md` | User-level instructions |
| [settings.json](settings.json) | `~/.claude/settings.json` | Default output style and prompt cache lifetimes |
| [output-styles/asd-ste100.md](output-styles/asd-ste100.md) | `~/.claude/output-styles/asd-ste100.md` | ASD-STE100 output style |

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

## Enable the ASD-STE100 output style

From this repository's root, install the style for your user:

```sh
mkdir -p ~/.claude/output-styles
cp -i claude/output-styles/asd-ste100.md ~/.claude/output-styles/asd-ste100.md
```

For one project, copy the file to that project's `.claude/output-styles/` instead.
Restart Claude Code after you add or edit the file. Then run `/config`, select
**Output style**, and select **ASD-STE100**. On Claude Code v2.1.269 or later,
you can also run:

```text
/output-style ASD-STE100
```

This selection is saved in the project's `.claude/settings.local.json`.
To use the style by default across projects, merge this field into
`~/.claude/settings.json`. Preserve the file's other settings:

```json
{
  "outputStyle": "ASD-STE100"
}
```

The setting is case-sensitive. Project settings can override the user default.
The style sets `keep-coding-instructions: true` to preserve Claude's built-in
coding instructions when Claude uses the full system prompt. This setting has
no effect with the shorter system prompt. To require the full prompt, start
Claude Code with:

```sh
CLAUDE_CODE_SIMPLE_SYSTEM_PROMPT=0 claude
```

The style complements `CLAUDE.md`; it does not replace the question rules there.
Separate subagents do not inherit the output style.

To check it, confirm the selected style in `/config`, then request a short change
explanation and a code comment. Check both against the style rules. This is an
instruction-based style, not a formal ASD-STE100 compliance check.

See the official [output style guide](https://code.claude.com/docs/en/output-styles).

## Apply settings

Use the [shared settings command](../README.md#apply-shared-settings) from the
repository root to merge [settings.json](settings.json) and install the output
style. The command also merges the Codex settings.

```sh
./scripts/apply-settings --dry-run
./scripts/apply-settings
```

The file selects ASD-STE100 by default and requests a one-hour prompt cache for
the main conversation and a five-minute cache for other requests, including
subagents. The cache settings require Claude Code v2.1.242 or later.
Environment overrides, including
`FORCE_PROMPT_CACHING_5M`, can take precedence. Provider support still applies.
One-hour cache writes cost more than five-minute writes on metered usage.

Restart Claude Code after installation. Check the style in `/config`. To verify
the main conversation's cache lifetime, inspect `usage.cache_creation` in JSON
output from a request: one-hour writes appear under `ephemeral_1h_input_tokens`.
See the official [prompt caching guide](https://code.claude.com/docs/en/prompt-caching).
