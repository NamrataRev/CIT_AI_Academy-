# Unit 8 — Applied Maths Lab
## Topic 2: Evaluation Metrics in Depth

*(Covers: Precision vs recall trade-off — when does recall matter more than precision? · F1 score — balancing precision and recall into one metric · Computing accuracy, precision, recall, and F1 by hand from a confusion matrix)*

---

## 1. Learning Objectives

By the end of this topic, you will be able to:

1. **Explain** the difference between precision and recall in plain language, without relying on the formulas alone.
2. **Identify** which metric (precision or recall) matters more for a given real-world scenario.
3. **Implement** (by hand) the calculation of accuracy, precision, recall, and F1 score from a confusion matrix.
4. **Differentiate** between a model that is "accurate but useless" and one that is "genuinely reliable" using these deeper metrics.
5. **Evaluate** a classifier's performance and justify, with numbers, whether it is fit for a given use case.

---

## 2. Overview

In **Week 7**, you were introduced to accuracy, precision, recall, and the confusion matrix as concepts. This topic goes one level deeper: we now *use* those metrics together to make a real judgment call, because in real AI-native engineering work, you will rarely be handed a single number and asked to decide "is this model good?" — you will be handed a full confusion matrix, and you will need to compute multiple metrics, weigh their trade-offs, and defend your recommendation.

This is squarely inside the "AI implements, you specify and verify" discipline — your job is not to build the classifier's internal maths, but to **verify its output quality** using these exact calculations, and to know *which* metric should carry more weight for the specific system you're overseeing. Getting this wrong has real consequences: choosing the wrong metric to optimise for can mean a fraud-detection system that misses actual frauds, or a medical-screening AI that gives false reassurance to a sick patient.

---

## 3. Description

### 3.1 Precision vs Recall — Trade-off

**Quick recap of definitions:**

- **Precision** answers: *"Of everything the model FLAGGED as positive, how many were actually positive?"* High precision = few false alarms.
- **Recall** answers: *"Of everything that was ACTUALLY positive, how many did the model catch?"* High recall = few missed cases.

