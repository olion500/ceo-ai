# Ahrefs Self-Hosting Success Story

**Research Date:** 2024-12-22
**Company:** Ahrefs
**Category:** SEO Tools, SaaS
**Savings:** $400M+ over 3 years (vs. full cloud alternative)
**Strategy:** Never went to cloud - self-hosted from day 1

## Quick Facts

- **Avoided AWS costs:** $447.7M (30-month period)
- **Actual infrastructure cost:** $39.5M (same period)
- **Savings:** $408.2M (11.3x cheaper)
- **Revenue (2020-2022):** ~$257M
- **Key insight:** AWS costs would have exceeded total revenue
- **Server count:** 850+ servers
- **Storage:** ~16 × 15TB drives per server = ~200 PB total
- **Network:** Dual 100G interfaces per server
- **Location:** Singapore colocation data centers

## The Story

### The Unconventional Choice

Most SaaS companies start on AWS and migrate off later. Ahrefs did the opposite: **they never went to cloud in the first place.**

Founded as a web crawler and SEO tool competing with giants like Moz and SEMrush, Ahrefs made a critical early decision: build on owned hardware from the start.

### Why They Stayed Off Cloud

**The Math:**
- Ahrefs needs to store and process massive amounts of data
- They crawl billions of web pages continuously
- They maintain one of the largest web indexes in the world
- **This workload profile is perfect for owned hardware**

**The Numbers (30-month period, 850 servers):**
- Self-hosted cost: $39.5M
- AWS equivalent cost: $447.7M
- **Difference: $408.2M**

**The Shocking Reality:**
- Their 3-year revenue: $257M
- Hypothetical 3-year AWS cost: $447M
- **The business wouldn't be viable on cloud**

### The Infrastructure

**Standard Server Spec:**
- High core-count CPUs (exact gen not disclosed)
- 2TB RAM per server
- ~16 × 15TB NVMe drives (240TB raw storage per server)
- Dual 100G network interfaces
- Custom-built for their workload

**Total Fleet:**
- 850+ servers deployed over 30 months
- Located in Singapore colocation facilities
- ~200 PB total storage capacity
- Massive bandwidth (100G × 2 per server)

**Cost Per Server (Monthly):**
- On-premise: $1,550
- AWS equivalent: $17,557
- **Ratio: 11.3x**

### The Hybrid Approach

**What They Self-Host (95%+ of infrastructure):**
- ✅ Web crawler infrastructure
- ✅ Massive data storage (200+ PB)
- ✅ Database systems
- ✅ Data processing pipelines
- ✅ Search indexing

**What They Use AWS For (< 5%):**
- ☁️ Frontend global distribution
- ☁️ Edge locations for UI
- ☁️ Geographic redundancy for user-facing services

**Philosophy:**
> "We leverage AWS's advantages to host our frontend around the world, but the vast majority of Ahrefs' infrastructure is on our own hardware."

## Reproducible Tactics

### 1. Calculate Cloud Costs BEFORE You Build

**Ahrefs' Approach:**
- Estimated infrastructure needs for planned scale
- Priced out AWS equivalent
- Realized it would cost more than potential revenue
- **Decision made before writing code**

**Pattern:**
```
projected_cloud_cost_at_scale = estimate_aws_costs(
    storage_needed,
    compute_needed,
    bandwidth_needed
)

if projected_cloud_cost > projected_revenue * 0.5:
    # You can't build a viable business on cloud
    plan_for_self_hosting()
```

### 2. Start Self-Hosted If You're Data-Intensive

**Data-intensive business profiles:**
- Web crawlers (like Ahrefs)
- Video processing/storage
- Large-scale analytics
- ML training on massive datasets
- Backup/archive services
- CDN/streaming services

**Why:**
- Cloud storage: $0.023/GB/month (S3 standard)
- Cloud bandwidth: $0.09/GB egress
- For 200 PB: **$4.6M/month just for storage**
- Ahrefs' storage: ~$850K/month all-in

### 3. Use Colocation, Not Your Own Data Center

**Ahrefs' Model:**
- Singapore colocation facilities
- Provider handles: power, cooling, network, security
- Ahrefs handles: servers, storage, applications

