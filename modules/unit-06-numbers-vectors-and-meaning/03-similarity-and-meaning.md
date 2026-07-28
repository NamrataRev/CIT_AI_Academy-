# Unit 6 — Numbers, Vectors and Meaning
## Topic 3: Similarity and Meaning

*(Covers: Dot product as similarity · Embeddings · Why "king − man + woman ≈ queen" works · Cosine similarity)*

---

## 1. Learning Objectives

By the end of this topic, you will be able to:

1. **Explain** what an embedding is and why AI systems use them to represent meaning.
2. **Calculate** the dot product of two simple vectors by hand.
3. **Calculate** the cosine similarity between two vectors by hand and interpret what the resulting number means.
4. **Describe**, using a worked numeric example, why vector arithmetic on embeddings (like "king − man + woman") can approximate "queen".
5. **Differentiate** between the dot product and cosine similarity as two related but distinct ways of measuring similarity.

---

## 2. Overview

You now know that a vector is a list of numbers describing multiple properties of one thing, and that vectors close together in space represent similar things. This topic gives you the actual mathematical tools to measure "how close" two vectors are — the **dot product** and **cosine similarity** — and introduces **embeddings**, the special kind of vector AI models use to represent the *meaning* of words, sentences, images, and more.

This is one of the most important topics in the entire program, because embeddings and similarity scoring are the mathematical engine behind search, recommendations, and Retrieval-Augmented Generation (RAG) — the technique you'll build hands-on in Week 14, where an AI system finds the most *relevant* piece of information by comparing embedding vectors, not by matching exact keywords. Everything you learn here — by hand, with small numbers — is exactly what happens (at a much larger scale) inside a real production AI system. Understanding it by hand first means you'll never be confused by "the AI just knows what's similar" — you'll know precisely *how* it knows.

---

## 3. Description

### 3.1 The Dot Product — Vectors Pointing the Same Direction Score High

**Definition:** The **dot product** of two vectors is a single number calculated by multiplying each pair of matching components together, and then adding up all those products.

**Formula, explained symbol by symbol:**

For two vectors `A = [a1, a2, a3]` and `B = [b1, b2, b3]`:

```
A · B  =  (a1 × b1)  +  (a2 × b2)  +  (a3 × b3)
```

- `A · B` — read as "A dot B"; the **dot (·)** symbol is the standard notation for this operation (this is exactly where the name "dot product" comes from).
- `a1, a2, a3` — the individual components (numbers) of vector A, in order.
- `b1, b2, b3` — the individual components of vector B, in the *same* order/positions as A.
- The operation: multiply the 1st component of A by the 1st component of B, multiply the 2nd by the 2nd, multiply the 3rd by the 3rd, then **add all three results together**. The final answer is always a single scalar number (not a vector).

**Worked Calculation (by hand):**

Let's use two music-taste vectors (pop score, rock score), each rated 0–10:

```
A (Ananya) = [4, 3]
B (Kabir)  = [5, 2]
```

```
A · B = (4 × 5) + (3 × 2)
      = 20 + 6
      = 26
```

The dot product of Ananya and Kabir's taste vectors is **26**.

