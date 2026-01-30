---
name: idea-elaborator
description: Elaborate and flesh out rough business ideas into detailed, concrete product concepts. Use when a user has a vague idea and needs it turned into a structured concept with core features, target customers, business model, differentiation, MVP scope, and positioning strategy. Bridges the gap between idea discovery and idea evaluation. Handles idea elaboration, concept development, idea detailing, product concepting, and idea refinement.
---

# Idea Elaborator

## Purpose

Transform rough, vague business ideas into detailed, actionable product concepts. This skill bridges the gap between idea discovery (idea-finder) and idea validation (idea-validator) by fleshing out the "what exactly would this be?" question.

## When to Use This Skill

Automatically activates when users mention elaborating, detailing, fleshing out, or concretizing a business idea. See skill-rules.json for complete trigger list.

**Typical input:** "개발자용 시간 관리 도구" (rough idea)
**Expected output:** Full product concept document with features, customers, model, positioning, MVP scope

## Pipeline Position

```
idea-finder → [idea-elaborator] → idea-validator → business-orchestrator
  발굴            구체화              검증+평가          종합 분석
```

## Elaboration Framework

### Phase 1: Idea Intake & Clarification

Before elaborating, gather context from the user:

**Required:**
- What's the core idea? (one sentence)
- Who is it for? (even a rough guess)
- What problem does it solve?

**Optional (ask if not provided):**
- Your skills/background
- Time commitment (full-time/side project)
- Revenue goal
- Specific inspiration or reference product

### Phase 2: Problem Deep Dive

Expand the problem space:

```markdown
## Problem Analysis

### Primary Problem
- What exactly hurts? [Specific pain description]
- How often does it occur? [Daily/Weekly/Monthly/Event-driven]
- What's the cost of NOT solving it? [Time/Money/Opportunity]

### Current Alternatives
- Alternative 1: [What exists] → Weakness: [Why inadequate]
- Alternative 2: [What exists] → Weakness: [Why inadequate]
- Workaround: [What people do now] → Friction: [Why painful]

### Problem Severity Signal
- Are people searching for solutions? [Evidence]
- Are people paying for imperfect solutions? [Evidence]
- Are people complaining in forums/communities? [Evidence]
```

### Phase 3: Target Customer Definition

Go from "developers" to a specific persona:

```markdown
## Target Customers

### Primary Persona
- **Who:** [Specific role + context]
- **Size:** [Estimated number of potential users]
- **Pain frequency:** [How often they face this]
- **Current spend:** [What they pay for alternatives]
- **Where they gather:** [Communities, platforms, events]

### Secondary Persona
- **Who:** [Adjacent audience]
- **Why secondary:** [Less urgent need or smaller segment]

### Anti-Persona (Who this is NOT for)
- **Exclude:** [Specific group and why]
```

### Phase 4: Product Concept

Define what the product actually IS:

```markdown
## Product Concept

### One-Line Pitch
[Product] helps [persona] do [outcome] by [mechanism].

### Core Value Proposition
- **Before:** [User's current painful state]
- **After:** [User's desired state with product]
- **Magic moment:** [The "aha" experience]

### Core Features (Must-Have for MVP)
1. **[Feature Name]** - [What it does] → [Why essential]
2. **[Feature Name]** - [What it does] → [Why essential]
3. **[Feature Name]** - [What it does] → [Why essential]
(Maximum 3-5 core features for MVP)

### Nice-to-Have Features (Post-MVP)
1. [Feature] - [Why deferred]
2. [Feature] - [Why deferred]
3. [Feature] - [Why deferred]

### Explicitly Out of Scope
1. [Feature/Scope] - [Why excluded]
2. [Feature/Scope] - [Why excluded]
```

### Phase 5: Business Model Design

```markdown
## Business Model

### Revenue Model
- **Type:** [SaaS/One-time/Freemium/Usage-based/Marketplace]
- **Pricing structure:**
  - Free tier: [What's included / or no free tier]
  - Paid tier 1: $[X]/month - [What's included]
  - Paid tier 2: $[X]/month - [What's included] (optional)
- **Pricing rationale:** [Why this price point]

### Unit Economics (Estimated)
- **Target MRR (12 months):** $[X]
- **Customers needed at target:** [N] (at $[X]/month avg)
- **Estimated CAC:** $[X] [Based on channel]
- **Estimated LTV:** $[X] [Based on churn assumption]
- **LTV:CAC Ratio:** [X]:1

### Revenue Milestones
- **Month 1-3:** $[X] MRR ([N] customers) - Validation
- **Month 4-6:** $[X] MRR ([N] customers) - Traction
- **Month 7-12:** $[X] MRR ([N] customers) - Growth
```

### Phase 6: Differentiation & Positioning

```markdown
## Differentiation Strategy

### Competitive Landscape
| Competitor | Strengths | Weaknesses | Our Advantage |
|-----------|-----------|------------|---------------|
| [Name] | [List] | [List] | [How we're better] |
| [Name] | [List] | [List] | [How we're better] |
| [Name] | [List] | [List] | [How we're better] |

### Positioning Statement
For [target persona] who [need/pain], [Product Name] is a [category]
that [key benefit]. Unlike [primary competitor], we [key differentiator].

### Unique Angles (Pick 1-2)
- **Speed:** Faster to use / faster results
- **Simplicity:** Radically simpler than alternatives
- **Price:** More affordable for target segment
- **Niche focus:** Purpose-built for specific use case
- **Integration:** Works with tools they already use
- **Design:** Significantly better UX
- **AI-native:** Built with AI from ground up
- **Community:** Built with/for a specific community
```

