# rumdl Lint Rules Reference

Complete reference for all 57 rumdl markdown linting rules.

## Table of Contents

- [Rule Categories](#rule-categories)
- [Heading Rules (MD001-MD003, MD018-MD019, MD020-MD024, MD026, MD041, MD043)](#heading-rules)
- [List Rules (MD004-MD007, MD027-MD030, MD032)](#list-rules)
- [Whitespace Rules (MD009-MD012, MD022-MD023, MD031, MD037-MD038, MD044)](#whitespace-rules)
- [Code Block Rules (MD014, MD031, MD040, MD046-MD048)](#code-block-rules)
- [Link Rules (MD034, MD039, MD042, MD051-MD053)](#link-rules)
- [Line Rules (MD013)](#line-rules)
- [Emphasis Rules (MD036-MD037, MD049-MD050)](#emphasis-rules)
- [Other Rules](#other-rules)

---

## Rule Categories

| Category | Count | Rules |
|----------|-------|-------|
| **Headings** | 13 | MD001, MD002, MD003, MD018-MD024, MD026, MD041, MD043 |
| **Lists** | 8 | MD004-MD007, MD027-MD030, MD032 |
| **Whitespace** | 11 | MD009-MD012, MD022-MD023, MD031, MD037-MD038, MD044 |
| **Code Blocks** | 5 | MD014, MD031, MD040, MD046-MD048 |
| **Links** | 5 | MD034, MD039, MD042, MD051-MD053 |
| **Line Length** | 1 | MD013 |
| **Emphasis** | 4 | MD036-MD037, MD049-MD050 |
| **Other** | 10 | MD025, MD033, MD035, MD045, MD054-MD057 |

---

## Heading Rules

### MD001 - Heading levels should increment by one

**What it checks**: Ensures heading hierarchy is sequential (no skipping levels).

❌ **Bad**:
```markdown
# H1
### H3 (skipped H2)
```

✅ **Good**:
```markdown
# H1
## H2
### H3
```

**Auto-fix**: Yes

---

### MD002 - First heading should be H1

**What it checks**: Document starts with an H1 heading.

❌ **Bad**:
```markdown
## Introduction
```

✅ **Good**:
```markdown
# Document Title
## Introduction
```

**Auto-fix**: No (requires manual decision)

---

### MD003 - Heading style

**What it checks**: Consistent heading style throughout document.

**Styles**:
- **ATX**: `# Heading` (recommended)
- **Setext**: Underlined with `===` or `---`
- **Consistent**: Whatever you choose

❌ **Bad** (mixed):
```markdown
# ATX Style

Setext Style
============
```

✅ **Good** (consistent ATX):
```markdown
# Heading 1
## Heading 2
### Heading 3
```

**Auto-fix**: Yes

**Config**:
```toml
heading_style = "atx"  # or "setext" or "consistent"
```

---

### MD018 - No space after hash on ATX heading

❌ **Bad**:
```markdown
#Heading without space
```

✅ **Good**:
```markdown
# Heading with space
```

**Auto-fix**: Yes

---

### MD019 - Multiple spaces after hash

❌ **Bad**:
```markdown
#  Heading with extra spaces
```

✅ **Good**:
```markdown
# Heading with one space
```

**Auto-fix**: Yes

---

### MD020 - No space inside hashes on closed ATX heading

❌ **Bad**:
```markdown
#Heading#
```

✅ **Good**:
```markdown
# Heading #
```

**Auto-fix**: Yes

---

### MD021 - Multiple spaces inside hashes on closed ATX

❌ **Bad**:
```markdown
#  Heading  #
```

✅ **Good**:
```markdown
# Heading #
```

**Auto-fix**: Yes

---

### MD022 - Headings should be surrounded by blank lines

❌ **Bad**:
```markdown
# Heading
Immediately followed by text
```

✅ **Good**:
```markdown
# Heading

Text with blank line before
```

**Auto-fix**: Yes

---

### MD023 - Headings must start at the beginning of the line

❌ **Bad**:
```markdown
  # Heading with leading spaces
```

✅ **Good**:
```markdown
# Heading at start of line
```

**Auto-fix**: Yes

---

### MD024 - Multiple headings with the same content

**What it checks**: Duplicate heading text (can indicate poor structure).

❌ **Warning**:
```markdown
## Details
Some content
## Details (duplicate)
```

✅ **Better**:
```markdown
## API Details
## Configuration Details
```

**Auto-fix**: No (requires manual renaming)

**Note**: This is often a false positive. Configure to allow duplicates:
```toml
disabled_rules = ["MD024"]
```

---

### MD026 - Trailing punctuation in heading

❌ **Bad**:
```markdown
## Introduction:
## What is it?
## Getting Started!
```

✅ **Good**:
```markdown
## Introduction
## What is it
## Getting Started
```

**Exception**: Question marks in FAQ sections may be acceptable.

**Auto-fix**: Yes

---

### MD041 - First line in file should be H1

❌ **Bad**:
```markdown
Some text

# Heading
```

✅ **Good**:
```markdown
# Heading

Some text
```

**Auto-fix**: No

---

### MD043 - Required heading structure

**What it checks**: Enforces a specific heading structure (when configured).

**Config**:
```toml
[MD043]
headings = ["# Title", "## Introduction", "## Body", "## Conclusion"]
```

**Auto-fix**: No (structural decision)

---

## List Rules

### MD004 - Unordered list style

**What it checks**: Consistent list markers.

**Styles**:
- **Dash**: `-`
- **Asterisk**: `*`
- **Plus**: `+`
- **Consistent**: Pick one

❌ **Bad** (mixed):
```markdown
- Item 1
* Item 2
+ Item 3
```

✅ **Good** (consistent):
```markdown
- Item 1
- Item 2
- Item 3
```

**Auto-fix**: Yes

**Config**:
```toml
list_marker = "-"  # or "*" or "+"
```

---

### MD005 - Inconsistent indentation for list items at same level

❌ **Bad**:
```markdown
- Item 1
  - Sub-item
    - Sub-sub-item
  - Another sub (inconsistent indent)
```

✅ **Good**:
```markdown
- Item 1
  - Sub-item
    - Sub-sub-item
  - Another sub
```

**Auto-fix**: Yes

---

### MD006 - Consider starting bulleted lists at beginning of line

❌ **Bad**:
```markdown
 - Indented list
```

✅ **Good**:
```markdown
- List at start of line
```

**Auto-fix**: Yes

---

### MD007 - Unordered list indentation

**What it checks**: Consistent indentation (2 or 4 spaces).

**Config**:
```toml
[MD007]
indent = 2  # or 4
```

✅ **Good** (2 spaces):
```markdown
- Item
  - Sub-item
```

✅ **Good** (4 spaces):
```markdown
- Item
    - Sub-item
```

**Auto-fix**: Yes

---

### MD027 - Multiple spaces after blockquote symbol

❌ **Bad**:
```markdown
>  Quote with extra spaces
```

✅ **Good**:
```markdown
> Quote with one space
```

**Auto-fix**: Yes

---

### MD028 - Blank line inside blockquote

❌ **Bad**:
```markdown
> Quote line 1

> Quote line 2 (should be continuous)
```

✅ **Good**:
```markdown
> Quote line 1
> Quote line 2
```

**Auto-fix**: Yes

---

### MD029 - Ordered list item prefix

**What it checks**: Consistent numbering style.

**Styles**:
- **Ordered**: `1. 2. 3.`
- **One**: `1. 1. 1.` (auto-numbering)

✅ **Good** (ordered):
```markdown
1. First
2. Second
3. Third
```

✅ **Good** (one):
```markdown
1. First
1. Second
1. Third
```

**Auto-fix**: Yes

---

### MD030 - Spaces after list markers

**What it checks**: Consistent spacing after markers.

**Config**:
```toml
[MD030]
ul_single = 1  # spaces after unordered marker
ol_single = 1  # spaces after ordered marker
```

✅ **Good**:
```markdown
- Item (1 space)
1. Item (1 space)
```

**Auto-fix**: Yes

---

### MD032 - Lists should be surrounded by blank lines

❌ **Bad**:
```markdown
Some text
- List item
- Another item
More text
```

✅ **Good**:
```markdown
Some text

- List item
- Another item

More text
```

**Auto-fix**: Yes

---

## Whitespace Rules

### MD009 - Trailing spaces

**What it checks**: No trailing whitespace at end of lines.

❌ **Bad**:
```markdown
Line with trailing spaces
```

✅ **Good**:
```markdown
Line without trailing spaces
```

**Exception**: Two trailing spaces for hard line break (not recommended).

**Auto-fix**: Yes

---

### MD010 - Hard tabs

**What it checks**: No tab characters (use spaces).

❌ **Bad**:
```markdown
	Indented with tab
```

✅ **Good**:
```markdown
    Indented with spaces
```

**Auto-fix**: Yes

**Config**:
```toml
[MD010]
code_blocks = false  # allow tabs in code blocks
```

---

### MD011 - Reversed link syntax

❌ **Bad**:
```markdown
(text)[https://example.com]
```

✅ **Good**:
```markdown
[text](https://example.com)
```

**Auto-fix**: Yes

---

### MD012 - Multiple consecutive blank lines

❌ **Bad**:
```markdown
Line 1


Line 2 (too many blank lines)
```

✅ **Good**:
```markdown
Line 1

Line 2 (one blank line)
```

**Auto-fix**: Yes

**Config**:
```toml
[MD012]
maximum = 1  # max consecutive blank lines
```

---

### MD022 - Headings surrounded by blank lines

(See Heading Rules section above)

---

### MD023 - Headings at start of line

(See Heading Rules section above)

---

### MD031 - Fenced code blocks surrounded by blank lines

❌ **Bad**:
```markdown
Text before
```python
code
```
Text after
```

✅ **Good**:
```markdown
Text before

```python
code
```

Text after
```

**Auto-fix**: Yes

---

### MD037 - Spaces inside emphasis markers

❌ **Bad**:
```markdown
** bold **
* italic *
```

✅ **Good**:
```markdown
**bold**
*italic*
```

**Auto-fix**: Yes

---

### MD038 - Spaces inside code spans

❌ **Bad**:
```markdown
` code `
```

✅ **Good**:
```markdown
`code`
```

**Auto-fix**: Yes

---

### MD044 - Proper names should be capitalized

**What it checks**: Enforces capitalization of configured proper names.

**Config**:
```toml
[MD044]
names = ["JavaScript", "GitHub", "API"]
```

**Auto-fix**: Yes (if configured)

---

## Code Block Rules

### MD014 - Dollar signs used before commands

❌ **Bad**:
```markdown
```bash
$ npm install
$ npm start
```
```

✅ **Good**:
```markdown
```bash
npm install
npm start
```
```

**Why**: Dollar signs prevent copy-paste.

**Auto-fix**: Yes

---

### MD031 - Fenced code surrounded by blank lines

(See Whitespace Rules section above)

---

### MD040 - Fenced code blocks should have language

❌ **Bad**:
```markdown
```
code without language
```
```

✅ **Good**:
```markdown
```javascript
code with language
```
```

**Auto-fix**: No (requires manual language specification)

**Why**: Enables syntax highlighting and better accessibility.

---

### MD046 - Code block style

**What it checks**: Consistent code block style.

**Styles**:
- **Fenced**: ` ``` ` (recommended)
- **Indented**: 4 spaces
- **Consistent**: Pick one

✅ **Good** (fenced):
```markdown
```python
code
```
```

✅ **Good** (indented):
```markdown
    code
```

**Auto-fix**: Yes

**Config**:
```toml
code_block_style = "fenced"  # or "indented"
```

---

### MD047 - Files should end with single newline

❌ **Bad**:
```markdown
Last line with no newline character
```

✅ **Good**:
```markdown
Last line with newline character
<newline>
```

**Auto-fix**: Yes

---

### MD048 - Code fence style

**What it checks**: Consistent fence characters.

**Styles**:
- **Backtick**: ` ``` `
- **Tilde**: `~~~`
- **Consistent**: Pick one

✅ **Good** (backticks):
```markdown
```python
code
```
```

**Auto-fix**: Yes

**Config**:
```toml
code_fence = "```"  # or "~~~"
```

---

## Link Rules

### MD034 - Bare URL used

❌ **Bad**:
```markdown
See https://example.com for details
```

✅ **Good**:
```markdown
See [example](https://example.com) for details
```

Or:
```markdown
See <https://example.com> for details
```

**Auto-fix**: No (requires descriptive text)

---

### MD039 - Spaces inside link text

❌ **Bad**:
```markdown
[ text ](url)
```

✅ **Good**:
```markdown
[text](url)
```

**Auto-fix**: Yes

---

### MD042 - No empty links

❌ **Bad**:
```markdown
[](url)
[text]()
```

✅ **Good**:
```markdown
[text](url)
```

**Auto-fix**: No

---

### MD051 - Link fragments reference existing headers

**What it checks**: Anchor links point to actual headings.

❌ **Bad**:
```markdown
[Link](#nonexistent-section)
```

✅ **Good**:
```markdown
## Existing Section

[Link](#existing-section)
```

**Auto-fix**: No

---

### MD052 - Reference links/images need blank line

❌ **Bad**:
```markdown
Text
[ref]: url
```

✅ **Good**:
```markdown
Text

[ref]: url
```

**Auto-fix**: Yes

---

### MD053 - Link/image reference definitions should be needed

**What it checks**: No unused reference definitions.

❌ **Bad**:
```markdown
[unused]: https://example.com
```

✅ **Good**:
```markdown
[used]: https://example.com

See [used] for details.
```

**Auto-fix**: No (requires manual cleanup)

---

## Line Rules

### MD013 - Line length

**What it checks**: Lines don't exceed configured length.

❌ **Bad**:
```markdown
This is a very long line that exceeds the maximum line length and should be broken into multiple lines for better readability in source code.
```

✅ **Good**:
```markdown
This is a line that fits within the maximum length.
Or broken across multiple lines.
```

**Auto-fix**: No (requires manual reformatting)

**Config**:
```toml
[MD013]
line_length = 120
code_blocks = false  # exclude code blocks
tables = false       # exclude tables
headings = false     # exclude headings
```

---

## Emphasis Rules

### MD036 - Emphasis instead of heading

❌ **Bad**:
```markdown
**Section Title**

Content...
```

✅ **Good**:
```markdown
## Section Title

Content...
```

**Auto-fix**: No

---

### MD037 - Spaces inside emphasis

(See Whitespace Rules section above)

---

### MD049 - Emphasis style

**What it checks**: Consistent emphasis style.

**Styles**:
- **Asterisk**: `*italic*` and `**bold**`
- **Underscore**: `_italic_` and `__bold__`
- **Consistent**: Pick one

✅ **Good** (asterisk):
```markdown
*italic* and **bold**
```

**Auto-fix**: Yes

**Config**:
```toml
emphasis_style = "asterisk"  # or "underscore"
```

---

### MD050 - Strong style

**What it checks**: Consistent strong (bold) style.

Similar to MD049 but specifically for bold.

**Auto-fix**: Yes

---

## Other Rules

### MD025 - Multiple top-level headings

**What it checks**: Only one H1 heading in document.

❌ **Bad**:
```markdown
# First H1
# Second H1
```

✅ **Good**:
```markdown
# Only H1

## Subsections use H2
```

**Auto-fix**: No

---

### MD033 - Inline HTML

**What it checks**: Discourages inline HTML (not pure markdown).

❌ **Warning**:
```markdown
<div>HTML content</div>
```

✅ **Preferred**:
```markdown
Use markdown syntax when possible
```

**Note**: Some HTML is necessary (images with size, etc.). Configure allowed tags:

```toml
[MD033]
allowed_elements = ["img", "br"]
```

**Auto-fix**: No

---

### MD035 - Horizontal rule style

**What it checks**: Consistent horizontal rule style.

**Styles**:
- `---`
- `***`
- `___`

✅ **Good** (consistent):
```markdown
---

Content

---
```

**Auto-fix**: Yes

---

### MD045 - Images should have alt text

❌ **Bad**:
```markdown
![](image.png)
```

✅ **Good**:
```markdown
![Descriptive alt text](image.png)
```

**Auto-fix**: No (requires descriptive text)

---

## Configuration Example

**`.rumdl.toml`**:
```toml
# Disable specific rules
disabled_rules = ["MD013", "MD024", "MD033"]

# Line length
line_length = 120

# Heading style
heading_style = "atx"

# List markers
list_marker = "-"

# Code fence
code_fence = "```"

# Emphasis
emphasis_style = "asterisk"

# MD013 configuration
[MD013]
line_length = 120
code_blocks = false
tables = false

# MD033 - allowed HTML tags
[MD033]
allowed_elements = ["img", "br", "kbd"]

# MD044 - proper name capitalization
[MD044]
names = ["JavaScript", "TypeScript", "GitHub", "API", "JSON", "YAML"]
```

---

## Quick Rule Reference by Number

| Rule | Description | Auto-fix |
|------|-------------|----------|
| MD001 | Heading increment | ✅ |
| MD002 | First heading H1 | ❌ |
| MD003 | Heading style | ✅ |
| MD004 | List marker style | ✅ |
| MD005 | List indentation | ✅ |
| MD006 | List at line start | ✅ |
| MD007 | List indent amount | ✅ |
| MD009 | Trailing spaces | ✅ |
| MD010 | Hard tabs | ✅ |
| MD011 | Reversed link syntax | ✅ |
| MD012 | Multiple blank lines | ✅ |
| MD013 | Line length | ❌ |
| MD014 | Dollar signs in commands | ✅ |
| MD018 | Space after hash | ✅ |
| MD019 | Multiple spaces after hash | ✅ |
| MD020 | Space inside hashes | ✅ |
| MD021 | Multiple spaces inside hashes | ✅ |
| MD022 | Headings surrounded by blanks | ✅ |
| MD023 | Heading at line start | ✅ |
| MD024 | Duplicate headings | ❌ |
| MD025 | Multiple H1 | ❌ |
| MD026 | Trailing punctuation | ✅ |
| MD027 | Blockquote spacing | ✅ |
| MD028 | Blank in blockquote | ✅ |
| MD029 | Ordered list prefix | ✅ |
| MD030 | List marker spacing | ✅ |
| MD031 | Code block blanks | ✅ |
| MD032 | List blanks | ✅ |
| MD033 | Inline HTML | ❌ |
| MD034 | Bare URL | ❌ |
| MD035 | Horizontal rule style | ✅ |
| MD036 | Emphasis as heading | ❌ |
| MD037 | Spaces in emphasis | ✅ |
| MD038 | Spaces in code span | ✅ |
| MD039 | Spaces in link | ✅ |
| MD040 | Code language | ❌ |
| MD041 | First line H1 | ❌ |
| MD042 | Empty links | ❌ |
| MD043 | Required structure | ❌ |
| MD044 | Proper names | ✅* |
| MD045 | Image alt text | ❌ |
| MD046 | Code block style | ✅ |
| MD047 | File ending newline | ✅ |
| MD048 | Code fence style | ✅ |
| MD049 | Emphasis style | ✅ |
| MD050 | Strong style | ✅ |
| MD051 | Link fragments | ❌ |
| MD052 | Reference definition blanks | ✅ |
| MD053 | Unused references | ❌ |

*if configured

---

**Total**: 57 rules (41 auto-fixable, 16 manual)
