# Unit 4 — The 2026 AI Stack
## Topic 4: Comparing and Evaluating AI Tools

*(Covers: How to compare two AI tools — designing a measurable evaluation rubric · Presenting a findings-based recommendation — evidence, not opinion)*

---

## 1. Learning Objectives

By the end of this topic, you will be able to:

1. **Explain** why comparing AI tools needs a structured, measurable approach rather than a gut-feeling opinion.
2. **Design** a simple evaluation rubric with clear, measurable criteria for comparing two AI tools.
3. **Implement** a small comparison test between two AI tools on the same set of tasks.
4. **Create** a findings-based recommendation that presents evidence rather than personal preference.

---

## 2. Overview

By this point in Unit 4, you have learned what foundation models are, how they get adapted (fine-tuning, RAG), how agents and tool use extend them, and how multimodal AI expands what they can process. A natural next question, and one you will face constantly in a real job, is: **"Which AI tool should we actually use for this task?"**

This is not a question to answer with "I just liked using it" or "it felt smarter." As someone responsible for specifying and overseeing AI systems, you need to evaluate tools the way an engineer evaluates any component — with **clear, measurable criteria**, tested **evidence**, and a **written recommendation** that others can verify and trust. This topic teaches you exactly that skill: designing a fair rubric, running a simple comparison, and presenting your findings professionally. This is also excellent preparation for your capstone project in Week 15, where you will be expected to justify your architectural choices with evidence, not opinion.

---

## 3. Description

### 3.1 Designing a Measurable Evaluation Rubric

**Definition:** An **evaluation rubric** is a predefined set of criteria, each with a clear way to measure or score it, used to judge and compare options fairly and consistently.

**Why this exists:** Without a rubric, comparisons become subjective — "Tool A felt nicer" is not something a manager, a client, or a teammate can independently verify. A rubric forces you to decide *in advance* what "better" means for your specific task, and to measure it the same way for every option you're comparing.

**Common criteria used to compare AI tools:**

| Criterion | What It Measures | How to Measure It |
|---|---|---|
| **Accuracy / Correctness** | Does the tool give the right answer for the task? | Run the same test questions through both tools; score correct vs incorrect |
| **Latency** | How fast does it respond? | Time each response in seconds |
| **Cost** | How much does it cost to run per request or per month? | Check official pricing pages; calculate cost for expected usage volume |
| **Ease of Use** | How easy is it to set up and integrate? | Note setup steps, documentation quality, time to first working call |
| **Consistency** | Does it give reasonably stable answers across repeated tries? | Run the same prompt multiple times (recall Unit 1 — probabilistic systems); note variation |
| **Safety / Reliability** | Does it handle edge cases and errors gracefully? | Test a few deliberately tricky or invalid inputs |

**Rules for a good rubric:**

1. Choose criteria **before** running the comparison — deciding criteria afterward, based on which tool already looks better, introduces bias.
2. Make each criterion **measurable** — a vague criterion like "quality" should be broken into specific, testable things (accuracy, tone match, format correctness).
3. Use the **same test inputs** for every tool being compared — comparing Tool A on easy questions and Tool B on hard questions is not a fair test.
4. Decide a **weighting** if some criteria matter more than others for your specific use case (e.g., latency may matter more for a live chat feature than for a batch report generator).

**Common Mistakes:**