### Phase 7: MVP Scope Definition

```markdown
## MVP Definition

### MVP Goal
Validate that [specific hypothesis] by getting [metric] within [timeframe].

### MVP Feature Set
| Feature | Priority | Complexity | Included in MVP? |
|---------|----------|------------|-----------------|
| [Feature 1] | Must | Low | Yes |
| [Feature 2] | Must | Medium | Yes |
| [Feature 3] | Should | Low | Yes |
| [Feature 4] | Could | High | No - Post-MVP |

### Tech Stack Suggestion
- **Frontend:** [Recommendation + why]
- **Backend:** [Recommendation + why]
- **Database:** [Recommendation + why]
- **Hosting:** [Recommendation + why]
- **Key 3rd-party:** [APIs/services needed]

### MVP Success Criteria
- [ ] [N] users signed up within [timeframe]
- [ ] [N] users completed core action
- [ ] [N] users willing to pay
- [ ] NPS score > [X] from beta users
- [ ] Retention: [X]% return within [timeframe]
```

### Phase 8: Go-to-Market Sketch

```markdown
## Go-to-Market Strategy

### Launch Channels (Ranked by fit)
1. **[Channel]** - [Why suitable] - Expected reach: [N]
2. **[Channel]** - [Why suitable] - Expected reach: [N]
3. **[Channel]** - [Why suitable] - Expected reach: [N]

### Content/Marketing Angle
- **Story:** [What narrative resonates with audience]
- **Hook:** [What catches attention]
- **Proof:** [What builds credibility]

### First 100 Customers Plan
1. **Customers 1-10:** [Direct outreach strategy]
2. **Customers 11-50:** [Community/content strategy]
3. **Customers 51-100:** [Scalable channel strategy]
```

## Output Template

**IMPORTANT:** Save elaborated ideas to `research/ideas/` folder using this template.

```markdown
---
title: "[Product Name] - Idea Elaboration"
date: YYYY-MM-DD
type: Idea Elaboration
status: Elaborated
original-idea: "[Original rough idea from user]"
one-line-pitch: "[Product] helps [persona] do [outcome] by [mechanism]"
target-customer: "[Primary persona]"
revenue-model: "[SaaS/One-time/Freemium/etc]"
tags: [idea-elaboration, category-tags]
---

# [Product Name]: Idea Elaboration

## Original Idea
> [User's original rough idea, verbatim]

## Executive Summary
[2-3 sentences: what it is, who it's for, why it matters]

## Problem Analysis
[Phase 2 output]

## Target Customers
[Phase 3 output]

## Product Concept
[Phase 4 output]

## Business Model
[Phase 5 output]

## Differentiation & Positioning
[Phase 6 output]

## MVP Definition
[Phase 7 output]

## Go-to-Market Sketch
[Phase 8 output]

## Open Questions
- [Question that needs validation]
- [Assumption that needs testing]
- [Decision that needs user input]

## Recommended Next Steps
1. **Validate:** Use `idea-validator` to score and validate this concept (6 frameworks)
2. **Full Analysis:** Use `business-orchestrator` for comprehensive plan with success patterns

---
*Elaborated by idea-elaborator skill*
*Original idea → Detailed concept → Ready for evaluation*
```

## Elaboration Quality Checklist

Before completing, verify:

- [ ] Original idea preserved verbatim
- [ ] Problem is specific, not generic
- [ ] Target customer is a real person, not "everyone"
- [ ] Core features limited to 3-5 (not a feature wishlist)
- [ ] Business model has specific pricing numbers
- [ ] At least 2 competitors identified
- [ ] Positioning statement is clear and specific
- [ ] MVP scope is achievable in <3 months
- [ ] Go-to-market has concrete first steps
- [ ] Open questions are honest about unknowns

## Common Mistakes to Avoid

### Mistake 1: Over-Elaboration
**Problem:** Turning a simple idea into an enterprise platform
**Fix:** Keep MVP scope ruthlessly small. "What's the smallest thing that delivers value?"

### Mistake 2: Feature Stuffing
**Problem:** Listing 20+ features "needed" for launch
**Fix:** Max 3-5 core features. Ask: "Would a user pay for JUST this one feature?"

### Mistake 3: Vague Target Customer
**Problem:** "Developers" or "small businesses" as target
**Fix:** Specify role, company size, pain frequency. "Senior backend developers at 10-50 person startups who deploy daily"

### Mistake 4: Copying Competitor Positioning
**Problem:** "Like [Competitor] but better"
**Fix:** Find a unique angle. Better for WHO? Better HOW specifically?

### Mistake 5: Ignoring Distribution
**Problem:** Great product concept, no idea how to reach customers
**Fix:** Always include go-to-market sketch. If you can't describe how customer #1 finds you, the concept is incomplete.

## Integration with Other Skills

### Before Idea Elaborator
- `idea-finder` → generates rough ideas to elaborate
- `success-story-researcher` → provides market context

### After Idea Elaborator
1. `idea-validator` → score and validate the elaborated concept (6 frameworks, composite score)
2. `business-orchestrator` → comprehensive analysis with success patterns + action plan

### Full Pipeline
```
idea-finder (discover)
    ↓
idea-elaborator (flesh out)  ← YOU ARE HERE
    ↓
idea-validator (score + validate)
    ↓
business-orchestrator (plan)
```

---

**Key Principle:** Elaboration ≠ Validation. This skill makes ideas concrete and specific, but doesn't prove they'll work. Always follow up with evaluation and feasibility checking.
