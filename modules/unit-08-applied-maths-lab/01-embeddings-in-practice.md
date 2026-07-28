# Unit 8 — Applied Maths Lab
## Topic 1: Embeddings in Practice

*(Covers: Embedding explorer — comparing domain-specific word clusters in 2D · Similarity scoring — computing cosine similarity between sentence pairs)*

---

## 1. Learning Objectives

By the end of this topic, you will be able to:

1. **Explain** what it means to "explore" embeddings by plotting words or sentences as points in space.
2. **Identify** which words or sentences will cluster together based on their embedding vectors.
3. **Implement** (by hand, with pen and paper) the cosine similarity calculation between two toy sentence embeddings.
4. **Analyze** a set of similarity scores to decide which sentence pairs are "close in meaning" and which are not.
5. **Evaluate** why this hands-on calculation matters before you ever call a real embedding API in later units.

---

## 2. Overview

In **Week 6 (Numbers, Vectors and Meaning)**, you learned the *theory*: words and sentences can be turned into vectors (called **embeddings**), and **cosine similarity** measures how close two vectors point in the same direction — which, for embeddings, tells us how similar two pieces of text are in *meaning*.

This lab topic is where you stop reading about it and start **doing it with your own hands**. We will not use any real AI model or code here (that comes from Unit 11 onward) — instead, we use small, simplified "toy" embeddings with easy numbers, so you can compute everything on paper and truly understand what is happening. This muscle memory matters immensely: when you later use a real embedding model (with vectors of 768 or 1536 numbers, not just 2 or 3), you will *trust* the similarity score it gives you, because you will have already computed the exact same kind of calculation by hand, on a small scale, and seen it work correctly.

This is exactly what "Applied Maths for AI" means — not memorising formulas, but being able to sanity-check what an AI system is doing under the hood, which is core to your job as someone who specifies and verifies AI systems.

---

## 3. Description

### 3.1 Embedding Explorer — Comparing Domain-Specific Word Clusters in 2D

**Definition (recap):** An embedding is a list of numbers (a vector) assigned to a word or sentence, such that words with similar meanings get vectors that are numerically close to each other.

**Why this exercise exists:** It is much easier to *see* clustering than to imagine it. If we simplify embeddings down to just 2 numbers per word (instead of hundreds), we can plot them on a simple graph with an X-axis and a Y-axis, and literally see similar words group together.

**Worked Setup:** Suppose we assign the following simplified 2D toy embeddings to six words from two very different domains — **banking** and **food delivery**:

| Word | Domain | X | Y |
|---|---|---|---|
| loan | Banking | 1.0 | 1.0 |
| interest | Banking | 1.2 | 0.9 |
| EMI | Banking | 0.9 | 1.1 |
| pizza | Food | 5.0 | 5.0 |
| burger | Food | 5.2 | 4.8 |
| fries | Food | 4.9 | 5.1 |

**A Simple ASCII Plot:**

```
Y
6 |
5 |              burger  pizza
  |               fries
4 |
3 |
2 |
1 |  loan
  |  EMI interest
0 +-----------------------------  X
  0    1    2    3    4    5    6
```

