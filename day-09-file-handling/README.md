<div align="center">

# 🐍 Day 9 — File Handling & Exception Handling

![Day](https://img.shields.io/badge/Day-9-blue?style=for-the-badge)
![Phase](https://img.shields.io/badge/Phase-1%20Foundations-green?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Complete-brightgreen?style=for-the-badge)

> *"Real hacking tools never crash. They handle every error, log it, and keep going."*

[← Previous Day](../day-08-string-manipulation/) • [🏠 Home](../README.md) • [Next Day →](../day-10-modules-regex/)

</div>

---

## 📋 Overview

| | |
|---|---|
| 📅 **Date** | July 2026 |
| 🎯 **Goal** | Read/write files and handle errors like a professional tool |
| 📦 **Files** | 8 Python files + 4 generated files |
| ✅ **Status** | Complete |

---

## 🧠 What I Learned Today

- File modes — `r`, `w`, `a`, `x`, `rb`, `wb`
- `with open()` — auto-close, safer than manual `close()`
- Reading files — `read()`, `readlines()`, `splitlines()`, line-by-line loop
- Writing files — `write()`, `writelines()`, append mode
- `try/except/else/finally` — full exception handling structure
- Common exceptions — `ValueError`, `FileNotFoundError`, `ZeroDivisionError`
- `except Exception as e` vs bare `except` — why one is dangerous
- `os` module — file existence, size, timestamps, directory listing
- `datetime` — timestamped logging
- Raising custom exceptions with `raise`
- Duplicate removal with `dict.fromkeys()`
- Professional logging pattern — timestamp + level + message

---

## 📁 File Structure

```
day-09-file-handling/
│
├── 📄 file_basics.py           ← target list: create, read, append, deduplicate
├── 📄 safe_calculator.py       ← calculator with full exception handling
├── 📄 wordlist_processor.py    ← read, filter, analyze, save passwords
├── 📄 log_writer.py            ← timestamped logging system
├── 📄 file_scanner.py          ← folder scanner with size + modified date
├── 📄 recon_file_manager.py    ← full recon pipeline with file I/O
├── 📄 hacker_application.py    ← wordlist loader + result saver
├── 📄 debugging.py             ← 5 errors found and fixed
│
├── 📝 targets.txt              ← generated: IP target list
├── 📝 results.txt              ← generated: scan output
├── 📝 scan.log                 ← generated: activity log
└── 📄 README.md
```

---

## 💡 Key Concepts

### File Modes
```python
"r"   # read only — file must exist, default mode
"w"   # write — creates new OR overwrites existing content
"a"   # append — adds to end, creates file if missing
"x"   # exclusive create — fails if file already exists
"rb"  # read binary — images, executables, encrypted files
"wb"  # write binary
```

### with open() — Always Use This
```python
# OLD way — must close manually, risky if error occurs
f = open("targets.txt", "r")
content = f.read()
f.close()              # forgot this = file stays locked

# PROFESSIONAL way — auto closes even if exception occurs
with open("targets.txt", "r") as f:
    content = f.read()
# file automatically closed here — guaranteed
```

### Reading Files — 4 Ways
```python
with open("targets.txt", "r") as f:
    content = f.read()           # entire file as one string
    lines   = f.readlines()      # list of lines including \n
    words   = f.read().splitlines()  # list without \n — cleaner
    line    = f.readline()       # one line at a time

# Best for large files — loop directly, memory efficient
with open("targets.txt", "r") as f:
    for line in f:
        print(line.strip())      # strip() removes trailing \n
```

### Writing Files
```python
# Write — creates or overwrites
with open("results.txt", "w") as f:
    f.write("Port 80: OPEN\n")
    f.write("Port 443: OPEN\n")

# Append — keeps existing, adds to end
with open("results.txt", "a") as f:
    f.write("Port 22: OPEN\n")

# Write list of lines
lines = ["192.168.1.1\n", "192.168.1.2\n"]
with open("targets.txt", "w") as f:
    f.writelines(lines)

# Clean way — join with newline
ips = ["192.168.1.1", "192.168.1.2", "10.0.0.1"]
with open("targets.txt", "w") as f:
    f.write("\n".join(ips))
```

### Exception Handling — Full Structure
```python
try:
    result = 10 / 0           # code that might fail
except ZeroDivisionError:
    print("Cannot divide by zero")
except ValueError as e:
    print(f"Value error: {e}")
except FileNotFoundError:
    print("File not found")
except Exception as e:        # catch-all — use last
    print(f"Unexpected: {e}")
else:
    print("Success")          # runs ONLY if no exception
finally:
    print("Always runs")      # cleanup — runs no matter what
```

### except Exception vs bare except
```python
# WRONG — bare except catches everything including Ctrl+C
except:
    print("Error")            # hides serious system errors

# CORRECT — catches standard exceptions, shows message
except Exception as e:
    print(f"Error: {e}")      # tells you what went wrong
```

### OS Module — File Operations
```python
import os

os.path.exists("file.txt")         # True/False — does it exist?
os.path.isfile("file.txt")         # True if file (not directory)
os.path.isdir("folder")            # True if directory
os.path.getsize("file.txt")        # size in bytes
os.path.getmtime("file.txt")       # last modified timestamp
os.path.join("folder", "file.txt") # safe path joining
os.listdir(".")                     # list files in directory
os.makedirs("logs/scans")          # create directory tree
os.rename("old.txt", "new.txt")    # rename file
os.remove("file.txt")              # delete file
```

### Professional Logging Pattern
```python
from datetime import datetime

def log(level, message):
    with open("scan.log", "a") as f:
        time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f.write(f"{time} [{level}] {message}\n")

log("INFO",     "Scan started")
log("INFO",     "Port 80 is open")
log("WARNING",  "Port 21 is closed")
log("ERROR",    "Connection timeout")
log("CRITICAL", "System failure")

# Output in scan.log:
# 2026-07-09 14:32:11 [INFO] Scan started
# 2026-07-09 14:32:15 [WARNING] Port 21 is closed
```

### Duplicate Removal from File
```python
with open("targets.txt", "r") as f:
    ips = f.read().splitlines()

# Remove duplicates preserving order
ips = list(dict.fromkeys(ips))

with open("targets.txt", "w") as f:
    f.write("\n".join(ips))
```

---

## 🏋️ Exercises Completed

| # | Exercise | Concept Practiced | Status |
|---|----------|-------------------|--------|
| 1 | Target list — create, read, append, deduplicate | File modes + dict.fromkeys | ✅ Good |
| 2 | Safe calculator — never crashes | try/except/ZeroDivisionError/ValueError | ✅ Excellent |
| 3 | Wordlist processor — filter + save | splitlines, comprehension, max/min | ✅ Perfect |
| 4 | Log writer — timestamped entries | datetime + append mode | ✅ Perfect |
| 5 | File scanner — size + modified date | os module + datetime | ✅ Excellent |

---

## 🔨 Mini Project — Recon File Manager

**What it does:**
Complete recon pipeline — creates target list,
reads targets, simulates scan, saves results,
logs all activity, shows summary. Full error handling.

```python
def log(msg):
    with open("scan.log", "a") as f:
        t = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f.write(f"{t} - {msg}\n")

try:
    # Create target list
    targets = ["192.168.1.1", "10.0.0.1", "8.8.8.8"]
    with open("targets.txt", "w") as f:
        f.write("\n".join(targets))
    log("targets.txt created")

    # Read targets
    with open("targets.txt", "r") as f:
        targets = f.read().splitlines()

    # Scan and save results
    with open("results.txt", "w") as f:
        for ip in targets:
            result = f"{ip} - Port 80 Open"
            print(result)
            f.write(result + "\n")
            log(f"Scanned {ip}")

    print(f"\nScan Complete — {len(targets)} targets")

except FileNotFoundError as e:
    print("File error:", e)
    log(f"ERROR: {e}")
except Exception as e:
    print("Unexpected error:", e)
    log(f"CRITICAL: {e}")
```

**Generated Files:**
```
targets.txt  → 192.168.1.1 / 10.0.0.1 / 8.8.8.8
results.txt  → scan output per IP
scan.log     → timestamped activity log
```

---

## 🐛 Debugging Practice

5 errors found and fixed:

| # | Error | Wrong | Fix |
|---|-------|-------|-----|
| 1 | SyntaxError | `with open("targets.txt") as f` missing `:` | Added `:` at end |
| 2 | Bad practice | bare `except:` catches everything | `except Exception as e:` |
| 3 | SyntaxError | `finally` missing `:` | `finally:` |
| 4 | UnsupportedOperation | `open("log.txt", "r")` then `f.write()` | Change to `"a"` or `"w"` mode |
| 5 | AttributeError | `os.path.exist()` — doesn't exist | `os.path.exists()` with `s` |

```python
# Error 1 — missing colon
with open("targets.txt") as f:     # added :
    content = f.read()

# Error 2 — bare except → specific
except Exception as e:
    print("Error:", e)

# Error 3 — finally missing colon
finally:                            # added :
    print("Done")

# Error 4 — wrong file mode
f = open("log.txt", "a")           # changed r to a
f.write("Scan complete")

# Error 5 — typo in method name
if os.path.exists("file.txt"):      # added s
    print("File found")
```

---

## ❓ Interview Questions

**Q1: Difference between `"w"` and `"a"` mode?**
> `"w"` creates a new file or completely overwrites
> existing content — all previous data is lost.
> `"a"` appends to the end of existing content —
> previous data is preserved.
> Use `"w"` for fresh reports. Use `"a"` for logs
> that grow over time.

**Q2: Why use `with open()` instead of `open()`?**
> `with open()` is a context manager — it automatically
> closes the file when the block ends, even if an
> exception occurs. Without it, forgetting `f.close()`
> causes file locks, data corruption, or resource leaks.
> Always use `with open()` in professional code.

**Q3: Difference between `except Exception` and bare `except`?**
> `except Exception as e` catches all standard Python
> exceptions and gives you the error message via `e`.
> Bare `except:` catches EVERYTHING — including
> `SystemExit`, `KeyboardInterrupt` (Ctrl+C), and
> `GeneratorExit` which should never be suppressed.
> Bare `except` is dangerous and considered bad practice.

---

## ❌ Mistakes I Made Today

```python
# WRONG — file opened in read mode then written to
f = open("log.txt", "r")
f.write("data")            # UnsupportedOperation

# CORRECT — use write or append mode
f = open("log.txt", "a")
f.write("data")

# WRONG — typo in os method
os.path.exist("file.txt")   # AttributeError

# CORRECT
os.path.exists("file.txt")  # note the 's'

# WRONG — bare except hides errors
except:
    print("Error")

# CORRECT — always catch specifically
except Exception as e:
    print(f"Error: {e}")
```

---

## 🔐 Hacker Application

```python
import os
from datetime import datetime

def load_wordlist(filepath):
    """Load password wordlist — handles all file errors"""
    try:
        with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
            passwords = [line.strip() for line in f if line.strip()]
        print(f"[+] Loaded {len(passwords)} passwords")
        return passwords
    except FileNotFoundError:
        print(f"[-] Wordlist not found: {filepath}")
        return []
    except PermissionError:
        print(f"[-] Permission denied: {filepath}")
        return []

def save_results(results, output_file):
    """Save scan results — handles write errors"""
    try:
        with open(output_file, "w") as f:
            f.write("=" * 50 + "\n")
            f.write(f"SCAN RESULTS — {datetime.now()}\n")
            f.write("=" * 50 + "\n\n")
            for result in results:
                f.write(result + "\n")
        print(f"[+] Saved to {output_file}")
    except PermissionError:
        print(f"[-] Cannot write to {output_file}")

def log_activity(message, level="INFO"):
    """Append timestamped entry to activity log"""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("activity.log", "a") as f:
        f.write(f"{timestamp} [{level}] {message}\n")

# Usage — same pattern used by Hydra, Nmap, Metasploit
wordlist = load_wordlist("rockyou.txt")
log_activity("Wordlist loaded")
log_activity("Scan started on 192.168.1.0/24", "INFO")
```

**Real tools using file handling:**

| Tool | File Handling Usage |
|------|-------------------|
| Hydra | Reads wordlist line by line from file |
| Nmap | Reads target list `-iL targets.txt`, writes `-oN output.txt` |
| Metasploit | Reads/writes session logs and workspace files |
| Burp Suite | Saves request/response logs to files |
| Aircrack-ng | Reads capture files, reads wordlist |

---

## 📊 Day Score

| Category | Score |
|----------|-------|
| Exercise 1 — Target List | ✅ Good |
| Exercise 2 — Safe Calculator | ✅ Excellent |
| Exercise 3 — Wordlist Processor | ✅ Perfect |
| Exercise 4 — Log Writer | ✅ Perfect |
| Exercise 5 — File Scanner | ✅ Excellent |
| Mini Project — Recon Manager | ✅ Professional |
| Debug Fix — 5 errors | ✅ |
| Interview Questions | ✅ All correct |
| **Total** | **9/10** |

---

## 🔗 Connect

[![Portfolio](https://img.shields.io/badge/Portfolio-000000?style=flat&logo=vercel&logoColor=white)](https://mithleshrana450.github.io/mithleshrana-portfolio/)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2?style=flat&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/mithleshrana450/)
[![GitHub](https://img.shields.io/badge/GitHub-181717?style=flat&logo=github&logoColor=white)](https://github.com/Mithleshrana450)

---

<div align="center">

**[← Previous Day](../day-08-string-manipulation/)** • **[🏠 Back to Home](../README.md)** • **[Next Day →](../day-10-modules-regex/)**

*Part of [Python for Ethical Hacking — 4 Month Journey](../README.md)*

</div>