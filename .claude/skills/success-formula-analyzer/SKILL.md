---
name: success-formula-analyzer
description: Analyze successful indie developers and small team businesses to extract reproducible success formulas. Use when researching success patterns, analyzing revenue models, studying product-market fit, examining marketing strategies, or understanding what makes solo/small team products profitable. Covers pattern extraction, revenue analysis, growth tactics, and methodology replication for 1-person or small development teams.
---

# Success Formula Analyzer

## Purpose

Extract and analyze reproducible success patterns from successful indie developers and small team businesses. Transform case studies into actionable formulas that can be applied to new business ideas.

## When to Use This Skill

Automatically activates when you mention:
- Success patterns or formulas
- Indie developer success stories
- Revenue models for solo developers
- Product-market fit analysis
- Small team business strategies
- Analyzing what makes products profitable
- Learning from successful cases
- Reproducible business methods
- Solo founder strategies
- Bootstrapped business models

## Core Analysis Framework

### 1. Success Pattern Extraction

When analyzing a successful case, extract:

**Product Characteristics:**
- What problem does it solve?
- Target audience size and characteristics
- Unique value proposition
- Product complexity (MVP vs full-featured)
- Time to first revenue
- Tech stack simplicity

**Revenue Model:**
- Pricing strategy (one-time, subscription, freemium)
- Average revenue per user (ARPU)
- Customer acquisition cost (CAC)
- Lifetime value (LTV)
- Revenue milestones and timeline
- Multiple revenue streams?

**Distribution & Marketing:**
- Primary customer acquisition channel
- Marketing budget (if any)
- Community building approach
- Content marketing strategy
- SEO/SEM approach
- Word-of-mouth mechanics
- Launch strategy

**Founder Characteristics:**
- Solo or team?
- Technical background
- Previous experience
- Time invested
- Initial capital invested
- Skills leveraged

### 2. Success Formula Template

```markdown
## [Product Name] Success Formula

### The Core Pattern
[One sentence describing the essence of their success]

### Key Ingredients
1. **Problem**: [Specific pain point addressed]
2. **Solution**: [Simple description of the product]
3. **Market**: [Target audience size and characteristics]
4. **Differentiation**: [What makes it different/better]
5. **Monetization**: [How they make money]
6. **Distribution**: [How they reach customers]

### Numbers That Matter
- Time to Build: [X weeks/months]
- Time to First Revenue: [X days/months]
- Initial Investment: [$X or sweat equity]
- Current Revenue: [$X/month or $X/year]
- Growth Rate: [X% month-over-month]
- Team Size: [X people]

### Reproducible Tactics
1. [Specific tactic 1 with details]
2. [Specific tactic 2 with details]
3. [Specific tactic 3 with details]

### Warning Signs / Prerequisites
- Skills required: [List]
- Capital required: [Amount]
- Time commitment: [Hours/week]
- Market timing considerations: [Any]
```

### 3. Pattern Classification System

When extracting patterns from success stories, classify them into these categories:

**Common Patterns** (`research/patterns/common/`)
- Patterns that ALL successful businesses do regardless of niche
- Universal best practices (validate before building, focus on distribution, etc.)
- Non-negotiable fundamentals
- Save as: `research/patterns/common/[pattern-name].md`

**Idea Discovery Patterns** (`research/patterns/idea-discovery/`)
- How founders found their business ideas
- Methods for identifying opportunities
- Ranked by success probability (highest first)
- Save as: `research/patterns/idea-discovery/[method-name].md`
- Examples: scratch-your-own-itch, observe-market-gaps, productize-services

**Validation Patterns** (`research/patterns/validation/`)
- How founders validated ideas before building
- Testing methods and experiments
- Ranked by reliability (most reliable first)
- Save as: `research/patterns/validation/[method-name].md`
- Examples: landing-page-test, manual-first-approach, pre-sell-validation

**MVP Building Patterns** (`research/patterns/mvp-building/`)
- Strategies for building minimum viable products
- Speed vs quality tradeoffs
- Ranked by speed-to-market (fastest first)
- Save as: `research/patterns/mvp-building/[strategy-name].md`
- Examples: no-code-first, manual-behind-curtain, feature-prioritization

**Customer Acquisition Patterns** (`research/patterns/customer-acquisition/`)
- How founders got their first 10-100 customers
- Early customer finding tactics
- Ranked by effectiveness for cold start (most effective first)
- Save as: `research/patterns/customer-acquisition/[tactic-name].md`
- Examples: direct-outreach, founder-led-sales, niche-community-targeting

