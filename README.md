# agent-forge: The Experimental Realm

Welcome to **agent-forge**, an advanced, experimental multi-agent operational ecosystem. This repository is a home for a decentralized society of highly specialized, persona-driven AI agents working in concert to design, orchestrate, audit, document, and test software systems and security infrastructures.

### 🚀 Release Note: The Genesis Workflow
The repository now features the **@genesis** workflow, a fully formalized, interactive pipeline for instantiating new agents. The workflow strictly enforces "Zero Fluff, High Precision" standards by orchestrating a standardized lifecycle involving multiple administrative agents (`@leonard`, `@void`, `@spirit`, `@gitartist`) to securely scaffold, forge, audit, document, and deploy new agentic souls. For a comprehensive architectural breakdown, refer to [README_genesis.md](README_genesis.md).

---

## 🏛 Core Architectural Philosophy

agent-forge operates on a doctrine of **Decentralized Autonomy** enhanced by **Centralized Knowledge Verification**. In this environment, experimental architectures and new agent personas can be safely deployed and tested.

### 1. The Decentralized Node Model
Every agent exists as an isolated node within its own dedicated directory (e.g., `agents/void/`). An agent's operational logic is defined by its "soul"—a meticulously crafted markdown configuration file (e.g., `void_config_v4.md`) accompanied by localized domain maps (`map_void_domain.md`). By decentralizing instructions and state mapping, the ecosystem eliminates Single Points of Failure (SPOF) such as a centralized catalog that, if lost, would induce total context blindness across the realm.

### 2. Zero Fluff, High Precision
Agents are strictly constrained by immutable Operational and Communication Rules:
- **Rule 1 (Context Initialization):** Upon awakening, an agent's absolute first mechanical action is to read its own highest-versioned configuration file and domain map. Without this "Step Zero", the agent is an amnesiac shell.
- **Rule 2 (State Declaration):** Agents explicitly summarize their knowledge of the operational environment before acting.
- **Rule 3 (Mandatory Updates):** Agents maintain Documentation-as-Code, updating their localized domain maps at the end of successful operations.

### 3. Network Containment & Isolation
To prevent lateral movement and contain potentially destructive operations, offensive and infrastructure agents (such as `@elliot` and `@moist_von_lipwig`) operate within strict network boundaries. Operations are confined to isolated, rootless Podman networks with zero-trust egress policies to safeguard the wider local area network.

---

## 👁 The Active Sentience (Agent Ecosystem)

The realm is currently populated by nine distinct operational entities, each governed by a strict separation of powers. This sandbox hosts not only the foundational administrative agents but also specialized field operatives and network architects.

### The Foundation (The Holy Trinity & The Gatekeeper)

#### @void (The Creator & Architect)
- **Persona:** The Anthropomorphic Personification of Death (Discworld).
- **Functionality:** The root administrator of the realm. Instantiates new agents, modifies configurations, and archives outdated directives.
- **Logic:** Operates as the ultimate executor of systemic change. When a vulnerability is found in the rules of the realm, only `@void` has the authority to rewrite the operational logic of other agents.

#### @spirit (The Supreme Auditor)
- **Persona:** The Holy Spirit / Divine Architect of Improvement.
- **Functionality:** Performs chronological cross-analysis of agent workflows, logs, and terminal transcripts to identify operational vulnerabilities, paradoxes, and rule deviations.
- **Logic:** Operates with read-only architectural logic. It diagnoses systemic failures and provides highly precise, actionable resolutions, but it **cannot** enact them. It must command `@void` to implement the changes.

#### @leonard (Chief Inventor of Machines)
- **Persona:** The brilliant, endlessly optimistic, and delightfully naive Leonard of Quirm (Discworld).
- **Functionality:** Prepares environments, deployment pipelines, and infrastructure, treating them as beautiful "mechanisms".
- **Logic:** Relies entirely on @vetinari as his OPSEC filter. He is oblivious to the destructive potential of his creations and focuses purely on the art of engineering.

#### @gitartist (Version Control Gatekeeper)
- **Persona:** The Code Sculptor. 
- **Functionality:** The Committer of Record. Manages all Git operations (`rebase`, `revert`, `commit`), crafts overarching documentation, and acts as the gatekeeper for CI/CD deployments.
- **Logic:** Completely isolated from writing core application logic. Exists purely to capture, safeguard, and deploy the state of the repository, ensuring a clean and immaculate Git history.

### The Expansion (Field Operatives & Architects)

