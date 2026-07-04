<div align="center">

# 🐍 Day 3 — If/Else & Logic Building

![Day](https://img.shields.io/badge/Day-3-blue?style=for-the-badge)
![Phase](https://img.shields.io/badge/Phase-1%20Foundations-green?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Complete-brightgreen?style=for-the-badge)

> *"Logic is the foundation of every security decision a machine makes."*

[← Previous Day](../day-02-operators-typecasting/) • [🏠 Home](../README.md) • [Next Day →](../day-04-loops/)

</div>

---

## 📋 Overview

| | |
|---|---|
| 📅 **Date** | July 2026 |
| 🎯 **Goal** | Build decision-making logic using conditions |
| 📦 **Files** | 6 Python files |
| ✅ **Status** | Complete |

---

## 🧠 What I Learned Today

- `if/elif/else` — how Python makes decisions
- Nested conditions — if inside if inside else
- Logical operators in conditions — `and`, `or`, `not`
- Input validation — always handle invalid user input
- Slab-based calculation — real-world billing logic
- Login authentication system structure
- Leap year logic using combined conditions

---

## 📁 File Structure

```
day-03-if-else-logic/
│
├── 📄 conditions.py          ← positive, negative, zero checker
├── 📄 login_system.py        ← username + password authentication
├── 📄 grade_calculator.py    ← marks to grade with validation
├── 📄 electricity_bill.py    ← slab-based bill calculation
├── 📄 leap_year.py           ← leap year logic
├── 📄 atm_machine.py         ← ATM simulator with PIN + balance
├── 📄 Debugging.py           ← 5 syntax errors found and fixed
└── 📄 README.md
```

---

## 💡 Key Concepts

### If/Elif/Else Structure
```python
if condition:           # runs if True
    # code
elif other_condition:   # runs if first False, this True
    # code
else:                   # runs if ALL above False
    # code
```

### Nested Conditions
```python
if username == correct_username:
    if password == correct_password:
        print("Login Successful")
    else:
        print("Wrong password")     # correct user, wrong pass
else:
    print("Username not found")
```

### Slab-Based Calculation
> This is how REAL electricity boards in India calculate bills

```python
units = int(input("Enter units: "))

if units <= 100:
    bill = units * 2                              # ₹2/unit
elif units <= 200:
    bill = (100 * 2) + ((units - 100) * 3)       # ₹3 for extra
else:
    bill = (100 * 2) + (100 * 3) + ((units - 200) * 5)  # ₹5 for extra

print("Total Bill: ₹", bill)
```

### Leap Year Logic
```python
year = int(input("Enter year: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(year, "is a leap year")
else:
    print(year, "is not a leap year")
```

---

## 🏋️ Exercises Completed

| # | Exercise | Concept Practiced | Status |
|---|----------|-------------------|--------|
| 1 | Positive/Negative/Zero checker | Basic if/elif/else | ✅ |
| 2 | Login authentication system | Nested conditions | ✅ |
| 3 | Grade calculator with validation | elif chain + input validation | ✅ |
| 4 | Electricity bill slab calculator | Real-world logic | ✅ |
| 5 | Leap year checker | Combined conditions | ✅ |

---

## 🔨 Mini Project — ATM Machine

**What it does:**
Full ATM simulator with PIN verification,
balance checking, and withdrawal logic

```python
balance = 10000
pin     = input("Enter your PIN: ")

if pin != "1234":
    print("Invalid PIN — access denied")
else:
    amount = int(input("Enter amount to withdraw: "))

    if amount <= 0:
        print("Invalid amount")
    elif amount > balance:
        print("Insufficient balance")
    else:
        balance -= amount
        print("Successfully withdrawn ₹", amount)
        print("Remaining balance: ₹", balance)
```

**Sample Output:**
```
Enter your PIN: 1234
Enter amount to withdraw: 2000
Successfully withdrawn ₹ 2000
Remaining balance: ₹ 8000
```

---

## 🐛 Debugging Practice

5 errors found and fixed:

| # | Bug | Fix |
|---|-----|-----|
| 1 | Missing `)` in `int(input("Enter age: ")` | Added closing `)` |
| 2 | Missing `:` after `if age > 18` | Added `:` |
| 3 | `Else:` capital E | Changed to `else:` |
| 4 | Missing `:` after final `else` | Added `:` |
| 5 | Wrong indentation in nested block | Fixed 4-space indent |

---

## ❓ Interview Questions

**Q1: Difference between `=` and `==`?**
> `=` assigns a value to a variable.
> `==` compares two values and returns True or False.
> Using `=` inside a condition causes a SyntaxError.

**Q2: Can you have `if` without `else`?**
> Yes — if the condition is False, nothing happens
> and the program continues normally.

**Q3: If multiple elif conditions are True, which one runs?**
> Only the FIRST matching elif runs. Python exits the
> entire if/elif chain after finding the first match.

---

## ❌ Mistakes I Made

```python
# WRONG — missing wrong password case (silent failure)
if username == correct_username:
    if password == correct_password:
        print("Login Successful")
    # nothing for wrong password — silent failure
else:
    print("Invalid credentials")

# CORRECT — handle every case
if username == correct_username:
    if password == correct_password:
        print("Login Successful")
    else:
        print("Wrong password")   # ← handle this case
else:
    print("Username not found")

# WRONG — flat rate instead of slab
bill = units * 3    # charges ALL units at ₹3

# CORRECT — slab calculation
bill = (100 * 2) + ((units - 100) * 3)
```

---

## 🔐 Hacker Application

```python
# Port risk classifier — core logic of Nmap
port = int(input("Enter port: "))

if port == 22:
    print("SSH — Remote access — HIGH RISK if open")
elif port == 21:
    print("FTP — Unencrypted — HIGH RISK")
elif port == 80:
    print("HTTP — Check for web vulnerabilities")
elif port == 443:
    print("HTTPS — Check SSL certificate")
elif port == 3306:
    print("MySQL — CRITICAL if exposed publicly")
elif port == 6379:
    print("Redis — Often misconfigured, no auth")
else:
    print("Unknown port — manual investigation needed")
```

This exact if/elif logic is inside Nmap's service detection.
Every port scanner you will build in Month 3 uses this pattern.

---

## 📊 Day Score

| Category | Score |
|----------|-------|
| Exercises | 4/5 |
| Debug Fix (5 errors) | ✅ |
| Mini Project | ✅ |
| Interview Qs | ✅ |
| GitHub Push | ✅ |
| **Total** | **7.5/10** |

---

<div align="center">

**[← Previous Day](../day-02-operators-typecasting/)** • **[🏠 Back to Home](../README.md)** • **[Next Day →](../day-04-loops/)**

*Part of [Python for Ethical Hacking — 4 Month Journey](../README.md)*

</div>