- Testing with only one or two examples and generalising broadly — a fair comparison needs a reasonably sized, varied test set (this connects to Week 8's evaluation-metrics ideas).
- Letting personal preference ("I just like this interface more") quietly influence a supposedly "objective" score.
- Ignoring cost or latency because accuracy "felt" more important — for many real products, latency and cost are just as critical to the business.

---

### 3.2 Presenting a Findings-Based Recommendation — Evidence, Not Opinion

**Definition:** A **findings-based recommendation** is a conclusion supported directly by the specific evidence you gathered during testing — as opposed to a general impression or preference stated without proof.

**Why this exists:** In a professional AI-native engineering role, your recommendations will influence real decisions — which vendor to pay for, which tool to integrate into a product used by thousands of people. A recommendation backed by evidence can be checked, defended, and trusted; an opinion cannot.

**Structure of a strong findings-based recommendation:**

1. **What was compared** — name the tools/models and the exact task(s) tested.
2. **How it was tested** — the rubric, the number of test cases, and the method.
3. **What was found** — the actual scores/results, ideally in a table.
4. **The recommendation** — which option to choose, and for which specific use case (a recommendation can be conditional: "Tool A for high-accuracy legal summaries; Tool B for fast, low-cost chat replies").
5. **Limitations** — be honest about what your test did *not* cover (this builds credibility, not weakness).

**Important Note:** A good recommendation is often *not* a single universal winner — it is common and professionally sound to say "Tool A is better for X, Tool B is better for Y," because different tools genuinely have different strengths (recall the **jagged frontier** idea from Week 3).

---

## 4. Real World Application

- **Customer Support Product Teams:** Compare two AI chat models on real historical support tickets, scoring accuracy, tone match, and response time, before choosing which powers the live chatbot.
- **Healthcare Software Vendors:** Compare AI document-summarisation tools on de-identified medical reports, with accuracy and safety (does it ever drop critical information?) weighted heavily.
- **EdTech Companies:** Compare AI tutoring tools on their ability to explain a Class 10 mathematics concept correctly and at an appropriate reading level.
- **Startups Choosing an AI Vendor:** Compare cost-per-request and latency across providers before committing to one for a high-volume feature like automated invoice processing.
- **Government/Public Sector AI Procurement:** Formal, rubric-based comparisons are often legally required before choosing an AI vendor for citizen-facing services — connecting this topic directly to the governance frameworks in Week 5.

---

## 5. Worked Example

**Scenario:** A college placement cell wants an AI tool to auto-draft personalised outreach emails to companies for campus placements. They are comparing two AI assistants, "Assistant A" and "Assistant B."

**Step 1 — Define the rubric (decided before testing):**

| Criterion | Weight | How Measured |
|---|---|---|
| Correctness of company/role details used | 40% | Manually check 10 generated emails against source data |
| Professional tone | 30% | Human reviewer rates tone 1–5 on 10 emails |
| Response time | 15% | Average seconds per email generated |
| Cost per 100 emails | 15% | Based on published pricing |

**Step 2 — Run the same 10 test cases through both tools and record results:**

| Criterion | Assistant A | Assistant B |
|---|---|---|
| Correctness (out of 10) | 9/10 correct | 10/10 correct |
| Tone rating (avg out of 5) | 4.6 | 3.9 |
| Avg response time | 2.1 sec | 4.8 sec |
| Cost per 100 emails | ₹80 | ₹45 |

**Step 3 — Weighted findings:** Assistant A scores higher on correctness and tone (the two highest-weighted criteria, 70% combined), while Assistant B is cheaper and slightly less accurate.

**Step 4 — Findings-based recommendation:**

> "Based on testing across 10 representative outreach scenarios, Assistant A is recommended for this task, primarily due to its stronger tone match (4.6 vs 3.9) and near-perfect factual correctness (9/10 vs 10/10, both acceptably high), which matter most for a placement cell's professional reputation. Assistant B remains a reasonable lower-cost alternative if outreach volume grows significantly and budget becomes the primary constraint. This test used only 10 email scenarios; a larger test set across more company types is recommended before a final, long-term commitment."

Notice how this recommendation cites specific numbers, states a clear-but-conditional conclusion, and honestly names its limitation — exactly the structure expected in a professional setting and in your Week 15 capstone presentation.

---

## 6. Key Takeaways

- Comparing AI tools requires a **measurable rubric** decided *before* testing, not a subjective impression formed afterward.
- Common comparison criteria include accuracy, latency, cost, ease of use, consistency, and safety/reliability.
- Use the **same test inputs** across all tools being compared for a fair test.
- A **findings-based recommendation** states what was tested, how, what was found (with numbers), the recommendation, and its limitations.
- The best recommendation is often conditional ("Tool A for X, Tool B for Y") rather than a single absolute winner — this reflects the AI **jagged frontier**.
- This skill directly prepares you for your **Week 15 capstone**, where you must justify your own architectural choices with evidence.
- **Interview tip:** When asked "how would you choose between two AI models/tools," always mention rubric design and evidence-based testing — this is a strong, structured answer interviewers look for.

---

## 7. Reference Links

- [Anthropic Documentation — Evaluating Model Performance](https://docs.claude.com/) — official guidance on evaluating model outputs.
- [Google Machine Learning Crash Course — Evaluation Concepts](https://developers.google.com/machine-learning/crash-course) — grounding in measurable evaluation approaches.
- [DeepLearning.AI — Short Courses on Evaluating LLM Applications](https://www.deeplearning.ai/short-courses/) — practical, beginner-accessible frameworks for comparing AI tools.
