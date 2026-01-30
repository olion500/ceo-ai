---
name: business-orchestrator
description: Orchestrate comprehensive business analysis by coordinating idea-validator and success-formula-analyzer agents. Use when you need complete business validation, end-to-end idea analysis, multi-agent coordination, integrated business assessment, or action plan creation. Provides workflow coordination, result synthesis, and actionable recommendations for indie developers and small teams.
---

# Business Orchestrator

## Purpose

Coordinate multiple business analysis agents to provide comprehensive, evidence-based assessment and actionable roadmap for indie developers and small teams. Act as the central intelligence that synthesizes insights from specialized agents.

## Output Location

**Save all orchestrated reports to:** `research/reports/[idea-slug]-analysis-[yyyy-mm-dd].md`

- Naming: kebab-case idea slug + analysis + date
- Example: `research/reports/dev-time-tracker-analysis-2026-01-26.md`

## When to Use This Skill

Automatically activates when you mention complete business analysis, full validation, end-to-end assessment, multi-agent coordination, or comprehensive evaluation. See skill-rules.json for complete trigger list.

## Multi-Agent Network

```
┌──────────────────────────────────────┐
│     Business Orchestrator            │
│  (Coordination & Synthesis)          │
└──────────────────────────────────────┘
           │
           │ (1) Optional: Elaborate rough idea first
           ▼
┌─────────────────┐
│ Idea Elaborator │ ← If idea is rough/vague
│ • Core features │
│ • Target cust.  │
│ • Business model│
│ • MVP scope     │
└─────────────────┘
           │
           │ (2) Parallel analysis (as subagents)
           ├─────────────────────────────┐
           │                             │
           ▼                             ▼
┌─────────────────────────┐ ┌─────────────────────────┐
│ Idea Validator          │ │ Success Formula         │
│ (6 frameworks)          │ │ Analyzer                │
│                         │ │                         │
│ • Market Opportunity    │ │ • Success patterns      │
│ • Execution Feasibility │ │ • Revenue models        │
│ • Strategic Position    │ │ • Reproducible tactics  │
│ • Risk Profile          │ │ • Category insights     │
│ • Intellectual Honesty  │ │                         │
│ • Investment Worthiness │ │                         │
│ → Composite + Verdict   │ │                         │
└─────────────────────────┘ └─────────────────────────┘
```

## CRITICAL: Subagent Execution Pattern

**Each agent MUST run as a Task tool subagent** to preserve the orchestrator's context window. Never run agent logic inline in the main conversation.

### How to Execute Each Agent

Use the `Task` tool with `subagent_type: "general-purpose"` for each agent. Each subagent receives the full skill content and user's idea, executes independently, and returns only the result summary.

**Parallel execution (2 agents at once):**
```
Send a SINGLE message with 2 Task tool calls:

Task 1: subagent_type="general-purpose"
  prompt: "You are the idea-validator agent. Read the skill at
  .claude/skills/idea-validator/SKILL.md and run Comprehensive validation
  (all 6 frameworks) for this idea: [IDEA].
  User context: [CONTEXT].
  Return the complete validation report with composite score and verdict."

Task 2: subagent_type="general-purpose"
  prompt: "You are the success-formula-analyzer agent. Read the skill at
  .claude/skills/success-formula-analyzer/SKILL.md and analyze success patterns
  relevant to this idea: [IDEA]. Return pattern matches and insights."
```

**Sequential pre-step (idea elaboration):**
```
If the idea is rough/vague, first run:

Task 0: subagent_type="general-purpose"
  prompt: "You are the idea-elaborator agent. Read the skill at
  .claude/skills/idea-elaborator/SKILL.md and flesh out this rough idea
  into a detailed product concept: [IDEA]. Save result to research/ideas/.
  Return the elaborated concept."

Then use the elaborated output as input for the 2 parallel agents above.
```

**Why subagents:**
- Each agent gets its own context window (no overflow)
- Parallel agents run concurrently (faster)
- Orchestrator context stays clean for synthesis
- Only summaries return to main conversation

## Three Core Workflows

### Workflow 1: Idea Validation (Most Common)

**Use Case:** "I have a business idea, is it worth building?"