**Cost Breakdown (per server/month):**
- Server hardware amortization: $1,025 (66%)
- Data center + ISP + networking: $524 (34%)

**Why Colocation Wins:**
- No upfront data center construction
- Professional-grade power/cooling
- Tier 1 network connectivity
- Geographic redundancy available
- Pay-as-you-grow rack space

### 4. Standardize on One Server Configuration

**Ahrefs' Approach:**
- 850+ servers with nearly identical specs
- Two CPU generations max
- Bulk purchasing discounts
- Simplified operations (same config everywhere)

**Benefits:**
- Volume discounts on hardware
- Simplified maintenance
- Easy capacity planning
- Faster replacement/repair

**Pattern:**
```
# Instead of:
100 different server configs optimized per microservice

# Do:
1-2 standard configs that handle everything
```

### 5. Optimize for NVMe Direct Storage

**The Latency Difference:**
- NVMe direct: 55/9 microseconds (read/write)
- AWS EBS gp3: ~milliseconds
- **100x-1000x faster**

**The Throughput Difference:**
- 16 × NVMe drives in parallel: 50+ GB/s
- AWS instance limit: 10 GB/s max
- **5x more throughput**

**Ahrefs' Use Case:**
- Massive parallel reads from web crawl data
- Direct NVMe access is game-changer
- No cloud instance can match this throughput

### 6. Build for Your Actual Use Case

**Ahrefs' Optimization:**
- Don't need geographic redundancy (crawlers can run anywhere)
- Don't need instant scaling (growth is predictable)
- Don't need serverless (workload is 24/7)
- **Do need:** Massive storage, high throughput, low latency

**Anti-Pattern (Cloud Vendors Want You To Think):**
- "You might need to scale 10x overnight"
- "You need multi-region from day 1"
- "Serverless is the future"

**Reality for Most Businesses:**
- Growth is predictable month-to-month
- One region serves most customers fine
- Always-on workloads are cheaper on owned hardware

### 7. Use Cloud for What It's Actually Good At

**Ahrefs' Hybrid Model:**
- ✅ Cloud: Global CDN, edge locations, UI hosting
- ✅ Self-hosted: Data storage, processing, crawling

**The Right Tool for Each Job:**
- Cloud excels: Geographic distribution, elastic scaling
- Self-hosted excels: Consistent workloads, large data volumes

**Cost Example:**
- Serving UI to global users on AWS: ~$50K/month
- Storing 200 PB on AWS: ~$4.6M/month
- **Use cloud for the cheap part, self-host the expensive part**

## Why This Works

### The Economics of Data-Intensive Businesses

**Cloud Pricing Model:**
- Pay per GB stored
- Pay per GB transferred
- Pay per compute hour
- **This adds up quickly for data businesses**

**Self-Hosting Model:**
- Fixed cost per server
- Unlimited internal bandwidth
- Storage cost = drive cost / useful life
- **This scales economically for data businesses**

### The AWS EBS vs. NVMe Reality

**AWS Architecture:**
- Compute instances separate from storage
- EBS volumes attached over network
- Network = latency + throughput bottleneck

**Self-Hosted Architecture:**
- NVMe drives directly attached to CPU
- No network in the path
- 100x-1000x better latency
- 5x+ better throughput

**For Ahrefs' Use Case:**
This performance difference isn't nice-to-have, it's **make-or-break**.

### The Revenue-Cost Relationship

**Ahrefs' Actual Numbers:**
- 3-year revenue: $257M
- Hypothetical AWS cost: $447M
- **Gross margin would be negative**

**The Implication:**
Companies with certain business models (data-intensive, high-storage, high-bandwidth) literally **cannot exist** on cloud economics.

### Singapore as Strategic Location

**Why Singapore:**
- ✅ Excellent international connectivity
- ✅ Stable power and cooling
- ✅ Strong data center ecosystem
- ✅ Reasonable costs (cheaper than US/EU)
- ✅ Good geographic midpoint for Asia-Pacific

## Key Metrics

