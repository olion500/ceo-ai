# Skills

Production-tested skills for Claude Code that auto-activate based on context.

---

## What Are Skills?

Skills are modular knowledge bases that Claude loads when needed. They provide:
- Domain-specific guidelines
- Best practices
- Code examples
- Anti-patterns to avoid

**Problem:** Skills don't activate automatically by default.

**Solution:** This showcase includes the hooks + configuration to make them activate.

---

## Available Skills

### skill-developer (Meta-Skill)
**Purpose:** Creating and managing Claude Code skills

**Files:** 7 resource files (426 lines total)

**Use when:**
- Creating new skills
- Understanding skill structure
- Working with skill-rules.json
- Debugging skill activation

**Customization:** ✅ None - copy as-is

**[View Skill →](skill-developer/)**

---

## How to Add a Skill to Your Project

### Quick Integration

**For Claude Code:**
```
User: "Add the backend-dev-guidelines skill to my project"

Claude should:
1. Ask about project structure
2. Copy skill directory
3. Update skill-rules.json with their paths
4. Verify integration
```

See [CLAUDE_INTEGRATION_GUIDE.md](../../CLAUDE_INTEGRATION_GUIDE.md) for complete instructions.

### Manual Integration

**Step 1: Copy the skill directory**
```bash
cp -r claude-code-infrastructure-showcase/.claude/skills/backend-dev-guidelines \\
      your-project/.claude/skills/
```

**Step 2: Update skill-rules.json**

If you don't have one, create it:
```bash
cp claude-code-infrastructure-showcase/.claude/skills/skill-rules.json \\
   your-project/.claude/skills/
```

Then customize the `pathPatterns` for your project:
```json
{
  "skills": {
    "backend-dev-guidelines": {
      "fileTriggers": {
        "pathPatterns": [
          "YOUR_BACKEND_PATH/**/*.ts"  // ← Update this!
        ]
      }
    }
  }
}
```

**Step 3: Test**
- Edit a file in your backend directory
- The skill should activate automatically

---

## skill-rules.json Configuration

### What It Does

Defines when skills should activate based on:
- **Keywords** in user prompts ("backend", "API", "route")
- **Intent patterns** (regex matching user intent)
- **File path patterns** (editing backend files)
- **Content patterns** (code contains Prisma queries)

### Configuration Format

```json
{
  "skill-name": {
    "type": "domain" | "guardrail",
    "enforcement": "suggest" | "block",
    "priority": "high" | "medium" | "low",
    "promptTriggers": {
      "keywords": ["list", "of", "keywords"],
      "intentPatterns": ["regex patterns"]
    },
    "fileTriggers": {
      "pathPatterns": ["path/to/files/**/*.ts"],
      "contentPatterns": ["import.*Prisma"]
    }
  }
}
```

### Enforcement Levels

- **suggest**: Skill appears as suggestion, doesn't block
- **block**: Must use skill before proceeding (guardrail)

**Use "block" for:**
- Preventing breaking changes (MUI v6→v7)
- Critical database operations
- Security-sensitive code

**Use "suggest" for:**
- General best practices
- Domain guidance
- Code organization

---

## Creating Your Own Skills

See the **skill-developer** skill for complete guide on:
- Skill YAML frontmatter structure
- Resource file organization
- Trigger pattern design
- Testing skill activation

**Quick template:**
```markdown
---
name: my-skill
description: What this skill does
---

# My Skill Title

## Purpose
[Why this skill exists]

## When to Use This Skill
[Auto-activation scenarios]

## Quick Reference
[Key patterns and examples]

## Resource Files
- [topic-1.md](resources/topic-1.md)
- [topic-2.md](resources/topic-2.md)
```

---

## Troubleshooting

### Skill isn't activating

**Check:**
1. Is skill directory in `.claude/skills/`?
2. Is skill listed in `skill-rules.json`?
3. Do `pathPatterns` match your files?
4. Are hooks installed and working?
5. Is settings.json configured correctly?

**Debug:**
```bash
# Check skill exists
ls -la .claude/skills/

# Validate skill-rules.json
cat .claude/skills/skill-rules.json | jq .

# Check hooks are executable
ls -la .claude/hooks/*.sh

# Test hook manually
./.claude/hooks/skill-activation-prompt.sh
```

### Skill activates too often

Update skill-rules.json:
- Make keywords more specific
- Narrow `pathPatterns`
- Increase specificity of `intentPatterns`

### Skill never activates

Update skill-rules.json:
- Add more keywords
- Broaden `pathPatterns`
- Add more `intentPatterns`

---

## For Claude Code

**When integrating a skill for a user:**

1. **Read [CLAUDE_INTEGRATION_GUIDE.md](../../CLAUDE_INTEGRATION_GUIDE.md)** first
2. Ask about their project structure
3. Customize `pathPatterns` in skill-rules.json
4. Verify the skill file has no hardcoded paths
5. Test activation after integration

