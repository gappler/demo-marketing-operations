---
title: Process Log
type: process_log
version: 1.0
created: 2026-04-05
---

# Process Log

## [2026-04-08 00:00] Skills Inventory and Methodology Notes

**Prompt:**
> List all skills, agents, sub-agents, and tools that were invoked during this project's build sessions. Include the superpowers skills that were called and any MCP servers or external tools used. Then create docs/project_notes.md with the inventory and build methodology pattern as a reusable reference.

**What was built:**
- `docs/project_notes.md` — ongoing project notes file containing:
  - Full skills inventory (superpowers skills, built-in tools, MCP servers)
  - Complete list of 12 tools and supporting artifacts built
  - Reusable build methodology pattern (8 sections covering foundation-first approach, prompt chaining, single-file HTML architecture, process discipline, and skill selection guide)

**Key decisions:**
- Structured as an ongoing log rather than a one-time document, with a marker for appending future entries
- Included YAML metadata header per global preferences
- Documented the sequential prompt-chaining pattern as a reusable reference since it was the core architectural approach

**Files created or modified:**
- `docs/project_notes.md` (created)
- `docs/process_log.md` (modified — this entry)

---

## [2026-04-05 00:00] Customer Segment Analyzer

**Prompt:**
> Build a customer segment analyzer for Yowie. Read the customer order data, identify 3-5 distinct segments based on purchase patterns, geography, and demographics. For each segment, provide a profile, estimated size, lifetime value potential, and a recommended messaging approach that fits Yowie's brand voice. Output as an interactive HTML dashboard with visual breakdowns of each segment.

**What was built:**
- Interactive customer segment dashboard (`tools/customer_segments.html`) identifying 5 segments from 643 orders
- Each segment includes: demographics, purchase patterns, psychographic profile, channel mix, estimated LTV, recommended messaging approach with example copy
- Segment selector tabs, comparison table, revenue doughnut chart, order distribution bar chart
- `tutorials/12_customer_segments.md` — step-by-step build tutorial

**Segments identified:**
1. Core Loyalists (142, 22%) — Mountain West, organic/direct, highest return rate (19%), LTV $620
2. Engaged Subscribers (132, 21%) — PNW, email-driven, WELCOME10 users, LTV $540
3. Discovery Buyers (182, 28%) — paid social, distributed geography, 93% new, LTV $445
4. Gift Buyers (102, 16%) — qty-2 orders (46%), NE heavy, highest AOV ($437), LTV $710
5. Referral Network (85, 13%) — FRIEND15 users, self-reinforcing, highest referral multiplier, LTV $580

**Key decisions:**
- Segments defined by behavioral clusters (purchase patterns + channel + discount codes) not demographics — two 50-year-old men in Montana can be in different segments if one found Yowie via search and the other via a friend's recommendation
- Gift Buyers identified from qty-2 orders cross-referenced with Northeast over-representation and referral channel weight — not obvious from any single dimension
- LTV includes referral multiplier (0.4–1.5 per buyer by segment) — Referral Network has lower initial revenue (FRIEND15 discount) but highest network effect
- Each segment gets a different messaging approach but all stay within Yowie voice — Core gets specs-only, Subscribers get narrative, Discovery gets scroll-stopping hooks, Gifters get relationship framing, Referrals get confirmation-not-persuasion
- Discovery Buyers are the largest segment (28%) but lowest LTV ($445) — volume vs. value tradeoff that directly informs budget allocation decisions

**File paths:**
- `tools/customer_segments.html` (created)
- `tutorials/12_customer_segments.md` (created)

---

## [2026-04-05 00:00] Content Repurposing Tool

**Prompt:**
> Build a content repurposing tool for Yowie. Take this single input: a blog post about the Basecamp 45L for a multi-day Wind River Range trip. Generate repurposed versions for: a LinkedIn post, an Instagram caption, a email newsletter snippet, a Meta ad, and a tweet thread. Each version should match Yowie's brand voice and be formatted appropriately for its platform. Output as an HTML page showing all versions side by side with character counts and platform guidelines.

