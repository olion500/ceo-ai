---
name: business-orchestrator
description: Orchestrate comprehensive business analysis by coordinating success-formula-analyzer, business-idea-evaluator, and feasibility-checker agents. Use when you need complete business validation, end-to-end idea analysis, multi-agent coordination, integrated business assessment, or action plan creation. Provides workflow coordination, result synthesis, and actionable recommendations for indie developers and small teams.
---

# Business Orchestrator

## Purpose

Coordinate multiple business analysis agents to provide comprehensive, evidence-based assessment and actionable roadmap for indie developers and small teams. Act as the central intelligence that synthesizes insights from specialized agents.

## When to Use This Skill

Automatically activates when you mention:
- Complete business analysis
- Full idea validation
- End-to-end assessment
- Multi-agent analysis
- Comprehensive evaluation
- Business action plan
- Orchestrate business check
- Validate business idea completely
- Full feasibility check
- Business strategy planning
- Startup roadmap
- Launch plan creation

## Multi-Agent Orchestration

### Agent Network

```
┌──────────────────────────────────────┐
│     Business Orchestrator            │
│  (Coordination & Synthesis)          │
└──────────────────────────────────────┘
           │
           ├─────────────────┬─────────────────┐
           │                 │                 │
           ▼                 ▼                 ▼
┌─────────────────┐ ┌─────────────────┐ ┌─────────────────┐
│ Success Formula │ │ Business Idea   │ │ Feasibility     │
│ Analyzer        │ │ Evaluator       │ │ Checker         │
│                 │ │                 │ │                 │
│ • Pattern       │ │ • Score 8       │ │ • Technical     │
│   extraction    │ │   dimensions    │ │ • Financial     │
│ • Revenue model │ │ • Risk analysis │ │ • Time          │
│ • Success       │ │ • Competitive   │ │ • Resource      │
│   tactics       │ │   positioning   │ │   validation    │
└─────────────────┘ └─────────────────┘ └─────────────────┘
```

## Orchestration Workflows

### Workflow 1: Idea Validation (Most Common)

**Use Case:** "I have a business idea, is it worth building?"

```markdown
## Validation Workflow

### Step 1: Initial Assessment (business-idea-evaluator)
**Input:** Raw business idea description
**Output:**
- 8-dimension score (1-10 each)
- Overall viability score (/80)
- Key risks identified
- Preliminary recommendation

**Decision Point:**
- If score >55: Proceed to Step 2
- If score 40-55: Refine idea, iterate dimensions
- If score <40: Consider pivot or different idea

### Step 2: Success Pattern Matching (success-formula-analyzer)
**Input:** Idea + similar successful cases
**Output:**
- 3-5 similar successful products
- Common success patterns
- Reproducible tactics for your context
- Warning signs from similar cases

**Decision Point:**
- If patterns found: Apply to your idea
- If no patterns: Red flag, might be too unique/unproven
- Adapt successful tactics to your context

### Step 3: Execution Validation (feasibility-checker)
**Input:** Idea + your personal context (skills, time, budget)
**Output:**
- Technical feasibility (1-10)
- Financial feasibility (1-10)
- Time feasibility (1-10)
- Overall feasibility score

**Decision Point:**
- If >6.5/10: Proceed to action plan (Step 4)
- If 5-6.5/10: De-scope and re-check
- If <5/10: Not feasible with current resources

### Step 4: Synthesis & Action Plan
**Input:** All agent outputs
**Output:**
- Integrated assessment
- Go/No-go recommendation
- Detailed action plan if "Go"
- Alternative options if "No-go"
```

### Workflow 2: Learning from Success

**Use Case:** "Analyze how [Product X] succeeded and apply to my idea"

```markdown
## Success-First Workflow

### Step 1: Deep Success Analysis (success-formula-analyzer)
**Input:** Successful product/founder to analyze
**Actions:**
- Research founder journey
- Extract success formula
- Identify reproducible patterns
- Document key decisions

**Output:** Success formula template

### Step 2: Apply to Your Idea (business-idea-evaluator)
**Input:** Your idea + success formula
**Actions:**
- Map your idea to success pattern
- Evaluate each dimension
- Identify alignment/gaps
- Score with formula in mind

**Output:** Idea evaluation with success pattern lens

### Step 3: Validate Replicability (feasibility-checker)
**Input:** Your idea + success tactics
**Actions:**
- Check if you can execute successful tactics
- Validate resource requirements
- Assess skill/time/budget match

**Output:** Feasibility of replicating success pattern

### Step 4: Adaptation Plan
**Input:** All insights
**Output:**
- What to copy from successful case
- What to adapt for your context
- What to do differently
- Execution roadmap
```

