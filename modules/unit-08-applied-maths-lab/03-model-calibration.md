# Unit 8 — Applied Maths Lab
## Topic 3: Model Calibration

*(Covers: Calibration — does the model's stated confidence match its actual accuracy?)*

---

## 1. Learning Objectives

By the end of this topic, you will be able to:

1. **Explain** what it means for a model to be "well-calibrated" versus "overconfident" or "underconfident."
2. **Describe** why a model's stated confidence score is not automatically trustworthy just because it sounds precise.
3. **Implement** (by hand) a simple calibration check by comparing stated confidence to actual observed accuracy.
4. **Evaluate** whether a given AI system's confidence scores can be trusted for a specific decision-making use case.

---

## 2. Overview

Many AI systems don't just give you an answer — they also give you a **confidence score** ("I am 92% sure this is correct"). But here's a question every AI-native engineer must learn to ask: **can you trust that number?**

**Calibration** is the study of exactly this question. A model is "well-calibrated" if, whenever it says "90% confident," it is actually correct about 90% of the time across many such predictions. A model can have excellent accuracy but still be poorly calibrated — for example, a model might be right 85% of the time overall, yet claim "99% confidence" on almost everything, which would make its confidence scores useless for decision-making, even though its raw answers are often correct.

This matters enormously for AI oversight: if your system says "I am 95% confident this loan applicant will repay," and you plan to auto-approve anything above 90% confidence, you are trusting that the 95% number is *meaningful*. If the model is actually overconfident, you could be approving many risky loans while believing you have a strong safety margin. Calibration checking is one of the concrete, numerical ways you — the human specifying and verifying the AI system — hold the model accountable, tying directly back to the **Judgment Framework's Question 2: "Can I verify this without the AI?"**

---

## 3. Description

**Definition:** A model is **calibrated** when its predicted confidence level matches its real-world accuracy rate over many predictions. It is **overconfident** if its stated confidence is consistently higher than its actual accuracy, and **underconfident** if the reverse is true.

**Key Terminology:**

| Term | Simple Meaning |
|---|---|
| **Confidence score** | The probability the model itself reports alongside its answer (e.g., "92% sure"). |
| **Actual accuracy (for a confidence bucket)** | Out of all predictions the model made at roughly that confidence level, what percentage were actually correct. |
| **Calibration gap** | The difference between stated confidence and actual accuracy for a group of predictions. A large gap means poor calibration. |

**How to check calibration by hand (the method):**

1. Collect a set of the model's predictions, along with the confidence score it gave for each one, and whether each was actually correct.
2. Group the predictions into "confidence buckets" (e.g., all predictions where the model said "around 90% confident").
3. For each bucket, calculate the **actual accuracy**: (number of correct predictions in that bucket) ÷ (total predictions in that bucket).
4. Compare the bucket's average stated confidence to its actual accuracy. A well-calibrated model will show these two numbers close together across every bucket.

**Worked Comparison Table:**

| Confidence Bucket | Number of Predictions | Number Actually Correct | Actual Accuracy | Calibration Gap | Verdict |
|---|---|---|---|---|---|
| ~90% confident | 20 | 12 | 12/20 = 60% | 90% − 60% = **30 points** | Badly **overconfident** |
| ~60% confident | 15 | 9 | 9/15 = 60% | 60% − 60% = **0 points** | **Well-calibrated** |
| ~40% confident | 10 | 6 | 6/10 = 60% | 40% − 60% = **−20 points** | **Underconfident** |

**Reading this table:** Notice something striking — in all three buckets, the model's *actual* accuracy is 60%. But its *stated* confidence varies wildly (90%, 60%, 40%) for predictions that are, in reality, all equally reliable. This is a textbook overconfidence problem in the first row and an underconfidence problem in the third row — only the middle bucket, where stated confidence (60%) matches actual accuracy (60%), is genuinely well-calibrated.

> **Important Note:** A model can have high overall accuracy and still be poorly calibrated (as shown above — all three groups had 60% real accuracy, yet the model claimed vastly different confidence levels). Calibration and accuracy are **two separate properties** — always check both, never assume one implies the other.

**Best Practices:**

- Never trust a confidence score at face value without checking it against real outcomes on a held-out test set (data the model wasn't trained or tuned on).
- For high-stakes decisions (loan approval, medical triage), require calibration checks before allowing the AI's confidence score to influence any automatic decision threshold.
- Re-check calibration periodically — a model that was calibrated at launch can drift as real-world data changes over time.

**Common Beginner Mistakes:**

- Assuming a model's stated "confidence" is a mathematically rigorous probability just because it's presented as a percentage — for many AI systems (especially LLMs describing their own certainty in words), this number is itself just another prediction, not a guaranteed truth.
- Checking calibration using the same data the model was trained on, which will make it look artificially well-calibrated — always use fresh, unseen test cases.
- Confusing "high confidence" with "high accuracy" — as this topic's worked table shows, these can point in completely different directions.

---

## 4. Real World Application

- **Banking / loan approval:** Before auto-approving loans above a "95% confidence" threshold, a bank's risk team must verify that the model's 95%-confidence predictions really are correct about 95% of the time on real historical outcomes.
- **Healthcare AI triage:** A diagnostic AI claiming "85% confident this scan shows an anomaly" must be calibration-tested on thousands of real, doctor-confirmed cases before hospitals can trust that number for triage prioritisation.
- **Weather forecasting apps:** "70% chance of rain" claims are calibration-checked over years of historical forecasts versus actual rainfall — a well-known, long-studied example of calibration in the real world.
- **AI content moderation:** A platform auto-removing posts only above a "99% confidence this is harmful content" threshold needs calibration proof that 99%-confidence flags really are correct 99% of the time, to avoid wrongly censoring genuine users.
- **Vernacular AI translation quality flags:** A translation tool flagging "low confidence" translations for human review is only useful if "low confidence" reliably correlates with actually poor translations.

---

## 5. Worked Example

**Scenario:** An AI-based skin-condition screening app is tested on 100 real, doctor-verified photos. It groups its predictions by stated confidence and reports the following:

| Confidence Bucket | Predictions | Actually Correct |
|---|---|---|
| ~95% confident | 40 | 39 |
| ~70% confident | 40 | 27 |
| ~50% confident | 20 | 9 |

**Step-by-step calibration check:**

1. **95% bucket:** Actual accuracy = 39/40 = **97.5%**. Calibration gap = 95% − 97.5% = **−2.5 points** (essentially well-calibrated, very slightly underconfident).
2. **70% bucket:** Actual accuracy = 27/40 = **67.5%**. Calibration gap = 70% − 67.5% = **+2.5 points** (essentially well-calibrated).
3. **50% bucket:** Actual accuracy = 9/20 = **45%**. Calibration gap = 50% − 45% = **+5 points** (reasonably close, slightly overconfident).

**Conclusion:** This particular model is reasonably well-calibrated across all three confidence bands — its stated confidence closely tracks its real-world accuracy, with gaps under 5 percentage points everywhere. This is a *good* sign for using its confidence scores to help prioritise which cases a dermatologist should review first (e.g., review "50% confident" flagged cases with more scrutiny than "95% confident" ones) — but note that even a well-calibrated AI screening tool must still route final diagnosis decisions to a qualified doctor, per the high-stakes-domain principle from Unit 9.

---

## 6. Key Takeaways

- **Calibration** checks whether a model's stated confidence matches its real-world accuracy — this is different from checking accuracy alone.
- **Overconfident** = stated confidence higher than actual accuracy. **Underconfident** = stated confidence lower than actual accuracy.
- Calculate actual accuracy per confidence bucket: (correct predictions in bucket) ÷ (total predictions in bucket), then compare to the bucket's average stated confidence.
- A model can be accurate overall but still badly calibrated — always check both properties separately.
- Never test calibration on training data — always use fresh, unseen, real-world test cases.
- **Interview tip:** Being asked "how would you check if a model's confidence scores are trustworthy?" is a direct calibration question — describe the bucket-and-compare method above.
- Calibration checks are a key part of preparing your **capstone evaluation plan** (the next topic in this unit) — a system's reliability is not just "is it right," but "does it know when it might be wrong."

---

## 7. Reference Links

- [Google Machine Learning Crash Course — Classification thresholds and calibration concepts](https://developers.google.com/machine-learning/crash-course) — foundational framing.
- [NIST AI Risk Management Framework — Measure Function](https://www.nist.gov/itl/ai-risk-management-framework) — official guidance on measuring AI system trustworthiness, including confidence reliability.
- [GeeksforGeeks — Model Evaluation Techniques](https://www.geeksforgeeks.org/) — supplementary reading on evaluation practices.
