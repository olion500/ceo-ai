---
name: success-formula-analyzer
description: Extract reproducible success patterns from a SINGLE success story file. Analyzes one story at a time and returns structured pattern data without creating files. Use when you need to extract patterns from individual success stories for classification.
---

# Success Formula Analyzer

## Purpose

Extract reproducible success patterns from a **single** success story file. Returns structured pattern data that can be used by agents for classification and file updates.

## Input

**Required:**
- `story_file_path`: Path to a single success story markdown file
  - Example: `research/stories/harvey-legal-ai-2025-12-16.md`

## Output

Returns structured pattern data in markdown format:

**IMPORTANT:** When creating pattern files or reports, MUST use Obsidian properties (YAML frontmatter).

### Pattern File Frontmatter Template
```yaml
---
title: [Pattern Name]
pattern-category: [idea-discovery | validation | mvp-building | customer-acquisition | product-market-fit | growth | monetization | distribution | retention | differentiation | common]
success-rate: [High | Medium | Low] ([percentage]+ if available)
time-investment: [Immediate | X days | X weeks | X months]
difficulty: [Easy | Medium | Hard]
tags: [pattern, category-name, relevant-tags]
type: Pattern
---
```

### Report File Frontmatter Template
```yaml
---
title: [Report Title]
analysis-date: YYYY-MM-DD
type: Pattern Analysis Report
stories-analyzed: [number]
deep-dive-count: [number if applicable]
tags: [report, pattern-analysis, relevant-tags]
---
```

### Pattern Extraction Output

```markdown
# Pattern Extraction: [Story Name]

## Story Metadata
- **File**: [path]
- **Product**: [name]
- **Outcome**: [key metrics]

## Extracted Patterns

### Common Patterns
1. **[Pattern Name]**
   - Description: [what they did]
   - Example: [specific from this story]

### Idea Discovery
1. **[Pattern Name]** (e.g., "Domain Expertise Gap", "Ride the Wave")
   - Description: [how they found the idea]
   - Context: [background]
   - Execution: [what they did]
   - Results: [outcome]
   - Key Insight: [why it worked]

### Validation
1. **[Pattern Name]** (e.g., "Reddit Validation Test", "Pre-Launch Waitlist")
   - Description: [how they validated]
   - Method: [specific approach]
   - Results: [validation outcome]

### MVP Building
1. **[Pattern Name]** (e.g., "Weekend Hack", "Partner with Platform Leader")
   - Description: [how they built MVP]
   - Timeline: [time taken]
   - Approach: [method used]
   - Trade-offs: [what they sacrificed/gained]

### Customer Acquisition
1. **[Pattern Name]** (e.g., "Product Hunt Launch", "Cold Email to Decision Maker")
   - Description: [how they got first customers]
   - Channel: [primary channel]
   - Results: [acquisition metrics]
   - Cost: [CAC or investment]

### Product-Market Fit
1. **[Pattern Name]** (e.g., "Land-and-Expand", "WAU Quadruple")
   - Description: [PMF signals]
   - Metrics: [specific indicators]
   - Timeline: [when achieved]

### Growth
1. **[Pattern Name]** (e.g., "Community-Led Growth", "Self-Use as Marketing")
   - Description: [how they scaled]
   - Tactics: [specific methods]
   - ROI: [return on investment]
   - Results: [growth metrics]

### Monetization
1. **[Pattern Name]** (e.g., "Delayed Monetization", "Seat-Based Pricing")
   - Description: [business model]
   - Pricing: [model details]
   - Conversion: [free to paid rate]
   - Results: [revenue metrics]

### Distribution
1. **[Pattern Name]** (e.g., "Browser-First Architecture", "AI Workers vs Tools")
   - Description: [distribution advantage]
   - Mechanism: [how it works]
   - Leverage: [competitive edge]

### Retention
1. **[Pattern Name]** (e.g., "Gated Expansion", "Custom Model Superiority")
   - Description: [retention strategy]
   - Impact: [churn reduction]
   - Mechanism: [how it works]

### Differentiation
1. **[Pattern Name]** (e.g., "Technical Moat", "Domain Expertise Hiring")
   - Description: [competitive advantage]
   - Defensibility: [how hard to copy]
   - Evidence: [proof of moat]
```

