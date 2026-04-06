---
title: "Tutorial 12: Building a Customer Segment Analyzer"
type: tutorial
version: 1.0
created: 2026-04-05
tool_built: tools/customer_segments.html
sequence: 12
---

# Tutorial 12: Building a Customer Segment Analyzer

## What You'll Build

An interactive dashboard that identifies five distinct customer segments from Yowie's 643 order records, profiles each with demographics, purchase patterns, psychographics, estimated lifetime value, and a recommended messaging approach — all written in Yowie's brand voice.

## Why This Matters

"Adults 40–65 who like the outdoors" is an audience definition. It's not a segmentation. Real customers within that audience behave differently — some find Yowie through search, some through ads, some through a friend at a trailhead. They convert at different rates, buy for different reasons, and respond to different messages. Segmentation turns one audience into five distinct conversations.

## Step 1: Analyze the Order Data

Cross-tabulations from 643 orders across five dimensions: region, attribution channel, customer type (new/returning), discount code usage, and quantity ordered. Key patterns that emerge:

| Pattern | Insight |
|---------|---------|
| Mountain West has 14.8% returning rate | Highest loyalty — core audience |
| PNW has 23.6% email channel attribution | Strongest email engagement |
| Northeast leads qty-2 orders (9.5%) | Gift-buying behavior |
| WELCOME10 skews 38% toward paid social | Discovery buyers use welcome offers |
| FRIEND15 users have 15% return rate | Referral network is self-reinforcing |

## Step 2: Define Five Segments

| Segment | Size | Key Signal | Avg LTV |
|---------|------|-----------|---------|
| Core Loyalists | 142 (22%) | Organic/direct, Mountain West, lowest discount use, highest return rate | $620 |
| Engaged Subscribers | 132 (21%) | Email channel, PNW heavy, WELCOME10 users, nurtured conversion | $540 |
| Discovery Buyers | 182 (28%) | 100% paid social, highest new-customer rate (93%), geographically distributed | $445 |
| Gift Buyers | 102 (16%) | 46% ordered qty 2, highest AOV ($437), NE heavy, referral channel over-indexes | $710 |
| Referral Network | 85 (13%) | FRIEND15 code, referral + direct channels, self-reinforcing network | $580 |

## Step 3: Write Segment-Specific Messaging

Each segment gets a recommended approach and example copy, all within Yowie's voice:

- **Core Loyalists:** Spec-forward, minimal. "That's the pitch. The pack speaks for itself."
- **Engaged Subscribers:** Narrative, materials-focused. The sailcloth nylon story.
- **Discovery Buyers:** Hook-first, scroll-stopping. Trip scenario in the first 125 characters.
- **Gift Buyers:** Relationship-driven. "You know someone who's carried the wrong pack for too long."
- **Referral Network:** Confirmation, not persuasion. "They already told you why. We'll just show you the specs."

## Step 4: Estimate Lifetime Value

LTV calculations include: base purchase, repeat purchase probability (varies 7–15% by segment), referral multiplier (0.4–1.5 referred customers per buyer), and initial discount impact.

Gift Buyers have the highest LTV ($710) despite moderate segment size — qty-2 purchases create $770 initial orders, and each gift recipient is a potential new Core Loyalist.

## The Prompt Used

```
Build a customer segment analyzer for Yowie. Read the customer order data,
identify 3-5 distinct segments based on purchase patterns, geography, and
demographics. For each segment, provide a profile, estimated size, lifetime
value potential, and a recommended messaging approach that fits Yowie's brand
voice. Output as an interactive HTML dashboard with visual breakdowns of
each segment.
```

## Output

See: [`customer_segments.html`](../tools/customer_segments.html)

## Replication Checklist

1. Cross-tabulate order data across multiple dimensions (region × channel, channel × discount, region × customer type)
2. Look for behavioral clusters, not just demographic groups
3. Name segments by behavior, not demographics ("Gift Buyers" not "Northeast 50+")
4. Include psychographic profiles — what motivates each segment's purchase decision
5. Calculate LTV including referral multiplier, not just repeat purchase
6. Write segment-specific messaging that stays within brand voice constraints
7. Include example copy for each segment so the messaging approach is concrete
8. Build a comparison table so all segments can be evaluated side by side
9. Identify the highest-LTV segment (Gift Buyers) and the highest-volume segment (Discovery) — they're different and require different strategies
