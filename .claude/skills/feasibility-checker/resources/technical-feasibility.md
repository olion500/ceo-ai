# Technical Feasibility Assessment

Detailed guide for evaluating technical execution capability.

## Overview

Assess whether you can technically build this project with your current skills and available technology.

## Skills Inventory

### Programming Languages Audit

**Example: Building a SaaS Analytics Dashboard**
```
Required Languages:
- TypeScript (Frontend + Backend) → Your level: 7/10 ✅
- SQL (Complex queries) → Your level: 4/10 ⚠️
- Python (Data processing) → Your level: 2/10 ❌

Gap Analysis:
- TypeScript: No gap, proceed
- SQL: Medium gap, 2-3 weeks learning → Acceptable
- Python: Large gap → DECISION: Use TypeScript + library instead
```

### Skill Gap Calculation Formula

```
Gap Score = (Required Level - Your Level) × Component Criticality

Where:
- Criticality: Core Feature (3x), Important (2x), Nice-to-Have (1x)
- Gap Score < 10: Proceed
- Gap Score 10-20: Learn first (budget time)
- Gap Score > 20: De-scope or outsource
```

**Real Example:**
```
Feature: Real-time collaborative editor
Required: WebSocket expertise (8/10), Your level: 2/10
Criticality: Core Feature (3x)
Gap Score = (8-2) × 3 = 18 → Learn first OR use managed service (Pusher/Ably)
```

### Frameworks & Tools

**Decision Tree:**
```
Need framework for [X]?
├─ Do you know it well? (7/10+)
│  └─ YES → Use it ✅
└─ NO → Is it industry standard?
   ├─ YES → Is learning time < 2 weeks?
   │  ├─ YES → Learn it, proceed ✅
   │  └─ NO → Use familiar alternative ⚠️
   └─ NO → Don't use, find standard solution ❌
```

### Infrastructure & DevOps

**Complexity Matrix:**
```
Task                  | DIY Complexity | Managed Service      | Recommendation
----------------------|----------------|----------------------|----------------
User auth             | 8/10           | Auth0/Clerk (2/10)   | Use managed
File uploads          | 6/10           | S3 + Presigned (3/10)| Use managed
Database hosting      | 7/10           | Supabase/PlanetScale | Use managed
Email sending         | 5/10           | SendGrid/Resend      | Use managed
Cron jobs             | 4/10           | Vercel Cron (2/10)   | Can DIY or managed
```

## Requirements Matrix

**Example Matrix for "Team Collaboration Tool":**

| Skill Needed | Required | Your Level | Gap | Learning Time | Blocker? | Action |
|--------------|----------|------------|-----|---------------|----------|---------|
| React | 7/10 | 8/10 | None | - | ❌ | Proceed |
| Node.js | 6/10 | 7/10 | None | - | ❌ | Proceed |
| WebSocket | 8/10 | 3/10 | Large | 3-4 weeks | ⚠️ | Use Pusher |
| PostgreSQL | 7/10 | 5/10 | Small | 1 week | ❌ | Learn basics |
| AWS Lambda | 6/10 | 2/10 | Medium | 2 weeks | ⚠️ | Use Vercel |
| Redis | 5/10 | 1/10 | Large | 2-3 weeks | ❌ | Optional, defer |

**Decision:** Proceed with managed services for WebSocket and serverless. Total learning time: ~1 week for PostgreSQL.

## Technical Complexity Scoring

Rate each component (1-10):
- Frontend complexity
- Backend complexity
- Database design
- Third-party integrations
- Special features (real-time, ML, etc.)

**Risk Levels:**
- Low: Complexity < Your Expertise
- Medium: Complexity ≈ Your Expertise
- High: Complexity > Expertise by 2-3
- Critical: Complexity > Expertise by 4+

## Tech Stack Validation

### Tech Stack Decision Tree

```
Building [Feature/Product]?
│
├─ Is this core to your value proposition?
│  ├─ YES → Invest in learning if needed
│  └─ NO → Use managed service/library
│
├─ Do you know a tech that solves this?
│  ├─ YES (7/10+) → Use what you know ✅
│  └─ NO → Evaluate options ↓
│
├─ Industry standard exists?
│  ├─ YES → Learn it (if < 2 weeks) ✅
│  └─ NO → RED FLAG: Might be too niche ❌
│
└─ Can you use managed service?
   ├─ YES → Use it (save time) ✅
   └─ NO → Might be too complex for solo ⚠️
```

**Example Decision: Email Notifications**
```
Q: Core to value prop? NO
Q: Managed service exists? YES (SendGrid, Resend, Postmark)
→ Decision: Use Resend ✅ (5 min setup vs 2 days building SMTP)
```

**Example Decision: Real-time Chat**
```
Q: Core to value prop? YES (it's a chat app)
Q: Know WebSocket? NO (2/10)
Q: Managed service? YES (Pusher, Ably)
→ Decision: Start with Pusher for MVP, learn WebSocket for v2 ✅
```

**Red Flags:**
- Using 3+ new technologies simultaneously
- "Latest/coolest" tech without proven use cases
- Building auth/payments/email from scratch
- Custom infrastructure when managed exists

**Green Flags:**
- 80%+ familiar tech, 20% learning
- Managed services for non-core features
- Battle-tested stack (React, Next.js, PostgreSQL, etc.)
- Active community + good docs

## Mitigation Strategies

- High Risk: Use managed services/proven libraries
- Critical Risk: Outsource or de-scope
- Skill Gaps: Budget learning time realistically

---

**See main SKILL.md for scoring framework and integration with other assessments.**
