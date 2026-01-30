---
name: idea-validator
description: Multi-framework business idea validation combining market analysis, execution feasibility, strategic positioning, risk assessment, intellectual honesty testing, and investment worthiness evaluation. Runs 6 specialized analysis frameworks in parallel to produce a composite score and GO/TEST MORE/PIVOT/NO-GO decision. Works standalone or as orchestrator sub-agent. Replaces business-idea-evaluator and feasibility-checker with unified, deeper analysis.
---

# Idea Validator

## Purpose

Validate business ideas through 6 specialized analysis frameworks running in parallel. Each framework evaluates the idea from a distinct perspective, producing individual scores that synthesize into a composite score with a clear decision recommendation.

**Replaces:** `business-idea-evaluator` + `feasibility-checker` (unified into one multi-framework analysis)

## Output Location

**Save all validation reports to:** `research/evaluations/[idea-slug]-validation-[yyyy-mm-dd].md`

- Naming: kebab-case idea slug + validation + date
- Example: `research/evaluations/dev-time-tracker-validation-2026-01-28.md`

## When to Use This Skill

Automatically activates when you mention evaluating, scoring, validating, assessing business ideas, checking feasibility, or analyzing business viability. See skill-rules.json for complete trigger list.

**Standalone:** Run directly when user wants idea evaluation or feasibility check.
**Sub-agent:** Called by `business-orchestrator` as part of comprehensive analysis.

## Execution Modes

### Quick Check (3 Frameworks)

**Use when:** Initial screening, quick go/no-go, comparing multiple ideas.

Runs 3 frameworks in parallel:
1. **Startup Validator** — Market Opportunity
2. **Execution Auditor** — Execution Feasibility
3. **Risk Analyst** — Risk Profile

```
Quick Composite = (Market Opportunity × 35%) + (Execution Feasibility × 35%) + (Risk Profile × 30%)
```

**Template:** [Quick Check Report](./resources/templates/quick-check.md)

### Comprehensive (6 Frameworks)

**Use when:** Serious commitment decision, full validation before building.

Runs all 6 frameworks in parallel:
1. **Startup Validator** — Market Opportunity (0-10)
2. **Execution Auditor** — Execution Feasibility (0-10)
3. **Strategic Advisor** — Strategic Position (0-10)
4. **Risk Analyst** — Risk Profile (0-10)
5. **Devil's Advocate** — Intellectual Honesty (0-10)
6. **Investor Lens** — Investment Worthiness (0-10)

```
Composite = (Market Opportunity × 20%) + (Execution Feasibility × 20%) +
            (Strategic Position × 15%) + (Risk Profile × 15%) +
            (Intellectual Honesty × 10%) + (Investment Worthiness × 20%)
```

**Template:** [Comprehensive Report](./resources/templates/comprehensive-report.md)

## The 6 Analysis Frameworks

Each framework asks a core question and evaluates distinct dimensions:

| # | Framework | Core Question | Score Name | Unique Domain |
|---|-----------|--------------|-----------|---------------|
| 1 | Startup Validator | Is there a real business? | Market Opportunity | Demand, market size, pricing, timing |
| 2 | Execution Auditor | Can I actually build this? | Execution Feasibility | Skills, costs, timeline, complexity, dependencies |
| 3 | Strategic Advisor | What position wins? | Strategic Position | Moats, differentiation, mental models, long-term |
| 4 | Risk Analyst | What will kill this? | Risk Profile | Failure scenarios, dependencies, threats, blind spots |
| 5 | Devil's Advocate | What am I getting wrong? | Intellectual Honesty | Assumptions, biases, counter-arguments |
| 6 | Investor Lens | Would smart money invest? | Investment Worthiness | Unit economics, ROI, scalability, revenue quality |

