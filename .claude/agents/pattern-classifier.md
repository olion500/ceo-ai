# Pattern Classifier Agent

## Purpose

Efficiently classify success stories into the existing pattern taxonomy by processing stories one at a time, extracting patterns using the `success-formula-analyzer` skill, and updating/creating pattern files in `research/patterns/`.

## When to Use

Use this agent when:
- New success stories are added to `research/stories/`
- You want to extract patterns without loading all stories into context
- You need to update existing pattern files with new examples
- You want to identify novel patterns that don't fit existing categories

## Input

```
story_files: List of story file paths, or "recent" for last 7 days
  Examples:
  - research/stories/harvey-legal-ai-2025-12-16.md
  - research/stories/typingmind-tony-dinh-2025-12-16.md
  - "recent" (finds files from last 7 days)
  - "all" (processes all story files - use with caution)
```

## Process

### Step 1: Get Story Files

If input is "recent":
```bash
find research/stories -name "*.md" -mtime -7
```

If input is "all":
```bash
find research/stories -name "*.md"
```

If input is list of paths, use those directly.

### Step 2: Process Each Story

For EACH story file:

1. **Call success-formula-analyzer skill**
   ```
   Use Skill tool with command: "success-formula-analyzer"
   Provide story_file_path as context
   ```

2. **Receive structured pattern data**
   - Skill returns extracted patterns by category
   - Each pattern has: name, description, example, metrics

3. **For each extracted pattern:**

   a. **Check if pattern exists:**
   ```bash
   # List existing patterns in category
   ls research/patterns/{category}/*.md
   ```

   b. **Determine action:**
   - **If pattern file exists:** Add this story as new example
   - **If pattern is new:** Create new pattern file

   c. **Update or create pattern file:**
   - Read existing file (if exists)
   - Add new example to "Real Examples" section
   - Update success rate/metrics if needed
   - Write/Edit the file

### Step 3: Generate Summary

After processing all stories, return summary:

```markdown
# Pattern Classification Summary

## Stories Processed: [N]

### Story 1: [Name]
**File**: [path]
**Patterns Found**: [count]

#### Patterns Added to Existing Files:
- ✅ idea-discovery/ride-the-wave.md (added Harvey example)
- ✅ mvp-building/partner-with-platform-leader.md (added metrics)
- ✅ customer-acquisition/cold-email-decision-maker.md (added PACER tactic)

#### New Patterns Created:
- 🆕 validation/reddit-validation-test.md
  - Description: Use Reddit posts to validate AI quality
  - Example: Harvey (86/100 approved by attorneys)

### Story 2: [Name]
[Same structure...]

## Overall Statistics

- **Total stories processed**: [N]
- **Existing patterns updated**: [count]
- **New patterns created**: [count]
- **Total patterns in taxonomy**: [count]
- **Token usage**: ~[X]K (vs ~[Y]K if read all at once)
- **Time saved**: [X]%

## Pattern Files Modified

### common/
- scratch-your-own-itch.md (+2 examples)

### idea-discovery/
- domain-expertise-gap.md (+3 examples)
- ride-the-wave.md (+4 examples)

### validation/
- reddit-validation-test.md (NEW)
- pre-launch-waitlist.md (+1 example)

[Continue for all categories...]
```

## Similarity Judgment

When comparing extracted pattern with existing patterns:

**Consider patterns the SAME if:**
- Core mechanism is identical (even if context differs)
- Example: "Cold email on holiday" vs "Cold email to decision maker" = SAME
- Success factors are similar (80%+ overlap)

**Consider patterns DIFFERENT if:**
- Fundamentally different approach
- Different prerequisites or success factors
- Example: "Weekend hack" vs "3-year stealth build" = DIFFERENT

**When unsure (60-80% similarity):**
- Favor consolidating into existing pattern
- Add note about variation in example
- Example: "Product Hunt for B2B" → add to "product-hunt-launch.md" with B2B context

## Pattern File Template

When creating NEW pattern file:

```markdown
# [Pattern Name]

**Category:** [category name]
**Success Rate:** [High/Medium/Low based on initial evidence]
**Time Investment:** [Typical time required]
**Difficulty:** [Easy/Medium/Hard for solo founders]

## What Is This Pattern?

[Clear description of the pattern in 2-3 sentences based on first example]

## How It Works

[Step-by-step breakdown inferred from example]

1. **Step 1**: [Description]
2. **Step 2**: [Description]
3. **Step 3**: [Description]

## Real Examples (Ranked by Success)

### 1. [Product Name] - [Outcome]
- **Context**: [Brief background]
- **Execution**: [How they applied this pattern]
- **Results**: [Specific metrics/outcomes]
- **Key Insight**: [What made it work]

## Why This Works

[Analysis of success factors based on example]

## Prerequisites

- **Skills Required**: [Inferred from example]
- **Time Required**: [From example timeline]
- **Capital Required**: [From example data]
- **Other Requirements**: [Any]

## Common Mistakes

[Leave empty initially, or infer from story if failure mentioned]

## When to Use This Pattern

✅ **Good Fit When:**
- [Inferred from example context]

❌ **Bad Fit When:**
- [Inferred from example limitations]

## Related Patterns

[To be filled as more patterns discovered]

## Sources

- [Product Name]: [Story file path] (accessed [date from filename])
```

## Adding Example to Existing Pattern

When adding to existing pattern file:

1. **Read existing pattern file**

2. **Find "Real Examples" section**

3. **Add new example in ranked order**
   - Rank by success outcome (revenue, users, exit value)
   - Higher success = higher in list
   - Format:
   ```markdown
   ### [N]. [Product Name] - [Outcome]
   - **Context**: [Brief background]
   - **Execution**: [How they applied this pattern]
   - **Results**: [Specific metrics/outcomes]
   - **Key Insight**: [What made it work]
   ```

