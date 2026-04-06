---
title: "Tutorial 08: Building a Competitive Intelligence Tracker"
type: tutorial
version: 1.0
created: 2026-04-05
tool_built: tools/competitive_intel.html
sequence: 8
---

# Tutorial 08: Building a Competitive Intelligence Tracker

## What You'll Build

An interactive HTML dashboard that compares Yowie against four real competitors — YETI, Stanley, Hydro Flask, and Osprey — across product positioning, pricing, target audience, marketing channels, and SWOT analysis. Users can select any two brands for side-by-side comparison.

## Why This Matters

A brand doesn't exist in isolation. Yowie's positioning as "understated, durable, anti-hype" only means something relative to competitors who are loud, trend-driven, or catalog-heavy. The competitive tracker makes these contrasts explicit and visual — it's a tool for understanding where Yowie fits in the landscape and where the gaps are.

For the AI marketing demonstration, this is the strategic context layer. Campaign decisions (messaging, channel mix, audience targeting) should be informed by what competitors are doing and where they're not.

## Step 1: Research Competitors

Four competitors were researched across consistent dimensions:

| Brand | Category | Why Included |
|-------|----------|-------------|
| Osprey | Backpacks | Closest direct competitor — same product category |
| YETI | Coolers/drinkware/bags | Premium outdoor benchmark — different category, similar positioning terrain |
| Stanley | Drinkware | Polar opposite positioning — trend-driven, young, viral |
| Hydro Flask | Bottles/drinkware | Design-led outdoor lifestyle — younger demographic |

**Research approach:** Each brand was researched for: founding year, parent company, product range, price points, target demographics, psychographics, marketing channels, revenue estimates, strengths, weaknesses, opportunities, and threats. Data reflects public information through early 2025.

**Key decision:** Included brands that are NOT direct competitors (Stanley, Hydro Flask) alongside one that is (Osprey). This is deliberate — understanding why Yowie is different from Stanley is as strategically valuable as understanding how it competes with Osprey.

## Step 2: Structure the Data

Each brand is stored as a JavaScript object with consistent fields:

- Identity: name, founded, parent, category
- Positioning: tagline, positioning statement, hero product
- Audience: age range, age center (for plotting), income, psychographic profile
- Economics: price range, price number (for plotting), revenue estimate, revenue scale (for bubble size)
- Channels: 12-item boolean map (Meta, Instagram, Facebook, TikTok, YouTube, Email, DTC, Retail, Influencer, Sponsorship, Content, PR)
- SWOT: strengths (5), weaknesses (5), opportunities (3), threats (3)

## Step 3: Build the Comparison Engine

The dashboard has four interactive sections:

1. **Brand selector** — two dropdowns, pick any two of five brands
2. **Side-by-side grid** — 13 dimensions compared in parallel columns
3. **SWOT panels** — full SWOT for both selected brands
4. **Yowie advantage callout** — when Yowie is selected, a contextual analysis explains the competitive relationship

Plus two always-visible sections:
5. **Positioning map** — bubble chart plotting price vs. audience age, bubble size = revenue
6. **Channel matrix** — dot grid showing which channels each brand uses

## Step 4: Write Competitive Positioning Insights

When Yowie is one of the selected brands, a contextual advantage callout appears:

- **vs. Osprey:** "Differentiates on single-product focus, older audience targeting, and anti-hype positioning. Osprey has 50 years of brand trust."
- **vs. YETI:** "Occupies a niche YETI doesn't serve. YETI's model is aspirational; Yowie's is respectful. Different audiences, minimal overlap."
- **vs. Stanley:** "Near-opposites: trend-driven vs. anti-trend, Gen Z vs. 40–65. The comparison illuminates Yowie's positioning by contrast."
- **vs. Hydro Flask:** "Both face the challenge of competing against larger brands, but in entirely different product categories."

These are strategic, not promotional. They acknowledge competitor strengths honestly.

## The Prompt Used

```
Build a competitive intelligence tracker that compares Yowie against YETI,
Stanley, Hydro Flask, and Osprey. Include product positioning, price points,
target audience, marketing channels used, strengths and weaknesses. Make it
an interactive HTML dashboard where I can compare any two brands side by side.
Use web search to pull real current data on the competitors.
```

## Output

See: [`competitive_intel.html`](../tools/competitive_intel.html)

## Things to Try

1. **Yowie vs. Osprey** — closest direct competitor, see where Yowie differentiates
2. **Yowie vs. Stanley** — polar opposites, clarifies what "anti-hype" means in practice
3. **YETI vs. Stanley** — the drinkware war, no Yowie involvement
4. **Check the positioning map** — Yowie is the only dot in the upper-right (high price + older audience)
5. **Check the channel matrix** — Yowie uses 7 of 12 channels; YETI and Osprey use all 12

## Replication Checklist

1. Research competitors across consistent dimensions — same fields for every brand
2. Include both direct and indirect competitors for strategic contrast
3. Structure data as JS objects with consistent schema
4. Build interactive selection (dropdown) rather than static pages
5. Include a positioning map that visualizes where brands cluster and where gaps exist
6. Channel matrix shows tactical overlap and gaps at a glance
7. Write honest competitive analysis — acknowledge competitor strengths
8. Full SWOT for every brand, including your own weaknesses
9. Contextual insights that appear based on selection, not generic summaries
