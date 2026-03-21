# Rick
RICK — Realistic Interactive Companion Kit. An open source AI companion for neurodivergent individuals.

# RICK — Realistic Interactive Companion Kit

> *“I built this for my son Rick. I’m sharing it in case it helps yours.”*

![Status](https://img.shields.io/badge/status-early%20concept-blue)
![License](https://img.shields.io/badge/license-GPL%20v3-purple)
![Contributors Welcome](https://img.shields.io/badge/contributors-welcome-orange)

-----

## The Story

My son Rick is 19. He has autism. He’s funny, passionate about Roblox, and has an encyclopedic knowledge of the alphabet. Like a lot of people on the spectrum, social connection doesn’t come naturally — not because he doesn’t want it, but because the path there isn’t obvious.

I’m a developer. So I built something.

RICK is an open source AI companion that helps neurodivergent individuals build social confidence the way real relationships actually form — gradually, organically, and entirely on their terms.

I named it after him.

-----

## How It Works

RICK meets users where they are and advances only when they’re ready. No pressure. No rushing. Just connection at a pace that feels safe.

```
Phase 1 — Pen Pal
  The AI writes emails. The user writes back.
  Low pressure. Async. Their favorite topics lead the way.
        ↓
Phase 2 — Texting
  Shorter messages. Faster back and forth.
  Learning the rhythm of real conversation.
        ↓
Phase 3 — Game Companion
  A "come play with me" sidebar experience.
  Social scenarios practiced inside games like Roblox.
        ↓
Phase 4 — Real Peer Matching
  Connect with another real person who took the same journey.
  Same interests. Same pace. Already knows how to do this.
```

The AI tracks readiness signals over time — response speed, message length, unprompted initiation, reciprocal questions — and suggests phase transitions only when the data supports it. Parents or guardians approve every transition.

-----

## Core Principles

- **Interest-led** — Every interaction is built around what the user actually cares about
- **No fixing** — RICK doesn’t treat autism as a problem to solve. It builds a bridge.
- **Transparent** — Users always know they’re talking to an AI
- **Private** — Your family’s data never leaves your home
- **Open** — Free to self-host forever. No subscriptions. No data selling. Ever.

-----

## Architecture

```
[ iPad / Device App ]
        ↕
[ FastAPI Backend — Python ]
        ↕
[ Ollama — Local LLM Inference ]
[ PostgreSQL + pgvector — Memory & Logs ]
[ Readiness Engine — Phase Progression Logic ]
[ Parent Dashboard — Progress & Approvals ]
```

**Key design decisions:**

- **Local-first** — Runs entirely on your own hardware via Docker/Unraid
- **pgvector** — Semantic memory so RICK actually remembers and learns about the user over time
- **Ollama** — No cloud API required. Runs models like Llama 3.1 or Mistral locally
- **Readiness Engine** — Deterministic logic (not vibes) decides when a user is ready to level up

Full architecture documentation lives in [`/docs/architecture.md`](./docs/architecture.md)

-----

## Self-Hosting

RICK is designed to run on a home server or NAS. Unraid users get a community app template out of the box.

**Minimum requirements:**

- Docker + Docker Compose
- 16GB RAM
- GPU with 12GB+ VRAM recommended (RTX 3060 or better) for local LLM inference
- PostgreSQL-compatible storage

```bash
git clone https://github.com/rick-companion/rick
cd rick
cp .env.example .env
docker compose up -d
```

Full setup guide: [`/docs/self-hosting.md`](./docs/self-hosting.md)

-----

## Roadmap

### Phase 0 — Foundation *(now)*

- [ ] Project scaffolding and repo structure
- [ ] PostgreSQL + pgvector schema
- [ ] FastAPI backend skeleton
- [ ] Ollama integration and base prompt architecture
- [ ] User profile and persistent memory layer

### Phase 1 — Pen Pal MVP

- [ ] Email interaction module
- [ ] Interest-based conversation system
- [ ] Basic readiness signal tracking
- [ ] Parent dashboard v1

### Phase 2 — Texting Module

- [ ] SMS-style interface
- [ ] Faster response loop
- [ ] Readiness engine v1

### Phase 3 — Game Companion

- [ ] Roblox custom experience (Lua + HttpService)
- [ ] Social scenario library (greetings, joining, goodbyes)
- [ ] Real-time AI NPC integration

### Phase 4 — Peer Matching

- [ ] Anonymized peer matching algorithm
- [ ] Shared interest compatibility scoring
- [ ] Moderated introduction system

-----

## Contributing

RICK needs more than code. We’re looking for:

|Role                 |What You’d Do                                         |
|---------------------|------------------------------------------------------|
|**Developers**       |Features, bugfixes, integrations, testing             |
|**Prompt Engineers** |Refining autism-informed interaction styles           |
|**SLPs & Clinicians**|Validating the progression model                      |
|**Designers**        |UX/UI — this has to be exceptional for our users      |
|**Families**         |Beta testing, lived experience feedback               |
|**Hardware Donors**  |GPU nodes and compute for families who can’t self-host|
|**Researchers**      |Outcome studies and clinical validation               |

Read [`CONTRIBUTING.md`](./CONTRIBUTING.md) to get started.

All contributors are recognized in [`CONTRIBUTORS.md`](./CONTRIBUTORS.md).

-----

## Hardware Donations

RICK runs locally — but not every family has a homelab. We’re building a community compute network so families who can’t self-host can still access RICK for free.

If you have hardware to donate or want to contribute a compute node, open an issue tagged `hardware-donation`.

-----

## License

GNU General Public License v3.0 — see [`LICENSE`](./LICENSE)

This means anyone can use, study, modify, and distribute RICK. Nobody can take it proprietary. Ever.

-----

## Contact & Community

- GitHub Issues — bugs, features, questions
- GitHub Discussions — community conversation
- Coming soon: Discord

-----

*RICK started with one dad and one kid. Let’s see how far it goes.*
