---
title: "Tutorial 02: Generating Historical Marketing Data"
type: tutorial
version: 1.0
created: 2026-04-05
tool_built: data/generate_historical_data.py
sequence: 2
---

# Tutorial 02: Generating Historical Marketing Data

## What You'll Build

A Python script that generates 12 months of internally consistent marketing data across five datasets: web traffic, email campaigns, Meta ads, social media, and customer orders — plus a rolled-up monthly summary. The data simulates a small premium DTC outdoor brand with realistic seasonal patterns.

## Why This Matters

AI marketing tools need historical data to produce meaningful analysis, forecasts, and campaign recommendations. Without a baseline, prompts like "analyze our performance" or "recommend a budget" produce generic answers. This historical data gives downstream AI workflows concrete numbers to reference, compare against, and optimize from.

The data also needs to be internally consistent — orders should correlate with ad spend and traffic, email list size should match the brand definition, and seasonal patterns should be coherent across all channels. A Python script ensures this consistency in a way that hand-crafted CSVs can't.

## Step 1: Ground the Data in Brand Constraints

Before writing any code, extract the hard numbers from `brand/brand_definition.md`:

- **Price:** $385 per unit
- **Email list:** ~4,200 subscribers (as of campaign launch in April 2026)
- **Channels:** Meta ads, email, organic search, direct, referral
- **Audience regions:** Mountain west, northeast, pacific northwest primarily
- **Campaign budget reference:** $25K for a 30-day push (gives a sense of spending scale)

These constraints anchor the data. A brand with 4,200 email subscribers and a $25K campaign budget is not generating 50,000 monthly sessions or $500K in revenue. Scale everything accordingly.

## Step 2: Define the Seasonal Model

Premium outdoor gear has a predictable seasonal curve:

| Month | Multiplier | Rationale |
|-------|-----------|-----------|
| Apr | 0.85 | Spring planning ramp-up |
| May | 1.00 | Baseline — trip planning begins |
| Jun | 1.25 | Summer trips starting |
| Jul | 1.40 | Peak summer |
| Aug | 1.35 | Peak summer continues |
| Sep | 1.20 | Fall transition, still strong |
| Oct | 1.10 | Fall trips + early holiday research |
| Nov | 0.75 | Holiday season (not a gift product at $385) |
| Dec | 0.60 | Winter lull |
| Jan | 0.55 | Lowest point |
| Feb | 0.65 | Slow recovery |
| Mar | 0.90 | Spring ramp begins |

**Key decision:** A single seasonal multiplier array is shared across all datasets. This is what creates cross-dataset correlation. When July has a 1.40 multiplier, traffic, ad spend, orders, and engagement all scale up together — just like a real business.

## Step 3: Set Realistic Baselines

For a small premium DTC brand in years 1–2:

- **Web traffic:** ~8,000 sessions/month at baseline. Sources: organic search (35%), paid social (25%), direct (22%), email (10%), referral (8%)
- **Email:** ~2 campaigns/month, 2,800 starting list size, growing ~120 subscribers/month (scaled by season)
- **Meta ads:** ~$2,500/month baseline spend, scaling with season. CPM $18–28, CTR 0.8–1.4%
- **Social:** Instagram (3,200 followers) + Facebook (1,850 followers), growing modestly
- **Orders:** ~55/month at baseline, ~720 total annual units

**Key decision:** These numbers are deliberately modest. A brand selling one $385 product with a 4,200-person email list is small. Inflating the numbers would make downstream campaign simulations unrealistic — you can't credibly plan a "sell 500 units" campaign if the brand was already selling 500/month.

## Step 4: Build Cross-Dataset Relationships

The script uses several mechanisms to keep datasets consistent:

1. **Shared seasonal index** — all datasets reference the same `SEASONAL` array
2. **Jitter function** — adds ±5–8% random noise so numbers aren't suspiciously smooth, but keeps the directional trend intact
3. **Derived metrics** — conversions derive from clicks, which derive from impressions, which derive from spend. This creates natural funnels rather than arbitrary numbers
4. **Order channel attribution** — order attribution weights (paid_social 30%, organic 28%, email 18%, direct 14%, referral 10%) roughly match web traffic source proportions
5. **Email list continuity** — list size carries forward month to month, with growth and unsubscribe churn applied sequentially

## Step 5: Generate Individual Order Records

The `orders.csv` file contains individual order rows, not monthly aggregates. This is important because:

- Individual records support cohort analysis, regional breakdowns, and discount code analysis
- It lets downstream AI workflows ask questions like "what's our repeat purchase rate?" or "which region has the highest AOV?"
- The data includes realistic details: 8% of orders are qty 2 (gifts), 85% pay full price, 10% use a WELCOME10 code, 5% use a FRIEND15 referral code

## Step 6: Create a Monthly Summary Rollup

The `monthly_summary.csv` aggregates all five datasets into one view. This is the file most downstream prompts will reference first — it provides the full picture without requiring the AI to join five CSVs.

## The Prompt Used

```
Generate 12 months of historical marketing data for Yowie. Include monthly
CSVs for web traffic by source, email campaign performance, Meta ad spend
and results, social media engagement, and customer orders. Make the data
realistic with seasonal patterns — stronger summer and fall, weaker winter.
Save everything to a data/ folder.
```

**Why it works:** The prompt specifies the five data types, the seasonal pattern, and the output location. It doesn't over-prescribe column names or exact values — it trusts the AI to derive realistic baselines from the brand definition.

## Output Files

| File | Rows | Description |
|------|------|-------------|
| `web_traffic.csv` | 60 | 5 sources × 12 months |
| `email_campaigns.csv` | 27 | 2–3 campaigns × 12 months |
| `meta_ads.csv` | 12 | Monthly Meta ad performance |
| `social_media.csv` | 24 | 2 platforms × 12 months |
| `orders.csv` | 643 | Individual order records |
| `monthly_summary.csv` | 12 | Cross-channel monthly rollup |
| `generate_historical_data.py` | — | Reproducible generation script |

## Annual Totals (Verification)

- **Total revenue:** ~$260K
- **Total units:** 690
- **Total orders:** 643
- **Meta spend:** ~$28.8K (annual)
- **Email list growth:** 2,800 → 3,930 (reaching ~4,200 by April 2026)
- **Peak month:** July 2025 — 83 orders, $33.6K revenue
- **Trough month:** January 2026 — 31 orders, $11.6K revenue

## Replication Checklist

1. Read your brand definition and extract all hard numbers (price, list size, budget scale, channels)
2. Define a seasonal multiplier array appropriate to your product category
3. Set modest baselines — err toward smaller numbers for a DTC brand
4. Use a shared seasonal index across all datasets for natural correlation
5. Add jitter (±5–8%) so the data doesn't look algorithmically perfect
6. Build derived metrics (conversions from clicks from impressions) rather than random values
7. Generate individual order records, not just aggregates
8. Create a monthly summary rollup for easy reference
9. Use a seeded random generator so the data is reproducible