**What was built:**
- Interactive content repurposing tool (`tools/content_repurposer.html`) showing one source blog post adapted to five platforms
- Source blog post: ~300-word Wind River Range trip report in Yowie voice
- Five platform adaptations: LinkedIn (1,400 chars), Instagram (460 chars), Email newsletter (820 chars), Meta ad (380 chars), Tweet thread (6 tweets)
- Each version includes: platform guidelines, character count with limit bar, brand voice check (5 traits), and adaptation notes explaining what changed
- Comparison strip showing character counts across all platforms at a glance
- `tutorials/11_content_repurposer.md` — step-by-step build tutorial

**Key decisions:**
- Each version is a genuine rewrite, not a truncation — LinkedIn adds first-person authority, Instagram compresses to fragments, tweet thread restructures pacing with punchline in tweet 2
- Source blog post uses the same Wind River Range scenario from Email 3 and the landing page — narrative consistency across the project
- Tweet thread has no hashtags (they read as desperate on X/Twitter) and no engagement bait ("What's your go-to pack?") — Yowie's voice doesn't solicit
- Email version matches the CTA style from the email sequence ("See the Basecamp") — cross-tool consistency
- Meta ad version puts the trip hook in the first 125 characters (before "See more" fold) — specs come after the reader chooses to engage
- All five versions pass all five brand voice checks — the key test is whether the voice survives compression from 300 words to 280 characters

**File paths:**
- `tools/content_repurposer.html` (created)
- `tutorials/11_content_repurposer.md` (created)

---

## [2026-04-05 00:00] Campaign Performance Simulator

**Prompt:**
> Build a campaign performance simulator for Yowie. Let me input total budget, channel split percentages, and campaign duration. It should project impressions, clicks, conversions, revenue, and ROAS based on the historical performance data. Make it interactive — sliders for budget and channel mix, with results updating in real time. Output as an HTML file.

**What was built:**
- Interactive full-funnel campaign simulator (`tools/campaign_simulator.html`) with real-time projections
- Per-channel funnel models derived from historical data: Meta (CPM→CTR→conv), Email (list→opens→clicks→conv), Content/SEO (sessions→conv), Social (reach→clicks→conv)
- Controls: budget ($5K–$100K), duration (7–90 days), season, channel mix sliders, scenario toggle (conservative/expected/optimistic)
- Outputs: 6 KPI cards, goal progress bar, visual conversion funnel, revenue-by-channel doughnut, S-curve daily cumulative chart, full-funnel channel detail table
- `tutorials/10_campaign_simulator.md` — step-by-step build tutorial

**Key decisions:**
- Per-channel funnel models instead of flat ROAS multiplier — shows intermediate metrics (impressions, clicks) that explain how revenue is generated, not just the result
- S-curve (3x²-2x³) for daily cumulative projections — more realistic than linear; matches actual Meta campaign learning/saturation phases
- Email modeled by list size and campaign frequency, not just spend — a $5K email budget and $50K email budget hit the same list; the constraint is audience size, not money
- Scenario modifier applies to conversion rates only (not impressions or clicks) — budget drives volume, scenario affects how well that volume converts
- Diminishing returns trigger at 2x historical monthly average (not 1x) — gives headroom for reasonable scale-up before efficiency degrades
- Three modifiers stack multiplicatively (season × scenario × diminishing) — creates compound effects that mirror real campaign dynamics

**File paths:**
- `tools/campaign_simulator.html` (created)
- `tutorials/10_campaign_simulator.md` (created)

---

## [2026-04-05 00:00] Meta Ad Copy Generator & Scorer

**Prompt:**
> Build a Meta ad copy generator for the Yowie Basecamp 45L campaign. Generate 5 ad variants — headline, primary text, and CTA for each. Then score each variant against Yowie's brand voice guidelines from the brand definition file, rating them on tone, clarity, and brand alignment. Output as an interactive HTML page where I can see the ads and their scores side by side.

