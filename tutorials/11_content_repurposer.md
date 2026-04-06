---
title: "Tutorial 11: Building a Content Repurposing Tool"
type: tutorial
version: 1.0
created: 2026-04-05
tool_built: tools/content_repurposer.html
sequence: 11
---

# Tutorial 11: Building a Content Repurposing Tool

## What You'll Build

An interactive HTML page that takes a single source blog post about the Basecamp 45L on a Wind River Range trip and shows five platform-specific repurposed versions — LinkedIn, Instagram, email newsletter, Meta ad, and tweet thread — each with character counts, platform guidelines, brand voice checks, and adaptation notes explaining what changed and why.

## Why This Matters

Content repurposing is one of the highest-ROI applications of AI in marketing. One piece of source content can feed five channels, but only if each version is genuinely adapted for its platform — not just truncated. A LinkedIn post reads differently from an Instagram caption. A tweet thread has different pacing than an email snippet. This tool demonstrates that adaptation is a craft, not a copy-paste operation.

For the AI marketing demonstration, this shows how brand voice is maintained across platforms while format, length, and structure adapt to each channel's norms.

## Step 1: Write the Source Blog Post

The source is a ~300-word trip report about carrying the Basecamp 45L on a five-day Wind River Range loop. It follows the day-by-day structure used in Email 3 (Tutorial 06) and the landing page use-case section (Tutorial 07), creating narrative consistency across the project.

**Voice compliance:** Short sentences, no exclamation marks, specs stated plainly, treats the reader as someone who has carried a pack before.

## Step 2: Define Platform Constraints

Each platform has different rules:

| Platform | Key Constraint | Ideal Length | Tone Shift |
|----------|---------------|-------------|------------|
| LinkedIn | 3,000 chars, first 2 lines visible | 1,200–1,800 chars | Professional, first-person authority |
| Instagram | 2,200 chars, visual-first | 150–400 chars | Fragment-style, supports an image |
| Email | Open rate depends on subject line | 200–400 words | Conversational, single CTA |
| Meta Ad | 125 chars before "See more" | Under 500 chars | Spec-forward, direct |
| Tweet Thread | 280 chars per tweet | 4–8 tweets | Punchy, standalone tweets |

## Step 3: Adapt the Content

Each platform version is a genuine rewrite, not a truncation:

- **LinkedIn:** Rewritten as first-person professional narrative. Opens with a hook visible before "See more." Personal credibility statement added. 5 restrained hashtags.
- **Instagram:** Compressed to fragments. Numbers lead (38 lbs, five days). Designed to support a photo. Hashtag block separated by dot spacers.
- **Email:** Formatted as newsletter snippet with subject line and preview text. CTA matches the email sequence style ("See the Basecamp"). Warranty in footer.
- **Meta Ad:** 80% reduction from source. First 125 characters tell the story. Headline and description as separate fields. CTA is "Learn More."
- **Tweet Thread:** 6 tweets, each standalone. Punchline in tweet 2 ("Almost nothing"). No hashtags (they read as desperate on X/Twitter). No engagement bait.

## Step 4: Score Each Version Against Brand Voice

Every platform version is checked against the five Yowie voice traits:

- **Plainspoken** — are sentences short and jargon-free?
- **Confident** — are facts stated without hedging?
- **Restrained** — is there any urgency, push, or hype?
- **Respectful** — does it assume the reader knows gear?
- **Dry** — is there understated character?

All five versions pass all five checks. The key test: does the brand voice survive compression? A 280-character tweet should still sound like Yowie.

## Step 5: Build the Interactive Page

The page includes:

1. **Source content** — the full blog post with word/character counts
2. **Comparison strip** — character counts for all five platforms at a glance
3. **Tabbed platform views** — click any tab to see the adapted copy alongside:
   - Platform guidelines (character limits, ideal lengths, format rules)
   - Content stats (characters, words, % of limit with visual bar)
   - Brand voice check (pass/note for each trait)
4. **Adaptation notes** — explains what changed and what was cut for each platform

## The Prompt Used

```
Build a content repurposing tool for Yowie. Take this single input: a blog post
about the Basecamp 45L for a multi-day Wind River Range trip. Generate repurposed
versions for: a LinkedIn post, an Instagram caption, a email newsletter snippet,
a Meta ad, and a tweet thread. Each version should match Yowie's brand voice and
be formatted appropriately for its platform. Output as an HTML page showing all
versions side by side with character counts and platform guidelines.
```

## Output

See: [`content_repurposer.html`](../tools/content_repurposer.html)

## Replication Checklist

1. Write the source content in brand voice first — adaptation can't fix a broken source
2. Define platform constraints before adapting — know the rules of each channel
3. Genuinely rewrite for each platform — don't truncate, restructure
4. Open each version with the strongest element for that platform (numbers for Instagram, hook for LinkedIn, subject line for email)
5. Maintain brand voice across all compressions — the 280-char tweet must sound like the 1,500-char LinkedIn post
6. Include character counts and limit percentages — shows the writer is working within constraints
7. Score every version against brand voice traits — makes quality auditable
8. Document what changed and what was cut — the adaptation notes are the learning artifact
9. Remove platform-specific bad habits (engagement bait on Twitter, excessive hashtags on Instagram, "link in bio" pushiness)
