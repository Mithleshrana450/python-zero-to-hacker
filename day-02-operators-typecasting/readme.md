<div align="center">

# 🐍 Day 2 — Operators & Type Casting

![Day](https://img.shields.io/badge/Day-2-blue?style=for-the-badge)
![Phase](https://img.shields.io/badge/Phase-1%20Foundations-green?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Complete-brightgreen?style=for-the-badge)

> *"Operators are the weapons of a programmer. Know them all."*

[← Previous Day](../day-01-variables-io/) • [🏠 Home](../README.md) • [Next Day →](../day-03-if-else-logic/)

</div>

---

## 📋 Overview

| | |
|---|---|
| 📅 **Date** | July 2026 |
| 🎯 **Goal** | Master all Python operators and deep type casting |
| 📦 **Files** | 5 Python files |
| ✅ **Status** | Complete |

---

## 🧠 What I Learned Today

- 7 types of Python operators — Arithmetic, Comparison, Logical, Assignment, Identity, Membership, Bitwise
- Floor division `//` vs regular division `/`
- Modulus `%` — remainder operator, critical for even/odd logic
- Truthiness — why `0`, `""`, `None` are False
- Type casting deep dive — every conversion scenario
- XOR bitwise operator `^` — foundation of encryption
- Assignment shorthand — `+=`, `-=`, `*=`, `//=`

---

## 📁 File Structure

```
day-02-operators-typecasting/
│
├── 📄 arithmetic_operation.py    ← all 7 arithmetic operators
├── 📄 type_casting.py            ← str→int, float→str, bool casting
├── 📄 boolean.py                 ← truthiness of 0, 1, "", None
├── 📄 even_odd.py                ← modulus for even/odd detection
├── 📄 calculator.py              ← mini calculator with operator input
├── 📄 gst_calculator.py          ← price + 18% GST calculation
└── 📄 README.md
```

---

## 💡 Key Concepts

### 7 Types of Operators

```python
# Arithmetic
17 + 5   # 22  addition
17 - 5   # 12  subtraction
17 * 5   # 85  multiplication
17 / 5   # 3.4 division — ALWAYS returns float
17 // 5  # 3   floor division — ALWAYS returns int
17 % 5   # 2   modulus (remainder) — critical in hacking logic
17 ** 5  # 1419857  power

# Comparison — always return True or False
a == b   # equal to
a != b   # not equal
a > b    # greater than
a >= b   # greater than or equal

# Logical
and      # both must be True
or       # at least one must be True
not      # reverses bool

# Assignment shorthand
score += 50    # same as score = score + 50
score -= 30    # same as score = score - 30
score *= 2     # same as score = score * 2
```

### Floor Division vs Regular Division
```python
print(17 / 5)     # 3.4  → always float
print(17 // 5)    # 3    → always int (floors result)
print(-17 // 5)   # -4   → floors DOWN, not toward zero
```

### XOR — Hacker's Operator
```python
# XOR encrypts AND decrypts with same key
message   = 72      # ASCII value of 'H'
key       = 25
encrypted = message ^ key    # encrypt → 81
decrypted = encrypted ^ key  # decrypt → 72 (original)
# Same XOR operation reverses itself — used in real malware
```

### Truthiness
```python
bool(0)        # False — zero
bool(1)        # True  — non-zero
bool("")       # False — empty string
bool("hacker") # True  — non-empty string
bool(None)     # False — None always falsy
```

---

## 🏋️ Exercises Completed

| # | Exercise | Concept Practiced | Status |
|---|----------|-------------------|--------|
| 1 | All 7 arithmetic operations | Arithmetic operators | ✅ |
| 2 | Even/odd checker with % | Modulus operator | ✅ |
| 3 | GST calculator with input() | Type casting + math | ✅ |
| 4 | Score to 750 using 3 operators | Assignment operators | ✅ |
| 5 | Bool values with comments | Truthiness | ✅ |

---

## 🔨 Mini Project — Calculator

**What it does:**
Takes two numbers and an operator as input,
returns the correct result, handles divide by zero

```python
a  = int(input("Enter first number: "))
b  = int(input("Enter second number: "))
op = input("Enter operator (+, -, *, /): ")

if op == "+":
    print("Result:", a + b)
elif op == "-":
    print("Result:", a - b)
elif op == "*":
    print("Result:", a * b)
elif op == "/":
    if b == 0:
        print("Cannot divide by zero")
    else:
        print("Result:", a / b)
else:
    print("Invalid operator")
```

---

## 🐛 Debugging Practice

| # | Bug | Fix |
|---|-----|-----|
| 1 | `a = input()` then `a + b` | Cast both with `int()` |
| 2 | String concatenation instead of addition | `int(input())` |

---

## ❓ Interview Questions

**Q1: What is the difference between `/` and `//`?**
> `/` always returns float. `//` always returns int (floor division).
> `-17 // 5` gives `-4`, not `-3` — it floors downward.

**Q2: What does `bool("")` return and why?**
> Returns False. Python has a truthiness concept — empty containers
> and zero values are always False because they represent nothing.

**Q3: Why can't you do `"Error: " + 404`?**
> Python cannot concatenate str and int directly.
> Must cast: `"Error: " + str(404)`

---

## ❌ Mistakes I Made

```python
# WRONG — hardcoded value
price = ("249.99")   # unnecessary parentheses + not using input()

# CORRECT
price = float(input("Enter price: "))

# WRONG — jumped to answer in one step
score = 500
score += 250   # reached 750 in one operator — missed the point

# CORRECT — use multiple operators
score = 500
score += 300   # 800
score -= 100   # 700
score += 50    # 750
```

---

## 🔐 Hacker Application

```python
# Port range calculation — used in every scanner
start_port = 1
end_port   = 1024
total      = end_port - start_port + 1
print("Scanning", total, "ports")   # 1024

# Even/odd logic used in hash analysis
hash_val = int("a3f2", 16)          # hex to int
print("Even hash?" , hash_val % 2 == 0)

# XOR cipher — base of real encryption tools
def xor_encrypt(text, key):
    return ''.join(chr(ord(c) ^ key) for c in text)

encrypted = xor_encrypt("HACK", 42)
decrypted = xor_encrypt(encrypted, 42)   # same key decrypts
print(decrypted)   # HACK
```

---

## 📊 Day Score

| Category | Score |
|----------|-------|
| Exercises | 4/5 |
| Debug Fix | ✅ |
| Mini Project | ✅ |
| Interview Qs | ✅ |
| GitHub Push | ✅ |
| **Total** | **8/10** |

---

<div align="center">

**[← Previous Day](../day-01-variables-io/)** • **[🏠 Back to Home](../README.md)** • **[Next Day →](../day-03-if-else-logic/)**

*Part of [Python for Ethical Hacking — 4 Month Journey](../README.md)*

</div>