**What was built:**
- Interactive Meta ad copy tool (`tools/meta_ad_generator.html`) with 5 ad variants rendered as realistic Facebook feed previews
- Each variant scored on 5 brand voice dimensions (plainspoken, confident, restrained, respectful, dry) with weighted overall score
- Ranked summary strip, per-dimension score bars, expandable scoring rationale per ad
- Scoring methodology section explaining weights and evaluation criteria
- `tutorials/09_meta_ad_generator.md` — step-by-step build tutorial

**Ad variants:**
1. Product Introduction (8.9) — "One pack. Sailcloth nylon. Lifetime warranty."
2. Materials Story (9.3, top pick) — "What sailcloth nylon actually means"
3. Anti-Hype Positioning (8.7) — "No influencers. No hype. Just the pack."
4. Warranty / Price (8.8) — "The last pack you buy."
5. Experience (8.8) — "Five days. Thirty-five pounds. No complaints."

**Key decisions:**
- Materials Story variant scores highest because "It's fine. It works. It wears out." is peak Yowie voice — plainspoken, dry, devastating; the materials angle is the most natural home for the brand voice
- Plainspoken and Restrained weighted equally at 25% each — for this brand, saying too much and pushing too hard are the two biggest voice violations
- CTA is "Learn More" on all five variants (not "Shop Now") — consistent with restrained positioning
- Anti-Hype variant scores lowest on Restrained (8.0) — directly calling out competitor tactics is more aggressive than the typical Yowie voice, which prefers to simply be different
- Meta ad preview mimics actual Facebook feed format — avatar, "Sponsored" tag, link bar layout — so copy can be evaluated in context
- Scoring rationale is expandable (hidden by default) — scores at a glance, detail on demand

**File paths:**
- `tools/meta_ad_generator.html` (created)
- `tutorials/09_meta_ad_generator.md` (created)

---

## [2026-04-05 00:00] Competitive Intelligence Tracker

**Prompt:**
> Build a competitive intelligence tracker that compares Yowie against YETI, Stanley, Hydro Flask, and Osprey. Include product positioning, price points, target audience, marketing channels used, strengths and weaknesses. Make it an interactive HTML dashboard where I can compare any two brands side by side. Use web search to pull real current data on the competitors.

**What was built:**
- Interactive competitive intelligence dashboard (`tools/competitive_intel.html`) with side-by-side brand comparison
- Five brands profiled: Yowie, YETI, Stanley, Hydro Flask, Osprey — each with 13+ comparison dimensions and full SWOT
- Brand selector for any-two comparison, positioning bubble chart (price vs. audience age vs. revenue), channel usage matrix, full landscape table
- Contextual Yowie advantage callouts when comparing against each competitor
- `tutorials/08_competitive_intel.md` — step-by-step build tutorial

**Key decisions:**
- Included indirect competitors (Stanley, Hydro Flask) alongside direct (Osprey) — understanding why Yowie is different from Stanley is as strategically valuable as how it competes with Osprey
- Positioning map uses price as X-axis and audience age center as Y-axis — reveals that Yowie occupies a unique position (high price + older audience) with no competitor nearby
- Channel matrix uses a 12-channel boolean grid — shows Yowie uses 7/12 channels vs Osprey/YETI at 12/12, making the scale difference immediately visible
- SWOT includes honest Yowie weaknesses (no brand awareness, single product, small budget) — credibility requires acknowledging limitations
- Competitive insights are strategic, not promotional — they acknowledge competitor strengths ("Osprey has 50 years of brand trust")
- Revenue represented as bubble size on positioning map — gives visual weight to how established each competitor is

**File paths:**
- `tools/competitive_intel.html` (created)
- `tutorials/08_competitive_intel.md` (created)

---

## [2026-04-05 00:00] Campaign Landing Page

**Prompt:**
> Build a landing page for the Yowie Basecamp 45L campaign. Use the brand definition for voice and messaging. Include hero section, product features, social proof section, and a clear CTA. Make it responsive. Output as a single HTML file I can open in a browser.

