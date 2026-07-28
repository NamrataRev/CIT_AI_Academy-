# Unit 1 — How Machines Think
## Topic 5: Applying It to Your Domain

*(Covers: Choosing your domain — writing a 3-sentence problem statement)*

---

## 1. Learning Objectives

By the end of this topic, you will be able to:

1. **Identify** a real-world domain (an area of interest, such as healthcare, education, or transport) that you would like to build AI-powered solutions for.
2. **Apply** decomposition, abstraction, and algorithmic thinking (Topics 1–4) to a real problem within your chosen domain.
3. **Create** a clear, 3-sentence problem statement that defines a specific problem worth solving.
4. **Evaluate** whether a problem statement is specific enough to be useful, or too vague to act on.
5. **Describe** why choosing a well-scoped problem early makes every later step of the AI-Native Engineering workflow easier.

---

## 2. Overview

You've now learned the core building blocks of computational thinking: decomposition (Topic 2), abstraction (Topic 2), expressing logic through pseudocode and flowcharts (Topic 3), and algorithmic thinking with its four defining properties (Topic 4). This final topic of Unit 1 asks you to put all of it together and apply it to something personal: **a domain you care about.**

Throughout this 15-week program, you will build toward a **Capstone project** (Week 15) — a complete, working AI-powered system that you design, specify, build, and evaluate yourself. That capstone has to start somewhere, and it starts here: by choosing a domain (an area like healthcare, agriculture, banking, education, or transport) and writing a clear, focused **problem statement** — a short, precise description of the real problem you want to solve.

Why does this matter so early in the program, before you've even touched Python or AI tools? Because a vague starting point ("I want to build something with AI in healthcare") leads to vague specifications later, which leads to AI systems that don't actually solve anything useful. A precise problem statement, written using the discipline you've just learned (decomposition, abstraction, algorithmic clarity), sets you up to succeed at every later stage — writing specifications (Week 2), evaluating AI output (Week 3–4), and eventually building your capstone (Week 15).

---

## 3. Description

### 3.1 Choosing Your Domain

**Definition:** A domain is a specific area or industry where a problem exists and a solution would create real value — for example, healthcare, banking/FinTech, education, agriculture, transport, or e-commerce.

**Why this matters:** AI-Native Engineers do not build "AI in general" — they build AI-powered solutions *for a specific problem, in a specific context, for specific users*. Choosing a domain early gives your learning purpose and direction: every new concept in this program (specifications, evaluation metrics, RAG, agents) becomes easier to understand when you can immediately picture how it would apply to a problem you actually care about.

**How to choose a good domain:**

