# Unit 11 — Python Foundations I
## Topic 3: Professional Coding Discipline

*(Covers: Spec-first discipline — writing the plain-English specification before writing or prompting code · The golden rule — never run code you cannot explain line by line · Edge cases — testing what happens at the boundary of expected input)*

---

## 1. Learning Objectives

By the end of this topic, you will be able to:

1. **Explain** why writing a plain-English specification before writing (or AI-generating) code is a professional discipline, not an optional extra step.
2. **Describe** "the golden rule" of AI-native coding and why it protects you professionally.
3. **Identify** edge cases for a simple program and predict how the program should behave at each one.
4. **Evaluate** a piece of AI-generated code against a specification, and decide whether it is safe to run.
5. **Apply** spec-first discipline and edge-case testing to a small Python program you write yourself.

---

## 2. Overview

You now know enough Python — variables, data types, `if`/`else`, and `for` loops — to write small working programs. But knowing the *syntax* of a language is not the same as coding *professionally*. This topic is about the habits and discipline that separate a hobbyist who copies code from the internet from an **AI-native engineer** who is trusted to build and ship real systems.

This matters more, not less, now that AI can write code for you. In an AI-native workflow, you will frequently ask Claude to generate a Python function for you. That is completely normal and expected — remember the 70/30 rule from Week 2: **AI implements, you specify and verify.** But "verify" is not a suggestion — it is your core professional responsibility. If you cannot explain what a piece of code does, you have no way to catch a mistake in it, and mistakes in AI-generated code (just like mistakes in human-written code) can cause real damage: a wrong bank balance, a wrongly rejected loan application, a leaked password.

This topic teaches you three linked habits: writing your specification *before* code exists (whether you or the AI writes it), refusing to run code you don't understand (the "golden rule"), and deliberately testing the edges of what your program is supposed to handle. These three habits will follow you through every remaining week of this program, and every real AI-native engineering job afterward.

---

## 3. Description

### 3.1 Spec-First Discipline

**Definition:** **Spec-first discipline** means writing a clear, plain-English specification of what a piece of code should do — its inputs, its expected output, and its failure conditions — *before* you write a single line of code, and before you ask an AI to write it for you.

You already learned how to write a good specification in Week 2 (testable, bounded, observable, actionable). Now we apply that exact skill directly to code.

**Why this discipline exists:** Without a specification, both you and an AI model are guessing at what "done" looks like. Two very different-sounding prompts, "write me a function for GST" and "write a Python function `calculate_gst(amount)` that takes a price in rupees and returns the total price including 18% GST, rounded to two decimal places," will produce wildly different quality of code — the second is a specification; the first is a wish.

**Bad prompt vs Good prompt (recap from Week 2, applied to code):**

| Bad ("wish") | Good (spec-first) |
|---|---|
| "Write code to check a transaction." | "Write a Python function `check_transaction(amount)` that returns the string `'Needs Verification'` if `amount` is greater than 5000, otherwise returns `'Approved'`. Input is always a positive number." |
| "Make a loop for marks." | "Write a Python `for` loop that computes the average of a list of integer marks, and prints `'Pass'` if the average is 35 or above, otherwise `'Fail'`." |

Notice the good versions state: the exact inputs, the exact expected outputs, and any assumption about what values are allowed ("input is always a positive number"). This is exactly what allows you to *verify* the resulting code afterward — you know precisely what "correct" was supposed to look like.

### 3.2 The Golden Rule: Never Run Code You Cannot Explain Line by Line

**The rule, stated plainly:** *Never run a piece of code — whether you wrote it, copied it from the internet, or an AI generated it for you — unless you can explain, out loud, what every single line does.*