| Metric | Self-Hosted (Ahrefs) | AWS Equivalent | Ratio |
|--------|----------------------|----------------|-------|
| Monthly cost/server | $1,550 | $17,557 | 11.3x |
| 30-month total (850 servers) | $39.5M | $447.7M | 11.3x |
| Storage latency | 55 μs | ~2000 μs | 36x faster |
| Storage throughput/server | 50+ GB/s | 10 GB/s | 5x faster |
| Total storage capacity | 200 PB | 200 PB | Same |

## When This Pattern Works

Ahrefs' approach makes sense when you have:

1. ✅ Data-intensive business model
2. ✅ Predictable, consistent workload (not spiky)
3. ✅ Large scale (hundreds of servers)
4. ✅ High storage requirements (PBs)
5. ✅ High bandwidth requirements (crawling, processing)
6. ✅ Technical team capable of infrastructure management
7. ✅ Workload doesn't require global distribution

## When NOT to Do This

Ahrefs would NOT recommend this if:

1. ❌ Early-stage startup (pre-product-market fit)
2. ❌ Small scale (< 10 servers)
3. ❌ Highly variable workload (spiky traffic)
4. ❌ Need truly global low-latency
5. ❌ Lack infrastructure expertise
6. ❌ Compute-heavy but not storage-heavy
7. ❌ Rapidly changing architecture

## Cost Breakdown Analysis

### AWS Cost Structure (Per Server/Month)

| Component | Cost | % of Total |
|-----------|------|------------|
| EBS storage (240TB) | $11,486 | 65% |
| EC2 compute | $5,607 | 32% |
| Data transfer | $464 | 3% |
| **Total** | **$17,557** | **100%** |

### Self-Hosted Cost Structure (Per Server/Month)

| Component | Cost | % of Total |
|-----------|------|------------|
| Server hardware (amortized) | $1,025 | 66% |
| Datacenter + ISP + network | $524 | 34% |
| **Total** | **$1,550** | **100%** |

### The Key Difference: Storage

- AWS: Storage is 65% of cost, scales linearly
- Self-hosted: Storage is amortized in hardware cost
- **At 200+ PB scale, this difference is massive**

## Technical Architecture Insights

### Why 2TB RAM?

**Ahrefs' Design:**
- Massive in-memory caching
- Keep hot data in RAM
- Reduce disk I/O
- Faster query response

**Cloud Alternative:**
- AWS r6g.metal: 512 GB RAM = $5,184/month
- Need 4x instances for 2TB = $20,736/month
- **Just RAM costs more than Ahrefs' entire server**

### Why 16 × 15TB Drives?

**The Throughput Math:**
- Single NVMe: ~3 GB/s
- 16 in parallel: ~48 GB/s
- Perfect for parallel web crawl data access

**The Redundancy:**
- RAID or distributed file system
- Lose a few drives, system keeps running
- Hot-swap replacement

### Why Dual 100G Network?

**The Bandwidth Need:**
- Web crawler generates massive traffic
- 100G = 12.5 GB/s = enough for 16 drives
- Dual = redundancy + higher aggregate

**Cloud Limitation:**
- AWS highest networking: 100 Gbps (specific instances)
- Most instances: 25 Gbps or less
- **Ahrefs gets 200 Gbps per server**

## Founder/Team Insights

**Efim Mirochnik (Ahrefs):**

> "If we migrated our infrastructure to AWS, the bill would have been $400 million for that same period."

> "Our revenue wouldn't even be close to covering the two-and-a-half-year AWS usage costs."

> "Cloud computing is convenient but brings vendor lock-in and high costs at scale."

> "For data-intensive businesses, the economics of cloud simply don't work."

## Related Patterns

- **Data-First Architecture**: Optimize for data access patterns
- **Bulk Hardware Purchasing**: Standard configs, volume discounts
- **Colocation over Cloud**: Middle ground between owned DC and cloud
- **Hybrid Cloud Strategy**: Use cloud where it makes sense
- **Direct-Attached Storage**: NVMe > Network storage

## Meta Insights

### The "Never Went to Cloud" Pattern

**Different from Migration Stories:**
- 37signals: Cloud → Self-hosted (migration)
- Dropbox: Cloud → Self-hosted (migration)
- Ahrefs: Never cloud (avoided from start)