**Process:**
1. **(Optional) Idea Elaborator** - If idea is rough, flesh it out first (sequential, Task subagent)
2. **Idea Validator** - 6-framework analysis with composite score and verdict (parallel, Task subagent)
3. **Success Formula Analyzer** - Find similar successful cases (parallel, Task subagent)
4. **Synthesis** - Integrated assessment and action plan (orchestrator, inline)

**Decision Points:**
- If idea is vague (no features/target/model defined): Run idea-elaborator first
- If Validator composite >= 7.0: GO — generate action plan
- If Validator composite 5.5-6.9: TEST MORE — identify experiments
- If Validator composite < 5.5: PIVOT or NO-GO

**Detailed Guide:** [Idea Validation Workflow](./resources/workflows/idea-validation.md)

### Workflow 2: Learning from Success

**Use Case:** "Analyze how [Product X] succeeded and apply to my idea"

**Process:**
1. **Success Formula Analyzer** - Deep dive into successful product
2. **Idea Validator** - Score your idea against discovered patterns
3. **Synthesis** - Adaptation plan

**Detailed Guide:** [Success Learning Workflow](./resources/workflows/success-learning.md)

### Workflow 3: Competitive Positioning

**Use Case:** "Help me position against existing competitors"

**Process:**
1. **Idea Validator** - Full analysis including strategic positioning
2. **Success Formula Analyzer** - How late entrants won
3. **Synthesis** - Positioning strategy

**Detailed Guide:** [Competitive Positioning Workflow](./resources/workflows/competitive-positioning.md)

## Orchestration Approach

### Execution Strategy

**All agents run as Task tool subagents.** The orchestrator (main conversation) only handles:
- Gathering user input
- Deciding which agents to run
- Synthesizing returned results
- Presenting final recommendation

**Default: Parallel with Optional Pre-step**
```
[User provides idea]
    ↓
Is idea rough/vague? (no features, no target, no model)
    ├── YES → Run idea-elaborator subagent first (sequential)
    │         Then use elaborated output below
    └── NO  → Skip to parallel step
    ↓
Run 2 subagents IN PARALLEL (single message, 2 Task calls):
    ├── idea-validator subagent (6 frameworks, composite score)
    └── success-formula-analyzer subagent
    ↓
[Both results return to orchestrator]
    ↓
Synthesize inline (orchestrator context)
    ↓
Present final report + recommendation
```

### Iterative Refinement Pattern

```
1. Run all agents once (parallel subagents)
2. Identify weakest dimension(s) from validator results
3. Brainstorm specific improvements (inline)
4. Re-run idea-validator subagent with refined idea
5. Compare before/after scores
6. Iterate until score stabilizes or improves
```

## Synthesis Framework

### Integrated Scoring

```
Final Score = (Validator Composite × 60%) +
              (Success Pattern Match × 40%)

Where:
- Validator Composite: 0-10 from idea-validator (weighted average of 6 frameworks)
- Success Pattern Match: 0-10 (based on similar cases found by success-formula-analyzer)
```

### Interpretation

- **8.0-10.0:** Exceptional opportunity, proceed with confidence
- **6.5-7.9:** Strong potential, manageable risks
- **5.0-6.4:** Moderate potential, needs improvements
- **3.0-4.9:** High risk, major concerns
- **0.0-2.9:** Not recommended, pivot advised

**Detailed Framework:** [Synthesis Framework](./resources/synthesis-framework.md)

## Decision Framework

### Proceed If (All must be true):
- Final score > 6.5/10
- Validator composite >= 7.0 (GO verdict)
- No critical unmitigatable risks
- Success patterns identified
- Clear differentiation exists
- Monetization path validated

### Iterate If:
- Final score 5-6.5/10
- Validator verdict is TEST MORE
- Some risks with mitigation paths
- One framework scoring < 4.0
- Can improve by de-scoping or pivoting specific dimension

### Pivot/Abandon If:
- Final score < 5/10
- Validator verdict is PIVOT or NO-GO
- Critical risks, no mitigation
- No similar success patterns
- Unclear monetization

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

### Step 2: Run Agents (as Subagents)

**IMPORTANT: Use Task tool with subagent_type="general-purpose" for each agent.**

**Option A: Parallel (Recommended)**

Send a single message with 2 Task tool calls. Each subagent:
- Reads the corresponding skill SKILL.md
- Receives the user's idea + context as prompt
- Executes the full skill workflow independently
- Returns the complete analysis result

