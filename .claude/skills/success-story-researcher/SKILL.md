---
name: success-story-researcher
description: Research and extract success stories from the web including founder journeys, revenue milestones, and building processes. Use when searching for indie developer success cases, researching product launches, finding founder stories, extracting building-in-public journeys, or gathering real-world business data. Covers effective search strategies, reliable sources, information extraction frameworks, and validation methods.
---

# Success Story Researcher

## Purpose

**Research and document detailed success stories** from indie developers and small teams. The goal is to create **comprehensive records** that capture every detail of the journey - so rich that you never need to re-read the original sources.

**This skill DOES NOT evaluate or analyze** - it only collects and organizes information. The `success-formula-analyzer` skill will later extract patterns from these detailed records.

**Key Focus:**
- One file per case (product or person)
- Maximum detail and context
- Rich information for later analysis
- Complete source references

## When to Use This Skill

Automatically activates when you mention:
- Research success stories
- Find indie developer cases
- Search for founder journeys
- Product launch stories
- Building in public examples
- Revenue milestone stories
- Startup post-mortems
- Indie hacker interviews
- How [product] was built
- Success case studies

## Core Research Framework: The 3-Layer Story Model

**Layer 1: The Outcome (What)**
- Current revenue/users
- Time to success
- Team size
- Total funding (if any)

**Layer 2: The Journey (How)** ⭐ Most Important
- Initial problem/motivation
- MVP timeline and features
- Launch strategy
- Growth tactics used
- Pivots and failures
- Key decisions and why
- Timeline of milestones

**Layer 3: The Context (Why)**
- Founder background
- Market timing
- Unique advantages
- Lessons learned

**Goal:** Find Layer 2 (Journey) rich stories, not just Layer 1 (Outcome) metrics.

## Research Workflow

### Step 0: Check for Existing Documentation (MANDATORY)

**BEFORE starting research, ALWAYS check if documentation already exists:**

```bash
# Check if a story for this product already exists
ls research/stories/ | grep -i "[product-slug]"
```

**Simple Rule:**
- **If file exists** → Skip, inform user that documentation already exists
- **If file doesn't exist** → Proceed with research

**Example:**

```
User: "Research Notion success story"

Claude:
1. Check: ls research/stories/ | grep -i "notion"
2. Found: notion-2024-11-15.md
3. Response: "✅ Documentation already exists: research/stories/notion-2024-11-15.md

   Skipping research to avoid duplicates. Use existing file."
```

**If researching multiple products:**

```
User: "간단한 웹툴 성공 사례 5개 찾아줘"

Claude:
1. Check each product slug in research/stories/
2. Skip products with existing files
3. Only research products without documentation
4. Report: "✅ Skipped 2 (docs exist), 📝 Created 3 new stories"
```

### Step 1: Search Multiple Sources

Use WebSearch and WebFetch to find rich, detailed stories.

**Start with Top 3 Sources:**

1. **Indie Hackers** (`indiehackers.com/interviews`)
   - Search: `"[product name] interview"` OR `"$0 to $X MRR"`
   - Why: Structured interviews with revenue data

2. **Reddit** (`r/EntrepreneurRideAlong`, `r/SaaS`)
   - Search: `"[product] revenue update"` OR `"My journey from 0 to X"`
   - Why: Long-form, authentic journey posts

3. **Twitter/X** (`#buildinpublic`)
   - Search: `#buildinpublic "[product]"` OR `"[founder] building"`
   - Why: Real-time building threads with details

**Quick Search Patterns:**
- Revenue-based: `"$0 to $10K MRR [industry]"`
- Timeline-based: `"[product] month 1"` OR `"6 month update"`
- Launch-based: `"How I launched [product]"`

**For more search strategies, see:** `resources/SEARCH_STRATEGIES.md`

### Step 2: Extract and Document

Use the comprehensive template to document everything in maximum detail.

**Essential Data to Extract:**
- Product information and metrics
- Founder background and motivation
- MVP timeline and features
- Launch strategy and results
- Growth journey (month by month)
- All tactics used (with context)
- Founder's direct quotes
- Complete source references