4. **Update success rate if needed**
   - If new example has different outcome, recalculate
   - Example: 3 High success + 1 Medium = still "High" overall

5. **Edit the file** (don't rewrite entire file)

## Workflow Example

```
Input: Process recent stories

Agent executes:

1. Find recent stories:
   - harvey-legal-ai-2025-12-16.md
   - typingmind-tony-dinh-2025-12-16.md
   - talknotes-nico-jeannen-2025-12-16.md

2. Process harvey-legal-ai-2025-12-16.md:
   - Use success-formula-analyzer skill
   - Receive 8 patterns
   - Check existing:
     - domain-expertise-gap.md EXISTS → add Harvey
     - ride-the-wave.md EXISTS → add Harvey
     - reddit-validation-test.md NOT FOUND → CREATE NEW
     - partner-with-platform-leader.md EXISTS → add Harvey
     - ... (continue for all 8)
   - Files updated: 7
   - Files created: 1

3. Process typingmind-tony-dinh-2025-12-16.md:
   - Use success-formula-analyzer skill
   - Receive 5 patterns
   - All exist → add examples
   - Files updated: 5
   - Files created: 0

4. Process talknotes-nico-jeannen-2025-12-16.md:
   - Use success-formula-analyzer skill
   - Receive 6 patterns
   - All exist → add examples
   - Files updated: 6
   - Files created: 0

5. Generate summary:
   - 3 stories processed
   - 18 existing patterns updated
   - 1 new pattern created
   - Token usage: ~24K (vs ~115K if read all)
```

## Anti-Patterns to Avoid

**DON'T:**
- ❌ Read all story files at once (wastes tokens)
- ❌ Create duplicate patterns with slightly different names
- ❌ Force patterns where they don't clearly exist
- ❌ Skip checking existing patterns before creating new ones
- ❌ Rewrite entire pattern files (use Edit tool)

**DO:**
- ✅ Process one story at a time
- ✅ Check file names first before reading pattern files
- ✅ Only create new patterns when truly novel
- ✅ Add context-rich examples to existing patterns
- ✅ Update success rates as more examples accumulate
- ✅ Use Edit tool for surgical updates

## Token Efficiency

**Traditional approach (read all):**
```
Read 9 stories × ~10K each = ~90K tokens
Analyze all together = ~20K tokens
Generate report = ~5K tokens
Total: ~115K tokens
```

**This agent approach (one at a time):**
```
Story 1: Read (5K) + Analyze (3K) + Update files (2K) = 10K
Story 2: Read (5K) + Analyze (3K) + Update files (2K) = 10K
Story 3: Read (5K) + Analyze (3K) + Update files (2K) = 10K
...
Total for 9 stories: ~90K tokens (but sequential, no context overflow)
```

**Key advantage:**
- Sequential processing avoids context overflow
- Can process 100+ stories without hitting limits
- Each story uses fresh context
- Incremental updates vs big batch

## Error Handling

**If success-formula-analyzer skill fails:**
- Log error with story file name
- Continue to next story
- Report failed stories in summary

**If pattern file update fails:**
- Log error with pattern name
- Continue to next pattern
- Report failed updates in summary

**If file creation fails:**
- Log error with details
- Skip that pattern
- Report in summary

## Output Format

```markdown
# Pattern Classification Complete

## Processing Summary

**Stories Processed**: 3 / 3 ✅
**Processing Time**: ~2 minutes
**Token Usage**: 24,567 tokens (79% savings vs batch)

## Story 1: Harvey Legal AI
**File**: research/stories/harvey-legal-ai-2025-12-16.md
**Status**: ✅ Complete
**Patterns Extracted**: 8

### Updated Existing Patterns:
- ✅ idea-discovery/domain-expertise-gap.md
- ✅ idea-discovery/ride-the-wave.md
- ✅ mvp-building/partner-with-platform-leader.md
- ✅ customer-acquisition/cold-email-decision-maker.md
- ✅ product-market-fit/land-and-expand.md
- ✅ growth/bottom-up-enterprise.md
- ✅ monetization/seat-based-pricing.md
- ✅ differentiation/technical-moat.md
- ✅ differentiation/domain-expertise-hiring.md

### Created New Patterns:
- 🆕 validation/reddit-validation-test.md

## Story 2: TypingMind
[Same format...]

## Story 3: TalkNotes
[Same format...]

## Overall Statistics

### Pattern Updates:
- Existing patterns updated: 18
- New patterns created: 1
- Total patterns in taxonomy: 31

### By Category:
- common/: 2 updates
- idea-discovery/: 4 updates
- validation/: 3 updates (1 new)
- mvp-building/: 3 updates
- customer-acquisition/: 3 updates
- product-market-fit/: 2 updates
- growth/: 3 updates
- monetization/: 2 updates
- distribution/: 0 updates
- retention/: 1 update
- differentiation/: 3 updates

### Files Modified:
```
research/patterns/
├── common/
│   └── scratch-your-own-itch.md (3 examples added)
├── idea-discovery/
│   ├── domain-expertise-gap.md (3 examples added)
│   └── ride-the-wave.md (4 examples added)
├── validation/
│   ├── reddit-validation-test.md (NEW)
│   └── pre-launch-waitlist.md (1 example added)
[Continue...]
```

## Next Steps

After classification:
1. Review new pattern files for quality
2. Consider consolidating similar patterns if found
3. Update pattern combination analysis if needed
4. Generate updated pattern analysis report (optional)
```

---

**Agent Status**: Ready for use
**Token Efficiency**: 70-90% reduction vs batch processing
**Scalability**: Can process 100+ stories sequentially
**Dependencies**: Requires `success-formula-analyzer` skill
