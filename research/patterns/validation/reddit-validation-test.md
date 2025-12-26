---
title: Reddit Validation Test
pattern-category: validation
tags: [pattern, validation]
type: Pattern
---
# Reddit Validation Test

## What Is This Pattern?

Use real questions from relevant Reddit communities to test your product's quality through blind expert evaluation. Professionals assess outputs without knowing they're AI/automated-generated, providing unbiased validation.

## How It Works

1. **Find Relevant Subreddit**: Identify community asking questions your product solves (r/legaladvice, r/accounting, etc.)
2. **Extract Real Questions**: Collect 50-100 representative questions from the community
3. **Generate Outputs**: Run questions through your product/prototype
4. **Blind Testing**: Give outputs to domain experts WITHOUT revealing source (AI vs human)
5. **Quality Threshold**: Set acceptance criteria (e.g., "Would you send this to a client with zero edits?")
6. **Validation Success**: If 70-90%+ pass expert review, you have product-market fit signal

## Real Examples (Ranked by Success)

### 1. Harvey Legal AI - Winston Weinberg & Gabriel Pereyra ($100M ARR)
- **Context**: Pre-launch validation for AI legal assistant (2022)
- **Execution**:
  - Scraped 100 questions from r/legaladvice (landlord-tenant law)
  - Ran chain-of-thought prompts over California statutes
  - Gave AI-generated answers to 3 landlord-tenant attorneys
  - Did NOT mention AI involvement (blind test)
  - Asked: "Would you send this to client with zero edits?"
- **Results**:
  - 86 out of 100 samples approved by 2+ attorneys
  - Proof that lawyers couldn't distinguish high-quality AI from human work
  - Gave founders confidence to pursue $5M seed funding
- **Timeline**: $0 → $100M ARR in 35 months (validation was foundation)
- **Key Insight**: Blind testing removes bias - if experts can't tell difference, quality is there

## Why This Works

**Unbiased Validation**:
- Experts evaluate on merit, not preconceptions
- Removes "AI skepticism" bias
- Objective quality measurement

**Real-World Questions**:
- Reddit questions are authentic user problems
- No cherry-picking easy scenarios
- Represents actual use cases

**Expert Standards**:
- Professionals have high quality bars
- "Would send to client" is real-world threshold
- If passes expert review, will pass user review

**Cheap & Fast**:
- Reddit questions are free and abundant
- Can test 100s of scenarios in days
- No need to recruit test users initially

## Prerequisites

- **Skills Required**:
  - Access to domain experts for blind review
  - Ability to extract/scrape Reddit data
  - Product prototype capable of answering questions
- **Time Required**: Days to weeks (question collection + expert review)
- **Capital Required**: Minimal (expert time, possibly small payments)
- **Other Requirements**:
  - Active subreddit relevant to your domain
  - Ethical clearance (don't mislead experts about purpose)
  - Domain expertise to interpret results

## Common Mistakes

1. **Mistake**: Revealing it's AI before getting feedback
   - **Why It Fails**: Bias against AI taints evaluation
   - **How to Avoid**: Present as "new research" or "experimental outputs"

2. **Mistake**: Cherry-picking easy questions
   - **Why It Fails**: Doesn't represent real product use
   - **How to Avoid**: Random sample or top-voted questions (hard ones)

3. **Mistake**: Testing with non-experts
   - **Why It Fails**: Can't distinguish good from mediocre
   - **How to Avoid**: Use practicing professionals in the domain

4. **Mistake**: Not setting clear acceptance criteria upfront
   - **Why It Fails**: Move goalposts after seeing results
   - **How to Avoid**: Define threshold before testing (e.g., "70% approval needed")

## When to Use This Pattern

✅ **Good Fit When:**
- Building AI/automation for professional domains (legal, medical, accounting, etc.)
- Quality is critical and measurable by experts
- Relevant active subreddit exists (r/legaladvice, r/accounting, r/medicine, etc.)
- Need objective validation before investing heavily
- Skepticism exists about AI in your domain

❌ **Bad Fit When:**
- Consumer product where preference is subjective
- No relevant Reddit community (too niche)
- Can't access domain experts for review
- Domain has no objective quality standards

## Validation Thresholds

**Interpretation Guide:**

| Approval Rate | Signal | Action |
|---------------|--------|--------|
| 90%+ | Exceptional quality | Proceed with confidence, strong PMF signal |
| 70-90% | Good quality | Proceed, iterate on edge cases |
| 50-70% | Marginal | Needs improvement, not ready for launch |
| <50% | Poor quality | Major rework needed or pivot |

**Harvey's 86% Approval**:
- 86 of 100 samples approved by 2+ of 3 attorneys
- Well above 70% threshold
- Strong enough to pursue $5M seed funding
- Foundation for $100M ARR outcome

## Related Patterns

- **Idea Discovery**: [domain-expertise-gap](../idea-discovery/domain-expertise-gap.md) - Insider knowledge required
- **MVP**: [partner-with-platform-leader](../mvp-building/partner-with-platform-leader.md) - Harvey + OpenAI
- **Customer Acquisition**: [domain-expert-hiring](../differentiation/domain-expert-hiring.md) - Hire professionals who understand quality

## Alternative Validation Methods

**If Reddit doesn't apply to your domain:**

1. **Quora Validation**: Similar approach with Quora questions
2. **Industry Forums**: Use Stack Exchange, niche forums
3. **Customer Support Tickets**: Use real support questions from companies
4. **Expert Panels**: Recruit small group of professionals for ongoing testing

## Sources

- Harvey Legal AI story: https://techcrunch.com/2025/11/14/inside-harvey-how-a-first-year-legal-associate-built-one-of-silicon-valleys-hottest-startups/ (accessed 2025-12-16)
- Harvey founding story: https://research.contrary.com/company/harvey (accessed 2025-12-16)
