# Unit 10 — Cognition in Practice — Case Studies
## Topic 1: Case Studies

*(Covers: Case study — AI in college admissions · Case study — automated medical triage · Case study — AI loan approval at scale)*

---

## 1. Learning Objectives

By the end of this topic, you will be able to:

1. **Describe** three real-world-style scenarios where an AI system's decision caused harm because human oversight was missing or too weak.
2. **Apply** the Judgment Framework (from Unit 9) to each case to identify exactly where the human override point should have existed.
3. **Identify** the specific failure mode each case represents (missed override, tolerated error rate, diffused accountability).
4. **Differentiate** between a system that had *no* human checkpoint, one that had a checkpoint that was ignored, and one where accountability itself was unclear.
5. **Evaluate** what a better-designed version of each system would have looked like.

---

## 2. Overview

In Unit 9, you learned the **Judgment Framework** — three questions you ask before letting AI make a decision on its own: *What is the cost of this being wrong? Can I verify this without the AI? Who is accountable if this fails?* That framework is only useful if you can actually recognise, in a real system, the moment it should have been applied — and was not.

This topic walks through three composite, illustrative case studies, each built from **patterns that have been widely and repeatedly reported across the AI industry** — in college admissions, healthcare triage, and loan approval. These are not reports on one specific named company or institution; they are realistic scenarios, of the kind documented in industry post-mortems and academic AI-safety literature, designed so you can practise spotting the missing human checkpoint.

As an AI-Native Engineer, this is one of your most important professional skills: given any AI-powered pipeline, you must be able to point to *exactly* where a human needs to stand between the AI's suggestion and the real-world consequence — and explain why. This topic gives you three worked practice scenarios before you design your own oversight checkpoints in Topic 3 of this unit.

---

## 3. Description

### 3.1 Case Study A — AI in College Admissions

**Situation:** A university deploys an AI model to screen thousands of undergraduate applications and produce a "recommend admit / recommend reject / borderline" label for each, based on patterns learned from previous years' admitted students. Admissions staff, overloaded with applications, begin accepting the "recommend reject" label for most candidates without a full manual review, treating it as a final decision rather than a suggestion.

**What the AI did:** It learned patterns from *historical* admissions data — data that reflected the biases of human decisions made in earlier years (for example, systematically favouring applicants from certain school types or geographic regions that were over-represented in the past). The model faithfully reproduced those old patterns.

**Where the human override point was missed:** The system was designed with a checkpoint on paper ("staff should review all recommend-reject cases") but under time pressure this checkpoint quietly stopped being exercised in practice. There was no *mandatory*, logged, auditable step forcing a second look — it depended entirely on individual staff discipline, with no system-level enforcement.

**Judgment Framework applied:**
| Question | Answer in this case |
|---|---|
| Q1: Cost of being wrong? | High — a wrongly rejected student loses a life-shaping opportunity; this is not a low-stakes decision. |
| Q2: Can I verify without the AI? | Yes — a human admissions officer can read an application and judge it independently. |
| Q3: Who is accountable if this fails? | Unclear — the AI vendor, the university, or the individual officer? Because it was unclear, nobody enforced the checkpoint. |

**What should have happened:** Given a high cost of error (Q1) and the ability to verify independently (Q2), this is exactly the kind of decision that Unit 9 tells us must keep a **mandatory**, not optional, human checkpoint — with clear, named accountability (Q3) for who signs off.

**Lesson:** A checkpoint that exists only "on paper," with no system enforcement and no named accountable person, is not a real checkpoint.

---

### 3.2 Case Study B — Automated Medical Triage

**Situation:** A hospital emergency department introduces an AI triage assistant that scores incoming patients' symptom descriptions and suggests a priority level (e.g., "routine," "urgent," "emergency"). To manage a high patient load, staff begin trusting scores of "routine" without a nurse re-checking vital signs for those patients first.

