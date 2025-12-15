---
name: idea-finder
description: Find new business ideas by applying proven success patterns from analyzed indie developer stories. Uses "scratch your own itch" methodology, data-driven selection, and market gap analysis to generate validated business opportunities.
triggers:
  - "find business ideas"
  - "generate business ideas"
  - "new startup ideas"
  - "what should I build"
  - "business opportunities"
  - "아이템 찾아줘"
  - "비즈니스 아이디어"
  - "뭘 만들면 좋을까"
skillType: project
version: 1.0.0
---

# Idea Finder

## Purpose

Generate new business ideas by applying proven success patterns from 24+ analyzed indie developer success stories. Use reproducible methodologies rather than random brainstorming.

## When to Use This Skill

Automatically activates when you mention:
- Finding/generating business ideas
- Looking for startup opportunities
- Asking what to build next
- Seeking validated business concepts
- Exploring market opportunities

**Manual activation**: Ask Claude "Find me business ideas using success patterns"

## Success Pattern Framework

This skill applies three proven idea discovery methods:

### Method 1: Scratch Your Own Itch (79% Success Rate)

**How It Works**:
1. Identify personal pain points in your work/life
2. Validate others face the same problem
3. Build solution you wish existed

**Real Success Examples**:
- TypingMind: Tony frustrated with ChatGPT UI → $83K MRR
- ShipFast: Marc Lou tired of rebuilding same stack → $50K MRR
- Bank Statement Converter: Angus manually converting PDFs → $16K MRR

### Method 2: Data-Driven Selection (60% Success Rate)

**How It Works**:
1. Analyze market data (app stores, trends, competitors)
2. Create ranking algorithm (demand × achievability)
3. Choose proven market with underserved niche

**Real Success Examples**:
- Online Solitaire: Holger scraped App Annie data → $10K MRR

### Method 3: Observe Market Gaps (50% Success Rate)

**How It Works**:
1. Find successful products with obvious flaws
2. Build improved version
3. Capture frustrated users

**Real Success Examples**:
- Vampire Survivors: Luca improved Magic Survival → £40M net worth

## Idea Generation Process

### Step 1: Context Gathering

Ask user about:
- **Skills**: What can you build? (frontend, backend, mobile, design, etc.)
- **Experience**: What domains do you know well? (developer tools, finance, gaming, etc.)
- **Time**: Solo project or with team? Full-time or side project?
- **Capital**: Bootstrapped or funded?
- **Goals**: Quick validation or long-term build?

### Step 2: Personal Pain Point Analysis

**For "Scratch Your Own Itch" Method**:

Ask user:
1. "What repetitive tasks frustrate you daily?"
2. "What tools do you use but hate?"
3. "What problems do you solve manually that should be automated?"
4. "What did you wish existed in your last project?"

**Evaluation Criteria**:
- ✅ Problem occurs daily/weekly (not one-time)
- ✅ Pain is strong (very frustrating, not mildly annoying)
- ✅ Others likely have same problem (not unique to you)
- ✅ Current solutions are inadequate
- ✅ You can build it with your skills

**Red Flags**:
- ❌ Hypothetical problem ("I wish I exercised more")
- ❌ Only you have this problem
- ❌ Problem doesn't exist in daily reality
- ❌ Requires massive resources you don't have

### Step 3: Market Validation Research

**For Each Idea Candidate**:

1. **Search for existing solutions**:
   - Google: "[problem] solution"
   - Reddit: r/SideProject, r/EntrepreneurRideAlong, niche subreddits
   - Twitter: Search for pain point keywords
   - Product Hunt: Similar products
   - Indie Hackers: Discussions about the problem

2. **Validate demand signals**:
   - People complaining about current solutions?
   - High upvotes/engagement on problem posts?
   - Competitors exist but are bad/expensive?
   - Niche communities discussing the pain?

3. **Estimate market size**:
   - How many people face this problem?
   - Are they willing to pay?
   - What's the price point?
   - Total addressable market (TAM)?

### Step 4: Success Pattern Matching

**Match idea to proven patterns**:

| Pattern | When to Use | Example |
|---------|-------------|---------|
| Developer Tools | Building for developers | ShipFast, TypingMind, DevUtils |
| Automation/Productivity | Repetitive manual tasks | Bank Statement Converter |
| AI Enhancement | Improve AI product UX/features | TypingMind (ChatGPT), Photo AI |
| Niche Community Tools | Serve specific group | Nomad List (digital nomads) |
| "Unbundling Excel" | Complex spreadsheets | Many opportunities |
| Data Converters | Format transformations | Bank Statement Converter |
| Boilerplates/Templates | Developers rebuilding same thing | ShipFast |

