# Unit 8 — Applied Maths Lab
## Topic 4: Planning Your Capstone Evaluation

*(Covers: Designing a domain evaluation plan — metric, test set size, pass/fail threshold)*

---

## 1. Learning Objectives

By the end of this topic, you will be able to:

1. **Explain** why every AI system needs a written evaluation plan before it can be trusted or deployed.
2. **Identify** an appropriate metric (accuracy, precision, recall, F1, or a custom rubric) for a given AI system's purpose.
3. **Create** a complete evaluation plan, including metric choice, test set size, and pass/fail threshold, for a real or illustrative AI system.
4. **Analyze** the trade-offs involved in choosing a small vs large test set, and a strict vs lenient threshold.

---

## 2. Overview

Every topic in this unit — embeddings, similarity scores, precision/recall, F1, and calibration — exists to serve one final, practical purpose: **helping you design a real evaluation plan** for an AI system you build or oversee. This is not an academic exercise. In **Week 15 (Capstone Build Sprint)**, you will be required to build a **5-case evaluation harness** for your own capstone project, and the planning skill you build here is exactly what makes that possible.

An evaluation plan answers three simple but critical questions, in writing, *before* your AI system goes anywhere near a real user:

1. **What will we measure?** (the metric)
2. **How much evidence do we need before trusting the result?** (the test set size)
3. **What result counts as "good enough to ship"?** (the pass/fail threshold)

Without answering these three questions in advance, "testing" an AI system becomes vague and subjective — you end up judging quality by vibes ("it seemed to work when I tried it a few times"), which is exactly the kind of unverified trust that leads to the real AI failures you studied in Unit 5 and Unit 10.

---

## 3. Description

**Definition:** An **evaluation plan** is a short, written document that specifies the metric, test set, and pass/fail threshold that will be used to judge whether an AI system's output quality is acceptable.

**Key Terminology:**

| Term | Simple Meaning |
|---|---|
| **Metric** | The specific number you will calculate to judge quality (e.g., accuracy, precision, recall, F1, or a simple pass/fail rubric score from human review). |
| **Test set** | A fixed collection of example inputs (with known correct/expected outputs) that you run the AI system against. |
| **Test set size** | How many test cases are in your test set — more cases give more confident results, but take more time to prepare and review. |
| **Pass/fail threshold** | The minimum score the system must achieve on the test set for you to consider it acceptable for its intended use. |

**Step-by-step framework for designing an evaluation plan:**

1. **Step 1 — Define what "correct" means for this specific system.** Is there one exact right answer (like a calculator), or is it more subjective (like "a helpful, polite customer support reply")? This decision determines whether you'll use a hard metric (accuracy/precision/recall/F1) or a human-rated rubric (e.g., a 1–5 quality scale).
2. **Step 2 — Choose the metric that matches the cost of errors** (recap from Topic 2 of this unit): if false negatives are more dangerous, prioritise recall; if false positives are more dangerous, prioritise precision; if both matter roughly equally, use F1 or an overall pass rate.
3. **Step 3 — Decide test set size.** As a practical minimum for a course capstone, use **at least 20–25 test cases** — enough to catch obvious failure patterns, without requiring the effort of a full production-scale test suite (which might use thousands of cases). Always deliberately include a few **edge cases** (unusual, tricky, or boundary inputs) alongside typical ones.
4. **Step 4 — Set a pass/fail threshold, and justify it in writing.** A higher-stakes system (health, finance, legal) should demand a stricter threshold (e.g., ≥90–95%) than a lower-stakes one (e.g., a casual recommendation feature, where ≥75–80% might be acceptable).
5. **Step 5 — Write it all down BEFORE running the tests.** Deciding your threshold *after* seeing results is a serious bias risk (you might unconsciously lower the bar to make your system "pass") — this is why professional evaluation plans are written and agreed upon in advance.

**Worked Example Evaluation Plan — Vernacular Translation Assistant:**

| Element | Decision |
|---|---|
| **System purpose** | Translate short customer-support messages from Hindi to Tamil for a regional e-commerce helpdesk. |
| **Metric** | % of translations rated "acceptable" (correct meaning, natural phrasing) by a human Tamil-speaking reviewer. |
| **Test set size** | 25 sentence pairs, covering 3 categories: order status queries (10), refund/complaint messages (10), and general greetings/small talk (5) — including a few deliberately tricky idiomatic phrases as edge cases. |
| **Pass/fail threshold** | ≥ 80% (at least 20 out of 25 translations rated acceptable). |
| **Why this threshold?** | This is a customer-facing but not safety-critical system — a few imperfect translations are recoverable through follow-up conversation, so 80% is a reasonable, achievable bar for course-project scope, while still being demanding enough to catch a genuinely broken system. |

**Worked Example Evaluation Plan — Loan-Eligibility Explainer Bot (higher stakes):**