**How to interpret this number:** On its own, "26" doesn't mean much — the dot product's raw value is affected by how large the numbers in the vectors are, not just their direction. A person who rated everything out of 100 instead of out of 10 would get a much bigger dot product, even with an identical *taste pattern*. This is exactly why the dot product alone is an incomplete similarity measure — which is what leads us to cosine similarity next. But the core intuition holds: **when two vectors point in roughly the same direction (their large values line up with each other's large values), the dot product tends to be a bigger positive number.** When vectors point in very different directions, the dot product is smaller, or even negative.

---

### 3.2 Embeddings — Turning Words Into Vectors That Capture Meaning

**Definition:** An **embedding** is a vector (usually with tens or hundreds of components) that represents the *meaning* of a piece of data — most commonly a word, sentence, image, or document — such that things with *similar meaning* end up as vectors that are *close together* in space.

**Why this exists:** Computers cannot compare the *meaning* of two words like "mango" and "banana" directly — they can only compare numbers. An embedding solves this by placing every word at a specific point in a (very high-dimensional) numeric space, learned by an AI model from studying huge amounts of real text. During this learning process, the model notices that words like "mango" and "banana" tend to appear in similar contexts ("I ate a ___ for breakfast", "___ smoothie") far more often than, say, "mango" and "car" — and it gradually positions "mango" and "banana" close together in this space, while "car" ends up somewhere far away.

**A simplified toy embedding (for intuition only):** Real embeddings have hundreds of dimensions with no single human-readable meaning per dimension, but let's imagine a simplified 2-dimensional toy embedding space with dimensions **(is_fruit, is_vehicle)**, each scored 0–10:

```
mango = [9, 0]
banana = [9, 1]
car    = [0, 9]
```

Even in this toy example, you can see "mango" and "banana" sit close together (both near `[9, 0]`), while "car" sits far away — exactly the geometric pattern that real, much larger embeddings produce, just with far more nuanced, machine-learned dimensions instead of our simplified "is_fruit" label.

---

### 3.3 Why "King − Man + Woman ≈ Queen" Works

This famous example shows that embeddings don't just place similar words near each other — they also capture *relationships* between words as directions in space, which means you can do arithmetic on meaning itself.

**Simplified toy embedding (2 dimensions: royalty_score, gender_score; gender_score is positive for "male-associated" and negative for "female-associated" in this toy model, used purely for teaching the arithmetic — real embeddings do not use a single explicit gender axis):**

```
king  = [8, 5]
man   = [1, 5]
woman = [1, -5]
```

**Step-by-step vector arithmetic:**

Step 1 — Compute `king − man` (subtract matching components):
```
king − man = [8 − 1, 5 − 5] = [7, 0]
```
This result, `[7, 0]`, represents "the direction of pure royalty, with the male/female component cancelled out" — because both `king` and `man` had the same gender_score (5), subtracting removed that shared part, leaving only the "royalty" difference.

Step 2 — Add `woman` to that result:
```
[7, 0] + woman = [7 + 1, 0 + (−5)] = [8, −5]
```

**Result:** `king − man + woman = [8, −5]`

Now compare this to an actual `queen` embedding in our toy space:
```
queen = [8, −5]
```

They match exactly! In a real embedding space (with hundreds of dimensions, learned from billions of words of text, not designed by hand like our toy example), the result of `king − man + woman` doesn't land *exactly* on `queen` — but it lands *very close* to it, closer than to almost any other word — which is why this is written as an **approximation**: `king − man + woman ≈ queen` (the "≈" symbol means "approximately equal to").

**Why this works conceptually:** `king − man` isolates the "royalty" direction by cancelling out the shared "male" component. Adding `woman` then re-applies that royalty direction onto the "female" starting point — arriving at "royal + female", which is exactly the concept "queen".

---

### 3.4 Cosine Similarity — Measuring the Angle Between Two Meaning-Vectors

**Definition:** **Cosine similarity** measures how similar two vectors are by looking at the **angle** between them, ignoring their length/magnitude — giving a score between −1 and 1, where 1 means "pointing in exactly the same direction" (maximally similar), 0 means "unrelated / at a right angle", and −1 means "pointing in exactly opposite directions".

**Formula, explained symbol by symbol:**

```
cosine_similarity(A, B) = (A · B) / (|A| × |B|)
```

- `A · B` — the dot product of A and B (which you already calculated above).
- `|A|` — the **magnitude** (length) of vector A, calculated as the square root of the sum of its squared components: for `A = [a1, a2]`, `|A| = √(a1² + a2²)`.
- `|B|` — the magnitude of vector B, calculated the same way.
- Dividing the dot product by both magnitudes **cancels out the effect of vector length**, leaving a pure measure of *direction/angle* — this is exactly what fixes the limitation of the raw dot product we noted in section 3.1.

**Worked Calculation (by hand) — using clean numbers:**

```
A = [3, 4]
B = [6, 8]
```

Step 1 — Dot product:
```
A · B = (3 × 6) + (4 × 8) = 18 + 32 = 50
```

Step 2 — Magnitude of A:
```
|A| = √(3² + 4²) = √(9 + 16) = √25 = 5
```

Step 3 — Magnitude of B:
```
|B| = √(6² + 8²) = √(36 + 64) = √100 = 10
```

Step 4 — Cosine similarity:
```
cosine_similarity(A, B) = 50 / (5 × 10) = 50 / 50 = 1
```

**Interpretation:** A cosine similarity of **1** means A and B point in *exactly* the same direction (B is simply A scaled up — indeed, `B = 2 × A`). Even though A and B are different in magnitude (length), their *direction* — and therefore what they represent — is identical, which is exactly the property cosine similarity is designed to detect.

**A second worked example — perpendicular (unrelated) vectors:**

```
A = [3, 4]
C = [4, -3]
```

```
A · C = (3 × 4) + (4 × −3) = 12 − 12 = 0
|A| = 5   (from above)
|C| = √(4² + (−3)²) = √(16 + 9) = √25 = 5

cosine_similarity(A, C) = 0 / (5 × 5) = 0
```

**Interpretation:** A cosine similarity of **0** means the two vectors are entirely unrelated in direction (mathematically, "orthogonal" / at a 90° angle) — in a real embedding space, this would suggest the two words/sentences have no meaningful semantic relationship.

**Comparison Table — Dot Product vs Cosine Similarity**

| Aspect | Dot Product | Cosine Similarity |
|---|---|---|
| Affected by vector length/magnitude? | Yes | No — cancelled out by dividing |
| Range of possible values | Any real number (unbounded) | Always between −1 and 1 |
| What it measures | Combination of direction and magnitude | Pure direction/angle |
| Typical AI use | A building block/step in other calculations | The standard metric for comparing embeddings (search, RAG, recommendations) |

### Best Practices

- When comparing embeddings for search, recommendations, or RAG, **cosine similarity is the standard choice** precisely because it ignores magnitude, which can vary for reasons unrelated to meaning (e.g., sentence length).
- Always interpret similarity scores in context — "0.85 cosine similarity" is meaningfully high for sentence embeddings, but you should verify this empirically for your specific model/use case rather than assuming a fixed universal threshold.

### Common Beginner Mistakes

- Assuming a bigger dot product always means "more similar," without accounting for vector length — this is precisely why cosine similarity exists.
- Forgetting that cosine similarity is bounded between −1 and 1, and misreading a value like 0.3 as "30% similar" — it is not a percentage, it is a measure of the angle between vectors.
- Believing `king − man + woman = queen` works by looking up dictionary definitions — it works because of learned geometric relationships in a numeric embedding space, entirely different from how a human defines these words.

---

## 4. Real World Application

- **RAG-based document assistants (Week 14):** When you ask an AI assistant a question, the system converts your question into an embedding and computes cosine similarity against embeddings of thousands of document chunks, retrieving the most relevant ones.
- **E-commerce search:** Searching "warm winter jacket" returns products whose description embeddings are cosine-similar to your query embedding, even if the exact words don't match.
- **Vernacular AI Translation:** Embeddings allow a model to recognize that a Hindi sentence and its Tamil translation are semantically similar, even though they share no common words.
- **Music/video recommendation:** Cosine similarity between a user's taste vector and a song's feature vector powers "Recommended for you."
- **Fraud detection in banking:** Comparing a new transaction's vector to a customer's historical "normal behaviour" vector using similarity scoring to flag unusual activity.

---

## 5. Worked Example

**Scenario:** An e-commerce RAG assistant needs to find which of two stored product-description embeddings is more relevant to a customer's search query embedding.

```
Query           Q = [2, 2]
Product A desc  A = [4, 4]
Product B desc  B = [1, -1]
```

**Cosine similarity(Q, A):**
```
Q · A = (2×4) + (2×4) = 8 + 8 = 16
|Q| = √(2² + 2²) = √8 ≈ 2.83
|A| = √(4² + 4²) = √32 ≈ 5.66
cosine_similarity(Q, A) = 16 / (2.83 × 5.66) ≈ 16 / 16.02 ≈ 1.0
```

**Cosine similarity(Q, B):**
```
Q · B = (2×1) + (2×−1) = 2 − 2 = 0
|B| = √(1² + (−1)²) = √2 ≈ 1.41
cosine_similarity(Q, B) = 0 / (2.83 × 1.41) = 0
```

**Conclusion:** Product A (cosine similarity ≈ 1.0, pointing in the same direction as the query) is far more relevant than Product B (cosine similarity = 0, unrelated direction) — this is exactly the calculation a real RAG system performs, just across hundreds of dimensions and thousands of candidate documents instead of two.

---

## 6. Key Takeaways

- The **dot product** multiplies matching components of two vectors and adds the results — a bigger positive value suggests the vectors point in a similar direction, but the raw value is also affected by vector length.
- An **embedding** is a vector that represents meaning, learned so that semantically similar things end up close together in numeric space.
- Vector arithmetic on embeddings (`king − man + woman ≈ queen`) works because embeddings capture relationships as consistent directions in space, not just isolated points.
- **Cosine similarity** = dot product ÷ (magnitude of A × magnitude of B) — it measures pure direction/angle, ranges from −1 to 1, and is the standard metric for comparing embeddings.
- Cosine similarity of 1 = same direction (maximally similar); 0 = unrelated; −1 = opposite direction.
- This exact maths — embeddings + cosine similarity — powers search, recommendations, and RAG (Week 14).
- **Interview tip:** Be ready to compute a dot product and a cosine similarity by hand for two small 2D vectors — this is a very common conceptual-check interview question for AI-native roles.

---

## 7. Reference Links

- [Google Machine Learning Crash Course — Embeddings](https://developers.google.com/machine-learning/crash-course) — official beginner-friendly coverage of embeddings and similarity.
- [GeeksforGeeks — Cosine Similarity](https://www.geeksforgeeks.org/) — supplementary worked examples.
- [TensorFlow Embedding Projector](https://projector.tensorflow.org/) — visually explore real word embeddings and their similarity clusters (hands-on in Topic 4).
- [Anthropic Documentation](https://docs.claude.com/) — for context on how embeddings are used in retrieval-augmented Claude applications.
