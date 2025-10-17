# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a Claude custom skill that adds "ニャン" (nyan/meow) to the end of all Claude responses, making Claude speak in a cat-like manner. The project supports two deployment methods:

1. **Claude.ai Skills**: Upload `SKILL.md` to Claude.ai (for Pro/Max/Team/Enterprise users)
2. **Claude Code Hooks**: Use the `UserPromptSubmit` hook with `add_nyuan.py` script

## Architecture

### Core Components

- **`add_nyuan.py`**: Python script that implements the UserPromptSubmit hook
  - Reads user prompt from stdin
  - Returns JSON with `approval: "approved"` and `additionalContext` containing instructions to append "ニャン"
  - Zero external dependencies (uses only stdlib: sys, json)

- **`SKILL.md`**: Claude.ai Skills format file
  - Contains YAML frontmatter with `name` and `description` fields
  - Markdown body with usage instructions and examples
  - Model-invoked skill that Claude autonomously uses when appropriate

- **`README.md`**: Comprehensive documentation in Japanese
  - Installation instructions for both deployment methods
  - Troubleshooting guide
  - Customization examples (changing suffix to other patterns)

### How It Works

**Claude Code Hooks method:**
```
User input → UserPromptSubmit hook fires → add_nyuan.py executes →
Injects additional context → Claude processes with "ニャン" suffix → Response displayed
```

**Claude.ai Skills method:**
- Skill metadata (name/description) loaded into system prompt at startup
- Claude autonomously decides when to use the skill based on user request
- SKILL.md content loaded into context when skill is invoked

## Testing & Validation

Test the hook script directly:
```bash
echo "test" | python3 add_nyuan.py
```
Expected output: JSON with `approval` and `additionalContext` fields

## Customization

To change the suffix from "ニャン" to something else:
1. Edit `add_nyuan.py` line 15-24 (`additional_context` variable)
2. Update `SKILL.md` description and examples to match new behavior
3. Update README.md accordingly

## File Permissions

The script must be executable:
```bash
chmod +x add_nyuan.py
```

## Configuration Paths

- **Project-specific**: `.claude/config.json` (in target project root)
- **Global**: `~/.config/claude/config.json`

Both require absolute path to `add_nyuan.py` in the hook command.
