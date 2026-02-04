# GitBook Links in Discord Notifications

## Overview

Enhance the GitBook to Discord workflow to include clickable links to specific sections that were updated in each change notification.

## Requirements

- Add GitBook URLs to Discord notifications pointing to specific sections/headers that changed
- Link format: `https://prtls.gitbook.io/portals-building-guide/{path}#{anchor}`
- Display format: Append ` → [View](url)` to the end of each bullet point
- Parse diffs to detect which headers were modified for precise section links

## Architecture

### Components

1. **Header Extraction Step** (new)
   - Parses git diff to identify modified markdown headers
   - Extracts header text and level
   - Position: After "Get changed files", before "Generate AI summary"

2. **URL Generation** (new)
   - Converts file paths to GitBook URLs
   - Generates URL anchors from header text
   - Creates mapping of files → sections → URLs

3. **AI Prompt Enhancement** (modified)
   - Receives URL mapping as additional context
   - Instructed to append ` → [View](url)` to each bullet
   - Matches changes to most relevant section link

4. **Discord Message** (unchanged)
   - Existing step handles markdown link rendering
   - No modifications needed

## Implementation Details

### URL Generation Logic

**File Path → GitBook URL**:
```
Input:  interactive-studio/effects/change-avatar.md
Remove: .md extension
Result: interactive-studio/effects/change-avatar
Final:  https://prtls.gitbook.io/portals-building-guide/interactive-studio/effects/change-avatar
```

**Header Text → URL Anchor**:
```
Input:  "Configuration Settings"
Steps:  lowercase → "configuration settings"
        spaces to hyphens → "configuration-settings"
        strip special chars → "configuration-settings"
Final:  #configuration-settings
```

### Header Extraction Process

For each changed `.md` file:

1. Parse the unified diff output
2. Find lines starting with `+#`, `+##`, `+###`, etc. (added/modified headers)
3. Extract header text: `+## Configuration` → `Configuration`
4. Convert to anchor format
5. Build full URL: base + path + anchor
6. Create mapping entry

**Fallback**: If no headers detected in diff, link to page root (no anchor)

### URL Mapping Format

Passed to AI as context:
```
Available section links:
- interactive-studio/effects/change-avatar.md → Configuration → https://prtls.gitbook.io/portals-building-guide/interactive-studio/effects/change-avatar#configuration
- token-swap/fee-wallet.md → Setup → https://prtls.gitbook.io/portals-building-guide/token-swap/fee-wallet#setup
```

### AI Prompt Updates

Add to system prompt:
- "For each bullet point, append ` → [View](url)` using the provided section links"
- "Match each change to the most relevant file and section from the mapping"
- "If multiple sections in one file changed, pick the most specific one per bullet"
- "If no link is available, omit the View link for that bullet"

Add to user message:
- Include the URL mapping after the diff content

### Output Format

Example Discord message:
```
**Updated**
- Added fee wallet configuration to Token Swap setup → [View](https://prtls.gitbook.io/portals-building-guide/token-swap/fee-wallet#setup)
- Updated avatar change effect parameters → [View](https://prtls.gitbook.io/portals-building-guide/interactive-studio/effects/change-avatar#configuration)

**Added**
- New multiplayer sync functions documentation → [View](https://prtls.gitbook.io/portals-building-guide/multiplayer/functions#sync)
```

## Error Handling

### URL Anchor Generation
- Strip emojis and special characters: `[^a-z0-9- ]`
- Handle consecutive spaces/hyphens: normalize to single hyphen
- Trim leading/trailing hyphens
- Empty result fallback: use page-level link

### Duplicate Headers
- GitBook adds `-1`, `-2` suffixes for duplicate headers
- Our implementation links to first occurrence (no suffix)
- Users can navigate to correct section from the page

### Edge Cases
- **No headers in diff**: Link to page root (no anchor)
- **Non-markdown files**: Skip in URL mapping
- **Invalid UTF-8**: Sanitize before anchor generation
- **Very long headers**: GitBook truncates anchors; we'll use first 50 chars

## Testing Plan

1. **Test commit with multiple file types**:
   - Modified `.md` files with headers
   - Modified `.md` files without headers
   - Non-`.md` files (should be skipped)

2. **Verify URL accuracy**:
   - Manually visit generated URLs
   - Confirm anchors scroll to correct section
   - Test special characters in headers

3. **Discord rendering**:
   - Check markdown links display correctly
   - Verify embed limits not exceeded
   - Test with long summaries

4. **AI matching**:
   - Confirm bullets match appropriate URLs
   - Check fallback behavior when uncertain

## Implementation Estimate

- New workflow step: ~50 lines bash + Python
- AI prompt modifications: ~10 lines
- Testing and refinement: Manual verification
- Total additions: ~60-100 lines of code

## Success Criteria

- Every bullet point in Discord has a clickable GitBook link
- Links point to specific sections when headers are modified
- Links point to page root when no specific section detected
- URLs are correctly formatted and functional
- AI consistently appends links in the correct format
