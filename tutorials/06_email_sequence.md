---
title: "Tutorial 06: Building a Campaign Email Sequence"
type: tutorial
version: 1.0
created: 2026-04-05
tool_built: tools/email_sequence/
sequence: 6
---

# Tutorial 06: Building a Campaign Email Sequence

## What You'll Build

A five-email nurture sequence for Yowie's 30-day Basecamp 45L campaign, targeting the 4,200-subscriber list. Outputs include a strategic markdown overview with send timing and performance projections, plus five production-ready HTML email templates with inline CSS for email client compatibility.

## Why This Matters

Email is the highest-ROI channel in Yowie's historical data (8.33x ROAS), but it's also the most voice-sensitive. A Meta ad gets 2 seconds of attention. An email from a brand the subscriber chose to hear from gets 15–30 seconds — enough to build or destroy trust. Getting the voice wrong here costs more than a low click-through rate; it costs list quality.

For the AI marketing demonstration, the email sequence is the hardest test of whether the brand voice is actually constraining AI output. Generic marketing language will be immediately visible in a 5-email series where the reader accumulates exposure.

## Step 1: Design the Sequence Arc

A nurture sequence is not five sales pitches sent on different days. It's a narrative arc with a purpose at each stage:

| Email | Day | Purpose | Pillar |
|-------|-----|---------|--------|
| 1. Announcement | Day 1 | Say what it is | Made for people who know |
| 2. Materials | Day 5 | Prove the claim | Built to outlast |
| 3. Use Case | Day 12 | Show it in context | Made for people who know |
| 4. Warranty | Day 20 | De-risk the price | Built to outlast |
| 5. Closing | Day 27 | Last word | Nothing unnecessary |

**Key decision:** This is a trust arc, not a pressure arc. No "limited time" or "only X left." This audience — experienced outdoor adults 40–65 — has been marketed to for decades. They recognize urgency tactics and they lose trust when they see them.

The sequence builds: introduce → prove → contextualize → de-risk → close. Each email earns the right to the next one.

## Step 2: Apply the Brand Voice

The brand definition specifies five voice traits: plainspoken, confident, restrained, respectful, dry. In email copy, this translates to:

**Dos:**
- Short sentences. Short paragraphs.
- State facts without hedging ("It costs us 3x more. We use it anyway.")
- Treat the reader as someone who already knows gear
- End emails cleanly — no "Thanks for reading" or "We appreciate your time"
- One CTA per email, same language every time ("See the Basecamp")

**Don'ts:**
- No exclamation marks
- No "we're excited" or "we're thrilled"
- No countdown timers or urgency language
- No emojis
- No "Dear [First Name]" — this audience doesn't want familiarity from a brand

**Example comparison:**

| Generic | Yowie |
|---------|-------|
| "We're thrilled to introduce our amazing new backpack!" | "We make one pack." |
| "Don't miss this incredible limited-time offer!" | "If now is the right time, the link is below." |
| "Our proprietary ActiveFlex technology provides superior comfort" | "Thermoformed HDPE, tuned for 30–40 lb carries." |

## Step 3: Write Each Email

### Email 1 — Announcement
Opens with the single strongest positioning statement: "We make one pack." Two sentences before the reader knows exactly what this brand is. Then specs — not benefits, specs. This audience reads denier counts and zipper brands.

### Email 2 — Materials
The deepest email in the sequence. Goes into sailcloth nylon vs. Cordura, includes a comparison table. This is the email that separates Yowie from brands that say "premium materials" without saying what the materials actually are.

**Key decision:** Included a spec comparison table (standard 500–1000D Cordura vs. 1680D sailcloth). This audience respects data. A table says "we're not hiding behind marketing language."

### Email 3 — Use Case
Shifts from specs to experience. Puts the pack on a real trip — Wind River Range, five days, named landmarks (Elkhart Park, Island Lake, Granite Pass). Specific places the reader may have actually been.

**Key decision:** Used second person ("You don't think about the pack") to put the reader in the scenario, but avoided the brand-story trap. This isn't "our founder's journey." It's the reader's trip, with the pack as a background character.

