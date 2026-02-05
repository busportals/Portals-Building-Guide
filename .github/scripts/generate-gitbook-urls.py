#!/usr/bin/env python3
"""
Generate GitBook URLs with section anchors from git diff output.
Reads diff from stdin, outputs URL mapping to stdout.
Only generates links for pages listed in SUMMARY.md (i.e. published in GitBook).
"""
import sys
import re
import os

GITBOOK_BASE = "https://prtls.gitbook.io/portals-building-guide"


def get_published_pages():
    """
    Parse SUMMARY.md to extract the set of file paths that are published in GitBook.
    Returns a set of relative paths like {'interactive-studio/overview.md', 'README.md', ...}
    """
    # SUMMARY.md is at the repo root; this script runs from repo root in CI
    summary_path = os.path.join(os.path.dirname(__file__), '..', '..', 'SUMMARY.md')
    summary_path = os.path.normpath(summary_path)

    published = set()
    try:
        with open(summary_path, 'r') as f:
            for line in f:
                # Match markdown links like [Title](path/to/file.md)
                for match in re.finditer(r'\[.*?\]\((.+?\.md)\)', line):
                    published.add(match.group(1))
    except FileNotFoundError:
        # If SUMMARY.md is missing, don't filter (allow all)
        return None

    return published

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

    # Get the set of pages published in GitBook
    published_pages = get_published_pages()

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

        # Skip files not published in GitBook (not listed in SUMMARY.md)
        if published_pages is not None and file_path not in published_pages:
            continue

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