Notice how the three banking words sit tightly clustered near the bottom-left corner (around X≈1, Y≈1), while the three food-delivery words sit tightly clustered near the top-right (around X≈5, Y≈5). **The distance between clusters represents the difference in meaning; the tightness within a cluster represents shared meaning.** This is exactly how a real embedding model (used in a RAG system, which you'll study in Unit 14) decides which stored documents are "about the same topic" as a user's question.

**Important Note:** In a real embedding model, each word or sentence is represented using hundreds or thousands of numbers, not 2 — we cannot draw that directly. Tools like the **TensorFlow Embedding Projector** (which you explored conceptually in Week 6) mathematically compress those hundreds of numbers down to 2 or 3 dimensions just so humans can visualise the clustering, using a technique that preserves *relative* closeness. The clustering idea is identical; only the number of dimensions changes.

---

### 3.2 Similarity Scoring — Computing Cosine Similarity Between Sentence Pairs

**Recap of the formula:**

$$\text{cosine similarity} = \frac{A \cdot B}{|A| \times |B|}$$

Where:
- **A · B** (dot product) = multiply matching positions of the two vectors and add up the results.
- **|A|** and **|B|** (magnitude) = the "length" of each vector, calculated as the square root of the sum of its squared values.
- The result always falls between **-1 and 1** for these kinds of embeddings — **1 means pointing in exactly the same direction (very similar meaning)**, **0 means unrelated**, and negative values mean opposite meaning (rare in practice for text embeddings, which are usually non-negative).

**Worked Setup:** Let's assign toy 3-dimensional embeddings to three short sentences from a food-delivery support chat:

| Sentence | Vector (3 numbers) |
|---|---|
| S1: "I want to order pizza" | (0.9, 0.1, 0.2) |
| S2: "I would like to order a burger" | (0.8, 0.2, 0.1) |
| S3: "The train is delayed today" | (0.1, 0.9, 0.8) |

**Step-by-step calculation — S1 vs S2 (both about ordering food):**

1. Dot product: `(0.9 × 0.8) + (0.1 × 0.2) + (0.2 × 0.1) = 0.72 + 0.02 + 0.02 = 0.76`
2. Magnitude of S1: `√(0.9² + 0.1² + 0.2²) = √(0.81 + 0.01 + 0.04) = √0.86 ≈ 0.927`
3. Magnitude of S2: `√(0.8² + 0.2² + 0.1²) = √(0.64 + 0.04 + 0.01) = √0.69 ≈ 0.831`
4. Cosine similarity: `0.76 ÷ (0.927 × 0.831) = 0.76 ÷ 0.770 ≈ 0.99`

**Result: ≈ 0.99 → extremely high similarity.** This makes sense — both sentences are about ordering food.

**Step-by-step calculation — S1 vs S3 (unrelated sentences):**

1. Dot product: `(0.9 × 0.1) + (0.1 × 0.9) + (0.2 × 0.8) = 0.09 + 0.09 + 0.16 = 0.34`
2. Magnitude of S1 (from above): `≈ 0.927`
3. Magnitude of S3: `√(0.1² + 0.9² + 0.8²) = √(0.01 + 0.81 + 0.64) = √1.46 ≈ 1.208`
4. Cosine similarity: `0.34 ÷ (0.927 × 1.208) = 0.34 ÷ 1.120 ≈ 0.30`

**Result: ≈ 0.30 → low similarity.** This also makes sense — a sentence about a food order and a sentence about a delayed train have almost nothing to do with each other.

**Rules to remember:**

1. Always compute the dot product first, then the two magnitudes, then divide.
2. Round to 2 decimal places for interpretation — you rarely need more precision by hand.
3. A cosine similarity above ~0.8 is generally considered "closely related" for text embeddings; below ~0.4 is generally "unrelated" — but the exact threshold always depends on the specific embedding model and task, and should be tuned using real evaluation data (a skill you'll practice in Topic 4 of this unit).

**Common Beginner Mistakes:**

- Forgetting to divide by the magnitudes and reporting the dot product alone as "similarity" — the dot product alone is affected by vector length, not just direction, so it can mislead you.
- Assuming a negative cosine similarity is common in text embeddings — in practice, most modern text embedding models produce vectors where similarity scores stay between 0 and 1.
- Mixing up rows when multiplying vector positions — always multiply position 1 with position 1, position 2 with position 2, and so on, never cross them.

---

## 4. Real World Application

- **RAG-based document assistants (Unit 14 preview):** When you ask a RAG chatbot a question, the system converts your question into an embedding and compares it — using this exact cosine similarity calculation — against the embeddings of thousands of stored document chunks, to retrieve the most relevant ones.
- **E-commerce search (Flipkart/Amazon-style):** Searching "sneakers for running" returns "running shoes" products because their description embeddings are close in cosine similarity, even though the exact words differ.
- **Banking fraud detection:** A transaction's "behaviour vector" (numbers describing amount, location, time, merchant type) can be compared to a customer's normal spending pattern vector — a low similarity score can flag a transaction as unusual.
- **Vernacular AI translation:** Sentence embeddings help systems detect when two sentences in different Indian languages (e.g., Hindi and Tamil) express the same meaning, which is used to check translation quality.
- **Education platforms:** Matching a student's doubt (typed in their own words) to the closest pre-written answer in a knowledge base, using sentence-embedding similarity.

---

## 5. Worked Example

**Scenario:** A college helpdesk chatbot has three stored FAQ answers, each represented as a toy 2D embedding. A student asks a question, also converted to a 2D embedding. Find which FAQ answer is the best match.

| Text | Vector |
|---|---|
| Student question: "How do I reset my student portal password?" | (0.85, 0.15) |
| FAQ 1: "Steps to reset your college portal login password" | (0.80, 0.20) |
| FAQ 2: "Hostel mess timings for this semester" | (0.10, 0.90) |
| FAQ 3: "How to apply for a bonafide certificate" | (0.40, 0.60) |

**Calculation for Student Question vs FAQ 1:**

- Dot product: `(0.85 × 0.80) + (0.15 × 0.20) = 0.68 + 0.03 = 0.71`
- Magnitude of question: `√(0.85² + 0.15²) = √(0.7225 + 0.0225) = √0.745 ≈ 0.863`
- Magnitude of FAQ 1: `√(0.80² + 0.20²) = √(0.64 + 0.04) = √0.68 ≈ 0.825`
- Cosine similarity: `0.71 ÷ (0.863 × 0.825) = 0.71 ÷ 0.712 ≈ 1.00`

**Calculation for Student Question vs FAQ 2:**

- Dot product: `(0.85 × 0.10) + (0.15 × 0.90) = 0.085 + 0.135 = 0.22`
- Magnitude of FAQ 2: `√(0.10² + 0.90²) = √(0.01 + 0.81) = √0.82 ≈ 0.906`
- Cosine similarity: `0.22 ÷ (0.863 × 0.906) = 0.22 ÷ 0.782 ≈ 0.28`

**Conclusion:** FAQ 1 (similarity ≈ 1.00) is overwhelmingly the best match to the student's question, while FAQ 2 (similarity ≈ 0.28) is almost unrelated. A RAG-style helpdesk system would retrieve and show FAQ 1 to the student. (Try computing Student Question vs FAQ 3 yourself, using the same three steps, to check your understanding — you should get a similarity somewhere between the two results above.)

---

## 6. Key Takeaways

- Plotting toy 2D embeddings makes "clustering" visible — words/sentences with similar meaning sit close together in the space.
- Cosine similarity = dot product ÷ (magnitude of A × magnitude of B) — always compute in that order.
- A similarity near 1 = very similar meaning; near 0 = unrelated.
- Real embedding models use hundreds/thousands of dimensions; tools like the TensorFlow Embedding Projector compress them to 2–3D just for human visualisation — the underlying maths is identical to what you did here by hand.
- This calculation is the mathematical engine behind RAG retrieval, search relevance, and recommendation systems.
- **Interview tip:** Being able to explain and hand-compute cosine similarity is one of the most common "prove you understand embeddings" questions for entry-level AI roles.
- Always double-check your arithmetic by re-verifying the dot product and both magnitudes separately before dividing.

---

## 7. Reference Links

- [Google Machine Learning Crash Course — Embeddings](https://developers.google.com/machine-learning/crash-course/embeddings) — official beginner-friendly explanation with interactive visuals.
- [TensorFlow Embedding Projector](https://projector.tensorflow.org/) — explore real high-dimensional embeddings compressed to 2D/3D.
- [GeeksforGeeks — Cosine Similarity](https://www.geeksforgeeks.org/) — supplementary worked examples for practice.