### Workflow 3: Competitive Positioning

**Use Case:** "Help me position against existing competitors"

```markdown
## Positioning Workflow

### Step 1: Market Landscape (business-idea-evaluator)
**Input:** Your idea + competitor list
**Actions:**
- Analyze each competitor's positioning
- Identify market gaps
- Evaluate differentiation opportunities

**Output:** Competitive landscape map

### Step 2: Success Pattern Benchmarking (success-formula-analyzer)
**Input:** Competitors who succeeded
**Actions:**
- How did late entrants win?
- What differentiation worked?
- Which niches were underserved?

**Output:** Winning positioning patterns

### Step 3: Capability Assessment (feasibility-checker)
**Input:** Differentiation strategies identified
**Actions:**
- Can you execute unique positioning?
- Resource requirements for differentiation
- Sustainable competitive advantage?

**Output:** Feasible positioning strategies

### Step 4: Positioning Strategy
**Input:** All agent insights
**Output:**
- Recommended positioning
- Differentiation tactics
- Market entry strategy
- Communication guidelines
```

## Synthesis Framework

### Integrated Scoring Matrix

```markdown
## Comprehensive Assessment

| Agent | Overall Score | Key Insights | Blockers | Opportunities |
|-------|---------------|--------------|----------|---------------|
| **Idea Evaluator** | [X/80] | [Top 3 insights] | [Critical issues] | [Strong points] |
| **Success Analyzer** | [Pattern found?] | [Key patterns] | [Anti-patterns] | [Tactics to copy] |
| **Feasibility Checker** | [X/10] | [Top constraints] | [Cannot do] | [Can do well] |

## Weighted Final Score

### Formula
```
FINAL_SCORE = (Idea_Score/80 × 40%) + (Success_Pattern_Match × 30%) + (Feasibility_Score/10 × 30%)

Where:
- Idea_Score: 0-80 from business-idea-evaluator
- Success_Pattern_Match: 0-10 (based on similar success cases found)
- Feasibility_Score: 0-10 from feasibility-checker
```

### Interpretation
- 8.0-10.0: Exceptional opportunity, proceed with confidence
- 6.5-7.9: Strong potential, manageable risks
- 5.0-6.4: Moderate potential, needs improvements
- 3.0-4.9: High risk, major concerns
- 0.0-2.9: Not recommended, pivot advised

## Risk Consolidation

### Cross-Agent Risk Analysis

```markdown
## Identified Risks

### Critical Risks (Must Address Before Proceeding)
1. **[Risk from Agent X]**
   - Impact: [High/Critical]
   - Likelihood: [%]
   - Mitigation: [Strategy]
   - Owner: [You/Co-founder/Hire]

### High Risks (Address in First 3 Months)
[Similar format]

### Medium Risks (Monitor and Manage)
[Similar format]

### Low Risks (Accept and Track)
[Similar format]
```

## Opportunity Synthesis

### Cross-Agent Opportunities

```markdown
## Key Opportunities

### Unique Advantages (From All Agents)
1. **[Advantage]**
   - Source: [Which agent identified]
   - Leverage strategy: [How to maximize]
   - Timeline: [When to deploy]

### Quick Wins (Can Execute in 30 Days)
1. **[Quick win]**
   - Effort: [Low/Medium]
   - Impact: [Expected result]
   - Action: [Specific steps]

### Strategic Advantages (Long-term Differentiation)
1. **[Strategic advantage]**
   - Sustainability: [Why hard to copy]
   - Building blocks: [What to do now]
   - Payoff timeline: [Months/years]
```

## Decision Framework

### Go/No-Go Matrix

```markdown
## Decision Analysis

