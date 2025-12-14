---
name: feasibility-checker
description: Validate execution feasibility for indie developers and small teams across technical, financial, and time dimensions. Use when checking if you can actually build something, estimating required resources, validating technical approach, calculating project costs, assessing time commitments, or determining if an idea is realistic for solo/small team execution. Covers skill gaps, infrastructure needs, budget requirements, and timeline estimation.
---

# Feasibility Checker

## Purpose

Systematically validate whether YOU can actually execute a business idea with your current resources, skills, and constraints. Focus on practical execution reality for indie developers and small teams.

**IMPORTANT - Documentation Links:**
- **Local document links**: Use markdown links `[Document Name](./relative-path.md)` for:
  - Idea specification files
  - Success pattern files in `research/patterns/`
  - Success story files in `research/stories/`
  - Related analysis reports
- **External links**: Include inline where data is cited (e.g., "CodeRabbit has [$15M ARR](https://techcrunch.com/...)")
- **References section**: Add comprehensive references list at end with all sources used

## When to Use This Skill

Automatically activates when you mention:
- Can I build this?
- Feasibility check
- Resource requirements
- Technical feasibility
- Time estimation
- Budget requirements
- Skill gap analysis
- Execution capability
- Implementation complexity
- Solo developer constraints
- Small team limitations
- Project scope validation

## Three-Pillar Feasibility Framework

### Pillar 1: Technical Feasibility (能 - Ability)
**Can you technically build this?**

### Pillar 2: Financial Feasibility (財 - Finance)
**Can you afford to build and run this?**

### Pillar 3: Time Feasibility (時 - Time)
**Can you complete this in reasonable timeframe?**

## Technical Feasibility Assessment

### 1. Skills Inventory

**Your Current Skills:**
```markdown
## Skills Audit

### Programming Languages
- [ ] [Language 1]: [Beginner/Intermediate/Advanced]
- [ ] [Language 2]: [Beginner/Intermediate/Advanced]
- [ ] [Language 3]: [Beginner/Intermediate/Advanced]

### Frameworks & Tools
- [ ] [Framework 1]: [Experience level]
- [ ] [Framework 2]: [Experience level]
- [ ] [Framework 3]: [Experience level]

### Infrastructure & DevOps
- [ ] Cloud platforms (AWS/GCP/Azure): [Experience level]
- [ ] Databases (SQL/NoSQL): [Experience level]
- [ ] CI/CD: [Experience level]
- [ ] Containerization: [Experience level]

### Domain Knowledge
- [ ] [Domain area 1]: [Experience level]
- [ ] [Domain area 2]: [Experience level]
```

### 2. Project Requirements Matrix

| Requirement | Your Level | Required Level | Gap | Learning Time | Blocker? |
|-------------|------------|----------------|-----|---------------|----------|
| React/Frontend | Advanced | Intermediate | None | 0 weeks | No |
| Node.js Backend | Intermediate | Advanced | Small | 2-3 weeks | No |
| Machine Learning | Beginner | Intermediate | Medium | 8-12 weeks | Maybe |
| iOS Development | None | Advanced | Large | 16+ weeks | Yes |

**Gap Classification:**
- **No Gap:** Can start immediately
- **Small Gap:** 1-4 weeks learning
- **Medium Gap:** 1-3 months learning
- **Large Gap:** 3+ months learning

**Blocker Determination:**
- Blocker: Gap requires >3 months or is mission-critical
- Not Blocker: Can learn on-the-go or outsource

### 3. Technical Complexity Score

Rate each component (1-10, where 10 is most complex):

| Component | Complexity | Your Expertise | Risk Level |
|-----------|------------|----------------|------------|
| Frontend | 4/10 | 8/10 | Low |
| Backend API | 5/10 | 7/10 | Low |
| Database Design | 6/10 | 6/10 | Medium |
| Authentication | 7/10 | 5/10 | Medium |
| Payment Integration | 8/10 | 3/10 | High |
| Real-time Features | 9/10 | 2/10 | Critical |

**Risk Assessment:**
- **Low Risk:** Complexity < Expertise
- **Medium Risk:** Complexity ≈ Expertise
- **High Risk:** Complexity > Expertise by 2-3 points
- **Critical Risk:** Complexity > Expertise by 4+ points

**Mitigation Strategies:**
- High Risk: Use managed services or proven libraries
- Critical Risk: Consider outsourcing or de-scoping

