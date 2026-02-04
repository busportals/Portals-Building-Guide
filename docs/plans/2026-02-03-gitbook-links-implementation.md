# GitBook Links in Discord Notifications - Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Add clickable GitBook section links to Discord update notifications

**Architecture:** Insert new workflow step to extract headers from git diffs, generate GitBook URLs with anchors, and pass URL mapping to AI for inclusion in summary bullets

**Tech Stack:** GitHub Actions, Bash, Python3, OpenAI API

---

## Task 1: Create URL Generation Script

**Files:**
- Create: `.github/scripts/generate-gitbook-urls.py`

**Step 1: Create scripts directory**

Run: `mkdir -p .github/scripts`
Expected: Directory created

**Step 2: Write URL generation script**

Create `.github/scripts/generate-gitbook-urls.py`:

```python
#!/usr/bin/env python3
"""
Generate GitBook URLs with section anchors from git diff output.
Reads diff from stdin, outputs URL mapping to stdout.
"""
import sys
import re

GITBOOK_BASE = "https://prtls.gitbook.io/portals-building-guide"

def extract_headers_from_diff(diff_text):
    """
    Parse unified diff to find added/modified headers.
    Returns: [(file_path, header_text), ...]
    """
    results = []
    current_file = None

    for line in diff_text.splitlines():
        # Track current file being diffed
        if line.startswith('diff --git'):
            # Extract b/ path (new version)
            match = re.search(r'b/(.+\.md)$', line)
            if match:
                current_file = match.group(1)

        # Look for added markdown headers (+ at start, then #)
        elif line.startswith('+#') and current_file:
            # Extract header level and text
            match = re.match(r'^\+(#{1,6})\s+(.+)$', line)
            if match:
                header_text = match.group(2).strip()
                results.append((current_file, header_text))

    return results

def text_to_anchor(text):
    """
    Convert header text to GitBook URL anchor format.
    Examples:
      "Configuration Settings" -> "configuration-settings"
      "Setup & Install" -> "setup-and-install"
    """
    # Lowercase
    anchor = text.lower()

    # Replace & with 'and'
    anchor = anchor.replace('&', 'and')

    # Keep only alphanumeric, spaces, and hyphens
    anchor = re.sub(r'[^a-z0-9\s-]', '', anchor)

    # Replace spaces with hyphens
    anchor = re.sub(r'\s+', '-', anchor)

    # Normalize multiple hyphens to single
    anchor = re.sub(r'-+', '-', anchor)

    # Trim hyphens from ends
    anchor = anchor.strip('-')

    # Limit length (GitBook truncates very long anchors)
    if len(anchor) > 50:
        anchor = anchor[:50].rstrip('-')

    return anchor

def file_path_to_url(file_path):
    """
    Convert file path to GitBook page URL.
    Example: "interactive-studio/effects/change-avatar.md"
          -> "https://prtls.gitbook.io/portals-building-guide/interactive-studio/effects/change-avatar"
    """
    # Remove .md extension
    page_path = file_path.replace('.md', '')

    # Build full URL
    return f"{GITBOOK_BASE}/{page_path}"

def main():
    # Read diff from stdin
    diff_text = sys.stdin.read()

    # Extract headers
    headers = extract_headers_from_diff(diff_text)

    if not headers:
        print("No section links available (no headers detected in diff)")
        return

    # Generate URL mapping
    print("Available section links:")

    # Track seen files to deduplicate (use first header per file)
    seen_files = set()

    for file_path, header_text in headers:
        if file_path in seen_files:
            continue
        seen_files.add(file_path)

        page_url = file_path_to_url(file_path)
        anchor = text_to_anchor(header_text)

        if anchor:
            full_url = f"{page_url}#{anchor}"
            print(f"- {file_path} → {header_text} → {full_url}")
        else:
            # Fallback to page-level link if anchor generation fails
            print(f"- {file_path} → {page_url}")

if __name__ == '__main__':
    main()
```

**Step 3: Make script executable**

Run: `chmod +x .github/scripts/generate-gitbook-urls.py`
Expected: Script is executable

**Step 4: Test script with sample diff**

Create test file:
```bash
cat > /tmp/test-diff.txt <<'EOF'
diff --git a/docs/test.md b/docs/test.md
index abc123..def456 100644
--- a/docs/test.md
+++ b/docs/test.md
@@ -1,3 +1,6 @@
 # Test Page

+## Configuration Settings
+
 Some content here.
EOF
```

Run: `cat /tmp/test-diff.txt | .github/scripts/generate-gitbook-urls.py`
Expected output:
```
Available section links:
- docs/test.md → Configuration Settings → https://prtls.gitbook.io/portals-building-guide/docs/test#configuration-settings
```

**Step 5: Commit**

```bash
git add .github/scripts/generate-gitbook-urls.py
git commit -m "feat: add GitBook URL generation script

- Extracts headers from git diffs
- Generates GitBook URLs with section anchors
- Handles special characters in header text
- Falls back to page-level URLs when needed

Co-Authored-By: Claude Sonnet 4.5 <noreply@anthropic.com>"
```

