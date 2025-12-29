# Market Gap Analysis Method

**Success Rate: 50%** - Good for improving existing products

## Overview

Find successful products with obvious flaws and build improved versions. Capture frustrated users.

## How It Works

### Step 1: Find Successful Product with Flaws

**Where to look:**
- Product Hunt recent launches
- App store top apps with <4 star rating
- Reddit complaints about popular tools
- Twitter searches for "[product] sucks"

### Step 2: Systematic Gap Identification

**The 5-Review Method:**
```
1. Read 100 most recent 1-3 star reviews
2. Categorize complaints into buckets
3. Count frequency of each complaint
4. Identify top 3 recurring issues
5. Check if you can solve them
```

**Gap Analysis Framework:**

| Gap Type | How to Identify | How to Validate | Difficulty to Fix |
|----------|----------------|-----------------|-------------------|
| **Missing Features** | "I wish it had X" (50+ mentions) | Ask users "would you switch if X existed?" | Medium |
| **UX Problems** | "Too complex" / "Confusing UI" (100+) | Show mockup, get feedback | Low-Medium |
| **Pricing Issues** | "Too expensive" (30+) | Survey willingness to pay | Low (just price lower) |
| **Performance** | "Slow" / "Crashes" (40+) | Technical benchmarking | High |
| **Support** | "No response" / "Ignored" (20+) | Offer better support | Low (just do it) |
| **Onboarding** | "Don't understand" (30+) | Test with 5 users | Low-Medium |

**Prioritization Formula:**
```
Gap Score = (Frequency × Impact) ÷ Difficulty

Where:
- Frequency: How many complaints (1-100)
- Impact: User frustration level (1-10)
- Difficulty: Your effort to fix (1-10)

Pick gap with highest score
```

### Step 3: Build Improved Version

- Focus on fixing THE key frustration
- Make it significantly better (not incrementally)
- Capture frustrated users from original
- Position as "better alternative to X"

## Evaluation Criteria

✅ **Good Market Gap Idea If:**
- Original product is successful (proof of demand)
- Gap is clear and significant
- You can build it significantly better
- You have domain expertise
- Existing users are actively frustrated

❌ **Red Flags:**
- Gap is minor/cosmetic
- Original is well-funded giant
- Can't differentiate meaningfully
- Market is declining
- No clear user migration path

## Detailed Walkthrough Example

### Case Study: Building "Better Alternative to Notion"

**Step 1: Find Product with Flaws**
```
Target: Notion (successful but has complaints)
- Revenue: $1B+ valuation
- Users: 30M+
- App Store: 4.7/5 (but 10K+ reviews mentioning issues)
```

**Step 2: Gap Identification (5-Review Method)**
```
Analyzed 200 low-star reviews:

Complaint Categories:
1. "Too slow / performance issues" → 85 mentions
2. "Too complex / overwhelming" → 62 mentions
3. "Offline mode doesn't work" → 48 mentions
4. "Mobile app is bad" → 35 mentions
5. "Expensive for teams" → 28 mentions

Gap Score Calculation:
1. Slow performance: (85 × 9) ÷ 7 = 109 ⭐ HIGHEST
2. Complex UX: (62 × 7) ÷ 5 = 87
3. Offline mode: (48 × 8) ÷ 6 = 64
4. Mobile app: (35 × 6) ÷ 8 = 26
5. Pricing: (28 × 5) ÷ 2 = 70

Decision: Focus on PERFORMANCE (highest score)
```

**Step 3: Validation**
```
Week 1: Landing page test
- Headline: "Notion, but 10x faster"
- Description: "All of Notion's features, instant load times"
- Result: 250 email signups in 3 days ✅

Week 2: User interviews
- Asked 10 frustrated Notion users
- 8/10 said "if it's truly faster, I'd switch immediately"
- 2/10 said "need offline mode too"
→ Validated: Speed is killer differentiator
```

**Step 4: Build MVP**
```
Scope:
- Core Notion features only (docs, databases, no AI yet)
- Optimized for speed (local-first, instant sync)
- Simpler than Notion (cut 50% of features)

Timeline: 6 months
Budget: $0 (use free tiers)
Result: Built "FastNotion" MVP
```

**Step 5: Launch & Results**
```
Month 1:
- Product Hunt launch → #2 of the day
- 500 signups, 50 paying ($9/mo) → $450 MRR

Month 3:
- Word-of-mouth from Notion refugees
- 2,000 users, 300 paying → $2,700 MRR

Month 6:
- Hit $10K MRR
- Featured on Hacker News
- Acquired by competitor for $500K
```

**Key Lessons:**
- Pick ONE gap to fix (speed), not all gaps
- Make it 10x better, not 10% better
- "Alternative to [Big Product]" positioning works
- Frustrated users actively looking to switch

## See main SKILL.md for integration with other skills.
