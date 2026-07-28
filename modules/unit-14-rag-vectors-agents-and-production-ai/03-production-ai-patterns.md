# Unit 14 — RAG, Vectors, Agents and Production AI
## Topic 3: Production AI Patterns

*(Covers: Production AI patterns — cost, latency, and reliability trade-offs · Writing an architectural decision)*

---

## 1. Learning Objectives

By the end of this topic, you will be able to:

1. **Describe** the cost, latency, and reliability trade-offs between a direct call, chained calls, RAG, and an agent.
2. **Explain** why more powerful patterns are not automatically "better" — each adds cost, delay, and new failure points.
3. **Analyze** a given business requirement and identify which production pattern fits it best.
4. **Create** a short architectural decision record (ADR) that justifies a chosen pattern with evidence-based reasoning.
5. **Evaluate** a proposed AI system design and identify a mismatched or over-engineered pattern choice.

---

## 2. Overview

You now know four ways to build with an LLM: a direct call, chained calls, RAG, and an agent (Topic 2). The final skill of this unit is choosing correctly between them **for a real system**, and being able to justify that choice in writing — exactly the kind of decision a working AI-native engineer must defend to a manager, a client, or a code reviewer.

Every pattern trades off three things: **cost** (how much you pay per request, since more API calls and more tokens cost more), **latency** (how long the user waits for a reply), and **reliability** (how likely the system is to fail, and how bad a failure looks when it happens). This topic gives you a structured way to reason about that trade-off, and a professional format — the **architectural decision record** — for writing your reasoning down. This is also the exact skill you will use in Unit 15's capstone, where you must justify your own system's architecture in writing.

---

## 3. Description

### 3.1 Cost, Latency, and Reliability Trade-Offs

**Key Terminology:**

| Term | Simple Meaning |
|---|---|
| **Cost** | What you pay per request — driven mainly by how many tokens are sent and received, and how many API calls are made per user request. |
| **Latency** | How long the user waits between asking and getting an answer. |
| **Reliability** | How consistently the system produces a correct, complete answer without failing partway through. |
| **Failure surface** | The number of distinct places a request could go wrong — each extra API call or tool call is one more place something could fail. |

**Comparison Table — Qualitative Trade-offs (relative to each other, not fixed numbers):**