---

## Task 2: Add URL Extraction Step to Workflow

**Files:**
- Modify: `.github/workflows/gitbook-to-discord.yml:27-39`

**Step 1: Add new workflow step after "Get changed files"**

Insert after line 38 (after the "Get changed files" step):

```yaml
      - name: Generate GitBook URLs
        id: urls
        run: |
          # Generate URL mapping from diff
          if [[ -n "${{ github.event.before }}" && -n "${{ github.event.after }}" ]]; then
            git diff ${{ github.event.before }} ${{ github.event.after }} | python3 .github/scripts/generate-gitbook-urls.py > urls.txt
          else
            echo "No section links available" > urls.txt
          fi
          # Escape newlines for GitHub Actions outputs
          URLS=$(sed ':a;N;$!ba;s/\n/\\n/g' urls.txt)
          echo "mapping=$URLS" >> $GITHUB_OUTPUT
```

**Step 2: Verify YAML syntax**

Run: `python3 -c "import yaml; yaml.safe_load(open('.github/workflows/gitbook-to-discord.yml'))"`
Expected: No errors (validates YAML syntax)

**Step 3: Commit**

```bash
git add .github/workflows/gitbook-to-discord.yml
git commit -m "feat: add URL generation step to workflow

- Extract headers and generate URLs after getting changed files
- Pass URL mapping to next step via GitHub Actions output
- Handle cases with no valid diff

Co-Authored-By: Claude Sonnet 4.5 <noreply@anthropic.com>"
```

---

## Task 3: Update AI Prompt with URL Mapping

**Files:**
- Modify: `.github/workflows/gitbook-to-discord.yml:40-99`

**Step 1: Add URLS environment variable**

Modify the "Generate AI summary" step to include URLS in env section (after line 45):

```yaml
      - name: Generate AI summary
        id: summary
        env:
          OPENAI_API_KEY: ${{ secrets.OPENAI_API_KEY }}
          DIFF: ${{ steps.diff.outputs.diff }}
          FILES: ${{ steps.files.outputs.files }}
          URLS: ${{ steps.urls.outputs.mapping }}
```

**Step 2: Update system prompt**

Modify the system prompt (line 49) to add link instructions:

Replace:
```
"You write public release notes for a GitBook documentation site (Markdown pages). Convert git changes into a concise, user‑facing 'Building Guide Update'. Rules:\n- Treat each *.md as a GitBook page, not a file.\n- Prefer page titles over filenames: use the first '# ' heading seen in the diff; otherwise derive a human title from the filename (drop '.md', replace '-'/'_' with spaces, Title Case).\n- Group items under sections: Added, Updated, Renamed, Removed (omit empty sections).\n- Focus on what changed for readers (e.g., 'Added fee wallet setting to Token Swap page'), not raw paths or code.\n- Be concise: 3–8 bullets total, under ~800 characters.\n- Do NOT wrap your answer in any quotation marks, code fences, or blockquotes.\n- Do NOT use '# ' headings; use bold for section names instead (e.g., **Added**, **Updated**), and do not restate the overall title.\n- If details are unclear, say 'Minor edits to existing pages.'\n"
```

With:
```
"You write public release notes for a GitBook documentation site (Markdown pages). Convert git changes into a concise, user‑facing 'Building Guide Update'. Rules:\n- Treat each *.md as a GitBook page, not a file.\n- Prefer page titles over filenames: use the first '# ' heading seen in the diff; otherwise derive a human title from the filename (drop '.md', replace '-'/'_' with spaces, Title Case).\n- Group items under sections: Added, Updated, Renamed, Removed (omit empty sections).\n- Focus on what changed for readers (e.g., 'Added fee wallet setting to Token Swap page'), not raw paths or code.\n- Be concise: 3–8 bullets total, under ~800 characters.\n- For each bullet point, append ' → [View](url)' using the GitBook section links provided. Match each change to the most relevant file and section. If multiple sections in one file changed, pick the most specific one per bullet. If no link is available for a bullet, you may omit the View link.\n- Do NOT wrap your answer in any quotation marks, code fences, or blockquotes.\n- Do NOT use '# ' headings; use bold for section names instead (e.g., **Added**, **Updated**), and do not restate the overall title.\n- If details are unclear, say 'Minor edits to existing pages.'\n"
```

**Step 3: Add URLs to user message**

Modify the user message (line 50) to include URL mapping:

Replace:
```
--arg user "Changed files (name-status):\n$FILES\n\nUnified diff (may be truncated):\n$DIFF"
```

With:
```
--arg user "Changed files (name-status):\n$FILES\n\nUnified diff (may be truncated):\n$DIFF\n\n$URLS"
```

**Step 4: Commit**