**Product-Market Fit Patterns** (`research/patterns/product-market-fit/`)
- How founders achieved and recognized PMF
- Iteration and feedback strategies
- Ranked by signal clarity (clearest signals first)
- Save as: `research/patterns/product-market-fit/[method-name].md`
- Examples: iterate-with-feedback, retention-over-acquisition, find-power-users

**Growth Patterns** (`research/patterns/growth/`)
- Strategies for scaling after achieving PMF
- Marketing and distribution channels
- Ranked by ROI (highest ROI first)
- Save as: `research/patterns/growth/[strategy-name].md`
- Examples: content-marketing, seo-driven-growth, viral-mechanics

**Monetization Patterns** (`research/patterns/monetization/`)
- Business models and pricing strategies
- Revenue optimization tactics
- Ranked by predictability (most predictable first)
- Save as: `research/patterns/monetization/[model-name].md`
- Examples: freemium-to-paid, usage-based-pricing, lifetime-deals

**Distribution Patterns** (`research/patterns/distribution/`)
- Channels and platforms for reaching customers
- Partnership and integration strategies
- Ranked by leverage (highest leverage first)
- Save as: `research/patterns/distribution/[channel-name].md`
- Examples: app-store-optimization, marketplace-strategy, integration-ecosystem

**Retention Patterns** (`research/patterns/retention/`)
- Strategies for keeping customers long-term
- Churn reduction tactics
- Ranked by impact (highest impact first)
- Save as: `research/patterns/retention/[tactic-name].md`
- Examples: onboarding-excellence, habit-forming-features, community-engagement

**Differentiation Patterns** (`research/patterns/differentiation/`)
- How founders stood out in crowded markets
- Unique positioning strategies
- Ranked by defensibility (most defensible first)
- Save as: `research/patterns/differentiation/[strategy-name].md`
- Examples: niche-specialization, unique-positioning, design-as-differentiator

## Analysis Process

### Step 1: Case Study Research

```markdown
## Research Checklist

- [ ] Product launch date and timeline
- [ ] Founder background and story
- [ ] Initial problem/opportunity identified (→ idea-discovery pattern)
- [ ] How they validated before building (→ validation pattern)
- [ ] MVP features and complexity (→ mvp-building pattern)
- [ ] First 10-100 customers strategy (→ customer-acquisition pattern)
- [ ] Product-market fit signals (→ product-market-fit pattern)
- [ ] Growth strategy and channels (→ growth pattern)
- [ ] Business model and pricing (→ monetization pattern)
- [ ] Distribution channels used (→ distribution pattern)
- [ ] Customer retention tactics (→ retention pattern)
- [ ] Differentiation strategy (→ differentiation pattern)
- [ ] Revenue milestones
- [ ] Current state (users, revenue, team)
- [ ] Key challenges overcome
- [ ] Lessons learned (from founder)
```

**Sources to Check:**
- Indie Hackers interviews
- Reddit (r/SideProject, r/EntrepreneurRideAlong)
- Twitter threads by founders
- Podcast interviews
- Blog post-mortems
- GitHub stars/activity (if open source)
- Product Hunt launch data

### Step 2: Extract and Classify Patterns

For EACH success story analyzed, extract patterns into the classification system:

**1. Identify Common Patterns First**
- What universal practices did they follow?
- What fundamentals were non-negotiable?
- Save to `research/patterns/common/[pattern-name].md`

**2. Extract Stage-Specific Patterns**
Go through each category and extract specific methods/tactics:

- **How did they find the idea?** → `idea-discovery/[method].md`
- **How did they validate it?** → `validation/[method].md`
- **How did they build the MVP?** → `mvp-building/[strategy].md`
- **How did they get first customers?** → `customer-acquisition/[tactic].md`
- **How did they achieve PMF?** → `product-market-fit/[method].md`
- **How did they grow?** → `growth/[strategy].md`
- **What's their business model?** → `monetization/[model].md`
- **What distribution channels?** → `distribution/[channel].md`
- **How do they retain customers?** → `retention/[tactic].md`
- **How do they differentiate?** → `differentiation/[strategy].md`

**3. Rank by Success Probability**
Within each pattern file, list specific tactics ranked by:
- Success probability (for discovery/validation)
- Speed to market (for MVP)
- Effectiveness (for acquisition/retention)
- ROI (for growth)
- Predictability (for monetization)
- Leverage (for distribution)
- Defensibility (for differentiation)