### 4. Technical Decision Framework

```markdown
## Technical Stack Validation

### Frontend
**Choice:** [Your chosen stack]
**Rationale:** [Why this choice]
**Familiarity:** [Your experience level]
**Alternatives Considered:** [Other options]
**Risk Level:** [Low/Medium/High]

### Backend
**Choice:** [Your chosen stack]
**Rationale:** [Why this choice]
**Familiarity:** [Your experience level]
**Alternatives Considered:** [Other options]
**Risk Level:** [Low/Medium/High]

### Database
**Choice:** [Your chosen database]
**Rationale:** [Why this choice]
**Familiarity:** [Your experience level]
**Alternatives Considered:** [Other options]
**Risk Level:** [Low/Medium/High]

### Infrastructure
**Choice:** [Hosting/cloud provider]
**Rationale:** [Why this choice]
**Familiarity:** [Your experience level]
**Alternatives Considered:** [Other options]
**Risk Level:** [Low/Medium/High]

### Third-party Services
- **Service 1:** [Purpose] - [Complexity] - [Cost]
- **Service 2:** [Purpose] - [Complexity] - [Cost]
```

**Red Flags:**
❌ Choosing new tech stack for production project
❌ Multiple "High Risk" components
❌ Any "Critical Risk" components
❌ Complex distributed systems for MVP
❌ Custom implementations of solved problems (auth, payments)

**Green Flags:**
✅ Using familiar technologies
✅ Leveraging managed services
✅ Proven tech stack for use case
✅ Clear upgrade path from MVP
✅ Strong community support

## Market & Competition Analysis

### 1. Competitor Research (CRITICAL - Use Web Search)

**MUST research competitors using WebSearch tool:**

```markdown
## Competitive Landscape

### Direct Competitors (Search: "[product category] tools", "[problem] solutions")
| Competitor | Pricing | Users/Revenue | Strengths | Weaknesses | Source |
|------------|---------|---------------|-----------|------------|--------|
| [Name 1] | $X/mo | [Data if found] | [List] | [List] | [URL] |
| [Name 2] | $X/mo | [Data if found] | [List] | [List] | [URL] |
| [Name 3] | $X/mo | [Data if found] | [List] | [List] | [URL] |

### Indirect Competitors (Alternatives users currently use)
- [Alternative 1]: [How they solve it] - [Why users might switch]
- [Alternative 2]: [How they solve it] - [Why users might switch]

### Market Gaps Identified
- Gap 1: [What competitors miss]
- Gap 2: [What competitors miss]
- Gap 3: [What competitors miss]

### Your Differentiation
- [How you'll be different from Competitor 1]
- [How you'll be different from Competitor 2]
- [What unique value you provide]

**Key Insight:** [1-2 sentences on competitive positioning]
```

**Search Queries to Run:**
- "[product type] pricing"
- "[product type] revenue" OR "[product type] MRR"
- "[problem] alternatives"
- "best [product category] 2024"
- "[competitor name] users" OR "[competitor name] customers"

### 2. Revenue Model Deep Dive

**Short-term Revenue (CRITICAL - Must have evidence):**

```markdown
## Short-term Revenue Potential (Week 1-4)

### Market Entry Speed
**Question: How fast can you get first customers?**

**If existing market (competitors exist):**
- Current market size: [Research from competitor data]
- Proof of payment: [Competitor pricing confirms willingness to pay]
- Distribution channels: [Where competitors get users - research this]
- Entry strategy: [Your specific plan with evidence]
- **Week 1 revenue potential:** $[X] - [Explain HOW - must be realistic]
- **Month 1 revenue potential:** $[X] - [Explain HOW - must be realistic]

**Evidence required:**
- [ ] Found 3+ competitors with pricing → Market exists ✅
- [ ] Found competitor user counts → Market size estimate
- [ ] Found competitor reviews → Pain points validated
- [ ] Found distribution channels → Path to customers clear
- [ ] Pricing research → Willingness to pay confirmed

**If no existing market (blue ocean):**
- ⚠️ **HIGH RISK**: Need to create market
- Validation required BEFORE building:
  - [ ] 10+ customer interviews
  - [ ] 5+ pre-sales commitments
  - [ ] Landing page with email signups (target: 100+ in 2 weeks)
- **Week 1 revenue potential:** $0 (validation phase)
- **Month 1 revenue potential:** $0 (likely still validating)

### Short-term Customer Acquisition (Must be specific)

**Launch Strategy (Week 1):**
1. [Specific platform] - [Expected reach] - [Expected conversion]
   - Example: "Product Hunt - 500 visitors - 2% signup = 10 users"
2. [Specific platform] - [Expected reach] - [Expected conversion]
3. [Specific platform] - [Expected reach] - [Expected conversion]

**Evidence for estimates:**
- Similar product on Product Hunt got [X] upvotes → [Y] visitors
- Average conversion for [category]: [Z]% (source: [URL])
- Competitor launched on [platform] got [results] (source: [URL])

**Realistic Month 1 Numbers:**
- Visitors: [X] (from [sources])
- Signups: [Y] ([Z]% conversion)
- Paying: [A] ([B]% conversion to paid)
- Revenue: $[Total]

**RED FLAG if:**
- ❌ No evidence for traffic estimates
- ❌ Using >3% conversion assumptions
- ❌ No research on competitor launches
- ❌ "Will go viral" thinking
```

