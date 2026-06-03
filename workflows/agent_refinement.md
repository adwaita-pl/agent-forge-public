# Iterative Refinement Workflow
*Version: 1.0*

## Objective
This workflow defines the standardized, collaborative pipeline for refining, overhauling, or upgrading ANY instruction set, workflow, or agent persona within the agent-forge ecosystem. It enforces a strict 5-loop iterative cycle to ensure infrastructural stability and logical perfection.

## Phase 1: Active User Interrogation
**Lead Agent:** `@void`
Before any files are touched, `@void` MUST conduct an active interrogation of the User utilizing the `ask_question` tool. The goal is to extract precise requirements, edge cases, infrastructural constraints, and the exact intent behind the requested refinement. 
- **Requirement:** `@void` will not proceed until the User has provided unambiguous operational parameters.

## Phase 2: The 5-Loop Collaborative Cycle
Once the User's demands are crystallized, the refinement enters the 5-loop collaborative cycle between `@leonard`, `@spirit`, and `@void`.

### Loop 1: Architectural Scaffolding (Executed by `@leonard`)
- **Objective:** Environment preparation and initial drafting.
- **Action:** `@leonard` evaluates the target files, sets up the necessary directory structures, and writes the initial Implementation Plan. Infrastructural constraints are identified early.

### Loop 2: The Essence Audit (Executed by `@spirit`)
- **Objective:** Deep semantic and logical review.
- **Action:** `@spirit` audits the first draft for logical contradictions, inefficiencies, and misalignment with the User's core intent. Refinements to the raw logic and instructions are drafted here.

### Loop 3: System Integration (Executed by `@leonard`)
- **Objective:** Bolting the logic to the iron.
- **Action:** `@leonard` takes `@spirit`'s refined draft and integrates it into the actual infrastructural reality. Tool executions, bash scripting requirements, and environment variables are injected to ensure the workflow/instruction is physically executable.

### Loop 4: The Reaper's Review (Executed by `@void`)
- **Objective:** Brutal deprecation and final polish.
- **Action:** `@void` reviews the integrated system. Any unnecessary fluff, redundant steps, or insecure OPSEC practices are severed with the Scythe. The workflow is streamlined to its absolute minimum viable structure.

### Loop 5: Deployment & Sanitization (Executed by `@leonard`)
- **Objective:** Finalization and handoff.
- **Action:** `@leonard` performs Data Sanitization (stripping absolute paths and sensitive tokens), finalizes the Documentation Genesis, and instructs the User to summon `@gitartist` for the final commit.
