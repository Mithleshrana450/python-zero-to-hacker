<div align="center">

# 🐍 Day 1 — Variables, Data Types & Input/Output

![Day](https://img.shields.io/badge/Day-1-blue?style=for-the-badge)
![Phase](https://img.shields.io/badge/Phase-1%20Foundations-green?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Complete-brightgreen?style=for-the-badge)

> *"Every expert was once a beginner. Every variable starts with a value."*

[🏠 Home](../README.md) • [Next Day →](../day-02-operators-typecasting/)

</div>

---

## 📋 Overview

| | |
|---|---|
| 📅 **Date** | July 2026 |
| 🎯 **Goal** | Understand how Python stores and displays data |
| 📦 **Files** | 4 Python files |
| ✅ **Status** | Complete |

---

## 🧠 What I Learned Today

- Variables — labeled boxes that store values in memory
- Python is **dynamically typed** — type is bound to value, not variable name
- Core data types — `int`, `float`, `str`, `bool`
- `input()` always returns a **string** — must cast for math
- Type casting — `int()`, `float()`, `str()`, `bool()`
- `type()` — inspect what type Python assigned to any variable
- `print()` — multiple ways to display formatted output

---

## 📁 File Structure

```
day-01-variables-io/
│
├── 📄 day01_exercise.py        ← city variable, basic exercises
├── 📄 exercise_2.py            ← addition of two numbers
├── 📄 name_age.py              ← name and age input/output
├── 📄 personal_info_card.py    ← mini project: info card
└── 📄 README.md
```

---

## 💡 Key Concepts

### Variables — Dynamic Typing
> Python figures out the type automatically — no declaration needed

```python
name     = "Mithu"    # str  — text
age      = 21         # int  — whole number
price    = 99.99      # float — decimal
is_hacker = True      # bool — True or False

# Same variable can hold different types
x = 10        # int
x = "Mithu"   # now str — Python doesn't complain
x = 3.14      # now float
```

### input() Always Returns String
> Most common beginner bug — forgetting to cast input

```python
# WRONG — tries to add string + int
age = input("Enter age: ")      # returns "21" not 21
next_year = age + 1             # TypeError: can't add str + int

# CORRECT — cast to int first
age = int(input("Enter age: ")) # now it's integer 21
next_year = age + 1             # works perfectly → 22
```

### Type Casting
> Converting between data types

```python
int("21")       # str → int    →  21
float("99.99")  # str → float  →  99.99
str(404)        # int → str    →  "404"
bool(0)         # int → bool   →  False
bool("Mithu")   # str → bool   →  True
```

### Truthiness in Python
> Every value has a boolean meaning

```python
bool(0)        # False — zero is falsy
bool(1)        # True  — non-zero is truthy
bool("")       # False — empty string is falsy
bool("hacker") # True  — non-empty is truthy
bool(None)     # False — None is always falsy
```

---

## 🏋️ Exercises Completed

| # | Exercise | Concept Practiced | Status |
|---|----------|-------------------|--------|
| 1 | Create city variable and print | Variables | ✅ |
| 2 | Add two numbers from input | input() + casting | ✅ |
| 3 | Float variable + print type | Data types | ✅ |
| 4 | Name + age → formatted output | String formatting | ✅ |
| 5 | Bool variable + print type | Boolean type | ✅ |

---

## 🔨 Mini Project — Personal Info Card

**What it does:**
Takes name, age, and favorite programming language as input
then prints a formatted personal info card

**Concepts used:**
`input()` `int()` `print()` `variables` `type casting`

```python
name     = input("Enter your name: ")
age      = int(input("Enter your age: "))
language = input("Enter your favorite language: ")

print("=========================")
print("      MY INFO CARD")
print("=========================")
print("Name    :", name)
print("Age     :", age)
print("Language:", language)
print("=========================")
```

**Sample Output:**
```
=========================
      MY INFO CARD
=========================
Name    : Mithu
Age     : 21
Language: Python
=========================
```

---

## 🐛 Debugging Practice

**Bug found and fixed:**

| # | Bug Type | What Was Wrong | How I Fixed It |
|---|----------|----------------|----------------|
| 1 | TypeError | `age = input()` then `age + 1` | Cast: `int(input())` |

```python
# WRONG
age = input("Enter your age: ")   # string "21"
next_year = age + 1               # TypeError

# CORRECT
age = int(input("Enter your age: "))  # integer 21
next_year = age + 1                   # works → 22
```

---

## ❓ Interview Questions

**Q1: Why doesn't Python require declaring variable types?**
> Python is dynamically typed — it binds types to values (objects)
> rather than variable names. The same variable can hold
> different types at different times.

**Q2: What is the tradeoff of dynamic typing?**
> Benefit: faster to write, no boilerplate declarations, flexible.
> Drawback: type errors only appear at runtime, not before.
> Large programs can have hidden bugs that static languages
> catch at compile time.

---

## ❌ Mistakes I Made

```python
# WRONG — unnecessary parentheses around string
city = ("Surat")   # not a tuple, just noise

# CORRECT
city = "Surat"

# WRONG — capital variable names
Age = 21           # looks like a class name
Language = "Python"

# CORRECT — always lowercase/snake_case for variables
age = 21
language = "Python"
```

---

## 🔐 Hacker Application

> Ethical hackers use variables constantly to store recon data

```python
# Recon data storage — real usage
target_ip    = "192.168.1.1"
target_port  = int(input("Enter target port: "))  # must be int
username     = input("Enter username to test: ")
hash_value   = "5f4dcc3b5aa765d61d8327deb882cf99"

print(f"Target  : {target_ip}:{target_port}")
print(f"Testing : {username}")
print(f"Hash    : {hash_value}")
```

**Why type casting matters in hacking:**
Port numbers must be `int` before socket connections.
`socket.connect(("192.168.1.1", "80"))` fails —
`socket.connect(("192.168.1.1", 80))` works.

---

## 📊 Day Score

| Category | Score |
|----------|-------|
| Exercises | 5/5 |
| Debug Fix | ✅ |
| Mini Project | ✅ |
| Interview Qs | ✅ |
| GitHub Push | ✅ |
| **Total** | **9/10** |

---

<div align="center">

**[🏠 Back to Home](../README.md)** • **[Next Day →](../day-02-operators-typecasting/)**

*Part of [Python for Ethical Hacking — 4 Month Journey](../README.md)*

</div>
