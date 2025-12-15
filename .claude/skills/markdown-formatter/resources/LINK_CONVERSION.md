# Link Conversion Guide

Advanced patterns and techniques for converting various link formats to standard markdown.

## Common Conversions

### Wiki-Style Links to Markdown

**Basic wiki link**:
```
Pattern: \[\[([^\]]+)\]\]
Example: [[document-name]]
Convert to: [document-name](document-name.md)
```

**Wiki link with alias**:
```
Pattern: \[\[([^\|]+)\|([^\]]+)\]\]
Example: [[document-name|Display Text]]
Convert to: [Display Text](document-name.md)
```

**Section links**:
```
Pattern: \[\[([^#\]]+)#([^\]]+)\]\]
Example: [[document#section]]
Convert to: [document](document.md#section)
```

**Same-document section**:
```
Pattern: \[\[#([^\]]+)\]\]
Example: [[#section-name]]
Convert to: [section-name](#section-name)
```

### Obsidian-Specific Formats

**Image embeds**:
```
Pattern: !\[\[([^\]]+\.(png|jpg|gif|svg))\]\]
Example: ![[image.png]]
Convert to: ![image](image.png)
```

**File embeds** (convert to links):
```
Pattern: !\[\[([^\]]+\.md)\]\]
Example: ![[document.md]]
Convert to: See [document](document.md)
```

### Bare URLs

**Simple URL**:
```
Pattern: (?<!\()https?://[^\s\)]+
Example: See https://example.com for details
Convert to: See [example.com](https://example.com) for details
```

**URL with context** (extract description from surrounding text):
```
Example: Check out https://github.com/user/repo
Convert to: Check out [user/repo](https://github.com/user/repo)
```

### File References

**Implicit markdown links**:
```
Pattern: ([a-z0-9-]+\.md)(?!\))
Example: See document-name.md for details
Convert to: See [document-name](document-name.md) for details
```

**Path references**:
```
Pattern: (\.\./[^\s]+\.md)
Example: Related: ../folder/doc.md
Convert to: Related: [doc](../folder/doc.md)
```

## Regex Patterns

### Detection Patterns

```javascript
// Wiki-style link
const wikiLinkRegex = /\[\[([^\]]+)\]\]/g;

// Wiki link with alias
const wikiAliasRegex = /\[\[([^\|]+)\|([^\]]+)\]\]/g;

// Bare URL
const bareUrlRegex = /(?<!\(|href="|src=")https?:\/\/[^\s)]+/g;

// File reference (not in link)
const fileRefRegex = /(?<!\()([a-z0-9-]+\.md)(?!\))/g;

// Section link
const sectionRegex = /\[\[([^#\]]+)#([^\]]+)\]\]/g;

// Image embed
const imageEmbedRegex = /!\[\[([^\]]+\.(png|jpg|gif|svg))\]\]/g;
```

### Conversion Functions

```javascript
// Convert wiki links
function convertWikiLinks(text) {
  // With alias
  text = text.replace(
    /\[\[([^\|]+)\|([^\]]+)\]\]/g,
    '[$2]($1.md)'
  );

  // Without alias
  text = text.replace(
    /\[\[([^\]]+)\]\]/g,
    '[$1]($1.md)'
  );

  return text;
}

// Convert bare URLs
function convertBareUrls(text) {
  return text.replace(
    /(?<!\()https?:\/\/([^\s)]+)/g,
    (match, domain) => {
      // Extract meaningful name from URL
      const name = extractUrlName(match);
      return `[${name}](${match})`;
    }
  );
}

// Extract readable name from URL
function extractUrlName(url) {
  // GitHub repo: https://github.com/user/repo → user/repo
  if (url.includes('github.com')) {
    const parts = url.split('github.com/')[1].split('/');
    return `${parts[0]}/${parts[1]}`;
  }

  // Domain: https://example.com/path → example.com
  try {
    return new URL(url).hostname;
  } catch {
    return url;
  }
}
```

## Advanced Patterns

### Link Text Optimization

**Before** (too long):
```markdown
[This is a very long link text that describes everything about the document](doc.md)
```

**After** (concise):
```markdown
See the [documentation](doc.md) for details.
```

### Smart Replacements

**GitHub URLs**:
```
https://github.com/user/repo
→ [user/repo](https://github.com/user/repo)

https://github.com/user/repo/issues/123
→ [user/repo#123](https://github.com/user/repo/issues/123)
```

**Documentation URLs**:
```
https://docs.example.com/api/v2/users
→ [API v2 Users](https://docs.example.com/api/v2/users)
```

## Batch Conversion Script

```bash
#!/bin/bash
# convert-links.sh

FILE="$1"

# Convert wiki links with alias
sed -i.bak 's/\[\[\([^|]*\)|\([^]]*\)\]\]/[\2](\1.md)/g' "$FILE"

# Convert wiki links without alias
sed -i.bak 's/\[\[\([^]]*\)\]\]/[\1](\1.md)/g' "$FILE"

# Convert image embeds
sed -i.bak 's/!\[\[\([^]]*\)\]\]/![\1](\1)/g' "$FILE"

echo "Converted links in $FILE"
echo "Backup saved as ${FILE}.bak"
```

## Edge Cases

### Handling Special Characters

**Spaces in filenames**:
```
[[My Document With Spaces]]
→ [My Document With Spaces](My%20Document%20With%20Spaces.md)
```

**Special characters**:
```
[[Feature (Beta)]]
→ [Feature (Beta)](Feature%20%28Beta%29.md)
```

### Preserving Existing Links

**Don't convert links that are already markdown**:
```javascript
// ❌ Bad: Converts already-correct links
text.replace(/\[\[([^\]]+)\]\]/g, '[$1]($1.md)');

// ✅ Good: Check if already markdown first
function convertWikiLinks(text) {
  const lines = text.split('\n');
  return lines.map(line => {
    // Skip if line contains markdown link
    if (/\[.*\]\(.*\)/.test(line)) return line;

    // Convert wiki links
    return line.replace(/\[\[([^\]]+)\]\]/g, '[$1]($1.md)');
  }).join('\n');
}
```

## Validation

**Check for unconverted links**:
```bash
# Find remaining wiki links
grep -r '\[\[.*\]\]' docs/

# Find bare URLs
grep -r 'https\?://[^ )]*' docs/ | grep -v '\[.*\](http'

# Find file references not in links
grep -r '\.md[^)]' docs/
```

**Verify converted links work**:
```bash
# Check all markdown links
for file in docs/**/*.md; do
  # Extract links
  grep -oP '\[.*?\]\(\K[^)]+' "$file" | while read link; do
    # Check if file exists (for relative links)
    if [[ ! $link =~ ^https?:// ]]; then
      target="docs/$link"
      if [[ ! -f "$target" ]]; then
        echo "Broken link in $file: $link"
      fi
    fi
  done
done
```