**Long-term Revenue (6-12 months):**

```markdown
## Long-term Revenue Model

### Growth Assumptions (Must be researched)

**Similar Product Benchmarks:**
| Similar Product | Month 1 | Month 6 | Month 12 | Source |
|-----------------|---------|---------|----------|--------|
| [Name 1] | $X | $Y | $Z | [URL] |
| [Name 2] | $X | $Y | $Z | [URL] |
| [Name 3] | $X | $Y | $Z | [URL] |

**Your Projections (Based on benchmarks):**
| Metric | Month 1 | Month 3 | Month 6 | Month 12 | Assumption |
|--------|---------|---------|---------|----------|------------|
| Users | [X] | [Y] | [Z] | [A] | [Basis] |
| Paying % | [X]% | [Y]% | [Z]% | [A]% | [Basis] |
| Avg Price | $[X] | $[Y] | $[Z] | $[A] | [Basis] |
| **MRR** | **$[X]** | **$[Y]** | **$[Z]** | **$[A]** | |
| Churn | [X]% | [Y]% | [Z]% | [A]% | [Basis] |

**Growth Drivers:**
1. [Driver 1]: [How it works] - [Expected impact]
2. [Driver 2]: [How it works] - [Expected impact]
3. [Driver 3]: [How it works] - [Expected impact]

**Constraints:**
- Market size limit: [X total potential customers]
- Distribution bottleneck: [What limits growth]
- Competition: [How they'll react]

**Realistic vs Optimistic:**
- Conservative (70% confidence): $[X] MRR by month 12
- Base case (50% confidence): $[Y] MRR by month 12
- Optimistic (20% confidence): $[Z] MRR by month 12

**Evidence-based reasoning:**
[Explain WHY these numbers are realistic based on competitor research]
```

## Financial Feasibility Assessment

### 1. Initial Development Costs

```markdown
## Development Phase Budget

### Infrastructure & Tools (One-time)
| Item | Cost | Required? | Alternative |
|------|------|-----------|-------------|
| Domain name | $10-15/year | Yes | None |
| Logo/Design | $0-500 | No | DIY with Figma |
| Development tools | $0-100/mo | Maybe | Free alternatives |
| Code editor/IDE | $0 | Yes | VS Code (free) |
| **TOTAL ONE-TIME** | **$X** | | |

### Monthly Operating Costs (Recurring)
| Item | Cost/Month | Required? | Can Start Free? |
|------|------------|-----------|-----------------|
| Hosting (Vercel/Netlify) | $0-20 | Yes | Yes (free tier) |
| Database (Supabase/PlanetScale) | $0-25 | Yes | Yes (free tier) |
| Authentication (Auth0/Clerk) | $0-25 | Yes | Yes (free tier) |
| Email service (SendGrid) | $0-15 | Yes | Yes (free tier) |
| Payment processing | 2.9% + 30¢ | When revenue | N/A |
| Analytics | $0 | Yes | Yes (Google Analytics) |
| Error tracking (Sentry) | $0-26 | No | Yes (free tier) |
| **TOTAL MONTHLY** | **$0-111** | | **Can start at $0** |
```

### 2. Free Tier Strategy

**Maximize Free Tiers:**
- **Hosting:** Vercel (free), Netlify (free), Railway ($5 free credit)
- **Database:** Supabase (500MB free), PlanetScale (5GB free)
- **Auth:** Clerk (10K MAU free), Supabase Auth (free)
- **Email:** SendGrid (100/day free), Resend (3K/month free)
- **Storage:** Cloudflare R2 (10GB free), Supabase Storage (1GB free)