**What the AI did:** The model was highly accurate *on average* — it correctly triaged the vast majority of cases. But "highly accurate on average" is not the same as "safe for every individual patient." A small percentage of genuinely urgent cases were scored as "routine" because their symptom description happened to resemble common, non-urgent patterns in the training data.

**Failure mode tolerated:** The hospital's rollout plan tolerated the model's overall accuracy rate (e.g., 97%) as "good enough," without separately asking: *what happens, specifically, to the 3% who are wrongly scored as low-priority?* This is a **confusion-matrix blind spot** (Unit 7/8): overall accuracy hides the cost of false negatives in a high-stakes domain.

**Judgment Framework applied:**
- **Q1 (cost of being wrong):** Extremely high — a missed emergency case can cost a life.
- **Q2 (verify without AI):** Yes — a nurse checking vital signs directly is a fast, reliable independent check.
- **Q3 (accountability):** The treating clinician remains legally and professionally accountable — but if they are trained to defer to the AI's score, accountability and actual practice drift apart.

**What should have happened:** Because Q1 is extremely high, the acceptable error threshold (Unit 9 — "defining safe boundaries") should have been near-zero for missed emergencies specifically, not just a good *average* accuracy. The system needed a low-cost, fast, **mandatory** human vital-signs check for every patient, regardless of the AI's score — using the AI to *prioritise* attention, never to *skip* it.

**Lesson:** A high overall accuracy score can hide an unacceptable failure rate on the specific sub-group where the cost of error is highest. Always ask "accurate for whom, and wrong in what way?" — not just "how accurate overall?"

---

### 3.3 Case Study C — AI Loan Approval at Scale

**Situation:** A lending platform uses an AI model to approve or reject small personal loans automatically, at a scale of thousands of applications per day, with human review reserved only for large loan amounts.

**What the AI did:** For small loans, the model's decision was final and immediate — approve, reject, or offer a different interest rate — with no human in the loop at all, because the *individual* cost of any one small loan being wrongly rejected seemed too small to justify the cost of manual review at that volume.

**Who was accountable:** When customers complained about being rejected without explanation, it became unclear who owned the decision — the data science team that built the model, the product team that set the "auto-approve below ₹50,000" policy, or the compliance team responsible for fair-lending rules. Each pointed to the model as the "decision-maker," diffusing human accountability.

**Judgment Framework applied:**
- **Q1:** Individually, the cost of one wrong small-loan rejection is moderate — but at scale, a systematic bias (e.g., consistently under-approving applicants from a particular income bracket or region) causes large, cumulative, and legally significant harm.
- **Q2:** Verifying every single small loan by hand is not practical at this volume — this is a case where full manual verification is genuinely not feasible.
- **Q3:** Accountability was never clearly assigned to a single named role or team — which is itself the core failure, independent of the AI's accuracy.

**What should have happened:** When Q2 says "full manual check of every case isn't feasible," the correct answer is *not* "therefore no oversight" — it is **statistical, sampled human oversight**: regularly auditing a random sample of auto-approved and auto-rejected decisions for patterns of unfair bias, with one clearly named, accountable role (e.g., a "model risk officer") who owns that audit and can pause the system if a bias pattern appears.

**Lesson:** When individual-case review isn't practical at scale, oversight shifts from *checking every decision* to *auditing the pattern of decisions* — but someone must still be clearly, individually accountable for running that audit.

---

**Comparison Table — The Three Failure Modes**

| Case | What went wrong | Failure type |
|---|---|---|
| College admissions | Checkpoint existed on paper but wasn't enforced | **Missed / unenforced override point** |
| Medical triage | Good average accuracy hid a dangerous failure rate on a critical sub-group | **Tolerated failure mode in a high-stakes subgroup** |
| Loan approval | No individual review was feasible, and no one owned pattern-level audit | **Diffused / unassigned accountability** |

> **Important Note:** None of these three cases requires the AI itself to be "bad." In every case, the *model* may have been reasonably accurate. The failure was in **how humans designed (or failed to design) the oversight around it.**