**Template Location:** `resources/STORY_TEMPLATE.md`

**Key Principles:**
- Document everything without filtering
- Use direct quotes with full context
- List all tactics mentioned
- Include specific numbers and dates
- Note what came from which source

### Step 3: Save and Format

**Save Location:** `research/stories/[product-slug]-[yyyy-mm-dd].md`

**Filename Rules:**
- All lowercase
- Replace spaces with hyphens
- Remove special characters
- Examples: `notion-2024-12-16.md`, `convertkit-2024-12-16.md`

**After saving:**
1. ✅ Verify all sources included
2. ✅ Check template sections filled
3. ✅ Format using `markdown-formatter` skill (auto-triggered)
4. ✅ Ready for `success-formula-analyzer`

## Top Sources Quick Reference

### Tier 1: Interview Platforms (Best Quality)
- **Indie Hackers** - `indiehackers.com/interviews` ⭐⭐⭐⭐⭐
- **Starter Story** - `starterstory.com` ⭐⭐⭐⭐⭐

### Tier 2: Community Platforms (High Signal)
- **Reddit** - `r/EntrepreneurRideAlong`, `r/SaaS` ⭐⭐⭐⭐
- **Twitter/X** - `#buildinpublic`, `#indiehacker` ⭐⭐⭐⭐

### Tier 3: Launch Platforms
- **Product Hunt** - `producthunt.com` ⭐⭐⭐
- **Hacker News** - `news.ycombinator.com` ⭐⭐⭐

**For complete source list with search strategies, see:** `resources/SEARCH_STRATEGIES.md`

## Source Quality Indicators

### High-Quality ✅
- First-hand account (founder writing)
- Specific numbers (revenue, users, timeline)
- Detailed tactics (not just "did marketing")
- Timestamps (month-by-month or week-by-week)
- Challenges mentioned (not just success)
- Recent (< 2 years old)
- Evidence provided (screenshots, links)

### Low-Quality ❌
- Vague metrics ("made some money")
- No timeline (unclear when things happened)
- Third-party summary (journalist, not founder)
- Marketing fluff (selling course, not sharing)
- No failures mentioned (too polished)
- Outdated (> 5 years old)

## File Storage Rules

### Directory Structure

```
research/
├── stories/          # Individual product success stories (YOUR JOB)
│   └── [product-slug]-[yyyy-mm-dd].md
├── reports/          # Analysis reports (success-formula-analyzer's job)
│   └── [topic]-analysis-[yyyy-mm-dd].md
└── patterns/         # Extracted patterns (success-formula-analyzer's job)
    └── [pattern-name].md
```

### Your Role vs Analyzer's Role

**success-story-researcher (YOU):**
- ✅ Find and document detailed information
- ✅ Record everything without filtering
- ✅ Provide rich context and quotes
- ✅ List all sources meticulously
- ✅ Save to `research/stories/[product]-[date].md`
- ❌ DO NOT analyze or conclude
- ❌ DO NOT create summary/comparison reports
- ❌ DO NOT extract patterns

**success-formula-analyzer (SEPARATE SKILL):**
- Reads your detailed records
- Identifies common patterns
- Extracts reproducible tactics
- Rates reproducibility
- Makes recommendations
- Creates reports in `research/reports/`

**DO NOT create:**
- ❌ Multi-story comparison reports
- ❌ Pattern analysis documents
- ❌ Benchmark tables across stories
- ❌ Recommendations based on patterns

## Using WebSearch & WebFetch Tools

### WebSearch Strategy

**Use for:**
- Initial discovery of success stories
- Finding multiple sources
- Getting overview of available content

**Example query:**
```
"indie developer success story SaaS $10K MRR 2024"
```

**Effective combinations:**
```
Revenue + Journey + Platform keywords:
"How I built SaaS $5K MRR indie hackers 2024"

Timeline + Product + Channel:
"[product] month 1 update reddit"
```