### Step 5: Idea Scoring

**Score each idea (1-10 scale)**:

1. **Personal Pain (1-10)**: Do YOU need this badly?
2. **Market Size (1-10)**: How many potential customers?
3. **Achievability (1-10)**: Can you build MVP in 1-7 days?
4. **Monetization Clarity (1-10)**: Clear how to charge?
5. **Competition (1-10)**: Existing solutions bad/expensive?
6. **Timing (1-10)**: Is now the right time? (API launch, trend, etc.)

**Total Score**: Sum / 6 = Average

**Recommendation**:
- 8-10: Strong idea, start building
- 6-7.9: Promising, validate more before building
- 4-5.9: Risky, needs significant validation
- <4: Avoid, find better idea

### Step 6: Idea Output Format

For each validated idea, output:

```markdown
## Idea: [Name]

**One-Liner**: [What it does in one sentence]

**Success Pattern**: [Which pattern(s) this follows]
- Scratch Your Own Itch / Data-Driven / Market Gap

**The Problem**:
[Specific pain point this solves]

**Target Customer**:
- Who: [Specific persona]
- Where: [Communities, platforms they use]
- Size: [Estimated market size]

**Validation Signals**:
- [Signal 1: e.g., Reddit post with 500 upvotes complaining]
- [Signal 2: e.g., Existing solution has 1-star reviews]
- [Signal 3: e.g., 10+ people you talked to confirmed pain]

**MVP Scope (1-7 days)**:
- Core Feature 1: [Must-have]
- Core Feature 2: [Must-have]
- Core Feature 3: [Must-have]
- [Strip everything else]

**Monetization**:
- Model: [One-time purchase / Subscription / Ads]
- Price Point: $[X] [monthly/one-time]
- Why It Works: [Reasoning based on similar successful products]

**Distribution Strategy**:
- Primary: [Building in Public / SEO / Community]
- Timeline: [0-3 months / 3-12 months / 1-3 years]

**Similar Success Stories**:
- [Product 1]: [Brief description + revenue]
- [Product 2]: [Brief description + revenue]

**Score**: [X/10]
- Personal Pain: [X/10]
- Market Size: [X/10]
- Achievability: [X/10]
- Monetization: [X/10]
- Competition: [X/10]
- Timing: [X/10]

**Recommendation**: [GO / VALIDATE MORE / AVOID]

**Next Steps**:
1. [Specific action 1]
2. [Specific action 2]
3. [Specific action 3]
```

## Idea Categories to Explore

### High-Probability Categories (Based on Patterns)

**1. Developer Tools** (High Success Rate)
- Why: Developers solve own problems, willing to pay for time-savers
- Examples: ShipFast, TypingMind, DevUtils
- Opportunities:
  - Boilerplates for new frameworks
  - Testing/debugging tools
  - Code converters/migration tools
  - API wrappers with better DX

**2. AI Enhancement Tools** (Currently Hot)
- Why: AI products have UX problems, APIs enable quick building
- Examples: TypingMind ($83K MRR), Photo AI ($132K MRR)
- Opportunities:
  - Better UI for ChatGPT/Claude/Gemini
  - AI for specific niches (lawyers, doctors, etc.)
  - AI-powered automation tools
  - Custom AI model interfaces

**3. "Unbundling Excel"** (Evergreen)
- Why: People use Excel for everything, specialized tools better
- Examples: Bank Statement Converter
- Opportunities:
  - Budget tracking for [specific industry]
  - Inventory management for [niche]
  - Data converters (PDF → Excel, CSV → JSON, etc.)
  - Report generators

**4. Niche Community Tools**
- Why: Serve specific group intensely > everyone poorly
- Examples: Nomad List ($1.5M ARR)
- Opportunities:
  - Tools for remote workers
  - Tools for indie hackers
  - Tools for content creators
  - Tools for [your community]

**5. Automation/Productivity**
- Why: Repetitive tasks = high pain + clear value
- Examples: Bank Statement Converter ($16K MRR)
- Opportunities:
  - Automate manual data entry
  - Batch processing tools
  - Workflow automation for [specific task]

## Research Resources

