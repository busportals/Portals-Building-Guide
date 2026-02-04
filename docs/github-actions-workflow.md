# GitHub Actions Workflow: GitBook to Discord

## Overview

This workflow automatically posts GitBook documentation updates to Discord with clickable section links.

## Workflow Steps

1. **Get commit diff** - Extracts git diff between before/after commits
2. **Get changed files** - Lists files with their change status (A/M/D/R)
3. **Generate GitBook URLs** - Parses diff to extract headers and generate section URLs
4. **Generate AI summary** - Uses OpenAI to create human-readable summary with links
5. **Send to Discord** - Posts formatted embed to Discord webhook

## GitBook URL Generation

The URL generation script (`.github/scripts/generate-gitbook-urls.py`) performs:

- **Header extraction**: Finds lines starting with `+#` in diff (added/modified headers)
- **Anchor generation**: Converts header text to URL-safe anchors
  - Lowercase transformation
  - Space-to-hyphen conversion
  - Special character removal (keeping alphanumeric and hyphens)
  - Length limiting (50 chars max)
- **URL construction**: `https://prtls.gitbook.io/portals-building-guide/{path}#{anchor}`

### Examples

| File Path | Header | Generated URL |
|-----------|--------|---------------|
| `interactive-studio/effects/change-avatar.md` | `Configuration` | `.../change-avatar#configuration` |
| `token-swap/fee-wallet.md` | `Setup & Install` | `.../fee-wallet#setup-and-install` |
| `docs/guide.md` | `User's Guide (Advanced)` | `.../guide#users-guide-advanced` |

## AI Integration

The AI receives:
- Changed files list (name-status format)
- Unified diff (truncated to 10KB)
- URL mapping (generated section links)

The AI is instructed to:
- Convert technical changes to user-facing descriptions
- Append ` → [View](url)` to each bullet point
- Match changes to most relevant section link
- Fall back to page-level link if no section match

## Discord Output Format

```
**Updated**
- Added fee wallet configuration to Token Swap setup → [View](url)
- Updated avatar change effect parameters → [View](url)

**Added**
- New multiplayer sync functions documentation → [View](url)
```

## Error Handling

- **No valid diff**: Fallback message with file list
- **No headers detected**: Page-level links without anchors
- **Non-markdown files**: Ignored by URL generation
- **AI API failure**: Shows "AI summary unavailable" with file list
- **Very long summaries**: Truncated to 2000 chars (Discord limit)

## Testing Locally

Test URL generation:
```bash
git diff HEAD~1 HEAD | python3 .github/scripts/generate-gitbook-urls.py
```

Test full workflow (requires secrets):
```bash
act push --secret-file .secrets
```

## Maintenance

When GitBook URL structure changes:
1. Update `GITBOOK_BASE` in `.github/scripts/generate-gitbook-urls.py`
2. Adjust `text_to_anchor()` function if anchor format changes
3. Test with sample diffs to verify URLs still work
