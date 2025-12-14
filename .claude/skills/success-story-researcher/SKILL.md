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
- Web scraping for business research

## Core Research Framework

### The 3-Layer Story Model

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

## Best Sources for Journey-Rich Stories

### Tier 1: Interview Platforms (Highest Quality)

**Indie Hackers**
- URL: `indiehackers.com/interviews`
- **Why Best:** Structured interviews with revenue data
- **Journey Coverage:** ⭐⭐⭐⭐⭐
- **Search Strategy:**
```
Site: indiehackers.com
Query: "[product name] interview"
OR: "from $0 to $X" interview
OR: "[industry] indie hacker interview"
```

**Starter Story**
- URL: `starterstory.com`
- **Why Good:** Detailed founder interviews
- **Journey Coverage:** ⭐⭐⭐⭐⭐
- **Search Strategy:**
```
Site: starterstory.com
Query: "How I built [industry] business"
OR: "How I started [product type]"
```

### Tier 2: Community Platforms (High Signal)

**Reddit**
- **r/SideProject** - Launch stories and feedback
- **r/EntrepreneurRideAlong** - Long-form journeys
- **r/SaaS** - SaaS-specific stories
- **r/IMadeThis** - Product launches

**Search Strategy:**
```
Site: reddit.com/r/EntrepreneurRideAlong
Query: "[product category] month revenue update"
OR: "My journey from 0 to X subscribers"
OR: "How I grew [product type] to $XK MRR"

Advanced:
"$X MRR" OR "$X/month" site:reddit.com/r/saas
```

**Twitter / X**
- **#buildinpublic** hashtag
- **#indiehacker** hashtag
- **#entrepreneur** threads

**Search Strategy:**
```
Site: twitter.com OR x.com
Query: #buildinpublic "[product name]"
OR: #buildinpublic "month 1" OR "week 1"
OR: "[founder name]" thread revenue

Look for thread URLs (long threads = journey stories)
```

### Tier 3: Product Hunt (Launch Data)

**Product Hunt**
- URL: `producthunt.com`
- **Why Useful:** Launch stories, early traction
- **Journey Coverage:** ⭐⭐⭐ (varies)

**Search Strategy:**
```
Site: producthunt.com
Query: "[product name]"

Then look for:
- Maker comments (founder responses)
- "Ask Me Anything" posts
- Launch day threads
```

### Tier 4: Blogs & Post-Mortems (Deep Dives)

**Personal Blogs**
- **Why Best:** Unfiltered, detailed journeys
- **Journey Coverage:** ⭐⭐⭐⭐⭐ (when found)

**Search Strategy:**
```
Google: "[product name] post-mortem"
OR: "[founder name] how I built"
OR: "[product name] journey" OR "story"
OR: "building [product name]" blog
OR: "[product name] lessons learned"
```

**Medium**
```
Site: medium.com
Query: "How I built [product]" OR "My journey building"
OR: "$0 to $X" startup story
```

**Dev.to (for developer tools)**
```
Site: dev.to
Query: "How I built [product]"
OR: "Building [product category] in public"
```

### Tier 5: Podcasts & Videos (Audio/Video Format)

**Podcasts:**
- Indie Hackers Podcast
- Startups For the Rest of Us
- My First Million
- Software Social
- Bootstrapped Web

**YouTube:**
- Pieter Levels channel
- Marc Lou channel
- Indie hacker vlogs

**Search Strategy:**
```
YouTube: "[product name] story"
OR: "How I built [product]"
OR: "[founder name] interview"

Podcast: Use Listen Notes or Spotify search
"[product name] OR [founder name]"
```

## Effective Search Query Patterns

### Pattern 1: Revenue-Based Search

```
Search Queries:
- "$0 to $10K MRR [industry]"
- "from 0 to $X in Y months"
- "[product category] revenue milestone"
- "How I reached $X/month"
- "X subscribers in Y days"

Why Effective: Revenue milestones = detailed journey stories
```

### Pattern 2: Timeline-Based Search

```
Search Queries:
- "[product] month 1" OR "week 1" OR "day 1"
- "[product] 6 month update"
- "building [product] - week X"
- "[product] one year later"

Why Effective: Timeline posts = building process documentation
```

### Pattern 3: Problem-Solution Search

```
Search Queries:
- "I built [product] because"
- "frustrated with [problem], so I built"
- "Why I created [product]"
- "[product] origin story"

Why Effective: Origin stories include motivation and early decisions
```

### Pattern 4: Launch Story Search

```
Search Queries:
- "Launching [product] on Product Hunt"
- "How I launched [product]"
- "[product] launch strategy"
- "Show HN: [product]" site:news.ycombinator.com

Why Effective: Launch stories include MVP details and early traction
```

