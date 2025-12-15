---
name: markdown-formatter
description: Format and polish markdown documents. Use when cleaning up markdown files, fixing lint errors, adding frontmatter metadata, converting internal links, removing duplicates, or improving document readability. Covers rumdl integration, Obsidian-style frontmatter, markdown link conversion, deduplication strategies, and readability best practices.
---

# Markdown Formatter

## Purpose

Automatically format, clean, and polish markdown documents to ensure consistency, readability, and proper structure. This skill integrates multiple formatting tools and best practices to transform messy markdown into clean, professional documentation.

## When to Use This Skill

Automatically activates when you mention:
- Formatting or cleaning markdown files
- Fixing markdown lint errors
- Adding frontmatter or metadata
- Converting internal links
- Removing duplicate content
- Improving document readability
- Polishing or prettifying markdown
- Document cleanup or organization
- rumdl, markdownlint, or markdown tools

---

## 5-Step Workflow

When formatting a markdown document, follow this systematic approach:

### 1. Run rumdl Lint Check

**Install and run rumdl:**

```bash
# Install (choose one)
cargo install rumdl
pip install rumdl
brew install rumdl

# Check for errors
rumdl check path/to/document.md

# Auto-fix
rumdl check --fix path/to/document.md
```

**Common auto-fixes:**
- Heading hierarchy (MD001, MD003)
- List formatting (MD004, MD005, MD007)
- Whitespace (MD009, MD010, MD012)
- Code block language tags (MD040)
- Blank lines around elements (MD022, MD031, MD032)

**For complete rule reference:** See [RUMDL_RULES.md](resources/RUMDL_RULES.md) (57 rules)

### 2. Add Obsidian-Style Frontmatter

**Basic template:**

```yaml
---
title: Document Title
created: 2024-12-16
updated: 2024-12-16
tags: [tag1, tag2]
category: Documentation
status: Draft | Review | Published
---
```

**Key fields:**
- `title`: Human-readable title
- `created`/`updated`: Dates (YYYY-MM-DD)
- `tags`: Array for categorization
- `status`: Lifecycle status
- `aliases`: Alternative names (Obsidian)

**For document-type templates:** See [FRONTMATTER_TEMPLATES.md](resources/FRONTMATTER_TEMPLATES.md)
- Documentation, API Reference, Tutorial
- Research, Meeting Notes, Blog Post
- Changelog, README, Specification

### 3. Convert Internal Links

**Transformations:**

```markdown
# Wiki-style → Markdown
[[document]] → [document](document.md)
[[doc|Custom Text]] → [Custom Text](doc.md)

# Bare URLs → Links
https://example.com → [example.com](https://example.com)

# Section links
[[doc#section]] → [doc](doc.md#section)
[[#section]] → [section](#section)
```

**Link text best practices:**
- Use descriptive text (not "click here")
- Keep concise (2-5 words)
- Make scannable

**For advanced patterns:** See [LINK_CONVERSION.md](resources/LINK_CONVERSION.md)

### 4. Remove Duplicate Content

**Strategies:**

**A. Delete exact duplicates** (100% match)
```markdown
# Before: Two identical sections
# After: Keep one, delete the other
```

**B. Consolidate near-duplicates** (>80% similar)
```markdown
# Before: Similar content in two places
# After: Merge into one comprehensive section
```

**C. Create single source + links**
```markdown
# Before: Repeated information
## Section A: Rate limit is 100/hour
## Section B: Remember 100/hour limit

# After: Single source of truth
## Rate Limiting
Free tier: 100 requests/hour

## Section A
See [Rate Limiting](#rate-limiting)
```

**For detection algorithms:** See [DEDUPLICATION_STRATEGIES.md](resources/DEDUPLICATION_STRATEGIES.md)

### 5. Apply Readability Best Practices

**Quick checklist:**
- [ ] One H1 heading only
- [ ] Sequential heading hierarchy (no skipping)
- [ ] Blank line between all elements
- [ ] Paragraphs: 2-4 sentences max
- [ ] Consistent list markers (all `-` or all `*`)
- [ ] Code blocks have language tags
- [ ] Line length ≤ 120 characters
- [ ] No trailing whitespace

**For complete guide:** See [READABILITY_GUIDE.md](resources/READABILITY_GUIDE.md)

---

## Quick Reference

### Complete Workflow Command

```bash
# 1. Run lint check
rumdl check --fix document.md

# 2-4. Manual edits (frontmatter, links, duplicates)

# 5. Final validation
rumdl check document.md
```

### Batch Processing

```bash
# Format all markdown files
find ./docs -name "*.md" -exec rumdl check --fix {} \;

# Pre-commit hook
echo 'rumdl check --fix **/*.md' > .git/hooks/pre-commit
chmod +x .git/hooks/pre-commit
```

### Configuration File

**Create `.rumdl.toml`:**

