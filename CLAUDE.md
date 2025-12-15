# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

CEO AI is a multi-agent business analysis system for indie developers and small teams. It uses Claude Code's skill system to coordinate specialized agents that research success stories, analyze patterns, evaluate ideas, and validate execution feasibility.

**Core Philosophy**: Don't copy successful products - copy the success formula and apply it to your own ideas.

### Dual Purpose Repository

This repository serves two purposes:

1. **Working Application**: A complete business analysis system ready to use
2. **Reference Library**: A showcase of Claude Code infrastructure components (skills, agents, hooks, commands) that can be integrated into other projects

**IMPORTANT FOR INTEGRATION**: When users ask to integrate components from this repository into their projects, always:
- Ask about their project structure first (monorepo vs single app, directory names)
- Check tech stack compatibility before copying development skills
- Customize `pathPatterns` in `skill-rules.json` to match their structure
- Never assume their project structure matches this one
- See `CLAUDE_INTEGRATION_GUIDE.md` for detailed integration procedures

## Architecture

### Multi-Agent System

This repository implements a coordinated multi-agent workflow using Claude Code skills:

```
User Request
    ↓
business-orchestrator (coordinates everything)
    ↓
    ├── success-story-researcher (web research)
    ├── success-formula-analyzer (pattern extraction)
    ├── business-idea-evaluator (8-dimension scoring)
    └── feasibility-checker (execution validation)
    ↓
Integrated Report + Action Plan
```

Each agent is a Claude Code skill located in `.claude/skills/[agent-name]/SKILL.md`.

### Key Components

**Skills** (`.claude/skills/`):
- Each skill has a main `SKILL.md` and optional `resources/` directory
- Skills auto-activate based on keywords/intent patterns defined in `skill-rules.json`
- Business analysis skills: `success-story-researcher`, `success-formula-analyzer`, `business-idea-evaluator`, `feasibility-checker`, `business-orchestrator`, `idea-finder`
- Documentation skills: `markdown-formatter`
- Development skills: `backend-dev-guidelines`, `frontend-dev-guidelines`, `route-tester`, `error-tracking`, `skill-developer`

**Data Storage** (`research/`):
- `stories/`: Individual product success stories (`[product-slug]-[yyyy-mm-dd].md`)
- `reports/`: Multi-product analysis reports (`[topic]-analysis-[yyyy-mm-dd].md`)
- `patterns/`: Extracted reusable success patterns, organized by business stage:
  - `common/`: Universal patterns all successful businesses follow
  - `idea-discovery/`: How to find business ideas (ranked by success probability)
  - `validation/`: How to validate ideas (ranked by reliability)
  - `mvp-building/`: MVP development strategies (ranked by speed)
  - `customer-acquisition/`: Getting first customers (ranked by cold-start effectiveness)
  - `product-market-fit/`: Achieving PMF (ranked by signal clarity)
  - `growth/`: Scaling strategies (ranked by ROI)
  - `monetization/`: Business models (ranked by predictability)
  - `distribution/`: Distribution channels (ranked by leverage)
  - `retention/`: Customer retention tactics (ranked by impact)
  - `differentiation/`: Differentiation strategies (ranked by defensibility)

