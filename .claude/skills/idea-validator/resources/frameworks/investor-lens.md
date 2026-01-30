# Investor Lens Framework

## Core Question

**스마트 머니가 투자할 것인가?** (Would smart money invest in this?)

## Score: Investment Worthiness (0-10)

This framework evaluates the idea through the lens of a rational investor — not necessarily seeking VC money, but applying the same rigor to your own time/money investment.

## Evaluation Dimensions

### 1. Unit Economics (0-10)

**What to assess:** Do the numbers work at the individual customer level?

| Score | Economics Level | Criteria |
|-------|----------------|---------|
| 0-2 | Broken | CAC > LTV, negative margins, no path to profitability |
| 3-4 | Questionable | CAC close to LTV, thin margins, requires scale |
| 5-6 | Workable | LTV:CAC 2-3:1, moderate margins, path visible |
| 7-8 | Strong | LTV:CAC 3-5:1, healthy margins, clear path |
| 9-10 | Exceptional | LTV:CAC >5:1, high margins, compounding revenue |

**Key metrics to calculate:**

```
CAC (Customer Acquisition Cost):
  = Total acquisition spend / New customers acquired
  Target for indie: < $50 (organic channels preferred)

LTV (Lifetime Value):
  = ARPU × Average customer lifespan (months)
  Or: ARPU / Monthly churn rate

LTV:CAC Ratio:
  Target: > 3:1 for sustainability
  Ideal: > 5:1 for growth

Payback Period:
  = CAC / Monthly ARPU
  Target: < 6 months

Gross Margin:
  = (Revenue - COGS) / Revenue
  SaaS target: > 70%
  Tool target: > 80%
```

### 2. Return on Investment (0-10)

**What to assess:** Is the expected return worth the investment of time and money?

| Score | ROI Level | Criteria |
|-------|----------|---------|
| 0-2 | Negative ROI | Expected loss, better alternatives exist |
| 3-4 | Low ROI | Marginal returns, high opportunity cost |
| 5-6 | Moderate ROI | Reasonable returns, comparable to alternatives |
| 7-8 | Strong ROI | Clear upside, favorable risk-reward ratio |
| 9-10 | Exceptional ROI | Asymmetric upside, minimal downside risk |

**ROI calculation for indie founders:**

```
Investment:
  - Time: [X] hours/week × [X] weeks × $[hourly value] = $[total]
  - Money: $[total direct costs]
  - Opportunity cost: $[foregone income/projects]
  Total Investment: $[sum]

Expected Return (12 months):
  - Best case: $[X] MRR × 12 = $[annual]
  - Base case: $[X] MRR × 12 = $[annual]
  - Worst case: $[X] (learning + assets built)

Expected ROI = (Base case return - Investment) / Investment × 100%
```

### 3. Scalability Assessment (0-10)

**What to assess:** Can this grow without proportional increase in effort?

| Score | Scalability Level | Criteria |
|-------|------------------|---------|
| 0-2 | Doesn't scale | Revenue = Time (consulting, services) |
| 3-4 | Limited scale | Some leverage but manual elements remain |
| 5-6 | Moderate scale | Software model with some manual parts |
| 7-8 | Highly scalable | Pure software, minimal per-customer cost |
| 9-10 | Infinite scale | Platform/marketplace, zero marginal cost |

**Scalability indicators:**
- Revenue per employee/founder hour trends up over time?
- Adding 10x customers requires 10x effort? (Bad) or 2x effort? (Good)
- Are there natural viral/organic growth loops?
- Does the product improve with usage (data effects)?

### 4. Revenue Quality & Predictability (0-10)

**What to assess:** How reliable and predictable is the revenue?

| Score | Revenue Quality | Criteria |
|-------|----------------|---------|
| 0-2 | Unpredictable | One-time sales, project-based, seasonal |
| 3-4 | Somewhat predictable | Repeat purchases but no lock-in |
| 5-6 | Moderately predictable | Subscription with moderate churn (>8% monthly) |
| 7-8 | Predictable | Subscription with low churn (<5% monthly) |
| 9-10 | Highly predictable | Annual contracts, negative churn, embedded workflow |

**Revenue quality factors:**
- **Recurring vs one-time**: Monthly/annual subscriptions preferred
- **Churn rate**: Lower is dramatically better (compounds)
- **Net revenue retention**: Do existing customers spend more over time?
- **Revenue diversity**: Not dependent on one large customer
- **Pricing power**: Can you raise prices without losing customers?

## Scoring Formula

```
Investment Worthiness = (Unit Economics × 30%) + (ROI × 25%) + (Scalability × 25%) + (Revenue Quality × 20%)
```

## Output Format

```markdown
### Investor Lens: Investment Worthiness Score

**Overall: X.X/10**

| Dimension | Score | Weight | Weighted |
|-----------|-------|--------|----------|
| Unit Economics | X/10 | 30% | X.X |
| ROI Potential | X/10 | 25% | X.X |
| Scalability | X/10 | 25% | X.X |
| Revenue Quality | X/10 | 20% | X.X |

**Key Numbers:**
- Estimated LTV:CAC: [X]:1
- Target MRR (12 months): $[X]
- Gross margin: [X]%
- Payback period: [X] months

**Investment Thesis (Why This Works):**
- [Reason 1]
- [Reason 2]

**Investment Concerns (Why This Might Not Work):**
- [Concern 1]
- [Concern 2]

**Comparable Exits/Outcomes:**
- [Similar product]: [Outcome achieved]

**Investment Verdict:** [One sentence summary]
```

## Common Pitfalls

- **Vanity metrics**: Users ≠ revenue. Downloads ≠ customers. Pageviews ≠ business.
- **Hockey stick projections**: Linear growth is the norm, exponential growth is the exception
- **Ignoring churn**: A small monthly churn rate destroys businesses over time
- **Undervaluing time**: Your time has a dollar value — account for it
- **Confusing revenue and profit**: Revenue means nothing if costs are higher
