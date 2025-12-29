---
name: feasibility-checker
description: Validate execution feasibility for indie developers and small teams across technical, financial, and time dimensions. Use when checking if you can actually build something, estimating required resources, validating technical approach, calculating project costs, assessing time commitments, or determining if an idea is realistic for solo/small team execution. Covers skill gaps, infrastructure needs, budget requirements, and timeline estimation.
---

# Feasibility Checker

## Purpose

Systematically validate whether YOU can actually execute a business idea with your current resources, skills, and constraints. Focus on practical execution reality for indie developers and small teams.

**IMPORTANT - Documentation Links:**
- **Local document links**: Use markdown links `[Document Name](./relative-path.md)` for idea specs, success patterns, and related analysis
- **External links**: Include inline where data is cited (e.g., "CodeRabbit has [$15M ARR](https://techcrunch.com/...)")
- **References section**: Add comprehensive references list at end with all sources used

## When to Use This Skill

Automatically activates when you mention feasibility checks, resource requirements, technical/financial/time validation, skill gaps, execution capability, or solo/small team constraints. See skill-rules.json for complete trigger list.

## Three-Pillar Feasibility Framework

### Pillar 1: Technical Feasibility (能 - Ability)
**Can you technically build this?**

Quick assessment:
- Skills match: Rate 1-10 (your skills vs required)
- Technical complexity: Rate 1-10 (project complexity)
- Learning required: Estimate weeks needed

**For detailed assessment:** See [Technical Feasibility Guide](./resources/technical-feasibility.md)

### Pillar 2: Financial Feasibility (財 - Finance)
**Can you afford to build and run this?**

Quick assessment:
- Initial costs: Estimate $[X]
- Monthly operating costs: Estimate $[X]/mo
- Personal runway: Calculate months

**For detailed assessment:** See [Financial Feasibility Guide](./resources/financial-feasibility.md)

### Pillar 3: Time Feasibility (時 - Time)
**Can you complete this in reasonable timeframe?**

Quick assessment:
- MVP timeline: Estimate weeks/months
- Available time: Hours per week
- Opportunity cost: Acceptable vs alternatives?

**For detailed assessment:** See [Time Feasibility Guide](./resources/time-feasibility.md)

### Market & Competition (Additional Critical Factor)

**Does the market exist and can you compete?**

Quick assessment:
- Competitors found: Count direct competitors
- Market validation: Evidence of demand
- Revenue model: Proven monetization path?

**For detailed assessment:** See [Market & Competition Guide](./resources/market-competition.md)

## Assessment Workflow

### Quick Check (10 minutes)

**Use when:** Initial idea screening, quick go/no-go decision

```markdown
## Quick Feasibility Check

1. **Technical** (1-10): [Score]
   - Can you build this with current skills? [Yes/No/With learning]
   - Major technical blockers? [List or None]

2. **Financial** (1-10): [Score]
   - Can start with <$100? [Yes/No]
   - Have 3+ months runway? [Yes/No]

3. **Time** (1-10): [Score]
   - Can build MVP in <3 months? [Yes/No]
   - Have 10+ hours/week? [Yes/No]

4. **Market** (1-10): [Score]
   - Found 3+ competitors? [Yes/No] (Good sign if yes!)
   - Evidence of paying customers? [Yes/No]

**Quick Score:** [Average of 4 scores]

**Decision:**
- >7: Proceed to comprehensive assessment
- 5-7: Address specific concerns, then reassess
- <5: Likely not feasible, consider different idea
```

**Template:** [Quick Check Template](./resources/templates/quick-check.md)

### Comprehensive Assessment (1-2 hours)

**Use when:** Committed to idea, need detailed validation before building

**Step 1: Technical Deep Dive**
- Complete skills inventory and requirements matrix
- Calculate complexity scores for each component
- Identify learning needs and blockers
- Validate tech stack decisions

**Guide:** [Technical Feasibility Guide](./resources/technical-feasibility.md)

**Step 2: Market & Competition Research**
- Research competitors thoroughly (MUST use WebSearch)
- Analyze revenue models and pricing
- Identify market gaps and differentiation
- Validate short-term and long-term revenue potential

**Guide:** [Market & Competition Guide](./resources/market-competition.md)

**Step 3: Financial Analysis**
- Calculate initial development costs
- Plan free tier usage strategy
- Determine personal runway
- Model break-even requirements

**Guide:** [Financial Feasibility Guide](./resources/financial-feasibility.md)

**Step 4: Time & Opportunity Cost**
- Estimate detailed timeline
- Assess opportunity costs
- Plan milestone-based approach
- Set decision points

**Guide:** [Time Feasibility Guide](./resources/time-feasibility.md)

**Step 5: Integrated Assessment**
- Calculate weighted feasibility score
- Identify critical risks and mitigations
- Generate comprehensive report

**Template:** [Comprehensive Report Template](./resources/templates/feasibility-report.md)

## Scoring Framework

### Overall Feasibility Score

```
Feasibility Score = (Technical × 30%) + (Financial × 20%) + (Time × 20%) + (Market × 30%)

Where each component is scored 0-10
```

### Interpretation

- **0.0-3.0:** ❌ Not feasible, high risk of failure
- **3.1-5.0:** ⚠️ Challenging, significant obstacles to overcome
- **5.1-7.0:** 🟡 Feasible with effort, manageable risks
- **7.1-9.0:** ✅ Highly feasible, good odds of success
- **9.1-10.0:** ✅✅ Ideal conditions, proceed with confidence

