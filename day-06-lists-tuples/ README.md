<div align="center">

# 🐍 Day 6 — Lists & Tuples

![Day](https://img.shields.io/badge/Day-6-blue?style=for-the-badge)
![Phase](https://img.shields.io/badge/Phase-1%20Foundations-green?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Complete-brightgreen?style=for-the-badge)

> *"A hacker's power lies in collections — ports, IPs, passwords, targets. Lists hold them all."*

[← Previous Day](../day-05-functions/) • [🏠 Home](../README.md) • [Next Day →](../day-07-dictionaries-sets/)

</div>

---

## 📋 Overview

| | |
|---|---|
| 📅 **Date** | July 2026 |
| 🎯 **Goal** | Master lists and tuples for real data management |
| 📦 **Files** | 6 Python files |
| ✅ **Status** | Complete |

---

## 🧠 What I Learned Today

- Lists — ordered, mutable collections using `[ ]`
- Tuples — ordered, immutable collections using `( )`
- Indexing — positive and negative index access
- Slicing — extracting portions with `[start:stop:step]`
- List methods — `append`, `insert`, `remove`, `pop`, `sort`, `reverse`
- `enumerate()` — loop with both index and value simultaneously
- List comprehension — powerful one-line filtering and mapping
- Tuple unpacking — destructuring into named variables
- `lambda` with `sort`, `max`, `min` — custom sorting
- Generator expressions — memory-efficient aggregation
- When to use list vs tuple — mutable vs immutable data

---

## 📁 File Structure

```
day-06-lists-tuples/
│
├── 📄 lists_basics.py          ← indexing, slicing, all methods
├── 📄 tuples_basics.py         ← creation, unpacking, immutability
├── 📄 list_comprehension.py    ← even numbers, odd squares, filters
├── 📄 port_scanner_v2.py       ← scan() function with list return
├── 📄 target_manager.py        ← add, remove, search, display targets
└── 📄 README.md
```

---

## 💡 Key Concepts

### List — Creation & Indexing
```python
ports = [22, 80, 443, 3306, 8080]
#         0   1    2     3     4    ← positive index
#        -5  -4   -3    -2    -1   ← negative index

print(ports[0])     # 22    — first item
print(ports[-1])    # 8080  — last item
print(ports[1:3])   # [80, 443] — slicing
print(ports[::-1])  # [8080, 3306, 443, 80, 22] — reversed
```

### List Methods — Complete Reference
```python
ports = [22, 80, 443]

# Adding
ports.append(8080)           # add to end → [22, 80, 443, 8080]
ports.insert(1, 21)          # insert at index → [22, 21, 80, 443, 8080]
ports.extend([3306, 9090])   # add multiple items

# Removing
ports.remove(21)             # remove by value (ValueError if missing)
ports.pop()                  # remove and return last item
ports.pop(0)                 # remove and return by index

# Searching
print(80 in ports)           # True — membership check
print(ports.index(80))       # 1 — find index of value
print(ports.count(80))       # 1 — count occurrences

# Sorting
ports.sort()                 # ascending in place
ports.sort(reverse=True)     # descending in place
ports.sort(key=str.lower)    # case-insensitive sort
```

### List Comprehension — One-Line Power
```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Syntax: [expression for item in iterable if condition]
even_numbers    = [i for i in numbers if i % 2 == 0]
# [2, 4, 6, 8, 10]

odd_squares     = [i**2 for i in numbers if i % 2 != 0]
# [1, 9, 25, 49, 81]

greater_than_5  = [i for i in numbers if i > 5]
# [6, 7, 8, 9, 10]

# Hacker use — generate username wordlist
names      = ["admin", "root", "user"]
variations = [name + str(n) for name in names for n in range(1, 4)]
# ["admin1", "admin2", "admin3", "root1", "root2", "root3"...]
```

### Tuple — Immutable Collections
```python
# Tuple cannot be changed after creation
target = ("192.168.1.1", 80, "HTTP")

print(target[0])           # 192.168.1.1
target[0] = "10.0.0.1"    # TypeError — tuples are immutable

# Single item tuple — comma required
wrong   = (22)             # just int 22 — NOT a tuple
correct = (22,)            # actual tuple — comma makes it

# Tuple unpacking — clean variable assignment
ip, port, protocol = target
print(ip)        # 192.168.1.1
print(port)      # 80
print(protocol)  # HTTP
```

### Tuple Unpacking in Loops
```python
targets = [
    ("192.168.1.1", 80,  "HTTP"),
    ("192.168.1.2", 22,  "SSH"),
    ("192.168.1.3", 443, "HTTPS")
]

# Without unpacking — less readable
for target in targets:
    print(target[0], target[1], target[2])

# With unpacking — clean and professional
for ip, port, service in targets:
    print(f"IP: {ip:<15} Port: {port:<6} Service: {service}")
```

### Lambda with Sort, Max, Min
```python
students = [
    ("alexa",   98),
    ("bob",     85),
    ("charlie", 92),
    ("david",   78),
    ("eve",     88)
]

# Sort by marks descending
students.sort(key=lambda x: x[1], reverse=True)

# Find highest and lowest
highest = max(students, key=lambda x: x[1])
lowest  = min(students, key=lambda x: x[1])

# Average using generator expression
average = sum(s[1] for s in students) / len(students)
print(f"Average: {average:.2f}")
```

### List vs Tuple — When to Use Which
```python
# Use LIST — data that changes
scan_results = []
scan_results.append("22/open")
scan_results.remove("22/open")

# Use TUPLE — data that never changes
COMMON_PORTS = (21, 22, 23, 25, 53, 80, 443, 3306, 8080)
HTTP_METHODS = ("GET", "POST", "PUT", "DELETE", "PATCH")
RISK_LEVELS  = ("Critical", "High", "Medium", "Low", "Info")
# constants — tuple protects from accidental modification
```

---

## 🏋️ Exercises Completed

| # | Exercise | Concept Practiced | Status |
|---|----------|-------------------|--------|
| 1 | Wordlist manager — add, remove, sort | List methods | ✅ |
| 2 | Port scanner with function + list return | Functions + lists | ✅ |
| 3 | Comprehension — even, odd squares, filter | List comprehension | ✅ |
| 4 | Loop targets with tuple unpacking | Tuple unpacking | ✅ |
| 5 | Student leaderboard — sort, max, min, avg | Lambda + tuples | ✅ |

---

## 🔨 Mini Project — Target Manager

**What it does:**
Full recon target manager — add targets as tuples,
remove by IP, display in formatted table with total count

```python
targets = []

def add_target(ip, port, service):
    targets.append((ip, port, service))
    print(f"[+] Added: {ip}:{port} ({service})")

def remove_target(ip):
    for t in targets:
        if t[0] == ip:
            targets.remove(t)
            print(f"[-] Removed: {ip}")
            return
    print(f"[!] Target {ip} not found")

def show_targets():
    print("\n" + "=" * 45)
    print(f"{'IP':<18} {'PORT':<8} {'SERVICE'}")
    print("=" * 45)
    for ip, port, service in targets:
        print(f"{ip:<18} {port:<8} {service}")
    print("=" * 45)
    print(f"Total targets in scope: {len(targets)}")
```

**Sample Output:**
```
[+] Added: 192.168.1.1:80 (HTTP)
[+] Added: 192.168.1.2:22 (SSH)

=============================================
IP                 PORT     SERVICE
=============================================
192.168.1.1        80       HTTP
192.168.1.2        22       SSH
=============================================
Total targets in scope: 2
```

---

## 🐛 Debugging Practice

4 errors found and fixed:

| # | Error Type | What Was Wrong | Fix |
|---|-----------|----------------|-----|
| 1 | IndexError | `ports[4]` on 4-item list (valid: 0-3) | `ports[3]` |
| 2 | TypeError | `ports.append[8080]` — used `[ ]` not `( )` | `ports.append(8080)` |
| 3 | ValueError | `ports.remove(9999)` — value not in list | Check with `if 9999 in ports` first |
| 4 | TypeError | `target[0] = "..."` — tuple is immutable | Convert to list, modify, convert back |

```python
# Error 3 — safe remove pattern
if 9999 in ports:
    ports.remove(9999)

# Error 4 — correct tuple modification
target = list(target)           # tuple → list
target[0] = "10.0.0.1"         # modify safely
target = tuple(target)          # list → tuple
```

---

## ❓ Interview Questions

**Q1: Difference between list and tuple?**
> List uses `[ ]` and is mutable — items can be added,
> removed, or changed anytime. Tuple uses `( )` and is
> immutable — cannot be changed after creation.
> Tuples are faster and use less memory than lists.

**Q2: When would you use a tuple instead of a list?**
> Use tuple when data should never change — constants,
> coordinates, fixed configurations, database records.
> Examples: COMMON_PORTS, HTTP_METHODS, RISK_LEVELS.
> Tuple protects data from accidental modification.

**Q3: What does enumerate() do and why is it useful?**
> enumerate() loops through a list giving both index AND
> value simultaneously — no need for a separate counter.
> `for i, port in enumerate(ports)` gives i=0,1,2...
> and port=22,80,443... at the same time. Used everywhere
> in professional code for clean indexed iteration.

---

## ❌ Mistakes I Made Today

```python
# WRONG — using index access instead of tuple unpacking
for target in targets:
    print(target[0], target[1], target[2])

# CORRECT — tuple unpacking is cleaner
for ip, port, service in targets:
    print(f"{ip} → {port} ({service})")

# WRONG — case sensitive sort causes unexpected order
passwords.sort()
# ['Admin', 'password', 'qwerty'] ← 'A' (65) < 'a' (97) in ASCII

# CORRECT — case insensitive sort
passwords.sort(key=str.lower)

# WRONG — reassigning tuple variable as "fix"
target = ("10.0.0.1", 80)   # just creates new tuple

# CORRECT — proper fix shows understanding
target = list(target)
target[0] = "10.0.0.1"
target = tuple(target)
```

---

## 🔐 Hacker Application

```python
# Brute force structure — exact logic of Hydra/Medusa
def load_wordlist():
    return [
        "admin", "password", "123456",
        "root", "toor", "hacker123",
        "letmein", "qwerty", "abc123"
    ]

def brute_force(target_user, target_pass, wordlist):
    print(f"[*] Target   : {target_user}")
    print(f"[*] Wordlist : {len(wordlist)} passwords")
    print("-" * 40)

    for i, pwd in enumerate(wordlist):
        print(f"[{i+1:>3}/{len(wordlist)}] Trying: {pwd}")
        if pwd == target_pass:
            print(f"\n[+] CRACKED  → {pwd}")
            print(f"[+] Attempts → {i+1}")
            return pwd

    print("[-] Password not found in wordlist")
    return None

# Username variation generator — OSINT technique
def generate_usernames(first, last):
    return [
        f"{first.lower()}_{last.lower()}",
        f"{first.lower()}{last.lower()}",
        f"{first[0].lower()}{last.lower()}",
        f"{first.lower()}123",
        f"{last.lower()}_{first.lower()}"
    ]

print(generate_usernames("Mithu", "Rana"))
```

**Real tools that use lists/tuples:**

| Tool | How Lists Are Used |
|------|-------------------|
| Hydra | Wordlist stored as list, iterated with loop |
| Nmap | Scan results stored as list of tuples |
| theHarvester | Emails collected into list |
| Sublist3r | Subdomains stored and deduplicated in list |
| Metasploit | Module options stored as list of tuples |

---

## 📊 Day Score

| Category | Score |
|----------|-------|
| Exercise 1 — Wordlist Manager | ✅ Good |
| Exercise 2 — Port Scanner | ✅ Excellent |
| Exercise 3 — Comprehension | ✅ Perfect |
| Exercise 4 — Tuple Unpacking | ✅ |
| Exercise 5 — Leaderboard | ✅ Outstanding |
| Debug Fix | ⚠️ 2/4 errors fully fixed |
| Mini Project | ✅ |
| Interview Questions | ✅ |
| **Total** | **8.5/10** |

---

## 🔗 Connect

[![Portfolio](https://img.shields.io/badge/Portfolio-000000?style=flat&logo=vercel&logoColor=white)](https://mithleshrana450.github.io/mithleshrana-portfolio/)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2?style=flat&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/mithleshrana450/)
[![GitHub](https://img.shields.io/badge/GitHub-181717?style=flat&logo=github&logoColor=white)](https://github.com/Mithleshrana450)

---

<div align="center">

**[← Previous Day](../day-05-functions/)** • **[🏠 Back to Home](../README.md)** • **[Next Day →](../day-07-dictionaries-sets/)**

*Part of [Python for Ethical Hacking — 4 Month Journey](../README.md)*

</div>