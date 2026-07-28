# Unit 12 — Python Foundations II + Calling an LLM
## Topic 1: Functions and Data Structures

*(Covers: Functions — named, reusable blocks of logic · Parameters and return values · One function = one job · Lists · Dictionaries)*

---

## 1. Learning Objectives

By the end of this topic, you will be able to:

1. **Explain** what a function is and why breaking code into functions makes programs easier to read, test, and reuse.
2. **Implement** Python functions that accept parameters and return values.
3. **Describe** the "one function = one job" principle and identify when a function is trying to do too much.
4. **Implement** lists to store and iterate over multiple related values.
5. **Implement** dictionaries to store structured, key-value data.
6. **Differentiate** between when to use a list versus when to use a dictionary for a given problem.

---

## 2. Overview

In Unit 11, you learned to write single, straight-line pieces of logic — variables, `if`/`else` decisions, and `for` loops that repeat an action. But real programs are rarely just one long list of instructions from top to bottom. As soon as your logic needs to be *reused* (used more than once, perhaps with different numbers each time) or needs to work on a *collection* of things (not just one exam mark, but all 30 students' marks), you need two new building blocks: **functions** (reusable blocks of logic) and **data structures** like **lists** and **dictionaries** (containers that hold many pieces of data together in one place).

This matters enormously for AI-native engineering. When you build a system around an AI model, you will almost never write one giant block of code. Instead, you will write small functions — one to build a prompt, one to call the AI, one to validate the AI's response — and you will store data (a batch of customer questions, a set of test cases, a user's chat history) in lists and dictionaries. In fact, in the very next topic of this unit, you will write a function that builds a prompt and pass it, later, to a function that calls the Anthropic API. Getting comfortable with functions, lists, and dictionaries here is what makes Topic 3 (Calling an LLM from Python) readable instead of overwhelming.

This is also where the "one function = one job" discipline enters your professional habits — the same discipline experienced AI-native engineers use to keep AI-powered systems debuggable: if each function does exactly one clearly named thing, then when something goes wrong, you know exactly which piece to inspect.

---

## 3. Description

### 3.1 Functions — Named, Reusable Blocks of Logic

**Definition:** A **function** is a named block of code that performs a specific task, which you can run ("call") whenever you need that task done — without rewriting the code each time.

**Why this concept exists:** Imagine you need to calculate the UPI transaction fee for 50 different payments in your program. Without functions, you would have to copy-paste the same fee-calculation formula 50 times. If the fee formula ever changes (say, the bank updates its charges), you'd have to find and fix it in 50 places — a recipe for mistakes. A function lets you write the formula **once**, give it a name, and call that name as many times as you like.

**Syntax, explained keyword by keyword:**

```python
def calculate_upi_fee(amount):
    fee = amount * 0.001   # 0.1% transaction fee
    return fee
```

- `def` — a Python **keyword** that means "I am about to define a function." Every function definition starts with `def`.
- `calculate_upi_fee` — the **name** you are giving this function. Just like a variable name, it should describe what the function does. Python convention (called `snake_case`) uses lowercase words joined with underscores.
- `(amount)` — the **parameter list**, in round brackets. `amount` is a **parameter**: a placeholder name for the value the function expects to receive when it is called. Parameters let the same function work on *different* inputs each time.
- `:` — the colon tells Python "the function's block of instructions starts now."
- The next lines are **indented** (usually 4 spaces). Indentation is not decoration in Python — it is how Python knows which lines belong *inside* the function. As soon as a line is no longer indented, Python knows the function has ended.
- `fee = amount * 0.001` — a normal calculation, just like you learned in Unit 11, but now it uses the parameter `amount` instead of a fixed number.
- `return fee` — the **`return`** keyword sends the calculated value back out of the function to wherever the function was called from. Without `return`, the function would do the calculation but give you nothing back to use.

**Calling the function:**

```python
fee1 = calculate_upi_fee(2000)
fee2 = calculate_upi_fee(500)
print(fee1)   # Output: 2.0
print(fee2)   # Output: 0.5
```

