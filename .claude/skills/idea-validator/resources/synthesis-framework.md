# Synthesis Framework

## Purpose

Integrate results from all 6 analysis frameworks into a unified composite score and actionable recommendation.

## Composite Score Calculation

```
Composite = (Market Opportunity × 20%) + (Execution Feasibility × 20%) +
            (Strategic Position × 15%) + (Risk Profile × 15%) +
            (Intellectual Honesty × 10%) + (Investment Worthiness × 20%)
```

### Weight Rationale

| Framework | Weight | Why |
|-----------|--------|-----|
| Market Opportunity | 20% | No market = no business, foundational |
| Execution Feasibility | 20% | Can't execute = idea stays an idea |
| Strategic Position | 15% | Determines long-term viability |
| Risk Profile | 15% | Unmanaged risks kill businesses |
| Intellectual Honesty | 10% | Keeps evaluation grounded in reality |
| Investment Worthiness | 20% | Numbers must work for sustainability |

### Custom Weight Adjustments

Adjust weights based on founder context:

**First-time founder (increase safety):**
```
Market: 15% | Execution: 25% | Strategic: 10% | Risk: 20% | Honesty: 10% | Investment: 20%
```

**Experienced builder (increase ambition):**
```
Market: 25% | Execution: 15% | Strategic: 20% | Risk: 10% | Honesty: 10% | Investment: 20%
```

**Resource-constrained (increase feasibility):**
```
Market: 15% | Execution: 30% | Strategic: 10% | Risk: 15% | Honesty: 10% | Investment: 20%
```

## Cross-Framework Analysis

After individual scores, perform cross-framework synthesis:

### 1. Consensus Points

**Agreement matrix:** Where do 4+ frameworks agree?

| Signal | Frameworks Agreeing | Confidence |
|--------|-------------------|-----------|
| [Strength/Weakness] | [List frameworks] | [High/Med/Low] |
| [Strength/Weakness] | [List frameworks] | [High/Med/Low] |

### 2. Divergence Points

**Contradiction matrix:** Where do frameworks disagree?

| Point | Framework A Says | Framework B Says | Resolution |
|-------|-----------------|-----------------|-----------|
| [Topic] | [View] | [View] | [Which to trust and why] |

### 3. Emergent Insights

Insights that only appear when combining multiple framework results:
- Pattern across frameworks that individual analysis missed
- Risk-opportunity combinations
- Strategic positioning implications from execution constraints

## Score Interpretation

### Individual Framework Thresholds

Each framework score has significance:

| Score Range | Individual Meaning | Action |
|------------|-------------------|--------|
| 8-10 | Exceptional strength | Leverage aggressively |
| 6-7.9 | Solid foundation | Build upon |
| 4-5.9 | Needs work | Address before proceeding |
| 2-3.9 | Critical weakness | Must fix or pivot |
| 0-1.9 | Disqualifying | Deal-breaker territory |

### Override Rules

Even with a good composite score, certain conditions override:

**Automatic downgrade triggers:**
- Any single framework < 3.0 → Cap composite at 5.9 (cannot be GO)
- Two frameworks < 4.0 → Cap composite at 4.9 (force PIVOT or NO-GO)
- Fatal risk identified → Cap composite at 5.4 regardless of score
- Zero validated assumptions → Cap composite at 5.0

## Quick Check Synthesis (3 frameworks)

When running Quick Check mode (Startup Validator + Execution Auditor + Risk Analyst):

```
Quick Composite = (Market Opportunity × 35%) + (Execution Feasibility × 35%) + (Risk Profile × 30%)
```

Quick Check uses higher weights on the three evaluated dimensions and applies the same decision thresholds but with a "preliminary" label.

## Output Template

```markdown
## Synthesis

### Composite Score: X.X/10

| Framework | Score | Weight | Weighted |
|-----------|-------|--------|----------|
| Market Opportunity | X.X | 20% | X.X |
| Execution Feasibility | X.X | 20% | X.X |
| Strategic Position | X.X | 15% | X.X |
| Risk Profile | X.X | 15% | X.X |
| Intellectual Honesty | X.X | 10% | X.X |
| Investment Worthiness | X.X | 20% | X.X |

### Cross-Framework Consensus
- **Agree (Strengths):** [What multiple frameworks confirm as strong]
- **Agree (Weaknesses):** [What multiple frameworks confirm as weak]
- **Disagree:** [Where frameworks conflict and resolution]

### Override Conditions
- [Any override triggers active? Y/N and details]

### Emergent Insights
- [Insight only visible from combining frameworks]
```