**Why a trade-off exists:** A model can almost always improve one of these at the cost of the other. If a fraud-detection model flags *every single transaction* as fraud, its recall becomes 100% (it never misses a real fraud) — but its precision collapses (almost every flag is a false alarm, and genuine customers get blocked constantly). Conversely, if the model only flags transactions it is *extremely* sure about, precision rises but recall drops (it now misses many real frauds that didn't look "obviously" suspicious).

**Comparison Table — When Recall Matters More vs When Precision Matters More**

| Scenario | Which metric matters more? | Why |
|---|---|---|
| Medical screening (e.g., flagging possible tumours from a scan) | **Recall** | Missing a real case (false negative) can cost a life; a false alarm just means an extra check-up. |
| Banking fraud detection | **Recall** (usually, with a human review step) | Missing real fraud costs real money; a false alarm can be resolved by a quick verification call. |
| Spam email filtering | **Precision** | Wrongly blocking an important real email (false positive) is more damaging to the user than letting one spam email through. |
| E-commerce product recommendation | **Precision** | Showing irrelevant products (false positives) annoys and drives away users; missing one possible relevant product (false negative) is low-cost. |
| Loan default risk flagging | **Balanced (F1)** | Both false approvals (bank loses money) and false rejections (denies a good customer) carry real cost. |

> **Important Note:** There is no metric that is "always correct" to optimise — the right choice always depends on **which type of mistake is more costly** for that specific real-world system. This directly connects to the **Judgment Framework's Question 1** ("What is the cost of this being wrong?") that you studied in Unit 9.

---

### 3.2 F1 Score — Balancing Precision and Recall

**Definition:** The **F1 score** is a single number that combines precision and recall into one balanced metric, using their **harmonic mean** (not a simple average).

**Why the harmonic mean, and not a simple average?** The harmonic mean punishes extreme imbalance much more heavily than a simple average would. For example, if precision = 100% but recall = 1%, a simple average would say "50% — not bad," which is misleading (the model is nearly useless, missing 99% of real cases). The harmonic mean correctly reports a very low score in this situation, reflecting the real weakness.

**Formula:**

$$F1 = 2 \times \frac{\text{Precision} \times \text{Recall}}{\text{Precision} + \text{Recall}}$$

- **2** — the constant that makes the harmonic mean formula work out correctly for two values.
- **Precision × Recall** (numerator part) — multiplying the two metrics together.
- **Precision + Recall** (denominator) — adding the two metrics together.

**When to use F1 instead of precision or recall alone:** Use F1 when you need one single number to compare models or track progress over time, and when both false positives and false negatives carry meaningfully similar costs (i.e., neither one clearly dominates, unlike the medical/spam examples above).

---

### 3.3 Computing Accuracy, Precision, Recall, and F1 by Hand From a Confusion Matrix

**Scenario:** A spam-email classifier is tested on 100 emails. Here is its confusion matrix:

| | Predicted: Spam | Predicted: Not Spam |
|---|---|---|
| **Actual: Spam** | TP = 24 | FN = 6 |
| **Actual: Not Spam** | FP = 10 | TN = 60 |

**Key Terminology (recap):**

| Term | Meaning |
|---|---|
| **TP (True Positive)** | Model said "spam," and it really was spam. |
| **FN (False Negative)** | Model said "not spam," but it really was spam (a miss). |
| **FP (False Positive)** | Model said "spam," but it really was not spam (a false alarm). |
| **TN (True Negative)** | Model said "not spam," and it really was not spam. |

**Step 1 — Sanity-check the totals:**
- Total emails = TP + FN + FP + TN = 24 + 6 + 10 + 60 = **100** ✓ (matches given total)
- Actual spam emails = TP + FN = 24 + 6 = **30**
- Actual not-spam emails = FP + TN = 10 + 60 = **70**

**Step 2 — Accuracy:**

$$\text{Accuracy} = \frac{TP + TN}{\text{Total}} = \frac{24 + 60}{100} = \frac{84}{100} = 0.84 = 84\%$$

**Step 3 — Precision:**

$$\text{Precision} = \frac{TP}{TP + FP} = \frac{24}{24 + 10} = \frac{24}{34} \approx 0.706 = 70.6\%$$

**Step 4 — Recall:**

$$\text{Recall} = \frac{TP}{TP + FN} = \frac{24}{24 + 6} = \frac{24}{30} = 0.80 = 80\%$$

**Step 5 — F1 Score:**

$$F1 = 2 \times \frac{0.706 \times 0.80}{0.706 + 0.80} = 2 \times \frac{0.565}{1.506} \approx 2 \times 0.375 = 0.75 = 75\%$$

*(Quick check using the shortcut formula F1 = 2TP ÷ (2TP + FP + FN) = 48 ÷ (48 + 10 + 6) = 48 ÷ 64 = 0.75 — matches ✓)*

**Interpretation:** This spam classifier is 84% accurate overall, but its precision (70.6%) is noticeably lower than its recall (80%) — meaning it is somewhat trigger-happy, letting through more false alarms (10 legitimate emails wrongly marked spam) than misses (6 spam emails wrongly let through). Since we established above that **precision matters more for spam filtering** (a blocked important email is worse than one spam email getting through), this model's current balance is a genuine weakness worth improving — even though 84% accuracy alone might have sounded acceptable.

**Best Practices:**

- Always calculate precision AND recall separately before jumping to F1 — F1 alone can hide *which* type of error is more common.
- Re-verify your arithmetic using at least one alternate formula (as shown above with the F1 shortcut) before trusting your final numbers.
- Always state which metric matters most for your specific use case *before* looking at the numbers, to avoid unconsciously favouring whichever metric looks better ("motivated reasoning").

**Common Beginner Mistakes:**

- Mixing up precision and recall's denominators (Precision divides by predicted positives = TP+FP; Recall divides by actual positives = TP+FN) — write out the confusion matrix labels every time until this becomes automatic.
- Reporting only accuracy on an imbalanced dataset (e.g., very few actual spam emails) — this can look excellent while the model is actually poor at catching the minority class (this exact trap was covered in Unit 7's "Confusion matrix — why 95% accuracy can still mean frequent failure").
- Averaging precision and recall directly instead of using the harmonic mean formula for F1.

---

## 4. Real World Application

- **Banking fraud detection:** Precision/recall trade-off analysis directly decides how aggressively a bank's fraud system flags transactions for manual review.
- **Healthcare AI screening:** Regulatory bodies increasingly require F1 (or recall-weighted metrics) to be reported before an AI diagnostic tool can be deployed, connecting directly to the **EU AI Act's high-risk system obligations** (Unit 5).
- **E-commerce search relevance:** Search engineering teams track precision heavily, since irrelevant top results directly hurt conversion rates.
- **Education platforms:** An AI system flagging "at-risk" students for extra academic support is tuned for high recall (better to falsely flag a student who's actually fine than to miss a student who genuinely needs help).
- **Content moderation on social media:** Balances precision (don't wrongly remove legitimate posts) and recall (don't miss genuinely harmful content) — often reported using F1 in trust & safety dashboards.

---

## 5. Worked Example

**Scenario:** A college's AI-based plagiarism detector is tested on 50 submitted assignments. Confusion matrix:

| | Predicted: Plagiarised | Predicted: Original |
|---|---|---|
| **Actual: Plagiarised** | TP = 8 | FN = 2 |
| **Actual: Original** | FP = 5 | TN = 35 |

**Full calculation:**

1. Total check: 8 + 2 + 5 + 35 = 50 ✓
2. Accuracy = (8 + 35) / 50 = 43/50 = **0.86 = 86%**
3. Precision = 8 / (8 + 5) = 8/13 ≈ **0.615 = 61.5%**
4. Recall = 8 / (8 + 2) = 8/10 = **0.80 = 80%**
5. F1 = 2 × (0.615 × 0.80) / (0.615 + 0.80) = 2 × 0.492/1.415 ≈ **0.695 = 69.5%**

**Judgment call:** Precision (61.5%) is quite low — meaning more than a third of the students flagged as "plagiarised" were actually original submissions. For a system whose false accusations can seriously harm a genuine student (an academic-integrity case), this precision level is a red flag: the Judgment Framework tells us a human reviewer must always verify a "plagiarised" flag before any disciplinary action is taken — the AI's role here is to *assist* a human's judgment, never to be the final word (a direct callback to Unit 9's high-stakes-domain principle).

---

## 6. Key Takeaways

- **Precision** = of what the model flagged, how much was correct. **Recall** = of what was truly positive, how much did the model catch.
- Improving one usually costs the other — this is the precision/recall trade-off.
- **F1 score** = harmonic mean of precision and recall; punishes extreme imbalance far more than a simple average would.
- Formula: `F1 = 2 × (Precision × Recall) / (Precision + Recall)`.
- Always compute TP, FN, FP, TN sanity-checks first (do the rows and columns add up to the given totals?).
- The "right" metric to prioritise depends entirely on which type of error is more costly for that specific system — never assume accuracy alone tells the full story.
- **Interview tip:** Interviewers commonly ask you to compute precision, recall, and F1 from a raw confusion matrix on the spot — practice doing this without a calculator.
- High-stakes domains (medical, academic integrity, legal) almost always require a human-in-the-loop check on top of any single metric, however good the numbers look.

---

## 7. Reference Links

- [Google Machine Learning Crash Course — Classification: Precision and Recall](https://developers.google.com/machine-learning/crash-course/classification/precision-and-recall) — official interactive explanation.
- [GeeksforGeeks — F1 Score in Machine Learning](https://www.geeksforgeeks.org/) — supplementary worked examples.
- [NIST AI Risk Management Framework — Measure Function](https://www.nist.gov/itl/ai-risk-management-framework) — for context on why documented evaluation metrics matter for AI system oversight.