### For Demand Validation
- **Reddit**: r/SideProject, r/EntrepreneurRideAlong, r/SaaS, niche subreddits
- **Twitter**: Search problem keywords, #buildinpublic
- **Indie Hackers**: Product discussions, revenue reports
- **Product Hunt**: See what's launching, comments reveal pain points
- **Hacker News**: "Show HN", "Ask HN: What tools do you wish existed?"

### For Market Data
- **App Annie / Sensor Tower**: Mobile app market data
- **SimilarWeb**: Website traffic estimates
- **Google Trends**: Search volume trends
- **BuiltWith**: Tech stack analysis

### For Pricing Research
- **Competitor pricing pages**: See what similar products charge
- **Indie Hackers**: Revenue reports show what works
- **Success stories**: See pricing evolution (e.g., TypingMind $9 → $39)

## Common Mistakes to Avoid

**Mistake 1: Building Without Validation**
- ❌ "I think people need this"
- ✅ "10 people confirmed they'd pay $X"

**Mistake 2: Choosing Sexy Over Proven**
- ❌ "This innovative AI blockchain VR idea"
- ✅ "Boring PDF converter for accountants"

**Mistake 3: Too Broad Target Market**
- ❌ "For everyone who needs productivity"
- ✅ "For React developers who hate setting up auth"

**Mistake 4: Ignoring Distribution**
- ❌ "Build it and they will come"
- ✅ "Build audience while building product"

**Mistake 5: Solving One-Time Problems**
- ❌ "Tool to migrate from X to Y" (one-time use)
- ✅ "Tool used daily/weekly" (recurring value)

## Output Guidelines

When user asks for ideas:

