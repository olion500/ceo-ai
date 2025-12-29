# Synthesis Framework

Framework for integrating insights from multiple agents.

## Integrated Scoring Matrix

**Example: Developer Analytics Tool**

| Agent | Overall Score | Key Insights | Blockers | Opportunities |
|-------|---------------|--------------|----------|---------------|
| **Idea Evaluator** | 56/80 (70%) | Large market, clear monetization, crowded space | Differentiation weak | Creator economy growing |
| **Success Analyzer** | 8/10 (3 patterns) | Privacy-first wins, Simple UX wins, Open source builds trust | Network effects hard | Integration strategy clear |
| **Feasibility Checker** | 7.5/10 | Can build in 6mo, $0 start cost, 15hr/week doable | Need to learn analytics basics | React skills strong |

## Weighted Final Score

### Formula

```
FINAL_SCORE = (Idea_Score/80 × 40%) + (Success_Pattern_Match × 30%) + (Feasibility_Score/10 × 30%)

Where:
- Idea_Score: 0-80 from business-idea-evaluator
- Success_Pattern_Match: 0-10 (based on similar success cases found)
- Feasibility_Score: 0-10 from feasibility-checker
```

### Calculation Example

**Developer Analytics Tool:**
```
Idea_Score = 56/80 = 0.70
Success_Pattern_Match = 8/10 = 0.80
Feasibility_Score = 7.5/10 = 0.75

FINAL_SCORE = (0.70 × 40%) + (0.80 × 30%) + (0.75 × 30%)
             = 0.28 + 0.24 + 0.225
             = 0.745 × 10
             = 7.45/10

Result: 7.45/10 → STRONG POTENTIAL ✅
Category: "Strong potential, manageable risks"
Recommendation: PROCEED with defined risk mitigation
```

### Interpretation

- **8.0-10.0:** Exceptional opportunity, proceed with confidence
- **6.5-7.9:** Strong potential, manageable risks ← (Example: 7.45)
- **5.0-6.4:** Moderate potential, needs improvements
- **3.0-4.9:** High risk, major concerns
- **0.0-2.9:** Not recommended, pivot advised

## Risk Consolidation

### Cross-Agent Risk Analysis

**Example Continued:**

**Critical Risks (Must Address Before Proceeding):**
1. **Weak Differentiation in Crowded Market**
   - Source: Idea Evaluator (scored 5/10 on differentiation)
   - Impact: Critical (could fail to acquire customers)
   - Likelihood: 60% if not addressed
   - Mitigation: Position as "privacy-first analytics for creators" + focus on React integration niche
   - Owner: You (define unique positioning before launch)
   - Timeline: Before MVP build starts (Week 1)

**High Risks (Address in First 3 Months):**
1. **Analytics Knowledge Gap**
   - Source: Feasibility Checker (rated skill 3/10)
   - Impact: High (could delay launch 2-3 months)
   - Likelihood: 40%
   - Mitigation: Use ChartJS library instead of custom analytics, hire contractor for complex features
   - Owner: You (learn basics in Week 1-2)
   - Timeline: Weeks 1-4

2. **Network Effects Hard to Replicate**
   - Source: Success Analyzer (identified Beehiiv's advantage)
   - Impact: High (limits viral growth)
   - Likelihood: 70% (most products don't get viral)
   - Mitigation: Focus on integrations (Beehiiv, ConvertKit) instead of building network
   - Owner: You
   - Timeline: Months 2-4 (post-MVP)

**Medium Risks (Monitor and Manage):**
1. **Part-time Execution Speed**
   - Source: Feasibility Checker (15hr/week vs full-time competitors)
   - Impact: Medium (slower to market)
   - Likelihood: 80% (will be slower)
   - Mitigation: Cut scope 50%, focus on core analytics only for MVP
   - Owner: You
   - Timeline: Ongoing

## Opportunity Synthesis

### Cross-Agent Opportunities

**Example Continued:**

**Unique Advantages (From All Agents):**
1. **Strong React Skills + Creator Market Growth**
   - Source: Feasibility (8/10 React) + Idea Evaluator (8/10 market timing)
   - Leverage strategy: Build React component library for emails, launch on /r/reactjs + Show HN
   - Timeline: Launch open source components Week 4 for early traction

2. **$0 Infrastructure Cost**
   - Source: Feasibility Checker (all free tiers work for MVP)
   - Leverage strategy: Aggressive pricing ($9/mo) to undercut competitors charging $29-99
   - Timeline: Launch pricing (vs competitors' $29+)

3. **Clear Success Patterns Identified**
   - Source: Success Analyzer (3 similar cases studied)
   - Leverage strategy: Copy privacy-first messaging + simple UX + integration strategy
   - Timeline: Apply patterns from Day 1 (positioning, design, go-to-market)

**Quick Wins (Can Execute in 30 Days):**
1. **Landing Page + Email Waitlist**
   - Effort: Low (1-2 days)
   - Impact: Validate demand, get 50-100 emails
   - Action: Build with Vercel + Resend, post on Twitter + IH

2. **Open Source React Email Components**
   - Effort: Medium (1 week)
   - Impact: GitHub stars, distribution channel, trust
   - Action: Release 5 basic components, post on Show HN

3. **10 Creator Interviews**
   - Effort: Medium (2 weeks, 30min each)
   - Impact: Validate positioning, find pain points
   - Action: DM 50 creators on Twitter, book 10 calls

## See main SKILL.md for decision framework and templates.
