# Contributing to Rick 🤖

First off, thank you for being here. Building a bridge for neurodivergent connection is a big task, and we’re glad to have you on the team. 

As we are currently in **Phase 0**, our primary focus is building the high-reasoning foundation of Rick.

---

## ⚡ Technical Standards & Privacy
Because Rick is designed for a vulnerable population, we have non-negotiable technical standards:

1. **Local-First Only:** No features should require a 3rd-party cloud API (OpenAI, Anthropic, etc.) for core functionality. Everything must be compatible with **Ollama** or local Python logic.
2. **Zero PII (Personally Identifiable Information):** Never write code that logs or transmits user data outside the local environment.
3. **No "Fixing" Mentality:** Code and prompts should be designed to support, mirror, and engage—not to "correct" neurodivergent behaviors.

---

## 🛠️ Development Environment
To contribute to the core LLM logic, we recommend the following setup:

### 1. Local LLM (Ollama)
You don't need the full "Dev Rig" to contribute, but you should have [Ollama](https://ollama.com/) installed locally to test your changes. 
* Target Model for Phase 0: `llama3.1:8b` (minimum) or `llama3.1:70b` (if your hardware supports it).

### 2. Claude Code (Optional but Recommended)
We use **Claude Code** for rapid repository indexing and refactoring. If you are a high-volume contributor, please mention this in your PRs so we can coordinate logic updates.

---

## 🤝 Contribution Process

### 1. Find an Issue
Check the **[Good First Issues](https://github.com/rick-companion/Rick/issues?q=is%3Aopen+is%3Aissue+label%3A%22good+first+issue%22)**. These are specifically scoped for Phase 0.

### 2. Branching Strategy
* **Main:** Stable code only.
* **Feature Branches:** Use `feat/feature-name` or `fix/bug-name`.

### 3. Pull Requests
When you submit a PR, please use our template. Ensure you:
* Explain the **clinical or developmental value** of the change.
* Confirm the change maintains **Local-First** privacy.
* Include a screenshot if the change affects the Parent Dashboard.

---

## 🎁 Beyond Code
If you aren't a developer, you can still contribute by:
* **Hardware Benchmarking:** Reporting how models run on your specific setup.
* **Clinical Review:** Helping us define "Readiness Signals" in the Wiki.
* **Sponsorship:** Helping us fund the [Development Rig](https://github.com/rick-companion/Rick#%E2%9A%A1-1-the-development-machine-priority). Note: As we are not a 501(c)(3), these are personal gifts to the project.

---

## 📜 Recognition
All contributors will be added to our `CONTRIBUTORS.md` file. Whether you fix a typo or build a whole module, your help matters.