### Pattern 5: Post-Mortem Search

```
Search Queries:
- "[product] post-mortem"
- "[product] failed OR shutdown"
- "Why [product] didn't work"
- "Lessons from [product]"

Why Effective: Failures teach as much as successes
```

### Pattern 6: Build-in-Public Search

```
Search Queries:
- "#buildinpublic [product]"
- "building [product] in public"
- "[founder] building [product]" twitter
- "[product] progress thread"

Why Effective: Real-time journeys with all the details
```

## Information Extraction Framework

### Essential Data Points

When you find a success story, your goal is to **document everything in maximum detail** without filtering or evaluating. Extract:

```markdown
## Story Extraction Template

### Product Information
- **Name:** [Product name]
- **Category:** [SaaS/App/Tool/Service]
- **URL:** [Website]
- **Launch Date:** [When launched]
- **Source URL:** [Where you found this story]

### Outcome Metrics
- **Current Revenue:** $[X]/month or $[X]/year
- **Users/Customers:** [Number]
- **Team Size:** [Number]
- **Funding:** [Bootstrapped / $X raised]
- **Time to First Revenue:** [X days/months]
- **Time to $X Revenue:** [Timeline]

### Founder Background
- **Name:** [Founder name]
- **Previous Experience:** [Background]
- **Skills:** [Technical/Marketing/etc]
- **Initial Motivation:** [Why they built it]
- **Full-time or Side Project:** [Which]

### Building Journey (MOST IMPORTANT)

**Problem Discovery:**
- [How they found the problem]
- [Validation process]

**MVP Development:**
- **Time to Build:** [X weeks/months]
- **Initial Features:** [List]
- **Tech Stack:** [Technologies used]
- **Solo or Team:** [Who built it]
- **Costs:** [Initial investment]

**Launch Strategy:**
- **Launch Platform:** [Product Hunt / HN / etc]
- **Launch Date:** [Date]
- **Launch Results:** [Metrics]
- **Pre-launch Activity:** [Email list / audience / etc]

**Growth Tactics (Chronological):**
- **Month 1-3:** [What they did]
- **Month 4-6:** [What they did]
- **Month 7-12:** [What they did]
- **Year 2+:** [What they did]

**Key Decisions:**
1. [Decision 1]: [Why made / Result]
2. [Decision 2]: [Why made / Result]
3. [Decision 3]: [Why made / Result]

**Pivots / Changes:**
- [If they changed direction, what and why]

**Marketing Channels:**
- **Primary Channel:** [What worked best]
- **Secondary Channels:** [What else worked]
- **Failed Attempts:** [What didn't work]

**Revenue Model:**
- **Pricing:** [How they charge]
- **Pricing Evolution:** [How it changed]
- **Conversion Rate:** [If mentioned]

**Challenges & Solutions:**
1. **Challenge:** [Problem faced]
   **Solution:** [How they solved it]
2. **Challenge:** [Problem faced]
   **Solution:** [How they solved it]

### All Tactics Used
[Document every tactic mentioned, without evaluating reproducibility]
1. [Tactic 1]: [How they did it, results, context]
2. [Tactic 2]: [How they did it, results, context]
3. [Tactic 3]: [How they did it, results, context]

### Founder's Lessons & Advice
[Direct quotes with full context - NO paraphrasing]
- "[Exact quote]" - [Context: when/why they said this]
- "[Exact quote]" - [Context: when/why they said this]
- "[Exact quote]" - [Context: when/why they said this]

### Source Information
- **Detail Level Available:** [What aspects had rich detail]
- **Information Gaps:** [What was missing or vague]
- **Data Currency:** [Date of most recent information]
- **Source Type:** [First-hand founder / Interview / Third-party report]
```

## Research Workflow

### Step 1: Define Search Parameters

```markdown
## Research Brief

**What I'm looking for:**
- Product category: [e.g., SaaS, mobile app, marketplace]
- Revenue range: [$X to $Y MRR]
- Team size: [Solo / 2-3 person / any]
- Industry: [Developer tools / B2B / B2C / etc]
- Timeline: [How recent - last 1 year / 2 years / any]

**Why I'm researching:**
- [To find patterns for my idea]
- [To validate approach]
- [To learn growth tactics]
```

### Step 2: Multi-Source Search

Execute searches across multiple platforms:

**Round 1: Indie Hackers (30 min)**
```
1. Search Indie Hackers interviews
2. Filter by revenue range if possible
3. Collect 3-5 most relevant stories
4. Extract using template above
```

**Round 2: Reddit (20 min)**
```
1. Search r/EntrepreneurRideAlong + r/SaaS
2. Look for "month X update" posts
3. Collect 2-3 journey stories
4. Extract key tactics
```