```toml
# Disable specific rules
disabled_rules = ["MD013", "MD024"]

# Settings
line_length = 120
heading_style = "atx"
list_marker = "-"
code_fence = "```"
emphasis_style = "asterisk"
```

---

## Common Tasks

### Fix Heading Hierarchy

```bash
# rumdl detects and auto-fixes:
# - Skipped levels (H1 → H3)
# - Multiple H1s
# - Inconsistent styles
rumdl check --fix doc.md
```

### Add Frontmatter to Multiple Files

```bash
# Use a script or manual edit
for file in docs/*.md; do
  # Add frontmatter if not present
  if ! grep -q "^---" "$file"; then
    cat frontmatter-template.md "$file" > temp && mv temp "$file"
  fi
done
```

### Convert All Wiki Links

See [LINK_CONVERSION.md](resources/LINK_CONVERSION.md) for regex patterns and scripts.

### Find Duplicates

See [DEDUPLICATION_STRATEGIES.md](resources/DEDUPLICATION_STRATEGIES.md) for detection algorithms.

---

## Reference Files

For detailed information:

- **[READABILITY_GUIDE.md](resources/READABILITY_GUIDE.md)** - Complete readability best practices
  - Document structure, heading guidelines, paragraph practices
  - List formatting, code blocks, links, tables
  - Visual elements, line length, whitespace, typography

- **[RUMDL_RULES.md](resources/RUMDL_RULES.md)** - All 57 lint rules explained
  - Heading rules (MD001-MD003, MD018-MD026, MD041, MD043)
  - List rules (MD004-MD007, MD027-MD032)
  - Whitespace rules (MD009-MD012, MD022-MD023, MD031, MD037-MD038)
  - Code block rules (MD014, MD031, MD040, MD046-MD048)
  - Link rules (MD034, MD039, MD042, MD051-MD053)
  - Configuration examples

- **[FRONTMATTER_TEMPLATES.md](resources/FRONTMATTER_TEMPLATES.md)** - Document-type templates
  - Basic, Documentation, API Reference
  - Tutorial, Research, Meeting Notes
  - Blog Post, Changelog, README, Specification
  - Custom fields reference, validation guide

- **[LINK_CONVERSION.md](resources/LINK_CONVERSION.md)** - Advanced link patterns
  - Wiki-style, Obsidian embeds, bare URLs
  - File references, section links
  - Regex patterns, conversion functions
  - Batch conversion scripts

- **[DEDUPLICATION_STRATEGIES.md](resources/DEDUPLICATION_STRATEGIES.md)** - Content deduplication
  - Detection methods (exact, near, conceptual)
  - Consolidation patterns
  - Automated detection scripts
  - Manual review checklist

---

## Integration Examples

### VS Code

```json
// .vscode/settings.json
{
  "rumdl.enable": true,
  "editor.formatOnSave": true,
  "[markdown]": {
    "editor.defaultFormatter": "rumdl"
  }
}
```

### GitHub Actions

```yaml
# .github/workflows/lint-markdown.yml
name: Lint Markdown
on: [push, pull_request]
jobs:
  lint:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - run: pip install rumdl
      - run: rumdl check ./docs
```

### Pre-commit Hook

```bash
#!/bin/bash
# .git/hooks/pre-commit

# Get staged markdown files
FILES=$(git diff --cached --name-only --diff-filter=ACM | grep '\.md$')

if [ -n "$FILES" ]; then
  echo "Running rumdl on staged markdown files..."
  echo "$FILES" | xargs rumdl check --fix

  # Re-stage fixed files
  echo "$FILES" | xargs git add
fi
```

---

## Tips & Best Practices

### Start Simple

Don't over-engineer frontmatter for simple documents. Start with basic template:

```yaml
---
title: My Document
created: 2024-12-16
tags: []
---
```

Add fields as needed.

### Incremental Formatting

Format documents incrementally:
1. First pass: rumdl auto-fix
2. Second pass: Frontmatter
3. Third pass: Links
4. Fourth pass: Duplicates
5. Final pass: Readability

### Test Changes

Before mass-formatting:
1. Test on one file
2. Review changes
3. Adjust configuration
4. Run on all files

### Preserve Intent

When removing duplicates or reformatting:
- Don't change meaning
- Preserve important context
- Keep intentional repetition (emphasis)
- Verify links still work

---

## Troubleshooting

### rumdl Not Installed

```bash
# Check installation
which rumdl
rumdl --version

# Install if missing
cargo install rumdl  # or pip/brew
```

### False Positives

Disable specific rules in `.rumdl.toml`:

```toml
disabled_rules = [
  "MD013",  # Line length (if you want long lines)
  "MD024",  # Duplicate headings (often false positive)
  "MD033"   # Inline HTML (sometimes necessary)
]
```

### Links Break After Conversion

- Use relative paths for internal links
- Verify file names match exactly
- Check for spaces/special characters
- Test all links after conversion

### Frontmatter Syntax Errors

Validate YAML:
```bash
# Extract and validate frontmatter
sed -n '/^---$/,/^---$/p' doc.md | yq eval
```

Common issues:
- Unquoted colons in values
- Wrong date format (use YYYY-MM-DD)
- Arrays need brackets: `[item1, item2]`

---

**Skill Status**: COMPLETE ✅
**Line Count**: <500 (following 500-line rule) ✅
**Progressive Disclosure**: 5 reference files for detailed info ✅