**Agents** (`.claude/agents/`):
- Standalone specialized agents for code review, refactoring, testing, debugging
- Work independently without configuration
- Note: Some agents reference auth/testing patterns from example projects (not this repo's structure)

### Skill Activation System

The `skill-rules.json` file controls when skills auto-activate:

- **Prompt triggers**: Keywords and intent patterns in user messages
- **File triggers**: Path patterns and content patterns in edited files
- **Enforcement levels**:
  - `suggest`: Shows suggestion, doesn't block
  - `block`: Requires skill usage before proceeding (guardrail)
  - `warn`: Shows warning, allows proceeding

Example activation:
```
User: "간단한 웹툴 성공 사례 10개 찾아줘"
→ Triggers success-story-researcher skill (keyword: "성공 사례")
```

## Common Usage Patterns

### Research Success Stories

```
"SaaS 분야에서 $10K MRR 달성한 스토리 3개 찾아줘"
```
- Activates `success-story-researcher` skill
- Searches web using patterns from `SEARCH_QUERIES_CHEATSHEET.md`
- Saves to `research/stories/[product]-[date].md`

### Analyze Patterns

```
"지금까지 수집한 스토리에서 공통 패턴 추출해줘"
```
- Activates `success-formula-analyzer` skill
- Reads files from `research/stories/`
- Extracts patterns into categorized directories:
  - Common patterns (must-do fundamentals)
  - Stage-specific patterns (idea discovery, validation, MVP, acquisition, PMF, growth, monetization, distribution, retention, differentiation)
  - Patterns ranked by success probability/effectiveness within each category
- Generates `research/reports/[topic]-patterns-[date].md` with cross-pattern analysis

### Evaluate Business Ideas

```
"완전한 비즈니스 분석 실행:
아이디어: [description]
타겟: [customer]
배경: [skills/time/budget]"
```
- Activates `business-orchestrator` skill
- Coordinates all 4 analysis agents in parallel
- Returns comprehensive report with:
  - Combined score (out of 10)
  - GO/ITERATE/NO-GO recommendation
  - 4-phase action plan
  - Risk analysis and mitigation strategies

### Format and Clean Markdown Documents

```
"이 마크다운 파일 정리해줘"
or
"format this markdown document and clean it up"
```
- Activates `markdown-formatter` skill
- Applies 5-step workflow:
  1. Run rumdl lint check and auto-fix
  2. Add Obsidian-style frontmatter metadata
  3. Convert internal links (wiki-style → markdown)
  4. Remove duplicate content
  5. Apply readability best practices
- **Auto-triggered** after creating research files
- Ensures all markdown files follow consistent formatting

## File Organization

### Research Data Templates

**Individual Story** (`research/stories/`):
```markdown
# [Product] Success Story
**Research Date:** YYYY-MM-DD
**Category:** [type]
**Revenue Range:** [$X - $Y MRR]

## Quick Facts
## The Story
## Reproducible Tactics
## Sources
```

**Pattern Analysis Report** (`research/reports/`):
```markdown
# [Topic] Pattern Analysis
**Analysis Date:** YYYY-MM-DD
**Stories Analyzed:** [N] success stories

## Common Patterns Identified
## Idea Discovery Patterns (Ranked by Success Rate)
## Validation Patterns (Ranked by Reliability)
## MVP Building Patterns (Ranked by Speed)
## Customer Acquisition Patterns (Ranked by Cold-Start Effectiveness)
## Product-Market Fit Patterns (Ranked by Signal Clarity)
## Growth Patterns (Ranked by ROI)
## Monetization Patterns (Ranked by Predictability)
## Distribution Patterns (Ranked by Leverage)
## Retention Patterns (Ranked by Impact)
## Differentiation Patterns (Ranked by Defensibility)
## Pattern Combinations
## Recommendations by Use Case
## Meta Insights
```

**Individual Pattern File** (`research/patterns/[category]/[pattern-name].md`):
```markdown
# [Pattern Name]
**Category:** [category]
**Success Rate:** High/Medium/Low
**Time Investment:** [estimate]
**Difficulty:** Easy/Medium/Hard

## What Is This Pattern?
## How It Works
## Real Examples (Ranked by Success)
## Why This Works
## Prerequisites
## Common Mistakes
## When to Use This Pattern
## Related Patterns
## Sources
```

### Naming Conventions

- Product slugs: lowercase, hyphens, no special chars (`notion`, `convertkit`, `dev-utils`)
- Story files: `[product-slug]-[yyyy-mm-dd].md`
- Report files: `[topic]-patterns-[yyyy-mm-dd].md`
- Pattern files: `[category]/[pattern-name].md` (kebab-case)
- Always include dates for temporal context

## Development Guidelines

### Frontend (React/MUI v7)

When editing files matching `frontend/src/**/*.tsx`:
- Uses **MUI v7** with Grid size={{}} prop (NOT xs/sm props)
- React best practices enforced via `frontend-dev-guidelines` skill
- File organization: features-based structure
- TypeScript strict mode required

### Backend (Node.js/Express/Prisma)

When editing files matching `**/src/**/*.ts` (backend paths):
- Layered architecture: Routes → Controllers → Services → Repositories
- Sentry error tracking required (ALL errors must be captured)
- Zod validation for input
- Prisma for database access
- See `backend-dev-guidelines` skill for patterns

### Skill Development

When creating/modifying skills:
- Main file: `SKILL.md` with YAML frontmatter
- Resources: Optional `resources/` directory for additional files
- Update `skill-rules.json` with triggers
- See `skill-developer` skill for meta-guidance

**IMPORTANT**: The `pathPatterns` in this repository's `skill-rules.json` are configured for example paths:
- `blog-api/src/**/*.ts`
- `auth-service/src/**/*.ts`
- `frontend/src/**/*.tsx`

These paths are **reference examples** only. When integrating into other projects, `pathPatterns` must be customized to match the target project's actual directory structure.

## Important Notes

### Tech Stack Compatibility

**Development Skills** (Framework-Specific):
- `frontend-dev-guidelines`: Requires React 18+, MUI v7, TanStack Query/Router, TypeScript
- `backend-dev-guidelines`: Requires Node.js, Express, Prisma, Sentry, TypeScript
- `route-tester`: Requires JWT cookie-based authentication (framework agnostic)
- `error-tracking`: Requires Sentry (works with most backends)

**Business Analysis Skills** (Tech-Agnostic):
- `success-story-researcher`: Works with any tech stack
- `success-formula-analyzer`: Works with any tech stack
- `business-idea-evaluator`: Works with any tech stack
- `feasibility-checker`: Works with any tech stack
- `business-orchestrator`: Works with any tech stack

**Meta Skills** (Universal):
- `skill-developer`: Works with any tech stack

**Integration Rule**: When integrating development skills into projects with different tech stacks:
1. **Ask first**: "Do you use [required tech]?"
2. **If NO**: Offer to adapt the skill as a template or extract framework-agnostic patterns
3. **If YES**: Copy and customize `pathPatterns` for their project structure

**What Transfers Across Tech Stacks**:
- ✅ Layered architecture patterns (Routes → Controllers → Services)
- ✅ File organization strategies (features/ directory pattern)
- ✅ Error handling philosophy
- ✅ Testing strategies
- ✅ Performance optimization principles

**What Doesn't Transfer**:
- ❌ Framework-specific code examples (React hooks, MUI components, Express middleware)
- ❌ ORM-specific queries (Prisma → different ORMs)
- ❌ Library APIs (MUI → Vuetify/Bootstrap)

### Data Verification

When researching success stories:
- Always include source URLs with dates accessed
- Cross-reference multiple sources for validation
- Focus on "how they built it" not just "they succeeded"
- Prefer founder first-hand accounts over third-party summaries
- Recent data (<2 years) preferred

### Multi-Language Support

This repository uses **Korean** as the primary language for documentation and user interactions, but the system works fully in English as well.

## Component Integration Guide

When users request to integrate components from this repository into their projects:

### Integrating Skills

**Step-by-Step**:
1. **Understand their project**:
   - Ask: "What's your project structure? Monorepo or single app?"
   - Ask: "Where is your [backend/frontend] code located?"
   - Ask: "What frameworks/technologies do you use?"

2. **Check compatibility**:
   - For development skills: Verify tech stack matches requirements
   - For business skills: No compatibility checks needed

3. **Copy the skill**:
   ```bash
   cp -r .claude/skills/[skill-name] $TARGET_PROJECT/.claude/skills/
   ```

4. **Customize `skill-rules.json`**:
   - If target project has no `skill-rules.json`: Copy and customize
   - If exists: Merge the new skill entry carefully
   - **CRITICAL**: Update `pathPatterns` to match their structure

**pathPatterns Examples**:
```json
// Monorepo with workspaces
"pathPatterns": ["packages/*/src/**/*.ts", "apps/*/src/**/*.tsx"]

// Nx monorepo
"pathPatterns": ["apps/api/src/**/*.ts", "libs/*/src/**/*.ts"]

// Simple single app
"pathPatterns": ["src/**/*.ts", "backend/**/*.ts"]
```

5. **Verify integration**:
   ```bash
   cat $TARGET_PROJECT/.claude/skills/skill-rules.json | jq .
   ```

### Integrating Agents

**Agents are standalone** - easiest to integrate:
```bash
cp .claude/agents/[agent-name].md $TARGET_PROJECT/.claude/agents/
```

Check for hardcoded paths before copying:
- Replace `~/git/old-project/` with `$CLAUDE_PROJECT_DIR` or `.`
- Update screenshot paths if needed

### Integrating Hooks

**Generic Hooks** (safe to copy as-is):
- `skill-activation-prompt.sh/ts`: Auto-suggests skills based on prompts
- `post-tool-use-tracker.sh`: Tracks file changes

Copy and add to target project's `.claude/settings.json`:
```json
{
  "hooks": {
    "UserPromptSubmit": [{
      "hooks": [{
        "type": "command",
        "command": "$CLAUDE_PROJECT_DIR/.claude/hooks/skill-activation-prompt.sh"
      }]
    }]
  }
}
```

**Project-Specific Hooks** (require customization):
- Stop hooks like `tsc-check.sh`: Only for multi-service monorepos, requires editing service names

### Common Integration Mistakes to Avoid

❌ **Don't**:
- Copy `skill-rules.json` as-is without updating `pathPatterns`
- Copy development skills without checking tech stack compatibility
- Assume their project structure matches this repository
- Add Stop hooks without testing them first
- Copy entire `.claude/settings.json`

✅ **Do**:
- Ask about project structure first
- Verify tech stack compatibility
- Customize `pathPatterns` for their directories
- Test manually before adding to settings
- Extract and merge only needed settings sections
- Make hooks executable: `chmod +x *.sh`

### Adaptation Workflow for Different Tech Stacks

When their stack differs from skill requirements:

**Option 1: Adapt Existing Skill**
1. Copy skill as starting point
2. Keep: Architecture patterns, file organization, best practices
3. Replace: Framework-specific code examples, library APIs
4. Update: skill-rules.json triggers for their stack

**Option 2: Extract Framework-Agnostic Patterns**
1. Identify transferable patterns (layered architecture, etc.)
2. Create new skill with just those patterns
3. Let user add framework-specific examples later

**Option 3: Use as Reference Only**
- User browses existing skill for inspiration
- Create new skill from scratch using structure as template

## Quick Reference

**Start business analysis:**
```
"완전한 비즈니스 분석 실행: [아이디어/타겟/배경]"
```

**Research competitors:**
```
"[Product name]이 어떻게 성공했는지 웹에서 찾고 분석해줘"
```

**Find success patterns:**
```
"[Category]에서 성공한 사례 [N]개 찾고 공통점 분석해줘"
```

**Integrate components into other projects:**
```
"Add the [skill/agent/hook name] to my project"
```
- See "Component Integration Guide" section above
- See `CLAUDE_INTEGRATION_GUIDE.md` for detailed procedures

**Reference documentation:**
- Quick start: `CEO_AI_QUICKSTART.md`
- Search strategies: `SEARCH_QUERIES_CHEATSHEET.md`
- Architecture overview: `README.md`
- Integration procedures: `CLAUDE_INTEGRATION_GUIDE.md`

## Version

**Version:** 1.0.0
**Last Updated:** 2024-12-10
**Repository Type:** Multi-agent business analysis system + Claude Code infrastructure showcase
