# Frontmatter Templates

Document-type-specific YAML frontmatter templates for various use cases.

## Table of Contents

- [Basic Template](#basic-template)
- [Documentation](#documentation)
- [API Reference](#api-reference)
- [Tutorial/Guide](#tutorialguide)
- [Research/Analysis](#researchanalysis)
- [Meeting Notes](#meeting-notes)
- [Blog Post](#blog-post)
- [Changelog](#changelog)
- [README](#readme)
- [Specification](#specification)
- [Custom Fields Reference](#custom-fields-reference)

---

## Basic Template

**Use for**: Generic documents, quick notes

```yaml
---
title: Document Title
created: 2024-12-16
updated: 2024-12-16
tags: []
---
```

---

## Documentation

**Use for**: Technical documentation, user guides, manuals

```yaml
---
title: Feature Documentation
type: Documentation
category: User Guide | Developer Guide | API | Reference
status: Draft | Review | Published | Deprecated
version: 1.0.0
audience: User | Developer | Admin
tags: [documentation, guide]
related:
  - other-doc.md
  - reference.md
toc: true
---
```

**Extended version** (comprehensive docs):
```yaml
---
title: Complete Feature Documentation
type: Documentation
category: Developer Guide
status: Published
version: 2.1.0
author: Team Name
created: 2024-01-15
updated: 2024-12-16
audience: Developer
difficulty: Intermediate | Beginner | Advanced
prerequisites:
  - Basic understanding of X
  - Installation of Y
tags: [documentation, feature-x, api]
related:
  - getting-started.md
  - api-reference.md
aliases: [feature-x-docs, x-guide]
toc: true
nav_order: 3
---
```

---

## API Reference

**Use for**: API documentation, endpoint references

```yaml
---
title: User API Reference
type: API Reference
category: REST API | GraphQL | RPC
version: v2.1
status: Published
baseURL: https://api.example.com/v2
authentication: Bearer | API Key | OAuth2
tags: [api, user-management]
endpoints:
  - GET /users
  - POST /users
  - PUT /users/{id}
  - DELETE /users/{id}
related:
  - authentication.md
  - rate-limiting.md
---
```

**Endpoint-specific**:
```yaml
---
title: GET /users/{id}
type: API Endpoint
method: GET
path: /users/{id}
category: User Management
authentication_required: true
rate_limit: 100 requests/minute
since_version: v1.0
tags: [api, users, get]
---
```

---

## Tutorial/Guide

**Use for**: Step-by-step tutorials, how-to guides

```yaml
---
title: Getting Started with Feature X
type: Tutorial
category: Getting Started | How-To | Walkthrough
difficulty: Beginner | Intermediate | Advanced
duration: 15 minutes
prerequisites:
  - Node.js 18+
  - Basic JavaScript knowledge
objectives:
  - Learn how to set up X
  - Create your first Y
  - Deploy to production
tags: [tutorial, getting-started]
related:
  - installation.md
  - troubleshooting.md
completed: false
---
```

---

## Research/Analysis

### General Research Document

**Use for**: Generic research notes, analysis documents, findings

```yaml
---
title: Market Research Analysis
type: Research
date: 2024-12-16
category: Market Analysis | Competitive Analysis | User Research
status: In Progress | Completed
author: Researcher Name
tags: [research, market, analysis]
sources:
  - https://source1.com
  - https://source2.com
methodology: Survey | Interview | Data Analysis
sample_size: 100
key_findings:
  - Finding 1
  - Finding 2
conclusions:
  - Conclusion 1
next_steps:
  - Action item 1
---
```

### Success Story

**Use for**: Documenting product success stories, founder journeys

```yaml
---
title: [Product Name] Success Story
research-date: YYYY-MM-DD
category: [AI SaaS | Web App | Developer Tool | etc]
tags: [success-story, relevant, tags]
type: Success Story
status: Active | Inactive | Acquired | Shut down
product: [Product Name]
website: [URL]
founder: [Founder Name]
founder-handle: [@handle]
founded: YYYY-MM
revenue-range: [$X - $Y MRR]
current-revenue: [$X MRR]
team-size: [Solo | Solo → 2 | etc]
funding: [Bootstrapped ($X) | $X raised]
time-to-first-revenue: [Launch day | X weeks]
time-to-10k-mrr: [X months]
users: [X paying customers]
---
```

### Business Idea

**Use for**: Business idea documentation and evaluation

```yaml
---
title: [Idea Name]
generated-date: YYYY-MM-DD
type: Business Idea
status: Generated | Validated | In Progress | Abandoned
score: X.X
recommendation: GO | ITERATE | VALIDATE MORE | NO-GO
success-patterns: [pattern1, pattern2]
expected-timeline:
  mvp: [X days]
  first-revenue: [X weeks]
  target-mrr: [$XK MRR in X months]
tags: [idea, category, tags]
---
```

### Pattern

**Use for**: Extracted success patterns

```yaml
---
title: [Pattern Name]
pattern-category: idea-discovery | validation | mvp-building | customer-acquisition | product-market-fit | growth | monetization | distribution | retention | differentiation | common
success-rate: High | Medium | Low ([percentage]+)
time-investment: Immediate | X days | X weeks
difficulty: Easy | Medium | Hard
tags: [pattern, category-name]
type: Pattern
---
```

### Pattern Analysis Report

**Use for**: Multi-story pattern analysis reports

```yaml
---
title: [Report Title]
analysis-date: YYYY-MM-DD
type: Pattern Analysis Report
stories-analyzed: [number]
deep-dive-count: [number]
data-source: [URL or description]
tags: [report, pattern-analysis, tags]
---
```

---

## Meeting Notes

**Use for**: Meeting minutes, discussion notes

```yaml
---
title: Weekly Team Meeting
type: Meeting
date: 2024-12-16
time: "14:00-15:00"
location: Conference Room A | Zoom | Office
attendees:
  - Person 1
  - Person 2
  - Person 3
absent:
  - Person 4
tags: [meeting, weekly, team]
agenda:
  - Topic 1
  - Topic 2
action_items:
  - "[Person 1] Do task X by 2024-12-20"
  - "[Person 2] Review document Y"
decisions:
  - Decision 1
  - Decision 2
next_meeting: 2024-12-23
---
```

---

## Blog Post

**Use for**: Blog articles, posts, essays

```yaml
---
title: How to Build Scalable APIs
type: Blog Post
author: Author Name
date: 2024-12-16
updated: 2024-12-16
category: Engineering | Product | Design
tags: [api, scalability, backend]
excerpt: Learn best practices for building scalable APIs that can handle millions of requests.
reading_time: 8 minutes
featured_image: /images/scalable-apis.png
published: true | false
seo:
  description: Complete guide to building scalable APIs
  keywords: [api, scalability, performance]
related_posts:
  - database-optimization.md
  - caching-strategies.md
---
```

---

## Changelog

**Use for**: Version history, release notes

```yaml
---
title: Changelog
type: Changelog
latest_version: 2.1.0
date: 2024-12-16
tags: [changelog, releases]
---

## [2.1.0] - 2024-12-16

### Added
- New feature X

### Changed
- Improved performance of Y

### Fixed
- Bug in Z

## [2.0.0] - 2024-12-01

...
```

---

## README

**Use for**: Project README files

```yaml
---
title: Project Name
type: README
version: 1.0.0
status: Active | Deprecated | Archived
license: MIT | Apache 2.0 | GPL
repository: https://github.com/user/repo
homepage: https://example.com
documentation: https://docs.example.com
tags: [project, readme]
language: JavaScript | Python | Go
requires:
  - Node.js 18+
  - PostgreSQL 14+
---
```

---

## Specification

**Use for**: Technical specifications, RFC documents

```yaml
---
title: Feature X Specification
type: Specification
status: Draft | Proposed | Accepted | Rejected | Implemented
version: 0.1.0
author: Author Name
created: 2024-12-16
updated: 2024-12-16
category: Technical Specification | Design Document | RFC
tags: [spec, feature-x]
reviewers:
  - Reviewer 1
  - Reviewer 2
implementation_status: Not Started | In Progress | Completed
target_version: 3.0.0
---
```

---

## Custom Fields Reference

### Common Fields

| Field | Type | Description | Example |
|-------|------|-------------|---------|
| `title` | string | Document title | `"API Reference"` |
| `type` | string | Document type | `"Documentation"` |
| `category` | string | Primary category | `"User Guide"` |
| `status` | string | Lifecycle status | `"Published"` |
| `version` | string | Document version | `"1.0.0"` |
| `author` | string | Creator/maintainer | `"John Doe"` |
| `created` | date | Creation date | `2024-12-16` |
| `updated` | date | Last update | `2024-12-16` |
| `tags` | array | Keywords | `[api, rest]` |

### Obsidian-Specific Fields

| Field | Type | Description | Example |
|-------|------|-------------|---------|
| `aliases` | array | Alternative names | `["alt-name", "shorthand"]` |
| `cssclass` | string | Custom CSS class | `"wide-page"` |
| `publish` | boolean | Publish to Obsidian Publish | `true` |
| `permalink` | string | Custom URL | `"/docs/api"` |

### Documentation Fields

| Field | Type | Description | Example |
|-------|------|-------------|---------|
| `audience` | string | Target audience | `"Developer"` |
| `difficulty` | string | Complexity level | `"Intermediate"` |
| `prerequisites` | array | Required knowledge | `["Basic JS"]` |
| `duration` | string | Time to complete | `"15 minutes"` |
| `related` | array | Related documents | `["guide.md"]` |
| `toc` | boolean | Show table of contents | `true` |
| `nav_order` | number | Navigation order | `3` |

### Content Fields

| Field | Type | Description | Example |
|-------|------|-------------|---------|
| `excerpt` | string | Short summary | `"Brief intro..."` |
| `description` | string | Detailed description | `"Complete guide..."` |
| `reading_time` | string | Estimated time | `"8 minutes"` |
| `featured_image` | string | Image URL/path | `"/img/hero.png"` |

### Status Fields

| Field | Type | Description | Common Values |
|-------|------|-------------|---------------|
| `status` | string | Document state | Draft, Review, Published, Deprecated, Archived |
| `published` | boolean | Published flag | `true` / `false` |
| `completed` | boolean | Completion flag | `true` / `false` |

### SEO Fields

| Field | Type | Description | Example |
|-------|------|-------------|---------|
| `seo.description` | string | Meta description | `"SEO-friendly text"` |
| `seo.keywords` | array | SEO keywords | `["keyword1"]` |
| `seo.title` | string | SEO title | `"Page Title"` |

### Technical Fields

| Field | Type | Description | Example |
|-------|------|-------------|---------|
| `version` | string | Version number | `"1.0.0"` |
| `since_version` | string | Added in version | `"v2.0"` |
| `deprecated_in` | string | Deprecated version | `"v3.0"` |
| `license` | string | License type | `"MIT"` |
| `language` | string | Programming language | `"JavaScript"` |

---

## Field Naming Conventions

### Case Styles

**snake_case** (recommended for Obsidian):
```yaml
created_at: 2024-12-16
reading_time: 8 minutes
```

**camelCase** (alternative):
```yaml
createdAt: 2024-12-16
readingTime: 8 minutes
```

**kebab-case** (avoid, causes parsing issues):
```yaml
created-at: 2024-12-16  # Can cause issues
```

### Boolean Values

```yaml
published: true        # Recommended
published: false
published: yes         # Alternative (YAML allows)
published: no
```

### Dates

**ISO 8601 format** (recommended):
```yaml
created: 2024-12-16
updated: 2024-12-16T14:30:00Z
```

### Arrays

**Flow style** (inline):
```yaml
tags: [api, rest, documentation]
```

**Block style** (multiline):
```yaml
tags:
  - api
  - rest
  - documentation
```

---

## Validation Example

**Valid frontmatter**:
```yaml
---
title: My Document
created: 2024-12-16
tags: [example]
---
```

**Invalid frontmatter** (common errors):
```yaml
---
title: My Document: With Colon (unquoted)  # ❌ Needs quotes
created: 12/16/2024  # ❌ Use YYYY-MM-DD
tags: example  # ❌ Should be array [example]
missing-closing-dashes  # ❌ No closing ---
```

**Fixed**:
```yaml
---
title: "My Document: With Colon"
created: 2024-12-16
tags: [example]
---
```

---

## Tools for Validation

**Online validators**:
- https://www.yamllint.com/
- https://jsonformatter.org/yaml-validator

**CLI validation**:
```bash
# Using yq
yq eval document.md

# Using yamllint
yamllint document.md

# Using rumdl (checks frontmatter syntax)
rumdl check document.md
```

---

**Recommendation**: Start with the Basic Template and add fields as needed. Don't over-engineer frontmatter for simple documents.