**Note:** This skill does NOT create or update pattern files. It only extracts and returns pattern data.

## When to Use This Skill

- When you have a single success story file and need to extract patterns
- When called by the `pattern-classifier` agent
- When you want structured pattern data without file updates
- For incremental pattern extraction from new stories

**Do NOT use for:**
- Analyzing multiple stories at once (use `pattern-classifier` agent instead)
- Creating pattern files (agent handles that)
- Generating reports (agent handles that)

## Analysis Process

### Step 1: Read the Story File

Read the **single** story file provided in `story_file_path`.

**What to extract:**
- Product launch date and timeline
- Founder background and story
- Initial problem/opportunity identified → idea-discovery pattern
- How they validated before building → validation pattern
- MVP features and complexity → mvp-building pattern
- First 10-100 customers strategy → customer-acquisition pattern
- Product-market fit signals → product-market-fit pattern
- Growth strategy and channels → growth pattern
- Business model and pricing → monetization pattern
- Distribution channels used → distribution pattern
- Customer retention tactics → retention pattern
- Differentiation strategy → differentiation pattern
- Revenue milestones
- Current state (users, revenue, team)

### Step 2: Identify Patterns by Category

For each category, look for these indicators in the story:

**Common Patterns:**
- Scratch Your Own Itch (founder experienced the problem)
- Build for Users Not Buyers (ICs over IT procurement)
- Data Quality First (focus on quality inputs)

**Idea Discovery:**
- Domain Expertise Gap (insider knowledge identified opportunity)
- Ride the Wave (launched during platform/tech shift)
- Observe Complaints (tracked what people complained about)

**Validation:**
- Reddit Validation Test (tested quality on real questions)
- Pre-Launch Waitlist (collected signups before building)
- Personal Chrome Extension (internal tool validated need)

**MVP Building:**
- Weekend Hack to Market (48 hours to launch)
- Partner with Platform Leader (leveraged OpenAI/etc)
- Stealth Build with Quality Focus (1-3 years perfecting)

**Customer Acquisition:**
- Product Hunt Launch (explosive initial traction)
- Cold Email to Decision Maker (personalized outreach)
- Founder Network (leveraged existing connections)

**Product-Market Fit:**
- Land-and-Expand (small deal → rapid expansion)
- Weekly Active Users Quadruple (usage explosion)
- 90% Market Share in 5 Years (category leadership)

**Growth:**
- Community-Led Growth (founder engagement)
- Self-Use as Marketing (dogfooding publicly)
- Bottom-Up Enterprise (individuals → teams → enterprise)

**Monetization:**
- Delayed Monetization → Willing Conversion (free tier first)
- Seat-Based Pricing (per-user enterprise model)
- Freemium with Viral Loop (sharing drives upgrades)

**Distribution:**
- Browser-First Architecture (platform independence)
- AI Workers vs Tools (compete with hiring budgets)
- B2B2B (service providers distribute to clients)

**Retention:**
- Gated Expansion (quality over rapid growth)
- Custom Model Superiority (97% preference over generic)
- Designed Constraints (limited customization for focus)

**Differentiation:**
- Technical Moat (proprietary technology)
- Domain Expertise Hiring (50%+ team from industry)
- Speed as Moat (5-10x faster execution)

### Step 3: Structure Pattern Data

For each pattern found, structure it as:

```
Pattern Name: [kebab-case-name]
Category: [category name]
Description: [1-2 sentence summary]
Example from Story:
  - Product: [name]
  - Context: [background]
  - Execution: [what they did]
  - Results: [specific metrics]
  - Key Insight: [why it worked]
Success Indicators:
  - [Metric 1]: [value]
  - [Metric 2]: [value]
```

### Step 4: Return Structured Output

Return all extracted patterns in the markdown format shown in "Output" section above.

**Do NOT:**
- Create files
- Update existing pattern files
- Generate reports
- Analyze multiple stories

**Do:**
- Extract patterns from single story
- Return structured data
- Include specific metrics and examples
- Note if pattern is novel or matches existing