**Detailed framework guides:**
- [Startup Validator](./resources/frameworks/startup-validator.md)
- [Execution Auditor](./resources/frameworks/execution-auditor.md)
- [Strategic Advisor](./resources/frameworks/strategic-advisor.md)
- [Risk Analyst](./resources/frameworks/risk-analyst.md)
- [Devil's Advocate](./resources/frameworks/devils-advocate.md)
- [Investor Lens](./resources/frameworks/investor-lens.md)

## Decision Matrix

| Decision | Score Range | Additional Conditions |
|----------|-----------|----------------------|
| **GO** | >= 7.0 | AND all frameworks >= 4.0, no fatal risks |
| **TEST MORE** | 5.5 - 6.9 | OR some frameworks < 4.0 but composite >= 5.5 |
| **PIVOT** | 4.0 - 5.4 | Fundamental changes needed |
| **NO-GO** | < 4.0 | OR 2+ frameworks < 3.0 regardless of composite |

**Override rules:**
- Any single framework < 3.0 → Composite capped at 5.9 (cannot be GO)
- Two frameworks < 4.0 → Composite capped at 4.9 (force PIVOT or NO-GO)
- Fatal risk identified → Composite capped at 5.4

**Detailed decision guide:** [Decision Framework](./resources/decision-framework.md)

## CRITICAL: Parallel Execution Pattern

**Each framework MUST run as a Task tool sub-agent** to preserve context and enable parallel execution.

### How to Execute Frameworks

Use `Task` tool with `subagent_type: "general-purpose"` for each framework. All frameworks in a mode run in a single message as parallel Task calls.

### Quick Check Execution (3 parallel tasks)

```
Send a SINGLE message with 3 Task tool calls:

Task 1: description="Validate market opportunity"
  subagent_type="general-purpose"
  prompt="You are the Startup Validator framework for idea validation.

  Read the framework guide at:
  .claude/skills/idea-validator/resources/frameworks/startup-validator.md

  Evaluate this idea: [IDEA]
  User context: [CONTEXT]

  Score all 4 dimensions (Demand Signal, Market Size, Pricing Power, Timing)
  on 0-10 scale with evidence and reasoning.
  Calculate weighted Market Opportunity score.
  Return the complete analysis in the output format specified in the guide."

Task 2: description="Audit execution feasibility"
  subagent_type="general-purpose"
  prompt="You are the Execution Auditor framework for idea validation.

  Read the framework guide at:
  .claude/skills/idea-validator/resources/frameworks/execution-auditor.md

  Evaluate this idea: [IDEA]
  User context: [CONTEXT]

  Score all 5 dimensions (Skills Match, Cost & Runway, Timeline Realism,
  Technical Complexity, Dependency Risk) on 0-10 scale.
  Calculate weighted Execution Feasibility score.
  Return the complete analysis in the output format specified in the guide."

Task 3: description="Analyze risk profile"
  subagent_type="general-purpose"
  prompt="You are the Risk Analyst framework for idea validation.

  Read the framework guide at:
  .claude/skills/idea-validator/resources/frameworks/risk-analyst.md

  Evaluate this idea: [IDEA]
  User context: [CONTEXT]

  Score all 4 dimensions (Failure Scenarios, Dependencies, External Threats,
  Blind Spots) on 0-10 scale.
  Identify top 3 kill risks with mitigations.
  Flag any fatal risks.
  Calculate weighted Risk Profile score.
  Return the complete analysis in the output format specified in the guide."
```

### Comprehensive Execution (6 parallel tasks)

```
Send a SINGLE message with 6 Task tool calls:

Tasks 1-3: Same as Quick Check above

Task 4: description="Assess strategic position"
  subagent_type="general-purpose"
  prompt="You are the Strategic Advisor framework for idea validation.

  Read the framework guide at:
  .claude/skills/idea-validator/resources/frameworks/strategic-advisor.md

  Evaluate this idea: [IDEA]
  User context: [CONTEXT]

  Score all 4 dimensions (Competitive Moat, Differentiation Clarity,
  Mental Model Fit, Long-term Position) on 0-10 scale.
  Identify primary moat type and differentiation archetype.
  Calculate weighted Strategic Position score.
  Return the complete analysis in the output format specified in the guide."

Task 5: description="Challenge assumptions"
  subagent_type="general-purpose"
  prompt="You are the Devil's Advocate framework for idea validation.

  Read the framework guide at:
  .claude/skills/idea-validator/resources/frameworks/devils-advocate.md

  Evaluate this idea: [IDEA]
  User context: [CONTEXT]

  Score all 3 dimensions (Assumption Audit, Cognitive Bias Detection,
  Counter-Argument Strength) on 0-10 scale.
  List unvalidated assumptions and detected biases.
  Provide strongest counter-arguments.
  Define kill criteria.
  Calculate weighted Intellectual Honesty score.
  Return the complete analysis in the output format specified in the guide."

Task 6: description="Evaluate investment worthiness"
  subagent_type="general-purpose"
  prompt="You are the Investor Lens framework for idea validation.

  Read the framework guide at:
  .claude/skills/idea-validator/resources/frameworks/investor-lens.md

  Evaluate this idea: [IDEA]
  User context: [CONTEXT]

  Score all 4 dimensions (Unit Economics, ROI Potential, Scalability,
  Revenue Quality) on 0-10 scale.
  Calculate key numbers (LTV:CAC, target MRR, gross margin, payback).
  Calculate weighted Investment Worthiness score.
  Return the complete analysis in the output format specified in the guide."
```

### Why Sub-agents

- Each framework gets its own context window (no overflow)
- All frameworks run concurrently (parallel = faster)
- Main conversation context stays clean for synthesis
- Only framework results return to the orchestrator

## Execution Workflow

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
```

If information is incomplete, ask for it before running frameworks. At minimum need: problem, solution, target audience.

### Step 2: Choose Mode

**Default selection logic:**
- If user says "quick check", "빠르게", "간단히" → Quick Check
- If user says "comprehensive", "전체", "완전히", "상세히" → Comprehensive
- If called as sub-agent by orchestrator → Comprehensive (default)
- If no preference stated → Ask user, recommend Comprehensive for serious ideas

### Step 3: Run Frameworks (Parallel)

Execute all frameworks for the chosen mode as parallel Task sub-agents in a single message.

### Step 4: Synthesize Results

After all framework results return:

1. **Collect scores** from each framework
2. **Calculate composite** using mode-appropriate formula
3. **Check override rules** (see Decision Matrix)
4. **Cross-reference frameworks** for consensus and conflicts
5. **Apply decision matrix** to determine verdict

**Synthesis guide:** [Synthesis Framework](./resources/synthesis-framework.md)

### Step 5: Generate Report

Using the appropriate template:
- Quick Check → [Quick Check Template](./resources/templates/quick-check.md)
- Comprehensive → [Comprehensive Report Template](./resources/templates/comprehensive-report.md)

Save to `research/evaluations/[idea-slug]-validation-[yyyy-mm-dd].md`

### Step 6: Present Decision

Present to user:
1. **Composite score** with scoring matrix table
2. **Verdict** (GO / TEST MORE / PIVOT / NO-GO)
3. **Top strengths** and **critical issues**
4. **Action plan** based on verdict
5. **Kill criteria** (conditions that would change the decision)

## Scoring Details

### Composite Score Weights

| Framework | Quick Check | Comprehensive |
|-----------|-----------|--------------|
| Market Opportunity | 35% | 20% |
| Execution Feasibility | 35% | 20% |
| Strategic Position | — | 15% |
| Risk Profile | 30% | 15% |
| Intellectual Honesty | — | 10% |
| Investment Worthiness | — | 20% |

### Score Interpretation

| Range | Meaning |
|-------|---------|
| 8.0 - 10.0 | Exceptional opportunity, rare alignment |
| 7.0 - 7.9 | Strong opportunity, proceed with confidence |
| 5.5 - 6.9 | Promising but needs more validation |
| 4.0 - 5.4 | Significant issues, pivot recommended |
| 0.0 - 3.9 | Not viable, move on |

## Integration

### As Standalone Skill

User triggers directly:
```
"이 아이디어 평가해줘" / "evaluate this idea"
"실현 가능성 검증해줘" / "check feasibility"
"validate my business idea"
```

### As Orchestrator Sub-agent

Called by `business-orchestrator`:
```
Task: description="Validate business idea"
  subagent_type="general-purpose"
  prompt="You are the idea-validator agent. Read the skill at
  .claude/skills/idea-validator/SKILL.md and run Comprehensive validation
  for this idea: [IDEA]. User context: [CONTEXT].
  Return the complete validation report with composite score and verdict."
```

The orchestrator receives the composite score and integrates it with success-formula-analyzer results.

### Pipeline Position

```
idea-finder (discover rough ideas)
    ↓
idea-elaborator (flesh out into concrete concept)
    ↓
idea-validator (THIS SKILL — score + decide)
    ↓
business-orchestrator (comprehensive plan with success patterns)
```

### After Validation

- **GO:** Start building with action plan
- **TEST MORE:** Run specific validation experiments
- **PIVOT:** Use idea-finder for alternatives, or pivot dimensions
- **NO-GO:** Archive learnings, try idea-finder

## Quick Reference

### When to Use Each Mode

| Situation | Mode | Why |
|-----------|------|-----|
| "Is this idea any good?" | Quick Check | Fast screening |
| Comparing 3+ ideas | Quick Check (each) | Efficient comparison |
| "Should I build this?" | Comprehensive | Full validation before commitment |
| Orchestrator sub-agent | Comprehensive | Deep analysis for synthesis |
| Post-pivot re-evaluation | Quick Check | Quick re-screen after changes |

### Common Patterns

**Pattern 1: Quick-to-Comprehensive funnel**
1. Quick Check on 3 ideas → Pick highest scorer
2. Comprehensive on the winner → Final decision

**Pattern 2: Iterative improvement**
1. Comprehensive → Identify weakest frameworks
2. Improve the idea targeting weak areas
3. Re-run affected frameworks → Compare before/after

**Pattern 3: Orchestrator integration**
1. Orchestrator receives idea
2. Runs idea-validator (Comprehensive) + success-formula-analyzer in parallel
3. Synthesizes both results into final recommendation

## Resources

### Framework Guides
- [Startup Validator](./resources/frameworks/startup-validator.md) — Market opportunity analysis
- [Execution Auditor](./resources/frameworks/execution-auditor.md) — Feasibility assessment
- [Strategic Advisor](./resources/frameworks/strategic-advisor.md) — Strategic positioning
- [Risk Analyst](./resources/frameworks/risk-analyst.md) — Risk identification
- [Devil's Advocate](./resources/frameworks/devils-advocate.md) — Assumption stress-testing
- [Investor Lens](./resources/frameworks/investor-lens.md) — Investment analysis

### Synthesis & Decision
- [Synthesis Framework](./resources/synthesis-framework.md) — Score integration methodology
- [Decision Framework](./resources/decision-framework.md) — GO/NO-GO criteria

### Report Templates
- [Comprehensive Report](./resources/templates/comprehensive-report.md) — Full 6-framework output
- [Quick Check Report](./resources/templates/quick-check.md) — 3-framework quick output

---

**Key Principle:** Validation ≠ Validation Theater. The goal is informed decision-making, not score optimization. An honest 5.0 with clear next steps is more valuable than an inflated 7.5 that hides real issues.