### Step 3: Pattern File Template

Each pattern file should follow this structure:

```markdown
# [Pattern Name]

**Category:** [common/idea-discovery/validation/etc.]
**Success Rate:** [High/Medium/Low based on evidence]
**Time Investment:** [Typical time required]
**Difficulty:** [Easy/Medium/Hard for solo founders]

## What Is This Pattern?

[Clear description of the pattern in 2-3 sentences]

## How It Works

[Step-by-step breakdown of the pattern]

1. **Step 1**: [Description]
2. **Step 2**: [Description]
3. **Step 3**: [Description]

## Real Examples (Ranked by Success)

### 1. [Product Name] - [Outcome]
- **Context**: [Brief background]
- **Execution**: [How they applied this pattern]
- **Results**: [Specific metrics/outcomes]
- **Key Insight**: [What made it work]

### 2. [Product Name] - [Outcome]
[Same structure...]

### 3. [Product Name] - [Outcome]
[Same structure...]

## Why This Works

[Analysis of success factors]

## Prerequisites

- **Skills Required**: [List]
- **Time Required**: [Estimate]
- **Capital Required**: [Estimate]
- **Other Requirements**: [Any]

## Common Mistakes

1. **Mistake**: [Description]
   - **Why It Fails**: [Explanation]
   - **How to Avoid**: [Solution]

2. [More mistakes...]

## When to Use This Pattern

✅ **Good Fit When:**
- [Condition 1]
- [Condition 2]

❌ **Bad Fit When:**
- [Condition 1]
- [Condition 2]

## Related Patterns

- [Link to related pattern in another category]
- [Link to prerequisite pattern]
- [Link to follow-up pattern]

## Sources

- [Product Name]: [URL] (accessed YYYY-MM-DD)
- [Article/Interview]: [URL] (accessed YYYY-MM-DD)
```

### Step 4: Cross-Pattern Analysis

After extracting individual patterns, look for combinations:

**Successful Pattern Combinations:**
```markdown
## Pattern Combo: [Name]

**Patterns Used:**
1. [Pattern from idea-discovery]
2. [Pattern from validation]
3. [Pattern from mvp-building]
4. [Pattern from customer-acquisition]

**Why This Combo Works:**
[Analysis]

**Examples:**
- [Product 1]: [How they combined these]
- [Product 2]: [How they combined these]
```

## Output Format

### When Analyzing Multiple Stories

Create a comprehensive analysis report at `research/reports/[topic]-patterns-[yyyy-mm-dd].md`:

```markdown
# [Topic] Pattern Analysis

**Analysis Date:** YYYY-MM-DD
**Stories Analyzed:** [N] success stories
**Categories Covered:** [List of pattern categories found]

## Common Patterns Identified

### [Pattern Name 1]
- **Found in:** [X/N] stories ([X]%)
- **Category:** common
- **Success Rate:** High/Medium/Low
- **Key Characteristics:** [Brief description]
- **Examples:** [Product 1], [Product 2], [Product 3]

[Repeat for each common pattern...]

## Idea Discovery Patterns (Ranked by Success Rate)

### 1. [Highest Success Pattern]
- **Found in:** [X/N] stories
- **Success Rate:** [X]%
- **Examples:** [Products that used this]
- **Key Insight:** [Why this works]

### 2. [Second Highest...]

[Continue ranking...]

## [Repeat for Each Category]

- Validation Patterns
- MVP Building Patterns
- Customer Acquisition Patterns
- Product-Market Fit Patterns
- Growth Patterns
- Monetization Patterns
- Distribution Patterns
- Retention Patterns
- Differentiation Patterns

## Pattern Combinations

### Combo 1: [Name] (Found in [X] stories)
- **Pattern Mix:**
  - Idea Discovery: [Pattern name]
  - Validation: [Pattern name]
  - MVP: [Pattern name]
  - Acquisition: [Pattern name]
- **Success Rate:** [X]%
- **Examples:** [Products]

## Recommendations by Use Case

### For Finding Ideas:
1. [Top pattern] - [Success rate]
2. [Second pattern] - [Success rate]

### For Validating Ideas:
1. [Top pattern] - [Reliability rate]
2. [Second pattern] - [Reliability rate]

[Continue for each category...]

## Meta Insights

- **Most common success path:** [Pattern combo description]
- **Fastest path to revenue:** [Pattern combo]
- **Highest success probability:** [Pattern combo]
- **Best for solo founders:** [Pattern combo]

## Individual Pattern Files Created

- `common/[pattern-name].md` ([N] files)
- `idea-discovery/[pattern-name].md` ([N] files)
- `validation/[pattern-name].md` ([N] files)
[List all pattern files created...]
```

