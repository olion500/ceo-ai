# 37signals Cloud Exit Success Story

**Research Date:** 2024-12-22
**Company:** 37signals (Basecamp, HEY)
**Category:** SaaS, Productivity Software
**Savings:** $10M+ over 5 years
**Strategy:** AWS → Self-hosted Dell hardware

## Quick Facts

- **Annual AWS spend before:** $3.2M
- **Annual spend after (2024):** $1.3M
- **Annual savings:** ~$2M/year
- **Hardware investment:** $700K (recouped by end of 2023)
- **Team size change:** None (same team manages everything)
- **Applications moved:** 7 apps including HEY and Basecamp
- **Timeline:** Started 2022, completed summer 2023
- **Company size:** ~80 employees
- **Revenue:** ~$100M ARR

## The Story

### The Wake-Up Call

In 2022, 37signals was spending $3.2 million annually on AWS cloud services. David Heinemeier Hansson (DHH), CTO and co-founder, started questioning whether this made economic sense for a company with stable, predictable workloads.

The key insight: **When your cloud bill becomes "substantial," it's time to do the math on buying your own hardware.**

### The Migration

**Phase 1: Compute (2022-2023)**
- Moved 7 cloud applications off AWS
- Invested ~$700K in Dell hardware
- Placed servers in existing data center racks (no new facility needed)
- Completed by summer 2023

**Phase 2: Storage (2024-2025)**
- Current: ~10 petabytes on AWS S3 across multiple regions
- Future: 18 petabytes on Pure Storage arrays
  - Upfront cost: $1.5M
  - Annual operating cost: $200K
  - Compare to: One year of S3 costs
- Expected completion: Summer 2025

### The Results

**First Full Year (2024):**
- Reduced AWS bill from $3.2M → $1.3M
- Savings: $1.9M in first clean year
- Total projected: **$10M+ over 5 years**

**Operational Impact:**
- **Zero** additional headcount needed
- Same team manages both cloud and on-premise
- "No hidden dragons" of additional workload
- Ongoing maintenance similar to cloud responsibilities

