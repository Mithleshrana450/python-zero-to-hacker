<div align="center">

# 🐍 Day 7 — Dictionaries & Sets

![Day](https://img.shields.io/badge/Day-7-blue?style=for-the-badge)
![Phase](https://img.shields.io/badge/Phase-1%20Foundations-green?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Complete-brightgreen?style=for-the-badge)

> *"Every scan result, every recon output, every config file — all dictionaries."*

[← Previous Day](../day-06-lists-tuples/) • [🏠 Home](../README.md) • [Next Day →](../day-08-string-manipulation/)

</div>

---

## 📋 Overview

| | |
|---|---|
| 📅 **Date** | July 2026 |
| 🎯 **Goal** | Master dictionaries and sets for real data management |
| 📦 **Files** | 7 Python files |
| ✅ **Status** | Complete |

---

## 🧠 What I Learned Today

- Dictionaries — key-value pair storage using `{ }`
- Dictionary methods — `get`, `keys`, `values`, `items`, `update`, `pop`
- Safe key access — `dict.get(key, default)` vs `dict[key]`
- Nested dictionaries — storing complex scan results
- Dictionary comprehension — one-line dict creation
- Sets — unordered unique collections
- Set operations — union `|`, intersection `&`, difference `-`
- Hash tables — why sets are O(1) for membership checks
- `key=average.get` — advanced sorting with dict values
- `count.get(word, 0) + 1` — professional frequency counting

---

## 📁 File Structure

```
day-07-dictionaries-sets/
│
├── 📄 dict_basics.py           ← target info dict, add/update/loop
├── 📄 port_service_mapper.py   ← get_service(port) function
├── 📄 word_frequency.py        ← word counter with sorted output
├── 📄 sets_basics.py           ← TCP/UDP scan set operations
├── 📄 Students_data.py         ← student registry with leaderboard
├── 📄 network_recon_report.py  ← full recon report mini project
├── 📄 Debugging.py             ← 4 errors found and fixed
└── 📄 README.md
```

---

## 💡 Key Concepts

### Dictionary — Creation & Access
```python
target = {
    "ip"      : "192.168.1.1",
    "port"    : 80,
    "service" : "HTTP",
    "os"      : "Linux"
}

# Access methods
print(target["ip"])                    # 192.168.1.1 — crashes if missing
print(target.get("ip"))                # 192.168.1.1 — safe
print(target.get("version", "N/A"))   # N/A — default if key missing
```

### Dictionary — Modifying
```python
target["status"] = "vulnerable"        # add new key
target["port"]   = 443                 # update existing
del target["service"]                  # delete key
removed = target.pop("os")             # delete and return value
target.update({"os": "Ubuntu 20.04"}) # merge dict
```

### Dictionary — Looping
```python
# Keys only
for key in target:
    print(key)

# Keys and values — most common
for key, value in target.items():
    print(f"{key:<15} : {value}")

# Values only
for value in target.values():
    print(value)
```

### Safe Key Access — dict.get() vs dict[]
```python
student = {"name": "Mithu", "marks": 95}

# UNSAFE — crashes if key missing
print(student["age"])          # KeyError: 'age'

# SAFE — returns None or default
print(student.get("age"))      # None — no crash
print(student.get("age", 0))   # 0 — custom default
```

### Nested Dictionary — Scan Results
```python
network = {
    "192.168.1.1": {
        "ports"  : [22, 80, 443],
        "os"     : "Linux",
        "risk"   : "Medium"
    },
    "192.168.1.2": {
        "ports"  : [23, 3306],
        "os"     : "Windows",
        "risk"   : "Critical"
    }
}

# Access nested data
print(network["192.168.1.1"]["os"])      # Linux
print(network["192.168.1.2"]["ports"])   # [23, 3306]

# Loop nested
for ip, data in network.items():
    print(f"{ip} → Risk: {data['risk']}")
```

### Dictionary Comprehension
```python
ports    = [22, 80, 443, 3306]
services = {22: "SSH", 80: "HTTP", 443: "HTTPS", 3306: "MySQL"}

# Create mapping only for known ports
port_map = {p: services[p] for p in ports if p in services}
# {22: 'SSH', 80: 'HTTP', 443: 'HTTPS', 3306: 'MySQL'}
```

### Sets — Unique Collections
```python
# Duplicates auto-removed
found = {22, 80, 443, 80, 22}
print(found)    # {443, 80, 22} — order not guaranteed

# Empty set — must use set() not {}
empty = set()   # correct
wrong = {}      # this is empty DICT not set
```

### Set Operations — Hacker Power
```python
scan_tcp = {21, 22, 80, 443, 3306, 8080}
scan_udp = {53, 80, 443, 161, 162, 8080}

print(scan_tcp | scan_udp)   # UNION — all unique ports from both
print(scan_tcp & scan_udp)   # INTERSECTION — ports in BOTH scans
print(scan_tcp - scan_udp)   # DIFFERENCE — only in TCP, not UDP
print(scan_tcp ^ scan_udp)   # SYMMETRIC DIFF — in one but not both
```

### Why Sets Are Faster Than Lists
```python
# List — O(n) — scans every item
ports_list = [22, 80, 443, 3306, 8080]
80 in ports_list    # checks 22, then 80 — found

# Set — O(1) — hash table, instant lookup
ports_set = {22, 80, 443, 3306, 8080}
80 in ports_set     # calculates hash(80), jumps directly — instant
# Speed difference: massive on large datasets (1M+ items)
```

---

## 🏋️ Exercises Completed

| # | Exercise | Concept Practiced | Status |
|---|----------|-------------------|--------|
| 1 | Target info dictionary | dict creation, add, update, loop | ✅ |
| 2 | Port service mapper | `dict.get()` with default | ✅ Perfect |
| 3 | Word frequency counter | frequency dict + sorted lambda | ✅ Excellent |
| 4 | TCP/UDP set operations | `\|`, `&`, `-` operators | ✅ Perfect |
| 5 | Student registry leaderboard | nested dict + `key=dict.get` | ✅ Outstanding |

---

## 🔨 Mini Project — Network Recon Report

**What it does:**
Full network scan report — stores hosts as nested dicts,
auto-assigns services, calculates risk level, generates report

```python
def calculate_risk(ports):
    if 23 in ports:
        return "Critical"      # Telnet = always critical
    if 3306 in ports or len(ports) > 5:
        return "High"          # DB exposed or too many ports
    if 22 in ports or 80 in ports:
        return "Medium"
    return "Low"

def add_host(ip, ports, os):
    scan_results[ip] = {
        "ports"    : ports,
        "services" : {p: services.get(p, "Unknown") for p in ports},
        "os"       : os,
        "risk"     : calculate_risk(ports)
    }
```

**Sample Output:**
```
=======================================================
           NETWORK RECON REPORT
=======================================================

[HOST]   192.168.1.1
  OS     : Ubuntu 20.04
  Risk   : Medium
  22     : SSH
  80     : HTTP
  443    : HTTPS

[HOST]   192.168.1.2
  OS     : Windows Server
  Risk   : Critical
  23     : Telnet
  3306   : MySQL

=======================================================
Total hosts scanned: 3
```

---

## 🐛 Debugging Practice

4 errors found and fixed:

| # | Error Type | What Was Wrong | Fix |
|---|-----------|----------------|-----|
| 1 | KeyError | `student["age"]` — key doesn't exist | Changed to `student["marks"]` |
| 2 | TypeError | `student[marks]` — missing quotes | Changed to `student["marks"]` |
| 3 | AttributeError | `{}.add(80)` — `{}` is dict not set | Changed to `set()` |
| 4 | ValueError | `for key, val in services` — missing `.items()` | Added `.items()` |

```python
# Error 1 — KeyError fix
print(student["marks"])           # key that actually exists

# Error 2 — missing quotes
total = sum(student["marks"])     # string key, not variable

# Error 3 — empty set vs empty dict
found_ports = set()               # correct empty set
found_ports.add(80)               # now works

# Error 4 — dict loop needs .items()
for key, val in services.items(): # unpacks (key, value) pairs
    print(key, val)
```

---

## ❓ Interview Questions

**Q1: Difference between `dict["key"]` and `dict.get("key")`?**
> `dict["key"]` raises a `KeyError` and crashes the program
> if the key doesn't exist. `dict.get("key")` returns `None`
> safely, or a custom default: `dict.get("key", 0)`.
> Always use `.get()` when key existence is uncertain —
> critical in hacking tools where data may be incomplete.

**Q2: Why are sets faster than lists for membership checks?**
> Sets use a **hash table** internally. Python calculates
> a hash of the value and jumps directly to its memory
> location — O(1) constant time regardless of size.
> Lists scan item by item — O(n) linear time.
> For 1 million items: list takes 1M checks, set takes 1.

**Q3: Difference between `|` and `&` for sets?**
> `|` is Union — combines ALL unique items from both sets.
> `&` is Intersection — returns ONLY items that exist in BOTH sets.
> Example: TCP ports | UDP ports = every port found anywhere.
> TCP ports & UDP ports = ports responding on both protocols.

---

## ❌ Mistakes I Made Today

```python
# WRONG — interview answer was incorrect
# dict["key"] is NOT a list
# dict.get("key") is NOT a set

# CORRECT understanding:
student["age"]          # KeyError if missing — crashes
student.get("age", 0)  # returns 0 safely — never crashes

# WRONG — incomplete set answer
# Only said "|" is union without explaining "&"

# CORRECT:
scan1 | scan2   # Union — ALL ports from both
scan1 & scan2   # Intersection — only COMMON ports

# WRONG — word counter with if/else (works but verbose)
if word in count:
    count[word] += 1
else:
    count[word] = 1

# CORRECT — professional one-liner
count[word] = count.get(word, 0) + 1
```

---

## 🔐 Hacker Application

```python
# Vulnerability scanner data structure
# Exact format used by Nmap, Metasploit, Burp Suite

scan_results = {
    "192.168.1.1": {
        "open_ports" : [22, 80, 443],
        "services"   : {22: "SSH", 80: "HTTP", 443: "HTTPS"},
        "os"         : "Ubuntu 20.04",
        "risk"       : "Medium",
        "vulns"      : ["CVE-2021-44228", "Weak SSH config"]
    },
    "192.168.1.2": {
        "open_ports" : [23, 3306],
        "services"   : {23: "Telnet", 3306: "MySQL"},
        "os"         : "Windows Server 2019",
        "risk"       : "Critical",
        "vulns"      : ["Telnet unencrypted", "MySQL exposed publicly"]
    }
}

# Port deduplication using sets — used in real scanners
tcp_results = {22, 80, 443, 80, 22, 443}  # raw scan (duplicates)
clean_ports = set(tcp_results)             # deduped instantly
print(f"Unique ports found: {clean_ports}")

# Word frequency on log files — real OSINT technique
log = "admin login failed admin login success root login failed"
words = log.split()
freq  = {w: words.count(w) for w in set(words)}
print(sorted(freq.items(), key=lambda x: x[1], reverse=True))
# Shows which usernames appear most in failed logins
```

**Real tools using dictionaries/sets:**

| Tool | Usage |
|------|-------|
| Nmap | Stores scan results as nested dicts per host |
| Metasploit | Workspace data stored as dict of dicts |
| Shodan API | Returns JSON (dict) per host |
| theHarvester | Email/domain results deduplicated with sets |
| Burp Suite | Request/response stored as key-value dicts |

---

## 📊 Day Score

| Category | Score |
|----------|-------|
| Exercise 1 — Target Dict | ✅ Good |
| Exercise 2 — Port Mapper | ✅ Perfect |
| Exercise 3 — Word Frequency | ✅ Excellent |
| Exercise 4 — Set Operations | ✅ Perfect |
| Exercise 5 — Student Registry | ✅ Outstanding |
| Debug Fix — 4 errors | ✅ All fixed |
| Mini Project | ✅ |
| Interview Q1 | ❌ → Corrected |
| Interview Q2 | ❌ → Corrected |
| Interview Q3 | ⚠️ → Completed |
| **Total** | **7.5/10** |

---

## 🔗 Connect

[![Portfolio](https://img.shields.io/badge/Portfolio-000000?style=flat&logo=vercel&logoColor=white)](https://mithleshrana450.github.io/mithleshrana-portfolio/)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2?style=flat&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/mithleshrana450/)
[![GitHub](https://img.shields.io/badge/GitHub-181717?style=flat&logo=github&logoColor=white)](https://github.com/Mithleshrana450)

---

<div align="center">

**[← Previous Day](../day-06-lists-tuples/)** • **[🏠 Back to Home](../README.md)** • **[Next Day →](../day-08-string-manipulation/)**

*Part of [Python for Ethical Hacking — 4 Month Journey](../README.md)*

</div>