Each **call** — `calculate_upi_fee(2000)` — runs the function's code with `amount` set to `2000` for that run only. This is the essence of *reusability*: one definition, many calls, each with its own input.

---

### 3.2 Parameters and Return Values

**Definition:** A **parameter** is the named placeholder in a function's definition for a value it expects to receive. An **argument** is the actual value you pass in when you call the function. The **return value** is the result the function hands back after it finishes.

| Term | Where it appears | Example |
|---|---|---|
| Parameter | In the function's `def` line | `def calculate_upi_fee(amount):` → `amount` is the parameter |
| Argument | In the function call | `calculate_upi_fee(2000)` → `2000` is the argument |
| Return value | Produced by `return` | `2.0` is what comes back from `calculate_upi_fee(2000)` |

A function can take **more than one parameter**, separated by commas:

```python
def calculate_total_bill(item_total, delivery_fee, gst_percent):
    gst_amount = item_total * (gst_percent / 100)
    total = item_total + delivery_fee + gst_amount
    return total

bill = calculate_total_bill(500, 40, 5)
print(bill)   # Output: 565.0
```

Here, `500` maps to `item_total`, `40` maps to `delivery_fee`, and `5` maps to `gst_percent` — Python matches arguments to parameters **in order**, left to right.

> **Important Note:** A function that has no `return` statement still runs perfectly, but it silently gives back a special value called `None` (Python's way of saying "nothing"). This is a very common beginner mistake — writing a function, forgetting `return`, and then being confused why `print(my_function())` shows `None`.

---

### 3.3 One Function = One Job (The Testable Unit Principle)

**Definition:** A well-designed function should do **exactly one clearly describable thing** — not several unrelated things bundled together.

**Why this rule exists:** If a function calculates a bill *and* prints a receipt *and* sends an SMS notification all at once, and something goes wrong, you cannot easily tell which of the three jobs failed. But if you split it into three small functions — `calculate_bill()`, `print_receipt()`, `send_sms()` — you can test and fix each one independently. This is exactly how you will later build and evaluate AI-powered systems: one function to build a prompt, a separate function to call the AI, a separate function to check the AI's answer — each piece independently "testable."

**A simple test to check yourself:** Can you describe what the function does in **one short sentence**, without using the word "and"? If you need "and," it's probably doing more than one job.

```python
# ❌ Doing too much in one function
def process_order(item_total, delivery_fee, gst_percent):
    total = item_total + delivery_fee + (item_total * gst_percent / 100)
    print("Your total is:", total)
    return total

# ✅ One job each — easier to test and reuse
def calculate_total(item_total, delivery_fee, gst_percent):
    return item_total + delivery_fee + (item_total * gst_percent / 100)

def display_total(total):
    print("Your total is:", total)

total = calculate_total(500, 40, 5)
display_total(total)
```

---

### 3.4 Lists — Storing and Iterating Over Multiple Values

**Definition:** A **list** is an ordered collection of values, stored under a single variable name, written inside square brackets `[ ]` with items separated by commas.

**Why this concept exists:** A single variable like `mark = 78` can hold only one exam mark. But if you have 30 students' marks, or 10 railway PNR statuses to check, you need one container that holds *all* of them together, in order, so you can process them as a group — typically with a `for` loop (from Unit 11).

```python
pnr_statuses = ["Confirmed", "Waitlisted", "Confirmed", "RAC", "Waitlisted"]

for status in pnr_statuses:
    print("Ticket status:", status)
```

- `pnr_statuses = [...]` — creates a list named `pnr_statuses` holding five text values.
- `[...]` — the square brackets mark the start and end of the list.
- Each value is separated by a comma `,`.
- `for status in pnr_statuses:` — a `for` loop (from Unit 11) that takes each item out of the list, one at a time, and temporarily names it `status` inside the loop body.

**Accessing one item by position (indexing):**

```python
print(pnr_statuses[0])   # Output: Confirmed
print(pnr_statuses[2])   # Output: Confirmed
```

> **Important Note:** Python counts list positions starting from **0**, not 1. So `pnr_statuses[0]` is the *first* item, and `pnr_statuses[2]` is the *third* item. This is one of the most common sources of beginner confusion — always double-check whether you want the 1st item (`index 0`) or the 2nd item (`index 1`).

**Useful list operations:**

| Operation | Code | What it does |
|---|---|---|
| Number of items | `len(pnr_statuses)` | Returns `5` |
| Add an item | `pnr_statuses.append("Confirmed")` | Adds to the end of the list |
| Check membership | `"RAC" in pnr_statuses` | Returns `True` |

---

### 3.5 Dictionaries — Key-Value Pairs for Structured Data

**Definition:** A **dictionary** is a collection of data stored as **key-value pairs**, written inside curly brackets `{ }`, where each unique **key** points to a **value** — like a real dictionary where each word (key) has a meaning (value).

**Why this concept exists:** A list is great for a simple sequence of similar items, but it doesn't *label* what each value means. If you have a student's data — name, roll number, and marks in three subjects — a dictionary lets you label each piece clearly, instead of just remembering "the third item in the list is the maths mark."

```python
student = {
    "name": "Priya",
    "roll_number": 21,
    "marks": {"maths": 88, "science": 91, "english": 79}
}

print(student["name"])              # Output: Priya
print(student["marks"]["science"])  # Output: 91
```

- `student = { ... }` — creates a dictionary named `student`.
- `"name": "Priya"` — a **key-value pair**: `"name"` is the key (like a label), `"Priya"` is the value. The colon `:` separates a key from its value.
- Keys and values are separated from the *next* pair by a comma `,`.
- `student["marks"]` is itself another dictionary (a dictionary can hold another dictionary inside it) — this is how real-world structured data (like a JSON response from an AI API, which you'll meet in Topic 3) is commonly organised.
- `student["name"]` — square brackets **with the key inside** retrieve the value for that key. This looks similar to list indexing, but here you use the **key** (a label), not a numeric position.

**Looping through a dictionary:**

```python
marks = {"maths": 88, "science": 91, "english": 79}

for subject, score in marks.items():
    print(subject, "→", score)

# Output:
# maths → 88
# science → 91
# english → 79
```

- `.items()` — a dictionary method that gives you each key-value pair together, so the loop can name them `subject` (the key) and `score` (the value) on each pass.

**Comparison Table — List vs Dictionary**

| Aspect | List | Dictionary |
|---|---|---|
| Written as | `[item1, item2, ...]` | `{key1: value1, key2: value2, ...}` |
| Access an item by | Position (index number, starting at 0) | Key (a label you choose) |
| Best used when | Order matters, items are similar in kind | You need to label *what* each value means |
| Example | List of PNR statuses | A student's profile: name, roll number, marks |

**Best Practices:**

- Use descriptive function names (`calculate_total`, not `func1`).
- Keep each function focused on one job — if you find yourself writing "and" to describe it, split it.
- Use dictionaries when your data has meaningful labels; use lists when you just have a simple sequence of similar values.

**Common Beginner Mistakes:**

- Forgetting `return` and then being surprised the function "gives nothing back" (it returns `None`).
- Mixing up list index `0` (Python starts counting from zero) with "the first item."
- Using square brackets `[ ]` for a dictionary key lookup but writing the wrong key name (this raises a `KeyError` — Python cannot find that label).
- Writing one giant function that does everything, making it hard to find bugs later.

---

## 4. Real World Application

- **Banking/FinTech:** A function `calculate_interest(principal, rate, years)` used every time a bank app needs to show projected savings — written once, reused everywhere.
- **E-commerce/Food Delivery:** A list of items in a cart (`cart_items = ["Paneer Butter Masala", "Naan", "Lassi"]`), and a dictionary storing the price of each (`prices = {"Paneer Butter Masala": 220, "Naan": 40, "Lassi": 60}`).
- **Education:** A dictionary storing a student's exam-wise marks (as shown above), used by a school's result-management portal.
- **Railway Booking Systems:** A list of PNR statuses processed in a loop to send bulk SMS updates to passengers.
- **AI-Native Engineering (forward look to Topic 3):** A function `build_prompt(user_question)` that returns a neatly formatted string, which is then handed to a separate function `call_claude(prompt)` that sends it to the Anthropic API — exactly the "one function = one job" principle in action in a real AI system.

---

## 5. Worked Example

**Scenario:** Build a small program for a food-delivery app that stores three orders, calculates each order's total (item total + delivery fee + 5% GST), and prints a clean summary.

```python
def calculate_total(item_total, delivery_fee, gst_percent):
    gst_amount = item_total * (gst_percent / 100)
    return item_total + delivery_fee + gst_amount

orders = [
    {"customer": "Ravi", "item_total": 450, "delivery_fee": 30},
    {"customer": "Meena", "item_total": 620, "delivery_fee": 0},
    {"customer": "Arjun", "item_total": 300, "delivery_fee": 25},
]

for order in orders:
    total = calculate_total(order["item_total"], order["delivery_fee"], 5)
    print(order["customer"], "needs to pay ₹", round(total, 2))
```

**Expected Output:**

```
Ravi needs to pay ₹ 502.5
Meena needs to pay ₹ 651.0
Arjun needs to pay ₹ 340.0
```

**Line-by-line explanation:**

- `def calculate_total(...)`: one function, one job — calculating a total. It takes three parameters and returns one value.
- `orders = [ {...}, {...}, {...} ]`: a **list of dictionaries** — a very common real-world pattern. Each dictionary represents one order, with clearly labelled keys (`"customer"`, `"item_total"`, `"delivery_fee"`).
- `for order in orders:`: loops through the list, giving us one order-dictionary at a time, named `order`.
- `order["item_total"]`: looks up the value stored under the key `"item_total"` inside the current order's dictionary.
- `calculate_total(order["item_total"], order["delivery_fee"], 5)`: calls our function, passing in the values pulled from the dictionary as arguments (5% GST is fixed here).
- `round(total, 2)`: rounds the result to 2 decimal places, appropriate for currency.

**Try it yourself:** Add a fourth order and a `discount_percent` parameter to `calculate_total` that reduces the item total before GST is applied.

---

## 6. Key Takeaways

- A **function** is a named, reusable block of logic, defined with `def`, that can accept **parameters** and give back a **return value**.
- Calling a function multiple times with different **arguments** avoids repeating the same code — write once, reuse everywhere.
- **One function = one job**: if you need "and" to describe what a function does, split it into smaller functions. This makes code easier to test and debug.
- A **list** (`[ ]`) is an ordered collection, best for a simple sequence of similar values, accessed by numeric **index starting at 0**.
- A **dictionary** (`{ }`) is a collection of **key-value pairs**, best when each value needs a clear label, accessed by its **key**.
- Real-world data is often a **list of dictionaries** (e.g., a list of orders, each order being a dictionary of details) — get comfortable with this pattern early.
- A function without `return` gives back `None`, not an error — a very common silent bug for beginners.
- **Interview tip:** Be ready to explain the difference between a parameter and an argument, and to justify when you'd choose a list over a dictionary (or vice-versa) for a given dataset.
- These building blocks — functions, lists, dictionaries — are exactly what you'll use in the very next topic to structure a clean, professional call to an AI model.

---

## 7. Reference Links

- [Python Official Documentation — Defining Functions](https://docs.python.org/3/tutorial/controlflow.html#defining-functions)
- [Python Official Documentation — Data Structures (Lists, Dictionaries)](https://docs.python.org/3/tutorial/datastructures.html)
- [GeeksforGeeks — Python Functions](https://www.geeksforgeeks.org/python-functions/)
- [W3Schools — Python Dictionaries](https://www.w3schools.com/python/python_dictionaries.asp)
