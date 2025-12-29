---
name: idea-finder
description: Find new business ideas by applying proven success patterns from analyzed indie developer stories. Uses "scratch your own itch" methodology, data-driven selection, and market gap analysis to generate validated business opportunities.
---

# Idea Finder

## Purpose

Generate new business ideas by applying proven success patterns from 24+ analyzed indie developer success stories. Use reproducible methodologies rather than random brainstorming.

## When to Use This Skill

Automatically activates when you mention finding/generating business ideas, looking for startup opportunities, asking what to build next, or exploring market opportunities. See skill-rules.json for complete trigger list.

## Three Proven Methods

### Method 1: Scratch Your Own Itch (79% Success Rate)

**How It Works:**
1. Identify personal pain points in your work/life
2. Validate others face the same problem
3. Build solution you wish existed

**Success Examples:**
- TypingMind: Tony frustrated with ChatGPT UI → $83K MRR
- ShipFast: Marc Lou tired of rebuilding same stack → $50K MRR
- Bank Statement Converter: Angus manually converting PDFs → $16K MRR

**Detailed Guide:** [Scratch Your Own Itch Method](./resources/methods/scratch-your-own-itch.md)

### Method 2: Data-Driven Selection (60% Success Rate)

**How It Works:**
1. Analyze market data (app stores, trends, competitors)
2. Create ranking algorithm (demand × achievability)
3. Choose proven market with underserved niche

**Success Examples:**
- Online Solitaire: Holger scraped App Annie data → $10K MRR

**Detailed Guide:** [Data-Driven Selection Method](./resources/methods/data-driven-selection.md)

### Method 3: Observe Market Gaps (50% Success Rate)

**How It Works:**
1. Find successful products with obvious flaws
2. Build improved version
3. Capture frustrated users

**Success Examples:**
- Vampire Survivors: Luca improved Magic Survival → £40M net worth

**Detailed Guide:** [Market Gap Analysis Method](./resources/methods/market-gap-analysis.md)

## Quick Idea Generation Workflow

### Step 1: Context Gathering (2 minutes)

Understand user's constraints:
- **Skills:** What can you build?
- **Experience:** What domains do you know?
- **Time:** Solo/team? Full-time/side project?
- **Capital:** Bootstrapped or funded?
- **Goals:** Quick validation or long-term?

### Step 2: Method Selection (1 minute)

**Choose method based on context:**
- **Beginner entrepreneur?** → Method 1 (Scratch Your Own Itch)
- **Data/research oriented?** → Method 2 (Data-Driven Selection)
- **Found inspiring product?** → Method 3 (Market Gap Analysis)

### Step 3: Generate Ideas (10-15 minutes)

**Follow selected method:**
- Use method-specific prompts and frameworks
- Generate 5-10 idea candidates
- Document each with problem/solution/target

**Template:** [Idea Generation Template](./resources/templates/idea-generation.md)

### Step 4: Quick Validation (5 minutes per idea)

For each promising idea:
- [ ] Search for 3+ competitors (good sign if found!)
- [ ] Check if people pay for solutions
- [ ] Identify clear market gap
- [ ] Assess personal fit (skills/excitement)

**Keep ideas scoring 7+/10 on quick validation.**

### Step 5: Deep Evaluation (Next step)

For top 2-3 ideas:
- Use `business-idea-evaluator` for detailed scoring
- Use `feasibility-checker` for execution validation
- Use `business-orchestrator` for comprehensive analysis

## Evaluation Criteria

### What Makes a Good Indie Developer Idea?

**Green Flags (Look for these):**
- ✅ Daily/weekly pain point (high frequency)
- ✅ You personally experienced it
- ✅ 3-10 competitors exist (market validation!)
- ✅ People currently pay for solutions
- ✅ Can build MVP in <3 months
- ✅ Solo/small team suitable
- ✅ Skills match >70%
- ✅ Clear monetization path
- ✅ Niche focus (specific audience)
- ✅ Personal excitement high

**Red Flags (Avoid these):**
- ❌ Hypothetical problem (not real pain)
- ❌ No competitors found (usually bad sign!)
- ❌ Requires massive resources
- ❌ Large team needed
- ❌ Unclear monetization
- ❌ Too broad target market
- ❌ Skills gap >50%
- ❌ MVP timeline >6 months
- ❌ "Pivot to X later" thinking
- ❌ No personal conviction

## Success Pattern Repository

**Key Insights from 24+ Success Stories:**

### Idea Discovery Patterns (Ranked by Success Rate)

1. **Solve Own Problem** (79%) - Highest success rate
2. **Data-Driven Market Selection** (60%)
3. **Improve Existing Product** (50%)
4. **Ride Platform Wave** (40%)
5. **Service to Product Transition** (35%)