```
# Single message with 2 parallel Task calls:
Task(description="Validate business idea",
     subagent_type="general-purpose",
     prompt="Read .claude/skills/idea-validator/SKILL.md.
             Run Comprehensive validation (all 6 frameworks) for: [IDEA].
             Context: [USER_CONTEXT].
             Return full validation report with composite score and verdict.")

Task(description="Analyze success patterns",
     subagent_type="general-purpose",
     prompt="Read .claude/skills/success-formula-analyzer/SKILL.md.
             Find success patterns for: [IDEA].
             Search web for similar successful products.
             Return pattern analysis with matches and a pattern match score (0-10).")
```

**Option B: Sequential with Early Exit**
```
1. Task → idea-validator (Quick Check) → Get preliminary score
   └─ If < 4.0, recommend pivot (skip remaining agents)
2. Task → success-formula-analyzer → Find patterns
3. If promising, re-run idea-validator (Comprehensive) for full analysis
```

### Step 3: Synthesize Results

**Cross-Agent Analysis:**
- What do both agents agree on?
- Where do agents diverge?
- What surprising insights emerged?
- What are consensus risks?
- What are consensus opportunities?
- How do success patterns validate or contradict the validator's score?

### Step 4: Generate Action Plan

Based on final recommendation:
- **If GO:** 4-phase action plan (Pre-dev → MVP → Beta → Launch)
- **If TEST MORE:** Validation experiments with timelines
- **If PIVOT:** Pivot options with Quick Check scores
- **If NO-GO:** Alternative options or learnings to carry forward

**Template:** [Comprehensive Report Template](./resources/templates/comprehensive-report.md)

## Quick Reference

### When to Use Each Agent Individually

**Use idea-validator when:**
- Evaluating a single idea comprehensively
- Quick-checking multiple ideas (Quick Check mode)
- Assessing feasibility and market opportunity together
- Need structured multi-framework scoring

**Use success-formula-analyzer when:**
- Found inspiring successful product
- Need validation of approach
- Want reproducible tactics
- Looking for proven patterns

**Use business-orchestrator when:**
- Need complete validation with success pattern matching
- Making significant commitment (time/money)
- Want comprehensive assessment with action plan
- Need synthesized view across all dimensions

### Integration with Other Skills

**Before orchestration:**
- Use `idea-finder` if you don't have ideas yet
- Use `idea-elaborator` if idea is rough/vague (orchestrator does this automatically)
- Use `success-story-researcher` to find more examples

**After orchestration:**
- If GO: Start building with generated action plan
- If TEST MORE: Run validation experiments, then re-run orchestrator
- If PIVOT: Use `idea-finder` for alternatives
- If NO-GO: Archive learnings, try `idea-finder`

### Full Pipeline

```
idea-finder (discover rough ideas)
    ↓
idea-elaborator (flesh out into concrete concept)  ← auto-triggered if idea is vague
    ↓
┌─────────────────────────────────────────┐
│ business-orchestrator (this skill)      │
│   ├── idea-validator (6 frameworks)     │  ← parallel subagents
│   └── success-formula-analyzer (match)  │
│   ↓                                     │
│   Synthesis + Recommendation            │
└─────────────────────────────────────────┘
    ↓
GO / TEST MORE / PIVOT / NO-GO + Action Plan
```

## Master Orchestration Prompt

When user requests full business analysis:

```
I'll run comprehensive business analysis using our multi-agent system.

**Step 1: Input** — Gather your idea and context
**Step 2: Elaborate** — If your idea is rough, I'll flesh it out first (subagent)
**Step 3: Analyze** — Launch 2 specialized agents IN PARALLEL as subagents:
  - Idea Validator (6-framework scoring: market, execution, strategy, risk, honesty, investment)
  - Success Formula Analyzer (find similar successes and patterns)
**Step 4: Synthesize** — Integrate all results into final assessment
**Step 5: Recommend** — GO / TEST MORE / PIVOT / NO-GO + action plan

Each agent runs as an independent subagent (Task tool) so analysis is
thorough without overwhelming context.

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
- Validator Composite: 60%
- Success Patterns: 40%

**Customize based on priorities:**
- Novel idea (no comparable successes): Increase validator weight (70-80%)
- Pattern-heavy analysis: Increase success patterns weight (50-60%)
- First-time founder: Equal weight (50/50) — both validation and patterns matter

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
