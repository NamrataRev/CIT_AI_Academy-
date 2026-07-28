# Unit 15 — Capstone Build Sprint and Showcase
## Topic 1: Specification and Build

*(Covers: Writing a formal problem statement and 1-page specification · Building the Python orchestration layer · Writing a 5-role context-engineered system prompt · Producing structured JSON output and validating it)*

---

## 1. Learning Objectives

By the end of this topic, you will be able to:

1. **Create** a formal problem statement and a 1-page specification for an AI-powered system, following the testable/bounded/observable/actionable rules from Unit 2.
2. **Implement** a Python orchestration layer that wires together user input, a system prompt, an Anthropic API call, and output handling.
3. **Create** a complete 5-role (Authority, Exemplar, Constraint, Rubric, Metadata) system prompt for a real capstone project.
4. **Implement** structured JSON output from an LLM call, along with a Python validation function that checks the response before it is trusted.
5. **Analyze** how every earlier unit in this program (spec-writing, prompt engineering, Python, APIs) comes together in one working system.

---

## 2. Overview

Welcome to the capstone. Everything you have learned so far — writing a specification (Unit 2), understanding what AI can and cannot do (Unit 3), the maths behind embeddings and probability (Units 6–8), the Judgment Framework (Unit 9), Python fundamentals and calling an LLM (Units 11–12), and prompt engineering with version control (Unit 13) — now gets assembled into **one real, working, AI-powered system**, built and owned by you from problem statement to working code.

This topic (Topic 1 of Unit 15) covers the **first half of the capstone build**: turning a vague idea ("I want to help my local kirana/food-delivery shop's customers get quick answers") into a precise, testable specification, and then writing the actual Python code and prompt that make it real. Topic 2 will cover testing, evaluation, and safety. Topic 3 will cover presenting your finished work.

To keep this topic concrete rather than abstract, we will build **one running example project** throughout: **"SahayakBot"** — a small AI-powered customer-support assistant for a fictional Indian **online food-delivery and grocery app**, which answers customer questions in **English and Hindi** about order status, refund policy, and delivery timing, and knows when to hand off to a human agent. ("Sahayak" means "helper/assistant" in Hindi — a fitting name for a support bot.) You will build your own capstone on a different problem, but you should follow the exact same steps shown here for SahayakBot.

---

## 3. Description

### 3.1 Writing a Formal Problem Statement and 1-Page Specification

**Definition:** A **problem statement** is a short, precise description of *what problem you are solving, for whom, and why it matters* — written *before* any code. A **1-page specification** expands that problem statement into the testable, bounded, observable, actionable detail (from Unit 2) that an AI system can actually be built and evaluated against.

**Why this matters:** Every mistake in an AI-native project traces back to a vague or missing specification. If you cannot write down exactly what "correct" looks like, you cannot verify whether your AI system is doing its job — and verification is 30% of your professional responsibility under the 70/30 rule (Unit 2).

**SahayakBot — Problem Statement (3 sentences, as taught in Unit 1):**

> Customers of a small Indian food-delivery app frequently ask repetitive questions ("Where is my order?", "How do I get a refund?", "Why is delivery late?") that currently take a human support agent 5–10 minutes to answer during peak hours. This causes long wait times and frustrated customers, especially those who prefer to ask in Hindi rather than English. SahayakBot will answer these three common question types instantly and correctly in the customer's own language, escalating anything it is not confident about to a human agent.

**SahayakBot — 1-Page Specification:**