1. Pick something you have some personal familiarity with or curiosity about (your own experience as a student, a family member's business, a local community issue).
2. Prefer domains with real, observable problems — not abstract or purely hypothetical ones.
3. It's fine (and expected) to explore areas like: student life & education, banking/UPI/FinTech, healthcare, agriculture, railway/transport booking, e-commerce/food delivery, or vernacular/regional-language AI applications.

### 3.2 Writing a 3-Sentence Problem Statement

**Definition:** A problem statement is a short, precise description of a real problem, written so clearly that anyone reading it understands exactly what issue needs solving, for whom, and why it matters — without yet describing *how* it will be solved.

**Why this concept exists:** Beginners often jump straight to a "solution" idea ("I'll build a chatbot!") without ever clearly stating the *problem* that solution is meant to solve. This backwards approach usually produces unfocused, unhelpful systems. Writing the problem statement first — and forcing it into just three sentences — makes you decompose your idea (Topic 2) down to its essential core before you get distracted by implementation details.

**The 3-Sentence Structure:**

| Sentence | What It Should Cover |
|---|---|
| **Sentence 1** | Who faces this problem, and what specifically goes wrong or is difficult for them today? |
| **Sentence 2** | Why does this problem matter — what is the cost or consequence of leaving it unsolved? |
| **Sentence 3** | What would meaningfully "solving" this problem look like, in plain terms (without yet describing the technical solution)? |

**Example — A Weak (Vague) Problem Statement:**

> "Students have trouble with their studies. AI can help them learn better. We should build something for this."

This fails the algorithmic-thinking test from Topic 4 — it isn't **definite**. Which students? What specific difficulty? "Help them learn better" could mean a thousand different things.

**Example — A Strong (Specific) Problem Statement:**

> "First-year engineering students in Tier-2 and Tier-3 Indian colleges often struggle to get quick, understandable answers to basic doubts outside class hours, since teaching assistants are not always available. This leads many students to either fall behind silently or rely on unreliable, unverified answers from random online forums. A good solution would let a student ask a doubt in their own words, at any time, and receive an accurate, syllabus-aligned explanation they can actually understand."

Notice how this version applies everything from this unit:
- **Decomposition (Topic 2):** it narrows "students" down to a specific group (first-year engineering students, Tier-2/3 colleges) and a specific difficulty (doubt-clearing outside class hours).
- **Definite language (Topic 4):** no vague words like "better" or "help" without explanation — it explains exactly what's hard and why.
- **Input/Output framing (Topic 1):** it implies a clear input (a student's doubt) and a clear desired output (an accurate, understandable explanation).

**Rules for a good problem statement:**

1. Name a **specific** group of people (not "everyone" or "students" in general).
2. Describe a **specific**, observable difficulty — not a general dissatisfaction.
3. Avoid naming your intended solution or technology in the problem statement itself (no "using AI, we will build a chatbot that…") — that comes later, in your specification (Week 2).
4. Keep it to exactly three sentences — this constraint forces clarity and prevents rambling.

**Best Practices:**

- Test your problem statement against the four algorithm properties from Topic 4: is it **definite** enough that two different people would understand the exact same problem after reading it?
- Talk to someone who actually experiences this problem (a fellow student, a family member, a shopkeeper) before finalising your statement — real problems are rarely obvious from the outside.
- Keep a notebook (physical or digital) of 3–4 candidate problem statements across different domains before picking your favourite — this is exactly the kind of decision you'll want to revisit once you've learned more about what AI can (and cannot) reliably do, in Week 3.

**Common Beginner Mistakes:**

- Writing a "solution statement" instead of a "problem statement" (jumping straight to "I will build an AI chatbot" without ever stating the actual problem).
- Choosing a domain so broad ("healthcare") that a real, specific problem never gets identified.
- Describing a problem no one actually experiences — always ground your problem statement in something real and observable.

---

## 4. Real World Application

- **Education:** "First-year students struggle to get doubt-clearing support outside class hours" is a real, addressable problem behind many ed-tech AI tutoring products used across Indian colleges today.
- **Agriculture:** "Small farmers in rural India often lack timely, local-language advice on crop disease and pest control" is the real problem statement behind several government and startup AI advisory systems.
- **Healthcare:** "Patients in rural clinics often wait a long time for a doctor to review basic scan results" is the type of problem statement that has led to AI-assisted triage tools (which you'll examine critically in Week 9's Judgment Framework, since healthcare decisions require careful human oversight).
- **Banking/FinTech:** "First-time UPI users often cannot tell whether a payment failure was due to their own mistake or a technical issue" is a specific, real problem — much stronger than a vague statement like "banking apps should be smarter."
- **Vernacular AI:** "Many farmers and small business owners are more comfortable describing problems in their regional language than in English or Hindi" is the real problem statement behind vernacular translation and voice-based AI assistants used across India.

---

## 5. Worked Example

**Scenario:** Apply the full unit's thinking (decomposition, abstraction, algorithmic properties) to draft your own 3-sentence problem statement in the domain of **railway travel**.

**Step 1 — Start broad (too vague to act on):**
> "Train travel in India can be improved with AI."

This fails immediately — it isn't decomposed, and it isn't definite (Topic 4).

**Step 2 — Decompose "train travel" into specific sub-areas** (Topic 2): ticket booking, platform information, delays/schedule updates, luggage safety, seat comfort, food quality.

**Step 3 — Pick one specific, real sub-problem:** "Passengers on waitlisted tickets often don't know their real chances of confirmation and check repeatedly out of anxiety."

**Step 4 — Write the final 3-sentence problem statement:**

> "Passengers with waitlisted railway tickets often have no clear sense of whether their ticket will be confirmed, so they repeatedly refresh the IRCTC app or website out of anxiety in the days before travel. This uncertainty causes unnecessary stress and makes it hard for passengers to plan backup travel options in time. A good solution would give waitlisted passengers a clear, realistic, and regularly updated sense of their confirmation chances well before the journey date."

**Step 5 — Verify against the four algorithm properties (Topic 4):**

| Property | Applied to this problem statement |
|---|---|
| Finite | The problem is scoped to a specific window (before the journey date) — not open-ended. |
| Definite | Names a specific group (waitlisted passengers) and a specific difficulty (no clear confirmation-chance visibility). |
| Input | The passenger's ticket status and history are the implied "input" the eventual solution would need. |
| Output | A "realistic, updated confirmation chance" is the implied, clear output the solution must produce. |

This problem statement is now specific and clear enough to carry forward into Week 2, where you'll learn to turn it into a full, testable AI specification.

---

## 6. Key Takeaways

- Choose a **domain** you have some familiarity with or curiosity about — healthcare, education, banking, agriculture, transport, and e-commerce are all rich sources of real problems.
- A good **problem statement** describes the problem, not the solution — never mention your intended technology in it.
- Use exactly **3 sentences**: (1) who + what's difficult, (2) why it matters, (3) what "solved" would look like.
- Apply the discipline from this whole unit — decomposition to narrow the problem, definite language to avoid vagueness, and the four algorithm properties as a sanity check.
- A vague problem statement guarantees a vague (and often useless) AI solution later — precision here saves enormous effort down the line.
- Ground your problem in something real — ideally something you've observed or experienced directly, not a guess.
- This problem statement is the seed of your **Week 15 Capstone project** — the more precise it is now, the smoother every later week (specification, building, evaluation) will be.
- **Interview tip:** Being able to clearly articulate "the problem, not just the solution" is one of the most valued skills interviewers look for in junior AI/software engineers.

---

## 7. Reference Links

- [Google Machine Learning Crash Course — Framing an ML Problem](https://developers.google.com/machine-learning/crash-course) — guidance on clearly defining a problem before choosing a technical approach.
- [GeeksforGeeks — Problem Solving Techniques](https://www.geeksforgeeks.org/) — supplementary reading on structured problem definition.
- [TutorialsPoint — Computational Thinking](https://www.tutorialspoint.com/) — reinforces decomposition and abstraction as applied to real problem selection.
