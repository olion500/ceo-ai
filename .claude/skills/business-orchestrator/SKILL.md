---
name: business-orchestrator
description: Orchestrate comprehensive business analysis by coordinating success-formula-analyzer, business-idea-evaluator, and feasibility-checker agents. Use when you need complete business validation, end-to-end idea analysis, multi-agent coordination, integrated business assessment, or action plan creation. Provides workflow coordination, result synthesis, and actionable recommendations for indie developers and small teams.
---

# Business Orchestrator

## Purpose

Coordinate multiple business analysis agents to provide comprehensive, evidence-based assessment and actionable roadmap for indie developers and small teams. Act as the central intelligence that synthesizes insights from specialized agents.

## When to Use This Skill

Automatically activates when you mention complete business analysis, full validation, end-to-end assessment, multi-agent coordination, or comprehensive evaluation. See skill-rules.json for complete trigger list.

## Multi-Agent Network

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
│ • Patterns      │ │ • 8 dimensions  │ │ • Technical     │
│ • Revenue model │ │ • Risk analysis │ │ • Financial     │
│ • Tactics       │ │ • Positioning   │ │ • Time/Market   │
└─────────────────┘ └─────────────────┘ └─────────────────┘
```

## Three Core Workflows

### Workflow 1: Idea Validation (Most Common)

**Use Case:** "I have a business idea, is it worth building?"

**Process:**
1. **Business Idea Evaluator** - Score across 8 dimensions
2. **Success Formula Analyzer** - Find similar successful cases
3. **Feasibility Checker** - Validate YOU can execute
4. **Synthesis** - Integrated assessment and action plan

**Decision Points:**
- If idea score >55: Proceed to feasibility
- If feasibility >6.5: Generate action plan
- Otherwise: Iterate or pivot

**Detailed Guide:** [Idea Validation Workflow](./resources/workflows/idea-validation.md)

### Workflow 2: Learning from Success

**Use Case:** "Analyze how [Product X] succeeded and apply to my idea"

**Process:**
1. **Success Formula Analyzer** - Deep dive into successful product
2. **Business Idea Evaluator** - Map your idea to success patterns
3. **Feasibility Checker** - Validate replicability
4. **Synthesis** - Adaptation plan

**Detailed Guide:** [Success Learning Workflow](./resources/workflows/success-learning.md)

### Workflow 3: Competitive Positioning

**Use Case:** "Help me position against existing competitors"

**Process:**
1. **Business Idea Evaluator** - Competitive landscape analysis
2. **Success Formula Analyzer** - How late entrants won
3. **Feasibility Checker** - Can you execute differentiation?
4. **Synthesis** - Positioning strategy

**Detailed Guide:** [Competitive Positioning Workflow](./resources/workflows/competitive-positioning.md)

## Orchestration Approach

### Sequential vs Parallel

**Run in Parallel (Faster):**
- Idea Evaluator + Feasibility Checker simultaneously
- When agents don't depend on each other
- Use when time is critical

**Run Sequential (More Thorough):**
- Use Success Analyzer output to inform Idea Evaluator
- Use Idea Evaluator score to decide if feasibility needed
- Better for iterative refinement

### Iterative Refinement Pattern

```
1. Run all agents once (parallel)
2. Identify weakest dimension(s)
3. Brainstorm specific improvements
4. Re-run affected agent(s)
5. Compare before/after scores
6. Iterate until score stabilizes or improves
```

## Synthesis Framework

### Integrated Scoring

```
Final Score = (Idea Score/80 × 40%) +
              (Success Pattern Match × 30%) +
              (Feasibility Score/10 × 30%)

Where:
- Idea Score: 0-80 from business-idea-evaluator
- Success Pattern Match: 0-10 (based on similar cases found)
- Feasibility Score: 0-10 from feasibility-checker
```

### Interpretation

- **8.0-10.0:** ✅✅ Exceptional opportunity, proceed with confidence
- **6.5-7.9:** ✅ Strong potential, manageable risks
- **5.0-6.4:** 🟡 Moderate potential, needs improvements
- **3.0-4.9:** ⚠️ High risk, major concerns
- **0.0-2.9:** ❌ Not recommended, pivot advised

**Detailed Framework:** [Synthesis Framework](./resources/synthesis-framework.md)

## Decision Framework

### Proceed If (All must be true):
- ✅ Final score >6.5/10
- ✅ No critical unmitigatable risks
- ✅ Feasibility score >6/10
- ✅ Success patterns identified
- ✅ Clear differentiation exists
- ✅ Monetization path validated
- ✅ Personal excitement high

### Iterate If:
- 🟡 Final score 5-6.5/10
- 🟡 Some risks with mitigation paths
- 🟡 One dimension scoring <5
- 🟡 Can improve feasibility by de-scoping

### Pivot/Abandon If:
- ❌ Final score <5/10
- ❌ Critical risks, no mitigation
- ❌ Feasibility score <4/10
- ❌ No similar success patterns
- ❌ Unclear monetization

## Comprehensive Analysis Process

### Step 1: Gather Input

**Required information:**
```markdown
## Business Idea

