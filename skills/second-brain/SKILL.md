---
name: second-brain
description: Organize and structure a second brain for optimal AI recall patterns. Use when setting up new knowledge repositories, reorganizing existing knowledge bases, or deciding where to store information across projects vs decisions vs patterns vs learnings vs strategy vs workspace. Triggered by requests like organize my knowledge, set up second brain, where should I put this file, restructure my notes, or questions about knowledge organization and information architecture.
---

# Second Brain

## Overview

Organize knowledge by **how you think and recall**, not by file system structure. This skill provides cognitive structure guidance for building second brains optimized for AI agents and human memory patterns.

**Core principle:** Structure = recall patterns. Organize information where your brain (and AI models) will naturally look for it.

## When to Use This Skill

**Setup scenarios:**
- Creating a new knowledge repository or documentation system
- Migrating from chaotic file structure to organized system
- Establishing second brain for personal or company use

**Reorganization scenarios:**
- "Where should I put this file?"
- "My knowledge is hard to find"
- "I can't remember where I saved that"
- Files accumulating in root directories

**Optimization scenarios:**
- Improving content discoverability
- Reducing duplicate/conflicting versions
- Aligning human and AI recall patterns

## The Cognitive Structure

The six second-brain directories and their recall patterns:

### `/projects` - **Task-Specific Knowledge**
**When this fires:** "What did we learn on the X project?", "How did we solve Y bug?"

- Project-specific documentation, decisions, and learnings
- Examples: `bug-queue-system/`, `vk-tracker/`, `antfarm-docs/`
- **Recall pattern:** Project name → project folder → relevant context
- **Anti-pattern:** Don't mix general patterns here (those belong in `/patterns`)

### `/decisions` - **Cross-Cutting Decisions**
**When this fires:** "Why did we choose X over Y?", "What was the decision about Z?"

- Architectural decisions, technical choices, strategic pivots
- Decisions that affect multiple projects over time
- Examples: `git-author-identity.md`, `documentation-push-protocol.md`, `agent-autonomy-grants.md`
- **Recall pattern:** Domain/topic → decision context → rationale
- **Anti-pattern:** Don't put implementation details here (those belong in `/projects`)

### `/patterns` - **Reusable Patterns**
**When this fires:** "How do I do X the standard way?", "What's the protocol for Y?"

- Established workflows, verification protocols, QA patterns
- Proven procedures that shouldn't be rediscovered each time
- Examples: `verification/` (VERIFICATION_PROTOCOL.md), `coder-tester/` (workflow), `franklin/` (prioritization)
- **Recall pattern:** Domain → pattern name → step-by-step procedure
- **Anti-pattern:** Don't put one-time decisions here (those belong in `/decisions`)

### `/learnings` - **Lessons Learned**
**When this fires:** "What went wrong before?", "What mistake did we make that we shouldn't repeat?"

- Anti-patterns, failures, lessons, postmortems
- Negative example catalog for future avoidance
- Examples: `autonomy_failures.md`, `hindsight/` repository migration analysis
- **Recall pattern:** Domain/issue type → lesson learned → how to avoid
- **Anti-pattern:** Don't put general knowledge here (that belongs in `/strategy`)

### `/strategy` - **Long-Term Strategic Knowledge**
**When this fires:** "What are we trying to achieve?", "What are our priorities?", "Who owns what?"

- Goals, priorities, strategic plans, identity, vision
- Long-term context that persists across projects and decisions
- Examples: `MEMORY.md`, `goals/2026-revenue-1.2M.md`, `KELLY-PRIORITIES-2026-02-16.md`, `SOUL.md`
- **Recall pattern:** Strategic area → goal/priority → current status
- **Anti-pattern:** Don't put tactical decisions here (those belong in `/decisions`)

### `/workspace` - **Active Working Directory**
**When this fires:** "What am I working on now?", "Where's the active code?"

