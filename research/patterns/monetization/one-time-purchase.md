---
title: One-Time Purchase Model
created: 2025-12-16
updated: 2025-12-16
tags: [pattern]
category: Research
type: Pattern
---
# One-Time Purchase Model

**Category:** monetization
**Success Rate:** High for developer tools, Medium for general SaaS
**Time Investment:** Same as subscription (payment integration)
**Difficulty:** Easy (simpler than subscriptions)

## What Is This Pattern?

Charge a one-time fee for lifetime access instead of monthly/annual subscriptions. Users pay once, get access forever.

## How It Works

1. **Set Fair Price**: Price based on value delivered ($9-$199 typical)
2. **Promise Lifetime Access**: No recurring fees
3. **Include Updates**: Future updates included (goodwill)
4. **Optional**: Paid major version upgrades (v1 → v2)
5. **Scale Through Volume**: More customers, not recurring revenue

## Real Examples (Ranked by Success)

### 1. TypingMind - Tony Dinh ($83K MRR one-time purchases)
- **Context**: ChatGPT enhancement tool
- **Execution**:
  - Started $9 one-time purchase
  - Increased to $39 as features added
  - Lifetime access + updates included
  - High volume sales model
- **Results**: $22K in 7 days, now $83K/month (sustained one-time purchases)
- **Key Insight**: Lower friction than subscription for tool category

### 2. ShipFast - Marc Lou ($50K MRR, $1.2M lifetime)
- **Context**: Next.js boilerplate for developers
- **Execution**:
  - One-time purchase model
  - Lifetime access to boilerplate + updates
  - $4K/day revenue from new purchases
- **Results**: $1.2M+ lifetime revenue, sustainable
- **Key Insight**: Developers prefer one-time for tools they'll use repeatedly

### 3. Vampire Survivors - Luca Galante (£40M net worth)
- **Context**: Indie game
- **Execution**:
  - $2.99 initial (bare bones)
  - $4.99 after content additions
  - One-time purchase + DLC model
- **Results**: 5-10M+ copies sold, £40M net worth
- **Key Insight**: Volume at low price point > subscriptions for games

### 4. Online Solitaire - Holger Sindbaek (Attempted, then pivoted)
- **Context**: Web solitaire game
- **Execution**:
  - Tried subscription: Only 5% of revenue
  - Pivoted to ads: 95% of revenue
  - Quote: "People don't want to pay for solitaire games"
- **Results**: Ad model won, subscription failed
- **Key Insight**: Know what users will/won't pay for

## Why This Works

**Lower Friction**:
- Single purchase decision vs recurring commitment
- Psychological: "Buy once, own forever"
- No cancellation anxiety
- Impulse purchase easier

**Customer Alignment**:
- No feeling of being "milked" monthly
- Appreciation for fair one-time pricing
- Trust in business model

**Marketing Simplicity**:
- Simpler messaging (price, not pricing tiers)
- Easier word-of-mouth ("costs $39")
- No complex funnel optimization

**Works for Certain Categories**:
- Developer tools (one-time setup)
- Templates/boilerplates (use repeatedly)
- Games (entertainment purchase)
- Productivity tools (use but don't consume)

## Drawbacks

**Revenue Predictability**:
- No MRR (Monthly Recurring Revenue)
- Must constantly acquire new customers
- Revenue drops if acquisition slows

**Lower LTV for Some Categories**:
- SaaS with ongoing costs (hosting, APIs)
- Continuous service delivery
- High support burden

**Valuation Impact**:
- VCs prefer recurring revenue
- Lower multiples for one-time vs subscription
- Not ideal if seeking funding

## Prerequisites

- **Skills Required**: Standard payment integration (Stripe, Gumroad)
- **Time Required**: Same as subscription setup
- **Capital Required**: Minimal (payment processing only)
- **Other Requirements**:
  - Product category where one-time makes sense
  - Ability to acquire customers consistently
  - Low ongoing operational costs

## Common Mistakes

1. **Mistake**: One-time purchase for high-cost ongoing service
   - **Why It Fails**: Can't sustain service with one-time revenue
   - **How to Avoid**: Match model to operational costs

2. **Mistake**: Pricing too low initially
   - **Why It Fails**: Hard to raise prices, leaves money on table
   - **How to Avoid**: Price based on value, can always discount

3. **Mistake**: No paid upgrades path (v2, v3)
   - **Why It Fails**: Eventually run out of new customers
   - **How to Avoid**: Plan for major version paid upgrades

4. **Mistake**: Applying to wrong category
   - **Why It Fails**: SaaS with APIs/hosting costs unsustainable
   - **How to Avoid**: Subscription for ongoing costs, one-time for static tools

## When to Use This Pattern

✅ **Good Fit When:**
- **Developer tools**: Boilerplates, templates, utilities
- **Digital products**: Ebooks, courses, assets
- **Games**: Indie games, mobile games
- **One-time setup tools**: Productivity apps without ongoing costs
- **Low ongoing costs**: No expensive APIs/infrastructure
- **Clear value delivery**: Solve problem immediately

❌ **Bad Fit When:**
- **High API costs**: OpenAI, data providers
- **Expensive hosting**: Video streaming, large storage
- **Continuous service**: Email providers, analytics SaaS
- **Enterprise B2B**: Expect ongoing support/updates
- **Community/social**: Ongoing moderation needed

## Pricing Strategies

**Developer Tools**:
- $19-$99: Simple utilities
- $99-$299: Comprehensive boilerplates
- $299-$999: Professional frameworks

**Digital Products**:
- $9-$29: Ebooks, small templates
- $29-$99: Course bundles
- $99-$299: Comprehensive resources

**Games**:
- $2.99-$9.99: Indie games
- $9.99-$29.99: Premium indie
- DLC for ongoing revenue

**Productivity Tools**:
- $9-$49: Simple tools
- $49-$199: Professional tools

## Evolution Strategies

**Start One-Time, Add Subscription Later**:
- Notion started one-time, added Teams subscription
- Offers both models (personal vs team)

**Grandfather Existing Customers**:
- Lifetime deals for early adopters
- New customers pay subscription
- Rewards early believers

**Major Version Upgrades**:
- v1 purchased once
- v2 requires new purchase (discounted for v1 owners)
- Keeps revenue flowing from improvements

## Related Patterns

- **Monetization**: [subscription-model](./subscription-model.md) - Compare trade-offs
- **MVP**: [lightning-fast-shipping](../mvp-building/lightning-fast-shipping.md) - Get to revenue fast
- **Distribution**: [product-hunt-launch](../distribution/product-hunt.md) - One-time launch drives one-time sales

## Key Metrics

**Instead of MRR, track**:
- Daily/Weekly/Monthly revenue (not recurring)
- Customer acquisition cost (CAC)
- Average order value (AOV)
- Repeat purchase rate (if applicable)
- New customer volume

## Sources

- Tony Dinh TypingMind: https://news.tonydinh.com/p/my-solopreneur-story-zero-to-45kmo (accessed 2024-12-14)
- Marc Lou ShipFast: https://newsletter.marclou.com/p/scratch-your-own-itch (accessed 2024-12-14)
- Online Solitaire: https://www.indiehackers.com/post/how-i-grew-a-simple-solitaire-game-to-10k-mrr (accessed 2024-12-14)
- Vampire Survivors: Various sources (accessed 2024-12-10)
