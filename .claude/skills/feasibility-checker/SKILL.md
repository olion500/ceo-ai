---
name: feasibility-checker
description: Validate execution feasibility for indie developers and small teams across technical, financial, and time dimensions. Use when checking if you can actually build something, estimating required resources, validating technical approach, calculating project costs, assessing time commitments, or determining if an idea is realistic for solo/small team execution. Covers skill gaps, infrastructure needs, budget requirements, and timeline estimation.
---

# Feasibility Checker

## Purpose

Systematically validate whether YOU can actually execute a business idea with your current resources, skills, and constraints. Focus on practical execution reality for indie developers and small teams.

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

### 1. Available Time Audit

```markdown
## Time Availability

### Current Commitments
- **Day Job:** [X] hours/week
- **Family:** [X] hours/week
- **Sleep:** [X] hours/week (56 recommended)
- **Other:** [X] hours/week
- **Total Committed:** [X] hours/week

### Available Time
- **Weekday evenings:** [X] hours × 5 = [Y] hours/week
- **Weekend days:** [X] hours × 2 = [Y] hours/week
- **Total Available:** [X] hours/week

### Realistic Working Hours
- Available time: [X] hours/week
- Account for life (×0.7): [X × 0.7] hours/week
- **Realistic capacity:** [X] hours/week for project
```

**Reality Check:**
- <5 hours/week: Very slow progress, 6-12 months for MVP
- 5-10 hours/week: Moderate progress, 3-6 months for MVP
- 10-20 hours/week: Good progress, 2-4 months for MVP
- 20-40 hours/week: Fast progress, 1-2 months for MVP
- 40+ hours/week: Full-time, can be aggressive

### 2. Project Timeline Estimation

```markdown
## MVP Timeline Breakdown

### Phase 1: Setup & Foundation ([X] hours)
- [ ] Tech stack setup: [X] hours
- [ ] Database schema design: [X] hours
- [ ] Authentication setup: [X] hours
- [ ] Basic UI scaffolding: [X] hours
- **Phase 1 Total:** [X] hours

### Phase 2: Core Features ([X] hours)
- [ ] Feature 1: [X] hours
- [ ] Feature 2: [X] hours
- [ ] Feature 3: [X] hours
- **Phase 2 Total:** [X] hours

### Phase 3: Polish & Launch ([X] hours)
- [ ] UI/UX refinement: [X] hours
- [ ] Testing: [X] hours
- [ ] Landing page: [X] hours
- [ ] Payment integration: [X] hours
- [ ] Launch prep: [X] hours
- **Phase 3 Total:** [X] hours

### Total Estimated Hours: [X]

### Timeline Calculation
- Total hours needed: [X]
- Hours available per week: [Y]
- **Weeks needed:** [X / Y] = [Z] weeks
- **Add 50% buffer:** [Z × 1.5] = [W] weeks
- **Realistic timeline:** [W] weeks = [W/4] months
```

### 3. Milestone Planning

```markdown
## Project Milestones

### Month 1
- [ ] Complete setup and foundation
- [ ] Ship basic working prototype
- [ ] Show to 5 potential users
- **Success metric:** Prototype demonstrates core value

### Month 2
- [ ] Implement core features
- [ ] Get 10 beta users
- [ ] Iterate based on feedback
- **Success metric:** Users return 3+ times

### Month 3
- [ ] Polish UI/UX
- [ ] Add payment processing
- [ ] Create landing page
- [ ] Launch publicly
- **Success metric:** First paying customer

### Decision Points
- If no user interest by Month 1 → Pivot or abandon
- If users don't return by Month 2 → Major iteration needed
- If no sales by Month 4 → Re-evaluate pricing/positioning
```

### 4. Opportunity Cost Analysis

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

## Executive Summary
**Can I build this?** [Yes/No/Maybe with changes]
**Confidence level:** [High/Medium/Low]
**Key blockers:** [List or "None"]
**Recommended action:** [Proceed/Iterate/Abandon]

## Technical Feasibility: X/10
**Assessment:** [1-2 sentences]
**Blockers:** [List or "None"]
**Mitigations:** [List]

## Financial Feasibility: X/10
**Assessment:** [1-2 sentences]
**Required investment:** $[X] initial, $[Y]/month ongoing
**Runway:** [X] months
**Risk level:** [Low/Medium/High]

## Time Feasibility: X/10
**Assessment:** [1-2 sentences]
**Available time:** [X] hours/week
**Estimated timeline:** [X] months
**Opportunity cost:** [Acceptable/Concerning]

## Overall Feasibility: X/10
**Recommendation:** [Detailed recommendation]

## If Proceeding
**Must-do items before starting:**
1. [Item]
2. [Item]
3. [Item]

**Success metrics (first 3 months):**
- Month 1: [Metric]
- Month 2: [Metric]
- Month 3: [Metric]

**Kill criteria:**
- If [condition] by [date], then abandon
- If [condition] by [date], then pivot

## If Not Proceeding
**Key reasons:**
1. [Reason]
2. [Reason]

**Alternative options:**
1. [Alternative approach 1]
2. [Alternative approach 2]

**What would need to change:**
- [Change 1]
- [Change 2]
```

---

**After Feasibility Check:**
1. If feasible (>6.5/10): Use business-orchestrator for execution plan
2. If borderline (5-6.5/10): Iterate on scope and re-check
3. If not feasible (<5/10): Consider different idea or major pivot