**Round 3: Twitter (20 min)**
```
1. Search #buildinpublic + product category
2. Find thread authors
3. Check their profiles for full journey
4. Extract timeline and tactics
```

**Round 4: Blogs & Post-Mortems (30 min)**
```
1. Google search for post-mortems
2. Look for founder blogs
3. Find Medium articles
4. Extract detailed journeys
```

### Step 3: Validate & Cross-Reference

**Validation Checklist:**
- [ ] Revenue numbers seem realistic?
- [ ] Timeline makes sense?
- [ ] Source is first-hand (founder) or credible interview?
- [ ] Enough detail to extract tactics?
- [ ] Story is recent enough (< 3 years old)?

**Cross-Reference:**
- Check multiple sources for same product
- Verify claims with external data (Product Hunt, etc)
- Look for founder social media for updates

### Step 4: Save and Prepare for Analysis

After documenting each story:

```markdown
## Your Next Step

**YOU (success-story-researcher):**
1. ✅ Saved detailed story to research/stories/
2. ✅ All sources documented with context
3. ✅ Information is rich enough to never revisit sources
4. ✅ Ready for analysis by other skills

**NEXT (use success-formula-analyzer):**
- After collecting multiple stories (5-10+)
- Run success-formula-analyzer on research/stories/
- It will extract patterns, timelines, common tactics
- It will create reports in research/reports/
- It will identify reproducible patterns

**DO NOT:**
- ❌ Try to extract patterns yourself
- ❌ Make conclusions about what works
- ❌ Evaluate reproducibility
- ❌ Compare multiple stories

Let success-formula-analyzer do the analysis work.
```

## Using WebSearch & WebFetch Tools

### WebSearch Strategy

**Basic Search:**
```
Use WebSearch for:
- Initial discovery of success stories
- Finding multiple sources
- Getting overview of available content

Example query:
"indie developer success story SaaS $10K MRR 2024"
```

**Advanced Search:**
```
Combine keywords strategically:
- Revenue keywords: "$X MRR", "revenue", "profitable"
- Journey keywords: "journey", "how I built", "story"
- Platform keywords: "indie hackers", "reddit"
- Timeline keywords: "month 1", "6 months", "one year"

Example:
"How I built SaaS $5K MRR indie hackers 2024"
```

### WebFetch Strategy

**When to Use WebFetch:**
- After finding promising URL from WebSearch
- To extract full article content
- To get interview transcripts
- To pull detailed blog posts

**Effective Prompts for WebFetch:**
```
Prompt: "Extract the founder's journey story including:
- Initial motivation
- MVP timeline and features
- Launch strategy
- Growth tactics used
- Revenue milestones and timeline
- Key lessons learned"
```

**Multi-URL Strategy:**
```
1. WebSearch: Find 5 relevant URLs
2. WebFetch URL 1: Extract story
3. WebFetch URL 2: Extract story
4. WebFetch URL 3: Extract story
5. Synthesize patterns across all 3
```

## Source Quality Assessment

### High-Quality Indicators

✅ **First-hand account** (founder writing)
✅ **Specific numbers** (revenue, users, timeline)
✅ **Detailed tactics** (not just "did marketing")
✅ **Timestamps** (month-by-month or week-by-week)
✅ **Challenges mentioned** (not just success story)
✅ **Recent** (< 2 years old for relevance)
✅ **Evidence provided** (screenshots, links)

### Low-Quality Indicators

❌ **Vague metrics** ("made some money")
❌ **No timeline** (unclear when things happened)
❌ **Third-party summary** (journalist, not founder)
❌ **Marketing fluff** (selling course, not sharing)
❌ **No failures mentioned** (too polished)
❌ **Outdated** (> 5 years old)

## Specialized Search Strategies

### Finding Build-in-Public Journeys

**Twitter Advanced Search:**
```
Search: (from:[founder_handle]) (#buildinpublic OR "building in public")

Then look for:
- Thread starters (🧵 emoji)
- "Month X update" posts
- Revenue screenshot posts
```

**Find the Founder First:**
```
1. Google: "[product name] founder"
2. Find their Twitter/X
3. Scroll through timeline for journey posts
4. Look for pinned threads
```

### Finding Post-Mortems (Failed Products)

**Why Important:** Failures teach reproducible lessons

**Search Queries:**
```
Google:
- "[product name] shut down" OR "shutting down"
- "[product name] post-mortem"
- "[product name] lessons learned"
- "Why [product name] failed"

Reddit:
- site:reddit.com "shut down my startup"
- site:reddit.com "failed side project lessons"
```