### Common Starting Points

**Most successful indie developers started by:**
- Building tools they needed (45%)
- Improving products they used (25%)
- Analyzing market data (15%)
- Productizing consulting (10%)
- Community-driven ideas (5%)

### What Didn't Work

**Low success approaches:**
- ❌ "Building what's trending" without personal connection
- ❌ "Startup idea generators" (random brainstorming)
- ❌ Copying successful products exactly
- ❌ Building for "everyone"
- ❌ Solutions looking for problems

## Quick Reference

### Choosing the Right Method

**Use Scratch Your Own Itch if:**
- You're a beginner entrepreneur
- You have clear pain points in your work
- You want highest success probability
- You value authentic positioning
- You have a specific domain expertise

**Use Data-Driven Selection if:**
- You're analytical/research-oriented
- You don't have obvious pain points
- You're willing to enter proven markets
- You can analyze competitor data
- You're comfortable with competition

**Use Market Gap Analysis if:**
- You found an inspiring but flawed product
- You can build it significantly better
- You have relevant expertise
- Market is growing
- Existing solutions have clear weaknesses

### Common Mistakes to Avoid

**Mistake 1: "No Competitors = Good"**
- Reality: Usually means no market demand
- Fix: Look for 3-10 competitors as validation
- Exception: Only if you have strong customer validation

**Mistake 2: Building for Yourself Only**
- Reality: Market of one isn't viable
- Fix: Validate 10+ others have same pain
- Check: Would they pay for solution?

**Mistake 3: Too Broad Market**
- Reality: "Everyone" is no one
- Fix: Start with specific niche
- Example: Not "productivity app", but "time tracking for freelance designers"

**Mistake 4: Solution-First Thinking**
- Reality: "Cool tech" ≠ business idea
- Fix: Start with problem validation
- Check: Do people actively seek solutions?

**Mistake 5: Ignoring Monetization**
- Reality: Users ≠ customers
- Fix: Research pricing early
- Validate: Willingness to pay confirmed?

## Integration with Other Skills

### Before Idea Finder:
- Use `success-story-researcher` to study more examples
- Read `research/patterns/` for additional patterns

### After Idea Finder:
1. **Generated 1-3 promising ideas:**
   - Use `business-idea-evaluator` to score each
   - Compare scores to pick best one

2. **Selected best idea:**
   - Use `feasibility-checker` for execution validation
   - If feasible >6.5/10, proceed

3. **Ready to commit:**
   - Use `business-orchestrator` for comprehensive analysis
   - Generate 4-phase action plan

### Decision Flow

```
idea-finder (generate options)
    ↓
business-idea-evaluator (score & compare)
    ↓
Pick highest scoring idea
    ↓
feasibility-checker (can you build it?)
    ↓
If feasible >6.5/10:
    business-orchestrator (comprehensive plan)
Else:
    Return to idea-finder (try different idea)
```

## Master Prompt

When generating ideas for user:

```
I'll help you find business ideas using proven success patterns:

**Step 1: Understanding Your Context**
- What skills do you have? (technical/domain)
- How much time can you dedicate? (hours/week)
- Are you solo or with a team?
- What's your goal? (quick validation vs long-term)

**Step 2: Method Selection**
Based on your answers, I'll recommend:
- Method 1: Scratch Your Own Itch (highest success rate)
- Method 2: Data-Driven Selection (analytical approach)
- Method 3: Market Gap Analysis (improve existing)

**Step 3: Idea Generation**
- Generate 5-10 idea candidates
- Quick validation for each
- Rank by success probability

**Step 4: Next Steps**
- Detailed evaluation of top 2-3 ideas
- Feasibility check
- Action plan if proceeding

Let's start! What skills and experience do you have?
```

## Resources & Templates

### Method Guides
- [Scratch Your Own Itch](./resources/methods/scratch-your-own-itch.md) - Detailed 79% success method
- [Data-Driven Selection](./resources/methods/data-driven-selection.md) - Analytical approach
- [Market Gap Analysis](./resources/methods/market-gap-analysis.md) - Improve existing products

### Templates
- [Idea Generation Template](./resources/templates/idea-generation.md) - Structured idea documentation
- [Quick Validation Checklist](./resources/templates/quick-validation.md) - Fast idea screening

### Success Patterns
- See `research/patterns/idea-discovery/` for extracted patterns
- See `research/stories/` for full founder stories

---

**Best Practice:** Start with Method 1 (Scratch Your Own Itch) - highest success rate and authentic positioning. Only use other methods if you don't have clear pain points.