**Upgrade Triggers:**
```markdown
## Free Tier Limits & Upgrade Points

| Service | Free Limit | Upgrade Cost | Trigger Point |
|---------|------------|--------------|---------------|
| Vercel | 100GB bandwidth | $20/mo | ~1K users |
| Supabase DB | 500MB | $25/mo | ~50K records |
| Clerk Auth | 10K MAU | $25/mo | 10K users |
| SendGrid | 100 emails/day | $15/mo | Daily emails >100 |

**Projected Upgrade Timeline:**
- Months 1-3: $0/month (all free tiers)
- Months 4-6: $20-50/month (hit first limits)
- Months 7-12: $50-150/month (growing user base)
```

### 3. Runway Calculation

```markdown
## Financial Runway

### Personal Financial Situation
- **Monthly Living Expenses:** $[X]
- **Current Savings:** $[X]
- **Monthly Income (if any):** $[X]
- **Months of Runway:** [Savings / (Expenses - Income)]

### Project Financial Situation
- **Initial Investment Needed:** $[X]
- **Monthly Operating Costs:** $[X] (start) → $[X] (after growth)
- **Break-even Revenue Target:** $[X]/month
- **Time to Break-even Estimate:** [X] months

### Risk Assessment
- Runway <3 months: 🔴 High risk, need income ASAP
- Runway 3-6 months: 🟡 Medium risk, aggressive timeline needed
- Runway 6-12 months: 🟢 Low risk, comfortable timeline
- Runway >12 months: 🟢 Very low risk, can iterate freely
```

### 4. Revenue Requirement Analysis

```markdown
## Break-even Analysis

### Target: $[X]/month to be sustainable

**Scenario 1: Subscription Model ($29/month)**
- Need [X / 29] = [Y] paying customers
- Assuming 2% conversion: Need [Y / 0.02] = [Z] total users
- Acquisition cost: $[A] per customer
- Marketing budget needed: $[Y × A]

**Scenario 2: One-time Purchase ($99)**
- Need [X / 99] = [Y] sales per month
- Assuming 1% conversion: Need [Y / 0.01] = [Z] visitors/month
- Can sustain with organic traffic? [Yes/No]

**Scenario 3: Freemium ($0/$49/month)**
- Assume 2% paid conversion
- Need [X / 49 / 0.02] = [Y] total users
- More users needed but lower barrier

**Recommended Model:** [Your choice + reasoning]
```

## Time Feasibility Assessment

### 1. Time Estimation (Simple)

**How long will this take?**
- MVP timeline: [X weeks/months]
- What needs to be done:
  - [Major task 1]
  - [Major task 2]
  - [Major task 3]
  - [Major task 4]

**Complexity factors:**
- Learning new tech: [Yes/No - what?]
- Third-party integrations: [List]
- Infrastructure setup: [Simple/Medium/Complex]

### 2. Opportunity Cost Analysis

```markdown
## Opportunity Cost

### What else could you do with this time?

**Option A: Freelance/Consulting**
- Hours available: [X]/week
- Hourly rate: $[Y]
- Potential income: $[X × Y × 4] per month
- Opportunity cost over [Z] months: $[X × Y × 4 × Z]

**Option B: Learning New Skills**
- Could learn [Skill 1] in [X] months
- Potential salary increase: $[Y]K/year
- ROI timeline: [Z] years

**Option C: Building This Product**
- Time investment: [X] months
- Best case revenue (year 1): $[Y]/month
- Worst case: $0 (learning experience)
- Break-even vs freelancing: Month [Z]

**Analysis:**
[Your reasoning about which option makes sense]
```

## Comprehensive Feasibility Matrix