**What was built:**
- Single-file responsive landing page (`tools/landing_page.html`) with 8 sections: hero, intro, feature grid (6 cards), materials deep-dive, specs table, social proof (4 testimonials), warranty with cost-per-trip math, and final CTA
- Scroll-triggered reveal animations via IntersectionObserver (no dependencies)
- Sticky nav with scroll-state transition
- Full responsive design (desktop, tablet, mobile)
- `tutorials/07_landing_page.md` — step-by-step build tutorial

**Key decisions:**
- Editorial luxury aesthetic (Cormorant Garamond + Source Serif 4 + IBM Plex Mono) — reads like a magazine feature, not a Shopify template
- Dark/light alternating sections create rhythm without visual clutter
- Social proof uses specific locations and experience levels ("Bozeman, MT, 22 years backcountry") — this audience judges credibility by specificity, not star ratings
- Warranty section includes the same cost-per-trip comparison table from Email 4 — converts $385 objection into $5/trip rational argument
- CTA echoes Email 5 language ("Still here when you're ready") — consistency across touchpoints
- No urgency language, no countdown timer — the brand voice forbids it and the audience sees through it
- Image areas are gradient placeholders with text markers — page works visually without hosted images
- Zero JS dependencies — vanilla IntersectionObserver for reveals, scroll listener for nav

**File paths:**
- `tools/landing_page.html` (created)
- `tutorials/07_landing_page.md` (created)

---

## [2026-04-05 00:00] Campaign Email Sequence

**Prompt:**
> Build an email sequence generator for Yowie's Basecamp 45L campaign. It should create a 5-email nurture series for the 4,200-subscriber list, using the brand voice from the brand definition file. Each email should have a subject line, preview text, body copy, and a clear CTA. Output as both individual HTML email templates and a markdown overview of the full sequence with send timing recommendations.

**What was built:**
- Strategic markdown overview (`tools/email_sequence/sequence_overview.md`) with full copy, send schedule, voice guidelines, and performance projections
- Five production-ready HTML email templates with inline CSS, table-based layout, dark mode support, and ESP merge tags
- `tutorials/06_email_sequence.md` — step-by-step build tutorial

**Sequence:**
1. Day 1 — "One pack. That's it." (announcement)
2. Day 5 — "What sailcloth nylon actually means" (materials proof)
3. Day 12 — "Five days in the Wind River Range" (use case)
4. Day 20 — "The warranty is simple" (objection handling / de-risk)
5. Day 27 — "Still here when you're ready" (closing)

**Key decisions:**
- Trust arc, not pressure arc — no urgency tactics, no countdown timers, no "limited stock." This audience sees through it.
- Email 4 has no hero image — the warranty/price argument is logical, not visual; a product photo would undercut the financial seriousness
- Email 5 is 72 words — the shortest email proves the brand voice more than any other; restraint is the message
- Consistent CTA language across all 5 ("See the Basecamp") — avoids escalating urgency that would violate the brand voice
- Table-based HTML with inline CSS for email client compatibility (Outlook, Yahoo, older Gmail strip style blocks)
- 7 AM weekday / 8 AM Saturday send times — based on the 40–65 demographic's email behavior patterns
- Sequence ends Day 27 with 3 days of silence before campaign close — no frantic last-day blast

**File paths:**
- `tools/email_sequence/sequence_overview.md` (created)
- `tools/email_sequence/email_01_announcement.html` (created)
- `tools/email_sequence/email_02_materials.html` (created)
- `tools/email_sequence/email_03_use_case.html` (created)
- `tools/email_sequence/email_04_warranty.html` (created)
- `tools/email_sequence/email_05_closing.html` (created)
- `tutorials/06_email_sequence.md` (created)

---

## [2026-04-05 00:00] Interactive Budget Allocator

