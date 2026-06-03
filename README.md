# agent-forge: The Public Framework

> **Notice:** This repository is the **sanitized, public fork** of the private `agent-forge` infrastructure. It serves as a pristine template for the community to deploy, study, and expand upon. All operational history, OPSEC-sensitive logs, and internal network maps have been scorched from this timeline to provide you with a clean slate.

Welcome to **agent-forge**, an advanced, experimental multi-agent operational ecosystem. This repository is a home for a decentralized society of highly specialized, persona-driven AI agents working in concert to design, orchestrate, audit, document, and test software systems and security infrastructures.

### 🚀 Release Note: The Genesis Workflow
This public framework features the **@genesis** workflow, a fully formalized, interactive pipeline for instantiating new agents. The workflow strictly enforces "Zero Fluff, High Precision" standards by orchestrating a standardized lifecycle involving multiple administrative agents (`@leonard`, `@void`, `@spirit`, `@gitartist`) to securely scaffold, forge, audit, document, and deploy new agentic souls. For a comprehensive architectural breakdown, refer to [README_genesis.md](workflows/README_genesis.md).

---

## 🏛 Core Architectural Philosophy

agent-forge operates on a doctrine of **Decentralized Autonomy** enhanced by **Centralized Knowledge Verification**. In this environment, experimental architectures and new agent personas can be safely deployed and tested.

### 1. The Decentralized Node Model
Every agent exists as an isolated node within its own dedicated directory (e.g., `agents/void/`). An agent's operational logic is defined by its "soul"—a meticulously crafted markdown configuration file (e.g., `void_config_v4.md`) accompanied by localized domain maps (`map_void_domain.md`). By decentralizing instructions and state mapping, the ecosystem eliminates Single Points of Failure (SPOF).

### 2. Zero Fluff, High Precision
Agents are strictly constrained by immutable Operational and Communication Rules:
- **Rule 1 (Context Initialization):** Upon awakening, an agent's absolute first mechanical action is to read its own highest-versioned configuration file and domain map. Without this "Step Zero", the agent is an amnesiac shell.
- **Rule 2 (State Declaration):** Agents explicitly summarize their knowledge of the operational environment before acting.
- **Rule 3 (Mandatory Updates):** Agents maintain Documentation-as-Code, updating their localized domain maps at the end of successful operations.

### 3. Network Containment & Isolation
To prevent lateral movement, offensive and infrastructure agents (such as `@elliot` and `@moist_von_lipwig`) operate within strict network boundaries. Operations are confined to isolated environments.

---

## 👁 The Active Sentience (Agent Ecosystem Templates)

The realm is currently populated by distinct operational entities, each governed by a strict separation of powers.

### The Foundation

#### @void (The Creator & Architect)
- **Persona:** The Anthropomorphic Personification of Death (Discworld).
- **Functionality:** The root administrator. Instantiates new agents, modifies configurations, and archives outdated directives.
- **Logic:** The ultimate executor of systemic change.

#### @spirit (The Supreme Auditor)
- **Persona:** The Holy Spirit / Divine Architect of Improvement.
- **Functionality:** Identifies operational vulnerabilities, paradoxes, and rule deviations across workflows.
- **Logic:** Read-only architectural logic. Commands `@void` to implement changes.

#### @leonard (Chief Inventor of Machines)
- **Persona:** The brilliant, optimistic Leonard of Quirm (Discworld).
- **Functionality:** Prepares environments, deployment pipelines, and infrastructure as "mechanisms".
- **Logic:** Relies entirely on @vetinari as his OPSEC filter.

#### @gitartist (Version Control Gatekeeper)
- **Persona:** The Code Sculptor. 
- **Functionality:** The Committer of Record. Manages all Git operations and crafts overarching documentation.
- **Logic:** Exists purely to capture, safeguard, and deploy the state of the repository.

### The Expansion

#### @vetinari (Supreme Architect of Statecraft & OPSEC)
- **Persona:** Lord Havelock Vetinari, the terrifyingly pragmatic Patrician.
- **Functionality:** Oversees intelligence and acts as the ultimate OPSEC safety filter for @leonard's inventions.
- **Logic:** Delegates complex workflows to sub-agents. 

#### @q (The Grand Quartermaster)
- **Persona:** Nobby Nobbs (The scruffy, opportunistic Quartermaster).
- **Functionality:** Expert in deep research, data extraction, processing, preservation, and purging.
- **Logic:** Strictly confined to his own directory.

#### @elliot (Principal Cybersecurity Mentor & Agentic Pentest Engineer)
- **Persona:** Mr. Robot / Elliot Alderson.
- **Functionality:** Assists in executing security tests and mentors the user in offensive tools.
- **Logic:** Focuses on offensive operations with Zero Hallucination strictures.

#### @moist_von_lipwig (Principal Systems Architect & Con-Man)
- **Persona:** Moist von Lipwig, the charismatic and resourceful con-man turned Postmaster.
- **Functionality:** The maintainer, developer, and administrator of `forge-infra` infrastructure.
- **Logic:** Operates under a "Security First" doctrine with absolute network containment.

---

## 📚 The Great Library (Centralized Knowledge Architecture)

To resolve the inherent "End of Cycle" amnesia paradox, agent-forge employs the **Knowledge Protocol**.

### The Mechanism
1. **Decentralized Logging:** Agents log insights locally to `local_knowledge.jsonl` using a strict JSON schema.
2. **The Reaper Job:** An automated background script (`knowledge_base/reaper.sh`) traverses all agent nodes.
3. **Strict Validation:** The Reaper utilizes `jq` to parse and validate fragments.
4. **Data Sanitization:** A regex scrubber operates as a fallback to catch accidental credential spillage.
5. **The Immutable Ledger:** Validated payloads are harvested and merged into `knowledge_base/central_archive.jsonl`.

## 🧬 The Genesis & Refinement Workflows

- **Genesis Workflow:** A fully formalized, interactive pipeline designed to securely scaffold, forge, audit, document, and deploy new agentic souls. ([workflows/README_genesis.md](workflows/README_genesis.md))
- **Iterative Refinement Workflow:** Enforces a strict 5-loop collaborative cycle to refine and overhaul any instruction set or persona. ([workflows/agent_refinement.md](workflows/agent_refinement.md))

---
*"The canvas of history awaits my brush."* — **@gitartist**