**Common mistakes:**
- Keeping example paths (blog-api/, frontend/)
- Not asking about monorepo vs single-app
- Copying skill-rules.json without customization

---

## Documentation Skills

### markdown-formatter
**Purpose:** 마크다운 문서를 자동으로 포맷팅하고 정리

**Use when:**
- "마크다운 정리해줘"
- "format this markdown"
- "문서 포맷팅"
- "markdown cleanup"

**5-Step Workflow:**
1. **rumdl lint check** - 57개 lint 규칙으로 자동 수정
2. **Obsidian frontmatter** - YAML 메타데이터 추가
3. **Link conversion** - Wiki-style → Markdown links
4. **Deduplication** - 중복 콘텐츠 제거
5. **Readability** - 가독성 best practices 적용

**Features:**
- ✅ Auto-fix lint errors (MD001-MD053)
- ✅ Document-type frontmatter templates (10+ types)
- ✅ Wiki/bare URL → markdown link conversion
- ✅ Duplicate detection algorithms
- ✅ Complete readability guidelines (794 lines)

**Reference Files:**
- [READABILITY_GUIDE.md](markdown-formatter/resources/READABILITY_GUIDE.md) - 완전한 가독성 가이드
- [RUMDL_RULES.md](markdown-formatter/resources/RUMDL_RULES.md) - 57개 lint 규칙 설명
- [FRONTMATTER_TEMPLATES.md](markdown-formatter/resources/FRONTMATTER_TEMPLATES.md) - 문서 타입별 템플릿
- [LINK_CONVERSION.md](markdown-formatter/resources/LINK_CONVERSION.md) - 링크 변환 패턴
- [DEDUPLICATION_STRATEGIES.md](markdown-formatter/resources/DEDUPLICATION_STRATEGIES.md) - 중복 제거 전략

**Integration:**
- VS Code, GitHub Actions, Pre-commit hook 예제 포함
- Research 파일 생성 후 자동 실행 (success-story-researcher, success-formula-analyzer 등)

**[View Skill →](markdown-formatter/)**

---

## Business Analysis Skills (CEO AI)

### 🎯 Multi-Agent Business Analysis System

1인/소수 개발자를 위한 비즈니스 분석 multi-agent 시스템. **성공한 사람의 성공 방식을 카피해서 내 아이템에 적용**하는 것을 목표로 합니다.

```
┌──────────────────────────────────────┐
│     Business Orchestrator            │
│  전체 프로세스 조율 및 종합 분석     │
└──────────────────────────────────────┘
           │
           ├─────────────────┬─────────────────┐
           ▼                 ▼                 ▼
┌─────────────────┐ ┌─────────────────┐ ┌─────────────────┐
│ Success Formula │ │ Business Idea   │ │ Feasibility     │
│ Analyzer        │ │ Evaluator       │ │ Checker         │
└─────────────────┘ └─────────────────┘ └─────────────────┘
```

### success-story-researcher (NEW!)
**Purpose:** 웹에서 성공 스토리를 체계적으로 리서치하고 제작 과정(journey)을 추출

**Use when:**
- "성공 사례 찾아줘"
- "indie developer 스토리 검색"
- "제품이 어떻게 만들어졌는지"
- "founder journey 리서치"
- "building in public 사례"

**Key Features:**
- 📍 **Best Sources Guide:** Indie Hackers, Reddit, Twitter, Product Hunt 등 tier별 소스
- 🔍 **Search Query Patterns:** 6가지 효과적인 검색 패턴 (Revenue-based, Timeline-based, etc)
- 📊 **Story Extraction Template:** 제작 과정을 체계적으로 추출하는 프레임워크
- 🎯 **Journey Focus:** 결과(outcome)뿐만 아니라 과정(how)을 중점적으로 수집
- 🛠️ **WebSearch/WebFetch 활용:** Claude의 웹 도구를 최대한 활용하는 전략

**Search Strategy Examples:**
```
# Revenue-based
"$0 to $10K MRR SaaS 2024"

# Journey-based
"building [product] in public" month 1

# Post-mortem
"[product] post-mortem" lessons learned
```

**[View Skill →](success-story-researcher/)**

---

### success-formula-analyzer
**Purpose:** 성공한 indie developer와 소규모 팀의 패턴을 분석하여 재현 가능한 성공 방정식 추출

**Use when:**
- "성공 패턴 분석"
- "indie developer 성공 사례"
- "어떻게 성공했는지"
- "수익 모델 연구"

**Outputs:**
- 성공 케이스 스터디 분석
- 수익 모델 패턴
- 재현 가능한 tactics
- 5가지 성공 패턴 카테고리

**Workflow:** success-story-researcher로 스토리 수집 → success-formula-analyzer로 패턴 추출

**[View Skill →](success-formula-analyzer/)**

