---
title: "Tutorial 01: Building a Simulation Brand Definition"
type: tutorial
version: 1.0
created: 2026-04-05
tool_built: brand/brand_definition.md
sequence: 1
---

# Tutorial 01: Building a Simulation Brand Definition

## What You'll Build

A complete brand definition document for a fictional DTC brand called "Yowie" — structured specifically to serve as a controlled input for AI-driven marketing automation workflows.

This is the foundation layer. Every downstream deliverable (campaigns, ads, emails, landing pages, performance simulations) depends on the constraints defined here.

## Why This Matters

AI marketing tools produce better output when they have tight, specific inputs. A vague brand brief produces vague campaigns. This tutorial shows you how to construct a brand definition that is:

- Constrained enough that AI outputs are predictable and traceable
- Rich enough to support a full marketing lifecycle
- Structured so every section feeds directly into a downstream workflow

## Step 1: Set the Role and Frame the Task

The prompt begins by assigning a specific role and framing the exercise clearly:

```
You are a senior brand strategist and marketing systems architect.

Your task is to create a fictional but realistic brand designed specifically
for demonstrating AI-driven marketing automation across a full lifecycle
(strategy → planning → production → execution → analysis → post-mortem).

This is NOT a creative writing exercise.
```

**Why this matters:** Without the role assignment, the AI defaults to generic marketing copy. The explicit "NOT a creative writing exercise" constraint prevents the AI from optimizing for cleverness over structure. You want a teaching tool, not a portfolio piece.

## Step 2: Define the Brand Parameters

The prompt locks down core variables so the AI doesn't invent unnecessary complexity:

```
Brand Name: Yowie
Category: Premium outdoor gear (DTC)
Core Product: Choose a single hero product
Target Audience: Adults 40–65, experienced outdoor users
Positioning: Premium, durable, understated
```

**Key decisions:**

- **Single product, single audience.** Multiple products or segments create branching complexity that makes it harder to trace how inputs affect outputs in downstream simulations. One product keeps the cause-and-effect chain visible.
- **Age range 40–65.** This is deliberate. Younger demographics invite influencer/social-first strategies that are harder to simulate. Older, experienced buyers make decisions based on specs and reputation — easier to model.
- **"Anti-hype" positioning.** This constrains the brand voice tightly. It prevents the AI from falling back on generic excitement-driven marketing language.

## Step 3: Specify the Output Structure

The prompt defines exactly six sections to produce:

1. Brand Overview (3–4 sentences)
2. Product Definition (name, description, price, features)
3. Target Audience Profile (demographics, mindset, use cases)
4. Brand Positioning (statement, pillars, reasons to believe)
5. Brand Voice & Tone (traits + example copy)
6. Marketing Objective (one campaign goal with parameters)

**Why this matters:** Specifying structure prevents the AI from inventing its own organization, which makes outputs inconsistent across sessions. Each section maps to a downstream workflow:

| Section | Feeds Into |
|---------|-----------|
| Brand Overview | Strategy briefs, campaign briefs |
| Product Definition | Ad copy, landing page content, email product blocks |
| Target Audience | Audience targeting, persona creation, channel selection |
| Brand Positioning | Messaging frameworks, creative direction |
| Brand Voice & Tone | All copy generation (ads, emails, social) |
| Marketing Objective | Campaign planning, budget allocation, performance simulation |

## Step 4: Set Constraints

The prompt includes explicit guardrails:

```
- Keep everything tight and specific
- Do NOT introduce multiple products or audiences
- Do NOT overcomplicate the business model
- Avoid generic marketing language
- Make all outputs usable as direct inputs into downstream AI workflows
```

**Why this matters:** Without these, the AI will naturally expand scope — adding product lines, secondary audiences, and aspirational brand pillars that sound good but make downstream simulation harder to control.

## Step 5: Provide Context on Intended Use

The prompt explains what the brand definition will be used for:

```
This brand will be used to demonstrate:
- AI-generated strategy
- campaign planning
- asset production (ads, emails, landing pages)
- simulated performance
- post-campaign analysis
```

**Why this matters:** The AI makes better structural choices when it knows the downstream use case. Knowing that this feeds into campaign simulations, the AI is more likely to include specific numbers (price points, budget, unit targets) rather than vague descriptors.

## The Output

The AI produced a brand definition with these key specifics:

- **Product:** Yowie Basecamp 45L Pack — a 45-liter backpack in 1680D sailcloth nylon
- **Price:** $385
- **Campaign goal:** 500 units in 30 days, $25K budget, target ROAS of 7.7x
- **Channels:** Meta ads, email (4,200 subscriber list), one landing page

**Decisions the AI made (and why they work):**

- **Chose a backpack over a cooler or bottle.** A pack has more features to describe in copy, a higher price point that justifies premium positioning, and a more complex purchase decision — all of which create richer material for downstream simulations.
- **Set a specific ROAS target (7.7x).** This gives the performance simulation a clear pass/fail threshold. Without it, any simulated result would be ambiguous.
- **Defined list size (4,200 subscribers).** This constrains the email channel realistically. The AI can't simulate sending to 100,000 people when the brand is defined as having 4,200.
- **Single main compartment philosophy.** A product design choice that mirrors the brand positioning ("nothing unnecessary") — this kind of internal consistency makes generated copy more coherent.

## Final Output

See: [`brand_definition.md`](../brand/brand_definition.md)

## What to Do Next

This brand definition becomes the input for the next stage: campaign strategy and planning. Every downstream prompt should reference this document directly so the AI's outputs stay grounded in these specific constraints.

## Replication Checklist

To build your own simulation brand from scratch:

1. Pick a category with a physical product (easier to describe in ads and landing pages)
2. Lock down ONE product, ONE audience, ONE positioning direction
3. Include specific numbers: price, budget, unit targets, list sizes
4. Define brand voice traits that are constraining (not just "friendly" or "authentic")
5. Set a campaign objective with a measurable success metric
6. Write the prompt with explicit output structure and constraints
7. Tell the AI what the output will be used for downstream
