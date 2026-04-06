---
title: "Tutorial 05: Building an Interactive Budget Allocator"
type: tutorial
version: 1.0
created: 2026-04-05
tool_built: tools/budget_allocator.html
sequence: 5
---

# Tutorial 05: Building an Interactive Budget Allocator

## What You'll Build

An interactive single-file HTML tool that takes Yowie's historical channel performance data, computes ROI efficiency by channel, and recommends an optimal budget split for a campaign. Users can adjust the total budget, campaign duration, target season, and allocation mode — and see projected revenue, units, ROAS, and CAC update in real time.

## Why This Matters

Budget allocation is where strategy becomes money. A campaign brief says "spend $25K across Meta, email, and organic" — but how much to each? This tool answers that question by grounding the split in historical performance data rather than gut feel or industry benchmarks.

For the AI marketing demonstration, this is the bridge between analysis (the dashboard, the reports) and execution (the campaign plan). It turns backward-looking data into forward-looking decisions.

## Step 1: Derive Channel Economics from Historical Data

Before building the tool, calculate the 12-month performance of each channel:

| Channel | Annual Spend | Revenue | Conversions | ROAS | CAC |
|---------|-------------|---------|-------------|------|-----|
| Meta Ads | $29,018 | $166,010 | 424 | 5.72x | $68 |
| Email | $1,248 | $10,395 | 27 | 8.33x | $46 |
| Content/SEO | $3,600 | $52,745 | 137 | 14.65x | $26 |
| Social Organic | $2,400 | $15,785 | 41 | 6.58x | $59 |
| Landing Page | $1,500 | — | — | — | — |

**Key decisions:**

- **Email cost is estimated** at $80/month ESP + marginal send cost. The CSV has no cost column, so this is derived from industry norms for a list of ~3,900.
- **Content/SEO cost is estimated** at $300/month. Organic search drives 35% of traffic; the cost is content creation time.
- **Landing page is an enabler**, not a direct revenue channel. Conversions flow through it but are attributed to the traffic source.
- These estimates are intentionally conservative — they make the ROI calculations defensible rather than inflated.

## Step 2: Build the Efficiency Scoring Model

Raw ROAS alone is misleading. Content/SEO has 14.65x ROAS but converts on a delay. Meta has 5.72x but scales predictably. The efficiency score combines two factors:

```
efficiency = (roas_normalized × 0.6) + (volume_normalized × 0.4)
```

- **ROAS normalized**: `min(roas / 15, 1)` — caps at 15x to prevent outliers from dominating
- **Volume normalized**: `min(conversions / 200, 1)` — rewards channels that convert reliably at volume

This scoring produces an allocation where Meta gets the largest share (it converts at volume), but content and email aren't starved (they're efficient).

## Step 3: Model Diminishing Returns

More money doesn't mean proportionally more results. The tool applies diminishing returns when spend exceeds historical averages:

```
if projected_monthly > historical_monthly:
    excess_ratio = (projected - historical) / 10000
    penalty = excess_ratio × diminishing_factor × 100
    adjusted_roas = base_roas × max(0.5, 1 - penalty/100)
```

Each channel has its own diminishing factor:
- **Meta (8%)**: Audience saturation and CPM inflation at higher spend
- **Social (4%)**: Content fatigue
- **Content (3%)**: Slow to scale, but relatively resilient
- **Email (2%)**: Nearly free marginal sends, minimal diminishing returns

This prevents the naive conclusion of "Meta has the best efficiency score, so put 100% there."

## Step 4: Add Seasonal Multipliers

Campaign timing changes everything. The tool applies seasonal multipliers to projected returns:

| Season | Multiplier | Context |
|--------|-----------|---------|
| Winter | 0.60x | Off-season. Higher CAC, lower conversion rates. |
| Spring | 0.92x | Ramp period. Momentum building. |
| Summer | 1.33x | Peak. Best efficiency across all channels. |
| Fall | 1.02x | Shoulder season. Solid but declining. |

These come directly from the seasonal index used in data generation (Tutorial 02). Consistency across tools is the point.

## Step 5: Build Three Allocation Modes

1. **Optimized** — weighted by efficiency score. Allocates proportional to each channel's combined ROAS + volume score, with min/max floors.
2. **Balanced** — equal split across all five channels. Useful as a baseline comparison.
3. **Manual** — user drags sliders to set any allocation they want.

All modes support channel locking — lock a channel's allocation, and the remaining budget redistributes among unlocked channels.

## Step 6: Build the Interactive Controls

The left panel provides:
- **Budget slider** ($5K–$75K) — see how scale affects efficiency
- **Duration slider** (14–90 days) — affects daily spend rate and diminishing returns
- **Mode toggle** — optimized / balanced / manual
- **Channel sliders** — active in manual mode, show allocation in all modes
- **Season toggle** — winter / spring / summer / fall
- **Lock buttons** — lock any channel to hold its share constant

Every control triggers `updateAll()`, which recomputes projections and re-renders all outputs.

## Step 7: Display Projections

The right panel shows:
- **Four KPI cards**: projected revenue, units, blended ROAS, blended CAC
- **Goal progress bar**: tracks against the 500-unit campaign goal from the brand definition
- **Allocation chart**: side-by-side bars showing budget vs. estimated revenue per channel
- **Channel projections table**: per-channel spend, revenue, units, ROAS, CAC
- **Historical basis table**: the 12-month data the model is built on, with efficiency scores

## The Prompt Used

```
Build a budget allocator tool for Yowie's $25K campaign. It should read the
historical channel performance data, calculate ROI by channel, and recommend
an optimal budget split across Meta, email, and other channels. Make it
interactive — let me adjust the total budget and see how the allocation
changes. Output as an HTML file.
```

## Output

See: [`budget_allocator.html`](../tools/budget_allocator.html)

Open by double-clicking or running `open tools/budget_allocator.html`.

## Things to Try

1. **Slide budget from $5K to $75K** — watch how ROAS decreases at higher spend (diminishing returns kicking in)
2. **Toggle seasons** — summer at $25K meets the 500-unit goal; winter at $25K falls far short
3. **Switch to manual mode** — put 85% into Meta and watch the blended ROAS drop as diminishing returns take over
4. **Lock email at 8%, then increase budget** — the extra budget flows to other channels proportionally

## Replication Checklist

1. Derive channel economics from historical data — include estimated costs for "free" channels
2. Build an efficiency score that combines ROI with volume reliability
3. Model diminishing returns — don't let the optimizer put everything in one channel
4. Apply seasonal multipliers from your existing seasonal model
5. Provide multiple allocation modes (optimized, balanced, manual)
6. Add channel locking for user control
7. Show projections against a defined campaign goal (500 units)
8. Include the historical basis so users can interrogate the model's assumptions
9. Single HTML file, no server, matches the brand aesthetic