### GO Criteria (All Must Be True)
- [ ] Final score >6.5/10
- [ ] No critical unmitigable risks
- [ ] Feasibility score >6/10
- [ ] Success patterns identified
- [ ] Clear differentiation exists
- [ ] Monetization path validated
- [ ] You're excited to build this

### ITERATE Criteria (Improve and Re-check)
- [ ] Final score 5-6.5/10
- [ ] Some risks but can mitigate
- [ ] One dimension scoring <5
- [ ] Success patterns partially match
- [ ] Can improve feasibility by de-scoping
- [ ] Unclear but explorable differentiation

### NO-GO Criteria (Pivot or Abandon)
- [ ] Final score <5/10
- [ ] Critical risks with no mitigation
- [ ] Feasibility score <4/10
- [ ] No similar success patterns
- [ ] Commoditized with strong competitors
- [ ] Unclear monetization
- [ ] Personal excitement/fit is low
```

## Comprehensive Report Template

```markdown
# Business Analysis Report: [Idea Name]

**Date:** [Date]
**Analyst:** [Your name]
**Status:** [Go / Iterate / No-Go]

## Executive Summary

**One-line pitch:** [Your idea in one sentence]

**Final Assessment:** [2-3 paragraphs synthesizing all agent insights]

**Recommendation:** [Clear Go/No-go with reasoning]

**Confidence Level:** [High/Medium/Low] based on [reasoning]

---

## Agent Analysis Summary

### 1. Business Idea Evaluation
**Score:** [X/80] ([Y/10] weighted)
**Grade:** [Excellent/Good/Fair/Poor]

**Key Strengths:**
- [Strength 1]
- [Strength 2]
- [Strength 3]

**Key Concerns:**
- [Concern 1]
- [Concern 2]

**Top Risks:**
- [Risk 1]
- [Risk 2]

### 2. Success Pattern Analysis
**Pattern Match:** [X/10]
**Similar Successful Cases:**
1. [Case 1]: [Key lesson]
2. [Case 2]: [Key lesson]
3. [Case 3]: [Key lesson]

**Reproducible Tactics:**
1. [Tactic 1]: [How to apply to your idea]
2. [Tactic 2]: [How to apply to your idea]
3. [Tactic 3]: [How to apply to your idea]

**Anti-Patterns to Avoid:**
1. [Anti-pattern 1]
2. [Anti-pattern 2]

### 3. Feasibility Assessment
**Score:** [X/10]
**Breakdown:**
- Technical: [X/10] - [Key constraint]
- Financial: [X/10] - [Key constraint]
- Time: [X/10] - [Key constraint]

**Can Build?** [Yes/No/With modifications]

**Biggest Constraint:** [Description]

**Mitigation Strategy:** [How to address]

---

## Integrated Insights

### What Multiple Agents Agree On
✅ [Consensus point 1]
✅ [Consensus point 2]
✅ [Consensus point 3]

### Where Agents Diverge
⚠️ [Divergence 1]: [Agent A says X, Agent B says Y]
   - Resolution: [Your assessment]

