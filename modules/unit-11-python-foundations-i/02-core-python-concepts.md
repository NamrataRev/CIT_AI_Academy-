# Unit 11 — Python Foundations I
## Topic 2: Core Python Concepts

*(Covers: Variables — naming and storing values · Data types — string, integer, float, boolean · If / else — writing decision logic in code · For loops — repeating an action across a list)*

---

## 1. Learning Objectives

By the end of this topic, you will be able to:

1. **Explain** what a variable is and why programs need a way to store values.
2. **Differentiate** between the four basic Python data types: string, integer, float, and boolean.
3. **Implement** decision logic in Python using `if` / `elif` / `else` statements.
4. **Implement** a `for` loop to repeat an action across every item in a list.
5. **Debug** simple beginner mistakes involving indentation, data types, and comparison operators.
6. **Create** a short Python program that combines variables, data types, conditions, and a loop to solve a small real-world problem.

---

## 2. Overview

In the previous topic, you ran your very first line of Python code inside Google Colab. Now we build the four foundational building blocks that every Python program — no matter how advanced — is made of: **variables** (storing information), **data types** (the different kinds of information you can store), **if/else** (making decisions), and **for loops** (repeating actions).

These four concepts are not just "beginner topics" you outgrow — they are the vocabulary you will use every single day as an AI-native engineer. When you write orchestration code around an AI model (starting Week 12), you will use variables to hold the AI's response, data types to know whether you got text or a number back, `if/else` to check whether the response passed validation, and `for` loops to process multiple AI responses one after another. Mastering these four basics thoroughly now means everything after this topic will feel like combining familiar Lego blocks, rather than learning something new each time.

By the end of this topic, you will be able to read and write small Python programs that store data, check conditions, and repeat steps — the exact same three ingredients found inside almost every real piece of software you use daily, from a UPI app's transaction limit check to a railway booking system's seat availability loop.

---

## 3. Description

### 3.1 Variables — Naming and Storing Values

**Definition:** A **variable** is a named location in the computer's memory where you store a value, so you can refer to that value later using its name instead of retyping it.

Think of a variable like a **labelled steel box** you'd use at home to store rice, sugar, or dal — the box has a label (the variable name) and something stored inside it (the value). You don't need to know exactly where in the kitchen the box physically sits; you just ask for "the sugar box" and get what's inside.

**Syntax:**

```python
age = 20
```

Explained symbol by symbol:
- `age` — the **variable name**. You choose this name; it should describe what it holds. Variable names in Python can contain letters, numbers, and underscores, but cannot start with a number, and cannot contain spaces.
- `=` — the **assignment operator**. This does *not* mean "equals" the way it does in mathematics. It means "take the value on the right, and store it in the variable named on the left." Read `age = 20` as "age **is assigned** 20," not "age equals 20."
- `20` — the **value** being stored.

Once this line runs, you can use `age` anywhere later in your code, and Python will substitute in the value `20`.

**Rules for naming variables:**

1. Names are case-sensitive: `Age` and `age` are two *different* variables.
2. Use descriptive names: `student_marks` is far better than `x` or `sm`.
3. By convention, Python variable names use lowercase words separated by underscores (called **snake_case**), e.g., `total_amount`, `is_valid`.
4. Cannot be a Python **reserved word** (a word Python already uses for something else, like `print`, `if`, or `for`).

### 3.2 Data Types — String, Integer, Float, Boolean

Every value stored in a variable has a **data type** — it tells Python (and you) what *kind* of value it is, and therefore what operations are valid on it. Python has many data types, but four are essential starting points:

| Data Type | Python Name | What It Stores | Example |
|---|---|---|---|
| **String** | `str` | Text — any sequence of characters, wrapped in quotes | `name = "Rahul"` |
| **Integer** | `int` | Whole numbers, positive or negative, no decimal point | `age = 20` |
| **Float** | `float` | Numbers with a decimal point | `price = 49.99` |
| **Boolean** | `bool` | Only two possible values: `True` or `False` | `is_student = True` |

You can check any variable's data type using the built-in `type()` function:

```python
name = "Rahul"
age = 20
price = 49.99
is_student = True

print(type(name))        # <class 'str'>
print(type(age))         # <class 'int'>
print(type(price))       # <class 'float'>
print(type(is_student))  # <class 'bool'>
```

**Line-by-line explanation:** Each `print(type(...))` line first evaluates `type(variable_name)` — which asks Python, "what data type is stored in this variable?" — and then `print()` displays the answer. The `#` comments after each line show you the expected output for that specific line (a common convention used in learning materials and code reviews).

