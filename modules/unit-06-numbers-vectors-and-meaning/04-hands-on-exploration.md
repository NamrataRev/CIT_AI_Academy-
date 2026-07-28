# Unit 6 — Numbers, Vectors and Meaning
## Topic 4: Hands-on Exploration

*(Covers: Using the TensorFlow Embedding Projector to explore word clusters)*

---

## 1. Learning Objectives

By the end of this topic, you will be able to:

1. **Describe** what the TensorFlow Embedding Projector is and what it visualizes.
2. **Navigate** the Embedding Projector tool to search for a word and inspect its nearest neighbours.
3. **Identify** clusters of semantically related words by observing their positions in the visualization.
4. **Analyze** why certain words appear close together and others appear far apart, connecting the visual result back to the maths (embeddings, cosine similarity) from Topic 3.
5. **Evaluate** the limitations of a 2D/3D visualization of a high-dimensional embedding space.

---

## 2. Overview

You've just spent Topic 3 learning, by hand, exactly how embeddings and cosine similarity work. Now it's time to *see* real embeddings — not toy 2-number examples, but actual high-dimensional word embeddings, learned by a real model from real text — using a free, official visualization tool built by Google's TensorFlow team: the **Embedding Projector**.

This is a "Practice" activity in our Learn → Understand → Practice → Apply progression: no coding is required (you haven't learned Python yet — that begins in Unit 11), just careful, guided observation inside your web browser. The goal is to build strong visual intuition for something you can currently only picture in your head — hundreds of words, positioned in space, clustering by meaning — so that when you learn RAG and search in Week 14, the underlying picture is already familiar and concrete, not abstract.

---

## 3. Description

### What Is the Embedding Projector?

The **TensorFlow Embedding Projector** (available for free at **projector.tensorflow.org**) is an official, browser-based visualization tool. It takes real word embeddings (vectors with hundreds of dimensions, exactly like the "mango"/"banana" example from Topic 3, but learned from enormous amounts of real text) and **compresses** them down to just 2 or 3 dimensions you can actually see on screen, using a mathematical compression technique (you do not need to know how this compression works internally for this activity — just that it preserves *relative* closeness as faithfully as possible).

### Key Terminology

| Term | Simple Meaning |
|---|---|
| **Projector** | The tool itself — projects (compresses) high-dimensional data down to a viewable 2D/3D space. |
| **Nearest neighbours** | The words whose embeddings are closest (most similar, by cosine similarity) to a chosen word. |
| **Cluster** | A visible group of points/words sitting close together, suggesting they share related meaning. |

### Guided Activity — Step by Step

Follow these steps in your browser. No installation, login, or coding is required.

1. **Open** [projector.tensorflow.org](https://projector.tensorflow.org/) in your browser.
2. By default, the tool loads a dataset of **word2vec** word embeddings (a well-known, real embedding model). You'll see a large 3D "cloud" of points — each point is one word's embedding, compressed for viewing.
3. On the right-hand panel, find the **search box**. Type in a word you're curious about — try **"mango"** first.
4. Click the word when it appears. The view will zoom to that point, and the right panel will show a ranked list of that word's **nearest neighbours** — the words with embeddings most similar (closest by cosine similarity) to "mango."
5. **Record what you observe:** What words appear as mango's nearest neighbours? (You should expect to see other fruit names ranking highly.)
6. Now search for a completely unrelated word, such as **"bicycle"**, and again note its nearest neighbours. Compare: does "bicycle" cluster anywhere near "mango"? It should not.
7. Try a word with more than one common meaning, such as **"bank"** (a riverbank vs. a financial bank). Observe its neighbours — do you see a mix of finance-related and geography-related words nearby? This is a useful, real limitation of basic word embeddings worth noting (a single word gets only one embedding, blending all its senses together — a nuance addressed by more advanced models, briefly previewed in Unit 3's discussion of LLMs).
8. Try searching for **"king"**, **"man"**, **"woman"**, and **"queen"** individually, and visually compare their relative positions. While the projector's 2D/3D compression won't let you verify the exact arithmetic from Topic 3 by eye, you should notice these four words sitting in a related region of the space.
9. Use the **"Isolate points"** feature (if visible) to isolate your searched word's nearest neighbours and see just that cluster on its own.

### Questions to Answer While Exploring

- Which words clustered tightly around "mango"? Were they what you expected?
- Was there any surprising or confusing neighbour in any of your searches? What might explain it?
- For the word "bank" — could this ambiguity cause a real AI system (e.g., a customer-support chatbot) to make a mistake? How?

### Best Practices

- Always test a *few* different words — one example alone can be misleading; patterns become clear only once you've compared several searches.
- When you notice something unexpected (e.g., an unrelated word appearing as a "close" neighbour), don't dismiss it — this is exactly the kind of observation that matters when you evaluate a real AI system for reliability later in this program (Unit 7–8).

### Important Notes

- **The visualization is a compression, not the real thing.** The actual embedding might have 100+ dimensions; the picture you see has been squeezed into 2 or 3. Two words can look reasonably close in the picture but be less similar than they appear (or vice versa) — treat the visualization as a helpful *intuition tool*, not a mathematically exact reading. This is why, in real systems, we always trust the actual computed cosine similarity number (Topic 3) over a visual impression.
- This tool uses a general-purpose embedding model trained on generic text, not Claude's internal representations — it is used here purely to build visual intuition about how *any* embedding space behaves.

---

## 4. Real World Application

- **RAG system debugging (Week 14):** Engineers use embedding visualizations exactly like this to sanity-check whether their document chunks are clustering sensibly before wiring up a retrieval pipeline.
- **Search relevance tuning (E-commerce):** Teams visualize product-description embeddings to verify that "running shoes" and "sports shoes" cluster together, while "running shoes" and "washing machine" do not.
- **Bias auditing (AI Ethics, Unit 5):** Researchers visualize embeddings to check whether certain words (e.g., job titles) are clustering in ways that reveal unwanted bias picked up from training data — a real, well-documented AI-safety concern.
- **Vernacular translation quality checks:** Visualizing cross-lingual embeddings can reveal whether a Hindi word and its intended Tamil translation land in the same conceptual cluster.

---

## 5. Worked Example

**Scenario walkthrough:** A learner searches for the word **"rupee"** in the Embedding Projector.

**Expected observation:** Nearest neighbours likely include other currency-related words — "dollar," "currency," "money," "price" — because word2vec learned these words appear in similar contexts across huge volumes of real text (e.g., news articles discussing prices and exchange rates).

**Connecting back to the maths:** Each of these words has its own high-dimensional embedding vector. The reason "rupee" and "dollar" cluster together is that their vectors have a **high cosine similarity** (close to 1) — precisely the calculation you performed by hand in Topic 3, just now happening automatically across hundreds of dimensions, for every pair of words in the entire vocabulary, so the tool can rank and display the closest ones.

**Reflection:** This single exploration ties together the whole unit: numbers (Topic 1) → organized as vectors (Topic 2) → compared using cosine similarity (Topic 3) → visualized as real, observable clusters (Topic 4). This is exactly the mental model you'll rely on throughout the rest of this program.

---

## 6. Key Takeaways

- The **TensorFlow Embedding Projector** (projector.tensorflow.org) is a free, official tool for visualizing real high-dimensional word embeddings, compressed down to 2D/3D.
- Searching a word shows its **nearest neighbours** — the words with the most similar embeddings (highest cosine similarity).
- Semantically related words form visible **clusters**; unrelated words sit far apart.
- Ambiguous words (like "bank") reveal a real limitation: one embedding may blend multiple meanings.
- The visualization is a *compressed approximation* — always trust the actual computed similarity score over visual impression alone.
- This hands-on exploration is the visual counterpart to the hand-calculated maths in Topic 3 — the same underlying principle (closeness = similarity) at real-world scale.
- **Interview tip:** Being able to explain *why* two words cluster together (in terms of cosine similarity of their embeddings) is a strong, concrete way to demonstrate you understand embeddings beyond buzzwords.

---

## 7. Reference Links

- [TensorFlow Embedding Projector](https://projector.tensorflow.org/) — the official tool used in this activity.
- [TensorFlow Documentation — Word Embeddings](https://www.tensorflow.org/text/guide/word_embeddings) — official background reading on how embeddings are learned.
- [Google Machine Learning Crash Course — Embeddings](https://developers.google.com/machine-learning/crash-course) — supplementary conceptual grounding.
