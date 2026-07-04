<div align="center">

# 🐍 Day 5 — Functions, Parameters, Scope & Recursion

![Day](https://img.shields.io/badge/Day-5-blue?style=for-the-badge)
![Phase](https://img.shields.io/badge/Phase-1%20Foundations-green?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Complete-brightgreen?style=for-the-badge)

> *"A hacker's toolkit is just a collection of well-named functions."*

[← Previous Day](../day-04-loops/) • [🏠 Home](../README.md) • [Next Day →](../day-06-lists-tuples/)

</div>

---

## 📋 Overview

| | |
|---|---|
| 📅 **Date** | July 2026 |
| 🎯 **Goal** | Write reusable, modular code using functions |
| 📦 **Files** | 8 Python files |
| ✅ **Status** | Complete |

---

## 🧠 What I Learned Today

- `def` — how to define and call functions
- Parameters vs arguments — placeholder vs actual value
- `return` — sending values back from functions
- Default parameters — values used when argument not passed
- Local vs global scope — where variables live and die
- `global` keyword — modifying global variables inside functions
- Recursion — function calling itself with a base case
- Lambda — one-line anonymous functions
- Single Responsibility Principle — each function does ONE job

---

## 📁 File Structure

```
day-05-functions/
│
├── 📄 basic_functions.py         ← calculate(a, b, op) — all operators
├── 📄 factorial.py               ← recursive factorial
├── 📄 recursion.py               ← recursion with comments
├── 📄 password_strength_checker.py ← Weak/Medium/Strong checker
├── 📄 ip_validator.py            ← validates IP address format
├── 📄 lambda_practice.py         ← square, is_even, to_upper
├── 📄 hacker_toolkit.py          ← banner, scan_port, username gen
├── 📄 hacker_application.py      ← modular recon tool
└── 📄 README.md
```

---

## 💡 Key Concepts

### Function Structure
```python
def function_name(parameter1, parameter2):
    # body — indented code
    return result    # sends value back to caller
```

### Parameter vs Argument
```python
def greet(name):         # name = PARAMETER (placeholder in definition)
    print("Hello", name)

greet("Mithu")           # "Mithu" = ARGUMENT (actual value when calling)
```

### return vs print
```python
# print — displays value, throws it away forever
def add(a, b):
    print(a + b)         # shown on screen, cannot be reused

result = add(10, 20)
print(result)            # None — nothing was returned

# return — sends value back so you can use it
def add(a, b):
    return a + b         # value sent back to caller

result = add(10, 20)     # result = 30
print(result * 2)        # 60 — can use it anywhere
```

### Local vs Global Scope
```python
password = "hacker123"   # GLOBAL — visible to entire file

def check():
    attempt = input("Enter: ")   # LOCAL — only inside this function
    if attempt == password:      # can READ global
        print("Correct")

check()
print(attempt)    # NameError — attempt died when function ended
```

### Recursion — How It Works
```python
def factorial(n):
    if n == 0 or n == 1:          # BASE CASE — must exist
        return 1
    return n * factorial(n - 1)  # RECURSIVE CALL

# factorial(5) unfolds as:
# 5 × factorial(4)
#     4 × factorial(3)
#         3 × factorial(2)
#             2 × factorial(1) = 1  ← base case
#             = 2 × 1 = 2
#         = 3 × 2 = 6
#     = 4 × 6 = 24
# = 5 × 24 = 120
```

### Lambda Functions
```python
square   = lambda x: x * x          # square of number
is_even  = lambda x: x % 2 == 0     # True if even
to_upper = lambda s: s.upper()       # string to uppercase

print(square(5))           # 25
print(is_even(8))          # True
print(to_upper("hello"))   # HELLO
```

---

## 🏋️ Exercises Completed

| # | Exercise | Concept Practiced | Status |
|---|----------|-------------------|--------|
| 1 | calculate(a, b, op) | Parameters + return | ✅ |
| 2 | Password strength checker | Functions + elif | ✅ |
| 3 | Recursive factorial | Recursion + base case | ✅ |
| 4 | IP address validator | Functions + string methods | ✅ |
| 5 | Lambda — square, is_even, to_upper | Lambda syntax | ✅ |

---

## 🔨 Mini Project — Hacker Toolkit

**What it does:**
4 modular functions — banner printer, port checker,
password strength checker, username generator

```python
def banner():
    print("=" * 50)
    print("     MITHU'S HACKER TOOLKIT v1.0")
    print("=" * 50)

def scan_port(port):
    open_ports = [22, 80, 443, 3306, 8080]
    return "OPEN" if port in open_ports else "CLOSED"

def check_password_strength(password):
    if len(password) < 6:
        return "Weak"
    elif len(password) <= 10:
        return "Medium"
    else:
        return "Strong"

def generate_username(first, last):
    u1 = first.lower() + "_" + last.lower()
    u2 = first.lower() + "123"
    u3 = first[0].lower() + "_" + last.lower()
    return u1, u2, u3

# Main
banner()
print("Port 80:", scan_port(80))
print("Password:", check_password_strength("abc123"))
print("Usernames:", generate_username("Mithu", "Rana"))
```

**Sample Output:**
```
==================================================
     MITHU'S HACKER TOOLKIT v1.0
==================================================
Port 80: OPEN
Password: Medium
Usernames: ('mithu_rana', 'mithu123', 'm_rana')
```

---

## 🐛 Debugging Practice

5 errors found and fixed:

| # | Error | Fix |
|---|-------|-----|
| 1 | Missing `:` after `def greet(name)` | Added `:` |
| 2 | `print("Hello" name)` missing comma | `print("Hello", name)` |
| 3 | Function returns but result not captured | Added `return` |
| 4 | `Calculate()` capital C — function not found | `calculate()` lowercase |
| 5 | Called before definition | Moved call after `def` |

---

## ❓ Interview Questions

**Q1: Difference between parameter and argument?**
> Parameter is the variable name in function definition (placeholder).
> Argument is the actual value passed when calling.
> `def scan(port)` — port is parameter.
> `scan(80)` — 80 is argument.

**Q2: Difference between local and global scope?**
> Local — variable exists only inside its function, destroyed when done.
> Global — variable accessible everywhere in the file.
> Local variables from one function are invisible to other functions.

**Q3: What does return do — what if no return?**
> return sends a value back to the caller so it can be stored and used.
> A function with no return automatically returns None.

---

## ❌ Mistakes I Made

```python
# WRONG — using if instead of elif in calculator
def calculate(a, b, op):
    if op == "+":
        return a + b
    if op == "-":      # should be elif — checks even after match
        return a - b

# CORRECT
def calculate(a, b, op):
    if op == "+":
        return a + b
    elif op == "-":    # elif stops after first match
        return a - b

# WRONG — redundant condition in password checker
elif len(password) >= 6 and len(password) <= 10:
# >= 6 is redundant — already eliminated by first if

# CORRECT
elif len(password) <= 10:   # clean — already know it's >= 6
```

---

## 🔐 Hacker Application

```python
# Modular recon tool — exact architecture of professional scanners
def get_target():
    return input("Enter target IP: ")

def scan_ports(target, ports):
    print(f"Scanning {target}...")
    found = []
    for port in ports:
        if port in [22, 21, 80, 443, 3306, 8080]:
            found.append(port)
    return found

def generate_report(target, open_ports):
    print("=" * 45)
    print("           SCAN REPORT")
    print("=" * 45)
    print(f"Target     : {target}")
    print(f"Open Ports : {open_ports}")
    print(f"Total Found: {len(open_ports)}")
    print("=" * 45)

# Main execution
target  = get_target()
results = scan_ports(target, range(1, 1025))
generate_report(target, results)
```

**Single Responsibility Principle:**
Each function does exactly ONE job.
This is how Nmap, Masscan, and every
professional security tool is architected.

**IP Validator — used in every network tool:**
```python
def is_valid_ip(ip):
    parts = ip.split(".")
    if len(parts) != 4:
        return False
    for part in parts:
        if not part.isdigit():
            return False
        if not 0 <= int(part) <= 255:
            return False
    return True
```

Bad IP = socket crash. Always validate before connecting.

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

**[← Previous Day](../day-04-loops/)** • **[🏠 Back to Home](../README.md)** • **[Next Day →](../day-06-lists-tuples/)**

*Part of [Python for Ethical Hacking — 4 Month Journey](../README.md)*

</div>