### Finding Niche-Specific Stories

**Developer Tools:**
```
- site:dev.to "How I built"
- site:hashnode.com "developer tool" journey
- site:news.ycombinator.com "Show HN" [category]
```

**B2B SaaS:**
```
- site:saastr.com founder story
- "B2B SaaS" revenue journey
- LinkedIn articles by founders
```

**E-commerce / Physical Products:**
```
- site:reddit.com/r/ecommerce success story
- Shopify blog case studies
- "Shopify store" revenue journey
```

## Research Deliverable

**Your deliverable is ALWAYS:**
```
research/stories/[product-slug]-[yyyy-mm-dd].md
```

**One file per success story.**

Each file contains:
- Complete story documentation
- Maximum detail without analysis
- All sources with context
- Rich information for later analysis

**If user asks for multiple stories:**
```
User: "Research 5 SaaS success stories"

You: Document 5 separate files:
- research/stories/product-1-2024-12-10.md
- research/stories/product-2-2024-12-10.md
- research/stories/product-3-2024-12-10.md
- research/stories/product-4-2024-12-10.md
- research/stories/product-5-2024-12-10.md

Then suggest:
"Stories documented. Use success-formula-analyzer to extract patterns?"
```

**DO NOT create:**
- ❌ Multi-story comparison reports
- ❌ Pattern analysis documents
- ❌ Benchmark tables across stories
- ❌ Recommendations based on patterns

**These are created by `success-formula-analyzer`.**

## Quick Reference: Best Queries by Goal

### Goal: Find Similar Product Success Stories

```
Primary: site:indiehackers.com "[product category]" interview
Secondary: "[product category] success story" revenue
Tertiary: site:reddit.com/r/saas "[product category]" MRR
```

### Goal: Find Launch Strategies

```
Primary: "launching on Product Hunt" [product category]
Secondary: site:indiehackers.com "launch strategy"
Tertiary: "how I launched" [product category] blog
```

### Goal: Find Growth Tactics

```
Primary: "[product category] growth tactics" indie
Secondary: site:reddit.com/r/entrepreneur "how I grew"
Tertiary: #buildinpublic [product category] twitter growth
```

### Goal: Find Revenue Journeys

```
Primary: "$0 to $10K MRR" [category]
Secondary: site:indiehackers.com revenue milestone
Tertiary: "revenue update" month site:reddit.com
```

### Goal: Find Founder Background Stories

```
Primary: "[founder name]" story OR journey
Secondary: "[founder name]" twitter thread
Tertiary: "[founder name]" interview podcast
```

## Advanced Techniques

### Reverse Engineering Success

**Process:**
1. Find successful product
2. Use Wayback Machine (archive.org) to see original version
3. Track changes over time
4. Identify what changed and when
5. Correlate with growth periods

**Example:**
```
1. Find product: ConvertKit
2. Archive.org: web.archive.org/web/*/convertkit.com
3. Look at snapshots: Jan 2014, Jan 2015, Jan 2016
4. See feature additions, messaging changes
5. Cross-reference with founder blog posts
```

