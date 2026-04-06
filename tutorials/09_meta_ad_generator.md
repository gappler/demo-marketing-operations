---
title: "Tutorial 09: Building a Meta Ad Copy Generator & Scorer"
type: tutorial
version: 1.0
created: 2026-04-05
tool_built: tools/meta_ad_generator.html
sequence: 9
---

# Tutorial 09: Building a Meta Ad Copy Generator & Scorer

## What You'll Build

An interactive HTML page that presents five Meta ad variants for the Yowie Basecamp 45L campaign, each rendered as a realistic Meta/Facebook ad preview. Every variant is scored against Yowie's five brand voice traits (plainspoken, confident, restrained, respectful, dry) with weighted scoring, rationale explanations, and a ranked summary strip.

## Why This Matters

Ad copy is where brand voice meets paid media. A well-defined brand voice is useless if the ads don't follow it. This tool demonstrates two things: (1) how to generate ad variants that each take a different angle while staying in voice, and (2) how to evaluate those variants systematically against the brand definition — not gut feel.

For the AI marketing demonstration, this is the quality-control layer. It shows that AI-generated copy can be scored against explicit criteria, making the process auditable and repeatable.

## Step 1: Define Five Ad Angles

Each variant takes a different persuasion approach while staying within Yowie's voice:

| Variant | Angle | Strategy |
|---------|-------|----------|
| A | Product Introduction | Lead with positioning, follow with specs |
| B | Materials Story | Technical proof — the sailcloth nylon argument |
| C | Anti-Hype Positioning | Define the brand by what it refuses to do |
| D | Warranty / Price Justification | Address the $385 objection directly |
| E | Experience / Use Case | Put the pack on a real trip |

**Key decision:** Five variants, not three or ten. Five gives enough variation to compare angles meaningfully without overwhelming. Each maps to a different messaging pillar or purchase-decision stage.

## Step 2: Write Each Ad

Each ad has four components matching Meta's ad format:
- **Primary text** — the main copy block (above the image)
- **Image** — placeholder (creative production is separate)
- **Link headline** — appears below the image
- **Link description** — subtitle below the headline
- **CTA button** — "Learn More" (not "Shop Now" — brand voice is restrained)

**Voice rules applied across all five:**
- No exclamation marks
- No urgency language
- No emojis
- CTA is "Learn More" on every variant — consistent, low-pressure
- Specs use actual material names (1680D sailcloth nylon, HDPE, YKK AquaGuard)
- Price is stated plainly when mentioned, never dressed up

## Step 3: Build the Scoring Model

Five dimensions, each weighted by importance to the Yowie voice:

| Dimension | Weight | What It Measures |
|-----------|--------|-----------------|
| Plainspoken | 25% | Sentence length, jargon absence, filler absence |
| Restrained | 25% | Urgency language, capitalization, exclamation marks |
| Confident | 20% | Hedging language, qualifying phrases, directness |
| Respectful | 15% | Assumes reader competence, doesn't over-explain |
| Dry | 15% | Understated humor or character without forced cleverness |

**Key decision:** Plainspoken and Restrained share the highest weight (25% each). For this brand, saying too much and pushing too hard are the two biggest voice violations. Dry humor is weighted lowest (15%) because it's a nice-to-have, not a requirement — an ad can be perfectly on-brand without a joke.

## Step 4: Score and Rank

Each variant receives scores 1–10 on all five dimensions, plus a written rationale explaining why.

**Results:**

| Variant | Angle | Overall | Top Dimension |
|---------|-------|---------|---------------|
| B | Materials Story | 9.3 | Plainspoken (9.5) |
| A | Product Introduction | 8.9 | Restrained (9.5) |
| D | Warranty | 8.8 | Plainspoken (9.3) |
| C | Anti-Hype | 8.7 | Dry (9.2) |
| E | Experience | 8.8 | Respectful (9.5) |

**Why Variant B wins:** "It's fine. It works. It wears out." is the most Yowie line in the entire set — plainspoken, dry, and devastatingly understated. "It costs us 3x more. We use it anyway." is confident without bragging. The variant hits high on every dimension because the materials story is the most natural home for Yowie's voice.

## Step 5: Build the Interactive Page

The page includes:
1. **Voice guidelines reference** — the five traits displayed at the top for context
2. **Ranked summary strip** — all five variants scored and ranked, click to scroll to any ad
3. **Ad cards** — each with a realistic Meta ad preview (Facebook feed format), score bars, overall score, and expandable rationale
4. **Scoring methodology** — explains the weighting and what each dimension measures

The Meta ad preview mimics the actual Facebook feed layout: avatar, brand name, "Sponsored" tag, primary text, image area, link bar with headline/description, and CTA button.

## The Prompt Used

```
Build a Meta ad copy generator for the Yowie Basecamp 45L campaign. Generate
5 ad variants — headline, primary text, and CTA for each. Then score each
variant against Yowie's brand voice guidelines from the brand definition file,
rating them on tone, clarity, and brand alignment. Output as an interactive
HTML page where I can see the ads and their scores side by side.
```

## Output

See: [`meta_ad_generator.html`](../tools/meta_ad_generator.html)

## Replication Checklist

1. Define distinct angles for each variant — don't just rephrase the same message
2. Apply brand voice constraints to every word choice (no exclamation marks, no urgency, specs not benefits)
3. Build a scoring model with weighted dimensions matching the brand definition
4. Write rationale for every score — makes the evaluation auditable
5. Render ads in the actual platform format (Meta feed layout) for realistic preview
6. Rank variants and identify a top pick with reasoning
7. Use consistent CTA across all variants — "Learn More" not "Shop Now"
8. Include the scoring methodology so stakeholders understand the rubric
9. Make rationale expandable — scores at a glance, detail on demand
