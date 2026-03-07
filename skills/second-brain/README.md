# Second Brain Skill for OpenClaw

An OpenClaw skill that provides cognitive structure guidance for building second brains optimized for AI agents and human memory patterns.

## Overview

Organize knowledge by **how you think and recall**, not by file system structure. This skill provides a proven framework for knowledge organization that aligns human and AI recall patterns.

**Core principle:** Structure = recall patterns. Organize information where your brain (and AI models) will naturally look for it.

## Installation

### Via OpenClaw Skill Package

```bash
# From the skill package file
openclaw skill install second-brain.skill
```

### Manual Installation

```bash
# Clone this repository
git clone https://github.com/aomnimedia/second-brain.git

# Copy to your OpenClaw workspace
cp -r second-brain/skills/second-brain ~/.openclaw/workspace/skills/
```

## The Cognitive Structure

The six second-brain directories and their recall patterns:

| Directory | Purpose | Recall Pattern |
|-----------|---------|----------------|
| `/projects` | Task-specific knowledge | "What did we learn on the X project?" |
| `/decisions` | Cross-cutting decisions | "Why did we choose X over Y?" |
| `/patterns` | Reusable patterns | "How do I do X the standard way?" |
| `/learnings` | Lessons learned | "What mistake did we make?" |
| `/strategy` | Long-term strategic knowledge | "What are we trying to achieve?" |
| `/workspace` | Active working directory | "What am I working on now?" |

## Usage

### When to Use This Skill

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

### Organization Workflow

1. **THINK** - What is this information?
2. **DESCRIBE** - How will I recall this later?
3. **CATEGORIZE** - Choose the directory
4. **WRITE** - Create the document

## Quick Start Example

```
second-brain/
├── projects/
│   ├── bug-queue-system/
│   ├── vk-tracker/
│   └── antfarm-docs/
├── decisions/
│   ├── git-author-identity.md
│   └── documentation-push-protocol.md
├── patterns/
│   ├── verification/
│   ├── coder-tester/
│   └── franklin/
├── learnings/
│   ├── autonomy_failures.md
│   └── hindsight/
├── strategy/
│   ├── MEMORY.md
│   ├── goals/
│   └── SOUL.md
└── workspace/
    ├── drafts/
    └── current-work/
```

## Key Principles

✅ **Organize by recall pattern, not deployment structure**
- Don't organize like a codebase (`src/`, `data/`, `tests/`)
- Organize by how your brain naturally looks for information

✅ **Single source of truth**
- Avoid duplicate storage
- Use references/links if needed

✅ **Progressive refinement**
- Start with 6 core directories
- Let usage refine structure over time

✅ **Search saves hierarchy**
- Good search beats perfect categorization
- Don't overthink - file somewhere, then refine

## Anti-Patterns to Avoid

❌ **Over-categorization** - Too many directories, too specific
❌ **Deployment structure** - Organizing by `src/`, `data/`, `tests/`
❌ **Premature organization** - Spending more time organizing than creating value
❌ **Duplicate storage** - Same content in multiple places
❌ **Hallucination-period conflicts** - Moving files during uncertainty

## Documentation

- **[SKILL.md](SKILL.md)** - Complete skill documentation with detailed patterns
- **[references/examples.md](references/examples.md)** - Real-world project organization examples

## Contributing

This is a reference skill for OpenClaw. Suggestions and improvements welcome via issues and pull requests.

## License

This skill is part of the OpenClaw ecosystem.

## About

Created for the AOmni OpenClaw system to help AI agents and humans organize knowledge in ways that optimize both human cognitive patterns and AI recall mechanisms.

**Key insight:** The goal is rapid recall, not perfect taxonomy. Organize for your brain and AI models, not for aesthetic file systems.