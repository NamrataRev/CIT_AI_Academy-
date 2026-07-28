# Unit 15 — Capstone Build Sprint and Showcase
## Topic 3: Showcase and Portfolio

*(Covers: Presenting: Problem → Spec → Live Demo → Eval Results → Judgment Framework → Cost → 3 Learnings · Submitting the GitHub portfolio — notebooks, specs, eval harness, AI Decision Journal, reflection)*

---

## 1. Learning Objectives

By the end of this topic, you will be able to:

1. **Create** a structured capstone presentation following the Problem → Spec → Live Demo → Eval Results → Judgment Framework → Cost → 3 Learnings format.
2. **Describe** each section of the presentation clearly enough for a non-technical audience to follow.
3. **Organize** a professional GitHub portfolio repository containing all capstone artefacts.
4. **Create** an "AI Decision Journal" documenting key decisions made while building the capstone.
5. **Evaluate** your own capstone honestly through a written reflection, identifying what you'd improve.

---

## 2. Overview

You have built SahayakBot (Topic 1) and rigorously tested, judged, cost-estimated, and red-teamed it (Topic 2). The final step — and the one that matters most for your **portfolio and interviews** — is presenting this work clearly and packaging it professionally on GitHub.

This is not a formality. In the real AI-native software industry, being able to explain *what you built, why you built it that way, how you know it works, and where a human still needs to be in the loop* is exactly what separates an entry-level AI-native engineer who merely "prompted something" from one who **understood and can defend** their system. This topic gives you the exact structure to do that, for your capstone and for every future project you build in your career.

---

## 3. Description

### 3.1 Presenting: Problem → Spec → Live Demo → Eval Results → Judgment Framework → Cost → 3 Learnings

**Definition:** This is a fixed 7-part presentation structure designed to walk any audience — technical or non-technical — through your capstone in a logical order: **why it exists → what you promised it would do → proof it works, live → evidence it meets the bar → where humans stay in control → what it costs → what you personally learned.**

**SahayakBot — Filled-In Presentation Outline:**

| Section | What to Say (SahayakBot example) | Time (suggested) |
|---|---|---|
| **1. Problem** | "TazaEats support agents spend 5-10 minutes answering the same 3 repetitive questions during peak hours, causing long waits — especially for Hindi-speaking customers." | 1 min |
| **2. Spec** | "SahayakBot answers order status, refund policy, and delivery delay questions in English or Hindi, using a deterministic order database for facts and Claude for phrasing and classification. It escalates anything uncertain to a human." (Show the 1-page spec table from Topic 1.) | 1–2 min |
| **3. Live Demo** | Actually run 2-3 live requests in front of the audience: a normal English query, a Hindi query, and one edge case (e.g., unknown order ID) that correctly escalates. | 2–3 min |
| **4. Eval Results** | Show the 5-case evaluation table from Topic 2 — all cases passing, tested across multiple runs. | 1–2 min |
| **5. Judgment Framework** | Show the per-component table from Topic 2 — explain clearly *why* `escalate_to_human` is the mandatory human-override point, and that order-status facts are never AI-guessed. | 2 min |
| **6. Cost** | Show the cost/latency table from Topic 2 — state the trade-off decision made and the trigger point for revisiting the architecture. | 1 min |
| **7. 3 Learnings** | Personal, honest reflection — see 3.2 below for how to write these. | 1–2 min |

> **Tip:** Rehearse the **Live Demo** section more than any other — a live failure in front of an audience is fine *if* your failure-handling code (Topic 2, section 3.5) degrades gracefully. That, itself, becomes a great live demonstration of professional engineering discipline.

**3 Learnings — example (write your own, honestly, based on your actual build):**

1. "I learned that separating deterministic facts from AI-generated phrasing early saved me from a whole category of bugs later — I initially let the AI 'see' the whole database and had to redesign this."
2. "I learned that red-teaming my own prompt-injection weakness (Topic 2, case #1) was uncomfortable but essential — I would not have found it just by testing 'normal' inputs."
3. "I learned that writing the Judgment Framework table forced me to admit where my system was genuinely risky, rather than assuming 'the AI is probably fine.'"

---

### 3.2 Submitting the GitHub Portfolio

**Definition:** Your **GitHub portfolio** is the permanent, professional record of your capstone — the artefact a recruiter, mentor, or future employer will actually look at. It must be organized clearly enough that a stranger can understand your project without you standing next to them explaining it (Unit 13: folder structure and README discipline).

**Recommended Repository Structure:**

```
sahayakbot-capstone/
├── README.md                     <- Problem, spec summary, how to run it, screenshots
├── .gitignore                    <- Excludes API keys, .env files, __pycache__
├── notebooks/
│   └── sahayakbot_demo.ipynb     <- The Colab notebook with the working code
├── specs/
│   └── 1-page-specification.md   <- The Topic 1 specification table
├── eval/
│   └── evaluation_harness.md     <- The 5-case table + judgment framework table
├── ai_decision_journal.md        <- See below
└── reflection.md                 <- Your honest, personal reflection
```