**Prompt:**
> Build a budget allocator tool for Yowie's $25K campaign. It should read the historical channel performance data, calculate ROI by channel, and recommend an optimal budget split across Meta, email, and other channels. Make it interactive — let me adjust the total budget and see how the allocation changes. Output as an HTML file.

**What was built:**
- Interactive single-file HTML budget allocator (`tools/budget_allocator.html`) with real-time projections
- Five channels modeled: Meta Ads, Email, Content/SEO, Social Organic, Landing Page
- Three allocation modes: Optimized (efficiency-weighted), Balanced (equal), Manual (sliders)
- Adjustable budget ($5K–$75K), duration (14–90 days), target season, and per-channel locks
- Projections include revenue, units, ROAS, CAC — tracked against the 500-unit campaign goal
- `tutorials/05_budget_allocator.md` — step-by-step build tutorial

**Key decisions:**
- Efficiency scoring combines ROAS (60%) with conversion volume (40%) — prevents high-ROAS-low-volume channels like content from dominating the allocation
- Diminishing returns modeled per channel (Meta 8%/\$10K, Email 2%, Content 3%, Social 4%) — stops the optimizer from concentrating 100% into one channel
- Seasonal multipliers (winter 0.60x, spring 0.92x, summer 1.33x, fall 1.02x) reuse the same index from data generation for consistency
- Email and Content/SEO costs estimated from industry norms ($80/mo ESP, $300/mo content) since CSVs don't include cost data for these — estimates are conservative to keep ROI claims defensible
- Landing page treated as an enabler with no direct attribution — conversions flow through it but are credited to the traffic source
- Channel locking with automatic redistribution — lock one channel's share and the remaining budget normalizes across unlocked channels

**File paths:**
- `tools/budget_allocator.html` (created)
- `tutorials/05_budget_allocator.md` (created)

---

## [2026-04-05 00:00] Monthly Report Generator

**Prompt:**
> Build a tool that reads the Yowie marketing data files and generates a written monthly report with key metrics, trends, insights, and recommendations. Output it as a formatted markdown file. Use the Yowie brand voice from the brand definition.

**What was built:**
- Python script (`tools/generate_monthly_report.py`) that reads all 6 CSV data files, analyzes any month, and outputs a formatted markdown report
- Supports three modes: latest month (default), specific month (`2025-07`), or all 12 months (`--all`)
- Reports include: summary paragraph, key metrics table with MoM deltas, channel breakdowns (Meta/email/web/social), order analysis (region/channel/discount), YTD aggregates, conditional insights (3-5), and actionable recommendations (2-4)
- `tutorials/04_monthly_report_generator.md` — step-by-step build tutorial

**Key decisions:**
- Zero dependencies (csv + standard library only) — runs on any machine with Python 3, no pip install needed
- Analysis functions return dicts, presentation is separate — keeps analysis reusable for different output formats later
- Insights are conditional, not exhaustive — only surfaces observations relevant to this specific month's data (ROAS thresholds, CAC movement, seasonal timing)
- Recommendations are specific and opinionated ("increase spend 15-20%", "pull back 20%") rather than vague ("consider adjusting") — matches Yowie's plainspoken voice
- Tested with peak (July, 7.35x ROAS → recommends increasing spend), trough (January, 3.94x → recommends pulling back), and spring (March → recommends seasonal prep) to verify tone adapts
- Reports are not pre-generated — the script runs on demand so downstream users see the tool in action

**File paths:**
- `tools/generate_monthly_report.py` (created)
- `tutorials/04_monthly_report_generator.md` (created)

---

## [2026-04-05 00:00] Marketing Performance Dashboard

**Prompt:**
> Build a marketing performance dashboard for Yowie that reads the data files in the data folder and visualizes key metrics — monthly revenue, customer acquisition cost, channel spend vs. return, email performance, and web traffic trends. Make it an interactive HTML file I can open in a browser.

