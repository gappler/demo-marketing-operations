---
title: "Tutorial 03: Building a Marketing Performance Dashboard"
type: tutorial
version: 1.0
created: 2026-04-05
tool_built: tools/dashboard.html
sequence: 3
---

# Tutorial 03: Building a Marketing Performance Dashboard

## What You'll Build

A single-file interactive HTML dashboard that visualizes 12 months of Yowie marketing data — revenue trends, customer acquisition costs, channel spend vs. return, email performance, web traffic by source, and regional order distribution.

## Why This Matters

Dashboards make historical data usable for two audiences: humans reviewing performance, and AI workflows that need context about "how things have been going." A well-structured dashboard also serves as a design reference for the brand's visual identity — in this case, the utilitarian, understated aesthetic that matches Yowie's positioning.

## Step 1: Choose the Architecture

**Decision: Single HTML file with embedded data.**

Alternatives considered:
- **Fetch CSVs at runtime** — breaks on `file://` protocol due to CORS. Would require a local server, adding friction.
- **React/framework app** — overkill for a visualization tool. Adds build steps, dependencies, and complexity that don't serve the goal.
- **Python notebook** — good for analysis, poor for sharing and presentation.

A single HTML file with Chart.js from CDN works everywhere: double-click to open, no server needed, no build step.

## Step 2: Design Direction

The dashboard aesthetic is derived from the brand, not from generic dashboard templates.

**Direction: Utilitarian field-notebook**
- Dark earth-toned background (`#1a1915`) — like worn leather
- Muted palette: olive green, burnt sienna, gold, slate — no bright blues or purples
- Monospace font (DM Mono) for all data — legibility and precision
- Serif display font (Instrument Serif) for headers — quiet authority
- Subtle topo-line background texture — outdoor reference without being literal
- No rounded corners, no shadows, no gradients on cards — flat, functional, restrained
- Hover states that reveal information, not decoration

**Why this matters for the project:** If this dashboard used a generic Bootstrap or Tailwind template, it would undermine the demonstration. The whole point is showing how brand identity flows through every touchpoint — including internal tools.

## Step 3: Embed the Data

The CSV data is converted to JavaScript objects directly in the HTML. This is the critical step that makes the file self-contained.

Structure:
- `summary[]` — 12 monthly rollup objects (from `monthly_summary.csv`)
- `metaAds[]` — 12 monthly Meta ad objects (from `meta_ads.csv`)
- `webTraffic{}` — sessions by source, 12 values each (from `web_traffic.csv`)
- `emailCampaigns[]` — 27 individual campaign objects (from `email_campaigns.csv`)
- `ordersByRegion{}` — pre-aggregated regional counts (from `orders.csv`)

**Key decision:** Orders are pre-aggregated by region rather than embedding all 643 rows. The dashboard doesn't need individual order records — that's for analysis tools, not visualization.

## Step 4: Build the KPI Strip

Six headline metrics across the top:
1. Annual Revenue ($260K) with H2 vs H1 delta
2. Units Sold (690) with order count
3. Average Order Value ($403)
4. Meta ROAS (5.4x) with total spend
5. Average CAC ($68) — Meta-attributed only
6. Email List (3,928) with growth percentage

**Why these six:** They answer the first questions any stakeholder asks — "how much did we make, how efficiently, and is the audience growing?" Every other chart is a drill-down from one of these.

## Step 5: Build the Charts

Six chart panels in a 2-column grid:

| Chart | Type | Why |
|-------|------|-----|
| Monthly Revenue | Bar + line overlay | Revenue bars show volume; units line shows if AOV is shifting |
| Customer Acquisition Cost | Area line | Trend matters more than absolute value — fill area shows magnitude |
| Channel Spend vs. Return | Bar + dual line | Spend bars against revenue line reveals efficiency; ROAS dashed line on secondary axis |
| Web Traffic by Source | Stacked area | Shows both total volume and channel mix shift over time |
| Email Performance | Tabbed (rates / list growth) | Two views that would clutter one chart; tabs keep it clean |
| Orders by Region | Doughnut | Part-to-whole relationship; confirms geographic distribution from brand definition |

**Chart.js configuration choices:**
- Tension 0.3 on all lines — slight smoothing prevents jagged noise while preserving trend shape
- Point backgrounds match the card color (`#1a1915`) with colored borders — creates a "cut-out" effect
- Grid lines at 40% opacity, no axis borders — present but recessive
- Tooltips with no border radius, monospace font — matches the utilitarian aesthetic

## Step 6: Add the Detail Table

A full monthly breakdown table at the bottom provides exact numbers for anyone who wants precision beyond what charts show. Includes a totals row with annual aggregates.

**Design choice:** The highest-revenue month gets a `highlight` class (brighter text). This is the only visual emphasis in the table — one signal, not many.

## The Prompt Used

```
Build a marketing performance dashboard for Yowie that reads the data files
in the data folder and visualizes key metrics — monthly revenue, customer
acquisition cost, channel spend vs. return, email performance, and web
traffic trends. Make it an interactive HTML file I can open in a browser.
```

## Output

See: [`dashboard.html`](../tools/dashboard.html)

Open by double-clicking the file or running `open tools/dashboard.html` from the project root.

## Replication Checklist

1. Read all data files and understand the schema before designing charts
2. Choose single-file HTML if the dashboard needs to work without a server
3. Embed data as JS objects — don't rely on fetch for local files
4. Derive the visual design from the brand identity, not from a generic template
5. Lead with KPIs that answer "how much, how efficiently, is it growing"
6. Use Chart.js with custom defaults — override fonts, colors, tooltip styles globally
7. Match chart types to the question being asked (trend = line, volume = bar, composition = doughnut)
8. Include a raw data table for precision — charts show patterns, tables show numbers
9. Add a seasonal indicator that connects the visual rhythm to business reality
10. Test by opening as `file://` — if it works there, it works everywhere