**Problem:** [What problem are you solving?]
**Solution:** [Your proposed solution]
**Target Audience:** [Who specifically?]
**Business Model:** [How will you make money?]

## Your Context

**Skills:** [Relevant technical/domain skills]
**Time Available:** [Hours per week]
**Budget:** [Can invest $X]
**Runway:** [Months of personal savings]
**Network:** [Relevant audience/connections]

## Competitors (if known)

- [Competitor 1]: [URL]
- [Competitor 2]: [URL]
```

### Step 2: Run Agents

**Option A: Parallel (Fast - 10-15 min)**
```bash
# Run all 3 agents simultaneously
1. business-idea-evaluator → Score & risks
2. success-formula-analyzer → Similar cases
3. feasibility-checker → Execution validation
```

**Option B: Sequential (Thorough - 20-30 min)**
```bash
1. business-idea-evaluator → Get score
   └─ If >40/80, continue
2. success-formula-analyzer → Find patterns
   └─ Use patterns to refine idea
3. feasibility-checker → Deep validation
   └─ Generate execution plan
```

### Step 3: Synthesize Results

**Cross-Agent Analysis:**
- What do all agents agree on?
- Where do agents diverge?
- What surprising insights emerged?
- What are consensus risks?
- What are consensus opportunities?

### Step 4: Generate Action Plan

Based on final recommendation:
- **If GO:** 4-phase action plan (Pre-dev → MVP → Beta → Launch)
- **If ITERATE:** Specific improvement roadmap
- **If NO-GO:** Alternative options or pivot strategies

**Template:** [Comprehensive Report Template](./resources/templates/comprehensive-report.md)

## Quick Reference

### When to Use Each Agent Individually

**Use business-idea-evaluator when:**
- Quickly comparing multiple ideas
- Need structured scoring framework
- Evaluating market opportunity
- Assessing competitive landscape

**Use success-formula-analyzer when:**
- Found inspiring successful product
- Need validation of approach
- Want reproducible tactics
- Looking for proven patterns

**Use feasibility-checker when:**
- Ready to commit to idea
- Need execution validation
- Assessing personal capability
- Planning resource requirements

**Use business-orchestrator when:**
- Need complete validation
- Making significant commitment (time/money)
- Want comprehensive assessment
- Need action plan with confidence

### Integration with Other Skills

**Before orchestration:**
- Use `idea-finder` if you don't have ideas yet
- Use `success-story-researcher` to find more examples

**After orchestration:**
- If GO: Start building with generated action plan
- If ITERATE: Use specific agent to improve weak areas
- If NO-GO: Use `idea-finder` for alternatives

## Master Orchestration Prompt

When user requests full business analysis:

```
I'll run comprehensive business analysis using our multi-agent system:

**Agents:**
1. Business Idea Evaluator - Score across 8 dimensions
2. Success Formula Analyzer - Find similar successful cases
3. Feasibility Checker - Validate YOUR execution capability

**Output:**
✅ Detailed agent reports
✅ Integrated synthesis and insights
✅ Clear Go/No-go recommendation
✅ Actionable roadmap if proceeding

**Please provide:**
- Your business idea (problem + solution)
- Target audience
- Your background (skills, time, budget)
- Any known competitors

Let's begin!
```

## Customization Options

### Adjust Scoring Weights

Default weights:
- Idea Quality: 40%
- Success Patterns: 30%
- Feasibility: 30%

**Customize based on priorities:**
- Financially constrained? Increase feasibility weight (40-50%)
- Passionate about idea? Increase success patterns weight
- Experienced builder? Increase idea quality weight (50%)

### Workflow Customization

Choose workflow based on situation:
- **New to entrepreneurship:** Start with Workflow 2 (learning from success)
- **Have specific idea:** Use Workflow 1 (idea validation)
- **Crowded market:** Use Workflow 3 (competitive positioning)
- **No idea yet:** Use `idea-finder` first, then Workflow 1

## Resources & Templates

### Detailed Workflows
- [Idea Validation](./resources/workflows/idea-validation.md) - Most common workflow
- [Success Learning](./resources/workflows/success-learning.md) - Learn from winners
- [Competitive Positioning](./resources/workflows/competitive-positioning.md) - Differentiation strategy

### Frameworks
- [Synthesis Framework](./resources/synthesis-framework.md) - Integration methodology
- [Decision Framework](./resources/decision-framework.md) - Go/no-go criteria

### Templates
- [Comprehensive Report](./resources/templates/comprehensive-report.md) - Full analysis output
- [Action Plan Template](./resources/templates/action-plan.md) - 4-phase execution plan

---

**Best Practice:** Start with idea validation workflow. Use other workflows for specific needs. Always synthesize insights from all agents before making final decision.