```markdown
# Overall Feasibility Assessment

| Factor | Score (1-10) | Weight | Weighted Score | Notes |
|--------|--------------|--------|----------------|-------|
| **Technical** | | | | |
| Skill match | X/10 | 20% | X.X | [Note] |
| Tech complexity | X/10 | 15% | X.X | [Note] |
| Learning curve | X/10 | 10% | X.X | [Note] |
| **Financial** | | | | |
| Initial costs | X/10 | 10% | X.X | [Note] |
| Operating costs | X/10 | 10% | X.X | [Note] |
| Runway | X/10 | 10% | X.X | [Note] |
| **Time** | | | | |
| Available time | X/10 | 10% | X.X | [Note] |
| Project timeline | X/10 | 10% | X.X | [Note] |
| Opportunity cost | X/10 | 5% | X.X | [Note] |
| **TOTAL** | | **100%** | **X.X/10** | |

## Interpretation
- 0.0-3.0: Not feasible, high risk of failure
- 3.1-5.0: Challenging, significant obstacles
- 5.1-7.0: Feasible with effort, manageable risks
- 7.1-9.0: Highly feasible, good odds of success
- 9.1-10.0: Ideal conditions, proceed with confidence
```

## Risk Mitigation Strategies

### Technical Risks

**High Complexity Components:**
- ✅ Use managed services (Auth0, Stripe, SendGrid)
- ✅ Leverage proven libraries/frameworks
- ✅ Start with simpler alternative (async → real-time later)
- ✅ Build spike/prototype to validate approach

**Skill Gaps:**
- ✅ Take focused course (weekend or 1-2 weeks)
- ✅ Hire contractor for specific component
- ✅ Find technical co-founder
- ✅ Use no-code/low-code for MVP

**Tech Stack Uncertainty:**
- ✅ Build small proof-of-concept first
- ✅ Choose battle-tested stack over trendy
- ✅ Prioritize strong community support
- ✅ Have exit strategy (easy to migrate)

### Financial Risks

**Limited Budget:**
- ✅ Maximize free tiers religiously
- ✅ Generate revenue before scaling costs
- ✅ Keep day job initially
- ✅ Bootstrap, avoid external funding pressure

**Unclear Costs:**
- ✅ Research exact pricing of all services
- ✅ Build cost calculator for different scales
- ✅ Set up billing alerts on all platforms
- ✅ Monitor costs weekly

**Long Runway Needed:**
- ✅ Side project approach (keep income)
- ✅ Pre-sell before building
- ✅ Find early customers ASAP
- ✅ Consider smaller scope for faster revenue

### Time Risks

**Limited Availability:**
- ✅ Ruthlessly cut scope to essentials
- ✅ Use existing solutions for non-core features
- ✅ Hire for time-intensive tasks
- ✅ Set aggressive but realistic deadlines

**Optimistic Timeline:**
- ✅ Add 50-100% buffer to estimates
- ✅ Track actual time spent weekly
- ✅ Set hard decision points
- ✅ Be ready to pivot or abandon

**Motivation/Burnout:**
- ✅ Set sustainable pace (not sprinting marathon)
- ✅ Public accountability (build in public)
- ✅ Find co-founder or accountability partner
- ✅ Define small wins to celebrate

## Go/No-Go Decision Framework

### Proceed If:
✅ **Technical feasibility >6/10**
   - Skills match or small learnable gaps
   - Manageable technical complexity
   - Clear technical approach

✅ **Financial feasibility >6/10**
   - Can start with <$100
   - 3+ months runway
   - Clear path to break-even

✅ **Time feasibility >6/10**
   - 5+ hours/week available
   - 3-6 month realistic timeline
   - Opportunity cost acceptable

✅ **Overall score >6.5/10**

### Iterate/De-scope If:
🟡 **Score 5-6/10 in any dimension**
   - Identify specific blocking factors
   - Create mitigation plan for each
   - Reduce scope to improve feasibility
   - Set strict decision timeline (30-60 days)

### Abandon/Pivot If:
❌ **Any dimension <4/10**
   - Critical blocker identified
   - No realistic mitigation path
   - Opportunity cost too high
   - Better alternatives available

❌ **Overall score <5/10**

## Feasibility Report Template