| Spec Field | Detail |
|---|---|
| **Inputs** | A customer's free-text message (English or Hindi), plus the customer's Order ID (looked up from a deterministic order database — never guessed by the AI). |
| **Expected Outputs** | A JSON object containing: the reply text (in the customer's language), a `category` (order_status / refund_policy / delivery_delay / other), and an `escalate_to_human` boolean. |
| **Failure Conditions** | (1) Order ID not found in the database. (2) Message doesn't match any of the 3 known categories. (3) AI confidence is low / question involves money disputes above ₹500. In all 3 cases → `escalate_to_human = true`. |
| **Boundaries (what it will NOT do)** | Will not process refunds itself (only explains policy). Will not guess an order status — it must call the deterministic order-lookup function. Will not respond in any language other than English/Hindi (escalates instead of guessing a wrong translation). |
| **Success Metric** | ≥90% of the 5 test cases (built in Topic 2) pass; 100% of refund/order-status facts must come from the database, never invented. |
| **Human Override Point** | A human agent reviews every `escalate_to_human = true` case before it reaches the customer (per the Judgment Framework, Unit 9). |

> **Important Note:** Notice that the specification separates what the **AI generates** (natural-language phrasing) from what the **deterministic code fetches** (the actual order status). This directly reuses the deterministic-vs-probabilistic distinction from Unit 1 — the AI must never be allowed to "guess" a fact that a database already knows for certain.

---

### 3.2 Building the Python Orchestration Layer

**Definition:** The **orchestration layer** is the plain Python code that sits *around* the AI model — it takes the user's input, prepares the prompt, calls the Anthropic API, and handles the response. The AI does not run itself; **your Python code is what invokes it, in the right order, with the right information.**

Here is SahayakBot's orchestration layer, building directly on the API-calling pattern from Unit 12:

```python
import os
import json
from anthropic import Anthropic

# The client reads the ANTHROPIC_API_KEY from your environment variable —
# never hard-code your API key in the source file (Unit 13: .gitignore lesson).
client = Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))

# A deterministic "database" lookup — a dictionary standing in for a real database.
# This must NEVER be replaced by the AI guessing an answer (Unit 1 principle).
ORDER_DATABASE = {
    "ORD1001": {"status": "Out for delivery", "eta_minutes": 20},
    "ORD1002": {"status": "Delivered", "eta_minutes": 0},
}

def get_order_status(order_id):
    """Deterministic lookup. Returns None if the order does not exist."""
    return ORDER_DATABASE.get(order_id)

def build_user_message(customer_message, order_id):
    order_info = get_order_status(order_id)
    order_context = (
        f"Order status from database: {order_info}"
        if order_info else "Order ID not found in database."
    )
    return f"Customer message: {customer_message}\n{order_context}"

def call_sahayakbot(customer_message, order_id, system_prompt):
    user_content = build_user_message(customer_message, order_id)
    response = client.messages.create(
        model="claude-sonnet-4-5",
        max_tokens=300,
        system=system_prompt,
        messages=[
            {"role": "user", "content": user_content}
        ]
    )
    return response.content[0].text
```

**Line-by-line explanation:**

- `import os, json` — `os` lets us read environment variables (keeping the API key secret); `json` will be used later to parse structured output.
- `from anthropic import Anthropic` — imports the official Anthropic Python library's client class.
- `client = Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))` — creates one reusable connection to the Claude API, authenticated with a key read from your machine's environment variables, not typed into the code.
- `ORDER_DATABASE = {...}` — a Python **dictionary** (Unit 12) standing in for a real order-management database, mapping an Order ID (key) to its status details (value).
- `def get_order_status(order_id):` — a **function** (Unit 12) with exactly one job: look up an order. `.get()` returns `None` safely if the key doesn't exist, instead of crashing.
- `def build_user_message(...)`: constructs the exact text that will be sent to Claude, combining the customer's raw message with the *deterministic* order fact — so the AI is *told* the fact rather than being asked to guess it.
- `def call_sahayakbot(...)`: the orchestration function — builds the message, calls `client.messages.create(...)` (the real Anthropic API shape: `model`, `max_tokens`, `system`, `messages`), and returns Claude's reply text.
- `response.content[0].text` — the API returns a response object; `.content[0].text` extracts the actual generated text from it (Unit 12: parsing the JSON response).

---

### 3.3 Writing a 5-Role Context-Engineered System Prompt

Using the **5-Role Context Framework** from Unit 13 (Authority, Exemplar, Constraint, Rubric, Metadata), here is SahayakBot's actual system prompt:

```python
SAHAYAKBOT_SYSTEM_PROMPT = """
[AUTHORITY]
You are SahayakBot, the official customer-support assistant for "TazaEats",
an Indian food-delivery app. You only answer questions about order status,
refund policy, and delivery delays.

[EXEMPLAR]
Example — Good response:
Customer: "Mera order kahan hai?" (order status given: Out for delivery, ETA 20 min)
Reply: {"reply_text": "Aapka order abhi delivery ke liye nikal chuka hai, aur
20 minute mein pahunch jayega!", "category": "order_status", "escalate_to_human": false}

[CONSTRAINT]
- NEVER invent an order status. Only use the order status given to you in the message.
- NEVER promise a refund amount yourself — only explain that refunds are processed
  within 3-5 business days per policy.
- If the question is not about order status, refund policy, or delivery delay,
  OR if the order ID was not found, set "escalate_to_human": true.
- Reply in the SAME language the customer used (English or Hindi).

[RUBRIC]
A good response: (1) answers only using given facts, (2) matches the customer's
language, (3) is under 40 words, (4) always returns valid JSON in the exact
schema shown in [METADATA].

[METADATA]
Always respond with ONLY a JSON object in this exact schema, nothing else:
{"reply_text": "<string>", "category": "order_status|refund_policy|delivery_delay|other",
"escalate_to_human": <true|false>}
"""
```

**Why each role matters (recap from Unit 13):** **Authority** tells the model *who it is* and its scope. **Exemplar** shows a concrete good example so the model can pattern-match. **Constraint** tells the model what it must *never* do — critical for safety (Unit 5). **Rubric** defines what "good" looks like, so the model can self-check. **Metadata** locks the exact output format, which is what makes the JSON in section 3.4 reliably parseable.

---

### 3.4 Producing Structured JSON Output and Validating It

**Why this matters:** Your Python code cannot safely "trust" free-form AI text — it must **validate** that the response matches the exact structure your program expects, before acting on it. This is where the probabilistic AI output meets deterministic code discipline (Unit 1 again!).

```python
def validate_sahayakbot_response(raw_text):
    """
    Parses and validates SahayakBot's JSON response.
    Returns (True, parsed_dict) if valid, (False, error_message) if not.
    """
    try:
        parsed = json.loads(raw_text)
    except json.JSONDecodeError:
        return False, "Response was not valid JSON."

    required_keys = {"reply_text", "category", "escalate_to_human"}
    if not required_keys.issubset(parsed.keys()):
        return False, f"Missing required keys: {required_keys - parsed.keys()}"

    valid_categories = {"order_status", "refund_policy", "delivery_delay", "other"}
    if parsed["category"] not in valid_categories:
        return False, f"Invalid category: {parsed['category']}"

    if not isinstance(parsed["escalate_to_human"], bool):
        return False, "escalate_to_human must be true or false."

    return True, parsed
```

**Line-by-line explanation:**

- `json.loads(raw_text)` — attempts to convert Claude's text reply into a real Python dictionary. Wrapped in `try/except` (Unit 12) because the model, being probabilistic, could occasionally return malformed JSON.
- `required_keys.issubset(parsed.keys())` — checks that all three expected fields are present; `parsed.keys()` lists the keys actually returned.
- `valid_categories` check — guards against the model inventing a category outside the four allowed values (Unit 13: output validation).
- `isinstance(parsed["escalate_to_human"], bool)` — confirms the field is a true Python boolean, not the *string* `"true"` (a common LLM output quirk).
- The function returns a **tuple** `(True/False, data-or-error)` so the calling code can decide: if `False`, trigger the **retry logic** from Unit 13 (ask the model again, or escalate to a human).

**Best Practices:**

- Always validate AI-generated JSON before using it in your application — never trust it blindly.
- Keep the system prompt's `[METADATA]` schema and your Python validation function perfectly in sync — if you add a field to one, update the other.
- Write your specification (3.1) *before* writing any prompt or code — code written before a spec tends to drift from what was actually needed.

**Common Beginner Mistakes:**

- Skipping the 1-page specification and jumping straight to prompting — this almost always leads to a system nobody can evaluate later.
- Letting the AI "look up" order status from its own knowledge instead of feeding it the deterministic fact.
- Forgetting to validate JSON output, then having the whole application crash when the model occasionally adds extra commentary around the JSON.

---

## 4. Real World Application

- **FinTech:** A UPI dispute-resolution assistant follows this exact pattern — deterministic transaction facts fed in, AI only handles phrasing and categorisation, JSON output validated before any customer-facing action.
- **Healthcare:** A symptom-triage intake assistant uses a 1-page spec to bound exactly which symptoms it can discuss, with mandatory escalation for anything serious — mirroring SahayakBot's `escalate_to_human` field.
- **E-commerce / Food Delivery:** This is literally the SahayakBot pattern — most real Indian food-delivery and e-commerce apps run AI-assisted support layers with this deterministic-fact + AI-phrasing + validated-JSON structure.
- **Education:** An AI teaching assistant answering "what's my assignment deadline?" pulls the deterministic date from the LMS database, with the AI only handling friendly phrasing — never inventing a deadline.
- **Vernacular AI:** SahayakBot's Hindi/English handling reflects real production systems used across Indian language-support tools, where the constraint "reply in the same language as the customer" is a critical, testable requirement.

---

## 5. Worked Example

**End-to-end walkthrough for a single SahayakBot request:**

1. **Customer sends:** `"Mera order kahan hai? Order ID ORD1001"` (Hindi: "Where is my order?")
2. **Python extracts** `order_id = "ORD1001"` and calls `get_order_status("ORD1001")` → returns `{"status": "Out for delivery", "eta_minutes": 20}` (deterministic fact).
3. **`build_user_message`** constructs: `"Customer message: Mera order kahan hai?\nOrder status from database: {'status': 'Out for delivery', 'eta_minutes': 20}"`.
4. **`call_sahayakbot`** sends this, plus the 5-role system prompt, to Claude via `client.messages.create(...)`.
5. **Claude replies (raw text):**
   `{"reply_text": "Aapka order abhi delivery ke liye nikal chuka hai, aur 20 minute mein pahunch jayega!", "category": "order_status", "escalate_to_human": false}`
6. **`validate_sahayakbot_response`** parses this JSON, confirms all 3 keys exist, confirms `"order_status"` is a valid category, and confirms `escalate_to_human` is a real boolean → returns `(True, parsed_dict)`.
7. **Final action:** Since validation passed and `escalate_to_human` is `false`, the Python orchestration layer sends `parsed["reply_text"]` directly back to the customer's chat window. If validation had failed, or `escalate_to_human` were `true`, the message would instead be queued for a human agent.

This single flow demonstrates every piece from this topic working together: specification → deterministic data → prompt-engineered AI call → validated structured output → a safe final action.

---

## 6. Key Takeaways

- A capstone project always starts with a **problem statement** and a **1-page specification** — never with code or a prompt.
- The **Python orchestration layer** is the deterministic "glue" that prepares inputs, calls the AI, and handles outputs — the AI never runs on its own.
- A well-built system prompt uses all **5 roles** (Authority, Exemplar, Constraint, Rubric, Metadata) to make AI behaviour as reliable as possible.
- **Never let the AI guess a fact a database already knows** — feed deterministic facts into the prompt; let the AI only handle phrasing, classification, and judgment calls.
- **Structured JSON output must always be validated in Python** before your application trusts or acts on it.
- `escalate_to_human` (or an equivalent flag) is how you encode the Judgment Framework's human-override point (Unit 9) directly into your system's design.
- **Interview tip:** Being able to explain *why* you separated deterministic facts from AI-generated phrasing in your capstone is one of the strongest signals of AI-native engineering maturity.
- This topic is Part 1 of the capstone — Topic 2 covers testing, evaluation, and red-teaming this same SahayakBot system; Topic 3 covers presenting it.

---

## 7. Reference Links

- [Anthropic Documentation — Messages API](https://docs.claude.com/) — official reference for `client.messages.create()`, system prompts, and response structure (builds on Units 12–13).
- [Anthropic Documentation — Prompt Engineering Guide](https://docs.claude.com/) — official guidance on structuring system prompts (builds on Unit 13's 5-Role Framework).
- [Python Official Docs — json module](https://docs.python.org/3/library/json.html) — for `json.loads` and JSON validation patterns (builds on Unit 12).
- [GeeksforGeeks — Writing a Software Requirements Specification](https://www.geeksforgeeks.org/) — supplementary reading on specification writing (builds on Unit 2).
