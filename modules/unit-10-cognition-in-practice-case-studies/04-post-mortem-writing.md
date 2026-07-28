# Unit 10 — Cognition in Practice — Case Studies
## Topic 4: Post-Mortem Writing

*(Covers: Writing a post-mortem — what failed, why, who was accountable, what governance would have prevented it)*

---

## 1. Learning Objectives

By the end of this topic, you will be able to:

1. **Explain** what a post-mortem is and why the tech industry treats it as a blameless, learning-focused document rather than a punishment record.
2. **Describe** the four essential sections of a good AI-system post-mortem.
3. **Differentiate** between a root cause and a superficial/immediate cause of a failure.
4. **Create** a complete, well-structured post-mortem for a given AI system incident.
5. **Evaluate** whether a proposed governance fix would actually have prevented the incident described.

---

## 2. Overview

Every AI system you build or oversee will, eventually, fail in some way — that is not a hypothetical, it is a certainty in real engineering practice. What separates a professional engineering team from an amateur one is not whether failures happen, but **whether the team writes a clear, honest post-mortem afterward, and whether that post-mortem actually changes how the system is built and governed next time.**

A **post-mortem** (literally, "after death" — borrowed from medical terminology, where it originally meant an examination performed after death to determine its cause) is a structured written account of what went wrong, why it went wrong, who was accountable, and — most importantly for you as a future AI-Native Engineer — **what governance control would have prevented it**.

This topic pulls together everything from this unit: you will use the case studies (Topic 1), the automation-complacency effect (Topic 2), and the human-oversight design method (Topic 3) as raw material, and turn them into the exact document format used by real engineering teams (including well-known industry practice at companies like Google) to learn from failure. This is also a direct rehearsal for your Unit 15 Capstone, which requires you to red-team your own AI system and document what you find.

---

## 3. Description

### Definition

A **post-mortem** is a structured, blameless report written after a failure or incident, whose purpose is to identify the root cause, assign clear (not punitive) accountability, and define concrete governance changes to prevent recurrence.

### Why "Blameless"?

**Blameless** does not mean "no one is accountable." It means the *document's purpose* is to fix the system, not to punish the individual — because punishing individuals for honest mistakes teaches people to hide failures instead of reporting them quickly, which makes the overall system less safe over time. Accountability (Unit 9's Q3) is still clearly named; it is simply separated from blame.

### The Four Essential Sections

| Section | What it answers |
|---|---|
| **What Failed** | A precise, factual description of the incident — what happened, when, and what the observable impact was. |
| **Why It Failed (Root Cause)** | The underlying reason — not just the immediate trigger, but the deeper system, process, or design gap that allowed it to happen. |
| **Who Was Accountable** | The specific role or team responsible for the failed component or checkpoint — stated factually, without blame language. |
| **What Governance Control Would Have Prevented It** | The specific, concrete process, checkpoint, or policy change that would have stopped this exact failure from happening (or caught it faster). |

### Root Cause vs Immediate Cause