### WebFetch Strategy

**Use for:**
- Extracting full article content
- Getting interview transcripts
- Pulling detailed blog posts

**Effective prompt:**
```
"Extract the founder's journey story including:
- Initial motivation
- MVP timeline and features
- Launch strategy
- Growth tactics used
- Revenue milestones and timeline
- Key lessons learned"
```

**Multi-URL workflow:**
1. WebSearch: Find 5 relevant URLs
2. WebFetch 3-5 URLs in parallel
3. Cross-reference information
4. Document in template

## Integration with Other Skills

### After Documenting Stories

**→ success-formula-analyzer**
```
"Analyze patterns from research/stories/"
```
- Reads your detailed stories
- Extracts reproducible success patterns
- Creates pattern files in `research/patterns/`
- Generates reports in `research/reports/`

**→ business-idea-evaluator**
```
"Compare my idea with [product] story"
```
- Uses detailed information to benchmark ideas
- Identifies similar success factors
- Evaluates if approach matches proven patterns

**→ markdown-formatter (AUTO)**
- Automatically formats saved markdown files
- Adds frontmatter metadata
- Fixes lint errors
- Ensures consistent formatting

### Workflow Integration

```
1. success-story-researcher → Document individual stories
                              ↓
2. success-formula-analyzer → Extract patterns from multiple stories
                              ↓
3. business-idea-evaluator  → Score your idea against patterns
                              ↓
4. feasibility-checker      → Validate execution feasibility
                              ↓
5. business-orchestrator    → Coordinate all analysis
```

## Must-Include Elements

Every research file MUST include:

1. ✅ **Complete Sources:** Every URL, date accessed, what info extracted from each
2. ✅ **Detailed Timeline:** Specific dates, not vague timeframes
3. ✅ **Concrete Numbers:** Exact revenue, costs, metrics - no "approximately"
4. ✅ **Founder's Voice:** Direct quotes, their explanations, decision rationale
5. ✅ **Tech & Tools:** Complete stack, all tools used, why chosen
6. ✅ **Financial Details:** All costs, revenue breakdown, margins
7. ✅ **Marketing Specifics:** Exact tactics, time/money invested, results
8. ✅ **Context:** Why decisions made, what alternatives considered

## Quality Checklist

Before saving, verify:

**Sources (CRITICAL):**
- [ ] Every URL included with full context
- [ ] Date published AND date accessed for each
- [ ] Specific information extracted from each source listed
- [ ] At least one primary (founder first-hand) source
- [ ] Cross-referenced facts from multiple sources

**Detail Level:**
- [ ] Timeline has specific dates (not "around 2020")
- [ ] Numbers are exact (not "around $10K")
- [ ] Tech stack is complete (not just "React")
- [ ] Marketing tactics are specific (not just "did SEO")
- [ ] Financial details include breakdowns
- [ ] Founder quotes are verbatim with context

**Completeness:**
- [ ] All template sections filled (or marked N/A if truly unavailable)
- [ ] Missing information explicitly noted
- [ ] Enough detail that reader never needs to visit original sources

**Technical:**
- [ ] File named correctly: `[product-slug]-[yyyy-mm-dd].md`
- [ ] Saved in correct folder: `research/stories/`
- [ ] Markdown formatting valid

## After Research Checklist

**After completing research:**

1. ✅ Document findings in maximum detail (MANDATORY)
2. ✅ Include all source links with context (MANDATORY)
3. ✅ Save to `research/stories/[product]-[date].md` (MANDATORY)
4. ✅ Format using `markdown-formatter` skill (MANDATORY)
5. Then suggest: "Use success-formula-analyzer to extract patterns?"

**Your Purpose:** Detailed documentation, NOT analysis ✅

## Resources

- **Full Template:** `resources/STORY_TEMPLATE.md`
- **Search Strategies:** `resources/SEARCH_STRATEGIES.md`

---

**Remember:** You are a researcher, not an analyst. Document everything in rich detail. Let other skills do the analysis work.