| Pattern | Relative Cost | Relative Latency | Relative Reliability Risk | Why |
|---|---|---|---|---|
| Direct call | Lowest | Fastest | Lowest risk | One request, one response, nothing else can go wrong in between |
| Chained calls | Low–Medium | Medium (sum of each step's latency) | Low–Medium | Multiple calls, but the sequence is fixed and predictable, so failures are easier to anticipate and test |
| RAG | Medium | Medium (retrieval step adds time before generation) | Medium | Adds a retrieval step that can itself go wrong (e.g., poor retrieval quality), on top of generation |
| Agent | Highest | Slowest (multiple reasoning + tool-call rounds) | Highest risk | Each self-chosen step is an extra chance for the model to make a wrong decision, and delays compound across rounds |

> **Important Note:** These are *relative*, qualitative comparisons to guide your thinking, not fixed prices or millisecond figures — actual numbers change over time and depend on model, prompt length, and provider, so always check current documentation/pricing rather than memorising a number that will go stale.

**Best Practices:**
- Always default to the simplest pattern (top of the table) that can satisfy the requirement — this is the same discipline as the decision matrix in Topic 2.
- Add complexity (RAG, then agents) only when you have a specific, named reason the simpler pattern cannot meet (e.g., "the answer depends on data the model wasn't trained on" → RAG is justified).
- Measure actual latency and cost during evaluation (Unit 15) rather than assuming — real behaviour often surprises you.

**Common Mistakes:**
- Choosing an agent "because it sounds more advanced," when a single well-specified prompt would have worked.
- Ignoring latency until users complain — always estimate it during design, not after deployment.
- Forgetting that every added step is also an added *place things can go wrong* — reliability, not just cost and speed, must be weighed.

---

### 3.2 Writing an Architectural Decision

**Definition:** An **Architectural Decision Record (ADR)** is a short, structured written document that captures: what decision was made, what alternatives were considered, and why the chosen option was picked over the others.

**Why this exists:** Six months after you build a system, nobody — including you — will remember *why* you chose RAG over a simple direct call. An ADR is a permanent, professional record of that reasoning, so future engineers (including future-you) can understand and revisit the decision if requirements change.

**A Simple ADR Template:**

```
Title: [Short name for the decision]
Context: [What problem are we solving? What are the constraints?]
Options Considered: [List each pattern considered]
Decision: [Which pattern was chosen]
Reasoning: [Why this pattern, and not the others, given cost/latency/reliability]
Consequences: [What this choice means going forward — trade-offs accepted]
```

---

## 4. Real World Application

- **Banking/FinTech:** A UPI query assistant chooses RAG (not an agent) because the answers depend on retrievable policy documents, but no multi-step autonomous decision-making is required.
- **Railway booking systems:** A full trip-planning assistant ("check trains, check seat availability, check fares, then summarise") justifiably chooses an agent, because the exact sequence of lookups depends on what earlier lookups reveal.
- **E-commerce:** A simple "write a product description" feature uses a direct call — no retrieval, no tools, no agent needed.
- **Healthcare:** A clinical-notes summarisation tool uses chained calls (extract → summarise → format) rather than an agent, because the steps are fixed and known in advance, and predictability matters more than flexibility in this high-stakes domain.
- **Education:** A capstone-project assistant (Unit 15) might use RAG to answer questions about a student's own submitted spec document.

---

## 5. Worked Example

**Scenario:** Your team must build "RailMitra," an assistant that answers passenger questions about train status, refunds, and platform information, sourced from IRCTC's own current data feeds.

**Completed ADR:**

```
Title: Choosing an architecture pattern for RailMitra

Context: RailMitra must answer questions about live train status (changes constantly),
refund policy (fixed, but long and detailed), and platform info (changes constantly).
Answers must be grounded in current, real data — not the model's training-time knowledge.

Options Considered:
1. Direct call — rejected: the model was not trained on today's live train data,
   so it would hallucinate.
2. Chained calls — rejected: the exact sequence of lookups needed depends on what
   the user asks and what earlier lookups reveal (e.g., only check refund policy
   if the train is actually delayed/cancelled) — a fixed chain can't adapt to this.
3. RAG only — partially rejected: RAG alone retrieves evidence but cannot decide
   to look up "seat availability" only after first discovering the train is delayed.
4. Agent (using RAG as one of its tools) — SELECTED.

Decision: Build RailMitra as an agent with three tools: get_train_status,
get_refund_policy (implemented via RAG over the policy documents), and
get_platform_info. The agent reasons about which tools to call based on the
user's actual question.

Reasoning: The task requires the system to decide its own sequence of lookups
based on discovered information (Unit 14 Topic 2's decision matrix — this is
exactly what distinguishes an agent from RAG or chained calls). The added cost
and latency of the agent pattern is accepted because passengers need accurate,
current, multi-part answers, and getting this wrong (e.g., wrong refund info)
has real consequences — reliability of the FINAL answer matters more here than
raw speed.

Consequences: We accept higher latency (multiple reasoning rounds) and higher
cost per query than a simple direct call. We will add human review sampling on
a percentage of refund-related answers (Unit 9's Judgment Framework: refund
amounts are financially consequential enough to warrant spot-check oversight),
and we will evaluate the agent using the 5-case harness from Unit 15 before
launch.
```

---

## 6. Key Takeaways

- Every pattern trades off **cost, latency, and reliability** — more powerful patterns are not automatically better; they are *more expensive and riskier when unnecessary*.
- Always justify moving down the pattern ladder (direct call → chained → RAG → agent) with a specific, named reason the simpler pattern cannot meet.
- An **ADR** (Architectural Decision Record) is the professional format for writing down and defending a pattern choice: Context, Options Considered, Decision, Reasoning, Consequences.
- Reliability risk compounds with each added step — an agent's flexibility is also its biggest risk surface.
- **Interview tip:** If asked "how would you decide whether to use RAG or an agent," answer with the specific test: *"Does the exact sequence of steps need to be decided dynamically based on what's discovered along the way? If yes, agent. If the retrieval alone answers it, RAG is enough."*
- This ADR skill is directly reused in your Unit 15 capstone, where you must document and justify your own system's architecture.

---

## 7. Reference Links

- [Anthropic Documentation — Building with Claude](https://docs.claude.com/) — official guidance on choosing patterns for production systems.
- [Google Machine Learning Crash Course — Production ML Systems](https://developers.google.com/machine-learning/crash-course) — supplementary grounding in production trade-off thinking.
