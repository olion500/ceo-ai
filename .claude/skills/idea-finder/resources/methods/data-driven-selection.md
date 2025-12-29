# Data-Driven Selection Method

**Success Rate: 60%** - Good for analytical minds

## Overview

Use market data to identify opportunities. Choose proven markets with underserved niches.

## How It Works

### Step 1: Analyze Market Data

**Specific Data Sources & How to Use Them:**

**1. Google Trends (Free)**
```
URL: trends.google.com
How to use:
- Search "[product category]" (e.g., "project management")
- Check 5-year trend → growing, stable, or declining?
- Compare related terms (e.g., "asana" vs "linear" vs "notion")
- Look for "Breakout" queries (rising fast)

What to look for:
- Rising trend = good opportunity
- Stable high volume = proven market
- Declining = avoid unless you have unique angle
```

**2. Similar Web / Ahrefs (Paid, ~$100/mo)**
```
What you get:
- Competitor website traffic
- Top traffic sources
- Keyword rankings
- Backlink data

How to use:
- Search top 5 competitors
- Check monthly visits → estimate $$ (visits × 0.5% × avg price)
- See traffic sources → know where to market
- Find content gaps → your differentiation
```

**3. Reddit/Subreddit Stats**
```
URL: subredditstats.com
How to use:
- Search "[your niche]" subreddits
- Check subscriber count + growth rate
- Read top posts for pain points

Example:
- /r/productivity: 300K subs, +20% YoY → growing market
- Top complaints: "Notion too complex", "Todoist too simple"
```

**4. App Store Intelligence (App Annie, Sensor Tower)**
```
What you get:
- App download estimates
- Revenue estimates (for paid apps)
- Keyword rankings
- Review sentiment

How to use:
- Search "[category] apps"
- Find apps with 10K-100K downloads (sweet spot)
- Read 1-star reviews → pain points to solve
```

**5. Search Volume Data (Google Keyword Planner, Ubersuggest)**
```
How to use:
- Enter "[problem] solution" keywords
- Check monthly search volume
- Look for 1K-10K searches → not too niche, not too competitive

Example:
- "markdown editor": 5K searches/mo → viable
- "markdown editor for developers": 500/mo → too niche
```

### Step 2: Create Ranking Algorithm

**Formula:** `Opportunity Score = Demand Score (0-10) × Achievability Score (0-10)`

**Demand Score Calculation:**
```
Factor                  | Weight | How to Score
------------------------|--------|-------------
Google Trends (growth)  | 30%    | Rising=10, Stable=7, Declining=3
Search volume          | 30%    | >10K/mo=10, 1-10K=7, <1K=3
Competitor revenue     | 40%    | $100K+=10, $10-100K=7, <$10K=3
```

**Achievability Score Calculation:**
```
Factor                  | Weight | How to Score
------------------------|--------|-------------
Your skill match       | 40%    | Expert=10, Intermediate=7, Beginner=3
MVP complexity        | 30%    | Simple=10, Medium=7, Complex=3
Competition level     | 30%    | 3-5 competitors=10, 10+=5, None=3
```

**Real Example: Markdown Note-Taking App**
```
DEMAND SCORE:
- Google Trends: Stable high volume (7 × 0.3) = 2.1
- Search volume: "markdown editor" 5K/mo (7 × 0.3) = 2.1
- Competitor revenue: Obsidian ~$10M ARR (10 × 0.4) = 4.0
→ Demand Score = 8.2/10

ACHIEVABILITY SCORE:
- Skill match: You know React + Electron (10 × 0.4) = 4.0
- MVP complexity: Text editor is medium complexity (7 × 0.3) = 2.1
- Competition: 5 major competitors (10 × 0.3) = 3.0
→ Achievability Score = 9.1/10

OPPORTUNITY SCORE = 8.2 × 9.1 = 74.6/100

Interpretation:
- 80-100: Exceptional opportunity
- 60-79: Strong opportunity ← (Example: 74.6)
- 40-59: Moderate opportunity
- <40: Not recommended
```

**Decision: PURSUE** (with differentiation strategy)

### Step 3: Choose Proven Market with Niche

- Pick market with validated demand
- Find underserved segment or niche
- Build better/faster/cheaper version

## Evaluation Criteria

✅ **Good Data-Driven Idea If:**
- Market data shows strong demand
- Multiple competitors exist (validation!)
- You can differentiate clearly
- You have relevant skills
- Entry barrier is manageable

❌ **Red Flags:**
- Data shows declining market
- No clear differentiation possible
- Requires extensive expertise you lack
- Too capital-intensive

## Real Success Examples

**Online Solitaire** - Holger scraped App Annie data → $10K MRR

## See main SKILL.md for integration with other skills.
