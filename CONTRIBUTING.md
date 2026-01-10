# Contributing to Portals Building Guide

Thank you for your interest in contributing to the Portals Building Guide! This repo hosts the markdown source for our GitBook documentation on building interactive spaces in Portals. We welcome contributions from the community to keep the guide accurate, up to date, and comprehensive.

## Types of Contributions
- **Typos and Fixes**: Correct spelling, grammar, or broken links.
- **Content Additions**: New sections, examples, or "How To" guides (e.g., advanced tutorials).
- **Improvements**: Add images, screenshots, or clarifications to existing pages.
- **Updates**: Reflect new Portals features or fix outdated info.
- **Translations**: If interested in multi-language support.

We do not accept spam, off-topic content, or changes that alter the guide's core focus.

## How to Contribute
1. **Fork the Repository**:
   - Go to https://github.com/busportals/Portals-Building-Guide.
   - Click the "Fork" button in the top-right corner to create your own copy.

2. **Clone Your Fork**:
   - Clone the forked repo to your local machine:
     ```sh
     git clone https://github.com/YOUR-USERNAME/Portals-Building-Guide.git
     ```
   - Navigate into the directory:
     ```sh
     cd Portals-Building-Guide
     ```

3. **Create a Branch**:
   - Create a new branch for your changes (use a descriptive name, e.g., `fix-typo-in-triggers`):
     ```sh
     git checkout -b your-branch-name
     ```

4. **Make Your Changes**:
   - Edit markdown files using a text editor (e.g., VS Code).
   - Follow the existing style: use headers (`#` for H1, `##` for H2), bullet points, and reference images from `.gitbook/assets`.
   - If adding images, place them in `.gitbook/assets` and link them relatively (e.g., `![Alt text](.gitbook/assets/image.png)`).
   - Test locally: if you have GitBook installed (`npm install -g gitbook-cli`), run `gitbook serve` to preview.

5. **Commit Your Changes**:
   - Stage and commit with a clear message:
     ```sh
     git add .
     git commit -m "Brief description of changes"
     ```

6. **Push to Your Fork**:
   - Push the branch to GitHub:
     ```sh
     git push origin your-branch-name
     ```

7. **Open a Pull Request (PR)**:
   - Go back to your forked repo on GitHub.
   - Click "Compare & pull request" (or go to the original repo and click "New pull request").
   - Provide a title and description: explain what you changed, why, and reference any issues (e.g., "Fixes #issue-number").
   - Submit the PR. We'll review it soon.

## Guidelines
- Keep changes focused: one PR per feature or fix.
- Ensure markdown is valid (no broken links or formatting).
- If proposing major additions, open an issue first to discuss.
- Be respectful in comments and follow the [Code of Conduct](https://docs.github.com/en/site-policy/github-terms/github-community-code-of-conduct) (add one if needed).

## Questions?
Open an issue on the repo or reach out via Portals [Discord](https://discord.com/invite/portals).

Thanks for helping improve the guide!