## Pattern Categories Reference

Current taxonomy structure:

```
research/patterns/
├── common/                    # Universal patterns (100% success rate)
├── idea-discovery/            # Finding business ideas (ranked by success rate)
├── validation/                # Testing ideas before building (ranked by reliability)
├── mvp-building/              # MVP development strategies (ranked by speed)
├── customer-acquisition/      # Getting first customers (ranked by cold-start effectiveness)
├── product-market-fit/        # Achieving PMF (ranked by signal clarity)
├── growth/                    # Scaling strategies (ranked by ROI)
├── monetization/              # Business models (ranked by predictability)
├── distribution/              # Distribution channels (ranked by leverage)
├── retention/                 # Customer retention (ranked by impact)
└── differentiation/           # Competitive advantages (ranked by defensibility)
```

## Example Usage

**Input:**
```
story_file_path: research/stories/harvey-legal-ai-2025-12-16.md
```

**Output:**
```markdown
# Pattern Extraction: Harvey Legal AI

## Story Metadata
- **File**: research/stories/harvey-legal-ai-2025-12-16.md
- **Product**: Harvey
- **Outcome**: $0 → $100M ARR in 35 months

## Extracted Patterns

### Idea Discovery
1. **Domain Expertise Gap**
   - Description: Lawyer + AI researcher identified legal tech gap
   - Context: Winston Weinberg frustrated with legal tools as junior associate
   - Execution: Combined legal expertise with AI research background
   - Results: Built AI lawyers trust (97% preference over GPT-4)
   - Key Insight: Insiders see problems outsiders can't

2. **Ride the Wave**
   - Description: Launched during AI boom (ChatGPT release)
   - Context: ChatGPT released Nov 2022, Harvey founded Aug 2022
   - Execution: Perfect timing for legal AI
   - Results: $0 → $1M ARR in 5 months
   - Key Insight: Market demand exploding during platform shifts

### Validation
1. **Reddit Validation Test**
   - Description: Validated AI quality with real legal questions
   - Method: Grabbed 100 r/legaladvice questions, ran through 3 attorneys
   - Results: 86/100 approved with zero edits
   - Key Insight: Blind testing proved lawyers couldn't distinguish AI from human

### MVP Building
1. **Partner with Platform Leader**
   - Description: Partnered with OpenAI instead of building own LLMs
   - Timeline: 6 months to launch (vs years for proprietary)
   - Execution: Cold emailed Sam Altman July 4th → same-day call
   - Results: Custom legal models, 97% lawyer preference over GPT-4

### Customer Acquisition
1. **Cold Email to Decision Maker**
   - Description: Used PACER to find partners who wrote litigation briefs
   - Channel: Personalized outreach with their own work
   - Results: 8 of 10 highest-grossing US law firms
   - Cost: Time for personalization (minimal monetary cost)

### Product-Market Fit
1. **Land-and-Expand**
   - Description: Start with 10-50 seats, expand to hundreds
   - Metrics: 558% YoY growth in 2024
   - Timeline: Rapid expansion within firms

### Growth
1. **Bottom-Up Enterprise**
   - Description: Free tier → Team pilots → Enterprise accounts
   - Results: 8 of 10 top law firms, revenue mix 60% firms / 40% corporates
   - ROI: Low CAC via organic adoption

### Monetization
1. **Seat-Based Pricing**
   - Pricing: ~$1,000/user/month (estimated)
   - Results: $100M ARR with 500 customers = $200K per customer
   - Model: Per-seat with land-and-expand

### Differentiation
1. **Technical Moat**
   - Description: Custom case law model
   - Evidence: 97% lawyer preference over GPT-4
   - Defensibility: Hard to replicate, requires domain + AI expertise

2. **Domain Expertise Hiring**
   - Description: 50%+ team has legal background
   - Execution: Recruited from White & Case, Latham & Watkins
   - Impact: Product matches BigLaw workflows, credible sales conversations
```

---

**Next Steps After Extraction:**
- Pattern data is returned to calling agent
- Agent compares with existing pattern files
- Agent updates or creates pattern files as needed
- Agent generates summary of classification
