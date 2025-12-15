# Deduplication Strategies

Techniques for identifying and removing duplicate content in markdown documents.

## Detection Methods

### Exact Duplicates

**Full section duplicates**:
```markdown
## Section A
This exact text appears here.

## Section B
This exact text appears here.  # EXACT DUPLICATE
```

**Detection**: String comparison
```javascript
function findExactDuplicates(sections) {
  const seen = new Map();
  const duplicates = [];

  sections.forEach((section, index) => {
    const normalized = section.content.trim().toLowerCase();

    if (seen.has(normalized)) {
      duplicates.push({
        original: seen.get(normalized),
        duplicate: index,
        content: section.content
      });
    } else {
      seen.set(normalized, index);
    }
  });

  return duplicates;
}
```

### Near Duplicates (>80% similarity)

**Similar but not identical**:
```markdown
## Version 1
The API requires authentication with an API key.

## Version 2
The API requires authentication using an API key.  # 95% similar
```

**Detection**: Levenshtein distance or cosine similarity
```javascript
function calculateSimilarity(text1, text2) {
  // Tokenize
  const tokens1 = new Set(text1.toLowerCase().split(/\s+/));
  const tokens2 = new Set(text2.toLowerCase().split(/\s+/));

  // Jaccard similarity
  const intersection = new Set(
    [...tokens1].filter(x => tokens2.has(x))
  );
  const union = new Set([...tokens1, ...tokens2]);

  return intersection.size / union.size;
}
```

### Conceptual Duplicates

**Same meaning, different words**:
```markdown
## Section A
API stands for Application Programming Interface.

## Section B
An API (Application Programming Interface) is a software intermediary...
```

**Strategy**: Manual review or semantic analysis

## Consolidation Patterns

### Pattern 1: Keep One, Delete Others

**Before**:
```markdown
## Introduction
This document covers API usage.

## Overview
This document covers API usage.  # Duplicate

## Getting Started
Let's begin...
```

**After**:
```markdown
## Introduction
This document covers API usage.

## Getting Started
Let's begin...
```

### Pattern 2: Merge and Enhance

**Before**:
```markdown
## Authentication
Use API keys for authentication.

## Security
Authentication requires API keys. Always use HTTPS.
```

**After**:
```markdown
## Authentication
Use API keys for authentication. Always use HTTPS for security.
```

### Pattern 3: Create Single Source + Links

**Before**:
```markdown
## Section A
Rate limiting: 100 requests per hour.

## Section B
Remember: 100 requests per hour limit.

## Section C
Don't exceed 100 requests per hour.
```

**After**:
```markdown
## Rate Limiting
Free tier: 100 requests per hour.

## Section A
See [Rate Limiting](#rate-limiting) for details.

## Section B
See [Rate Limiting](#rate-limiting).
```

### Pattern 4: Glossary Extraction

**Before**:
```markdown
## API Basics
API means Application Programming Interface.

## REST Overview
An API (Application Programming Interface) allows...

## Getting Started
APIs (Application Programming Interfaces) are...
```

**After**:
```markdown
## Glossary

**API**: Application Programming Interface - a software intermediary

## API Basics
See [API](#glossary) for definition.

## REST Overview
An [API](#glossary) allows...
```

## Automated Detection Script

```bash
#!/bin/bash
# detect-duplicates.sh

FILE="$1"

# Extract all headings and following content
awk '
  /^##/ {
    if (content) print section "||" content;
    section = $0;
    content = "";
    next;
  }
  { content = content $0 "\n"; }
  END { if (content) print section "||" content; }
' "$FILE" | \
sort -t'|' -k2 | \
uniq -D -f1 --all-repeated=separate

echo "Potential duplicates found above"
```

## Manual Review Checklist

When reviewing potential duplicates:

- [ ] Is the content 100% identical?
- [ ] Does one version have more detail?
- [ ] Are they in different contexts?
- [ ] Can they be merged without losing information?
- [ ] Should one become a reference to the other?
- [ ] Is this intentional repetition for clarity?

## Deduplication Workflow

1. **Run detection** - Find duplicates
2. **Categorize** - Exact, near, or conceptual
3. **Choose strategy** - Delete, merge, or link
4. **Update** - Apply chosen strategy
5. **Verify** - Check document still makes sense
6. **Update links** - Fix broken references

## Common Duplicate Patterns

### Repeated Definitions

**Pattern**: Technical terms defined multiple times
**Solution**: Create glossary section, link to it

### Repeated Examples

**Pattern**: Same code example in multiple sections
**Solution**: Create "Examples" section, reference it

### Repeated Warnings

**Pattern**: Same warning/note in multiple places
**Solution**: Create "Important Notes" section at top

### Repeated Instructions

**Pattern**: Same setup/installation steps repeated
**Solution**: Create "Prerequisites" section, link to it

## Tools

**Diff tools**:
```bash
# Compare sections
diff <(sed -n '/^## Section A/,/^##/p' doc.md) \
     <(sed -n '/^## Section B/,/^##/p' doc.md)
```

**Similarity detection** (Python):
```python
from difflib import SequenceMatcher

def similarity(a, b):
    return SequenceMatcher(None, a, b).ratio()

# Find similar paragraphs
paragraphs = content.split('\n\n')
for i, p1 in enumerate(paragraphs):
    for j, p2 in enumerate(paragraphs[i+1:], i+1):
        sim = similarity(p1, p2)
        if sim > 0.8:
            print(f"Similar ({sim:.2%}): {i} and {j}")
```
