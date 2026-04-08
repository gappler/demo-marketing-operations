---
title: Project Notes
project: demo-marketing-operations
created: 2026-04-08
version: 1
---

# Project Notes

Ongoing log of insights, methodology notes, and reusable patterns for this project.

---

## Skills Inventory

### Superpowers Skills Called

| Skill | Purpose |
|-------|---------|
| `superpowers:brainstorming` | Initial brand conceptualization (Yowie brand definition) |
| `superpowers:writing-plans` | Planning the 12-tool sequential workflow |
| `superpowers:executing-plans` | Executing the implementation plan across all 12 tools |
| `frontend-design:frontend-design` | Used for 8 interactive HTML tools (dashboard, budget allocator, landing page, campaign simulator, meta ad generator, competitive intel, content repurposer, customer segments) |

### Claude Code Built-in Tools

| Tool | Usage |
|------|-------|
| Read | Reading existing files for context |
| Write | Creating new files (48 total files created) |
| Edit | Modifying files incrementally |
| Bash | Running Python scripts, git commands |
| Glob / Grep | File discovery and content search |
| Agent | Subagent dispatching for parallel or isolated work |

### MCP Servers / External Tools

None. The project uses zero external APIs, no MCP servers, no Claude API/SDK imports, and no remote triggers. Everything is self-contained.

### What Was Built (12 Tools)

1. Brand Definition (`brand/brand_definition.md`)
2. Historical Data Generator (`data/generate_historical_data.py` + 6 CSVs)
3. Marketing Dashboard (`tools/dashboard.html`) — Chart.js
4. Monthly Report Generator (`tools/generate_monthly_report.py`)
5. Budget Allocator (`tools/budget_allocator.html`)
6. Email Sequence (`tools/email_sequence/` — 5 HTML templates)
7. Landing Page (`tools/landing_page.html`)
8. Competitive Intelligence (`tools/competitive_intel.html`)
9. Meta Ad Generator (`tools/meta_ad_generator.html`)
10. Campaign Simulator (`tools/campaign_simulator.html`)
11. Content Repurposer (`tools/content_repurposer.html`)
12. Customer Segments Analyzer (`tools/customer_segments.html`)

### Supporting Artifacts

- Process log (`docs/process_log.md`) — full task history with timestamps and prompts
- 12 tutorials (`tutorials/01_*.md` through `tutorials/12_*.md`)
- 12 monthly reports (`docs/report_2025_*.md`, `docs/report_2026_*.md`)
- Guided tour (`index.html`) — interactive showcase page

---

## Build Methodology Pattern

A reusable reference for prompt-chained project builds.

### 1. Foundation First

Start with a brand/domain definition that establishes vocabulary, constraints, and design language. Every subsequent tool inherits from this foundation. In this project, `brand/brand_definition.md` set the tone, palette, typography, and strategic positioning that all 12 tools referenced.

### 2. Generate Realistic Data Early

Before building any visualization or analysis tool, generate synthetic but plausible historical data. This gives every downstream tool concrete material to work with rather than placeholder content. The Python data generator (`data/generate_historical_data.py`) produced 6 CSVs covering 12 months of marketing metrics.

### 3. Sequential Prompt Chaining

Each tool's output feeds into the next tool's input. The build order matters:

```
Brand Definition
  → Historical Data
    → Dashboard (visualizes data)
      → Monthly Reports (analyzes data)
        → Budget Allocator (informed by reports)
          → Email Sequence (uses brand voice)
            → Landing Page (extends email campaign)
              → Competitive Intel (positions brand)
                → Meta Ad Generator (uses brand + competitive data)
                  → Campaign Simulator (projects from all inputs)
                    → Content Repurposer (adapts existing content)
                      → Customer Segments (synthesizes all data)
```

### 4. Single-File HTML Architecture

All interactive tools are self-contained HTML files with embedded CSS and JavaScript. Benefits:

- **No build step** — works immediately with `file://` protocol
- **No server required** — no CORS issues, no dependencies to install
- **Portable** — each file is a complete, shareable artifact
- **Data embedded** — CSV data converted to JavaScript objects inline

### 5. Process Discipline via CLAUDE.md

Project rules enforced three practices automatically:

- **Process logging** — every task appended to `docs/process_log.md` with timestamp, prompt, decisions, and file paths
- **Tutorials** — each tool documented with step-by-step replication instructions in `tutorials/`
- **Git discipline** — commit after each tool, not in batches

### 6. Zero External Dependencies

- Python scripts use only the standard library
- HTML tools use vanilla JavaScript (Chart.js loaded via CDN is the sole exception)
- No package.json, no requirements.txt, no build tooling

This keeps the project reproducible without environment setup.

### 7. Brand-Aligned Design System

Rather than generic styling, derive a design system from the brand definition:

- Typography choices (Cormorant Garamond, Source Serif 4, IBM Plex Mono)
- Color palette (earth-toned, utilitarian)
- Layout patterns (understated, functional)

This creates visual coherence across all 8 HTML tools without a shared CSS framework.

### 8. When to Use Which Skill

| Situation | Skill |
|-----------|-------|
| Starting a new project or feature | `superpowers:brainstorming` |
| Planning multi-step implementation | `superpowers:writing-plans` |
| Executing a written plan | `superpowers:executing-plans` |
| Building any web UI or page | `frontend-design:frontend-design` |
| Debugging unexpected behavior | `superpowers:systematic-debugging` |
| Multiple independent tasks | `superpowers:dispatching-parallel-agents` |
| Verifying work before completion | `superpowers:verification-before-completion` |
| Finishing a feature branch | `superpowers:finishing-a-development-branch` |

---

*Add new entries above this line.*
