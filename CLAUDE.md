# Project Rules

## Process Logging

Every task must be logged to `docs/process_log.md`. Each entry must include:

- **Timestamp** — date and time the task was completed
- **Prompt** — the full user prompt that initiated the task
- **What was built** — concise description of deliverables produced
- **Key decisions** — non-obvious choices made during execution and why
- **File paths** — all files created or modified

Log entries are appended in reverse chronological order (newest first). Use the following format:

```
## [YYYY-MM-DD HH:MM] Task Title

**Prompt:**
> (full user prompt)

**What was built:**
- (deliverables)

**Key decisions:**
- (decision — rationale)

**File paths:**
- (paths)

---
```

## Tutorials

After each tool or deliverable is built, generate a step-by-step tutorial in the `tutorials/` folder. Tutorials must:

- Document the exact prompts used to produce the output
- Explain key decisions and why they were made
- Show the final output (or reference the file path)
- Be written as if teaching someone to replicate the work from scratch
- Follow the naming convention: `tutorials/NN_short_name.md` (zero-padded, sequential)

Tutorials are learning artifacts — they should be clear, honest about tradeoffs, and useful to someone who has never seen this project before.
