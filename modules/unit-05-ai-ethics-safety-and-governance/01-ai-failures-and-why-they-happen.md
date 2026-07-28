# Unit 5 — AI Ethics, Safety and Governance
## Topic 1: AI Failures and Why They Happen

*(Covers: Real AI failure cases — healthcare misdiagnosis, hiring bias, deepfake harm · Hallucination — why AI states falsehoods confidently · Data bias — how biased training data produces biased model output)*

---

## 1. Learning Objectives

By the end of this topic, you will be able to:

1. **Describe** at least three real categories of AI failure and the pattern of harm each one causes.
2. **Explain** why an AI model can state a wrong answer with complete confidence (hallucination).
3. **Identify** how bias enters an AI system through its training data.
4. **Differentiate** between a hallucination failure and a bias failure.
5. **Analyze** a given AI failure scenario and trace it back to its root cause (bad data, bad design, or missing oversight).
6. **Evaluate** what safeguard could have prevented a specific AI failure case.

---

## 2. Overview

Every powerful technology has a failure history — bridges collapsed before engineers understood load limits, and medicines were withdrawn before regulators understood drug safety trials. AI is no different, except its failures are happening in **public, at scale, and right now**, while you are training to build the next generation of these systems.

As someone who will specify, build, and oversee AI-powered software, you cannot treat "the AI might get it wrong" as a footnote. You must treat it as a **first-class engineering constraint** — the same way a civil engineer treats gravity. This topic studies three recurring failure patterns: real-world failure cases across industries, **hallucination** (AI confidently stating false information), and **data bias** (AI inheriting unfairness from the data it learned from).

This connects directly to the **Judgment Framework** (Unit 9) and the **governance frameworks** (Topic 4 of this unit) — you cannot design good oversight until you know precisely what you are guarding against. Understanding *why* these failures happen — not just that they happen — is what separates an AI-native engineer who can responsibly ship a system from someone who is merely impressed by a demo.

---

## 3. Description

### 3.1 Real AI Failure Cases

**Definition:** An AI failure is any instance where an AI system's output causes harm, unfairness, or a wrong decision that a careful human process would likely have avoided.

Let's look at three well-documented **categories** of AI failure (described generically, as patterns you should recognise — not as an accusation against any single named product or company):

