---
title: "Tutorial 10: Building a Campaign Performance Simulator"
type: tutorial
version: 1.0
created: 2026-04-05
tool_built: tools/campaign_simulator.html
sequence: 10
---

# Tutorial 10: Building a Campaign Performance Simulator

## What You'll Build

An interactive HTML campaign simulator that models the full marketing funnel — from impressions through clicks, conversions, and revenue — across five channels. Users adjust budget, duration, season, channel mix, and scenario (conservative/expected/optimistic) with results updating in real time.

## Why This Matters

The budget allocator (Tutorial 05) answers "how much to each channel?" This simulator answers "what happens when we do?" It models the full funnel for each channel, showing not just revenue but the intermediate metrics (impressions, clicks, conversion rates) that explain how the revenue gets generated.

For the AI marketing demonstration, this is the forecasting layer. It turns strategy into projectable outcomes that can later be compared against simulated actuals in a post-campaign analysis.

## Step 1: Define Channel Funnel Models

Each channel has a different funnel shape, derived from historical data:

**Meta Ads:**
```
Spend → Impressions (via CPM: $22 base)
     → Clicks (via CTR: 1.0% base)
     → Conversions (via conv rate: 3.2% of clicks)
     → Revenue ($385 × conversions)
```

**Email:**
```
List size (4,200) × deliverability (95%) × campaigns in period
     → Opens (35.5% open rate)
     → Clicks (4.5% of opens)
     → Conversions (3.0% of clicks)
     → Revenue
```

**Content/SEO:**
```
Spend → Organic sessions (9.3 sessions per $1K spent)
     → Conversions (2.5% of sessions)
     → Revenue
```

**Social Organic:**
```
Spend → Reach (42.5 reach per $1K spent)
     → Link clicks (1.0% of reach)
     → Conversions (1.8% of clicks)
     → Revenue
```

**Landing Page:** Enabler — no direct attribution, conversions flow through other channels.

## Step 2: Add Modifiers

Three layers of modification applied to base rates:

1. **Seasonal multipliers** — same index used across all project tools (winter 0.60x, spring 0.92x, summer 1.33x, fall 1.02x)
2. **Scenario multipliers** — applied to conversion rates only (conservative 0.8x, expected 1.0x, optimistic 1.2x)
3. **Diminishing returns** — when channel spend exceeds 2x the historical monthly average, efficiency degrades per channel's diminishing factor

These stack multiplicatively: a summer + optimistic Meta campaign has conversion rate = 3.2% × 1.33 × 1.2 = 5.1%.

## Step 3: Build the Daily Projection

The cumulative chart uses an S-curve (3x² - 2x³) to model realistic campaign pacing:
- Days 1–7: slower ramp as creative enters learning phase
- Days 8–22: fastest accumulation
- Days 23–30: taper as audience saturates

This is more realistic than a linear projection and matches how Meta campaigns actually perform.

## Step 4: Build the Interactive Controls

- **Budget slider** ($5K–$100K) — wider range than the budget allocator for scenario exploration
- **Duration slider** (7–90 days) — affects email campaign count and daily spend rate
- **Season toggle** — dramatically changes projections (summer vs. winter is ~2.2x difference)
- **Channel mix sliders** — adjust any channel, others normalize automatically
- **Scenario toggle** — conservative/expected/optimistic applies to conversion rates

All controls trigger a full re-simulation and re-render.

## Step 5: Build the Outputs

1. **Six KPI cards** — revenue, units, ROAS, impressions, clicks, CAC
2. **Goal progress bar** — tracks against the 500-unit campaign goal
3. **Conversion funnel** — visual bar chart showing impressions → clicks → conversions → revenue
4. **Revenue by channel** — doughnut chart of revenue contribution
5. **Daily cumulative** — S-curve chart showing revenue and unit accumulation over the campaign
6. **Channel detail table** — full-funnel metrics per channel (budget, impressions, clicks, CTR, conversions, conv rate, revenue, ROAS, CAC)

## The Prompt Used

```
Build a campaign performance simulator for Yowie. Let me input total budget,
channel split percentages, and campaign duration. It should project impressions,
clicks, conversions, revenue, and ROAS based on the historical performance data.
Make it interactive — sliders for budget and channel mix, with results updating
in real time. Output as an HTML file.
```

## Output

See: [`campaign_simulator.html`](../tools/campaign_simulator.html)

## Things to Try

1. **Summer + Expected at $25K** — baseline campaign scenario, check if it hits 500 units
2. **Toggle to Winter** — watch revenue drop ~55%, ROAS plummet
3. **Slide budget to $75K** — diminishing returns kick in, ROAS decreases
4. **Put 80% into Meta** — high volume but efficiency drops from audience saturation
5. **Switch to Conservative** — conversion rates drop 20%, stress-tests the plan
6. **Set duration to 14 days** — higher daily spend, stronger diminishing returns

## Replication Checklist

1. Define per-channel funnel models from historical data (CPM, CTR, conv rate)
2. Stack seasonal, scenario, and diminishing-return modifiers multiplicatively
3. Use an S-curve for daily projections — not linear
4. Model email separately (list-size-limited, campaign-count-driven)
5. Treat landing page as enabler with no direct attribution
6. Show the full funnel visually — impressions through revenue
7. Include a scenario toggle (conservative/expected/optimistic) for planning ranges
8. Display per-channel detail table so users can interrogate the model
9. Track against a defined campaign goal (500 units)
10. Document the model basis so users know what assumptions drive the projections