### Email 4 — Warranty / De-risk
The only email that acknowledges the price objection directly: "$385 is a lot for a pack. We know that." Then addresses it with the warranty terms and a cost-per-trip comparison table.

**Key decision:** No hero image on this email. It's the most text-forward email in the sequence — deliberately. The warranty argument is logical, not visual. A big product photo would undercut the seriousness of the financial argument.

### Email 5 — Closing
The shortest email. 72 words of body copy. Summarizes the product in one line, states the price, then steps back: "If it's not [the right time], we're not going anywhere." Ends with "good trails" — dry, warm, not trying too hard.

**Key decision:** No new information. No additional offer. No "last chance." The restraint is the point. This email communicates confidence — we said what we had to say, and we're not going to beg.

## Step 4: Build the HTML Templates

Email HTML is not web HTML. Every template uses:

- **Table-based layout** — `<div>` layout breaks in Outlook, Yahoo, and older Gmail
- **Inline CSS** — most email clients strip `<style>` blocks (media queries are the exception)
- **`role="presentation"`** on all tables — accessibility for screen readers
- **Preheader text** via hidden `<div>` — controls preview text in inbox list views
- **Dark mode support** via `prefers-color-scheme` media query — background and text colors adapt
- **MSO conditionals** — `<!--[if mso]>` blocks for Outlook-specific rendering
- **Merge tags** — `{{UNSUBSCRIBE_URL}}` and `{{WEBVIEW_URL}}` for ESP integration

**Design system across all 5 emails:**
- Background: warm parchment (#f4f1eb)
- Card: white (#ffffff) with subtle border (#e0ddd4)
- Body text: Georgia serif, 15px secondary / 17px primary
- Data/specs: Courier New monospace, 12px
- CTA: dark block (#2a2920) with monospace uppercase text
- Footer: 10px monospace, muted

## Step 5: Set Send Timing

- **7:00 AM local** for all weekday sends — catches the pre-work email check window for this demographic
- **8:00 AM Saturday** for Email 4 (warranty) — more reflective reading state for a consideration-stage message
- **4–7 day gaps** between emails — prevents fatigue on a small list (4,200)
- **Sequence ends Day 27** — three days of silence before campaign closes; no frantic last-day blast

## The Prompt Used

```
Build an email sequence generator for Yowie's Basecamp 45L campaign. It should
create a 5-email nurture series for the 4,200-subscriber list, using the brand
voice from the brand definition file. Each email should have a subject line,
preview text, body copy, and a clear CTA. Output as both individual HTML email
templates and a markdown overview of the full sequence with send timing recommendations.
```

## Output Files

| File | Purpose |
|------|---------|
| `tools/email_sequence/sequence_overview.md` | Full strategy, copy, timing, and projections |
| `tools/email_sequence/email_01_announcement.html` | Day 1 — "One pack. That's it." |
| `tools/email_sequence/email_02_materials.html` | Day 5 — "What sailcloth nylon actually means" |
| `tools/email_sequence/email_03_use_case.html` | Day 12 — "Five days in the Wind River Range" |
| `tools/email_sequence/email_04_warranty.html` | Day 20 — "The warranty is simple" |
| `tools/email_sequence/email_05_closing.html` | Day 27 — "Still here when you're ready" |

Preview any email by opening the HTML file in a browser.

## Replication Checklist

1. Design the sequence arc before writing copy — know the purpose of each email
2. Choose trust arc over pressure arc for skeptical, experienced audiences
3. Apply brand voice as a constraint: sentence length, tone, what you never say
4. Write copy in markdown first (the overview), then build HTML templates from it
5. Use table-based HTML with inline CSS for email client compatibility
6. Include dark mode support, preheader text, and merge tags
7. Maintain a consistent design system across all emails (same fonts, colors, CTA style)
8. Set send timing based on audience behavior, not platform defaults
9. Include performance projections grounded in historical email data
10. End the sequence with restraint — the closing email proves the brand voice more than any other