**Category A — Healthcare misdiagnosis pattern:** AI diagnostic tools trained mostly on data from one demographic group (e.g., lighter skin tones in dermatology image datasets, or one hospital's patient population) have shown reduced accuracy when used on patients outside that group. The failure isn't that "the AI is bad at medicine" — it's that the AI only ever *saw* a narrow slice of medicine during training, and confidently applied that narrow pattern to everyone.

**Category B — Hiring bias pattern:** Several companies have piloted AI résumé-screening tools that learned from years of past hiring decisions. If those past decisions favoured one gender or background (even unintentionally), the AI learns that pattern as "what a good candidate looks like" and repeats it — automating yesterday's bias at today's scale.

**Category C — Deepfake harm pattern:** Generative AI can now create highly realistic fake images, audio, and video of real people saying or doing things they never did. This has been used for financial fraud (fake voice calls impersonating executives to authorize wire transfers), fake celebrity endorsements, and non-consensual harmful content. The underlying technology (multimodal generation) is neutral — the harm comes from the *absence of safeguards* around who can generate what.

**Why this matters for you:** All three categories share one root lesson — **an AI system reflects and amplifies the data and process it was built on.** It does not have independent moral judgment. It cannot tell you "this is unfair" unless it was specifically designed and tested to catch that.

---

### 3.2 Hallucination — Why AI States Falsehoods Confidently

**Definition:** **Hallucination** is when an AI model generates information that sounds fluent and confident but is factually incorrect, fabricated, or unsupported by any real source.

**Why this happens:** Recall from Unit 1 and Unit 3 that an LLM generates text by predicting the *most statistically likely next word*, based on patterns learned during training — it is not "looking up" facts in a database. If you ask it something obscure, or something outside its training data, it will still try to produce a fluent, confident-sounding answer, because fluency is what it was trained to produce. It has no built-in mechanism that says "I don't actually know this" unless it has been specifically trained and prompted to express uncertainty.

**A simple analogy:** Imagine a very well-read student who has to answer an exam question instantly, out loud, with no notes, and has been trained their whole life to *never leave a blank answer*. Faced with a question they don't fully know, they'll construct the most plausible-sounding answer they can, using patterns from everything else they've studied — sounding completely confident while being wrong. That is hallucination, in human terms.

**Key terminology:**

| Term | Simple Meaning |
|---|---|
| **Hallucination** | A confident, fluent, but factually wrong AI output. |
| **Grounding** | Connecting an AI's answer to a verifiable, real source of truth (e.g., a document, a database). |
| **Confabulation** | A term borrowed from psychology — filling gaps in memory with plausible-sounding fabrication, without intent to deceive. Hallucination is the AI-system equivalent. |

**Important Note:** Hallucination is *not* a rare bug that will disappear with the next model update — it is a structural consequence of how generative AI works today. The correct professional response is not "hope it doesn't happen," but designing your system (through RAG, verification steps, and human review — covered later in Units 9 and 14) to **catch** it before it reaches a real decision.

---

### 3.3 Data Bias — How Biased Training Data Produces Biased Output

**Definition:** **Data bias** occurs when the data used to train an AI model over- or under-represents certain groups, situations, or outcomes, causing the model to learn a skewed pattern of "normal."

**Why this exists:** AI models learn entirely from examples. If 90% of the loan-approval examples an AI was trained on came from applicants in cities, it may perform poorly (or unfairly) when evaluating rural applicants — not because it is "prejudiced," but because it never saw enough rural examples to learn accurate patterns for them.

**How bias enters a system — three common entry points:**

1. **Historical bias:** The real-world data itself reflects past human decisions that were already unfair (e.g., historical hiring or lending records).
2. **Sampling bias:** The data collected over-represents one group and under-represents another (e.g., a voice-recognition dataset recorded mostly from one accent group).
3. **Labeling bias:** The humans who labelled the training data (e.g., "this loan application is risky" / "not risky") carried their own unconscious assumptions into those labels.

**Comparison Table — Hallucination vs Data Bias**

| Aspect | Hallucination | Data Bias |
|---|---|---|
| What goes wrong | The model invents information that isn't true | The model learns a skewed/unfair pattern from real data |
| Root cause | Predicting plausible text without a grounding check | Training data that over/under-represents groups or outcomes |
| Typical symptom | A confident, wrong fact (e.g., a fake case citation) | Consistently worse or unfair outcomes for a specific group |
| Primary fix | Grounding (RAG), verification, human review | Auditing training data, testing outcomes across groups, fairness metrics |

**Best Practices:**

- Always test an AI system's outputs across different user groups before deployment — don't assume uniform performance.
- Never treat an AI's confident tone as evidence of correctness — confidence and correctness are **not the same thing** in generative AI.
- Document *what data* your system was trained or fine-tuned on, so future bias audits are possible.

**Common Beginner Mistakes:**

- Assuming that because a model is "big" or "advanced," it cannot be biased or wrong.
- Testing an AI system only with the type of user you personally represent, and missing failures for other groups.
- Treating a single hallucinated wrong answer as a one-off "bug" instead of a pattern to be systematically tested for.

---

## 4. Real World Application

- **Healthcare (India):** An AI symptom-checker used in rural telemedicine must be tested on diverse regional health data (not just urban hospital records) before being trusted for triage — else it risks the "healthcare misdiagnosis" failure pattern for underserved populations.
- **Banking/FinTech:** A loan-approval AI must be regularly audited to ensure it isn't systematically rejecting applicants from certain pin codes or occupations due to historical bias in past loan data.
- **Recruitment Tech:** Companies using AI résumé screeners in India must audit whether the tool is filtering out candidates from certain colleges, genders, or regions in patterns that don't reflect actual job performance.
- **Content Moderation / Social Media:** Deepfake-detection AI must be continuously retrained as generation techniques evolve, since a static detector quickly becomes outdated.
- **AI Chatbots / Legal & Compliance Copilots:** A chatbot answering questions about company policy must be grounded in the actual policy document (RAG, Unit 14) — not left to hallucinate an answer from general training patterns, especially in regulated domains.

---

## 5. Worked Example

**Scenario:** A fictional Indian ed-tech startup builds an AI tool that predicts which students are "at risk of dropping out" so teachers can intervene early. After six months, teachers notice the tool flags a disproportionate number of first-generation college students (students whose parents did not attend college) as "high risk," even when their grades are average.

**Root-cause walkthrough:**

1. **Ask:** What data was this model trained on? → Past student records, where "dropped out" was the label the model learned to predict.
2. **Ask:** Did the historical dropout data include more first-generation students, for reasons unrelated to ability (e.g., financial pressure, lack of family academic support)? → Yes.
3. **Diagnosis:** This is a **data bias** failure (historical bias) — the model learned "first-generation student" as a correlated pattern with "dropout," even though it is not a fair or causal predictor of a specific student's risk.
4. **Not** a hallucination — the model isn't inventing facts; it is faithfully reflecting a skewed pattern from real historical data.
5. **Fix:** Remove or down-weight proxy variables correlated with protected characteristics, test the model's flagging rate across student subgroups, and require a human counsellor to review any "high risk" flag before any action is taken — never let the AI's flag alone determine a student's outcome.

---

## 6. Key Takeaways

- AI failures generally fall into recognisable patterns: skewed training data, confident fabrication (hallucination), or missing human oversight.
- **Hallucination** = confident, fluent, but factually wrong output — a structural feature of how generative models predict text, not a rare glitch.
- **Data bias** = the model faithfully learns and repeats unfair patterns present in its training data.
- Confidence in tone is not evidence of correctness — never confuse the two.
- Bias can enter through historical data, sampling, or human labelling — audit all three.
- The fix for hallucination is grounding + verification; the fix for bias is data auditing + outcome testing across groups.
- Always test AI systems across diverse user groups before trusting them in production.
- **Interview tip:** If asked to explain hallucination, mention *token-prediction without grounding* — this shows you understand the mechanism, not just the symptom.
- This topic is the practical foundation for the **four pillars of ethics** (Topic 2) and **governance frameworks** (Topic 4) later in this unit.

---

## 7. Reference Links

- [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework) — official U.S. framework discussing AI failure modes including bias and reliability.
- [Anthropic Documentation](https://docs.claude.com/) — model usage guidance, including notes on model limitations and responsible use.
- [Google Machine Learning Crash Course — Fairness](https://developers.google.com/machine-learning/crash-course) — beginner-friendly introduction to fairness and bias in ML systems.
