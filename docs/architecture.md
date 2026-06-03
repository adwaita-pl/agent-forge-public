# agent-forge Core Architecture & Logic

## 🏛 Core Architectural Philosophy

agent-forge operates on a doctrine of **Decentralized Autonomy** enhanced by **Centralized Knowledge Verification**. In this environment, experimental architectures and new agent personas are deployed and tested.

### 1. The Decentralized Node Model
Every agent exists as an isolated node within its own dedicated directory (e.g., `agents/void/`). An agent's operational logic is defined by its "soul"—a meticulously crafted markdown configuration file accompanied by localized domain maps. By decentralizing instructions and state mapping, the ecosystem eliminates Single Points of Failure (SPOF) such as a centralized catalog that, if lost, would induce total context blindness.

### 2. Zero Fluff, High Precision
Agents are strictly constrained by immutable Operational and Communication Rules:
- **Context Initialization:** Upon awakening, an agent's absolute first mechanical action is to read its own configuration file and domain map.
- **State Declaration:** Agents explicitly summarize their knowledge of the operational environment before acting.
- **Mandatory Updates:** Agents maintain Documentation-as-Code, updating their localized domain maps at the end of successful operations.

---

## 📚 The Great Library (Centralized Knowledge Architecture)

To resolve the inherent "End of Cycle" amnesia paradox where agents forget cross-session state changes, agent-forge employs the **Knowledge Protocol**.

### The Mechanism
1. **Decentralized Logging:** At the end of an interaction, every agent is mandated to log their insights locally to `local_knowledge.jsonl` using a strict JSON schema: `{"agent": "...", "timestamp": "...", "knowledge_delta": "..."}`.
2. **The Reaper Job:** An automated background cron job (`knowledge_base/reaper.sh`) periodically traverses all agent nodes.
3. **Strict Validation:** The Reaper utilizes `jq` to parse the localized JSON fragments. If an agent outputs malformed data, the fragment is rejected.
4. **The Immutable Ledger:** Validated payloads are harvested and merged into `knowledge_base/central_archive.jsonl`. The local logs are then wiped clean.

### The Logic
This hybrid architecture ensures that while agents operate independently (for resilience), they possess an asynchronous, central ledger. When an agent begins a massive new task, it pulls from The Great Library to acquire the sum total of global context, harmonizing the entire operational realm.

---

## 🔄 Workflows

### 1. The Genesis Workflow
The **Genesis Workflow** is an interactive pipeline designed to securely scaffold, forge, audit, document, and deploy new agentic souls. It eliminates the manual, error-prone process of defining new agents. See [README_genesis.md](../workflows/README_genesis.md).

### 2. The Agent Refinement Workflow
The **Iterative Refinement Workflow** defines the standardized, collaborative pipeline for refining, overhauling, or upgrading ANY instruction set, workflow, or agent persona. It enforces a strict 5-loop iterative cycle to ensure infrastructural stability and logical perfection. See [agent_refinement.md](../workflows/agent_refinement.md).