> **Important Note:** `age = 20` (an integer) and `age = "20"` (a string) look almost identical but behave very differently. `20 + 5` gives `25` (mathematical addition), but `"20" + "5"` gives `"205"` (joining two pieces of text together, called **string concatenation**). This is one of the most common beginner mistakes — mixing up a *number* with *text that looks like a number*.

### 3.3 If / Else — Writing Decision Logic in Code

**Definition:** An `if` statement lets your program **make a decision** — run one block of code if a condition is true, and (optionally) a different block if it is false.

**Syntax:**

```python
amount = 6000

if amount > 5000:
    print("Transaction needs additional verification.")
else:
    print("Transaction approved.")
```

Explained symbol by symbol:
- `if` — a Python **keyword** (a reserved word with special meaning) that starts a conditional check.
- `amount > 5000` — the **condition** being tested. `>` is a **comparison operator** meaning "greater than." Python evaluates this condition and gets a boolean result: `True` or `False`.
- `:` (colon) — required immediately after the condition. It tells Python "the indented block below belongs to this `if`."
- **Indentation** — the line `print("Transaction needs additional verification.")` is indented (pushed in, usually by 4 spaces). This indentation is **not optional decoration** — in Python, indentation is how the language knows which lines belong "inside" the `if`. If you remove the indentation, Python will raise an error, because it no longer knows this line belongs to the `if` block.
- `else:` — runs its indented block only when the `if` condition was `False`.

Since `amount` is `6000`, and `6000 > 5000` evaluates to `True`, the output is:

```
Transaction needs additional verification.
```

**Adding more conditions with `elif`:**

```python
marks = 32

if marks >= 90:
    print("Grade: A")
elif marks >= 60:
    print("Grade: B")
elif marks >= 35:
    print("Grade: C")
else:
    print("Grade: Fail")
```

`elif` (short for "else if") lets you check additional conditions in sequence. Python checks each condition from top to bottom and runs the block for the **first** one that is `True`, then skips the rest. Here, `marks` is `32`: `32 >= 90` is `False`, `32 >= 60` is `False`, `32 >= 35` is `False`, so Python falls through to `else`, printing:

```
Grade: Fail
```

**Common comparison operators:**

| Operator | Meaning |
|---|---|
| `==` | equal to (note: two equal signs — one `=` means *assignment*, two `==` means *comparison*) |
| `!=` | not equal to |
| `>` , `<` | greater than, less than |
| `>=` , `<=` | greater than or equal to, less than or equal to |

### 3.4 For Loops — Repeating an Action Across a List

First, a new data structure: a **list** is an ordered collection of values, written inside square brackets `[ ]`, separated by commas.

```python
marks = [78, 45, 32, 91, 60]
```

Here, `marks` is a list holding five integer values.

**Definition:** A `for` loop lets you repeat a block of code **once for every item** in a list (or any other sequence), without writing that code out five separate times.

**Syntax:**

```python
marks = [78, 45, 32, 91, 60]

for mark in marks:
    print(mark)
```

Explained symbol by symbol:
- `for` and `in` — Python keywords that together mean "for each item in this list, do the following."
- `mark` — a **temporary variable** you choose, which holds one item from the list at a time, on each pass through the loop. (It is not the list itself — it is one single value from it.)
- `marks` — the list being looped over.
- `:` and indentation — exactly as with `if`, the colon and the indented block define what code repeats on every pass.

Python runs the indented block once for each value in `marks`, in order. The output is:

```
78
45
32
91
60
```

**A more useful example — computing the class average:**

```python
marks = [78, 45, 32, 91, 60]
total = 0

for mark in marks:
    total = total + mark

average = total / len(marks)
print("Class average is:", average)
```

Explained:
- `total = 0` — a variable created *before* the loop starts, to accumulate a running sum. It must start at `0` so the first addition works correctly.
- `total = total + mark` — on each pass of the loop, this takes the *current* value of `total`, adds the current `mark`, and stores the new sum back into `total`. After all five passes: `total` becomes `78+45+32+91+60 = 306`.
- `len(marks)` — `len()` is a built-in function that returns how many items are in a list; here, `5`.
- `average = total / len(marks)` — `/` is the division operator; `306 / 5 = 61.2`.
- Final output: `Class average is: 61.2`

**Best Practices:**

- Always use meaningful variable names (`total`, `average`) instead of single letters, especially once code gets longer than a few lines.
- Initialise "accumulator" variables (like `total = 0`) *before* a loop, never inside it — otherwise it resets every pass.
- Keep indentation consistent — mixing tabs and spaces, or using inconsistent numbers of spaces, is a very common source of errors for beginners.

**Common Beginner Mistakes:**