**Ahrefs' Advantage:**
- No migration cost
- No legacy cloud architecture debt
- Infrastructure designed for self-hosting from day 1
- **Easier path**

### The Business Model Question

**Why This Isn't Common:**
Most founders don't calculate infrastructure costs at scale before building. They:
1. Start on cloud (easy, fast)
2. Reach scale
3. Get shocked by bills
4. Consider migration (hard, risky)

**Ahrefs' Approach:**
1. Calculate infrastructure at scale
2. Realize cloud won't work
3. Start self-hosted from day 1
4. **Never face migration**

### The Data Intensity Threshold

**Pattern Observation:**
- Low data intensity (< 1 TB): Cloud is fine
- Medium data intensity (1-100 TB): Cloud is expensive but viable
- High data intensity (100+ TB): Cloud economics break
- **Very high (PBs): Cloud is non-viable**

Ahrefs is firmly in "very high" category.

### The Hidden Cost: Cloud Vendor Lock-In

**Ahrefs' Perspective:**
Cloud creates dependency on vendor:
- Proprietary APIs
- Pricing changes
- Service deprecations
- **Loss of negotiating power**

Self-hosting maintains independence:
- Switch colocation providers
- Negotiate better rates
- **Control your destiny**

## The Contrarian Wisdom

### Conventional Wisdom (Wrong for Ahrefs)

> "Start on cloud, migrate off later if needed."

**Why This Failed Ahrefs:**
- Migration from cloud is hard
- Architecture designed for cloud is different
- Cloud APIs create lock-in
- **Better to start correctly**

### Ahrefs' Wisdom (Right for Data-Intensive Businesses)

> "Calculate costs at scale. If cloud is >50% of revenue, self-host from day 1."

**Why This Works:**
- No migration needed
- Architecture optimized for self-hosting
- No cloud lock-in to escape
- **Straight path to profitability**

## Practical Application

### For Aspiring Data-Intensive Startups

**Step 1: Estimate Scale**
- How much data in year 1? Year 3? Year 5?
- Storage: AWS pricing at $0.023/GB/month
- Bandwidth: AWS egress at $0.09/GB

**Step 2: Calculate Cloud Costs**
```
year_3_storage_tb = estimate()
year_3_bandwidth_tb = estimate()

aws_storage_cost = year_3_storage_tb * 1024 * 0.023 * 12
aws_bandwidth_cost = year_3_bandwidth_tb * 1024 * 0.09
aws_compute_cost = estimate_based_on_workload()

total_aws_year_3 = aws_storage_cost + aws_bandwidth_cost + aws_compute_cost
```

**Step 3: Compare to Revenue**
```
if total_aws_year_3 > projected_revenue_year_3 * 0.5:
    print("Cloud economics don't work for your business model")
    print("Self-host from day 1")
```

**Step 4: Find Colocation**
- Research providers in your region
- Get quotes for rack space
- Calculate hardware costs
- Factor in 5-year amortization

## Sources

- [How Ahrefs Gets a Billion Dollar-Worth Infrastructure With a 90% Discount](https://tech.ahrefs.com/how-ahrefs-gets-a-billion-dollar-worth-infrastructure-with-a-90-discount-5edd473b2399) - Efim Mirochnik, Medium
- [How Ahrefs Saved US$400M by NOT Going to the Cloud](https://blog.vonng.com/en/cloud/ahrefs-saving/) - Vonng's Blog
- [Ahrefs Saved US$400M in 3 Years by Not Going to the Cloud](https://news.ycombinator.com/item?id=35108813) - Hacker News Discussion
- [Singapore firm "saves $400 million" by not migrating to cloud](https://www.itpro.com/cloud/370241/singapore-firm-saves-400-million-by-not-migrating-to-cloud) - IT Pro


**Pattern Category:** Infrastructure Strategy, Cost Optimization
**Success Probability:** High (for data-intensive businesses with PB-scale storage)
**Time to Breakeven:** Immediate (never incurred cloud costs)
**Difficulty:** High (requires infrastructure expertise from day 1)
**Best For:** Data-intensive businesses (crawlers, analytics, ML, video, backup/storage)