### When Analyzing Single Story

Extract all applicable patterns and either:
1. Update existing pattern files with new example
2. Create new pattern files if pattern is novel

Always maintain ranking within each pattern file based on evidence.

## Red Flags to Avoid

### Anti-Patterns

❌ **Building in Vacuum**
- Not talking to potential customers before building
- Assuming you know what people want
- Over-engineering the first version

❌ **Competitive Markets Without Differentiation**
- Entering saturated market with "me too" product
- Competing on price alone
- No clear reason to switch from existing solutions

❌ **Complex Products for Small Markets**
- Building Salesforce competitor as solo developer
- Requiring months/years of development
- Difficult to support at scale

❌ **No Clear Monetization**
- "We'll figure out how to make money later"
- Relying on ads with small audience
- Underpricing significantly

❌ **Ignoring Distribution**
- "Build it and they will come" mentality
- No plan for customer acquisition
- No existing audience or distribution channel

## Success Metrics to Track

### Early Stage (0-3 months)
- Customer conversations conducted
- MVP completion percentage
- Email list signups (if applicable)
- Social media engagement

### Growth Stage (3-12 months)
- Monthly Recurring Revenue (MRR)
- Customer Acquisition Cost (CAC)
- User retention rate
- Feature usage metrics
- Customer feedback themes

### Mature Stage (12+ months)
- MRR growth rate
- Churn rate
- Lifetime Value (LTV)
- LTV:CAC ratio (should be > 3:1)
- Net Promoter Score (NPS)
- Revenue per employee

## Framework Application

### How to Use This Analysis on Your Idea

1. **Identify Similar Successful Cases**
   - Find 3-5 products in similar space
   - Or similar business models in different spaces
   - Research their journey thoroughly

2. **Extract Common Patterns**
   - What did they all do similarly?
   - What were the critical success factors?
   - What was the typical timeline?

3. **Adapt to Your Context**
   - What parts are reproducible for you?
   - What skills/resources do you have?
   - What can you do differently/better?

4. **Create Your Formula**
   - Combine proven patterns with your advantages
   - Identify potential pitfalls specific to your case
   - Set realistic milestones based on similar cases

5. **Validate Before Building**
   - Talk to 10+ potential customers
   - Get commitment (email, pre-order, or letter of intent)
   - Adjust based on feedback

## Example Analysis Template

```markdown
## Analysis: [Product Name]

### Overview
- **Founder**: [Name]
- **Launch Date**: [Date]
- **Current Status**: $[X]/month, [Y] customers
- **Time to First Revenue**: [X] months
- **Team Size**: [X] people

### Success Formula
[Core pattern description]

### Key Decisions That Worked
1. [Decision 1]: [Why it worked]
2. [Decision 2]: [Why it worked]
3. [Decision 3]: [Why it worked]

### Reproducible for Me?
- ✅ [Aspect 1]: [Why I can replicate this]
- ✅ [Aspect 2]: [Why I can replicate this]
- ⚠️ [Aspect 3]: [Challenge but possible]
- ❌ [Aspect 4]: [Not feasible for my situation]

### Action Items from This Analysis
1. [Specific action]
2. [Specific action]
3. [Specific action]
```

## Resources for Research

### Platforms
- Indie Hackers (interviews and metrics)
- MicroConf talks
- Starter Story interviews
- Bootstrapped.fm podcast
- Software Social podcast

### Communities
- Reddit: r/SideProject, r/EntrepreneurRideAlong, r/SaaS
- Twitter: #buildinpublic hashtag
- Indie Hackers forums
- Hacker News (Show HN posts)

### Metrics Sources
- BuiltWith (tech stack)
- SimilarWeb (traffic estimates)
- Product Hunt (launch traction)
- GitHub (if open source)
- Crunchbase (if funded)

---

**Next Steps After Analysis:**
1. ✅ Format all generated markdown files using markdown-formatter skill (MANDATORY)
2. Use business-idea-evaluator to score your adapted formula
3. Use feasibility-checker to validate execution capability
4. Use business-orchestrator to create comprehensive action plan