**Why this exists:** Code executes with real consequences. It can delete a file, send real money, expose private data, or make a decision about a real person (a loan, a medical triage flag). An AI model like Claude is very good at producing code that *looks* correct and often *is* correct — but it can also make mistakes, misunderstand your intent, or (in rare cases) include something genuinely harmful if a prompt was crafted maliciously (this connects to **prompt injection**, which you'll study formally in Week 5). Your job as the human in the loop — the "30%" in the 70/30 rule — is to catch what the AI could have gotten wrong, and you can only do that if you actually understand the code in front of you.

**A short worked example — code you should question before running:**

Imagine you asked an AI assistant: *"Write a Python function that removes a student's record from our results file if their marks are below 35."* It gives you back:

```python
import os

def remove_failed_record(filename):
    os.remove(filename)
```

**Stop. Do not run this yet.** Walk through it line by line:

- `import os` — brings in Python's built-in `os` module, which lets your code interact with the operating system (files, folders, etc.).
- `def remove_failed_record(filename):` — defines a function (we study function definitions formally in Week 12) named `remove_failed_record`, which takes one input, `filename`.
- `os.remove(filename)` — this line **permanently deletes the entire file** named by `filename` from the computer's storage.

Compare this to your specification: you asked to remove *one student's record from within a file*, not delete the *entire file*. This code is dangerously wrong — running it would destroy the whole results file for every student, not just the one who failed. This is a perfect, realistic example of why the golden rule exists: if you had simply run this code because "the AI wrote it, so it must be right," you could have caused serious, irreversible damage.

**Best Practices:**

- Read every line of AI-generated code before running it — treat it the same as code from a stranger on the internet.
- If any single line's purpose is unclear to you, look it up (official documentation, or ask the AI to explain that specific line) *before* running it — never *after*.
- Be especially cautious of any code that deletes, overwrites, or sends data somewhere (files, networks, databases) — these are the operations with the most serious, often irreversible, consequences.
- Run new or AI-generated code on safe, sample data first — never directly on real production data.

**Common Beginner Mistakes:**

- Copy-pasting code from a forum or from an AI chat window straight into a program handling real data, without reading it.
- Assuming that because code "runs without an error," it must be doing the *correct* thing — a program can run perfectly and still produce the wrong result if the logic doesn't match your actual specification.
- Trusting AI output more because it sounds confident — remember from Unit 1, AI text generation is probabilistic and can be fluently, confidently wrong.

### 3.3 Edge Cases: Testing the Boundary of Expected Input

**Definition:** An **edge case** is an input at the extreme boundary of what your program is designed to handle — the smallest, largest, emptiest, or otherwise unusual values that test whether your code's logic truly holds up, not just for typical, "happy path" inputs.

**Why this matters:** Most bugs in real software are not found in the "normal" case — a program almost always works correctly for the input its author was picturing while writing it. Bugs live at the **edges**: an empty list, a zero, a negative number, the very first or very last item, unexpected text where a number was expected.

**Worked example — finding edge cases for our GST function:**

Specification: *"Write a Python function `calculate_gst(amount)` that returns the total price including 18% GST, rounded to two decimal places. Input is a positive number representing rupees."*

```python
def calculate_gst(amount):
    total = amount + (amount * 0.18)
    return round(total, 2)

print(calculate_gst(1000))
```

**Line-by-line:** `amount * 0.18` calculates 18% of the amount; adding it to `amount` gives the GST-inclusive total; `round(total, 2)` rounds the result to two decimal places (paise); `return` sends this value back out of the function to wherever it was called from. For `amount = 1000`: `1000 * 0.18 = 180`, so `total = 1180`, and the output is `1180.0`.

Now, let's deliberately test edge cases:

| Edge case | Input | What should happen (per spec) | What the code actually does |
|---|---|---|---|
| Zero | `calculate_gst(0)` | Total should be `0.0` (0% of nothing is still nothing) | Returns `0.0` — correct. |
| Very small decimal | `calculate_gst(0.01)` | Small rounding behaviour | Returns `0.01` (rounds down) — worth double-checking against real GST rounding rules used by your organisation. |
| Negative number | `calculate_gst(-500)` | **Undefined by the spec** — the spec says "input is a positive number," so a negative input is *outside* the contract | Code runs anyway and returns `-590.0` — a nonsensical result (negative GST) that could silently corrupt real data if this ever happens in production. |
| Non-number (a string) | `calculate_gst("1000")` | **Undefined by the spec** | Python raises a `TypeError` (a Python error/crash), because you cannot multiply a string by a float without an explicit conversion. |

This is exactly why testing edge cases matters: the "happy path" (`amount = 1000`) worked perfectly and gave you false confidence, but the function silently produces a wrong, misleading answer for a negative input, and crashes entirely on a string input. A professional engineer would go back and update either the specification (state clearly what should happen for invalid input) or the code (add validation, for example an `if amount < 0:` check that rejects bad input clearly, rather than silently computing nonsense).

**Best Practices for finding edge cases:**

- Always test: zero, negative numbers, the largest realistic value, an empty list `[]`, and a value of the wrong data type.
- Ask yourself: "What is the *smallest* and *largest* input this code should ever realistically receive — and what happens right at those two extremes?"
- When specifying code (to yourself or to an AI), explicitly state what should happen for invalid input — don't leave it undefined, or the resulting code's behaviour becomes unpredictable.

---

## 4. Real World Application

- **Banking / FinTech:** A UPI transaction validation function must correctly handle the edge case of ₹0, a negative amount (which should never be allowed), and an amount exceeding a daily limit — real financial software is tested extensively against exactly these boundaries before going live.
- **Healthcare:** An AI-assisted triage tool's code must be verified line by line by a human before deployment, and tested against edge cases like a missing vital-sign reading or an implausible value (e.g., a temperature of 0°C) — because a silent, wrong calculation here has real patient-safety consequences (this connects directly to Unit 9's Judgment Framework).
- **E-commerce:** A discount-calculation function must handle the edge case of a cart with zero items, or a coupon applied to a ₹0 order — both are realistic customer scenarios that "happy path" testing alone would miss.
- **AI-native engineering (industry norm):** Code review at real companies almost always includes an explicit step of asking "what happens at the edges?" — and increasingly, reviewing whether AI-generated code was verified against a specification before being merged into a production codebase.

