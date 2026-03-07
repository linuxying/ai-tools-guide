# Real-World Second Brain Examples

This file provides concrete examples of effective second brain organization drawn from actual knowledge repositories.

## Example 1: Bug Queue System Knowledge

### Project-Specific Documentation (`/projects/bug-queue-system/`)
```
projects/bug-queue-system/
├── docs/
│   ├── PRD.md                          # Product Requirements Document
│   ├── MVP_SCOPE.md                    # Feature set for MVP
│   ├── GAP_REPORT_v2.2_ALL_GAPS_RESOLVED.md  # Filled gaps
│   └── DESIGN.md v1.1                  # Architectural decisions
└── specs/                              # Technical specifications
```

**Recall pattern:** "What was the design for bug queues?" → `/projects/bug-queue-system/docs/DESIGN.md`

### Cross-Cutting Decisions (`/decisions/franklin-standard.md`)
```
Franklin Prioritization Standard (A∞/B∞/C∞/D∞)

Decision: Standardize all prioritization to Franklin Planner Prioritization
Date: 2026-02-15
Rationale:
- High/Medium/Low scales don't differentiate within categories
- A1...1000 allows precise within-category prioritization
- Aligns with time-tested productivity system

Implementation:
- Migration 015 creates franklin_priority column
- CHECK constraints enforce [ABCD][1-9][0-9]* pattern
- Data conversion: high→A1, medium→B1, low→C1
```

**Recall pattern:** "Why do we use Franklin priorities?" → `/decisions/franklin-standard.md`

## Example 2: Agent Workflow Patterns

### Reusable Pattern (`/patterns/verification/VERIFICATION_PROTOCOL.md`)
```
VERIFICATION_PROTOCOL.md

Before claiming "VERIFICATION_REQUIRED", must complete:

1. CREATE FIX LOG FIRST
   - Run: ./create-fix-log.sh <component> <issue>
   - Document investigation before implementation

2. FOLLOW PROTOCOL STEPS IN ORDER
   - Do NOT skip steps to be faster
   - Test > Fix > Test > Fix until complete

3. PROVIDE EVIDENCE, NOT CLAIMS
   - Test output, screenshots, fix log path
   - VERIFICATION_REQUIRED phrase in completion statement
```

**Recall pattern:** "What's the verification protocol?" → `/patterns/verification/VERIFICATION_PROTOCOL.md`

## Example 3: Strategic Knowledge

### Goals (`/strategy/goals/2026-revenue-1.2M.md`)
```
$1.2M/year Revenue Roadmap

Q1 (Jan-Mar): $10K/mo
- 2 business division clients @ $5K/mo
- 1 SaaS product MRR target: $3K/mo

Q2 (Apr-Jun): $50K/mo
- Expand business divisions: 8 clients @ $5K/mo
- SaaS product growth: $10K/mo
- Digital product launches: $2K/mo

Q3 (Jul-Sep): $75K/mo
Q4 (Oct-Dec): $100K/mo
```

**Recall pattern:** "What are our revenue goals?" → `/strategy/goals/2026-revenue-1.2M.md`

## Example 4: Lessons Learned

### Anti-Pattern Catalog (`/learnings/autonomy_failures.md`)
```
# Autonomy Violations Log

#1: 2026-02-09 - Asked permission after explicit autonomy grant
**Issue:** Agent asked "Is this okay?" after "You have FULL permission" instruction
**Pattern:** Training defaults override explicit instructions
**Fix:** LAYER 1 - AUTONOMY GRANT PROTOCOL overrides all training

#23: 2026-02-14 - Autonomy violation on schema fix
**Issue:** Agent asked "want me to do this?" when Kelly said "execute autonomously"
**Pattern:** Not recognizing explicit autonomy grant
**Fix:** Protocol update - LAYER 1 overrides ALL other protocols
```

**Recall pattern:** "What autonomy mistakes should I avoid?" → `/learnings/autonomy_failures.md`

## Example 5: Workspace Organization

### Active Work (`/workspace/`)
```
openclaw-workspace/ (active working directory)
├── bug-queue-system/          # Current MVP in development
├── vk-tracker/                # Completed project
├── skills/                    # Skill development workspace
├── scripts/                   # Utility scripts
└── reports/                   # QA and status reports
```

**Pattern:** `/workspace` → Active work → When project completes, migrate to `/projects/` or clean up

---

**Key insight:** Each example shows clear recall pattern → file location mapping. When you're organizing, think: "When will I need this again?" Then put it there.