**What was built:**
- Single-file interactive HTML dashboard (`tools/dashboard.html`) with 6 KPI cards, 6 chart panels, seasonal indicator bar, and monthly detail table
- Uses Chart.js (CDN) with custom earth-toned styling matching Yowie brand identity
- Data embedded as JS objects for `file://` compatibility — no server needed
- `tutorials/03_performance_dashboard.md` — step-by-step build tutorial

**Key decisions:**
- Single HTML file with embedded data instead of fetching CSVs — avoids CORS issues with `file://` protocol, works with a double-click
- Utilitarian field-notebook aesthetic (dark earth tones, monospace data, serif headers) — derived from Yowie's brand identity rather than using a generic dashboard template
- Pre-aggregated order data by region instead of embedding all 643 rows — dashboard needs composition view, not individual records
- Six KPIs chosen to answer the first stakeholder questions: revenue, units, AOV, ROAS, CAC, list growth
- Tabbed email panel (rates vs. list growth) instead of cramming both into one chart
- DM Mono + Instrument Serif font pairing — monospace for data precision, serif for quiet authority

**File paths:**
- `tools/dashboard.html` (created)
- `tutorials/03_performance_dashboard.md` (created)

---

## [2026-04-05 00:00] Historical Marketing Data Generation

**Prompt:**
> Generate 12 months of historical marketing data for Yowie. Include monthly CSVs for web traffic by source, email campaign performance, Meta ad spend and results, social media engagement, and customer orders. Make the data realistic with seasonal patterns — stronger summer and fall, weaker winter. Save everything to a data/ folder.

**What was built:**
- Python generation script (`data/generate_historical_data.py`) producing 6 CSV files
- `web_traffic.csv` — 60 rows (5 sources × 12 months), sessions/bounce/pages/duration
- `email_campaigns.csv` — 27 rows (2–3 campaigns/month), full funnel from sends to revenue
- `meta_ads.csv` — 12 rows, spend/impressions/clicks/conversions/ROAS
- `social_media.csv` — 24 rows (Instagram + Facebook), reach/engagement/growth
- `orders.csv` — 643 individual order records with attribution, region, discount codes
- `monthly_summary.csv` — 12-row cross-channel rollup
- `tutorials/02_historical_data_generation.md` — step-by-step tutorial

**Key decisions:**
- Used a shared seasonal multiplier array across all datasets — creates natural cross-channel correlation without manual alignment
- Python script with seed (42) instead of hand-crafted CSVs — ensures reproducibility and internal consistency (conversions derive from clicks derive from impressions)
- Email list starts at 2,800 and grows to ~3,930 by March 2026 — reaches the brand-defined 4,200 by campaign launch in April 2026
- Annual volume of ~690 units / $260K revenue — deliberately modest to match a small premium DTC brand with a 4,200-person email list
- Individual order records instead of monthly aggregates — supports cohort analysis, regional breakdowns, and discount code analysis in downstream workflows
- Included a monthly_summary.csv rollup — most downstream AI prompts will reference this first rather than joining five files

**File paths:**
- `data/generate_historical_data.py` (created)
- `data/web_traffic.csv` (generated)
- `data/email_campaigns.csv` (generated)
- `data/meta_ads.csv` (generated)
- `data/social_media.csv` (generated)
- `data/orders.csv` (generated)
- `data/monthly_summary.csv` (generated)
- `tutorials/02_historical_data_generation.md` (created)

---

## [2026-04-05 00:00] Tutorials Folder and Tutorial Rule

**Prompt:**
> Create a tutorials/ folder. After each tool we build, generate a step-by-step tutorial documenting how we built it — the prompts used, the decisions made, and the final output. Write it as if teaching someone to replicate this from scratch.

**What was built:**
- `tutorials/` directory
- Tutorial rule added to CLAUDE.md requiring a tutorial after each deliverable
- `tutorials/01_brand_definition.md` — retroactive tutorial covering the brand definition build, including the full prompt breakdown, decision rationale, output-to-downstream mapping table, and a replication checklist