- **Immediate cause:** "The AI model scored a genuine emergency case as routine." (This is just *what* happened.)
- **Root cause:** "There was no mandatory human vital-signs check before acting on a 'routine' AI score, so the system had no way to catch this specific type of error." (This is *why the system allowed it* to happen — and it's the root cause that governance fixes must target.)

A common beginner mistake is writing a post-mortem that stops at the immediate cause ("the AI was wrong") without digging into the root cause ("our process had no independent check for this case"). Always ask **"why did our system allow this to happen?"**, not just **"what did the AI do wrong?"**

### Best Practices

- Write the post-mortem soon after the incident, while details are fresh, but only once the immediate issue has been contained.
- Use neutral, factual language — describe actions and gaps in the *system*, not character judgments about people ("the checkpoint was not enforced," not "the reviewer was careless").
- Always end with specific, assignable action items — a post-mortem without concrete next steps is just a complaint, not an engineering document.
- Share post-mortems widely within the team (and, where appropriate, publicly) — the value of a post-mortem compounds when more people learn from it.

### Common Mistakes

- Stopping at the immediate cause instead of digging to the root cause.
- Writing in blame language ("X person failed to..."), which discourages honest future reporting.
- Proposing a vague fix ("we will be more careful") instead of a concrete governance control ("we will add a mandatory sampled audit reviewed weekly by the named model-risk officer").

---

## 4. Real World Application

- **Software Engineering / SRE (Site Reliability Engineering):** Post-mortems are a core discipline at nearly every major tech company for both software outages and, increasingly, AI-system failures.
- **Healthcare:** Hospitals conduct "morbidity and mortality" reviews — a close medical cousin of the engineering post-mortem, examining what happened and what safeguard would prevent recurrence.
- **Banking / Fraud Systems:** After a missed fraud pattern or wrongful account block, banks conduct internal post-mortems to update both the model and the human review process.
- **Aviation:** Incident and near-miss reports (closely related to post-mortems) are legally mandated and are a major reason commercial aviation is so safe today.
- **AI Governance Compliance:** Under frameworks like the EU AI Act, documented incident analysis and corrective action are explicit obligations for high-risk AI systems — a real post-mortem can serve as compliance evidence.

---

## 5. Worked Example

**Scenario:** Using Case Study B from Topic 1 (automated medical triage), write a complete post-mortem.

---

**POST-MORTEM: AI Triage Assistant — Missed Emergency Case**

**What Failed:**
On a routine operating day, the AI triage assistant scored a patient's symptom description as "routine" priority. The patient was, in fact, experiencing an emergency cardiac event. Because staff had begun trusting "routine" scores without an independent vital-signs check, the patient waited significantly longer than a true emergency case should, before the error was caught by an unrelated nurse observation.

**Why It Failed (Root Cause):**
The triage assistant's overall accuracy (97%) was treated as sufficient justification to skip an independent vital-signs check for "routine"-scored patients. No process existed to specifically monitor the failure rate *within* the highest-risk sub-group (patients with atypical emergency symptom descriptions). Additionally, six months of consistently correct "routine" scores had produced automation complacency (Topic 2) among triage staff, further reducing the chance of the error being caught quickly through informal vigilance.

**Who Was Accountable:**
The clinical operations lead was accountable for approving the triage workflow rollout without a mandatory independent vital-signs check step. The AI vendor was accountable for not providing sub-group-level accuracy reporting alongside the overall accuracy metric.

**What Governance Control Would Have Prevented It:**
1. A **mandatory, system-enforced** vital-signs check for every patient before any action is taken on a "routine" AI score — removing reliance on staff discretion (directly fixing the missed checkpoint from Topic 3's decision rule).
2. **Sub-group accuracy reporting** from the AI vendor, specifically tracking false-negative rate on atypical/rare-presentation emergency cases — not just overall accuracy (directly fixing the "hidden failure rate" pattern from Case Study B).
3. A **periodic injected test case** in the review workflow (Topic 2's automation-complacency safeguard), to verify staff vigilance remains active even after months of reliable AI performance.

---

This worked example demonstrates the complete four-section structure, written in neutral, blameless, but fully accountable language, with governance recommendations specific enough to actually prevent recurrence — exactly the standard expected of your Unit 15 Capstone red-teaming write-up.

---

## 6. Key Takeaways

- A **post-mortem** is a structured, blameless report: What Failed → Why It Failed (root cause) → Who Was Accountable → What Governance Control Would Have Prevented It.
- **Blameless** means the document's purpose is system improvement, not punishment — but accountability is still clearly, factually named.
- Always dig past the **immediate cause** ("the AI was wrong") to the **root cause** ("why did our system/process allow this to happen").
- End every post-mortem with **specific, assignable governance actions** — vague promises to "be more careful" are not acceptable fixes.
- Post-mortems are industry-standard practice (SRE culture, aviation incident reports, hospital M&M reviews) and, under frameworks like the EU AI Act, can serve as regulatory compliance evidence.
- **Interview tip:** Being able to write a clear, root-cause-focused, blameless post-mortem is a strong signal of engineering maturity — many interviewers ask candidates to critique or write one.
- This topic closes Unit 10 by turning Topics 1–3 (case studies, complacency, checkpoint design) into one professional deliverable format you will reuse in your Capstone.

---

## 7. Reference Links

- [Google SRE Book — Postmortem Culture: Learning from Failure](https://sre.google/sre-book/postmortem-culture/) — the primary authentic industry reference for blameless post-mortem practice.
- [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework) — Manage function, on documenting and responding to AI system incidents.
- [EU AI Act — official text](https://artificialintelligenceact.eu/) — incident documentation obligations for high-risk AI systems.
