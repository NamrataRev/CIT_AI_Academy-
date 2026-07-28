# Unit 7 — Probability, Statistics and AI Confidence
## Topic 2: How LLMs Use Probability

*(Covers: Why LLMs output a probability distribution, not a single fixed answer · Temperature — low picks the most likely token, high introduces variation)*

---

## 1. Learning Objectives

By the end of this topic, you will be able to:

1. **Explain** why an LLM produces a probability distribution over possible next words instead of one fixed answer.
2. **Describe** the role of a "logit" (raw score) in how a model ranks possible next tokens.
3. **Calculate**, by hand, how the softmax-with-temperature formula reshapes a probability distribution.
4. **Differentiate** between low-temperature and high-temperature output, using a worked numeric example.
5. **Evaluate** which temperature setting is appropriate for a given real-world AI task.

---

## 2. Overview

In Unit 1, you learned *that* an LLM like Claude is probabilistic — the same prompt can produce different answers. In Unit 7 Topic 1, you learned the mathematics of probability itself. Now we bring the two together: **exactly how** does a model turn its internal calculations into the probability percentages you saw in the Unit 1 example ("New Delhi" — 91% likely)?

Understanding this matters enormously for an AI-native engineer, because a setting called **temperature** — which controls exactly how "confident vs. creative" a model's output is — is something you will directly configure every time you call an LLM's API (you'll do this hands-on from Unit 12 onward). Get temperature wrong, and you'll either get a chatbot that repeats the same robotic phrasing every time, or one that starts inventing unreliable, overly random answers. This topic gives you the mathematical intuition to make that decision correctly, rather than by guesswork.

---

## 3. Description

### 3.1 Why LLMs Output a Probability Distribution, Not a Single Fixed Answer

**Definition:** At each step of generating text, an LLM does not "know" one correct next word. Instead, it calculates a **probability distribution** — a full list of every possible next word (technically, "token") in its vocabulary, each paired with a probability of how likely it is to come next, with all these probabilities adding up to exactly 1 (100%).

**Why this exists:** Language is inherently ambiguous and creative — for the sentence "The weather today is...", many different next words ("sunny", "hot", "pleasant", "cloudy") are all reasonable. There is no single "correct" answer the way there is for `2 + 2`. So instead of forcing one fixed rule, the model is trained to estimate *how likely* each possible continuation is, based on patterns learned from enormous amounts of text.

**Key Terminology:**

| Term | Simple Meaning |
|---|---|
| **Token** | A chunk of text the model reads/writes at a time — often a whole word, sometimes part of a word. |
| **Logit** | A raw, unprocessed "score" the model calculates for each possible next token — higher logit = model prefers that token more, but logits are not yet valid probabilities (they don't sum to 1 and can be negative). |
| **Softmax** | The mathematical function that converts a list of logits into a valid probability distribution (all values between 0–1, summing to exactly 1). |
| **Sampling** | The process of actually picking one token from the probability distribution to output — this is where the "randomness" of an LLM's behaviour comes from. |

**A simplified illustration** — logits (raw scores) the model calculated for the next word after "The capital of India is":

```
Delhi     : logit = 2.0
Mumbai    : logit = 1.0
Chennai   : logit = 0.5
```

These raw logits are not yet probabilities — "Delhi" having a logit of 2.0 doesn't mean "200%". They need to be converted using **softmax**, which we do fully in the next section.

---

### 3.2 Temperature — Low Picks the Most Likely Token, High Introduces Variation

**Definition:** **Temperature** is a number (usually between 0 and 2) that controls how "sharp" or "flat" the model's probability distribution becomes before a token is sampled. **Low temperature** makes the model strongly favour its top-choice token (more predictable, more repeatable). **High temperature** flattens the distribution, giving lower-ranked tokens a bigger chance of being picked (more varied, more creative — but also more prone to unexpected or lower-quality output).

**The Formula (Softmax with Temperature):**

```
P(token_i) = exp(logit_i / T) / [ sum of exp(logit_j / T) for every token j in the vocabulary ]
```

Explaining every symbol:
- `logit_i` — the raw score for one specific candidate token (explained above).
- `T` — the **temperature** value we choose. T = 1 is "neutral" (no reshaping). T < 1 sharpens the distribution. T > 1 flattens it.
- `exp(x)` — means "e raised to the power of x," where **e ≈ 2.71828** (a fixed mathematical constant, similar in spirit to π). You can compute this with any scientific calculator's `eˣ` button.
- The bottom part (the sum) makes sure all the final probabilities add up to exactly 1 (100%) — this step is called **normalising**.

**Worked Calculation — using our three candidate tokens (Delhi = 2.0, Mumbai = 1.0, Chennai = 0.5):**

**Case 1: T = 1 (neutral, no reshaping)**

```
exp(2.0/1) = exp(2.0) = 7.389
exp(1.0/1) = exp(1.0) = 2.718
exp(0.5/1) = exp(0.5) = 1.649
Sum = 7.389 + 2.718 + 1.649 = 11.756

P(Delhi)   = 7.389 / 11.756 = 0.629 → 62.9%
P(Mumbai)  = 2.718 / 11.756 = 0.231 → 23.1%
P(Chennai) = 1.649 / 11.756 = 0.140 → 14.0%
(Check: 62.9 + 23.1 + 14.0 = 100.0% ✓)
```

**Case 2: T = 0.5 (LOW temperature — dividing each logit by 0.5 is the same as multiplying it by 2)**

```
exp(2.0/0.5) = exp(4.0) = 54.598
exp(1.0/0.5) = exp(2.0) = 7.389
exp(0.5/0.5) = exp(1.0) = 2.718
Sum = 54.598 + 7.389 + 2.718 = 64.705

P(Delhi)   = 54.598 / 64.705 = 0.844 → 84.4%
P(Mumbai)  = 7.389 / 64.705  = 0.114 → 11.4%
P(Chennai) = 2.718 / 64.705  = 0.042 → 4.2%
(Check: 84.4 + 11.4 + 4.2 = 100.0% ✓)
```

Notice: at low temperature, "Delhi" jumped from 62.9% to **84.4%** — the model becomes much more confident and predictable, almost always choosing the top answer.

**Case 3: T = 2 (HIGH temperature)**

```
exp(2.0/2) = exp(1.0)  = 2.718
exp(1.0/2) = exp(0.5)  = 1.649
exp(0.5/2) = exp(0.25) = 1.284
Sum = 2.718 + 1.649 + 1.284 = 5.651

P(Delhi)   = 2.718 / 5.651 = 0.481 → 48.1%
P(Mumbai)  = 1.649 / 5.651 = 0.292 → 29.2%
P(Chennai) = 1.284 / 5.651 = 0.227 → 22.7%
(Check: 48.1 + 29.2 + 22.7 = 100.0% ✓)
```

Notice: at high temperature, "Delhi" dropped to only **48.1%** — nearly a coin flip against the other options — meaning the model becomes far more likely to pick a less-obvious word, producing more varied/creative (but less predictable) text.

```
Temperature effect on P(Delhi) — same 3 candidate words:

T = 0.5  ████████████████████████████████████████  84.4%  (sharp — very predictable)
T = 1.0  ████████████████████████████               62.9%  (neutral)
T = 2.0  ████████████████████                       48.1%  (flat — more random)
```

**Comparison Table — Low vs High Temperature**

| Aspect | Low Temperature (e.g., 0.2–0.5) | High Temperature (e.g., 1.2–2.0) |
|---|---|---|
| Distribution shape | Sharp/peaked | Flat/spread out |
| Behaviour | Predictable, near-deterministic | Varied, creative, sometimes surprising |
| Best for | Factual Q&A, code generation, data extraction, JSON output | Creative writing, brainstorming, marketing copy |
| Risk | Can feel repetitive/robotic | Can produce inconsistent or off-topic output |

**Best Practices:**

- For tasks needing consistency (extracting structured data, writing code, answering factual questions), set a **low temperature** (often close to 0).
- For creative or brainstorming tasks (generating multiple ad-copy ideas, story writing), a **higher temperature** is appropriate.
- Always test your chosen temperature by running the same prompt multiple times and checking whether the variation is acceptable for your use case — this is the practical, hands-on skill you'll apply from Unit 12 onward when calling the Anthropic API in Python.

**Common Beginner Mistakes:**

- Assuming temperature = 0 makes an LLM perfectly deterministic like a calculator — in practice it makes output *highly* consistent, but some model implementations may still show tiny variations.
- Setting temperature very high for tasks that need factual precision (e.g., generating exact GST calculations or medical dosage text) — this significantly increases the risk of hallucination-like errors.
- Confusing "temperature" with "the model's confidence in truth" — temperature only controls *how the model samples from its own distribution*; it does not make wrong information more or less true.

---

## 4. Real World Application

- **AI Chatbots/Copilots:** Customer-support bots are usually run at low-to-moderate temperature, so answers stay consistent and on-brand across many customers asking the same question.
- **Code-Generation Assistants:** Nearly always run at very low temperature — a single most-likely, syntactically correct suggestion is far more useful than a "creative" but broken one.
- **Marketing/Content Tools:** Deliberately run at higher temperature to generate multiple varied taglines or social-media captions for a brand to choose from.
- **Vernacular Translation Apps:** Usually low temperature, since a translation should be accurate and stable rather than "creative."
- **Exam/Quiz Generators for EdTech platforms:** Moderate temperature — enough variation to avoid generating the exact same question every time, but low enough to keep factual accuracy.

---

## 5. Worked Example

**Scenario:** You are building an AI-native application for an Indian bank that auto-generates a short SMS message confirming a successful UPI payment. You must decide the temperature setting.

**Reasoning:**
1. The task requires **factual accuracy** (correct amount, correct recipient name) — never invent numbers.
2. Some **natural language variation** is acceptable and even nice (e.g., "Payment successful!" vs. "Your payment has gone through") so messages don't feel robotically identical every time.
3. Given this, you would choose a **low-to-moderate temperature** (for example, around 0.3–0.5) — low enough that the model reliably inserts the exact correct amount and recipient (which, in a real system, should actually come from your own deterministic database — see Unit 1's "hybrid systems" idea — not be "guessed" by the LLM at all), but with a small amount of variation in the wrapping sentence for a more natural, less robotic tone.

This decision-making process — balancing consistency against natural variation, and knowing which facts must come from a deterministic source rather than the LLM's guess — is exactly the kind of judgment call you'll be trained to make throughout this program.

---

## 6. Key Takeaways

- An LLM calculates a **logit** (raw score) for every possible next token, then converts these into a valid **probability distribution** using the **softmax** function.
- **Softmax formula:** `P(token_i) = exp(logit_i / T) / sum(exp(logit_j / T))` — every logit is divided by temperature T before being exponentiated and normalised.
- **Low temperature (T < 1)** sharpens the distribution — the top token becomes even more dominant, producing predictable output.
- **High temperature (T > 1)** flattens the distribution — lower-ranked tokens get a real chance of being picked, producing varied/creative output.
- Choose low temperature for factual, structured, or code-related tasks; choose higher temperature for creative or brainstorming tasks.
- Temperature never changes what is *true* — it only changes *how the model samples* from its own existing probability estimates.
- **Interview tip:** Be ready to explain softmax-with-temperature with actual numbers, not just "low = same answer, high = random answer" — interviewers at AI-native companies value quantitative intuition.
- This topic is the mathematical foundation for a decision you will make in every real Anthropic API call from Unit 12 onward.

---

## 7. Reference Links

- [Anthropic Documentation — Messages API Parameters (temperature)](https://docs.claude.com/) — official documentation on configuring temperature for real API calls.
- [Google Machine Learning Crash Course — Softmax](https://developers.google.com/machine-learning/crash-course) — beginner explanation of softmax in classification/generation contexts.
- [GeeksforGeeks — Softmax Function](https://www.geeksforgeeks.org/) — supplementary worked examples.
