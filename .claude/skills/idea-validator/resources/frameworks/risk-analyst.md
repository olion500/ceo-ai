# Risk Analyst Framework

## Core Question

**무엇이 이것을 죽일 것인가?** (What will kill this?)

## Score: Risk Profile (0-10)

This framework identifies and scores existential risks, dependencies, and blind spots. Higher score = lower risk = better.

## Evaluation Dimensions

### 1. Failure Scenario Analysis (0-10, lower risk = higher score)

**What to assess:** What are the most likely ways this fails?

**Systematic failure categories:**

| Category | Description | Example |
|----------|------------|---------|
| **Market risk** | No one wants it | Building solution to non-problem |
| **Execution risk** | Can't build it well enough | Technical challenges, quality issues |
| **Timing risk** | Too early or too late | Market not ready, or already saturated |
| **Competition risk** | Outcompeted | Incumbent launches similar, VC-funded clone |
| **Business model risk** | Can't monetize | Users won't pay, unit economics don't work |
| **Founder risk** | Personal burnout/pivot | Motivation loss, life changes, skills gap |
| **Platform risk** | Dependent on platform changes | API deprecation, policy changes |
| **Regulatory risk** | Legal/compliance issues | Data privacy, industry regulations |

**Scoring:**
- 0-2: Multiple high-probability failure paths, existential risks present
- 3-4: 2-3 significant failure paths, some mitigatable
- 5-6: 1-2 moderate failure paths, all have mitigation plans
- 7-8: Minor failure paths only, strong mitigations in place
- 9-10: No significant failure paths identified, robust against scenarios

### 2. Dependency & Fragility Analysis (0-10)

**What to assess:** How many single points of failure exist?

| Score | Fragility Level | Criteria |
|-------|----------------|---------|
| 0-2 | Extremely fragile | 3+ single points of failure, any could kill the business |
| 3-4 | Fragile | 2 critical dependencies, limited alternatives |
| 5-6 | Moderate | 1 critical dependency with backup plan |
| 7-8 | Resilient | No critical dependencies, multiple alternatives for each |
| 9-10 | Anti-fragile | Gets stronger from disruptions, self-reinforcing |

**Dependency audit:**

```
Dependency           | Type     | Criticality | Alternative?
--------------------|----------|-------------|-------------
[API/Platform]       | Tech     | High/Med/Low| [Y/N: what]
[Payment provider]   | Business | High/Med/Low| [Y/N: what]
[Distribution ch.]   | Market   | High/Med/Low| [Y/N: what]
[Key person]         | Team     | High/Med/Low| [Y/N: what]
```

### 3. External Threat Assessment (0-10)

**What to assess:** What external forces could destroy this?

**Threat categories:**

| Threat | Probability | Impact | Mitigation |
|--------|------------|--------|-----------|
| **Big Tech entry** | [H/M/L] | [H/M/L] | [Strategy] |
| **VC-funded competitor** | [H/M/L] | [H/M/L] | [Strategy] |
| **Platform policy change** | [H/M/L] | [H/M/L] | [Strategy] |
| **Technology shift** | [H/M/L] | [H/M/L] | [Strategy] |
| **Regulatory change** | [H/M/L] | [H/M/L] | [Strategy] |
| **Economic downturn** | [H/M/L] | [H/M/L] | [Strategy] |

**Scoring:**
- 0-2: Multiple high-probability, high-impact threats with no mitigation
- 3-4: 2-3 moderate threats, partial mitigations
- 5-6: Threats exist but all have viable mitigation strategies
- 7-8: Low-probability threats only, strong positioning against external forces
- 9-10: Business model inherently resistant to external threats

### 4. Blind Spot Detection (0-10)

**What to assess:** What is the founder NOT seeing?

**Common blind spots for indie developers:**

- **Customer support burden**: Underestimating support time at scale
- **Churn dynamics**: Acquiring customers ≠ keeping them
- **Content/community maintenance**: Ongoing effort often underestimated
- **Legal/compliance**: Privacy, terms of service, tax implications
- **Internationalization**: Different markets have different needs
- **Security**: Data breaches can kill small companies instantly
- **Burnout trajectory**: Sustainable pace vs sprint mentality

**Scoring:**
- 0-2: Multiple critical blind spots unacknowledged
- 3-4: Some blind spots identified but not addressed
- 5-6: Most blind spots identified with awareness plans
- 7-8: Thorough self-awareness, mitigation plans for known unknowns
- 9-10: Actively seeking disconfirming evidence, stress-testing assumptions

## Scoring Formula

```
Risk Profile = (Failure Scenarios × 30%) + (Dependencies × 25%) + (External Threats × 25%) + (Blind Spots × 20%)
```

## Output Format

```markdown
### Risk Analyst: Risk Profile Score

**Overall: X.X/10** (higher = lower risk)

| Dimension | Score | Weight | Weighted |
|-----------|-------|--------|----------|
| Failure Scenarios | X/10 | 30% | X.X |
| Dependencies | X/10 | 25% | X.X |
| External Threats | X/10 | 25% | X.X |
| Blind Spots | X/10 | 20% | X.X |

**Top 3 Kill Risks:**
1. 🔴 [Risk 1]: [Description] → Mitigation: [Strategy]
2. 🟠 [Risk 2]: [Description] → Mitigation: [Strategy]
3. 🟡 [Risk 3]: [Description] → Mitigation: [Strategy]

**Fatal Risk Present?** [Yes/No — if yes, this is a potential deal-breaker]

**Dependency Map:**
- Critical: [List]
- Important: [List]
- Replaceable: [List]

**Risk Verdict:** [One sentence summary]
```

## Common Pitfalls

- **Optimism bias**: Founders systematically underestimate risks
- **Survivorship bias**: Studying only successes hides how common failure is
- **Ignoring mundane risks**: Most startups die from boring problems (no customers, ran out of money)
- **Over-focusing on exotic risks**: "What if Google copies us?" matters less than "Can we get 10 paying users?"
- **Risk avoidance vs risk management**: Some risks are worth taking — the goal is informed decision-making
