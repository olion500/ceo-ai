# Decision Framework

## Purpose

Translate composite scores and framework analysis into clear GO / TEST MORE / PIVOT / NO-GO decisions with specific action items.

## Decision Matrix

| Decision | Score Range | Additional Conditions |
|----------|-----------|----------------------|
| **GO** | >= 7.0 | AND all frameworks >= 4.0, no fatal risks |
| **TEST MORE** | 5.5 - 6.9 | OR some frameworks < 4.0 but composite >= 5.5 |
| **PIVOT** | 4.0 - 5.4 | Fundamental changes needed to core approach |
| **NO-GO** | < 4.0 | OR 2+ frameworks < 3.0 regardless of composite |

## Decision Details

### GO (>= 7.0)

**Meaning:** Strong opportunity with manageable risks. Proceed to execution.

**Required conditions (ALL must be true):**
- Composite score >= 7.0
- No individual framework < 4.0
- No fatal/existential risk identified
- Clear path to first paying customer
- Founder commitment confirmed

**Action plan:**
1. Define MVP scope (max 3-5 core features)
2. Set 90-day execution plan with weekly milestones
3. Establish kill criteria (what would make you stop)
4. Begin building immediately
5. Plan first customer outreach in parallel with development

**Monitoring cadence:** Weekly check-ins against milestones

### TEST MORE (5.5 - 6.9)

**Meaning:** Promising but unvalidated. Need more evidence before committing.

**Typical triggers:**
- Good composite but 1-2 frameworks are weak
- Strong idea but unvalidated assumptions
- Market opportunity exists but execution path unclear
- Good execution fit but market demand uncertain

**Action plan:**
1. Identify top 3 unvalidated assumptions
2. Design cheapest experiment to test each:
   - Landing page test (market demand)
   - Prototype/mockup user tests (solution fit)
   - Pre-sale attempt (willingness to pay)
   - Competitor customer interviews (switching intent)
3. Set validation timeline (2-4 weeks max)
4. Define success criteria for each test
5. Re-evaluate after tests complete

**Monitoring cadence:** Bi-weekly validation sprints

### PIVOT (4.0 - 5.4)

**Meaning:** Core concept has issues but elements may be salvageable.

**Typical triggers:**
- Market exists but approach is wrong
- Good skills match but wrong problem
- Right problem but wrong customer segment
- Execution feasible but market too small

**Action plan:**
1. Identify what IS working (which frameworks scored well)
2. Identify what MUST change (which frameworks scored poorly)
3. Generate 3 pivot options:
   - **Customer pivot:** Same solution, different audience
   - **Problem pivot:** Same audience, different problem
   - **Solution pivot:** Same problem, different approach
   - **Channel pivot:** Same product, different distribution
   - **Revenue model pivot:** Same product, different monetization
4. Score top pivot option through Quick Check (3 frameworks)
5. If pivot scores > 6.0, proceed to TEST MORE phase

**Monitoring cadence:** One-time pivot analysis, then restart cycle

### NO-GO (< 4.0)

**Meaning:** Fundamental issues that cannot be addressed. Move on.

**Typical triggers:**
- No real market demand
- Multiple framework scores < 3.0
- Fatal risk with no mitigation
- Unit economics fundamentally broken
- Critical skills gap with no learning path

**Action plan:**
1. Document key learnings (what did you discover?)
2. Archive idea with notes for future reference
3. Identify transferable assets:
   - Market research that applies elsewhere
   - Technical skills gained
   - Customer relationships built
   - Content/brand assets created
4. Use idea-finder to explore alternatives
5. Apply learnings to next idea evaluation

**Monitoring cadence:** N/A — move on

## Confidence Levels

Each decision comes with a confidence level based on evidence quality:

| Confidence | Evidence Quality | Recommendation |
|-----------|-----------------|---------------|
| **High** | Multiple data points, validated assumptions, market evidence | Trust the decision |
| **Medium** | Some data, partially validated, reasonable assumptions | Proceed with monitoring |
| **Low** | Limited data, many assumptions, theoretical analysis | Gather more evidence first |

## Edge Cases

### High Score but Low Confidence
- Score says GO but evidence is thin
- **Action:** Treat as TEST MORE until confidence improves

### Low Score but Strong Conviction
- Score says NO-GO but founder has deep domain expertise
- **Action:** Identify which frameworks are wrong and why. If domain expertise genuinely invalidates the scoring, adjust. But be honest about cognitive bias.

### Mixed Signals
- Some frameworks say GO, others say NO-GO
- **Action:** Focus on the disagreement. The truth usually lies in understanding WHY frameworks disagree, not in averaging them.

## Output Template

```markdown
## Decision

### Verdict: [GO / TEST MORE / PIVOT / NO-GO]

**Composite Score:** X.X/10
**Confidence:** [High / Medium / Low]
**Override Conditions:** [None / Details]

### Rationale
[2-3 sentences explaining the decision based on framework results]

### Key Strengths to Leverage
1. [Strength from highest-scoring framework]
2. [Strength from second-highest framework]

### Critical Issues to Address
1. [Issue from lowest-scoring framework]
2. [Second critical issue]

### Immediate Next Steps (Next 2 Weeks)
1. [Action 1]
2. [Action 2]
3. [Action 3]

### Kill Criteria
If ANY of these prove true, reconsider the decision:
- [Criterion 1]
- [Criterion 2]
- [Criterion 3]
```
