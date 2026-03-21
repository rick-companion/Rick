# RICK — System Architecture

This document describes the technical architecture of RICK. It is a living document and will evolve as the project grows.

-----

## Overview

RICK is a local-first, privacy-preserving AI companion system. Every component is designed to run entirely on a home server or NAS. No user data ever leaves the household unless the family explicitly opts into the community hosted version.

```
[ Device App — iPad / Browser ]
            ↕
[ FastAPI Backend — Python ]
            ↕
    ┌───────────────────┐
    │   Ollama          │  ← Local LLM inference
    │   PostgreSQL      │  ← Persistent storage
    │   pgvector        │  ← Semantic memory search
    │   Readiness Engine│  ← Phase progression logic
    └───────────────────┘
            ↕
[ Parent Dashboard ]
```

-----

## Components

### 1. Device App

The user-facing interface running on an iPad or browser. In early phases this is primarily an email and messaging interface. In Phase 3 it becomes a game sidebar companion.

**Tech:** React Native (iPad) or React (browser)
**Communicates with:** FastAPI backend via REST

-----

### 2. FastAPI Backend

The core of the system. Handles all business logic, memory injection, session management, and orchestration between components.

**Responsibilities:**

- Receive user input from the device app
- Build context-enriched prompts for the LLM
- Store and retrieve memories via pgvector
- Log all sessions and interactions
- Expose endpoints for the parent dashboard
- Manage phase state and readiness signal tracking

**Tech:** Python, FastAPI, SQLAlchemy, asyncpg

-----

### 3. Ollama — Local LLM Inference

Runs large language models entirely on local hardware. No cloud API required.

**Recommended models:**

|VRAM Available|Recommended Model             |Quality  |
|--------------|------------------------------|---------|
|12GB          |llama3.2:8b or mistral:7b     |Good     |
|24GB          |llama3.1:32b or mistral:32b   |Great    |
|24GB          |llama3.3:70b (4-bit quantized)|Excellent|

**GPU recommendation:** RTX 3090 (24GB VRAM) is the community sweet spot. Runs 70B quantized models at conversational speed.

-----

### 4. PostgreSQL + pgvector

The primary data store. pgvector extends PostgreSQL with vector similarity search, enabling semantic memory retrieval.

#### Schema

```sql
-- Core user profile
CREATE TABLE user_profile (
  key         TEXT PRIMARY KEY,
  value       JSONB,
  updated_at  TIMESTAMP
);

-- Episodic memory with semantic search
CREATE TABLE memories (
  id                UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  content           TEXT,
  embedding         vector(1536),
  tags              TEXT[],
  emotional_valence TEXT,        -- positive / neutral / negative
  created_at        TIMESTAMP DEFAULT now()
);

-- Full session transcripts
CREATE TABLE sessions (
  id          UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  phase       TEXT,             -- email / sms / game
  scenario    TEXT,             -- greeting / joining / goodbye etc.
  transcript  JSONB,
  outcomes    JSONB,            -- readiness signals observed
  created_at  TIMESTAMP DEFAULT now()
);

-- User interests and personal data
CREATE TABLE interests (
  category    TEXT,             -- alphabet / roblox_games / foods etc.
  key         TEXT,
  value       TEXT,
  notes       TEXT,
  PRIMARY KEY (category, key)
);

-- Phase state and readiness tracking
CREATE TABLE phase_state (
  id                    UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  current_phase         TEXT,
  readiness_signals     JSONB,
  transition_approved   BOOLEAN DEFAULT false,
  updated_at            TIMESTAMP DEFAULT now()
);
```

-----

### 5. Memory Injection Pipeline

Before every LLM call, RICK builds a context-enriched prompt. This is what makes interactions feel personal rather than generic.