**Performance Benefits:**
- Faster computers (custom spec'd hardware)
- Much more storage capacity
- Better control over infrastructure

## Reproducible Tactics

### 1. Calculate Your Break-Even Point

```
If (annual_cloud_bill > $200K):
    hardware_cost = cloud_bill * 0.5  # rough estimate
    if hardware_cost < (cloud_bill * 3):
        # You'll break even in < 3 years
        consider_self_hosting()
```

**37signals' Math:**
- $3.2M/year cloud → $700K hardware
- Break-even: ~4 months
- 5-year savings: $10M+

### 2. Start with Compute, Then Storage

**Why this order:**
- Compute migration is simpler (stateless workloads)
- Learn operations while cloud storage provides safety net
- Storage migration is complex but saves most money long-term

**37signals' Approach:**
1. Move applications first (2022-2023)
2. Validate operations and team capacity
3. Tackle storage when confident (2024-2025)

### 3. Use Existing Infrastructure

**Key cost saver:**
- 37signals fit new hardware into existing data center racks
- No new facility costs
- No power upgrades needed
- Savings exceeded initial $7M estimate → $10M+

**Pattern:**
```
IF you have existing data center capacity:
    savings = (cloud_cost - hardware_cost) * years
ELSE:
    savings = (cloud_cost - hardware_cost - rack_rental) * years
    # Still profitable if cloud_bill > $500K/year
```

### 4. Don't Hire for the Migration

**37signals' Key Insight:**
- Same team that managed cloud infrastructure can manage on-premise
- Skills transfer: monitoring, scaling, debugging
- Cloud management time ≈ On-premise management time

**Reality Check:**
- Initial setup: ~40 hours
- Monthly maintenance: ~30 minutes for HA systems
- Weekly tasks: ~10 minutes (backup validation, query logs)

### 5. Pick Your Cloud Battles

**37signals' Hybrid Model:**
- ✅ Self-host: Core applications, databases, storage
- ☁️ Stay on cloud: Global CDN, edge locations, DNS
- 💡 Insight: Use cloud for what it's actually good at (global distribution)

### 6. Wait for Long-Term Contracts to Expire

**Timing Strategy:**
- Don't break contracts early (penalties)
- Plan migration to complete as contracts roll off
- 37signals: Hardware paid off by time contracts ended

### 7. Communicate the Journey Publicly

**DHH's Strategy:**
- Blog posts documenting decision and progress
- Transparent cost breakdowns
- Technical details of migration
- Response to criticism

**Benefits:**
- Attracts like-minded customers
- Recruiting tool ("we run our own infrastructure")
- Thought leadership positioning
- Community support and advice

## Why This Works

### Economic Reality

**Cloud Pricing Inversion:**
- Cloud made sense in 2010s (cheap, pay-as-you-go)
- 2020s: Prices increased while hardware got cheaper
- AWS db.r6g.xlarge (4 vCPU, 32GB RAM): $328/month
- Hetzner dedicated (32 cores, 256GB RAM): $220/month
- **Ratio: 10x+ more resources for less money**

### The 37signals Profile

Cloud exit makes sense when you have:
1. ✅ Predictable workloads (not spiky traffic)
2. ✅ Substantial cloud spend ($200K+ annually)
3. ✅ In-house technical talent
4. ✅ Mature product (not rapid experimentation phase)
5. ✅ Geographic concentration (not global from day 1)

### What Changed from 2015 to 2023

**Then (Dropbox era):**
- Custom infrastructure required massive engineering effort
- "Magic Pocket" took years to build
- Only viable for huge companies

**Now (37signals era):**
- Commodity hardware is incredibly powerful
- Open-source tooling is mature (K8s, monitoring, etc.)
- Colocation providers offer turnkey solutions
- **Mid-sized companies can do this**

## Common Objections (and DHH's Responses)

### "But what about opportunity cost?"

**Objection:** Engineers should build features, not manage infrastructure.

**DHH's Response:**
- Same engineers manage cloud infrastructure already
- Time investment is roughly equal
- $2M/year savings >>> cost of a few engineers
- Infrastructure work is valuable engineering experience

### "But what about scaling?"

**Objection:** Cloud provides unlimited scale on-demand.

**DHH's Response:**
- Most companies don't need unlimited scale
- 37signals serves millions of users on owned hardware
- When you do scale, buy more servers (cheaper than cloud anyway)
- Predictable growth = predictable hardware purchases

### "But what about redundancy?"

**Objection:** Cloud gives you geographic redundancy automatically.

**DHH's Response:**
- Dual data centers with Pure Storage arrays
- Same HA setup they'd need to configure in cloud anyway
- Physical redundancy at lower cost
- Many cloud services run in single AZ by default

### "You're just big enough to do this"

**Objection:** This only works for companies at 37signals' scale.

**DHH's Response:**
- Break-even point is ~$200K/year cloud spend
- Many companies reach this with <20 employees
- Hetzner dedicated servers start at $40/month
- Smaller companies might save even higher percentage

## Key Metrics

| Metric | Before (Cloud) | After (Self-Hosted) | Change |
|--------|----------------|---------------------|--------|
| Annual infrastructure cost | $3.2M | $1.3M | -59% |
| Team size | Same | Same | 0% |
| Storage capacity | 10 PB (S3) | 18 PB (Pure) | +80% |
| Time to provision | Minutes | Hours | Acceptable |
| Geographic distribution | Global | US-focused | Trade-off |

## When NOT to Do This

37signals would NOT recommend cloud exit if:

1. ❌ Early-stage startup (< product-market fit)
2. ❌ Spiky, unpredictable traffic
3. ❌ Truly global audience from day 1
4. ❌ Cloud spend < $200K/year
5. ❌ No in-house infrastructure experience
6. ❌ Regulated industry requiring cloud compliance
7. ❌ Rapidly changing architecture (lots of experiments)

## Founder Insights (DHH Quotes)

> "The cloud is not a religious choice. It's an economic calculation."

> "We're not anti-cloud. We're pro-math."

> "At $3.2M/year, we're renting very expensive computers. At $700K, we own extremely powerful computers."

> "The team managing everything is still the same. This idea that you need a massive ops team to run your own hardware is cloud vendor FUD."

> "2024 was our first clean year of savings. We brought the cloud bill down from $3.2M to $1.3M. That's almost $2M/year saved."

> "If you have existing data center racks and power, the savings are even better than we projected."

## Related Patterns

- **Build-in-Public**: DHH documented entire journey publicly
- **Cost Optimization as Competitive Advantage**: Lower costs = higher margins or lower prices
- **Hybrid Cloud Strategy**: Use cloud where it makes sense, self-host where it doesn't
- **Long-term Thinking**: Optimized for 5-year costs, not next quarter
- **Technical Leverage**: Small team managing large infrastructure

## Meta Insights

### The Pendulum Swings

**2000s:** Everyone buys servers (only option)
**2010s:** Everyone moves to cloud (better option for most)
**2020s:** Large companies move back to owned hardware (cloud got expensive)

This isn't "cloud is bad" — it's "cloud pricing has reached a point where the old model makes sense again for mature companies."

### The Hidden Benefit: Recruiting

37signals found unexpected benefit: engineers want to work on "real" infrastructure.

- Running your own hardware is a differentiator
- Attracts systems-oriented engineers
- Provides valuable learning opportunities
- Cloud-only experience is becoming commodity

### The Real Innovation

**It's not the technology** (hardware, colocation, etc.)

**It's the economic analysis:**
- Transparently calculating break-even
- Publicly sharing the numbers
- Challenging the "cloud is always cheaper" narrative
- Proving mid-sized companies can do this

## Sources

- [Our cloud-exit savings will now top ten million over five years](https://world.hey.com/dhh/our-cloud-exit-savings-will-now-top-ten-million-over-five-years-c7d9b5bd) - DHH, Oct 2024
- [Developer pockets $2M in savings from going cloud-free](https://www.theregister.com/2024/10/21/37signals_aws_savings/) - The Register, Oct 2024
- [37signals on-prem migration to save millions](https://www.theregister.com/2025/05/09/37signals_cloud_repatriation_storage_savings/) - The Register, May 2025
- [Our cloud spend in 2022](https://dev.37signals.com/our-cloud-spend-in-2022/) - 37signals Dev, 2022


**Pattern Category:** Cost Optimization, Infrastructure Strategy
**Success Probability:** High (for companies with >$200K annual cloud spend)
**Time to Breakeven:** 3-12 months
**Difficulty:** Medium (requires infrastructure expertise)
**Best For:** Mature SaaS companies with predictable workloads