| Element | Decision |
|---|---|
| **System purpose** | Explain, in plain language, why a loan application was approved or rejected, based on a fixed set of bank-provided reasons. |
| **Metric** | % of explanations rated "accurate and non-misleading" by a human loan-officer reviewer. |
| **Test set size** | 20 cases, covering both approvals and rejections across different reason codes. |
| **Pass/fail threshold** | ≥ 90% (at least 18 out of 20 explanations rated accurate). |
| **Why this threshold?** | This system touches a financial decision that affects real people's lives and involves fairness/transparency obligations (recall Unit 5's four pillars) — a stricter threshold and mandatory human review of any failing cases is justified. |

**Best Practices:**

- Always write the evaluation plan **before** building or testing the system, not after.
- Include deliberately tricky "edge case" inputs in your test set, not just easy typical examples — real failures usually hide in the edge cases.
- Match your threshold's strictness to the real-world cost of failure for that specific system (recap of the Judgment Framework, Unit 9).
- Re-run your evaluation plan whenever you make a meaningful change to your system's prompt or logic — a passing system today can silently regress after a change.

**Common Beginner Mistakes:**

- Testing with only 3–5 "easy" examples and declaring success — too small a test set can hide real failure patterns.
- Choosing the pass/fail threshold only after seeing how the system performed (this is a form of "moving the goalposts" and undermines the entire point of evaluation).
- Using accuracy as the default metric for every system, without checking whether precision, recall, or a human-rated rubric would better reflect what "success" actually means for that use case.

---

## 4. Real World Application

- **Capstone project (Unit 15):** This exact framework is what you will apply to build your own 5-case (minimum) evaluation harness for your final AI-native engineering project.
- **Enterprise AI rollouts:** Companies deploying an AI customer-support bot typically require a signed-off evaluation plan, including thresholds, before the bot is allowed to go live with real customers.
- **Healthcare AI regulatory approval:** Regulators (aligned with frameworks like the EU AI Act's high-risk obligations, Unit 5) require documented evaluation plans, including test set design and pass/fail criteria, before approving medical AI tools.
- **EdTech platforms:** Before deploying an AI grading assistant, a school might require it to match human-graded scores within a defined tolerance on a test set of previously graded assignments.
- **Government/public-sector AI (e.g., agricultural advisory chatbots):** Evaluation plans with clear thresholds are increasingly required for public accountability, aligning with MEITY's advisory guidance (Unit 5).

---

## 5. Worked Example

**Scenario:** You are building a capstone project: an AI assistant that answers common railway-booking questions (e.g., "How do I check my PNR status?", "What is the cancellation policy?"). Design a complete evaluation plan.

**Step 1 — What does "correct" mean here?** Since answers are informational (not a single fixed calculation), correctness will be judged by a human reviewer checking: (a) factual accuracy against the real railway policy documents, and (b) clarity for a non-technical user.

**Step 2 — Choose the metric:** % of answers rated "factually accurate and clear" by a human reviewer using a simple pass/fail rubric per question (not a numeric score, to keep grading fast and consistent).

**Step 3 — Test set size:** 25 test questions: 10 about PNR/booking status, 8 about cancellations/refunds, 5 about general travel rules, and 2 deliberately tricky edge cases (e.g., a question mixing two topics, or a question the system should correctly say "I don't have information on this — please check with railway staff").

**Step 4 — Pass/fail threshold:** ≥ 80% (at least 20 out of 25 correct) — chosen because this is an informational assistant (not processing actual payments or bookings), so the cost of an occasional imperfect answer is moderate, not severe, but 80% still ensures the system is reliably useful rather than a coin-flip.

**Step 5 — Documented in writing, before testing begins:**

> *"This evaluation plan for the Railway FAQ Assistant will be considered PASSED if the system achieves ≥ 80% (20/25) correct, human-verified answers across the 25-question test set described above, including the 2 required edge cases. This threshold and test set were finalised before any testing began."*

This single paragraph — written *before* running a single test — is the exact deliverable expected in your capstone's testing-and-evaluation documentation (Unit 15).

---

## 6. Key Takeaways

- An evaluation plan answers three questions in advance: **what metric**, **how much test data**, and **what score counts as passing**.
- Match your chosen metric to what "success" genuinely means for that system — a hard numeric metric (accuracy/precision/recall/F1) for objectively checkable tasks, a human-rated rubric for subjective/informational tasks.
- Use at least 20–25 test cases for a course-level evaluation, always including a few deliberate edge cases.
- Set your pass/fail threshold based on the real-world cost of failure — stricter for high-stakes systems, more lenient for low-stakes ones.
- Always finalise metric, test set, and threshold **before** testing begins, to avoid biased goalpost-shifting.
- This planning framework is the direct foundation for your **capstone's 5-case evaluation harness** (Unit 15).
- **Interview tip:** Being able to describe how you would design an evaluation plan for a hypothetical AI system is a very common entry-level AI engineering interview question — practice the 5-step framework above until it's second nature.

---

## 7. Reference Links

- [Google Machine Learning Crash Course — Validation and Test Sets](https://developers.google.com/machine-learning/crash-course) — official grounding on why test data design matters.
- [NIST AI Risk Management Framework — Measure Function](https://www.nist.gov/itl/ai-risk-management-framework) — official guidance on structured AI evaluation planning.
- [GeeksforGeeks — Model Evaluation Techniques in Machine Learning](https://www.geeksforgeeks.org/) — supplementary reading.
