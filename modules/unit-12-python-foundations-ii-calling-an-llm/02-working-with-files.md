# Unit 12 — Python Foundations II + Calling an LLM
## Topic 2: Working with Files

*(Covers: Reading from a file · Writing to a file · try / except — handling errors gracefully)*

---

## 1. Learning Objectives

By the end of this topic, you will be able to:

1. **Explain** why programs need to read from and write to files, instead of only working with values typed directly into the code.
2. **Implement** Python code to open, read, and close a text file.
3. **Implement** Python code to open, write to, and close a text file.
4. **Explain** why errors happen in programs and why crashing on every error is undesirable.
5. **Implement** `try` / `except` blocks to handle errors gracefully without stopping the whole program.
6. **Debug** simple file- and error-related issues using the error messages Python provides.

---

## 2. Overview

So far, every piece of data in your programs has lived only *while the program is running* — the moment your Python program ends, all your variables, lists, and dictionaries disappear. But real software needs to **persist** data: save a list of customer questions to review later, store an evaluation log of AI responses, or read a document that a RAG system (which you'll study in Unit 14) will search through. This is exactly what **files** are for — reading data *from* a file into your program, and writing data *from* your program into a file that survives after the program stops.

Alongside this, real programs constantly meet situations that don't go as planned: a file that doesn't exist, a network call that fails, an AI API that times out. If your program crashes the instant something unexpected happens, it is not fit for real use — imagine a railway booking app crashing entirely just because one payment gateway request was slow! That is why Python gives us `try` / `except`: a way to say "attempt this action, and if something goes wrong, handle it calmly instead of crashing."

Both skills — files and `try`/`except` — are essential preparation for the very next topic, where you will call a real AI model over the internet. Network calls to AI APIs can fail (no internet, wrong key, server overloaded), and professional AI-native code always wraps such calls in `try`/`except`. Equally, storing a batch of AI-generated responses in a file, so you can evaluate them later, is a routine, everyday task for anyone building or overseeing AI systems.

---

## 3. Description

### 3.1 Reading From a File

**Definition:** Reading a file means opening it and pulling its stored content into your Python program so you can use it.

```python
file = open("customer_questions.txt", "r")
content = file.read()
print(content)
file.close()
```

- `open("customer_questions.txt", "r")` — the `open()` function opens a file. The first argument is the **file name** (assumed to be in the same folder as your program, unless you give a full path). The second argument, `"r"`, is the **mode** — `"r"` means "read mode": you only want to read the file's content, not change it.
- `file` — a variable holding a reference to the now-open file, often called a **file object** or **file handle**.
- `file.read()` — a method that reads the *entire* content of the file as one single piece of text (a string) and stores it in `content`.
- `print(content)` — displays what was read.
- `file.close()` — **closes** the file, telling the operating system you are done with it. Forgetting to close a file can, in larger programs, waste memory or even lock the file so other programs cannot use it.

**Reading line by line (very common, since most real data is organised in lines):**

```python
file = open("pnr_list.txt", "r")
for line in file:
    print("PNR:", line.strip())
file.close()
```

- `for line in file:` — Python lets you loop directly over an open file, giving you **one line at a time**.
- `line.strip()` — every line read from a file includes an invisible "new line" character (`\n`) at the end (marking where the line ends). `.strip()` removes that extra invisible character (and any stray spaces) so your output looks clean.

**A safer, more professional way — the `with` block:**

```python
with open("pnr_list.txt", "r") as file:
    for line in file:
        print("PNR:", line.strip())
```

- `with open(...) as file:` — the `with` keyword automatically closes the file for you once the indented block finishes, **even if an error happens partway through**. This is the recommended, professional way to work with files in Python, because you can never forget to call `.close()`.

---

### 3.2 Writing to a File

**Definition:** Writing to a file means taking data from your program and saving it into a file, so it persists after the program ends.

```python
with open("evaluation_log.txt", "w") as file:
    file.write("Test case 1: PASS\n")
    file.write("Test case 2: FAIL - unexpected output\n")
```

- `"w"` — **write mode**. This tells Python you want to write to the file. **Important:** `"w"` mode *replaces* the entire existing content of the file if it already exists — use it carefully.
- `file.write("...")` — writes the given text into the file. Unlike `print()`, `.write()` does **not** add a new line automatically — that's why we include `\n` (the new-line character) ourselves wherever we want a line break.

**Appending to a file (adding to the end, without erasing what's already there):**

```python
with open("evaluation_log.txt", "a") as file:
    file.write("Test case 3: PASS\n")
```

- `"a"` — **append mode**. Instead of erasing the file, new content is added to the *end* of whatever is already there.

**Comparison Table — File Modes**

| Mode | Meaning | Effect on existing content |
|---|---|---|
| `"r"` | Read | File must already exist; content is not changed |
| `"w"` | Write | **Erases** existing content, then writes fresh |
| `"a"` | Append | Keeps existing content, adds new content at the end |

---

### 3.3 try / except — Handling Errors Gracefully

**Definition:** `try` / `except` is a Python structure that lets you **attempt** a risky piece of code, and if it fails, **catch** the failure and respond calmly instead of the whole program crashing.

**Why this concept exists:** Some errors are outside your control — a file might be missing, a user might type an unexpected value, or (as you'll see in the very next topic) an AI API call might fail due to no internet connection. Without `try`/`except`, any one of these situations would stop your entire program immediately with an error message and nothing else would run.

```python
try:
    file = open("marks.txt", "r")
    content = file.read()
    file.close()
except FileNotFoundError:
    print("Sorry, the file 'marks.txt' does not exist yet.")
```

- `try:` — marks the start of the block of code you want to *attempt*. Python runs this block normally, line by line.
- `except FileNotFoundError:` — if, while running the `try` block, Python encounters the **specific error type** `FileNotFoundError` (Python's built-in error for "this file does not exist"), it immediately jumps here **instead of crashing** and runs this block.
- If no error occurs, the `except` block is simply skipped, and the program continues normally after it.

**Catching any kind of error (a safety net):**

```python
try:
    result = 10 / 0
except Exception as error:
    print("Something went wrong:", error)
```

- `Exception` — the general, "catch-all" category that covers nearly all Python errors. Using `Exception` is useful as a safety net, but where possible, it's better practice to catch the **specific** error you expect (like `FileNotFoundError`), so you don't accidentally hide a *different*, unexpected bug.
- `as error` — stores the actual error details in a variable named `error`, so you can inspect or print it.

**Important Note:** `try`/`except` is not a way to *ignore* problems — it's a way to *respond* to them sensibly (show a clear message, try again, or safely stop that one operation) instead of letting one small failure bring down an entire program.

**Best Practices:**

- Prefer the `with open(...) as file:` pattern over manually calling `.close()` — it's safer and is what professional Python code uses.
- Catch **specific** error types when you know what could go wrong (e.g., `FileNotFoundError`), and use the general `Exception` only as a last-resort safety net.
- Never leave an `except:` block empty — at minimum, print or log what happened, so failures aren't silently swallowed.

**Common Beginner Mistakes:**

- Forgetting that `"w"` mode erases existing file content — always double-check you meant to overwrite, not append.
- Forgetting to add `\n` when using `.write()`, resulting in all text running together on one line.
- Wrapping the *entire* program in one giant `try`/`except`, which makes it hard to know exactly which line failed.

---

## 4. Real World Application

- **Education:** A teacher's script reads a `.txt` or `.csv` file of student roll numbers and marks, and writes a summary report file at the end.
- **Banking/FinTech:** A batch job reads a file of pending UPI transactions each night and writes a log file recording which succeeded and which failed — wrapped in `try`/`except` so one bad record doesn't crash the entire batch.
- **Healthcare:** An AI triage script reads patient symptom notes from a file (or, in a full RAG system per Unit 14, a whole folder of documents), and safely handles the case where a file is missing or unreadable.
- **AI-Native Engineering (forward look):** Every professional call to an AI API is wrapped in `try`/`except`, because networks are unreliable — you will use exactly this pattern in the very next topic when calling the Anthropic API. Evaluation logs (a core requirement of your Week 15 capstone) are typically written to a file using the write/append patterns you just learned.

---

## 5. Worked Example

**Scenario:** Read a file of customer support questions, one per line, and write a new file recording each question along with a placeholder "processed" status — while gracefully handling the case where the input file does not exist.

```python
try:
    with open("questions.txt", "r") as input_file:
        questions = input_file.readlines()

    with open("processed_questions.txt", "w") as output_file:
        for question in questions:
            clean_question = question.strip()
            output_file.write(clean_question + " -> STATUS: Processed\n")

    print("File processed successfully.")

except FileNotFoundError:
    print("Error: 'questions.txt' was not found. Please check the file name and location.")
```

**Line-by-line explanation:**

- `try:` — everything below is attempted; if `questions.txt` is missing, we jump straight to `except FileNotFoundError:` instead of crashing.
- `input_file.readlines()` — reads the whole file and returns it as a **list**, one string per line (connecting back to Topic 1's lists).
- The second `with open(..., "w")` opens a *new* file in write mode to store the results.
- `for question in questions:` — loops through each line read earlier.
- `question.strip()` — removes the invisible newline character from the end of each line.
- `output_file.write(clean_question + " -> STATUS: Processed\n")` — builds a new line of text and writes it, adding our own `\n` so each entry appears on its own line.
- If `questions.txt` doesn't exist, `FileNotFoundError` is caught, and a clear, friendly message is shown instead of a program crash.

**Expected Output (if `questions.txt` exists with 2 lines "What is your refund policy?" and "How do I track my order?"):**

```
File processed successfully.
```

And `processed_questions.txt` will contain:

```
What is your refund policy? -> STATUS: Processed
How do I track my order? -> STATUS: Processed
```

**Try it yourself:** Delete or rename `questions.txt` and re-run the program — confirm you see the friendly error message instead of a crash.

---

## 6. Key Takeaways

- Files let your program's data **persist** beyond a single run — essential for logs, reports, and stored documents.
- `open(filename, mode)` opens a file; common modes are `"r"` (read), `"w"` (write — erases existing content), and `"a"` (append — adds to the end).
- Prefer `with open(...) as file:` over manual `open()`/`close()` — it automatically closes the file safely, even if an error occurs.
- `.read()` gets the whole file as one string; looping with `for line in file:` gets it one line at a time; `.readlines()` gets it as a list of lines.
- `.strip()` removes the invisible newline character from the end of each line read from a file.
- `try` / `except` lets your program **attempt** risky code and **respond calmly** to specific errors (like `FileNotFoundError`) instead of crashing.
- Catch **specific** error types when possible; use the general `Exception` only as a safety net, and never leave an `except` block empty.
- **Interview tip:** Be ready to explain why `"w"` mode is dangerous if used carelessly, and why `try`/`except` is essential for any code that talks to an external file, service, or API.
- This exact pattern — safe file handling plus `try`/`except` — is what makes the next topic's AI API calls robust and production-ready.

---

## 7. Reference Links

- [Python Official Documentation — Reading and Writing Files](https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files)
- [Python Official Documentation — Errors and Exceptions](https://docs.python.org/3/tutorial/errors.html)
- [GeeksforGeeks — Reading and Writing Files in Python](https://www.geeksforgeeks.org/reading-writing-text-files-python/)
- [W3Schools — Python Try Except](https://www.w3schools.com/python/python_try_except.asp)
