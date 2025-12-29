# Decision Framework & Risk Mitigation

Detailed guide for making go/no-go decisions and managing risks.

## Overview

Synthesize all feasibility assessments into clear decision with risk mitigation plan.

## Comprehensive Scoring

```
Overall Feasibility = (Technical × 30%) + (Financial × 20%) + (Time × 20%) + (Market × 30%)
```

Each component scored 0-10.

## Decision Criteria

### Proceed If (ALL must be true):
- ✅ Overall score >6.5/10
- ✅ No component score <4/10
- ✅ No critical unmitigatable risks
- ✅ Clear path to first customer
- ✅ Personal excitement/commitment high
- ✅ Opportunity cost acceptable

### Iterate/De-scope If:
- 🟡 Overall score 5-6.5/10
- 🟡 One component <5/10 but improvable
- 🟡 Risks exist with mitigation plans
- 🟡 Can reduce scope to improve feasibility
- 🟡 Need more validation

**Actions:**
- Identify specific blocking factors
- Create mitigation plan for each
- Set strict timeline (30-60 days)
- Re-assess after improvements

### Abandon/Pivot If:
- ❌ Overall score <5/10
- ❌ Any component <3/10
- ❌ Critical blocker with no solution
- ❌ Personal runway <3 months
- ❌ Better alternative exists
- ❌ Lost excitement/commitment

**Actions:**
- Document learnings
- Use idea-finder for alternatives
- Consider pivot vs new idea

## Risk Mitigation Strategies

### Quick Reference Table

| Risk Type | Risk Level | Mitigation Tactic | Time Cost | Success Rate |
|-----------|------------|-------------------|-----------|--------------|
| **High complexity feature** | 🔴 Critical | Use managed service (Pusher, Ably) | 1 day | 95% |
| **Skill gap (>3 points)** | 🔴 Critical | Hire contractor OR use no-code | 1-2 weeks | 85% |
| **Unfamiliar tech stack** | 🟡 High | Build POC first (2 days max) | 2 days | 70% |
| **Limited budget (<$500)** | 🟡 High | All free tiers + pre-sales | 0 cost | 80% |
| **Long timeline (>6 mo)** | 🟡 High | Cut scope by 50% | 1 day planning | 90% |
| **No proven demand** | 🔴 Critical | 20+ customer interviews first | 1-2 weeks | 75% |
| **Strong competition** | 🟡 High | Target niche OR unique angle | Ongoing | 60% |
| **Burnout risk** | 🟡 High | Public accountability + partner | Ongoing | 70% |

### Detailed Mitigation Tactics

**Technical Risks:**
- High complexity → Managed services (Pusher, Clerk, Supabase)
- Skill gaps → Hire contractor or use no-code for MVP
- Uncertain tech → Build 2-day POC before committing

**Financial Risks:**
- Limited budget → Free tiers only + pre-sales before spending
- Unclear costs → Set billing alerts, monitor weekly
- Long runway needed → Side project mode, not full-time

**Time Risks:**
- Limited availability → Cut scope 50%, use existing solutions
- Optimistic timeline → Add 2x buffer, track weekly
- Burnout risk → Sustainable pace + public accountability

**Market Risks:**
- Unproven demand → 20+ interviews + landing page validation
- Strong competition → Find niche or unique differentiation
- Monetization unclear → Research competitors + test early

## Decision Points & Kill Criteria

### Decision Checkpoint Examples

**Example 1: SaaS Analytics Tool - Month 1**
```
Metrics:
- Beta signups: 45 users ✅ (target: 20+)
- Active users: 12 (27% retention) ⚠️ (target: 40%+)
- Feedback: "Love the idea, UI is confusing" ⚠️
- Technical: No major blockers ✅

Decision: ITERATE
- Fix UI based on feedback (2 weeks)
- Re-check retention in Month 2
```

**Example 2: B2B Automation Tool - Month 3**
```
Metrics:
- Paying customers: 3 ($147 MRR) ✅ (target: 1+)
- Churn: 0% ✅
- CAC: $50, LTV: $600 ✅
- Growth: +30% MoM ✅

Decision: PROCEED
- Double down on acquisition
- Add features customers request
```

### Month 1 Checkpoint
**Evaluate:**
- User interest level
- Feedback quality
- Technical feasibility confirmed

**Continue if:**
- 10+ engaged beta users
- Positive core value prop feedback
- No critical technical blockers

**Pivot if:**
- Little user interest
- Negative feedback
- Major technical issues

### Month 3 Checkpoint
**Evaluate:**
- Retention metrics
- Revenue (if applicable)
- Market response

**Continue if:**
- Users returning 3+ times
- At least 1 paying customer
- Clear path forward

**Pivot if:**
- Users don't stick
- No willingness to pay
- Better opportunity identified

### Month 6 Checkpoint
**Evaluate:**
- Revenue trajectory
- Growth rate
- Sustainability

**Continue if:**
- Revenue >$500 MRR or growing >10%/mo
- Clear path to break-even
- Product-market fit indicators

**Abandon if:**
- Revenue <$200 MRR, flat growth
- Unsustainable costs
- Opportunity cost too high

## Integration with Action Plan

After decision:

**If PROCEED:**
- Generate action plan with business-orchestrator
- Set milestone-based timeline
- Define success metrics
- Plan decision checkpoints

**If ITERATE:**
- Identify specific improvements needed
- Set 30-day iteration cycle
- Re-run feasibility check
- Decide again with new data

**If ABANDON:**
- Document learnings
- Use idea-finder for new ideas
- Maintain relationships/audience
- Apply learnings to next idea

---

**See main SKILL.md for complete feasibility framework.**
