---
name: skill-synabun-knowledge-v1
description: >
  Motor de chunking de sessão baseado no Synabun para extração estruturada de contexto.
---

## Skill Synabun Knowledge | 🧠

Este documento detalha os componentes principais de inteligência extraídos do repositório Synabun para reutilização no ecossistema Nexus.AI.

---

## 1. Document Processing Engine (Markdown Splitting)

Synabun uses a specialized "Session Chunking" motor to process interaction logs (JSONL) into logical, searchable units. Unlike generic text splitters, this engine is context-aware and boundary-driven.

### Core Logic: `neural-interface/lib/session-chunker.js`
- **Task Boundary Detection**: Splits conversation logs into "chunks" based on time gaps (`TASK_BOUNDARY_GAP_MS = 120,000` or 2 minutes) between human messages.
- **Synthesis Engine**: Instead of storing raw logs, it synthesizes a structured markdown "content" block for embedding:
    - **Header**: Project, branch, and date.
    - **USER/ASSISTANT Snippets**: Cleaned text (stripping system tags/reminders).
    - **Tool Usage Tracking**: Aggregates tools used in the chunk (e.g., `Write(2)`, `Read(1)`).
    - **File Impact**: Tracks `FILES MODIFIED` and `FILES READ` via tool input analysis.
- **Constraints**:
    - `MAX_CONTENT_CHARS = 8000`
    - `MAX_USER_MESSAGES = 5`
    - `MAX_ASSISTANT_CHARS = 500`

---

## 2. Metadata Logic for Semantic Search

Synabun's search capability (Recall) relies on a rich metadata schema and multi-layered scoring.

### Metadata Schema: `mcp-server/src/services/sqlite.ts`
Stored in SQLite with the following searchable/filterable fields:
- **`category` / `subcategory`**: Hierarchical organization.
- **`project`**: Auto-detected from working directory to scope searches.
- **`tags`**: JSON array of user-defined or auto-generated keywords.
- **`importance`**: 1-10 scale used for boosting.
- **`file_checksums`**: Stores hashes of `related_files` to detect staleness (sync tool).
- **`related_memory_ids`**: Manual links between memories.

### Search Scoring: `mcp-server/src/tools/recall.ts`
- **Time Decay**: Semantic similarity is adjusted by age using a half-life formula (e.g., 90-day half-life for standard memories, 14-day for recency-boosted ones).
- **Importance Boost**: Memories with importance 8+ bypass time decay.
- **Project Boost**: Results matching the current project get a 1.2x multiplier.
- **Hybrid Search**: Fallback to **FTS5 (Full-Text Search)** when vector similarity is low (catches exact identifiers, error codes, and proper nouns).

---

## 3. Knowledge Structuring System Prompts

Synabun uses "Mode" prompts to ensure the AI structures knowledge consistently and avoids hallucination.

### Key Prompt: `skills/synabun/modules/memorize.md`
- **Structuring Rule**: Forces the AI into a "memorize mode" with a multi-phase process.
- **Markdown Template**: Precise schema for "Context Memories":
    - `## Context: [Title]`
    - `### Summary` (2-4 specific sentences)
    - `### Key Details` (Decision reasoning, technical specifics)
    - `### Files Referenced`
    - `### Open Items`
- **Verification Loop**: Phase 4 requires presenting the draft to the user for validation BEFORE calling the `remember` tool.
- **Hallucination Guard**: Explicit instruction: "The user's conversation IS the source — don't invent details. Only memorize what was actually discussed."

### Key Prompt: `skills/synabun/modules/audit.md`
- **Validation Protocol**: Defines status levels (**VALID**, **STALE**, **INVALID**, **UNVERIFIABLE**) and actions.
- **Verification Loop**: Uses delegation tools to verify memories against the current state of the codebase.

---

## 4. Technical Architecture Notes

- **Backend**: Node.js with built-in `node:sqlite` for vector and relational storage.
- **Embeddings**: Local generation using Transformers.js (via `local-embeddings.ts`).
- **Bridge**: The `neural-interface` serves as an Express bridge for browser control and UI-driven memory management.