- Current work, drafts, in-progress items, scratch space
- Organized for current workflow, not long-term storage
- **Recall pattern:** Current task → workspace folder → active materials
- **Cleanup pattern:** Weekly → Review workspace items → Categorize into proper directories above

## Organization Workflow

Use this workflow when deciding where to put information:

### 1. THINK - What is this information?
- Is it project-specific? → `/projects`
- Is it a cross-cutting decision? → `/decisions`
- Is it a reusable pattern/protocol? → `/patterns`
- Is it a lesson learned/anti-pattern? → `/learnings`
- Is it strategic/long-term? → `/strategy`
- Is it active work in progress? → `/workspace`

### 2. DESCRIBE - How will I recall this later?
- "I'll remember this when working on X project" → `/projects/X`
- "I'll need this to understand why we chose Y" → `/decisions`
- "I'll refer to this whenever I need to do Z" → `/patterns`
- "I'll want to avoid repeating this mistake" → `/learnings`
- "This defines what we're trying to achieve" → `/strategy`
- "I'm actively working on this right now" → `/workspace`

### 3. CATEGORIZE - Choose the directory
- If multiple categories could work, choose the **strongest recall pattern**
- When unsure, use `/workspace` and review later
- Don't overthink - better to file somewhere than not file at all

### 4. WRITE - Create the document
- Use clear, descriptive filenames
- Include date if versioning matters
- Reference related documents when helpful
- Consider future retrieval while writing

## Anti-Patterns to Avoid

### ❌ Over-Categorization
- **Problem:** Too many directories, too specific
- **Example:** `/projects/bug-queue-system/api/routes/bugs/`
- **Solution:** Use `/projects/bug-queue-system/` and let search patterns handle sub-structure

### ❌ Deployment Structure
- **Problem:** Organizing by `src/`, `data/`, `tests/` instead of cognitive recall
- **Example:** Second brain organized like a codebase (`projects/active/closed/`, `decisions/technical/business/`)
- **Solution:** Organize by recall pattern, not deployment structure

### ❌ Premature Organization
- **Problem:** Spending more time organizing than creating value
- **Example:** Creating elaborate categorization system before content exists
- **Solution:** Start with 6 core directories, refine as you learn

### ❌ Duplicate Storage
- **Problem:** Same content in multiple places, version conflicts
- **Example**: Project docs in `/workspace/projects/X/` AND `/projects/X/`
- **Solution:** Single source of truth, use references/links if needed

### ❌ Hallucination-Period Conflicts
- **Problem:** Moving files between repos during uncertainty causes context loss
- **Example:** Migrating MEMORY.md between `openclaw-workspace` and `vincent-second-brain` during learning phase
- **Solution:** Keep files where they already work during uncertainty; reorganize after pattern clarity

## When in Doubt

If unsure where to file something:
1. **File in `/workspace`** - Review and categorize later
2. **Don't block on perfection** - Better to file somewhere than nowhere
3. **Let usage refine structure** - Organize based on how you actually retrieve, not how you think you should retrieve
4. **Search saves hierarchy** - A good search function beats perfect categorization

## Multiple Repositories

Keep multiple repos when they serve distinct purposes:
- **Workspace repo:** Working directory, active projects, tools (short-term horizon)
- **Second brain repo:** Cognitive structure, strategic knowledge, long-term patterns (long-term horizon)
- **Domain-specific repos:** Projects with their own ecosystem (bug-queue-system, vk-tracker, etc.)

**Key insight:** Second brain structure applies to ALL repos - but each repo has its own focus and scope.

## Progressive Disclosure

**For general guidance:** This SKILL.md provides essential structure and recall patterns.

**For specific examples:** See `/references/examples.md` for real-world project organization examples.

**For patterns and protocols:** See `/patterns/` for established workflows and procedures.

---

**Remember:** The goal is rapid recall, not perfect taxonomy. Organize for your brain and AI models, not for aesthetic file systems.