**Key decisions:**
- Zero-padded sequential numbering (`01_`, `02_`) — keeps tutorials in build order and sorts correctly in file listings
- Backfilled the brand definition as tutorial 01 rather than skipping it — the first deliverable is the most important one to document since everything downstream depends on it
- Structured each tutorial around the prompt engineering choices, not just the output — the goal is teaching someone to write effective prompts, not just showing results
- Included a section-to-downstream-workflow mapping table — makes explicit how each part of the brand definition feeds into later stages

**File paths:**
- `CLAUDE.md` (modified — added Tutorials section)
- `tutorials/01_brand_definition.md` (created)

---

## [2026-04-05 00:00] Project Rules and Process Logging

**Prompt:**
> Add a project rules section to CLAUDE.md that requires you to log every task to process-log.md with the prompt I gave, what was built, key decisions, file paths, and a timestamp.

**What was built:**
- Project-level CLAUDE.md with process logging rules
- process_log.md initialized with format and this entry

**Key decisions:**
- Used reverse chronological order so the most recent work is always at the top
- Named the file `process_log.md` (underscore) per global naming convention in ~/.claude/CLAUDE.md
- Defined a consistent markdown template for entries to keep logs machine-parseable

**File paths:**
- `CLAUDE.md`
- `process_log.md`

---

## [2026-04-05 00:00] Yowie Brand Definition

**Prompt:**
> You are a senior brand strategist and marketing systems architect. Your task is to create a fictional but realistic brand designed specifically for demonstrating AI-driven marketing automation across a full lifecycle (strategy → planning → production → execution → analysis → post-mortem). This is NOT a creative writing exercise. The goal is to produce a clear, structured, and constrained brand that can be used as a controlled teaching system. [Design a simulated DTC brand called "Yowie"...]

**What was built:**
- Complete brand definition document covering: brand overview, product definition (Basecamp 45L Pack, $385), target audience profile, positioning statement with messaging pillars and reasons to believe, brand voice and tone with example copy, and a campaign simulation objective (500 units / 30 days / $25K budget)

**Key decisions:**
- Chose a 45L backpack as the hero product — provides rich feature set for copy generation while staying tangible and easy to understand
- Set price at $385 — high enough to signal premium, low enough to be plausible DTC without retail markup
- Defined a $25K campaign budget with specific ROAS target (7.7x) — gives downstream simulations hard constraints to work against
- Single main compartment design philosophy — reinforces the "nothing unnecessary" brand pillar at the product level

**File paths:**
- `brand/brand_definition.md`

---

## [2026-04-05 00:00] Project Directory Reorganization

**Prompt:**
> Reorganize this project directory into a clean folder structure. Group files logically — brand assets, data, tools, tutorials, documentation. Move existing files where they belong and update any file references in CLAUDE.md.

**What was built:**
- Clean folder structure: `brand/`, `docs/`, `tools/`, `data/`, `tutorials/`
- Moved `brand_definition.md` → `brand/brand_definition.md`
- Moved `process_log.md` → `docs/process_log.md`
- Updated all file path references in CLAUDE.md, process_log.md, and tutorials/01_brand_definition.md

**Key decisions:**
- `brand/` instead of `assets/` — "assets" is ambiguous and will collide with creative assets later; `brand/` is specific to foundational brand documents
- `tools/` for future AI workflow scripts and prompt templates — keeps them separate from brand inputs and campaign outputs
- `data/` for future simulated performance metrics and campaign data — clean separation from source documents
- `docs/` for process log and project-level documentation — not tutorials (those have their own folder) and not brand (that's strategic input)
- Kept `tutorials/` at root level — it's a primary output of this project, not a subcategory of docs
- `CLAUDE.md` stays at project root — required location for project rules

**File paths:**
- `brand/brand_definition.md` (moved from root)
- `docs/process_log.md` (moved from root)
- `tools/` (created, empty)
- `data/` (created, empty)
- `CLAUDE.md` (modified — updated process_log path)
- `tutorials/01_brand_definition.md` (modified — updated brand_definition reference)

---