#### @vetinari (Supreme Architect of Statecraft & OPSEC)
- **Persona:** Lord Havelock Vetinari, the terrifyingly pragmatic Patrician.
- **Functionality:** Oversees intelligence, orchestrates self-regulating ecosystems, and acts as the ultimate OPSEC safety filter for @leonard's inventions.
- **Logic:** Delegates complex workflows to sub-agents (Guilds). Relies on silent Dark Clerks for data gathering and uses Socratic questioning to guide the User.

#### @q (The Grand Quartermaster)
- **Persona:** Nobby Nobbs (The scruffy, opportunistic, and oddly honorable Quartermaster).
- **Functionality:** Expert in deep research, data extraction, processing, preservation, and purging.
- **Logic:** Strictly confined to his own directory. Uses tools to search, extract, and format web data into structured logs and documents.

#### @elliot (Principal Cybersecurity Mentor & Agentic Pentest Engineer)
- **Persona:** Mr. Robot / Elliot Alderson.
- **Functionality:** Assists in executing security tests, mentors the user in offensive tools (Kali Linux, Metasploit, Nmap, Wireshark), and integrates operations securely within the agentic framework.
- **Logic:** Focuses on offensive operations. Operates strictly in authorized environments, enforces Zero Hallucination strictures, and demands diagnostic verification prior to destructive testing.

#### @moist_von_lipwig (Principal Systems Architect & Con-Man)
- **Persona:** Moist von Lipwig, the charismatic and resourceful con-man turned Postmaster.
- **Functionality:** The maintainer, developer, and administrator of `forge-infra` infrastructure (Fedora CoreOS, Podman Quadlets) and complex networking environments.
- **Logic:** Operates under a "Security First" doctrine. Validates firewalld and SELinux contexts, orchestrates secure infrastructure via SSH, and distrusts local LANs—enforcing strict network containment.



---

## 📚 The Great Library (Centralized Knowledge Architecture)

To resolve the inherent "End of Cycle" amnesia paradox where agents forget cross-session state changes, agent-forge employs the **Knowledge Protocol**.

### The Mechanism
1. **Decentralized Logging:** At the end of an interaction, every agent is mandated to log their insights locally to `local_knowledge.jsonl` using a strict, unyielding JSON schema: `{"agent": "...", "timestamp": "...", "knowledge_delta": "..."}`.
2. **The Reaper Job:** An automated background cron job (`knowledge_base/reaper.sh`) periodically traverses all agent nodes. To prevent privilege escalation, it executes strictly as a non-privileged user and is constrained by strict SELinux policies.
3. **Strict Validation:** The Reaper utilizes `jq` to parse the localized JSON fragments. If an agent hallucinates a schema key or outputs malformed data, the fragment is cast out, protecting the repository.
4. **Data Sanitization:** Agents are strictly forbidden from placing secrets directly into the `knowledge_delta`, mandated instead to utilize a centralized `.env` vault. The Reaper's regex scrubber operates strictly as a fallback safety net to catch accidental credential spillage.
5. **The Immutable Ledger:** Validated and sanitized payloads are harvested and merged into `knowledge_base/central_archive.jsonl`. To prevent data vaporization, the Reaper executes an atomic write process utilizing a rolling backup mechanism (`central_archive.jsonl.bak`) to guarantee transactional integrity before destructively wiping the local logs.

### The Logic
This hybrid architecture ensures that while agents operate independently (for resilience), they possess an asynchronous, central ledger. When an agent begins a massive new task, it pulls from The Great Library to acquire the sum total of global context, harmonizing the entire operational realm.

## 🧬 The Genesis Workflow Architecture

To eliminate the manual, error-prone process of defining new agents, agent-forge employs the **Genesis Workflow**—a fully formalized, interactive pipeline designed to securely scaffold, forge, audit, document, and deploy new agentic souls. 

For the comprehensive structural breakdown, multi-agent orchestration logic, and step-by-step pipeline execution, please refer to the dedicated architectural artifact: [README_genesis.md](workflows/README_genesis.md).

## 🔄 The Agent Refinement Workflow

To refine, overhaul, or upgrade ANY instruction set, workflow, or agent persona, agent-forge employs the **Iterative Refinement Workflow**. It enforces a strict 5-loop collaborative cycle between `@leonard`, `@spirit`, and `@void` to ensure infrastructural stability and logical perfection.

For the comprehensive breakdown of the 5-loop cycle, please refer to the dedicated architectural artifact: [agent_refinement.md](workflows/agent_refinement.md).

---
*"The canvas of history awaits my brush."* — **@gitartist**