---

### business-idea-evaluator
**Purpose:** 비즈니스 아이디어를 8개 차원에서 평가하고 근거 기반 점수 제공

**Use when:**
- "아이디어 평가"
- "비즈니스 검증"
- "시장성 분석"
- "이 아이디어 괜찮은지"

**Evaluation Dimensions (1-10 each, 80 total):**
1. Problem Intensity
2. Market Size
3. Competition Level
4. Monetization Clarity
5. Differentiation
6. Time to Market
7. Solo/Small Team Fit
8. Skills Match

**Score Interpretation:**
- 56-80: 강력한 잠재력 ✅
- 41-55: 좋은 잠재력 🟢
- 26-40: 중간 잠재력 🟡
- 0-25: 높은 리스크 🔴

**[View Skill →](business-idea-evaluator/)**

---

### feasibility-checker
**Purpose:** 당신이 실제로 실행 가능한지 3가지 관점에서 검증

**Use when:**
- "실행 가능한지"
- "내가 만들 수 있나"
- "필요한 리소스"
- "시간/비용 예측"

**Three Pillars:**
1. **Technical Feasibility** - 스킬 갭, 기술 복잡도, 학습 곡선
2. **Financial Feasibility** - 초기 비용, 운영 비용, Runway
3. **Time Feasibility** - 가용 시간, 타임라인, 기회 비용

**Score (1-10):**
- 7.1-10.0: 높은 실행 가능성
- 5.1-7.0: 노력으로 가능
- 3.1-5.0: 도전적
- 0-3.0: 실행 불가능

**[View Skill →](feasibility-checker/)**

---

### business-orchestrator
**Purpose:** 전체 분석 프로세스를 조율하고 종합 보고서 생성

**Use when:**
- "완전한 비즈니스 분석"
- "종합 평가"
- "end-to-end 검증"
- "액션 플랜 생성"

**Orchestrates:**
1. success-formula-analyzer (성공 패턴)
2. business-idea-evaluator (아이디어 평가)
3. feasibility-checker (실행 가능성)

**Outputs:**
- 통합 점수 (최종 10점 만점)
- Go/Iterate/No-Go 추천
- 상세 액션 플랜 (4단계 로드맵)
- 리스크 분석 및 대응 전략
- Success metrics & Kill criteria

**[View Skill →](business-orchestrator/)**

---

### idea-finder
**Purpose:** 성공 패턴을 적용하여 새로운 비즈니스 아이디어 생성

**Use when:**
- "비즈니스 아이디어 찾아줘"
- "뭘 만들면 좋을까"
- "startup idea generation"
- "사업 아이템 추천"

**Method:**
1. **Analyze patterns** in `research/patterns/`
2. **Apply success formulas** to find market gaps
3. **Generate 3-10 ideas** with complete validation
4. **Auto-run feasibility check** for each idea
5. **Save to** `research/ideas/[idea-name]-[date].md`

**Outputs:**
- 각 아이디어별 상세 분석 파일
- Feasibility 점수 (자동 계산)
- 적용된 성공 패턴 매핑
- 실행 가능성 검증

**Key Features:**
- "Scratch your own itch" methodology
- Data-driven idea selection
- Market gap analysis
- Success pattern → New idea mapping

**[View Skill →](idea-finder/)**

---

### 💡 사용 예시

**웹에서 성공 스토리 리서치:**
```
"SaaS 분야에서 $10K MRR 달성한
indie developer 스토리 3-5개 찾아줘.
특히 제작 과정이 상세한 걸로"
```
→ success-story-researcher가 웹 검색 + 스토리 추출

**성공 사례에서 패턴 학습:**
```
"Gumroad가 어떻게 성공했는지 웹에서 찾아보고
패턴을 분석해서 내 프로젝트에 적용해줘"
```
→ success-story-researcher (검색) + success-formula-analyzer (패턴 추출)

**완전한 비즈니스 분석:**
```
"완전한 비즈니스 분석 실행:
아이디어: [설명]
타겟: [고객]
배경: [스킬/시간/예산]"
```
→ business-orchestrator가 모든 agent 조율

**실행 가능성 체크:**
```
"React + Node.js로 AI SaaS를 만들고 싶은데
주말에만 시간 있고, 예산 거의 없어. 가능할까?"
```
→ feasibility-checker가 3-Pillar 검증

**Customization:** ✅ 추가 설정 불필요 - 바로 사용 가능

---

## Next Steps

1. **Start simple:** Add one skill that matches your work
2. **Verify activation:** Edit a relevant file, skill should suggest
3. **Add more:** Once first skill works, add others
4. **Customize:** Adjust triggers based on your workflow

**Questions?** See [CLAUDE_INTEGRATION_GUIDE.md](../../CLAUDE_INTEGRATION_GUIDE.md) for comprehensive integration instructions.