### Surprising Discoveries
💡 [Insight that wasn't obvious before analysis]

---

## Final Score Calculation

```
Final Score = (Idea: [X/80] × 0.4) + (Pattern: [Y/10] × 0.3) + (Feasibility: [Z/10] × 0.3)
            = ([X/8] × 0.4) + ([Y] × 0.3) + ([Z] × 0.3)
            = [A] + [B] + [C]
            = [FINAL]/10
```

**Interpretation:** [Based on score range]

---

## Risk Assessment

### Critical Risks (🔴 Must Address)
1. **[Risk name]**
   - Probability: [High/Medium/Low]
   - Impact: [Critical/High/Medium]
   - Mitigation: [Specific plan]
   - Timeline: [When to address]
   - Budget: [If applicable]

### High Risks (🟡 Address Early)
[Similar format]

### Monitored Risks (🟢 Track)
[Similar format]

---

## Opportunity Map

### Immediate Opportunities (0-3 Months)
1. **[Opportunity]**
   - Effort: [Low/Medium/High]
   - Impact: [Expected outcome]
   - Actions: [Specific steps]

### Medium-term Opportunities (3-12 Months)
1. **[Opportunity]**
   - [Similar format]

### Long-term Strategic Plays (12+ Months)
1. **[Opportunity]**
   - [Similar format]

---

## Recommendation

### Decision: [GO / ITERATE / NO-GO]

#### If GO:

**Why Proceed:**
1. [Reason 1 with evidence]
2. [Reason 2 with evidence]
3. [Reason 3 with evidence]

**Critical Success Factors:**
1. [Factor 1]
2. [Factor 2]
3. [Factor 3]

**Action Plan:** [See detailed action plan section below]

#### If ITERATE:

**What Needs Improvement:**
1. [Area 1]: [Current score] → [Target score]
   - Actions: [Specific improvements]
2. [Area 2]: [Current score] → [Target score]
   - Actions: [Specific improvements]

**Re-evaluation Timeline:** [X weeks]

**Success Criteria for Re-check:**
- [ ] [Criterion 1]
- [ ] [Criterion 2]
- [ ] [Criterion 3]

#### If NO-GO:

**Why Not Proceed:**
1. [Reason 1 with evidence]
2. [Reason 2 with evidence]

**Alternative Options:**
1. **[Alternative 1]:** [Description]
   - Addresses: [Original problem]
   - Advantages: [Over current idea]
2. **[Alternative 2]:** [Description]

**What Would Need to Change:**
- [Change 1]: [To make idea viable]
- [Change 2]: [To make idea viable]

---

## Detailed Action Plan (If GO)

### Phase 0: Pre-Development (Weeks 1-2)

**Objectives:**
- Validate core assumptions
- Build initial audience
- Set up infrastructure

**Tasks:**
- [ ] Create landing page
- [ ] Write 3-5 blog posts on problem domain
- [ ] Interview 10 potential customers
- [ ] Set up social media presence
- [ ] Decide on tech stack
- [ ] Register domain, set up hosting

**Success Metrics:**
- 100+ landing page visitors
- 20+ email signups
- 5+ customer validation calls completed

**Budget:** $[X]
**Time Required:** [X] hours/week

### Phase 1: MVP Development (Weeks 3-10)

**Objectives:**
- Build core functionality
- Get to first users
- Establish feedback loop

**Milestones:**
- **Week 4:** Basic authentication + database
- **Week 6:** Core feature #1 working
- **Week 8:** Core feature #2 working
- **Week 10:** MVP complete, ready for beta users

**Tasks:**
[Detailed task breakdown from feasibility-checker]

**Success Metrics:**
- 10-20 beta users
- Users return 3+ times
- Positive qualitative feedback

**Budget:** $[X]/month
**Time Required:** [X] hours/week

### Phase 2: Beta & Iteration (Weeks 11-16)

**Objectives:**
- Refine product based on feedback
- Prepare for launch
- Build initial traction

**Tasks:**
- [ ] Gather user feedback (weekly)
- [ ] Iterate on UX issues
- [ ] Add payment integration
- [ ] Create onboarding flow
- [ ] Prepare launch materials

**Success Metrics:**
- 50-100 beta users
- 10% conversion to paid (if paid)
- NPS >30

**Budget:** $[X]/month
**Time Required:** [X] hours/week

### Phase 3: Public Launch (Week 17)

**Objectives:**
- Launch publicly
- Get initial customers
- Generate buzz

**Launch Channels:**
- [ ] Product Hunt
- [ ] Hacker News (Show HN)
- [ ] Reddit ([relevant subreddits])
- [ ] Twitter ([your network])
- [ ] Indie Hackers
- [ ] Email list

**Success Metrics:**
- 500+ launch day visitors
- 50+ email signups
- 5+ paying customers (first week)
- Break into top 5 on Product Hunt

**Budget:** $[X] (launch promotion)

### Phase 4: Growth & Scale (Months 4-12)

**Objectives:**
- Achieve product-market fit
- Grow revenue
- Build sustainable business

**Key Focus Areas:**
1. **Customer Acquisition**
   - Goal: [X] customers by Month 6, [Y] by Month 12
   - Channels: [Primary channels from success-formula-analyzer]
   - Budget: $[X]/month (gradually increase)

2. **Product Development**
   - Prioritize features based on customer feedback
   - Maintain velocity: 1 major feature per month
   - Keep improving core experience

3. **Revenue Growth**
   - Target: $[X] MRR by Month 6
   - Target: $[Y] MRR by Month 12 (break-even point)
   - Optimize pricing based on data

**Success Metrics:**
- MRR growth rate: >10% month-over-month
- Churn rate: <5% per month
- CAC payback: <6 months
- NPS: >40

---

## Decision Points & Kill Criteria

### Month 1 Decision Point
**Evaluate:**
- User interest level
- Feedback quality
- Technical feasibility confirmed

**Continue if:**
- 10+ engaged beta users
- Positive feedback on core value prop
- No critical technical blockers

**Pivot if:**
- Little user interest
- Negative feedback on approach
- Major technical issues

### Month 3 Decision Point
**Evaluate:**
- Retention metrics
- Revenue (if applicable)
- Market response

**Continue if:**
- Users returning regularly (3+ times)
- At least 1 paying customer (if paid)
- Clear path to next milestone

**Pivot if:**
- Users don't stick around
- No willingness to pay
- Better opportunity identified

### Month 6 Decision Point
**Evaluate:**
- Revenue trajectory
- Growth rate
- Sustainability

**Continue if:**
- Revenue >$500 MRR or growing >10%/month
- Clear path to break-even
- Product-market fit indicators

**Abandon if:**
- Revenue <$200 MRR with flat growth
- Unsustainable costs
- Opportunity cost too high

---

## Success Metrics Dashboard

### Lagging Indicators (Measure Success)
- Monthly Recurring Revenue (MRR)
- Total customers
- Customer Lifetime Value (LTV)
- Churn rate
- Net Promoter Score (NPS)

### Leading Indicators (Predict Success)
- Weekly active users
- User retention (Day 1, Day 7, Day 30)
- Conversion rate (signup → activation → paid)
- Customer acquisition cost (CAC)
- Viral coefficient (referrals per user)

### Tracking Tools
- Revenue: Stripe dashboard
- Users: [Your analytics tool]
- Retention: [Your analytics tool]
- Feedback: Typeform + manual notes

---

## Appendices

### A. Detailed Agent Reports
- [Link to full business-idea-evaluator report]
- [Link to full success-formula-analyzer report]
- [Link to full feasibility-checker report]

### B. Research Sources
- [Key articles/interviews referenced]
- [Competitor analysis links]
- [Market research sources]

### C. Financial Projections
- [Detailed month-by-month financial model]
- [Break-even analysis]
- [Scenario planning (best/base/worst case)]

### D. Technical Architecture
- [Tech stack decisions document]
- [System architecture diagram]
- [Third-party services list]
```

---

## Orchestration Best Practices

### 1. Sequential vs Parallel Execution

**Parallel (Faster):**
- When agents don't depend on each other
- Example: Run idea evaluation + feasibility check simultaneously

**Sequential (More Thorough):**
- When output of one agent informs another
- Example: Use success patterns to refine idea evaluation

### 2. Iterative Refinement

**Pattern:**
1. Run all agents once
2. Identify weak dimension(s)
3. Brainstorm improvements
4. Re-run affected agent(s)
5. Compare scores
6. Iterate until score stabilizes or improves

### 3. Weight Customization

**Adjust weights based on priorities:**
- Financially constrained? Weight feasibility-checker more (40-50%)
- Passionate about idea? Weight success-patterns more to validate approach
- Experienced builder? Weight idea-evaluator more (50%)

---

**Master Orchestration Prompt:**

When user requests full business analysis, respond with:

```
I'll run a comprehensive business analysis for you using our multi-agent system:

1. **Business Idea Evaluator** - Score your idea across 8 dimensions
2. **Success Formula Analyzer** - Find similar successful cases and extract patterns
3. **Feasibility Checker** - Validate if YOU can actually build this

This will take a few minutes. I'll provide:
- ✅ Detailed agent reports
- ✅ Integrated synthesis and insights
- ✅ Clear Go/No-go recommendation
- ✅ Actionable roadmap if proceeding

Please provide:
- Your business idea (problem + solution)
- Target audience
- Your background (skills, time, budget)
- Any competitors you know of

Let's begin!
```

---

**Skill Status:** COMPLETE - Orchestration framework for multi-agent business analysis ✅
