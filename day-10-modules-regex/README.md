<div align="center">

# 🐍 Day 10 — Modules, Packages & Regular Expressions

![Day](https://img.shields.io/badge/Day-10-blue?style=for-the-badge)
![Phase](https://img.shields.io/badge/Phase-1%20Foundations-green?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Complete-brightgreen?style=for-the-badge)

> *"Regex is the hacker's scalpel — find anything in any text, instantly."*

[← Previous Day](../day-09-file-handling/) • [🏠 Home](../README.md) • [Next Day →](../day-11-oop/)

</div>

---

## 📋 Overview

| | |
|---|---|
| 📅 **Date** | July 2026 |
| 🎯 **Goal** | Build reusable modules and extract intelligence from text using regex |
| 📦 **Files** | 8 Python files + 4 generated files |
| ✅ **Status** | Complete |

---

## 🧠 What I Learned Today

- Creating custom modules — `hacker_utils.py`
- Importing modules — `import`, `from x import y`, aliases
- `if __name__ == "__main__"` — the critical module pattern
- Built-in modules — `hashlib`, `socket`, `sys`, `random`, `string`
- `hashlib` — MD5, SHA1, SHA256 hashing
- `socket.getservbyport()` — real system service lookup
- `sys.argv` — command line argument parsing
- Regex patterns — `.`, `\d`, `\w`, `\s`, `+`, `*`, `?`, `{n}`
- Regex functions — `findall`, `search`, `match`, `sub`, `compile`
- Named capture groups — `(?P<name>pattern)`
- Non-capturing groups — `(?:pattern)`
- Real OSINT patterns — email, IP, URL, phone, MD5, SHA256
- Building a real OSINT extraction tool

---

## 📁 File Structure

```
day-10-modules-regex/
│
├── 📄 hacker_utils.py        ← custom module: hash, IP validate, service, password gen
├── 📄 main.py                ← imports and uses hacker_utils
├── 📄 regex_extractor.py     ← extracts emails, IPs, URLs, phones, MD5
├── 📄 log_analyzer.py        ← brute force detection via regex
├── 📄 hash_checker.py        ← password hashing + known hash comparison
├── 📄 cli_scanner.py         ← sys.argv command line port scanner
├── 📄 osint_extractor.py     ← full OSINT tool: manual/file input + report
├── 📄 debugging.py           ← 5 errors found and fixed
│
├── 📝 hashes.txt             ← generated: MD5/SHA1/SHA256 output
├── 📝 osint_report.txt       ← generated: extracted intelligence
├── 📝 activity_log.txt       ← generated: timestamped activity
└── 📄 README.md
```

---

## 💡 Key Concepts

### Creating & Importing Modules
```python
# hacker_utils.py — your custom module
import hashlib
import socket
import random
import string

def hash_password(password):
    md5    = hashlib.md5(password.encode()).hexdigest()
    sha256 = hashlib.sha256(password.encode()).hexdigest()
    return md5, sha256

def is_valid_ip(ip):
    parts = ip.split(".")
    return len(parts) == 4 and all(
        p.isdigit() and 0 <= int(p) <= 255 for p in parts
    )

def get_service(port):
    try:
        return socket.getservbyport(port)   # real system call
    except OSError:
        return "Unknown"

def generate_random_password(length):
    chars = string.ascii_letters + string.digits
    return "".join(random.choice(chars) for _ in range(length))

# Only runs when executed directly, NOT when imported
if __name__ == "__main__":
    print(hash_password("test"))
```

```python
# main.py — import your module
# WRONG — pollutes namespace
from hacker_utils import *

# CORRECT — explicit imports
from hacker_utils import hash_password, is_valid_ip, get_service, generate_random_password

md5, sha = hash_password("hello123")
print("MD5   :", md5)
print("SHA256:", sha)
print("Valid IP:", is_valid_ip("192.168.1.1"))
print("Service :", get_service(80))
print("Password:", generate_random_password(12))
```

### if __name__ == "__main__"
```python
# When you RUN the file directly:
# __name__ == "__main__"  → block RUNS

# When you IMPORT the file as a module:
# __name__ == "hacker_utils"  → block SKIPPED

# This prevents test code from running on import
if __name__ == "__main__":
    print("Running directly — test mode")
    # This won't execute when someone imports your module
```

### Built-in Modules for Hacking
```python
import hashlib     # MD5, SHA1, SHA256, SHA512 hashing
import socket      # network connections, service lookup
import sys         # argv, version, exit, platform
import random      # randint, choice, shuffle
import string      # ascii_letters, digits, punctuation
import os          # file system, environment variables
import subprocess  # run system commands
import base64      # encode/decode data
import json        # parse JSON responses

# hashlib — most used in security
hashlib.md5("pass".encode()).hexdigest()      # 32 char hex
hashlib.sha1("pass".encode()).hexdigest()     # 40 char hex
hashlib.sha256("pass".encode()).hexdigest()   # 64 char hex

# sys.argv — command line tools
# python tool.py 192.168.1.1 80
# sys.argv[0] = "tool.py"
# sys.argv[1] = "192.168.1.1"
# sys.argv[2] = "80"
```

### Regex — Core Patterns
```python
import re

# Pattern reference
# .        any character
# \d       digit 0-9
# \w       word char a-z A-Z 0-9 _
# \s       whitespace
# \b       word boundary
# +        1 or more
# *        0 or more
# ?        0 or 1
# {3}      exactly 3
# {1,3}    1 to 3
# [abc]    a or b or c
# [^abc]   NOT a, b, or c
# (?:...)  non-capturing group
# (?P<name>...) named group

# Core functions
re.findall(pattern, text)    # returns LIST of all matches
re.search(pattern, text)     # returns first MATCH OBJECT or None
re.match(pattern, text)      # matches at START only
re.sub(pattern, replacement, text)  # find and replace
re.compile(pattern)          # compile for reuse (faster)
```

### Real OSINT Regex Patterns
```python
import re

text = "admin@company.com logged in from 192.168.1.1 via https://target.com"

# Email
emails = re.findall(r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}', text)

# IP address — non-capturing group for efficiency
ips = re.findall(r'\b(?:\d{1,3}\.){3}\d{1,3}\b', text)

# URL
urls = re.findall(r'https?://\S+|www\.\S+', text)

# Phone (10 digit)
phones = re.findall(r'\b\d{10}\b', text)

# MD5 hash (32 hex chars)
md5 = re.findall(r'\b[a-fA-F0-9]{32}\b', text)

# SHA256 hash (64 hex chars)
sha256 = re.findall(r'\b[a-fA-F0-9]{64}\b', text)

print("Emails:", emails)
print("IPs   :", ips)
print("URLs  :", urls)
```

### search() vs match() vs findall()
```python
text = "Port 80 open, Port 443 open"

# search — finds FIRST match ANYWHERE in string
re.search(r'\d+', text).group()      # "80"

# match — matches at START of string ONLY
re.match(r'\d+', text)               # None — doesn't start with digit
re.match(r'Port', text).group()      # "Port" — starts with Port

# findall — finds ALL matches, returns LIST
re.findall(r'\d+', text)             # ['80', '443']
```

### Log Analysis with Regex
```python
import re

logs = [
    "2026-07-09 14:32:11 FAILED LOGIN admin 192.168.1.105",
    "2026-07-09 14:32:15 FAILED LOGIN admin 192.168.1.105",
    "2026-07-09 14:33:01 SUCCESS LOGIN admin 10.0.0.1",
    "2026-07-09 14:33:19 FAILED LOGIN admin 192.168.1.105",
]

count = {}
for log in logs:
    if re.search(r"FAILED", log):
        ip = re.search(r"\d+\.\d+\.\d+\.\d+", log).group()
        count[ip] = count.get(ip, 0) + 1

for ip, c in count.items():
    flag = "⚠️ ALERT" if c > 3 else ""
    print(f"{ip:<20} {c} attempts {flag}")
```

---

## 🏋️ Exercises Completed

| # | Exercise | Concept Practiced | Status |
|---|----------|-------------------|--------|
| 1 | hacker_utils.py module | hashlib, socket, random, string | ✅ Outstanding |
| 2 | Regex extractor | findall, IP/email/URL/MD5 patterns | ✅ Good |
| 3 | Log analyzer | regex search + dict counting | ✅ |
| 4 | Password hash checker | hashlib + file writing | ✅ |
| 5 | CLI scanner | sys.argv parsing + range flag | ✅ Good |

---

## 🔨 Mini Project — OSINT Extractor

**What it does:**
Full OSINT intelligence extractor — accepts manual
text or file input, extracts 6 data types using regex,
saves report, logs activity with timestamp

```python
import re
from datetime import datetime

# Extract all intelligence types
emails  = re.findall(r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}', text)
ips     = re.findall(r'\b(?:\d{1,3}\.){3}\d{1,3}\b', text)
urls    = re.findall(r'https?://\S+|www\.\S+', text)
phones  = re.findall(r'\b\d{10}\b', text)
md5     = re.findall(r'\b[a-fA-F0-9]{32}\b', text)
sha256  = re.findall(r'\b[a-fA-F0-9]{64}\b', text)

# Save to report file
with open("osint_report.txt", "w") as f:
    f.write("OSINT EXTRACTION REPORT\n\n")
    f.write(f"Emails     ({len(emails)})  : {emails}\n")
    f.write(f"IPs        ({len(ips)})     : {ips}\n")
    f.write(f"URLs       ({len(urls)})    : {urls}\n")
    f.write(f"Phones     ({len(phones)})  : {phones}\n")
    f.write(f"MD5 Hashes ({len(md5)})     : {md5}\n")
    f.write(f"SHA256     ({len(sha256)})  : {sha256}\n")
```

**Sample Output:**
```
Extraction Completed!
Emails       : 2
IPs          : 2
URLs         : 2
Phone Numbers: 1
MD5 Hashes   : 1
SHA256 Hashes: 0

Report saved as osint_report.txt
Log saved as activity_log.txt
```

---

## 🐛 Debugging Practice

5 errors found and fixed:

| # | Error | Wrong | Fix |
|---|-------|-------|-----|
| 1 | ImportError | `import Re` — case sensitive | `import re` lowercase |
| 2 | AttributeError | `re.Findall()` — wrong case | `re.findall()` lowercase |
| 3 | Regex missing raw string | `compile('\d{1,3}...')` — `\d` treated as escape | `compile(r'\d{1,3}...')` |
| 4 | TypeError | `hashlib.md5("password")` — needs bytes | `.encode()` → `hashlib.md5("password".encode())` |
| 5 | IndexError | `sys.argv[2]` — no safety check | `if len(sys.argv) > 1` guard |

```python
# All 5 fixes
import re                                          # Fix 1 — lowercase
emails = re.findall(r'[\w]+@[\w]+\.[\w]+', text)  # Fix 2 — lowercase findall
pattern = re.compile(r'\d{1,3}\.\d{1,3}...')      # Fix 3 — raw string r''
hash_v  = hashlib.md5("password".encode()).hexdigest()  # Fix 4 — .encode()
target  = sys.argv[1] if len(sys.argv) > 1 else "None"  # Fix 5 — safe check
```

---

## ❓ Interview Questions

**Q1: What does `if __name__ == "__main__"` do?**
> When a Python file is run directly, `__name__`
> equals `"__main__"`. When imported as a module,
> `__name__` equals the file name. This pattern
> prevents test or execution code from running
> when your module is imported by another file.
> Essential for writing reusable modules.

**Q2: Difference between `re.search()` and `re.match()`?**
> `re.search()` scans the ENTIRE string and returns
> the first match anywhere. `re.match()` only checks
> at the BEGINNING of the string — returns None if
> pattern doesn't start at position 0.
> Use `search()` for log parsing. Use `match()` when
> you need to validate string format from the start.

**Q3: What does `re.findall()` return?**
> Returns a LIST of all non-overlapping matches.
> If pattern has groups `()`, returns list of tuples.
> If no match found, returns empty list `[]` — never
> raises an error. This makes it safe for scanning
> large text where matches may not exist.

---

## ❌ Mistakes I Made Today

```python
# WRONG — import * pollutes namespace
from hacker_utils import *

# CORRECT — explicit, readable, professional
from hacker_utils import hash_password, is_valid_ip

# WRONG — bare except in module function
except:
    return "Unknown"

# CORRECT — specific exception
except OSError:
    return "Unknown"

# WRONG — old file style (Day 9 lesson forgotten)
file = open("hashes.txt", "w")
file.write(...)
file.close()

# CORRECT — context manager, always
with open("hashes.txt", "w") as f:
    f.write(...)

# WRONG — no input validation on sys.argv
target = sys.argv[2]    # IndexError if not provided

# CORRECT — always guard argv access
if len(sys.argv) > 2:
    target = sys.argv[2]
else:
    print("Usage: python script.py <ip> <port>")
    sys.exit(1)
```

---

## 🔐 Hacker Application

```python
import re
import hashlib
import sys
from datetime import datetime

# Real OSINT extraction patterns — used in bug bounty recon
PATTERNS = {
    "emails" : r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}',
    "ips"    : r'\b(?:\d{1,3}\.){3}\d{1,3}\b',
    "urls"   : r'https?://\S+|www\.\S+',
    "md5"    : r'\b[a-fA-F0-9]{32}\b',
    "sha256" : r'\b[a-fA-F0-9]{64}\b',
}

def extract_intelligence(text):
    return {name: list(set(re.findall(p, text)))
            for name, p in PATTERNS.items()}

# Hash cracking prep — generate rainbow table entry
def generate_hash_entry(password):
    return {
        "password" : password,
        "md5"      : hashlib.md5(password.encode()).hexdigest(),
        "sha1"     : hashlib.sha1(password.encode()).hexdigest(),
        "sha256"   : hashlib.sha256(password.encode()).hexdigest()
    }

# Brute force detection — real SIEM logic
def detect_brute_force(logs, threshold=3):
    count = {}
    for log in logs:
        if re.search(r"FAILED", log):
            ip = re.search(r"\d+\.\d+\.\d+\.\d+", log).group()
            count[ip] = count.get(ip, 0) + 1
    return {ip: c for ip, c in count.items() if c >= threshold}

# CLI tool pattern — used in every real hacking tool
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(f"Usage: python {sys.argv[0]} <target>")
        sys.exit(1)
    target = sys.argv[1]
    print(f"[*] Targeting: {target}")
```

**Real tools using these concepts:**

| Tool | Module/Regex Usage |
|------|-------------------|
| theHarvester | Regex to extract emails/IPs from search results |
| Maltego | Pattern matching for OSINT intelligence |
| Splunk | Regex field extraction from log lines |
| Nikto | sys.argv for CLI target specification |
| Hashcat | hashlib-equivalent for hash generation |

---

## 📊 Day Score

| Category | Score |
|----------|-------|
| Exercise 1 — hacker_utils module | ✅ Outstanding |
| Exercise 2 — Regex extractor | ✅ Good |
| Exercise 3 — Log analyzer | ✅ |
| Exercise 4 — Hash checker | ✅ |
| Exercise 5 — CLI scanner | ✅ Good |
| Mini Project — OSINT extractor | ✅ Professional |
| Debug Fix — 5 errors | ✅ All fixed |
| Interview Questions | ✅ |
| **Total** | **8.5/10** |

---

## 🔗 Connect

[![Portfolio](https://img.shields.io/badge/Portfolio-000000?style=flat&logo=vercel&logoColor=white)](https://mithleshrana450.github.io/mithleshrana-portfolio/)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2?style=flat&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/mithleshrana450/)
[![GitHub](https://img.shields.io/badge/GitHub-181717?style=flat&logo=github&logoColor=white)](https://github.com/Mithleshrana450)

---

<div align="center">

**[← Previous Day](../day-09-file-handling/)** • **[🏠 Back to Home](../README.md)** • **[Next Day →](../day-11-oop/)**

*Part of [Python for Ethical Hacking — 4 Month Journey](../README.md)*

</div>