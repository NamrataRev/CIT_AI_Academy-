# Unit 13 — Prompt Engineering + Version Control
## Topic 1: Prompt Engineering Fundamentals

*(Covers: System prompt vs user prompt · Role assignment · Few-shot examples · Chain-of-thought prompting · Constraints · Output format control)*

---

## 1. Learning Objectives

By the end of this topic, you will be able to:

1. **Differentiate** between a system prompt and a user prompt, and explain what each one is responsible for.
2. **Implement** role assignment in a prompt to change how an LLM responds.
3. **Create** a few-shot prompt that teaches the model a pattern using examples.
4. **Apply** chain-of-thought prompting to get a model to reason step by step before answering.
5. **Write** clear constraints that tell an AI what it must NOT do.
6. **Implement** output format control so an LLM's reply is returned as clean, predictable JSON.

---

## 2. Overview

In **Unit 12**, you learned how to send a message to Claude using the Anthropic API and read back its reply. That got you a *working* call. But if you send the same rough request to an LLM every time, you will get inconsistent, sometimes-useless answers — and in a professional AI-native role, "it sort of works" is not good enough.

**Prompt engineering** is the practice of *deliberately designing* the text you send to an LLM so that it reliably produces the output you actually need. It sits exactly at the centre of the "70/30 rule" you learned in Week 2: **you specify (through a well-engineered prompt), the AI implements, and you verify.** A well-engineered prompt is your specification, written in a language the model can act on.

This topic teaches you six practical techniques that professional AI-native engineers use every day: separating system prompts from user prompts, assigning the model a role, teaching it with examples (few-shot), asking it to "think out loud" (chain-of-thought), telling it what not to do (constraints), and forcing a specific output shape (format control). By the end, you will be able to turn a vague request like "summarise this" into a precise instruction that produces the same reliable shape of answer, every time you run it — bridging back to Unit 1's lesson that probabilistic systems can still be made *reliable* through good design, even though they are not fully deterministic.

---

## 3. Description

### 3.1 System Prompt vs User Prompt

**Definition:** In the Anthropic API, a request is built from two distinct kinds of instructions:

- The **system prompt** — a one-time block of instructions that sets the *context, role, and rules* for the entire conversation. The model treats this as its "job description."
- The **user prompt** — the actual, live request or question for this specific turn — what you (or your application's user) is asking right now.

**Why this exists:** Imagine a call-centre employee. Before they take a single call, they are given a briefing: "You work for XYZ Bank. Always be polite. Never share account numbers over the phone." That briefing is the **system prompt** — set once, applies to everything. Then, each customer call is different: "What's my account balance?", "I lost my card." Each of those live requests is the **user prompt**.

```python
import anthropic

client = anthropic.Anthropic()  # reads ANTHROPIC_API_KEY from your environment (see Unit 12)

response = client.messages.create(
    model="claude-sonnet-4-5",
    max_tokens=300,
    system="You are a helpful assistant for an Indian railway enquiry desk. Always answer in simple English and mention PNR status only if the user provides a PNR number.",
    messages=[
        {"role": "user", "content": "Can you tell me if train 12622 runs on Sundays?"}
    ]
)
print(response.content[0].text)
```

**Line-by-line:**
- `import anthropic` — loads the Anthropic Python library installed in Unit 12.
- `client = anthropic.Anthropic()` — creates the connection object that will talk to Claude's servers, using your API key.
- `system="..."` — this is the **system prompt**: it tells the model its role and its permanent rules for this whole conversation.
- `messages=[{"role": "user", "content": "..."}]` — this is the **user prompt**: the specific, live question for this turn.
- `client.messages.create(...)` — sends the whole request (system + user message) to Claude and waits for the reply.
- `response.content[0].text` — pulls out the plain text of Claude's reply from the JSON response object (as you learned in Unit 12).

| Aspect | System Prompt | User Prompt |
|---|---|---|
| Set how often? | Usually once per conversation/application | Every single turn |
| Contains | Role, rules, tone, boundaries | The actual question/request |
| Who writes it? | The developer (you) | The end user, or your app on their behalf |
| Analogy | Employee's job briefing | Customer's specific question |

---

### 3.2 Role Assignment

**Definition:** Role assignment means telling the model, explicitly, *who it is* for this task — e.g., "You are an experienced Indian tax consultant" or "You are a friendly UPI payments support agent." This is usually written inside the system prompt.

**Why this matters:** LLMs have been trained on an enormous variety of text — legal documents, casual chats, code, poetry. Assigning a role narrows the model's behaviour toward the tone, vocabulary, and depth appropriate for that persona, producing far more consistent answers.

**Before (no role assigned):**
```python
system_prompt = ""
user_prompt = "Is it okay to skip my loan EMI this month?"
```
Without a role, the model might answer generically, sometimes vaguely, sometimes overly casual.

**After (role assigned):**
```python
system_prompt = (
    "You are a responsible financial advisor for an Indian bank's customer app. "
    "You give cautious, factually accurate guidance and always recommend contacting "
    "the bank directly for account-specific decisions."
)
user_prompt = "Is it okay to skip my loan EMI this month?"

response = client.messages.create(
    model="claude-sonnet-4-5",
    max_tokens=300,
    system=system_prompt,
    messages=[{"role": "user", "content": user_prompt}]
)
print(response.content[0].text)
```
Now the model consistently answers with the caution and tone of a real financial advisor, not a generic chatbot.

---

### 3.3 Few-Shot Examples

**Definition:** "Few-shot prompting" means showing the model a small number of **example input → output pairs** directly inside the prompt, so it learns the *pattern* you want it to follow, before giving it the real input.

**Why this exists:** Some tasks are hard to describe in words but easy to demonstrate. Instead of writing paragraphs of instructions, you show 2–3 examples of exactly what "good" looks like.

**Before (zero-shot — no examples):**
```python
user_prompt = "Classify this review as Positive, Negative, or Neutral: 'Food was cold but delivery was fast.'"
```
This can work, but on tricky, mixed-sentiment reviews like this one, the model's answer can vary between runs.

**After (few-shot — pattern taught with examples):**
```python
few_shot_prompt = """Classify each review as Positive, Negative, or Neutral. Follow the exact format shown.

Review: "Amazing biryani, will order again!"
Classification: Positive

Review: "Order was 2 hours late and cold."
Classification: Negative

Review: "Packaging was fine, taste was average."
Classification: Neutral

Review: "Food was cold but delivery was fast."
Classification:"""

response = client.messages.create(
    model="claude-sonnet-4-5",
    max_tokens=10,
    messages=[{"role": "user", "content": few_shot_prompt}]
)
print(response.content[0].text)
```
**Why the output is more reliable:** the model now has a clear pattern — "Review: ... / Classification: <one word>" — and simply continues that pattern for the new review, instead of guessing the format itself.

---

### 3.4 Chain-of-Thought Prompting

**Definition:** Chain-of-thought (CoT) prompting means asking the model to **explain its reasoning step by step before giving a final answer**, instead of jumping straight to a conclusion.

**Why this matters:** Just like a student who "shows their working" in a maths exam is less likely to make a silly mistake, a model that reasons step by step before answering is generally more accurate on multi-step problems (arithmetic, logic, planning).

**Before (direct answer, no reasoning):**
```python
user_prompt = "A train travels 60 km in the first hour and 90 km in the second hour. What is its average speed?"
```

**After (chain-of-thought):**
```python
cot_prompt = (
    "A train travels 60 km in the first hour and 90 km in the second hour. "
    "What is its average speed? Think step by step, showing each calculation, "
    "then give the final answer on the last line as 'Final Answer: ...'."
)

response = client.messages.create(
    model="claude-sonnet-4-5",
    max_tokens=300,
    messages=[{"role": "user", "content": cot_prompt}]
)
print(response.content[0].text)
```
**Expected style of output:**
```
Step 1: Total distance = 60 km + 90 km = 150 km
Step 2: Total time = 1 hour + 1 hour = 2 hours
Step 3: Average speed = Total distance / Total time = 150 / 2 = 75 km/h
Final Answer: 75 km/h
```
By forcing the "Final Answer:" label, you also make it easy for your Python code to reliably pull out just the answer from the longer explanation.

---

### 3.5 Constraints

**Definition:** Constraints are explicit instructions in your prompt about what the model must **not** do — a boundary, not just an instruction on what *to* do.

**Why this matters:** Without constraints, a helpful model may over-deliver — adding unwanted disclaimers, generating extra unrelated content, or guessing at facts it doesn't actually know (a form of the **hallucination** you studied in Unit 3 and Unit 5).

**Example — without constraints:**
```python
user_prompt = "Write a 2-line SMS telling a customer their food delivery is delayed."
```
The model might add extra sentences, emojis, or a signature the app doesn't want.

**Example — with constraints:**
```python
constrained_prompt = (
    "Write a 2-line SMS telling a customer their food delivery is delayed. "
    "Constraints: Do NOT use emojis. Do NOT exceed 160 characters total. "
    "Do NOT mention a specific new delivery time unless one is given to you. "
    "Do NOT add a greeting or sign-off."
)

response = client.messages.create(
    model="claude-sonnet-4-5",
    max_tokens=100,
    messages=[{"role": "user", "content": constrained_prompt}]
)
print(response.content[0].text)
```
**Important Note:** Constraints work best when they are specific and measurable ("do not exceed 160 characters") rather than vague ("keep it short").

---

### 3.6 Output Format Control

**Definition:** Output format control means instructing the model to return its answer in a specific, predictable structure — such as JSON, a numbered list, or a fixed template — so that your Python code can reliably read and use the response (instead of a human having to read free-flowing prose).

**Why this matters:** Real AI-native applications rarely just print the model's reply to a screen — they pass it to *other code*. That code needs a predictable shape. If the model sometimes says `{"status": "delayed"}` and sometimes says `"The status is delayed"`, your program will crash trying to read it.

```python
import json

format_prompt = """Extract the order status from the customer message below.
Return ONLY valid JSON in exactly this shape, with no extra text before or after it:
{"order_id": "<string or null>", "status": "<one of: delayed, delivered, cancelled, unknown>"}

Customer message: "Hi, my order #4521 still hasn't arrived, it's been 2 hours!"
"""

response = client.messages.create(
    model="claude-sonnet-4-5",
    max_tokens=100,
    messages=[{"role": "user", "content": format_prompt}]
)

raw_text = response.content[0].text
data = json.loads(raw_text)   # converts the JSON text into a Python dictionary
print(data["order_id"], data["status"])
```

**Line-by-line (new parts):**
- `import json` — Python's built-in module for reading and writing JSON text.
- `raw_text = response.content[0].text` — the model's raw reply, which we *expect* to be pure JSON text because we instructed it to be.
- `json.loads(raw_text)` — parses that JSON text into a real Python dictionary (`data`), so `data["status"]` gives you the value directly instead of you having to search through a sentence.

> **Important Note:** Never fully trust that the model obeyed the format instruction 100% of the time (remember — LLMs are probabilistic, from Unit 1!). Section 3.4 of the next topic, and the whole of Topic 3 in this unit, cover **output validation and retry** — the professional safety net for exactly this risk.

**Best Practices (all six techniques):**
- Keep the system prompt stable across a session; put the changing information in the user prompt.
- Use few-shot examples when a task's *format* is hard to describe in plain words.
- Ask for chain-of-thought only when the task genuinely needs multi-step reasoning — it costs more tokens (and money) than a direct answer.
- Make constraints specific and testable, not vague.
- Always ask for a fixed output format when your code — not a human — will read the response next.

**Common Beginner Mistakes:**
- Mixing role instructions and the live question together in one long paragraph, making it hard for the model (and you) to tell what's a permanent rule vs. a one-time request.
- Giving inconsistent few-shot examples (different formats in each example), which confuses the model instead of teaching it a clear pattern.
- Forgetting to say "ONLY return JSON, no extra text" — models often add a friendly sentence like "Sure, here's the JSON:" which breaks `json.loads()`.

---

## 4. Real World Application

- **Banking/FinTech:** A system prompt assigning the role "cautious financial assistant" plus strict constraints ("never guess an account balance") keeps an AI chat assistant safe for real banking use.
- **E-commerce/Food Delivery:** Few-shot examples train a model to classify thousands of customer reviews into Positive/Negative/Neutral in a consistent format for a dashboard.
- **Healthcare:** Chain-of-thought prompting helps an AI assistant reason through a multi-step triage checklist out loud, so a human nurse overseeing it (per the Judgment Framework, Unit 9) can see *why* it reached its suggestion.
- **Vernacular AI Translation:** Output format control (e.g., `{"original": "...", "translated": "...", "confidence": "..."}`) lets a translation feature plug directly into a mobile app's UI without a human parsing free text.
- **Customer Support Copilots:** Combining role assignment + constraints + JSON output format is the standard recipe for a production support chatbot that both sounds right and integrates cleanly with backend systems.

---

## 5. Worked Example

**Scenario:** Build a single, well-engineered prompt for an Indian food-delivery app's support assistant that uses all six techniques together.

```python
import anthropic
import json

client = anthropic.Anthropic()

system_prompt = (
    "You are 'FoodieBot', the official customer support assistant for a food-delivery app in India. "     # Role assignment
    "Always be polite, brief, and reassuring. "
    "Constraints: Do NOT promise a specific refund amount. Do NOT guess an order's live location. "         # Constraints
    "Do NOT use emojis."
)

few_shot_and_cot_prompt = """Classify the customer's issue and draft a short reply. Think step by step
internally, but only output the final JSON. Follow this exact pattern:

Customer: "My order is 1 hour late, I'm really hungry!"
Output: {"issue_type": "delay", "reply": "We're sorry for the delay — our team is checking with the delivery partner now and will update you shortly."}

Customer: "The food I received was completely different from what I ordered."
Output: {"issue_type": "wrong_item", "reply": "We're sorry about that! Please raise a replacement request in the app and our team will resolve it right away."}

Now classify this customer message and respond in the exact same JSON format, with no extra text:
Customer: "It's been 2 hours and my order still shows preparing, what is going on?"
Output:"""

response = client.messages.create(
    model="claude-sonnet-4-5",
    max_tokens=200,
    system=system_prompt,
    messages=[{"role": "user", "content": few_shot_and_cot_prompt}]
)

data = json.loads(response.content[0].text)
print("Issue type:", data["issue_type"])
print("Reply to send:", data["reply"])
```

**What's happening, technique by technique:**
1. **System vs user prompt** — the persona and safety rules live in `system`; the live customer message and task live in the user message.
2. **Role assignment** — "FoodieBot... official customer support assistant."
3. **Few-shot examples** — two full example Customer→Output pairs teach the exact JSON pattern.
4. **Chain-of-thought** — "Think step by step internally" nudges better reasoning, while "only output the final JSON" keeps the visible reply clean.
5. **Constraints** — explicit "Do NOT" rules protect against over-promising.
6. **Output format control** — the JSON shape lets `json.loads()` reliably extract `issue_type` and `reply` for the app to use.

---

## 6. Key Takeaways

- **System prompt** = permanent role and rules; **user prompt** = the live, changing request.
- **Role assignment** narrows an LLM's tone and behaviour to match a specific persona.
- **Few-shot examples** teach a pattern through demonstration when instructions alone are hard to write.
- **Chain-of-thought** prompting improves accuracy on multi-step reasoning tasks by making the model "show its work."
- **Constraints** define hard boundaries — what the model must never do.
- **Output format control** (e.g., strict JSON) is essential whenever your code, not a human, will consume the model's response.
- These six techniques are combinable — production prompts almost always use several together.
- **Interview tip:** Be ready to explain *why* each technique improves reliability, not just how to write it — interviewers often ask "why would you use few-shot here instead of just explaining the rule?"
- None of these techniques make an LLM deterministic (Unit 1) — they only make its probabilistic output *more consistently* useful, which is why output validation (Topic 3) is still required in production.

---

## 7. Reference Links

- [Anthropic Documentation — Prompt Engineering Overview](https://docs.claude.com/) — official guidance on system prompts, roles, and prompting techniques.
- [Anthropic Documentation — Use Examples (Multishot Prompting)](https://docs.claude.com/) — official few-shot prompting guidance.
- [Anthropic Documentation — Chain of Thought Prompting](https://docs.claude.com/) — official CoT guidance for Claude models.
- [Python Official Docs — json module](https://docs.python.org/3/library/json.html) — for parsing structured model output.
