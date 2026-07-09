<div align="center">

# 🐍 Day 8 — String Manipulation

![Day](https://img.shields.io/badge/Day-8-blue?style=for-the-badge)
![Phase](https://img.shields.io/badge/Phase-1%20Foundations-green?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Complete-brightgreen?style=for-the-badge)

> *"Every URL, password, log file, and HTTP header is a string. Own strings, own hacking."*

[← Previous Day](../day-07-dictionaries-sets/) • [🏠 Home](../README.md) • [Next Day →](../day-09-file-handling/)

</div>

---

## 📋 Overview

| | |
|---|---|
| 📅 **Date** | July 2026 |
| 🎯 **Goal** | Master string manipulation for real security tool development |
| 📦 **Files** | 7 Python files |
| ✅ **Status** | Complete |

---

## 🧠 What I Learned Today

- String indexing and slicing — same rules as lists
- Essential string methods — `upper`, `lower`, `strip`, `find`, `replace`, `split`, `join`
- String formatting — `%`, `.format()`, f-strings
- `any()` with generator expressions — professional pattern checking
- `split()` for dynamic parsing — never use hardcoded indexes
- Caesar cipher — `ord()` and `chr()` for ASCII manipulation
- `Counter` from `collections` — frequency analysis
- Common password detection — security best practice
- Log file parsing — real SIEM technique
- Why `print()` should never be assigned to a variable

---

## 📁 File Structure

```
day-08-string-manipulation/
│
├── 📄 string_basics.py              ← all string methods practice
├── 📄 url_analyzer.py               ← dynamic URL parser using split()
├── 📄 log_parser.py                 ← log file parser using split()
├── 📄 password_validator.py         ← password requirements checker
├── 📄 caesar_cipher.py              ← encode/decode with shift
├── 📄 password_strength_analyzer.py ← full analyzer with score + bar
├── 📄 debugging.py                  ← 5 errors found and fixed
└── 📄 README.md
```

---

## 💡 Key Concepts

### String Methods — Complete Reference
```python
s = "  Hello Hacker  "

# Case
s.upper()           # "  HELLO HACKER  "
s.lower()           # "  hello hacker  "
s.title()           # "  Hello Hacker  "
s.swapcase()        # "  hELLO hACKER  "

# Cleaning
s.strip()           # "Hello Hacker"    — both ends
s.lstrip()          # "Hello Hacker  "  — left only
s.rstrip()          # "  Hello Hacker"  — right only

# Searching
s.find("Hacker")    # 8  — index, returns -1 if missing
s.index("Hacker")   # 8  — index, raises ValueError if missing
s.count("l")        # 2  — occurrences
s.startswith("  H") # True
s.endswith("  ")    # True
"Hacker" in s       # True — membership

# Modifying
s.replace("Hacker", "World")   # "  Hello World  "

# Splitting and joining
"22,80,443".split(",")          # ['22', '80', '443']
"-".join(['22', '80', '443'])   # "22-80-443"
"hello world".split()           # ['hello', 'world'] — splits on whitespace

# Checking
"abc".isalpha()     # True  — only letters
"123".isdigit()     # True  — only digits
"abc123".isalnum()  # True  — letters and numbers
"  ".isspace()      # True  — only whitespace
```

### f-String Formatting — Professional Style
```python
ip      = "192.168.1.1"
port    = 80
service = "HTTP"

# Basic
print(f"Target: {ip}:{port}")

# Alignment — column formatting
print(f"{'IP':<18} {'PORT':<6} {'SERVICE'}")
print(f"{ip:<18} {port:<6} {service}")

# Number formatting
print(f"{3.14159:.2f}")     # 3.14   — 2 decimal places
print(f"{port:05d}")        # 00080  — zero padded
print(f"{score}/10")        # 8/10   — simple
```

### Dynamic Parsing — split() vs Hardcoded Index
```python
url = "https://target.com/admin/login.php?user=admin"

# WRONG — hardcoded indexes break if URL changes
protocol = url[0:5]      # only works for THIS url
domain   = url[8:14]     # breaks with different domains

# CORRECT — dynamic split() always works
protocol, rest = url.split("://")
domain         = rest.split("/")[0]
path_query     = "/" + "/".join(rest.split("/")[1:])
path, query    = path_query.split("?") if "?" in path_query else (path_query, "None")

print("Protocol:", protocol)   # https
print("Domain  :", domain)     # target.com
print("Path    :", path)       # /admin/login.php
print("Query   :", query)      # user=admin
```

### any() with Generator — Professional Pattern
```python
password = "Hello123!"

# Check if ANY character matches condition
has_upper   = any(c.isupper() for c in password)   # True
has_digit   = any(c.isdigit() for c in password)   # True
has_special = any(c in "!@#$%^&*" for c in password) # True

# isdigit() vs any(isdigit) — critical difference
"Hello123".isdigit()                        # False — ALL must be digits
any(c.isdigit() for c in "Hello123")        # True  — ANY digit exists
```

### Caesar Cipher — ASCII Manipulation
```python
def caesar_cipher(message, shift, mode):
    result = ""
    if mode.lower() == "decode":
        shift = -shift           # reverse shift for decoding
    for char in message:
        if char.isalpha():
            if char.isupper():
                # A=65, wrap within 26 uppercase letters
                new_char = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            else:
                # a=97, wrap within 26 lowercase letters
                new_char = chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            result += new_char
        else:
            result += char       # leave symbols/spaces unchanged
    return result

# ord() converts char to ASCII number
# chr() converts ASCII number back to char
# % 26 wraps around the alphabet
```

### Log Parser — Real SIEM Technique
```python
log = "2026-07-01 14:32:11 FAILED LOGIN admin 192.168.1.105"

parts      = log.split()   # split on whitespace
date       = parts[0]      # 2026-07-01
time       = parts[1]      # 14:32:11
status     = parts[2]      # FAILED
username   = parts[4]      # admin
ip_address = parts[5]      # 192.168.1.105
```

---

## 🏋️ Exercises Completed

| # | Exercise | Concept Practiced | Status |
|---|----------|-------------------|--------|
| 1 | URL analyzer | dynamic split() parsing | ✅ |
| 2 | Password validator | any() + generator + join() | ✅ Excellent |
| 3 | Log file parser | split() on whitespace | ✅ |
| 4 | Caesar cipher | ord(), chr(), % 26 | ✅ Outstanding |
| 5 | String statistics | Counter, any(), sum() | ✅ Excellent |

---

## 🔨 Mini Project — Password Strength Analyzer

**What it does:**
Full password analyzer with score out of 10,
visual strength bar, character checks,
common password detection, and improvement suggestions

```python
def analyze_password(password):
    score       = 0
    suggestions = []

    has_upper   = any(c.isupper() for c in password)
    has_lower   = any(c.islower() for c in password)
    has_digit   = any(c.isdigit() for c in password)
    has_special = any(c in "!@#$%^&*" for c in password)

    # Score based on length
    if len(password) >= 16:  score += 4
    elif len(password) >= 12: score += 3
    elif len(password) >= 8:  score += 2
    else: suggestions.append("Use at least 8 characters")

    # Score based on character types
    if has_upper:   score += 1
    if has_lower:   score += 1
    if has_digit:   score += 1
    if has_special: score += 1

    # Bonus for all types combined
    if all([has_upper, has_lower, has_digit, has_special]):
        score += 1

    # Visual bar
    bar = "█" * score + "░" * (10 - score)
    print(f"Strength: {bar} {score}/10")
```

**Sample Output:**
```
========== PASSWORD ANALYSIS ==========
Password Length : 12
Strength Score  : 8/10
Strength        : Strong
Strength Bar    : ████████░░

Character Checks
----------------
Uppercase : ✓
Lowercase : ✓
Digits    : ✓
Special   : ✓

Common Password : NO

Suggestions
-----------
Excellent password! No improvements needed.
```

---

## 🐛 Debugging Practice

5 errors found and fixed:

| # | Error | Wrong | Fix |
|---|-------|-------|-----|
| 1 | AttributeError | `url.Upper()` | `url.upper()` — methods are lowercase |
| 2 | IndexError | `parts[2]` — only 2 items | `parts[0]` — domain is index 0 |
| 3 | Logic Error | `password.isdigit()` — checks ALL chars | `any(c.isdigit() for c in password)` |
| 4 | SyntaxError | `replace("world" "hacker")` — missing comma | `replace("world", "hacker")` |
| 5 | TypeError | `"IP is: " + 192.168.1.1` — int + str | `"IP is: " + ip` — use variable |

```python
# Error 3 — most important fix
# WRONG — isdigit() needs ALL chars to be digits
if password.isdigit():            # "Hello123" → False always

# CORRECT — any() checks if AT LEAST ONE char is digit
if any(char.isdigit() for char in password):   # "Hello123" → True
```

---

## ❓ Interview Questions

**Q1: Why are strings immutable in Python?**
> Strings cannot be changed after creation — every
> operation returns a NEW string. This is for memory
> safety and performance — Python can cache and reuse
> identical strings (string interning). To "modify" a
> string you must reassign: `s = s.replace("a", "b")`

**Q2: Difference between `find()` and `index()`?**
> Both return the index of a substring.
> `find()` returns `-1` if not found — safe.
> `index()` raises `ValueError` if not found — crashes.
> Use `find()` when unsure if substring exists.
> Use `index()` when you're certain it's there.

**Q3: What does `split()` return with no arguments?**
> Splits on any whitespace (spaces, tabs, newlines)
> and removes empty strings from result.
> `"hello   world".split()` → `['hello', 'world']`
> `"hello   world".split(" ")` → `['hello', '', '', 'world']`
> No-argument split is smarter for log parsing.

---

## ❌ Mistakes I Made Today

```python
# WRONG — assigning print() result to variable
Protocol = print("Protocol:", url[0:6])
# Protocol = None — print() always returns None

# CORRECT — store value first, then print
protocol = url.split("://")[0]
print("Protocol:", protocol)

# WRONG — hardcoded slicing
domain = url[8:14]    # breaks with any different URL

# CORRECT — dynamic split
domain = url.split("://")[1].split("/")[0]

# WRONG — isdigit() checks ALL characters
if password.isdigit():     # "Hello123" → False

# CORRECT — any() checks AT LEAST ONE
if any(c.isdigit() for c in password):   # True
```

---

## 🔐 Hacker Application

```python
# Brute force detection — real SIEM log analysis
logs = [
    "2026-07-01 14:32:11 FAILED LOGIN admin 192.168.1.105",
    "2026-07-01 14:32:15 FAILED LOGIN admin 192.168.1.105",
    "2026-07-01 14:32:19 FAILED LOGIN admin 192.168.1.105",
    "2026-07-01 14:32:23 SUCCESS LOGIN admin 192.168.1.105",
    "2026-07-01 14:33:01 FAILED LOGIN root 192.168.1.200",
]

def analyze_logs(logs):
    failed = {}
    for log in logs:
        parts = log.split()
        if parts[2] == "FAILED":
            key = f"{parts[4]}@{parts[5]}"
            failed[key] = failed.get(key, 0) + 1

    print("=" * 45)
    print("  BRUTE FORCE DETECTION REPORT")
    print("=" * 45)
    for target, count in failed.items():
        alert = "⚠️ ALERT" if count >= 3 else "Normal"
        print(f"{target:<30} {count} attempts  {alert}")

analyze_logs(logs)

# Caesar cipher — used in CTF challenges constantly
# XOR is stronger but Caesar teaches the concept
# Every CTF has at least one Caesar/ROT13 challenge

# URL parameter extraction — used in web pentesting
# Burp Suite does exactly this to find injection points
url    = "https://target.com/login?user=admin&pass=1234"
params = url.split("?")[1]
for param in params.split("&"):
    key, value = param.split("=")
    print(f"Parameter: {key} = {value}")
    # Test each parameter for SQLi, XSS, etc.
```

**Real tools using string manipulation:**

| Tool | String Usage |
|------|-------------|
| Burp Suite | Parses HTTP requests/responses as strings |
| Splunk/SIEM | Splits log lines to extract fields |
| Nikto | Parses URL strings for vulnerability testing |
| SQLMap | Manipulates query string parameters |
| Hashcat | Applies rules to password strings |

---

## 📊 Day Score

| Category | Score |
|----------|-------|
| Exercise 1 — URL Analyzer | ✅ |
| Exercise 2 — Password Validator | ✅ Excellent |
| Exercise 3 — Log Parser | ✅ |
| Exercise 4 — Caesar Cipher | ✅ Outstanding |
| Exercise 5 — String Statistics | ✅ Excellent |
| Mini Project — Password Analyzer | ✅ Professional |
| Debug Fix — 5 errors | ⚠️ 4/5 |
| Interview Questions | ✅ |
| **Total** | **8/10** |

---

## 🔗 Connect

[![Portfolio](https://img.shields.io/badge/Portfolio-000000?style=flat&logo=vercel&logoColor=white)](https://mithleshrana450.github.io/mithleshrana-portfolio/)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2?style=flat&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/mithleshrana450/)
[![GitHub](https://img.shields.io/badge/GitHub-181717?style=flat&logo=github&logoColor=white)](https://github.com/Mithleshrana450)

---

<div align="center">

**[← Previous Day](../day-07-dictionaries-sets/)** • **[🏠 Back to Home](../README.md)** • **[Next Day →](../day-09-file-handling/)**

*Part of [Python for Ethical Hacking — 4 Month Journey](../README.md)*

</div>