### Component Score Guidelines

**Technical Feasibility (1-10):**
- 1-3: Major skill gaps, >3 months learning, critical blockers
- 4-6: Some gaps, 1-3 months learning, manageable risks
- 7-9: Strong match, minor gaps, low risk
- 10: Perfect match, can start immediately

**Financial Feasibility (1-10):**
- 1-3: High costs, limited runway, unclear path to revenue
- 4-6: Moderate costs, 3-6 months runway, uncertain revenue
- 7-9: Low costs, 6+ months runway, clear revenue path
- 10: Can start free, strong runway, pre-validated revenue

**Time Feasibility (1-10):**
- 1-3: >6 months MVP, limited time, high opportunity cost
- 4-6: 3-6 months MVP, moderate time, acceptable opportunity cost
- 7-9: 1-3 months MVP, sufficient time, good opportunity cost
- 10: <1 month MVP, abundant time, excellent opportunity cost

**Market Feasibility (1-10):**
- 1-3: Crowded market, no clear differentiation, unclear demand
- 4-6: Moderate competition, some differentiation, proven demand
- 7-9: Limited competition, strong differentiation, validated demand
- 10: Blue ocean, unique positioning, customers asking for it

## Decision Framework

### Proceed If (All must be true):
- ✅ Overall score >6.5/10
- ✅ No component <4/10
- ✅ No critical unmitigatable risks
- ✅ Clear path to first customer
- ✅ Personal excitement/commitment high

### Iterate/De-scope If:
- 🟡 Overall score 5-6.5/10
- 🟡 One component <5/10 but improvable
- 🟡 Risks exist but have mitigation plans
- 🟡 Can reduce scope to improve feasibility

### Abandon/Pivot If:
- ❌ Overall score <5/10
- ❌ Any component <3/10
- ❌ Critical blocker with no solution
- ❌ Better alternative opportunity exists

**Detailed Decision Framework:** [Decision Guide](./resources/decision-framework.md)

## Common Feasibility Mistakes

### Mistake 1: Overestimating Your Speed
**Problem:** "I can build this in 3 months" → actually takes 9 months
**Fix:** Add 2-3x buffer for unknowns, learning, and iteration
**Reality Check:** Track actual time on similar past projects

### Mistake 2: Underestimating Costs
**Problem:** "I'll just use free tiers" → hits limits fast
**Fix:** Research exact pricing tiers, plan upgrade triggers
**Reality Check:** Model costs at 10x, 100x current scale

### Mistake 3: Ignoring Skill Gaps
**Problem:** "I'll just learn as I go" → drowns in learning curve
**Fix:** Be honest about skill gaps, budget learning time
**Reality Check:** Test with small prototype first

### Mistake 4: Assuming Market Exists
**Problem:** "People will definitely pay for this"
**Fix:** ALWAYS research competitors and talk to customers
**Reality Check:** If no competitors exist, usually no market exists

### Mistake 5: Not Validating Revenue Early
**Problem:** "Build it first, monetize later"
**Fix:** Research competitor pricing, validate willingness to pay upfront
**Reality Check:** Pre-sell before building when possible

## Quick Reference

### Essential Checklists

**Before Starting Any Project:**
- [ ] Completed quick feasibility check (>7/10)
- [ ] Researched 5+ competitors thoroughly
- [ ] Talked to 10+ potential customers
- [ ] Validated pricing/willingness to pay
- [ ] Can build MVP in <3 months
- [ ] Have 6+ months personal runway
- [ ] Skills match >6/10

**Red Flags (Stop and reconsider):**
- ❌ No competitors found AND no clear market
- ❌ MVP timeline >6 months
- ❌ Skill gap >50% of requirements
- ❌ Unclear monetization path
- ❌ Personal runway <3 months
- ❌ Opportunity cost too high

**Green Flags (Proceed with confidence):**
- ✅ Found 3-10 competitors with paying customers
- ✅ Can build MVP in 1-3 months
- ✅ Skills match >7/10
- ✅ Can start with <$100
- ✅ 6+ months runway
- ✅ Clear revenue model
- ✅ Scratching own itch

## Integration with Other Skills

**After Feasibility Check:**

1. **If feasible (>6.5/10):**
   - Use `business-orchestrator` for comprehensive action plan
   - Use `success-formula-analyzer` to find similar success patterns
   - Start building with confidence

2. **If borderline (5-6.5/10):**
   - Use `business-idea-evaluator` to reconsider idea quality
   - Iterate on weak dimensions
   - Re-run feasibility check after improvements

3. **If not feasible (<5/10):**
   - Use `idea-finder` to generate alternative ideas
   - Consider pivoting or different approach
   - Document learnings for future reference

## Resources & Templates

### Detailed Guides
- [Technical Feasibility](./resources/technical-feasibility.md) - Skills, complexity, tech stack decisions
- [Financial Feasibility](./resources/financial-feasibility.md) - Costs, runway, revenue models
- [Time Feasibility](./resources/time-feasibility.md) - Timeline, opportunity cost
- [Market & Competition](./resources/market-competition.md) - Competitor research, revenue analysis
- [Decision Framework](./resources/decision-framework.md) - Risk mitigation, go/no-go criteria

### Templates
- [Quick Check Template](./resources/templates/quick-check.md) - 10-minute assessment
- [Comprehensive Report Template](./resources/templates/feasibility-report.md) - Full analysis

---

**Best Practice:** Start with quick check. Only do comprehensive assessment if quick check scores >7/10 and you're seriously committed to the idea.