---

## 5. Worked Example

**Specification:** "Write a Python function `classify_attendance(percentage)` that takes a student's attendance percentage (a number from 0 to 100) and returns `'Eligible'` if it is 75 or above, otherwise returns `'Not Eligible'`."

**Step 1 — Write the code matching the spec exactly:**

```python
def classify_attendance(percentage):
    if percentage >= 75:
        return "Eligible"
    else:
        return "Not Eligible"

print(classify_attendance(80))
print(classify_attendance(75))
print(classify_attendance(60))
```

**Expected output:**

```
Eligible
Eligible
Not Eligible
```

**Step 2 — Explain every line (golden rule check before trusting this code):**

- `def classify_attendance(percentage):` — defines a function named `classify_attendance` that accepts one input, `percentage`.
- `if percentage >= 75:` — checks whether the input meets the eligibility threshold; `>=` includes exactly 75, matching the specification's "75 or above."
- `return "Eligible"` / `return "Not Eligible"` — sends back one of two possible string results, matching exactly what the spec requires.
- Three `print(classify_attendance(...))` calls test three different values.

**Step 3 — Deliberately test edge cases before trusting this for real use:**

| Input | Expected (per spec) | Actual result | Verified? |
|---|---|---|---|
| `100` (maximum possible) | `'Eligible'` | `'Eligible'` | ✅ |
| `75` (exact boundary) | `'Eligible'` | `'Eligible'` | ✅ (this is the trickiest edge case — confirms `>=` was used correctly, not `>`) |
| `74.9` (just below boundary) | `'Not Eligible'` | `'Not Eligible'` | ✅ |
| `0` (minimum possible) | `'Not Eligible'` | `'Not Eligible'` | ✅ |
| `-5` (invalid, outside spec) | Undefined by spec | `'Not Eligible'` (code doesn't distinguish invalid input from genuinely low attendance) | ⚠️ Flag this as a specification gap — should invalid input be rejected explicitly? |
| `105` (invalid, outside spec) | Undefined by spec | `'Eligible'` (silently treats impossible attendance as valid) | ⚠️ Same gap — worth raising before shipping this to real students' data. |

**Conclusion:** The function is correct for all *valid* inputs (0–100), including the tricky exact-boundary case of 75. But edge-case testing revealed a real gap: the specification never said what should happen for impossible values like `-5` or `105`. This is exactly the kind of gap-finding you learned to do with specifications in Week 2 — now you're doing the same discipline, applied to real running code.

---

## 6. Key Takeaways

- **Spec-first discipline**: write a clear, testable specification — inputs, outputs, failure conditions — before writing or AI-generating any code.
- The **golden rule**: never run code (yours, a stranger's, or AI-generated) unless you can explain every line of it yourself.
- AI-generated code can look confident and correct while still containing a serious mistake — always verify against your specification before trusting it, exactly as illustrated by the file-deletion example.
- An **edge case** is an input at the extreme boundary of what a program should handle: zero, negative numbers, the maximum value, an empty list, or the wrong data type.
- Testing only the "happy path" gives false confidence — most real bugs live at the edges, not in typical everyday inputs.
- Always explicitly test the *exact boundary* value stated in a specification (e.g., exactly 75, not just 74 and 76) — boundary mistakes (using `>` instead of `>=`) are one of the most common real bugs.
- If testing reveals undefined behaviour for an edge case, treat it as a **specification gap**, not just a code bug — fix the spec, then fix the code.
- **Interview tip:** Interviewers frequently ask "what edge cases would you test for this function?" — having a ready checklist (zero, negative, maximum, empty, wrong type) will serve you in almost every technical interview.
- These three habits — spec-first, the golden rule, and edge-case testing — are the professional discipline that makes AI-assisted coding safe and trustworthy, and they apply to every remaining Python topic in this program.

---

## 7. Reference Links

- [Python Official Documentation — Defining Functions](https://docs.python.org/3/tutorial/controlflow.html#defining-functions) — official reference on function syntax used in the examples above.
- [GeeksforGeeks — Software Testing Basics (Boundary Value Analysis)](https://www.geeksforgeeks.org/software-engineering-boundary-value-analysis/) — supplementary reading on edge-case / boundary testing as a formal testing technique.
- [W3Schools — Python Functions](https://www.w3schools.com/python/python_functions.asp) — beginner-friendly supplementary reading on function syntax.
- [Anthropic Documentation](https://docs.claude.com/) — for later reference on responsibly reviewing AI-generated code once you begin calling Claude's API in Week 12.
