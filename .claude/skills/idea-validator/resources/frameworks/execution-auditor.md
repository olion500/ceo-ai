# Execution Auditor Framework

## Core Question

**내가 실제로 만들 수 있는가?** (Can I actually build this?)

## Score: Execution Feasibility (0-10)

This framework validates whether the founder/team has the skills, resources, time, and runway to execute.

## Evaluation Dimensions

### 1. Skills Match (0-10)

**What to assess:** How well do existing skills cover what's needed?

| Score | Match Level | Criteria |
|-------|------------|---------|
| 0-2 | Critical gap | >70% of required skills missing, need multiple new domains |
| 3-4 | Major gap | 50-70% skills gap, 1-2 new domains to learn |
| 5-6 | Moderate gap | 30-50% gap, learning needed but within comfort zone |
| 7-8 | Strong match | 10-30% gap, minor learning needed |
| 9-10 | Perfect match | <10% gap, can start building immediately |

**Skills audit template:**

```
Required Skills      | Have? | Level (1-5) | Learning Time
--------------------|-------|-------------|-------------
[Skill 1]           | Y/N   | X           | X weeks
[Skill 2]           | Y/N   | X           | X weeks
[Skill 3]           | Y/N   | X           | X weeks
```

### 2. Cost & Runway (0-10)

**What to assess:** Financial sustainability through to revenue.

| Score | Financial Level | Criteria |
|-------|----------------|---------|
| 0-2 | Unsustainable | >$500/mo costs, <2 months runway, no revenue path |
| 3-4 | Tight | $200-500/mo costs, 2-4 months runway |
| 5-6 | Manageable | $50-200/mo costs, 4-8 months runway |
| 7-8 | Comfortable | <$50/mo costs, 8-12 months runway |
| 9-10 | Ideal | Can start free, 12+ months runway, quick path to revenue |

**Cost breakdown template:**

```
Category            | Initial  | Monthly  | Notes
--------------------|----------|----------|------
Infrastructure      | $X       | $X       | [Provider details]
Domain/SSL          | $X       | $X       |
3rd-party APIs      | $X       | $X       | [Free tier limits]
Tools/SaaS          | $X       | $X       |
Marketing           | $X       | $X       |
TOTAL               | $X       | $X/mo    |
```

**Runway calculation:**
```
Personal savings / (Monthly burn + Living expenses) = Runway months
Required: Runway > (MVP timeline × 2) + 3 months buffer
```

### 3. Timeline Realism (0-10)

**What to assess:** Can a viable product be built in reasonable time?

| Score | Timeline Level | Criteria |
|-------|---------------|---------|
| 0-2 | Unrealistic | >12 months to anything usable, scope too large |
| 3-4 | Stretched | 6-12 months to MVP, complex dependencies |
| 5-6 | Moderate | 3-6 months to MVP, some complexity |
| 7-8 | Realistic | 1-3 months to MVP, well-scoped |
| 9-10 | Fast | <1 month to MVP, proven tech stack, clear scope |

**Timeline validation rules:**
- Add 2-3x buffer to initial estimate (optimism bias correction)
- Account for learning time in new technologies
- Factor in part-time vs full-time availability
- Include non-coding work: design, marketing, support

### 4. Technical Complexity (0-10, inverted: lower complexity = higher score)

**What to assess:** How complex is the technical build?

| Score | Complexity | Criteria |
|-------|-----------|---------|
| 0-2 | Extreme | Requires novel algorithms, distributed systems, real-time at scale |
| 3-4 | High | Multiple integrations, complex data models, custom infrastructure |
| 5-6 | Moderate | Standard web app with some complexity, known patterns |
| 7-8 | Low | Simple CRUD, API wrapper, standard patterns |
| 9-10 | Minimal | Static site, simple tool, no-code possible |

**Complexity multipliers:**
- Each external API integration: +1 complexity
- Real-time features: +2 complexity
- Multi-tenant architecture: +2 complexity
- Payment processing: +1 complexity
- User-generated content moderation: +2 complexity
- Mobile app requirement: +3 complexity

### 5. Dependency Risk (0-10, fewer dependencies = higher score)

**What to assess:** How many external factors could block progress?

| Score | Risk Level | Criteria |
|-------|-----------|---------|
| 0-2 | High dependency | Requires platform approval, regulatory compliance, partnerships |
| 3-4 | Moderate dependency | Depends on 3+ external APIs, needs specific integrations |
| 5-6 | Some dependency | 1-2 key external dependencies, manageable |
| 7-8 | Low dependency | Mostly self-contained, replaceable dependencies |
| 9-10 | Independent | Fully self-contained, no external blockers |

## Scoring Formula

```
Execution Feasibility = (Skills × 25%) + (Cost/Runway × 20%) + (Timeline × 20%) + (Complexity × 20%) + (Dependencies × 15%)
```

## Output Format

```markdown
### Execution Auditor: Feasibility Score

**Overall: X.X/10**

| Dimension | Score | Weight | Weighted |
|-----------|-------|--------|----------|
| Skills Match | X/10 | 25% | X.X |
| Cost & Runway | X/10 | 20% | X.X |
| Timeline Realism | X/10 | 20% | X.X |
| Technical Complexity | X/10 | 20% | X.X |
| Dependency Risk | X/10 | 15% | X.X |

**Skills Gap Analysis:**
- [Skill gap 1]: [Impact and mitigation]
- [Skill gap 2]: [Impact and mitigation]

**Cost Projection:**
- Initial: $[X] | Monthly: $[X]/mo | Break-even: [X] months

**Timeline Estimate:**
- MVP: [X] months | First Revenue: [X] months

**Critical Blockers:**
- [Blocker 1 or "None identified"]

**Execution Verdict:** [One sentence summary]
```

## Common Pitfalls

- **Optimism bias**: Multiply your time estimate by 2-3x for reality
- **Hidden costs**: Free tiers expire, APIs have rate limits, infrastructure scales up
- **Skill gap denial**: "I'll learn it quickly" rarely works under time pressure
- **Scope creep tolerance**: Build the smallest thing that delivers value first
- **Solo founder burnout**: Factor in sustainable pace, not sprint speed