```markdown
# Feasibility Report: [Project Name]

**Generated Date:** [YYYY-MM-DD]
**Idea Score:** [X.X]/10
**Feasibility Score:** [X.X]/10
**Final Recommendation:** [PROCEED/VALIDATE MORE/AVOID]

---

## Executive Summary

**Can I build this?** [Yes/No/Maybe with changes]

**Confidence level:** [High/Medium/Low] ([X]%)

**Key blockers:**
- [Blocker 1 or "None"]
- [Blocker 2]

**Recommended action:** [PROCEED/VALIDATE MORE/AVOID with specific next steps]

**Why this assessment:**
- Technical: [1 sentence]
- Market: [1 sentence]
- Financial: [1 sentence]
- Time: [1 sentence]

---

## Market & Competition Analysis

### Competitive Landscape

**Direct Competitors:**
| Competitor | Pricing | Users/Revenue | Strengths | Weaknesses | Source |
|------------|---------|---------------|-----------|------------|--------|
| [[Name 1]](https://competitor1.com) | $X/mo | [Data] | [List] | [List] | [Source link](https://source.com) |
| [[Name 2]](https://competitor2.com) | $X/mo | [Data] | [List] | [List] | [Source link](https://source.com) |
| [[Name 3]](https://competitor3.com) | $X/mo | [Data] | [List] | [List] | [Source link](https://source.com) |

**Indirect Competitors:**
- [[Alternative 1]](https://alt1.com): [How they solve it]
- [[Alternative 2]](https://alt2.com): [How they solve it]

**Market Gaps:**
- [Gap 1]
- [Gap 2]
- [Gap 3]

**Your Differentiation:**
- [How you'll be different]
- [Unique value proposition]

---

## Revenue Model Analysis

### Short-term Revenue (Week 1-4)

**Market Entry Speed:**
- Market exists: [Yes/No]
- Proof of payment: [Evidence from competitors]
- Distribution channels: [Where competitors get users]
- **Week 1 revenue potential:** $[X] - [How specifically]
- **Month 1 revenue potential:** $[X] - [How specifically]

**Launch Strategy:**
1. [Platform]: [Expected reach] - [Expected conversion]
2. [Platform]: [Expected reach] - [Expected conversion]
3. [Platform]: [Expected reach] - [Expected conversion]

**Realistic Month 1 Numbers:**
- Visitors: [X] (from [sources])
- Signups: [Y] ([Z]% conversion)
- Paying: [A] ([B]% conversion)
- Revenue: $[Total]

### Long-term Revenue (6-12 months)

**Similar Product Benchmarks:**
| Similar Product | Month 1 | Month 6 | Month 12 | Source |
|-----------------|---------|---------|----------|--------|
| [Name 1] | $X | $Y | $Z | [URL] |
| [Name 2] | $X | $Y | $Z | [URL] |

**Your Projections:**
| Metric | Month 1 | Month 3 | Month 6 | Month 12 | Assumption |
|--------|---------|---------|---------|----------|------------|
| Users | [X] | [Y] | [Z] | [A] | [Basis] |
| Paying % | [X]% | [Y]% | [Z]% | [A]% | [Basis] |
| **MRR** | **$[X]** | **$[Y]** | **$[Z]** | **$[A]** | |

**Evidence-based reasoning:**
[Why these numbers are realistic based on research]

---

## Technical Feasibility: X/10

### Skills Assessment

**Your Current Skills:**
- [Skill 1]: [Level] (X/10)
- [Skill 2]: [Level] (X/10)
- [Skill 3]: [Level] (X/10)

### Requirements Matrix

| Requirement | Your Level | Required | Gap | Learning Time | Blocker? |
|-------------|------------|----------|-----|---------------|----------|
| [Tech 1] | X/10 | Y/10 | [None/Small/Medium/Large] | [Time] | [Yes/No] |
| [Tech 2] | X/10 | Y/10 | [None/Small/Medium/Large] | [Time] | [Yes/No] |
| [Tech 3] | X/10 | Y/10 | [None/Small/Medium/Large] | [Time] | [Yes/No] |

**Gap Summary:**
- [Summary of learning needs]
- Total learning time: [X weeks/months]
- Blockers: [Yes/No - which ones]

### Complexity Assessment

| Component | Complexity | Expertise | Risk |
|-----------|------------|-----------|------|
| [Component 1] | X/10 | Y/10 | [Low/Medium/High/Critical] |
| [Component 2] | X/10 | Y/10 | [Low/Medium/High/Critical] |
| [Component 3] | X/10 | Y/10 | [Low/Medium/High/Critical] |

**Risk Analysis:**
- Low: [X]/[Total] components ✅
- Medium: [X]/[Total] components ⚠️
- High: [X]/[Total] components ⚠️
- Critical: [X]/[Total] components 🔴

**Technical Feasibility Score: X/10** [✅/⚠️/🔴]

---

## Financial Feasibility: X/10

### Costs

**Initial:**
- [Item]: $[X]
- **Total: $[X]** [✅/⚠️/🔴]

**Monthly:**
| Service | Free Tier | Paid |
|---------|-----------|------|
| [Service 1] | $[X] | $[Y]/mo |
| [Service 2] | $[X] | $[Y]/mo |
| **Total** | **$[X]** | **$[Y]/mo** |

**Break-even:**
- [X] customers × $[Y] = $[Z]/mo
- [Assessment of achievability]

**Financial Feasibility Score: X/10** [✅/⚠️/🔴]

---

## Time Feasibility: X/10

### Timeline

**How long will this take?**
- MVP timeline: [X weeks/months]

**What needs to be done:**
- [Major task 1]
- [Major task 2]
- [Major task 3]
- [Major task 4]

**Complexity factors:**
- Learning new tech: [Yes/No - what?]
- Third-party integrations: [List]
- Infrastructure setup: [Simple/Medium/Complex]

**Time Feasibility Score: X/10** [✅/⚠️/🔴]

---

## Overall Feasibility: X/10

| Factor | Score | Weight | Weighted | Notes |
|--------|-------|--------|----------|-------|
| **Technical** | X/10 | 30% | X.X | [Note] |
| **Financial** | X/10 | 20% | X.X | [Note] |
| **Time** | X/10 | 20% | X.X | [Note] |
| **Market** | X/10 | 30% | X.X | [Note] |
| **TOTAL** | | 100% | **X.X/10** | |

**Interpretation:** [Highly feasible/Feasible with effort/Challenging/Not feasible]

---

## Recommendation: [PROCEED/VALIDATE MORE/AVOID]

[Detailed recommendation with specific next steps]

**If PROCEED:**
- Start with: [Specific first step]
- Timeline: [Realistic timeline]
- Success probability: [X]%

**If VALIDATE MORE:**
- What to validate: [Specific items]
- How to validate: [Specific methods]
- Decision criteria: [What determines proceed/abandon]

**If AVOID:**
- Key blockers: [List]
- Alternative options: [List]
- What would need to change: [List]

---

## References

### Local Documents
- **Idea Specification:** [Idea Name](./[idea-slug]-[yyyy-mm-dd].md)
- **Success Patterns Applied:**
  - [Pattern 1](../../patterns/[category]/[pattern-name].md)
  - [Pattern 2](../../patterns/[category]/[pattern-name].md)
- **Similar Success Stories:**
  - [Story 1](../../stories/[story-slug]-[yyyy-mm-dd].md)
  - [Story 2](../../stories/[story-slug]-[yyyy-mm-dd].md)

### Competitor Research
1. [Competitor 1 Name](https://competitor1.com) - Official website
2. [Competitor 1 Pricing](https://competitor1.com/pricing) - Pricing page
3. [Competitor 1 Revenue/Users](https://source.com/article) - Third-party data source
4. [Competitor 2 Name](https://competitor2.com) - Official website
5. [Competitor 2 Case Study](https://casestudy.com) - Success metrics

### Market Research
6. [Product Hunt Launch Data](https://producthunt.com/research) - Launch statistics
7. [Hacker News Traffic Stats](https://example.com/hn-stats) - Traffic benchmarks
8. [Industry Report](https://example.com/report) - Market size data
9. [Pricing Research](https://example.com/pricing-analysis) - Competitor pricing analysis
10. [Customer Reviews](https://g2.com/product) - User feedback and pain points

### Technical Resources
11. [GitHub API Documentation](https://docs.github.com/api) - Technical implementation
12. [Claude API Documentation](https://docs.anthropic.com/claude/reference) - AI integration
13. [Similar Implementation](https://github.com/example/repo) - Open source reference
14. [Framework Documentation](https://framework.dev/docs) - Tech stack docs

### Revenue Benchmarks
15. [Similar Product Revenue](https://indiehackers.com/product) - Indie Hackers profile
16. [SaaS Metrics Study](https://example.com/saas-metrics) - Industry benchmarks
17. [Conversion Rate Data](https://example.com/conversion-rates) - Funnel metrics
18. [Churn Analysis](https://example.com/churn-study) - Retention data

---

**Assessment Completed:** [YYYY-MM-DD]
**Next:** [Specific next action]
**Status:** [Summary assessment]
```

---

**After Feasibility Check:**
1. If feasible (>6.5/10): Use business-orchestrator for execution plan
2. If borderline (5-6.5/10): Iterate on scope and re-check
3. If not feasible (<5/10): Consider different idea or major pivot