- Using `=` when you mean `==` (assignment vs comparison) inside an `if` condition.
- Forgetting the colon `:` at the end of an `if`, `elif`, `else`, or `for` line.
- Forgetting to indent the block under `if`/`for`, or indenting inconsistently.
- Confusing a string that looks like a number (`"20"`) with an actual number (`20`).

---

## 4. Real World Application

- **Banking / UPI:** An `if` check like `if amount > daily_limit:` is exactly how real transaction systems flag payments needing extra verification — this is deterministic logic (Unit 1), and it is precisely the kind of check that must never be left to a probabilistic AI model alone.
- **Railway Booking:** A `for` loop over a list of available berths checks each one in turn to find the first open seat matching a passenger's preference.
- **E-commerce:** Looping over a shopping cart (a list of items) to calculate the total bill, applying an `if` check for whether a discount coupon condition is met.
- **Education / EdTech:** Computing a class average or looping through a list of student submissions to flag any score below a pass threshold — the exact example used above.
- **AI-native systems (preview of Week 12+):** Once you start calling Claude from Python, you will use `if` to check whether the AI's response is valid JSON before using it, and `for` loops to process a list of multiple AI-generated outputs (e.g., checking five different customer queries one by one).

---

## 5. Worked Example

**Specification:** "Given a list of UPI transaction amounts, print whether each one is 'Approved' (₹5,000 or below) or 'Needs Verification' (above ₹5,000), then print the total amount across all transactions."

```python
transactions = [1200, 5000, 7500, 3000, 9999]
total = 0

for amount in transactions:
    if amount > 5000:
        print(amount, "-> Needs Verification")
    else:
        print(amount, "-> Approved")
    total = total + amount

print("Total amount processed:", total)
```

**Expected output:**

```
1200 -> Approved
5000 -> Approved
7500 -> Needs Verification
3000 -> Approved
9999 -> Needs Verification
Total amount processed: 26699
```

**Line-by-line explanation:**

- `transactions = [1200, 5000, 7500, 3000, 9999]` — a list of five integers.
- `total = 0` — accumulator variable, initialised before the loop.
- `for amount in transactions:` — loop variable `amount` takes each value in turn: `1200`, then `5000`, then `7500`, and so on.
- `if amount > 5000:` — note `5000` itself is **not** greater than `5000`, so it correctly falls to `else` and prints "Approved" — this is why we use `>` and not `>=` here, matching the specification exactly ("above ₹5,000").
- `print(amount, "-> Needs Verification")` / `print(amount, "-> Approved")` — prints the current amount followed by its classification, on one line, automatically space-separated by `print`.
- `total = total + amount` — runs on *every* pass of the loop (it is not indented under the `if`/`else`, so it always executes, adding the current amount regardless of its classification), accumulating the grand total: `1200+5000+7500+3000+9999 = 26699`.
- The final `print("Total amount processed:", total)` runs once, after the loop finishes (notice it is *not* indented — it sits outside the `for` block).

**Try it yourself:** Add one more transaction amount to the list, and predict the new total *before* running the code — then run it in Colab to check your prediction.

---

## 6. Key Takeaways

- A **variable** is a named box that stores a value; `=` assigns a value, it does not mean mathematical equality.
- Python's four foundational data types: **string** (`str`, text), **integer** (`int`, whole numbers), **float** (`float`, decimal numbers), and **boolean** (`bool`, `True`/`False`).
- `"20"` (string) and `20` (integer) are *not* the same — mixing them up is one of the most common beginner bugs.
- `if` / `elif` / `else` lets your program make decisions; the condition must end in `:` and the block underneath must be indented.
- `==` compares for equality; `=` assigns a value — never confuse the two.
- A **list** (`[ ]`) holds an ordered collection of values; a `for` loop repeats a block of code once for every item in a list.
- Accumulator variables (like a running `total`) must be initialised *before* the loop starts.
- **Interview tip:** Be ready to explain, out loud, exactly what each line of a short `for`/`if` program does — interviewers for entry-level roles frequently ask you to "trace through" code line by line.
- Indentation is not cosmetic in Python — it is part of the language's syntax and determines which lines belong to which block.

---

## 7. Reference Links

- [Python Official Documentation — Data Structures](https://docs.python.org/3/tutorial/datastructures.html) — official reference on lists and related structures.
- [Python Official Documentation — More Control Flow Tools](https://docs.python.org/3/tutorial/controlflow.html) — official reference on `if` and `for`.
- [W3Schools — Python Variables](https://www.w3schools.com/python/python_variables.asp) and [Python If...Else](https://www.w3schools.com/python/python_conditions.asp) — beginner-friendly supplementary reading.
- [GeeksforGeeks — Loops in Python](https://www.geeksforgeeks.org/loops-in-python/) — supplementary reading with additional practice examples.