```python
async def build_prompt(user_input: str) -> str:
    # Layer 1 — Always present
    core_profile    = await get_core_profile()
    autism_guidelines = load_interaction_guidelines()
    current_phase   = await get_current_phase()

    # Layer 2 — Semantically relevant memories
    relevant_memories = await vector_search(user_input, top_k=5)

    # Layer 3 — Recent session context
    recent_context  = await get_recent_exchanges(limit=10)

    # Layer 4 — User input
    return assemble_prompt(
        core_profile,
        autism_guidelines,
        current_phase,
        relevant_memories,
        recent_context,
        user_input
    )
```

-----

### 6. Readiness Engine

Determines when a user is ready to progress to the next phase. Transition suggestions are surfaced to the parent dashboard for approval — never automatic.

```python
readiness_signals = {
    "email_to_sms": [
        "response_time_trending_down",     # replying faster over time
        "message_length_trending_up",      # more to say
        "unprompted_initiation",           # they message first
        "reciprocal_questions",            # asking things back
        "consistent_engagement_30_days"    # sustained over time
    ],
    "sms_to_game": [
        "comfortable_with_open_ended",
        "handles_topic_changes_gracefully",
        "expresses_wants_and_preferences",
        "tolerates_response_delays"
    ],
    "game_to_peer": [
        "initiates_social_scenarios",
        "recovers_from_awkward_exchanges",
        "expresses_desire_for_real_connection"
    ]
}
```

All signals are logged. The engine never forces a transition — it surfaces a recommendation and waits for parent approval.

-----

### 7. Parent Dashboard

A simple web interface for parents or guardians to:

- View session transcripts and summaries
- See readiness signal progress over time
- Approve or defer phase transitions
- Update user profile and interests
- Review and export session logs

**Tech:** React, served by FastAPI

-----

### 8. Autism-Informed Interaction Guidelines

A curated prompt library built on evidence-based practices for communicating with autistic individuals. Stored in `/core/prompts/` and injected into every LLM call.

Core principles the AI follows:

- Use concrete, literal language — no idioms or sarcasm
- Be predictable and consistent in structure
- Follow the user’s lead on topics
- Never rush or pressure
- Acknowledge and validate special interests enthusiastically
- Use the user’s preferred communication style
- Signal topic changes clearly before making them

This library is one of the highest-impact areas for clinical contributors to shape.

-----

## Deployment

### Docker Compose (Recommended)

All services run as Docker containers orchestrated with Docker Compose.

```yaml
services:
  api:
    build: ./backend
    ports:
      - "8000:8000"
    depends_on:
      - db
      - ollama

  db:
    image: pgvector/pgvector:pg16
    volumes:
      - pgdata:/var/lib/postgresql/data
    environment:
      POSTGRES_DB: rick
      POSTGRES_USER: rick
      POSTGRES_PASSWORD: ${DB_PASSWORD}

  ollama:
    image: ollama/ollama
    volumes:
      - ollama_models:/root/.ollama
    deploy:
      resources:
        reservations:
          devices:
            - capabilities: [gpu]

  dashboard:
    build: ./dashboard
    ports:
      - "3000:3000"

volumes:
  pgdata:
  ollama_models:
```

### Unraid

A community app template for Unraid is planned for the first stable release. GPU passthrough is supported via the Unraid Nvidia plugin.

-----

## Data Privacy

- All data is stored locally on the host machine
- No telemetry, analytics, or external API calls by default
- The hosted community version (for families who can’t self-host) uses end-to-end encryption and strict data isolation per family
- Session logs are never shared without explicit informed consent
- Research participation is always opt-in

-----

## Security Considerations

- All API endpoints require authentication
- Parent dashboard is separated from the user-facing app by role
- Database credentials are managed via environment variables
- No external network access required for core functionality

-----

## Future Considerations

- **Federated peer matching** — connecting users across self-hosted instances without centralizing data
- **Fine-tuning pipeline** — allowing the local model to be fine-tuned on interaction history over time
- **Voice interface** — Whisper STT + TTS for users who prefer speaking over typing
- **Roblox integration** — custom Lua game with HttpService calling the RICK backend

-----

*This document is maintained by the RICK core team and updated with each major release. PRs welcome.*
