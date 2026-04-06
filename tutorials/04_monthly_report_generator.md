---
title: "Tutorial 04: Building a Monthly Report Generator"
type: tutorial
version: 1.0
created: 2026-04-05
tool_built: tools/generate_monthly_report.py
sequence: 4
---

# Tutorial 04: Building a Monthly Report Generator

## What You'll Build

A Python script that reads Yowie's CSV marketing data, analyzes a specified month, and outputs a formatted markdown report with key metrics, channel breakdowns, trend comparisons, insights, and recommendations — all written in the brand's voice.

## Why This Matters

Dashboards show you the numbers. Reports tell you what the numbers mean. This tool bridges that gap — it takes the same data as the dashboard and produces a written narrative that contextualizes performance, identifies patterns, and recommends actions.

For the AI marketing demonstration, this is also a key test: can a tool produce analysis that sounds like it came from someone who knows the brand? The Yowie voice — plainspoken, confident, no filler — is a constraint that makes the output more useful, not less.

## Step 1: Design the Report Structure

Before writing code, define what a good monthly report contains:

1. **The Month in Brief** — 2-3 sentences. Revenue, units, ROAS. No warm-up.
2. **Key Metrics Table** — numbers with month-over-month deltas
3. **Channel Performance** — Meta, email, web traffic, social. Each gets its own section.
4. **Order Breakdown** — region, channel attribution, new vs. returning, discount usage
5. **Year to Date** — cumulative numbers for context
6. **What We Noticed** — 3-5 data-driven insights
7. **What to Do About It** — 2-4 actionable recommendations

**Key decision:** The report opens with the conclusion, not the methodology. "Revenue is up 44%." Not "This report analyzes the performance of..." Yowie's voice respects the reader's time.

## Step 2: Build the Data Layer

The script loads all six CSV files and provides helper functions for:

- Getting a single month's row from any dataset
- Getting all rows for a month (email campaigns, web traffic sources)
- Computing month-over-month deltas
- Formatting numbers consistently (money, percentages, comma-separated integers)

**Key decision:** All data stays as Python dicts loaded from CSV. No pandas dependency. The datasets are small (60 rows max), and avoiding pandas keeps the tool zero-dependency — runs on any machine with Python 3.

## Step 3: Build Analysis Functions

Each data domain gets its own analysis function:

| Function | Inputs | Outputs |
|----------|--------|---------|
| `analyze_revenue()` | summary row + prior month | revenue, units, AOV, all with deltas |
| `analyze_meta()` | meta row + prior month | spend, ROAS, CAC, cart completion, deltas |
| `analyze_email()` | email campaign rows | open rate, CTR, conversions, best campaign |
| `analyze_web()` | web traffic rows + prior | sessions by source, total delta, ranked sources |
| `analyze_social()` | social rows | followers, engagement, growth per platform |
| `analyze_orders()` | order rows | region/channel breakdown, new%, discount% |
| `compute_ytd()` | all summary rows through month | cumulative revenue, units, ROAS |

**Key decision:** Each function returns a dictionary, not formatted text. This separates analysis from presentation — the same analysis can feed different report formats later.

## Step 4: Generate Insights Programmatically

The `generate_insights()` function checks conditions against thresholds and produces observations:

```
if meta["roas"] >= 6.0:
    "Meta ROAS hit 6.0x this month. The spend-to-return ratio is strong."
elif meta["roas"] < 4.0:
    "Meta ROAS dropped to 3.9x. Below the 4x floor, the math stops working."
```

Conditions checked:
- Revenue direction (up/down from prior month)
- Meta ROAS above 6x or below 4x
- CAC movement (>15% change either direction)
- Email open rates above 37% or below 32%
- Cart abandonment rate
- Traffic source composition (organic vs. paid dependency)

**Key decision:** Insights are conditional, not exhaustive. The report includes 3-5 of the most relevant observations, not every possible metric comparison. An insight that says "email was about the same as last month" wastes the reader's time.

**Voice application:** Insights use short declarative sentences. No hedging ("it appears that..."), no excitement ("amazing results!"), no unnecessary qualification. "CAC dropped to $71. More efficient month. The audience is responding."

## Step 5: Generate Recommendations

The `generate_recommendations()` function translates insights into actions:

- ROAS > 5.5x → increase spend 15-20%
- ROAS < 4x → pull back 20%, redirect to email/content
- Zero email conversions → test product-focused CTA
- Seasonal timing → prep for upcoming peak/trough
- High new-customer rate → explore repeat purchase triggers

**Key decision:** Recommendations are specific and opinionated. "Increase Meta spend by 15-20%" is useful. "Consider adjusting your ad budget" is not. The Yowie voice doesn't hedge.

## Step 6: Assemble the Report

The `generate_report()` function calls all analysis functions, generates insights and recommendations, then builds the markdown document section by section.

Each section is assembled as a list of strings, joined with newlines. YAML frontmatter is included at the top for machine parseability.

## The Prompt Used

```
Build a tool that reads the Yowie marketing data files and generates a written
monthly report with key metrics, trends, insights, and recommendations. Output
it as a formatted markdown file. Use the Yowie brand voice from the brand definition.
```

## Usage

```bash
# Generate report for the most recent month
python3 tools/generate_monthly_report.py

# Generate report for a specific month
python3 tools/generate_monthly_report.py 2025-07

# Generate reports for all 12 months
python3 tools/generate_monthly_report.py --all
```

Reports are written to `docs/report_YYYY_MM.md`.

## How the Voice Works in Practice

The same data point, written three ways:

| Generic | Corporate | Yowie |
|---------|-----------|-------|
| "Revenue increased by 24.4% compared to the previous month" | "We are pleased to report a 24.4% month-over-month revenue increase" | "Revenue is up 24.4% from last month. The seasonal pattern is doing its job." |
| "It may be worth considering a reduction in advertising spend" | "We recommend a strategic reallocation of marketing investment" | "Pull back Meta spend by 20%. Below 4x ROAS, we're buying conversions at a loss." |

The Yowie voice: state the fact, add one sentence of context, move on.

## Replication Checklist

1. Define report structure before writing code — what sections, in what order
2. Lead with conclusions, not methodology
3. Separate analysis (data → dict) from presentation (dict → markdown)
4. Make insights conditional — only surface observations that matter this month
5. Write recommendations that are specific and actionable, not vague
6. Apply brand voice as a constraint: sentence length, hedging level, jargon tolerance
7. Include YAML frontmatter for downstream machine consumption
8. Support single-month, specific-month, and all-months modes
9. Keep dependencies at zero — CSV + standard library only
10. Test with peak and trough months to verify the tone adapts to context
