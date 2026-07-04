<div align="center">

# 🐍 Day 4 — Loops (for & while)

![Day](https://img.shields.io/badge/Day-4-blue?style=for-the-badge)
![Phase](https://img.shields.io/badge/Phase-1%20Foundations-green?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Complete-brightgreen?style=for-the-badge)

> *"A hacker's best friend is a loop. One script, infinite targets."*

[← Previous Day](../day-03-if-else-logic/) • [🏠 Home](../README.md) • [Next Day →](../day-05-functions/)

</div>

---

## 📋 Overview

| | |
|---|---|
| 📅 **Date** | July 2026 |
| 🎯 **Goal** | Master loops — the backbone of every automation script |
| 📦 **Files** | 6 Python files |
| ✅ **Status** | Complete |

---

## 🧠 What I Learned Today

- `for` loop — iterate over range or list, known iterations
- `while` loop — repeat until condition becomes False
- `range()` — 3 variations: basic, start/stop, with step
- `break` — exit loop completely
- `continue` — skip current iteration, keep going
- `pass` — placeholder, does nothing
- `for/else` — else runs only when loop never hit break
- Nested loops — loop inside loop for patterns
- `while True` — standard pattern for input-until-correct

---

## 📁 File Structure

```
day-04-loops/
│
├── 📄 for_loop.py            ← sum of numbers, multiplication table
├── 📄 while_loop.py          ← number guessing game
├── 📄 patterns.py            ← star pattern with nested loops
├── 📄 password_system.py     ← 3-attempt login with for/else
├── 📄 port_scanner_sim.py    ← simulated port scanner 1-1024
├── 📄 Debugging.py           ← 3 syntax errors fixed
└── 📄 README.md
```

---

## 💡 Key Concepts

### range() — 3 Ways
```python
range(5)           # 0, 1, 2, 3, 4
range(1, 6)        # 1, 2, 3, 4, 5
range(2, 10, 2)    # 2, 4, 6, 8       ← step of 2
range(10, 0, -1)   # 10, 9, 8... 1    ← countdown
```

### break vs continue
```python
# break — exits loop completely
for i in range(10):
    if i == 5:
        break           # stops — never reaches 6, 7, 8, 9
    print(i)            # prints: 0 1 2 3 4

# continue — skips current round, loop keeps going
for i in range(10):
    if i == 5:
        continue        # skips 5, continues to 6, 7, 8, 9
    print(i)            # prints: 0 1 2 3 4 6 7 8 9
```

### for/else — Advanced Pattern
```python
# else runs ONLY if break was never triggered
for i in range(3):
    password = input("Enter password: ")
    if password == "hacker123":
        print("Access granted")
        break
else:
    print("Account locked")   # runs after 3 failed attempts
```

### while True — Standard Input Loop
```python
secret   = 7
attempts = 0

while True:                          # runs forever until break
    guess    = int(input("Guess: "))
    attempts += 1
    if guess == secret:
        print("Correct in", attempts, "attempts")
        break                        # only exit point
    else:
        print("Wrong — try again")
```

### Print Inside vs Outside Loop
```python
# WRONG — prints running total at every step
for i in range(1, n+1):
    total += i
    print("Sum =", total)    # inside — prints every iteration

# CORRECT — prints final answer only
for i in range(1, n+1):
    total += i
print("Sum =", total)        # outside — prints once at end
```

---

## 🏋️ Exercises Completed

| # | Exercise | Concept Practiced | Status |
|---|----------|-------------------|--------|
| 1 | Sum of 1 to n | for loop + accumulator | ✅ |
| 2 | Multiplication table | for + range(1,11) | ✅ |
| 3 | 3-attempt password system | for/else + break | ✅ |
| 4 | Number guessing game | while True + break | ✅ |
| 5 | Star pattern | nested loops | ✅ |

---

## 🔨 Mini Project — Port Scanner Simulator

**What it does:**
Simulates scanning ports 1-1024, identifies
open ports from a predefined list, reports findings

```python
open_ports = [22, 80, 443, 3306, 8080]
count      = 0

print("Starting scan on localhost...")
print("-" * 40)

for port in range(1, 1025):
    if port in open_ports:
        print(f"[OPEN]   Port {port}")
        count += 1

print("-" * 40)
print(f"Scan complete — {count} open ports found")
```

**Sample Output:**
```
Starting scan on localhost...
----------------------------------------
[OPEN]   Port 22
[OPEN]   Port 80
[OPEN]   Port 443
[OPEN]   Port 3306
[OPEN]   Port 8080
----------------------------------------
Scan complete — 5 open ports found
```

---

## 🐛 Debugging Practice

3 errors found and fixed:

| # | Error | Fix |
|---|-------|-----|
| 1 | Missing `:` after for loop | `for i in range(1, 6):` |
| 2 | Missing `count += 1` in while loop | Added increment |
| 3 | Missing `:` after if statement | `if i == 5:` |

---

## ❓ Interview Questions

**Q1: Difference between `break` and `continue`?**
> `break` exits the loop completely — remaining iterations cancelled.
> `continue` skips only the current iteration — loop keeps running.
> break = emergency exit. continue = skip this round.

**Q2: What happens if you forget increment in while loop?**
> Condition never becomes False — infinite loop.
> Program hangs and must be stopped with Ctrl+C.

**Q3: What does `range(2, 10, 2)` generate?**
> 2, 4, 6, 8 — starts at 2, stops before 10, step of 2.

---

## ❌ Mistakes I Made

```python
# WRONG — print inside loop, shows partial results
for i in range(1, n+1):
    total += i
    print("Sum =", total)   # prints every step

# CORRECT — print outside loop
for i in range(1, n+1):
    total += i
print("Sum =", total)       # prints final answer only

# WRONG — while condition never changes
while secret == 7:          # always True — infinite loop

# CORRECT — while True with break
while True:
    guess = int(input("Guess: "))
    if guess == secret:
        break

# WRONG — range starts at 0, causes blank line in pattern
for i in range(a):          # range(5) = 0,1,2,3,4
    for j in range(i):      # range(0) = nothing

# CORRECT — range starts at 1
for i in range(1, a + 1):   # 1,2,3,4,5
    for j in range(i):      # correct star count
```

---

## 🔐 Hacker Application

```python
# Brute force password cracker — exact logic of Hydra/Medusa
wordlist = ["admin", "password", "123456", "hacker123", "root"]
target   = "hacker123"
attempts = 0

for pwd in wordlist:
    attempts += 1
    print(f"[{attempts}] Trying: {pwd}")
    if pwd == target:
        print(f"\n[+] Password cracked: {pwd}")
        print(f"[+] Attempts taken  : {attempts}")
        break
else:
    print("[-] Password not in wordlist — try larger list")
```

This is the **exact loop structure** inside Hydra, Medusa,
and every password cracking tool ever built.
Just with a file of millions of passwords instead of a list.

---

## 📊 Day Score

| Category | Score |
|----------|-------|
| Exercises | 4/5 |
| Debug Fix | ✅ |
| Mini Project | ✅ |
| Interview Qs | ✅ |
| GitHub Push | ✅ |
| **Total** | **7.5/10** |

---

<div align="center">

**[← Previous Day](../day-03-if-else-logic/)** • **[🏠 Back to Home](../README.md)** • **[Next Day →](../day-05-functions/)**

*Part of [Python for Ethical Hacking — 4 Month Journey](../README.md)*

</div>