**Common Mistakes:**
- Treating "the AI is 95%+ accurate" as equivalent to "this system is safe to deploy without oversight."
- Designing a checkpoint that exists in a policy document but has no system-enforced trigger.
- Assuming that because full manual review isn't feasible at scale, no oversight is needed at all (the correct middle ground is sampled/statistical audit).

---

## 4. Real World Application

- **EdTech / Admissions:** Universities and scholarship boards using AI to pre-screen applicants must build in mandatory, logged human review for borderline and rejected cases — not just an optional one.
- **Healthcare:** Hospital triage and diagnostic-support tools are increasingly common in Indian hospitals; regulatory guidance (and basic patient safety) requires a human clinician to remain the final decision-maker, with the AI acting only as a prioritisation aid.
- **BFSI (Banking, Financial Services, Insurance):** RBI-regulated lenders using AI-based credit scoring must maintain fair-lending audits and explainability — a direct real-world analogue of Case Study C.
- **Hiring / HR Tech:** AI resume-screening tools face the same "missed override point" risk as Case Study A — a rejected candidate rarely gets a human second look unless it's specifically designed in.
- **Content Moderation:** Social media platforms using AI to auto-remove posts face the same "diffused accountability" pattern as Case Study C when appeals processes are slow or unclear.

---

## 5. Worked Example

**Task:** For a new AI system — an **AI-powered scholarship-award assistant** that ranks student applications and auto-approves the top 20% for a scholarship — apply the Judgment Framework and identify the correct oversight design, using the three case studies above as reference patterns.

1. **Q1 — Cost of being wrong?** High for individual students (losing a scholarship affects their education), moderate-to-high in aggregate (systemic unfairness damages institutional trust).
2. **Q2 — Can I verify without the AI?** Yes, for borderline cases (a human can read an application); no, for full-volume review at scale.
3. **Q3 — Who is accountable?** Recommendation: name a specific "Scholarship Committee Chair" role as the accountable owner — mirroring the fix identified for Case Study C.

**Recommended design (combining lessons from all three cases):**
- Clear top-tier auto-approvals and clear bottom-tier auto-rejections can be automated (like the small-loan case) **only if** a random sample audit is run monthly by the named accountable owner.
- All borderline-band applications get a **mandatory, system-enforced** human review — not an optional one left to staff discretion (fixing Case Study A's failure).
- The review dashboard must show sub-group breakdowns (by school type, region, gender) so a hidden bias affecting a specific group is visible, not hidden inside an "overall accuracy" number (fixing Case Study B's failure).

This worked example shows how the three failure patterns combine into one practical checklist you can apply to almost any AI decision-making system you are asked to specify or oversee.

---

## 6. Key Takeaways

- A human checkpoint that exists only in a policy document, with no system enforcement, is not a real checkpoint (Case A).
- High **overall** accuracy can hide a dangerous failure rate in a specific high-stakes sub-group — always check sub-group performance, not just the average (Case B).
- When full manual review isn't feasible at scale, shift to **sampled, statistical audits** with one clearly named accountable owner — never "no oversight" (Case C).
- Always run the 3-question Judgment Framework (cost of error, can you verify independently, who is accountable) on every new AI-decision system you are asked to build or oversee.
- **Interview tip:** If asked to critique an AI system's design, structure your answer as: "what's the cost of error, is there a verifiable/enforced checkpoint, and who is named as accountable" — this signals systematic judgment, not just opinion.
- These three failure types — missed override, tolerated sub-group failure, diffused accountability — are patterns you will see repeated across almost every real-world AI safety incident.

---

## 7. Reference Links

- [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework) — Govern/Map/Measure/Manage functions relevant to human oversight design.
- [EU AI Act — official text](https://artificialintelligenceact.eu/) — human oversight obligations for high-risk AI systems.
- [Google SRE Postmortem Culture](https://sre.google/sre-book/postmortem-culture/) — an authentic, industry-standard reference for structuring accountability and failure analysis (used again in Topic 4 of this unit).