```bash
git add .github/workflows/gitbook-to-discord.yml
git commit -m "feat: enhance AI prompt with GitBook URLs

- Add URLS environment variable to AI summary step
- Update system prompt to instruct AI to append View links
- Include URL mapping in user message context
- AI will match changes to section links automatically

Co-Authored-By: Claude Sonnet 4.5 <noreply@anthropic.com>"
```

---

## Task 4: Manual Testing

**Files:**
- Test: Workflow execution on real push

**Step 1: Create test documentation change**

```bash
cd docs
cat >> test-page.md <<'EOF'
# Test Page for URL Generation

## New Configuration Section

This is a test to verify GitBook URL generation.

### Subsection

More details here.
EOF

git add test-page.md
git commit -m "test: add test page for URL generation"
```

**Step 2: Push to trigger workflow**

Run: `git push origin feature/gitbook-discord-links`
Expected: GitHub Actions workflow triggers

**Step 3: Monitor workflow execution**

Run: `gh run list --branch feature/gitbook-discord-links --limit 1`
Expected: Workflow shows as running or completed

**Step 4: Check workflow logs**

Run: `gh run view --log`
Expected logs to show:
- URL generation step output with detected headers
- AI summary with ` → [View](url)` appended to bullets
- No errors in workflow execution

**Step 5: Verify Discord message (if webhook configured)**

Manual step: Check Discord channel for notification
Expected: Message contains clickable links in format:
```
**Added**
- New test page with configuration details → [View](https://prtls.gitbook.io/portals-building-guide/docs/test-page#new-configuration-section)
```

**Step 6: Verify GitBook URL works**

Manual step: Click the link in Discord
Expected: Browser opens to correct GitBook page and scrolls to section

**Step 7: Clean up test file**

```bash
git rm docs/test-page.md
git commit -m "test: remove test page"
```

---

## Task 5: Edge Case Testing

**Files:**
- Test: Various diff scenarios

**Step 1: Test with special characters in headers**

```bash
cat > docs/special-chars.md <<'EOF'
# Special Characters Test

## Setup & Configuration

## Feature: Token Swap

## User's Guide (Advanced)
EOF

git add docs/special-chars.md
git commit -m "test: headers with special characters"
```

**Step 2: Test URL generation locally**

Run: `git diff HEAD~1 HEAD | python3 .github/scripts/generate-gitbook-urls.py`
Expected output showing sanitized anchors:
```
Available section links:
- docs/special-chars.md → Setup & Configuration → https://prtls.gitbook.io/portals-building-guide/docs/special-chars#setup-and-configuration
```

**Step 3: Test with no headers in diff**

```bash
echo "Just adding content without headers." >> docs/special-chars.md
git add docs/special-chars.md
git commit -m "test: content change without headers"
```

Run: `git diff HEAD~1 HEAD | python3 .github/scripts/generate-gitbook-urls.py`
Expected: "No section links available (no headers detected in diff)"

**Step 4: Test with non-markdown files**

```bash
echo "test" > test.txt
git add test.txt
git commit -m "test: non-markdown file"
```

Run: `git diff HEAD~1 HEAD | python3 .github/scripts/generate-gitbook-urls.py`
Expected: No output or "No section links available" (script ignores non-.md files)

**Step 5: Clean up test files**

```bash
git rm docs/special-chars.md test.txt
git commit -m "test: clean up edge case test files"
```

**Step 6: Review all edge cases passed**

Manual verification:
- ✓ Special characters sanitized correctly
- ✓ Missing headers handled gracefully
- ✓ Non-markdown files ignored
- ✓ AI receives proper fallback message

---

## Task 6: Documentation

**Files:**
- Create: `docs/github-actions-workflow.md`

**Step 1: Document the workflow enhancement**

Create `docs/github-actions-workflow.md`:

```markdown
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
```

**Step 2: Commit documentation**

```bash
git add docs/github-actions-workflow.md
git commit -m "docs: document GitBook to Discord workflow

- Explain URL generation process
- Document AI integration
- Provide testing instructions
- Include error handling details

Co-Authored-By: Claude Sonnet 4.5 <noreply@anthropic.com>"
```

---

## Success Criteria

✅ URL generation script extracts headers from diffs correctly
✅ GitBook URLs formatted with proper anchors
✅ Workflow step integrated without breaking existing functionality
✅ AI prompt includes URL mapping and generates links
✅ Discord messages contain clickable ` → [View](url)` links
✅ Edge cases handled (no headers, special chars, non-markdown files)
✅ Documentation complete

## Verification Commands

After implementation:

```bash
# Verify workflow syntax
python3 -c "import yaml; yaml.safe_load(open('.github/workflows/gitbook-to-discord.yml'))"

# Test URL generation with sample diff
git diff HEAD~3 HEAD | python3 .github/scripts/generate-gitbook-urls.py

# Check recent workflow runs
gh run list --branch feature/gitbook-discord-links --limit 5

# View latest workflow logs
gh run view --log
```