1. **Ask questions first** (don't generate random ideas):
   - What are your skills?
   - What domains do you know?
   - What frustrates you personally?
   - Full-time or side project?
   - Quick validation or long-term build?

2. **Generate 3-5 ideas** (not 20):
   - Quality over quantity
   - Each should be well-researched
   - Include validation signals
   - Provide specific next steps

3. **Rank by score**:
   - Highest score first
   - Clear recommendation (GO/VALIDATE/AVOID)

4. **Include success story parallels**:
   - "This is similar to TypingMind because..."
   - "Bank Statement Converter used this pattern..."

5. **Be honest about challenges**:
   - Don't oversell
   - Highlight risks
   - Realistic timeline expectations

## Success Criteria for Generated Ideas

Good idea should:
- ✅ Solve a problem you personally face (or can deeply empathize with)
- ✅ Have 10+ people who'd pay for it (validated)
- ✅ Be buildable in 1-7 days (MVP)
- ✅ Have clear monetization path
- ✅ Existing solutions are bad/expensive (not perfect)
- ✅ Match a proven success pattern
- ✅ Have sustainable distribution strategy

## Examples of Well-Formatted Ideas

See `resources/example-ideas.md` for full examples.

## Related Skills

- **business-idea-evaluator**: Score and validate generated ideas
- **feasibility-checker**: Check if you can actually build it
- **business-orchestrator**: Full analysis (idea + validation + feasibility)

---

## CRITICAL WORKFLOW: Automatic Documentation and Feasibility Check

**IMPORTANT**: When this skill finds business ideas, it MUST follow this workflow:

### Step 1: Generate Ideas (as usual)
- Follow all steps above (Context → Pain Points → Validation → Scoring)
- Generate 3-5 validated ideas with scores

### Step 2: MANDATORY - Create Idea Documents

**IMMEDIATELY after generating ideas**:

1. **Create directory** if not exists:
   ```bash
   mkdir -p research/ideas
   ```

2. **Save EACH idea** as separate file:
   ```
   research/ideas/[idea-name-slug]-[yyyy-mm-dd].md
   ```

3. **Use this exact template** for each idea file:

```markdown
# [Idea Name]

**Generated Date:** YYYY-MM-DD
**Status:** Generated (not yet feasibility-checked)
**Score:** X.X/10
**Recommendation:** GO / VALIDATE MORE / AVOID

---

## Quick Summary

**One-Liner:** [What it does in one sentence]

**Success Pattern Applied:**
- [Pattern 1] (X% success rate)
- [Pattern 2] (X% success rate)
- [Pattern 3] (X% success rate)

**Expected Timeline:**
- MVP: [X] days/weeks
- First Revenue: [X] weeks
- $1K MRR: [X] months

---

## Problem & Solution

### The Problem
**Who:** [Target customer persona]
**What:** [Specific pain point]
**Current Pain:**
- [Pain point 1]
- [Pain point 2]
- [Pain point 3]

**Why It Hurts:**
[Explain impact - time wasted, money lost, frustration level]

### The Solution
[Describe what you'll build and how it solves the problem]

**Core Value Proposition:**
[One sentence: "Help [who] achieve [what] by [how]"]

---

## Market Analysis

### Target Customer
- **Primary:** [Specific persona with details]
- **Secondary:** [Optional secondary market]
- **Where They Hang Out:** [Communities, platforms, subreddits, etc.]
- **Estimated Market Size:** [Number of potential customers]

### Validation Signals
1. **Signal 1:** [Evidence of demand - Reddit posts, tweets, etc.]
2. **Signal 2:** [More evidence]
3. **Signal 3:** [More evidence]

### Competition Analysis
**Existing Solutions:**
| Solution | Price | Weakness | Our Advantage |
|----------|-------|----------|---------------|
| [Competitor 1] | $X/mo | [Weakness] | [How we're better] |
| [Competitor 2] | $X/mo | [Weakness] | [How we're better] |

**Market Gap:** [What's missing that we'll provide]

---

## Product Specification

### MVP Scope (Build in [X] days)

**Core Features (MUST HAVE):**
1. **[Feature 1]:** [Description]
   - Why essential: [Reason]
   - Implementation complexity: [Low/Medium/High]

2. **[Feature 2]:** [Description]
   - Why essential: [Reason]
   - Implementation complexity: [Low/Medium/High]

3. **[Feature 3]:** [Description]
   - Why essential: [Reason]
   - Implementation complexity: [Low/Medium/High]

**Excluded from MVP (Add Later):**
- ❌ [Feature 1]: [Why it can wait]
- ❌ [Feature 2]: [Why it can wait]
- ❌ [Feature 3]: [Why it can wait]

### Technical Requirements

**Frontend:**
- Stack: [Technology choices]
- Complexity: [1-10]
- Your expertise level: [1-10]

**Backend:**
- Stack: [Technology choices]
- Complexity: [1-10]
- Your expertise level: [1-10]

**Database:**
- Choice: [Database type]
- Complexity: [1-10]
- Your expertise level: [1-10]

**Third-party Services:**
- [Service 1]: [Purpose] - [Required/Optional]
- [Service 2]: [Purpose] - [Required/Optional]
- [Service 3]: [Purpose] - [Required/Optional]

**Required Skills:**
- [Skill 1]: [Your level: Beginner/Intermediate/Advanced]
- [Skill 2]: [Your level: Beginner/Intermediate/Advanced]
- [Skill 3]: [Your level: Beginner/Intermediate/Advanced]

**Skill Gaps:**
- [Gap 1]: [Need to learn X, estimated time: Y weeks]
- [Gap 2]: [Need to learn X, estimated time: Y weeks]
- OR: "No significant skill gaps"

---

## Business Model

### Monetization Strategy
**Model:** [Subscription / One-time / Freemium / Usage-based]

**Pricing Tiers:**
| Tier | Price | Features | Target Customer |
|------|-------|----------|-----------------|
| [Tier 1] | $X | [Features] | [Who] |
| [Tier 2] | $X | [Features] | [Who] |
| [Tier 3] | $X | [Features] | [Who] |

**Pricing Rationale:**
- Value created: $[X] (time/money saved)
- Price point: $[Y] ([Y/X]% of value)
- Competitor pricing: $[Z]
- Similar success stories: [Product] at $[W]

**Revenue Projections:**
- Month 1: [X] customers × $[Y] = $[Z] MRR
- Month 3: [X] customers × $[Y] = $[Z] MRR
- Month 6: [X] customers × $[Y] = $[Z] MRR
- Month 12: [X] customers × $[Y] = $[Z] MRR

### Cost Structure

**Initial Costs:**
| Item | Cost | Required? |
|------|------|-----------|
| Domain | $15/year | Yes |
| Logo/Design | $0-500 | No (DIY) |
| [Other] | $X | [Yes/No] |
| **TOTAL** | **$X** | |

**Monthly Operating Costs:**
| Service | Free Tier | Paid Tier | When to Upgrade |
|---------|-----------|-----------|-----------------|
| Hosting | $0 (Vercel) | $20/mo | >1K users |
| Database | $0 (Supabase) | $25/mo | >500MB |
| Auth | $0 (Clerk) | $25/mo | >10K MAU |
| Email | $0 (SendGrid) | $15/mo | >100/day |
| **TOTAL** | **$0/mo** | **$85/mo** | After traction |

**Break-even Analysis:**
- Operating costs: $[X]/month (after scale)
- Avg revenue per customer: $[Y]/month
- Customers needed to break-even: [X/Y] = [Z] customers
- Realistic timeline to break-even: [W] months

---

## Go-to-Market Strategy

### Distribution Channels

**Primary Channel:** [Building in Public / SEO / Community]
- Platform: [Twitter / Reddit / Dev.to]
- Strategy: [Specific tactics]
- Timeline: [X] months
- Expected CAC: $[X] or organic

**Secondary Channel:** [Channel name]
- Strategy: [Specific tactics]
- Timeline: [X] months
- Expected CAC: $[X]

**Quick Wins (Week 1-4):**
1. [Tactic 1]: [Expected result]
2. [Tactic 2]: [Expected result]
3. [Tactic 3]: [Expected result]

### Launch Plan

**Pre-launch (Week 1-2):**
- [ ] Create landing page
- [ ] Build email list (target: [X] signups)
- [ ] Reach out to [X] potential users
- [ ] Create launch content (blog, video, tweets)

**Launch (Week 3):**
- [ ] Product Hunt launch
- [ ] Reddit posts in [subreddit 1], [subreddit 2]
- [ ] Twitter announcement
- [ ] Email list blast

**Post-launch (Week 4+):**
- [ ] Iterate based on feedback
- [ ] Create content (guides, tutorials)
- [ ] Build in public updates
- [ ] Community engagement

---

## Success Metrics & Milestones

### Month 1 Goals
- [ ] Ship MVP (working product)
- [ ] [X] beta users testing
- [ ] First paying customer
- **Success Metric:** Users return 3+ times

### Month 2 Goals
- [ ] [X] paying customers
- [ ] $[Y] MRR
- [ ] [Z] active users
- **Success Metric:** Positive retention rate

### Month 3 Goals
- [ ] [X] paying customers
- [ ] $1K MRR
- [ ] [Y] active users
- **Success Metric:** Word-of-mouth growth

### Decision Points
- **By Month 1:** If no user interest → Pivot or abandon
- **By Month 2:** If users don't return → Major iteration needed
- **By Month 4:** If no sales → Re-evaluate pricing/positioning
- **By Month 6:** If <$1K MRR → Consider pivoting

---

## Risk Assessment

### Technical Risks
**Risk 1: [Risk name]**
- Probability: [Low/Medium/High]
- Impact: [Low/Medium/High]
- Mitigation: [How to reduce risk]

**Risk 2: [Risk name]**
- Probability: [Low/Medium/High]
- Impact: [Low/Medium/High]
- Mitigation: [How to reduce risk]

### Market Risks
**Risk 1: [Risk name]**
- Probability: [Low/Medium/High]
- Impact: [Low/Medium/High]
- Mitigation: [How to reduce risk]

**Risk 2: [Risk name]**
- Probability: [Low/Medium/High]
- Impact: [Low/Medium/High]
- Mitigation: [How to reduce risk]

### Execution Risks
**Risk 1: [Risk name]**
- Probability: [Low/Medium/High]
- Impact: [Low/Medium/High]
- Mitigation: [How to reduce risk]

---

## Similar Success Stories

### [Product 1 Name] - $[X] MRR
**Pattern Applied:** [Same pattern]
**What They Did:**
- [Key tactic 1]
- [Key tactic 2]
- [Key tactic 3]

**What We Can Learn:**
[Specific takeaway]

### [Product 2 Name] - $[X] MRR
**Pattern Applied:** [Same pattern]
**What They Did:**
- [Key tactic 1]
- [Key tactic 2]
- [Key tactic 3]

**What We Can Learn:**
[Specific takeaway]

---

## Detailed Score Breakdown

| Criterion | Score | Weight | Weighted Score | Reasoning |
|-----------|-------|--------|----------------|-----------|
| **Personal Pain** | X/10 | 20% | X.X | [Why this score] |
| **Market Size** | X/10 | 15% | X.X | [Why this score] |
| **Achievability** | X/10 | 20% | X.X | [Why this score] |
| **Monetization** | X/10 | 15% | X.X | [Why this score] |
| **Competition** | X/10 | 15% | X.X | [Why this score] |
| **Timing** | X/10 | 15% | X.X | [Why this score] |
| **TOTAL** | | **100%** | **X.X/10** | |

**Overall Assessment:** [GO / VALIDATE MORE / AVOID]

---

## Immediate Next Steps

**If Proceeding (Score >7.0):**
1. **Week 1:** [Specific action with deliverable]
2. **Week 2:** [Specific action with deliverable]
3. **Week 3:** [Specific action with deliverable]
4. **Week 4:** [Specific action with deliverable]

**If Validating More (Score 5.0-7.0):**
1. [Validation task 1]
2. [Validation task 2]
3. [Validation task 3]
4. Re-assess after validation

**If Avoiding (Score <5.0):**
- **Key Blockers:** [List specific issues]
- **What Would Need to Change:** [What would make this viable]
- **Alternative Approaches:** [If any]

---

## Resources & References

**Local Documents:**
- Success patterns: [Pattern Category](../../patterns/[category]/README.md)
- Similar success stories:
  - [Story 1](../../stories/[story-slug]-[yyyy-mm-dd].md)
  - [Story 2](../../stories/[story-slug]-[yyyy-mm-dd].md)
- Pattern analysis: [Pattern Analysis Report](../../reports/[topic]-patterns-[yyyy-mm-dd].md)

**External References:**
1. [Competitor/Product Name](https://example.com) - Description/revenue data
2. [Market Research Source](https://example.com) - Key finding
3. [Technical Documentation](https://example.com) - Implementation guide
4. [Pricing Research](https://example.com) - Competitor pricing
5. [Community Discussion](https://example.com) - User feedback/pain points

**Technical Resources:**
- [Framework/Library](https://docs.example.com) - Official documentation
- [Tutorial/Guide](https://example.com) - Implementation guide
- [Example Implementation](https://github.com/example) - Open source reference

---

**Status Log:**
- YYYY-MM-DD: Idea generated by idea-finder skill
- YYYY-MM-DD: [Next status update]
```

### Step 3: MANDATORY - Run Feasibility Check

**AFTER saving all idea documents**, IMMEDIATELY:

1. **For EACH idea document created**, run:
   ```
   Use Skill tool: feasibility-checker
   Provide the idea document path
   ```

2. **The feasibility-checker will:**
   - Analyze technical feasibility (skills, complexity)
   - Analyze financial feasibility (costs, runway)
   - Analyze time feasibility (timeline, availability)
   - Generate comprehensive feasibility report
   - Update idea status with feasibility results

3. **Save feasibility report** as:
   ```
   research/ideas/[idea-name-slug]-feasibility-[yyyy-mm-dd].md
   ```

### Step 4: Update Summary Document

**After all feasibility checks**, create/update:
```
research/ideas/README.md
```

With table:
```markdown
# Business Ideas Generated

| Idea | Date | Score | Feasibility | Status | Next Action |
|------|------|-------|-------------|--------|-------------|
| [Idea 1] | YYYY-MM-DD | X.X/10 | X.X/10 | [Status] | [Action] |
| [Idea 2] | YYYY-MM-DD | X.X/10 | X.X/10 | [Status] | [Action] |
```

---

## Complete Workflow Example

**User asks:** "지금 만들어져 있는 패턴을 가지고 새로운 아이템을 찾아줘"

**idea-finder does:**

1. ✅ Analyze patterns in `research/patterns/`
2. ✅ Generate 3-5 validated ideas
3. ✅ **Create `research/ideas/devstack-migrator-2024-12-15.md`** (all info above)
4. ✅ **Create `research/ideas/saasboard-2024-12-15.md`** (all info above)
5. ✅ **Create `research/ideas/github-pr-reviewer-2024-12-15.md`** (all info above)
6. ✅ **FOR EACH IDEA:** Run `feasibility-checker` skill
   - Generates `research/ideas/devstack-migrator-feasibility-2024-12-15.md`
   - Generates `research/ideas/saasboard-feasibility-2024-12-15.md`
   - Generates `research/ideas/github-pr-reviewer-feasibility-2024-12-15.md`
7. ✅ Update `research/ideas/README.md` with summary table
8. ✅ Present final ranked list to user with feasibility scores

**NEVER skip steps 3-7. This is mandatory workflow.**

---

**Next Steps After Finding Ideas**:
1. ✅ **DONE AUTOMATICALLY**: Ideas saved to `research/ideas/`
2. ✅ **DONE AUTOMATICALLY**: Feasibility check run for each idea
3. ✅ **Format all generated markdown files** using markdown-formatter skill (MANDATORY)
4. **MANUAL**: Talk to 10 potential customers before building
5. **MANUAL**: Ship MVP in 1-7 days, iterate based on feedback
