# Idea Validation Workflow

Complete workflow for validating if a business idea is worth building.

## Overview

**Use Case:** "I have a business idea, is it worth building?"

This is the most common orchestration workflow.

## Workflow Steps

### Step 1: Initial Assessment (business-idea-evaluator)

**Input:** Raw business idea description
**Output:**
- 8-dimension score (1-10 each)
- Overall viability score (/80)
- Key risks identified
- Preliminary recommendation

**Real Example: Email Newsletter Analytics Tool**
```
Idea: "Analytics dashboard for newsletter creators showing open rates, click patterns, and revenue attribution"

Agent Output:
1. Market Size: 8/10 (large creator economy)
2. Competition: 6/10 (Beehiiv, ConvertKit have this)
3. Monetization: 9/10 (clear SaaS model)
4. Differentiation: 5/10 (crowded space)
5. Solo Viability: 7/10 (feasible for 1 person)
6. Execution Complexity: 6/10 (medium)
7. Market Timing: 8/10 (creators growing)
8. Customer Acquisition: 7/10 (clear channels)

Overall: 56/80 (70%) → PROCEED with caution
Key Risk: Differentiation needed
```

**Decision Point:**
- If score >55: Proceed to Step 2 ✅
- If score 40-55: Refine idea, iterate dimensions
- If score <40: Consider pivot or different idea

### Step 2: Success Pattern Matching (success-formula-analyzer)

**Input:** Idea + similar successful cases
**Output:**
- 3-5 similar successful products
- Common success patterns
- Reproducible tactics for your context
- Warning signs from similar cases

**Real Example (continued):**
```
Agent searches and finds:
- Beehiiv ($15M ARR) - built creator network + referral system
- Plausible ($4M ARR) - privacy-first positioning
- Fathom ($1M ARR) - simpler UX than Google Analytics

Common Pattern Identified:
✅ "Privacy-first" messaging resonates with creators
✅ Simple UX beats feature-rich competitors
✅ Built-in distribution (integrations with ConvertKit, Substack)
⚠️ Network effects hard to replicate (Beehiiv's advantage)

Tactics to Apply:
1. Position as "privacy-first analytics for creators"
2. Make UX 10x simpler than existing tools
3. Build integrations with Beehiiv, ConvertKit, Buttondown
4. Launch on Indie Hackers, Product Hunt
```

**Decision Point:**
- If patterns found: Apply to your idea ✅
- If no patterns: Red flag, might be too unique/unproven
- Adapt successful tactics to your context

### Step 3: Execution Validation (feasibility-checker)

**Input:** Idea + your personal context (skills, time, budget)
**Output:**
- Technical feasibility (1-10)
- Financial feasibility (1-10)
- Time feasibility (1-10)
- Overall feasibility score

**Real Example (continued):**
```
Your Context:
- Skills: React (8/10), Node.js (7/10), Analytics (3/10)
- Time: 15 hours/week for 6 months
- Budget: $500 total

Agent Assessment:
- Technical: 7/10 (can use ChartJS, learn basics of analytics)
- Financial: 9/10 (can start with $0, all free tiers)
- Time: 6/10 (6 months realistic with scope cut)
- Market: 8/10 (validated market, clear monetization)

Overall Feasibility: 7.5/10 → PROCEED

Recommendations:
- Use ChartJS (not custom D3) to save time
- Start with basic metrics only, add advanced later
- Use Stripe for payments (don't build billing)
- Cut integrations to 2-3 most popular platforms for MVP
```

**Decision Point:**
- If >6.5/10: Proceed to action plan (Step 4) ✅
- If 5-6.5/10: De-scope and re-check
- If <5/10: Not feasible with current resources

### Step 4: Synthesis & Action Plan

**Input:** All agent outputs
**Output:**
- Integrated assessment
- Go/No-go recommendation
- Detailed action plan if "Go"
- Alternative options if "No-go"

**Real Example (Final Synthesis):**
```
INTEGRATED ASSESSMENT:
======================
Business Viability: 56/80 (70%) - GOOD
Feasibility Score: 7.5/10 - STRONG
Success Patterns: Found 3 similar cases - VALIDATED

FINAL RECOMMENDATION: GO ✅

Confidence Level: 75%
Expected Timeline: 6 months to launch
Expected First Revenue: Month 2-3 ($100-500)

4-PHASE ACTION PLAN:
====================
Phase 1 (Weeks 1-4): Validation
- Build landing page (Week 1)
- Get 50 creator emails (Week 2-3)
- 10 customer interviews (Week 4)
- GO/NO-GO checkpoint

Phase 2 (Weeks 5-12): MVP Build
- Core dashboard (Week 5-8)
- Beehiiv integration (Week 9-10)
- Stripe payments (Week 11)
- Beta testing (Week 12)

Phase 3 (Weeks 13-16): Launch
- Product Hunt launch
- Indie Hackers post
- Creator outreach (50 DMs)
- Target: 10 paying customers

Phase 4 (Weeks 17-24): Iterate
- Add requested features
- Build 2nd integration
- Focus on retention
- Target: $1K MRR
```

## See main SKILL.md for synthesis framework and templates.
