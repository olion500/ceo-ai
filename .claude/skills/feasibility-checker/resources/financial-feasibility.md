# Financial Feasibility Assessment

Detailed guide for evaluating financial viability and costs.

## Overview

Determine if you can afford to build and operate this business with your current financial situation.

## Initial Development Costs

### One-time Expenses
- Domain registration ($10-15/year)
- Design/branding (optional, $0-500)
- Development tools ($0-100/month)
- Legal/business setup (varies)

### Infrastructure Setup Example

**Typical SaaS MVP Stack Costs:**

| Service | Free Tier | Paid Start | What You Get (Free) |
|---------|-----------|------------|---------------------|
| **Hosting** |
| Vercel | ✅ Free | $20/mo | Unlimited sites, 100GB bandwidth |
| Netlify | ✅ Free | $19/mo | 100GB bandwidth, 300 build min |
| **Database** |
| Supabase | ✅ Free | $25/mo | 500MB storage, 2GB transfer, pause after 7 days inactive |
| PlanetScale | ✅ Free | $29/mo | 5GB storage, 1B row reads/mo |
| Neon | ✅ Free | $19/mo | 3GB storage, always-on |
| **Auth** |
| Clerk | ✅ Free | $25/mo | 10K MAU (Monthly Active Users) |
| Auth0 | ✅ Free | $35/mo | 7.5K MAU |
| Supabase Auth | ✅ Free | Included | Unlimited (with DB) |
| **Email** |
| Resend | ✅ Free | $20/mo | 3K emails/month, 100/day |
| SendGrid | ✅ Free | $20/mo | 100 emails/day |
| **Payments** |
| Stripe | ✅ Free | 2.9% + $0.30 | No monthly fee, per-transaction only |

**Total MVP Cost: $0-20/month** (can start completely free)

## Monthly Operating Costs

**Real Example: SaaS Tool at Different Scales**

### Phase 1: MVP (0-100 users)
```
Vercel:        $0 (free tier)
Supabase:      $0 (free tier)
Resend:        $0 (free tier, <3K emails/month)
Stripe:        $0 + 2.9% per transaction
Analytics:     $0 (Vercel Analytics free tier)
---
TOTAL:         $0/month + transaction fees
```

### Phase 2: Early Growth (100-1,000 users)
```
Vercel:        $20 (need more bandwidth)
Supabase:      $25 (need always-on + more storage)
Resend:        $20 (sending 5K+ emails/month)
Clerk:         $25 (over 10K MAU)
Stripe:        2.9% + $0.30 per transaction
---
TOTAL:         ~$90/month + transaction fees
Revenue needed to break even: $90 ÷ 0.3 = $300/month minimum
```

### Phase 3: Scaling (1,000-10,000 users)
```
Vercel Pro:    $20
Supabase Pro:  $25
Resend Pro:    $80 (30K+ emails/month)
Clerk:         $100 (50K MAU)
CDN:           $20 (Cloudflare Images)
Monitoring:    $25 (Better Stack)
---
TOTAL:         ~$270/month + transaction fees
Revenue needed: $900/month minimum (3x buffer)
```

## Free Tier Strategy & Upgrade Triggers

### Upgrade Decision Table

| Service | Free Limit | Upgrade Trigger | When to Upgrade | Cost Impact |
|---------|------------|-----------------|-----------------|-------------|
| **Vercel** | 100GB bandwidth | >80GB/month | ~500-1K users visiting regularly | +$20/mo |
| **Supabase** | 500MB storage | DB size >400MB OR need 24/7 uptime | ~200-500 users with data | +$25/mo |
| **PlanetScale** | 5GB storage | >4GB data | ~1K-2K users | +$29/mo |
| **Clerk** | 10K MAU | >8K active users/month | Growing user base | +$25/mo |
| **Resend** | 3K emails/month | Sending >2.5K/month | ~300-500 active users | +$20/mo |
| **Vercel Analytics** | 2.5K events | >2K events/month | Significant traffic | +$10/mo |

### Decision Framework

**Should I upgrade?**
```
IF (current_usage > 80% of limit) AND (revenue > 3x upgrade_cost):
  → Upgrade now ✅

IF (current_usage > 80% of limit) AND (revenue < 3x upgrade_cost):
  → Optimize usage first OR accept downtime risk ⚠️

IF (expecting 2x growth in 30 days):
  → Upgrade proactively ✅
```

**Example:**
```
Resend: Using 2,800/3,000 emails (93% of limit)
Monthly revenue: $200
Upgrade cost: $20/month
Decision: $200 > ($20 × 3) = $200 > $60 → Upgrade ✅
```

## Personal Runway Calculation

```
Runway (months) = Savings / (Living Expenses - Income)
```

**Risk levels:**
- <3 months: High risk, need fast revenue
- 3-6 months: Medium risk, aggressive timeline
- 6-12 months: Low risk, comfortable pace
- >12 months: Very low risk, can iterate freely

## Revenue Requirements

Calculate break-even:
- Monthly costs (personal + business)
- Required revenue target
- Customers needed at different price points
- Time to break-even estimate

## Cost Modeling

### Scaling Cost Projection

**Example: B2B SaaS Tool ($29/month per user)**

| Scale | Users | Monthly Costs | Revenue (@$29/user) | Profit Margin | Notes |
|-------|-------|---------------|---------------------|---------------|-------|
| **MVP** | 10 | $0 | $290 | 100% | All free tiers |
| **Early** | 100 | $90 | $2,900 | 97% | First paid services |
| **Growth** | 500 | $270 | $14,500 | 98% | Scale efficiently |
| **Scale** | 2,000 | $600 | $58,000 | 99% | High margin |
| **Enterprise** | 10,000 | $2,500 | $290,000 | 99% | Dedicated support needed |

**Cost Inflection Points:**
- **100 users**: First paid tier upgrades (~$90/month)
- **1,000 users**: Need better monitoring/support tools (~$270/month)
- **10,000 users**: May need dedicated infrastructure or support team

**Key Insight:** SaaS infrastructure costs scale sub-linearly (10x users ≠ 10x costs)

---

**See main SKILL.md for scoring framework and integration with other assessments.**