**Reference:**
- [ConvertKit](https://convertkit.com/)
- [Nathan Barry (Founder) Blog](https://nathanbarry.com/)
- [Wayback Machine - ConvertKit](https://web.archive.org/web/*/convertkit.com)

### Following the Founder

**Process:**
1. Find founder's social media (Twitter/X primary)
2. Use advanced search: (from:username) since:2020-01-01
3. Look for build-in-public threads
4. Find all revenue updates
5. Compile timeline

**Tools:**
- Twitter Advanced Search
- Thread Reader App (unroll long threads)
- Dewey (bookmark Twitter threads)

### Network Effect Research

**Process:**
1. Find one successful founder
2. See who they interact with (replies, mentions)
3. Check those people's profiles
4. Often find similar journey stories
5. Build database of multiple stories

**Example:**
```
1. Research: Pieter Levels (@levelsio)
2. See who he replies to often
3. Find: Marc Lou (@marc_louvion), Tony Dinh (@tdinh_me)
4. Research their journeys too
5. Extract common patterns
```

**Reference:**
- [Pieter Levels Twitter](https://twitter.com/levelsio)
- [Marc Lou Twitter](https://twitter.com/marc_louvion)
- [Tony Dinh Twitter](https://twitter.com/tdinh_me)
- [Pieter Levels Blog](https://levels.io/)

## Troubleshooting

### "Can't find detailed journey stories"

**Solutions:**
- Search for older content (2015-2020 had more detail)
- Look for podcast transcripts instead of articles
- Check founder's personal blog (not company blog)
- Search for "lessons learned" instead of "success story"

### "Stories are too high-level"

**Solutions:**
- Look for build-in-public Twitter threads (most detailed)
- Search for "month X update" (more tactical)
- Find post-mortems (often more honest/detailed)
- Search Reddit over Medium (more authentic)

### "Information is outdated"

**Solutions:**
- Add year to search: "success story 2024"
- Sort by date in search engines
- Follow current #buildinpublic founders
- Check Indie Hackers recent interviews

### "Too many results, can't filter"

**Solutions:**
- Add revenue filter: "$10K MRR" narrows significantly
- Add platform: site:indiehackers.com
- Add timeline: "6 months" OR "1 year"
- Add founder attribute: "solo founder"

---

## File Storage Rules

### IMPORTANT: Always Save Research Results

**When you complete research, you MUST:**
1. ✅ Save findings to markdown file
2. ✅ Include all source links
3. ✅ Follow naming conventions
4. ✅ Use appropriate folder

### File Structure

```
research/
├── stories/          # Individual product success stories
│   └── [product-slug]-[yyyy-mm-dd].md
├── reports/          # Comprehensive analysis reports
│   └── [topic]-analysis-[yyyy-mm-dd].md
└── patterns/         # Extracted common patterns
    └── [pattern-name].md
```

### When to Save Where

**Individual Story → `research/stories/` ⭐ PRIMARY FOCUS**
- **ALWAYS** one file per case (product or person)
- Detailed documentation of a single success story
- Example: "Research Gumroad success story"
- Filename: `gumroad-2024-12-10.md`
- **THIS IS YOUR MAIN JOB**

**Multiple Stories Analysis → `research/reports/`**
- ❌ **NOT your job** - this is for `success-formula-analyzer`
- Pattern extraction from multiple stories
- Cross-story comparisons
- Benchmarks and recommendations
- Example: success-formula-analyzer creates `saas-patterns-2024-12-10.md`

**Extracted Pattern → `research/patterns/`**
- ❌ **NOT your job** - this is for `success-formula-analyzer`
- Reproducible success patterns
- Validated across multiple stories
- Example: success-formula-analyzer creates `build-in-public-strategy.md`

**Your Focus:**
- ✅ Document ONE story per file in research/stories/
- ✅ Maximum detail for that single case
- ✅ Let success-formula-analyzer do the pattern extraction

### File Naming Rules

**Product Slug:**
- All lowercase
- Replace spaces with hyphens
- Remove special characters
- Examples:
  - "Notion" → `notion`
  - "ConvertKit" → `convertkit`
  - "Dev Utils" → `dev-utils`

**Topic Slug:**
- Descriptive and specific
- Use hyphens between words
- Examples:
  - `saas-10k-mrr-analysis`
  - `developer-tools-patterns`
  - `bootstrapped-comparison`

**Date Format:**
- Always: `yyyy-mm-dd`
- Example: `2024-12-10`

### Markdown Template for Stories

```markdown
# [Product Name] Success Story

**Research Date:** [Today's date]
**Category:** [SaaS / App / Tool / Marketplace / etc]
**Revenue Range:** [$X - $Y MRR or ARR]
**Team Size:** [Solo / 2-3 / 4-10 / etc]
**Status:** [Active / Acquired / Shut down]

---

## Quick Facts

| Metric | Value |
|--------|-------|
| **Product** | [Name] |
| **Website** | [URL] |
| **Founded** | [Date] |
| **Founder(s)** | [Name(s)] |
| **Current Revenue** | [$X/month or $X/year] |
| **Users/Customers** | [Number] |
| **Team Size** | [Number] |
| **Funding** | [Bootstrapped / $X raised] |
| **Time to First Revenue** | [X months] |
| **Time to $10K MRR** | [X months] |

---

## The Story

### Problem Discovery

[How they identified the problem]
- [Key insight 1]
- [Key insight 2]

### MVP Development

**Timeline:** [X weeks/months]

**Initial Features:**
- [Feature 1]
- [Feature 2]
- [Feature 3]

**Tech Stack:**
- Frontend: [Technology]
- Backend: [Technology]
- Database: [Technology]
- Infrastructure: [Platform]

**Development Process:**
- [Key decision 1]
- [Key decision 2]

### Launch Strategy

**Platform:** [Product Hunt / Hacker News / Reddit / etc]
**Date:** [Launch date]

**Pre-launch:**
- [Activity 1]
- [Activity 2]

**Launch Results:**
- [Metric 1]
- [Metric 2]

### Growth Journey

#### Phase 1: Early Days (Month 0-3)
- [What happened]
- [Key tactic]
- [Result]

#### Phase 2: Finding Traction (Month 4-6)
- [What happened]
- [Key tactic]
- [Result]

#### Phase 3: Scaling (Month 7-12)
- [What happened]
- [Key tactic]
- [Result]

#### Phase 4: Mature Growth (Year 2+)
- [What happened]
- [Key tactic]
- [Result]

### Key Decisions

1. **[Decision 1]**
   - **Why:** [Reasoning]
   - **Result:** [Outcome]

2. **[Decision 2]**
   - **Why:** [Reasoning]
   - **Result:** [Outcome]

### Pivots & Changes

- **[Change 1]:** [What changed and why]
- **[Change 2]:** [What changed and why]

### Marketing Channels

**Primary Channel:** [What worked best]
- [Tactic details]

**Secondary Channels:**
- [Channel 1]: [Results]
- [Channel 2]: [Results]

**Failed Attempts:**
- [What didn't work and why]

### Revenue Model

**Pricing:** [How they charge]

**Pricing Evolution:**
- [Initial]: [Price]
- [Current]: [Price]
- [Changes]: [Why changed]

**Conversion Rate:** [X%] (if mentioned)

### Challenges & Solutions

1. **Challenge:** [Problem faced]
   - **Solution:** [How they solved it]
   - **Result:** [Outcome]

2. **Challenge:** [Problem faced]
   - **Solution:** [How they solved it]
   - **Result:** [Outcome]

---

## All Tactics & Strategies Used

### Tactic 1: [Name]
- **What They Did:** [Exact description]
- **How They Implemented:** [Detailed steps]
- **Context:** [Why they chose this, what stage]
- **Results Achieved:** [Specific outcomes]
- **Time Investment:** [Hours/days]
- **Cost:** [$ if mentioned]

### Tactic 2: [Name]
[Same format]

### Tactic 3: [Name]
[Same format]

**Note:** List ALL tactics mentioned, regardless of whether they seem reproducible. Let `success-formula-analyzer` evaluate reproducibility later.

---

## Founder's Lessons & Reflections

### What They Say Worked
> "[Direct quote about what worked]" - [Context]

> "[Direct quote about what worked]" - [Context]

- [Additional lesson in their own words]

### What They Say Didn't Work
> "[Direct quote about what failed]" - [Context]

> "[Direct quote about what failed]" - [Context]

- [Additional lesson in their own words]

### Their Advice to Others
> "[Exact quote of advice]" - [Context: to whom, when]

> "[Exact quote of advice]" - [Context: to whom, when]

**Note:** Use direct quotes whenever possible. If paraphrasing, clearly mark as [Paraphrased] and cite source.

---

## Timeline Summary

```
Month 0:  [Milestone]
Month 1:  [Milestone]
Month 3:  [Milestone]
Month 6:  [Milestone]
Month 12: [Milestone]
Year 2:   [Milestone]
Current:  [Current status]
```

---

## Detailed Information

### Complete Tech Stack & Tools

**Development:**
- Frontend: [Framework, libraries, UI components]
- Backend: [Language, framework, APIs]
- Database: [Type, hosting]
- Infrastructure: [Hosting, CDN, services]

**Tools Used:**
- Design: [Figma, Sketch, etc]
- Development: [IDE, tools]
- Marketing: [Email, analytics, CRM]
- Operations: [Payment, support, monitoring]

**Integrations:**
- [Service 1]: [Why and how used]
- [Service 2]: [Why and how used]

### Founder's Mindset & Decision-Making

**Initial Beliefs:**
- [What they believed when starting]
- [Assumptions they had]

**Changed Beliefs:**
- [What changed over time]
- [What they learned was wrong]

**Critical Decisions Explained:**
1. **[Decision]**
   - **Context:** [Situation]
   - **Options Considered:** [Alternatives]
   - **Why Chose This:** [Reasoning]
   - **Outcome:** [What happened]

### Marketing Channel Breakdown

**Channel 1: [Name]**
- **When Started:** [Timeline]
- **Specific Tactics:** [Detailed tactics]
- **Time Investment:** [Hours/week]
- **Cost:** [$ if paid]
- **Results:** [Metrics]
- **Lessons:** [What worked/didn't]

**Channel 2: [Name]**
- [Same structure]

### Financial Breakdown

**Initial Investment:**
- [Cost item 1]: [$X]
- [Cost item 2]: [$X]
- **Total:** [$X]

**Monthly Costs (at different stages):**
- **Month 1:** [$X] - [Breakdown]
- **Month 6:** [$X] - [Breakdown]
- **Month 12:** [$X] - [Breakdown]
- **Current:** [$X] - [Breakdown]

**Revenue Breakdown:**
- **Revenue Streams:** [Multiple if applicable]
- **Customer LTV:** [$X]
- **CAC:** [$X]
- **Churn Rate:** [X%]
- **Margins:** [X%]

### Metrics & KPIs Tracked

**What They Measured:**
- [Metric 1]: [How tracked]
- [Metric 2]: [How tracked]

**What They Ignored (and why):**
- [Metric]: [Reason]

**Key Insights from Data:**
- [Data insight 1]
- [Data insight 2]

### Founder Quotes & Insights

> [Direct quote 1 with context]

> [Direct quote 2 with context]

> [Direct quote 3 with context]

**In Their Own Words:**
- On [Topic]: "[Quote]"
- On [Topic]: "[Quote]"

---

## Sources

### Primary Sources (Founder First-hand)

1. **[Source Title](URL)**
   - **Type:** Interview / Blog post / Tweet thread / Podcast / Video
   - **Date Published:** YYYY-MM-DD
   - **Date Accessed:** YYYY-MM-DD
   - **Quality:** ⭐⭐⭐⭐⭐
   - **Content Coverage:** [What topics covered]
   - **Information Extracted:**
     - ✅ [Specific info 1 from this source]
     - ✅ [Specific info 2 from this source]
     - ✅ [Specific info 3 from this source]
   - **Notable Quotes:** [Any key quotes from this source]
   - **Reliability Notes:** [Why this source is reliable]

2. **[Source Title](URL)**
   - [Same format]

### Secondary Sources (Third-party)

1. **[Source Title](URL)**
   - **Type:** News article / Case study / Third-party interview
   - **Author/Publisher:** [Name]
   - **Date Published:** YYYY-MM-DD
   - **Date Accessed:** YYYY-MM-DD
   - **Quality:** ⭐⭐⭐
   - **Cross-Referenced With:** [Primary source that validates this]
   - **Information Extracted:**
     - [Specific info from this source]
   - **Reliability Notes:** [Caveats or validation notes]

### Community Discussions & Social Media

**Twitter/X Threads:**
- [Thread Title](URL) - [Date] - [What info provided]

**Reddit Posts:**
- [Post Title](URL) - [Subreddit] - [Date] - [What info provided]

**Forum Discussions:**
- [Discussion Title](URL) - [Platform] - [Date] - [What info provided]

### Additional References

**Founder Social Media:**
- Twitter/X: [@handle](URL)
- LinkedIn: [URL]
- Personal Blog: [URL]
- YouTube: [URL]

**Product Resources:**
- Product Website: [URL]
- Product Hunt Page: [URL]
- GitHub: [URL] (if open source)
- Demo/Screenshots: [URL]

**Related Articles:**
- [Article 1 Title](URL) - [Brief description]
- [Article 2 Title](URL) - [Brief description]

---

## Research Metadata

**Research Quality:** [High / Medium / Low]
- **Completeness:** [% of template filled]
- **Source Diversity:** [Number of different source types]
- **First-hand Content:** [% from founder directly]
- **Data Recency:** [How recent is the data]

**Research Process:**
- **Time Spent:** [X hours]
- **Sources Reviewed:** [Total number]
- **Sources Used:** [Number cited above]
- **Search Queries Used:** [List key queries]

**Missing Information:**
- [ ] [What info couldn't be found]
- [ ] [What would make this more complete]

**Researcher Notes:**
[Any additional observations, caveats, or context needed to interpret this story]

**Validation Status:**
- [ ] Revenue numbers cross-referenced
- [ ] Timeline verified from multiple sources
- [ ] Founder identity confirmed
- [ ] Product still active/findable

**Follow-up Opportunities:**
- [Where to look for updates]
- [Potential for more detailed info]

---

**Last Updated:** [Date]
**Next Review Date:** [Date +6 months]
```

### Reports Template (NOT YOUR JOB)

**Note:** Reports are created by `success-formula-analyzer`, not by you.

After you document multiple stories in `research/stories/`, the user can invoke:
```
"Use success-formula-analyzer to analyze all stories in research/stories/"
```

The analyzer will:
- Read all your detailed story files
- Extract common patterns
- Compare timelines and tactics
- Identify what works across multiple cases
- Create reports in `research/reports/`

**Your job:** Document individual stories with maximum detail.
**Analyzer's job:** Find patterns across your documented stories.

### Must-Include Elements

Every research file MUST include:

1. ✅ **Complete Sources:** Every URL, date accessed, what info extracted from each
2. ✅ **Detailed Timeline:** Specific dates, not vague timeframes
3. ✅ **Concrete Numbers:** Exact revenue, costs, metrics - no "approximately"
4. ✅ **Founder's Voice:** Direct quotes, their explanations, decision rationale
5. ✅ **Tech & Tools:** Complete stack, all tools used, why chosen
6. ✅ **Financial Details:** All costs, revenue breakdown, margins
7. ✅ **Marketing Specifics:** Exact tactics, time/money invested, results
8. ✅ **Context:** Why decisions made, what alternatives considered

**DO NOT Include:**
- ❌ Your analysis or opinion
- ❌ Reproducibility scores
- ❌ Applicability assessments
- ❌ Success factor ratings
- ❌ Pattern conclusions

**These are for `success-formula-analyzer` to determine later.**

### Quality Checklist for Detailed Recording

**Before saving, verify information richness:**

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
- [ ] Missing information explicitly noted in Research Metadata
- [ ] Enough detail that reader never needs to visit original sources
- [ ] Context provided for all major decisions

**Technical:**
- [ ] File named correctly: `[product-slug]-[yyyy-mm-dd].md`
- [ ] Saved in correct folder: `research/stories/`
- [ ] Markdown formatting valid
- [ ] All links working

---

## Workflow: Research → Document → Save

### Step 1: Deep Research (WebSearch/WebFetch)
```
User: "Research Gumroad success story"

Claude:
1. Use WebSearch to find multiple sources (aim for 5+)
2. Use WebFetch to extract full details from each
3. Cross-reference information between sources
4. Look for founder first-hand accounts
5. Find specific numbers, dates, quotes
```

### Step 2: Detailed Documentation (Fill Template)
```
Claude:
1. Start with Stories template
2. Fill EVERY section with maximum detail
3. Include direct quotes with context
4. Document all numbers, dates, specifics
5. Explain WHY decisions were made
6. List what info came from which source
```

### Step 3: Source Documentation (CRITICAL)
```
Claude:
1. List every URL used
2. For each source, document:
   - Date published
   - Date accessed
   - What specific information came from it
   - Quality/reliability assessment
3. Add founder social media links
4. Note any missing information
```

### Step 4: Save to Markdown (REQUIRED)
```
Claude:
1. Choose correct folder: research/stories/
2. Create filename: [product-slug]-[yyyy-mm-dd].md
3. Save complete document
4. Verify all links work
```

### Step 5: Confirm Completeness
```
Claude: "✅ Detailed story documented and saved to:
research/stories/gumroad-2024-12-10.md

**Completeness Check:**
- Sources: [X] sources ([Y] primary, [Z] secondary)
- Detail Level: [High/Medium/Low]
- Timeline: [Covers X months/years]
- Missing Info: [List what couldn't be found]

**File is ready for:**
- ✅ success-formula-analyzer to extract patterns
- ✅ business-idea-evaluator for comparison
- ✅ Future reference without revisiting sources

Would you like me to:
- Research another story?
- Use success-formula-analyzer to extract patterns?
- Compare with another product?"
```

## Integration with Other Skills

**success-story-researcher** creates **raw, detailed records**.
Other skills use these records for analysis:

### After Documenting a Story

**→ success-formula-analyzer**
```
"Analyze patterns from research/stories/gumroad-2024-12-10.md"
```
- Reads the detailed story you documented
- Extracts reproducible success patterns
- Creates pattern files in research/patterns/

**→ business-idea-evaluator**
```
"Compare my idea with Gumroad story"
```
- Uses the detailed information to benchmark your idea
- Identifies similar success factors
- Evaluates if your approach matches proven patterns

**→ Multiple Story Analysis**
```
"Analyze all stories in research/stories/ and extract common patterns"
```
- success-formula-analyzer reads all your documented stories
- Creates comprehensive pattern analysis
- Saves to research/reports/

### Your Role vs Analyzer's Role

**success-story-researcher (YOU):**
- ✅ Find and document detailed information
- ✅ Record everything without filtering
- ✅ Provide rich context and quotes
- ✅ List all sources meticulously
- ❌ DO NOT analyze or conclude

**success-formula-analyzer (SEPARATE SKILL):**
- Reads your detailed records
- Identifies common patterns
- Extracts reproducible tactics
- Rates reproducibility
- Makes recommendations

**This separation ensures:**
- Your stories remain objective and factual
- Analysis can be re-run with new criteria
- Multiple stories can be compared
- Patterns emerge from data, not bias

---

**After Research:**
1. ✅ DOCUMENT findings in maximum detail (MANDATORY)
2. ✅ Include all source links with context (MANDATORY)
3. ✅ Save to research/stories/[product]-[date].md (MANDATORY)
4. Then use success-formula-analyzer to extract patterns
5. Then use business-idea-evaluator to apply insights
6. Then use feasibility-checker to validate tactics
7. Then use business-orchestrator for integrated plan

**Skill Purpose:** Detailed documentation, NOT analysis ✅
