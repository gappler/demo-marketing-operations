---
title: "Tutorial 07: Building a Campaign Landing Page"
type: tutorial
version: 1.0
created: 2026-04-05
tool_built: tools/landing_page.html
sequence: 7
---

# Tutorial 07: Building a Campaign Landing Page

## What You'll Build

A single-file responsive landing page for the Yowie Basecamp 45L campaign. The page includes a hero section, product introduction, feature grid, materials deep-dive, specs table, social proof, warranty section with cost-per-trip math, and a final CTA — all written in the Yowie brand voice with scroll-triggered reveal animations.

## Why This Matters

The landing page is where every other channel converges. Meta ads, email CTAs, organic search — they all point here. This page has to do three things in 30 seconds: establish what the product is, prove it's worth $385, and give the reader a clear path to purchase. For this audience (experienced outdoor adults 40–65), that means specs and substance, not lifestyle imagery and aspirational copy.

## Design Direction

**Editorial luxury meets field guide.** The page reads like a Monocle feature article about a piece of gear, not a Shopify product page:

- **Typography:** Cormorant Garamond (display) — high-contrast serif with character and quiet authority. Source Serif 4 (body) — warm, readable. IBM Plex Mono (data/specs) — technical precision.
- **Color:** Dark warm palette (#1c1b17 background) alternating with warm off-white (#f5f2eb) for contrast sections. Muted olive accent (#6b7f5e) — restrained, natural, never loud.
- **Layout:** Generous negative space. Asymmetric two-column sections. The page breathes.
- **Motion:** Scroll-triggered reveals via IntersectionObserver. Subtle — elements fade up 32px. No parallax, no bounce, no attention-seeking animation.
- **Atmosphere:** Subtle diamond-pattern SVG texture on the hero. Gradient meshes suggesting landscape depth. No stock photos — image areas are placeholder-ready.

## Page Sections and Strategy

| Section | Purpose | Voice Note |
|---------|---------|------------|
| Hero | Immediate positioning: "One pack. That's it." | Two sentences to clarity |
| Intro | Why this brand exists | First-person, confident, no mission statement |
| Features | 6 cards: material, frame, compartment, zippers, warranty, volume | Specs, not benefits. This audience reads denier counts. |
| Materials | Sailcloth nylon deep-dive with spec comparison | Side-by-side editorial layout |
| Specs Table | Full specifications | Monospace, technical, no marketing language |
| Social Proof | 4 testimonials from realistic customers | Named locations, years of experience, specific details |
| Warranty | De-risk the $385 price with cost-per-trip math | Acknowledges the objection directly |
| CTA | "Still here when you're ready." | Low-pressure, echoes Email 5 closing |

## Key Decisions

- **No countdown timer, no urgency language, no "limited stock."** The brand voice forbids it, and this audience sees through it. The CTA says "Order the Basecamp" — not "Buy now" or "Don't miss out."
- **Social proof uses specific locations and experience levels** — "Bozeman, MT, 22 years backcountry experience" — because this audience judges credibility by specificity, not star ratings.
- **The warranty section includes a cost-per-trip comparison table** (same one from Email 4) — converting a $385 price objection into a $5/trip rational argument.
- **Image areas are gradient placeholders** with text markers (`[ fabric detail close-up ]`). In production, replace with hosted images. The page works visually without them.
- **No JavaScript framework.** Vanilla JS for IntersectionObserver (scroll reveals) and nav scroll state. Zero dependencies beyond Google Fonts.

## The Prompt Used

```
Build a landing page for the Yowie Basecamp 45L campaign. Use the brand
definition for voice and messaging. Include hero section, product features,
social proof section, and a clear CTA. Make it responsive. Output as a
single HTML file I can open in a browser.
```

## Output

See: [`landing_page.html`](../tools/landing_page.html)

Open by double-clicking or running `open tools/landing_page.html`.

## Replication Checklist

1. Read the brand definition before writing any copy — voice traits constrain every word
2. Choose a design direction that matches the brand, not a generic template
3. Lead with positioning, not product — the hero should say what the brand *is*
4. Use specs instead of benefits for technical audiences
5. Write social proof with specific details (location, experience, gear context)
6. Address the price objection directly — don't hide from it
7. Use scroll-triggered reveals sparingly — subtle enhances, flashy distracts
8. Make the CTA low-pressure for trust-oriented audiences
9. Keep image areas as replaceable placeholders — the page should work without them
10. Test responsive breakpoints — this audience checks email on desktop and browses on tablets