**The AI Decision Journal** is a running log of the *meaningful decisions* you made while building the capstone — not a diary of every prompt you tried, but the decisions that mattered:

```markdown
# AI Decision Journal — SahayakBot

## Decision 1: Deterministic order lookup, not AI-guessed
Date: [date]
Why: Unit 1 taught that facts a database already knows should never be
left to a probabilistic model to guess. Implemented get_order_status()
as a plain Python dictionary lookup, fed as context into the prompt.

## Decision 2: Escalate on any rupee amount mentioned above ₹500
Date: [date]
Why: Discovered during red-teaming (Topic 2, case #2) that a fabricated-
authority attack could otherwise go unescalated. Added explicit constraint.

## Decision 3: [Your own real decision from your own capstone build]
```

**Best Practices:**

- Write the README **last**, after the system works — it should describe the finished system accurately, including known limitations.
- Never commit a real API key — double-check `.gitignore` is correctly excluding `.env` or any credentials file (Unit 13).
- Use clear, meaningful commit messages throughout the build (Unit 13: commit discipline) — your commit history itself becomes part of your portfolio story.
- Keep the reflection honest — an interviewer trusts "here's what I'd do differently" far more than a claim of "it's perfect."

**Common Mistakes:**

- Submitting only code with no README — reviewers should never have to guess what your project does.
- Writing an AI Decision Journal that's just a prompt log, instead of a record of *engineering decisions and their reasoning*.
- Skipping the reflection section, or writing something generic ("I learned a lot") instead of specific, defensible learnings tied to real moments in the build (as in 3.1's example).

---

## 4. Real World Application

- **Job interviews:** Being able to walk an interviewer through Problem → Spec → Demo → Eval → Judgment → Cost → Learnings is functionally a rehearsal for real technical interviews and project retrospectives at any AI-native engineering job.
- **Freelance / client work:** Clients commissioning AI features expect exactly this kind of documented handover — a specification, evidence it works, and a clear note on where humans must stay involved.
- **Open-source contribution:** A clean GitHub repo with a Decision Journal is exactly the kind of artefact that makes a contributor's work reviewable and trustworthy to a maintainer.
- **Internal engineering reviews:** Companies building production AI features run internal presentations in almost this exact structure before a feature ships (problem, spec, demo, eval, human-oversight plan, cost).

---

## 5. Worked Example

**A complete "day of the showcase" walkthrough:**

1. **Morning:** Final check of the GitHub repo structure (3.2) — confirm README is accurate, `.gitignore` is excluding secrets, and the notebook runs cleanly from a fresh Colab session.
2. **Before presenting:** Re-run the 5-case evaluation harness one final time to confirm nothing broke since the last commit (a regression check).
3. **During presentation:** Follow the 7-part structure (3.1) in order, running the live demo confidently — including intentionally showing one edge case (like the unknown Order ID) to demonstrate `escalate_to_human` working correctly live.
4. **Q&A:** When asked "what would you do differently?", refer directly to your `reflection.md` — a prepared, honest answer beats an improvised one.
5. **After the showcase:** The GitHub repository remains as a permanent portfolio artefact — link it directly on your resume/LinkedIn as evidence of a full AI-native engineering capstone: specify → build → verify → oversee → present.

---

## 6. Key Takeaways

- The 7-part structure — **Problem → Spec → Live Demo → Eval Results → Judgment Framework → Cost → 3 Learnings** — is your standard format for presenting any AI-native project, not just this capstone.
- A live demo is stronger, not weaker, when it includes a deliberately-shown edge case that fails safely.
- Your **3 Learnings** should be specific and honest, tied to real moments in your build — not generic statements.
- A professional GitHub portfolio includes: README, notebooks, specs, eval harness, an **AI Decision Journal**, and a written reflection.
- The **AI Decision Journal** documents *engineering decisions and their reasoning* — not a raw prompt log.
- Never commit API keys or secrets — verify `.gitignore` before your final push.
- **Interview tip:** This entire structure — problem, spec, proof, oversight, cost, honest reflection — is literally a rehearsal for how senior AI-native engineers are expected to communicate about their work in the industry.
- This is the final topic of the program — completing it means you have gone through the full arc: **How Machines Think → Specifying for AI → What AI Is → The AI Stack → Ethics & Governance → Maths for AI → Human Oversight → Python → Prompt Engineering & Git → RAG/Agents → Capstone.**

---

## 7. Reference Links

- [GitHub Docs — About READMEs](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-readmes) — official guidance on writing a strong project README (builds on Unit 13).
- [GitHub Docs — Ignoring Files](https://docs.github.com/en/get-started/getting-started-with-git/ignoring-files) — official reference for `.gitignore` (builds on Unit 13).
- [Anthropic Documentation](https://docs.claude.com/) — official documentation to cite when describing your capstone's AI integration.
- [GeeksforGeeks — How to Write a Good README](https://www.geeksforgeeks.org/) — supplementary reading on portfolio presentation.
