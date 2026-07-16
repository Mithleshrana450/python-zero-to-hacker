<div align="center">

# 🐍 Day 11 — Object Oriented Programming (OOP)

![Day](https://img.shields.io/badge/Day-11-blue?style=for-the-badge)
![Phase](https://img.shields.io/badge/Phase-2%20Intermediate-orange?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Complete-brightgreen?style=for-the-badge)

> *"Every major hacking framework — Metasploit, Scapy, Burp Suite — is built with OOP. This is where scripts become software."*

[← Previous Day](../day-10-modules-regex/) • [🏠 Home](../README.md) • [Next Day →](../day-12-socket-programming/)

</div>

---

## 📋 Overview

| | |
|---|---|
| 📅 **Date** | July 2026 |
| 🎯 **Goal** | Build professional tools using Object Oriented Programming |
| 📦 **Files** | 8 Python files |
| ✅ **Status** | Complete |

---

## 🧠 What I Learned Today

- Class definition and object creation
- `__init__` constructor — initializing attributes
- Instance attributes vs class attributes
- `self` — reference to current object
- Encapsulation — private attributes with `__`
- Inheritance — child class reusing parent code
- `super()` — calling parent class methods
- Method overriding — child redefines parent method
- Polymorphism — same method, different behavior
- Magic methods — `__str__`, `__repr__`, `__eq__`, `__len__`, `__contains__`
- Composition — objects containing other objects
- `NotImplementedError` — enforcing method implementation
- Class attributes — shared across all instances

---

## 📁 File Structure

```
day-11-oop/
│
├── 📄 classes_basics.py         ← Student class with marks, grades, __str__
├── 📄 encapsulation.py          ← BankAccount with private __balance
├── 📄 inheritance.py            ← SecurityTool → PortScanner, WebScanner, PasswordCracker
├── 📄 polymorphism.py           ← loop calling run() on different tool types
├── 📄 magic_methods.py          ← HashResult with __eq__, __len__, __contains__
├── 📄 hacking_tool_framework.py ← full OOP toolkit: HackingTool base + 3 subclasses
├── 📄 hacker_application.py     ← Target + Vulnerability classes with risk scoring
├── 📄 debugging.py              ← 5 OOP errors found and fixed
└── 📄 README.md
```

---

## 💡 Key Concepts

### Class & Object — Basics
```python
class Hacker:                           # class blueprint
    def __init__(self, name, level):    # constructor
        self.name  = name               # instance attribute
        self.level = level

    def introduce(self):                # method
        print(f"I am {self.name}, level {self.level}")

# Creating objects (instances)
h1 = Hacker("Mithu", "Beginner")       # object 1
h2 = Hacker("Root",  "Expert")         # object 2

h1.introduce()    # I am Mithu, level Beginner
h2.introduce()    # I am Root, level Expert
```

### Instance vs Class Attributes
```python
class Scanner:
    scan_count = 0             # class attribute — shared by ALL instances

    def __init__(self, ip):
        self.ip = ip           # instance attribute — unique per object
        Scanner.scan_count += 1

s1 = Scanner("192.168.1.1")
s2 = Scanner("192.168.1.2")
print(Scanner.scan_count)      # 2 — shared counter
print(s1.ip)                   # 192.168.1.1 — unique to s1
```

### Encapsulation — Private Attributes
```python
class BankAccount:
    def __init__(self, balance=0):
        self.__balance = balance    # __ makes it private

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
        else:
            print("Invalid deposit!")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient balance!")

    def get_balance(self):
        return self.__balance

    def transfer(self, other, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            other.deposit(amount)

a1 = BankAccount(1000)
a2 = BankAccount(500)
a1.transfer(a2, 400)
print(a1.get_balance())    # 600
print(a2.get_balance())    # 900
```

### Inheritance — Tool Hierarchy
```python
class SecurityTool:                      # Parent
    def __init__(self, name, version):
        self.name    = name
        self.version = version

    def run(self):
        print(f"Running {self.name}...")

    def __str__(self):
        return f"{self.name} v{self.version}"

class PortScanner(SecurityTool):         # Child
    def __init__(self, name, version, target):
        super().__init__(name, version)  # call parent __init__
        self.target = target

    def run(self):                       # override parent method
        print(f"Scanning ports on {self.target}")

    def __str__(self):
        return f"PortScanner: {self.name} v{self.version}, Target: {self.target}"

class WebScanner(SecurityTool):
    def __init__(self, name, version, target):
        super().__init__(name, version)
        self.target = target

    def run(self):
        print(f"Scanning website {self.target}")

class PasswordCracker(SecurityTool):
    def __init__(self, name, version, wordlist):
        super().__init__(name, version)
        self.wordlist = wordlist

    def run(self):
        print(f"Cracking passwords using {self.wordlist}")
```

### Polymorphism — Same Call, Different Behavior
```python
tools = [
    PortScanner("Nmap", "1.0", "192.168.1.1"),
    WebScanner("Nikto", "2.1", "example.com"),
    PasswordCracker("John", "3.0", "rockyou.txt")
]

# Same method call — completely different output per class
for tool in tools:
    print(tool)    # calls each class's __str__
    tool.run()     # calls each class's run()
```

### Magic Methods
```python
import hashlib

class HashResult:
    def __init__(self, password):
        self.password = password
        self.md5    = hashlib.md5(password.encode()).hexdigest()
        self.sha256 = hashlib.sha256(password.encode()).hexdigest()

    def __str__(self):          # print(obj) — human readable
        return f"Password: {self.password}\nMD5: {self.md5}"

    def __eq__(self, other):    # obj1 == obj2
        return self.md5 == other.md5

    def __len__(self):          # len(obj)
        return len(self.password)

    def __contains__(self, char):  # 'a' in obj
        return char in self.password

h1 = HashResult("admin123")
h2 = HashResult("admin123")
print(h1)              # Password: admin123\nMD5: ...
print(h1 == h2)        # True — same MD5
print(len(h1))         # 8
print("a" in h1)       # True
```

### Composition — Objects Inside Objects
```python
# Target CONTAINS Vulnerability objects
class Vulnerability:
    def __init__(self, cve, severity, description):
        self.cve         = cve
        self.severity    = severity
        self.description = description

    def __str__(self):
        return f"[{self.severity}] {self.cve}: {self.description}"

class Target:
    def __init__(self, ip):
        self.ip    = ip
        self.vulns = []         # list of Vulnerability objects

    def add_vuln(self, vuln):
        self.vulns.append(vuln)

    def get_risk_level(self):
        critical = sum(1 for v in self.vulns if v.severity == "CRITICAL")
        if critical > 0: return "CRITICAL"
        if len(self.vulns) > 3: return "HIGH"
        return "MEDIUM"
```

---

## 🏋️ Exercises Completed

| # | Exercise | Concept Practiced | Status |
|---|----------|-------------------|--------|
| 1 | Student class — marks, grades, __str__ | Class basics, methods | ✅ Perfect |
| 2 | BankAccount — private balance, transfer | Encapsulation | ✅ Excellent |
| 3 | SecurityTool hierarchy — 3 subclasses | Inheritance, super() | ✅ Excellent |
| 4 | Polymorphic tool loop | Polymorphism | ✅ Perfect |
| 5 | HashResult magic methods | __eq__, __len__, __contains__ | ✅ |

---

## 🔨 Mini Project — Hacking Tool Framework

**What it does:**
Complete OOP-based hacking toolkit — base class
`HackingTool` with shared functionality, 3 specialized
subclasses, class-level tool counter, result saving

```python
class HackingTool:
    tool_count = 0             # tracks total tools created

    def __init__(self, name, version, author):
        self.name    = name
        self.version = version
        self.author  = author
        self.results = []
        HackingTool.tool_count += 1

    def run(self):
        pass                   # subclasses must implement

    def save_results(self, filename):
        with open(filename, "w") as f:
            for r in self.results:
                f.write(r + "\n")

    def show_banner(self):
        print(f"{self.name} v{self.version} by {self.author}")

    def __str__(self):
        return f"{self.name} v{self.version}"

class PortScanner(HackingTool):
    def run(self):
        for p in self.ports:
            self.results.append(f"Port {p} is Open")
        print("Port Scan Completed")

class BruteForcer(HackingTool):
    def run(self):
        self.results.append(f"Password found using {self.wordlist}")
        print("Brute Force Completed")

class OSINTTool(HackingTool):
    def run(self):
        self.results.append(f"Information collected for {self.target}")
        print("OSINT Completed")

print("Total Tools:", HackingTool.tool_count)   # 3
```

---

## 🐛 Debugging Practice

5 errors found and fixed:

| # | Error | Wrong | Fix |
|---|-------|-------|-----|
| 1 | SyntaxError | `class Scanner` missing `:` | `class Scanner:` |
| 2 | AttributeError | `ip = ip` not `self.ip` | `self.ip = ip` |
| 3 | TypeError | `super().__init__()` missing `ip` | `super().__init__(ip)` |
| 4 | TypeError | `def scan():` missing `self` | `def scan(self):` |
| 5 | UnboundLocalError | `count += 1` not class-level | `Tool.count += 1` |

```python
# All 5 fixed
class Scanner:                          # Fix 1 — added colon
    def __init__(self, ip):
        self.ip = ip                    # Fix 2 — self.ip not ip

class AdvancedScanner(Scanner):
    def __init__(self, ip, port):
        super().__init__(ip)            # Fix 3 — pass ip to parent
        self.port = port

    def scan(self):                     # Fix 4 — added self
        super().scan()
        print(f"Port: {self.port}")

class Tool:
    count = 0
    def __init__(self):
        Tool.count += 1                 # Fix 5 — Tool.count not count
```

---

## ❓ Interview Questions

**Q1: Difference between a class and an object?**
> A class is a blueprint or template — it defines
> attributes and methods but holds no data itself.
> An object is an instance of a class — it's the actual
> thing created from the blueprint with real data.
> Example: `Scanner` is the class. `s = Scanner("192.168.1.1")`
> creates an object with real IP data.

**Q2: What does `super()` do?**
> `super()` gives access to the parent class from
> inside a child class. Most commonly used in `__init__`
> to call the parent constructor so inherited attributes
> are initialized properly without rewriting them.
> Without `super().__init__()`, the parent's attributes
> don't get created.

**Q3: Difference between `__str__` and `__repr__`?**
> `__str__` is for humans — called by `print()`,
> should be readable and friendly.
> `__repr__` is for developers — called in the REPL
> and by `repr()`, should be unambiguous and show
> how to recreate the object.
> If only `__str__` is defined, Python falls back to it.
> If only `__repr__` is defined, it's used for both.

---

## ❌ Mistakes I Made Today

```python
# WRONG — HashResult taking hash as parameter
class HashResult:
    def __init__(self, password, md5, sha256):
        self.md5 = md5          # manually passed in

h1 = HashResult("admin", "abc123", "xyz")  # defeats the purpose

# CORRECT — generate hashes inside class
class HashResult:
    def __init__(self, password):
        self.password = password
        self.md5    = hashlib.md5(password.encode()).hexdigest()
        self.sha256 = hashlib.sha256(password.encode()).hexdigest()

h1 = HashResult("admin")        # class handles hashing itself

# WRONG — class attribute modified without class name
class Tool:
    count = 0
    def __init__(self):
        count += 1              # UnboundLocalError

# CORRECT
class Tool:
    count = 0
    def __init__(self):
        Tool.count += 1         # must prefix with class name
```

---

## 🔐 Hacker Application

```python
import hashlib
from datetime import datetime

class Vulnerability:
    def __init__(self, cve, severity, description):
        self.cve         = cve
        self.severity    = severity
        self.description = description
        self.found_at    = datetime.now()

    def __str__(self):
        return f"[{self.severity}] {self.cve}: {self.description}"

class Target:
    def __init__(self, ip, hostname="Unknown"):
        self.ip         = ip
        self.hostname   = hostname
        self.open_ports = []
        self.services   = {}
        self.vulns      = []

    def add_port(self, port, service):
        self.open_ports.append(port)
        self.services[port] = service

    def add_vuln(self, vuln):
        self.vulns.append(vuln)

    def get_risk_level(self):
        critical = sum(1 for v in self.vulns if v.severity == "CRITICAL")
        if critical > 0:        return "CRITICAL"
        if len(self.vulns) > 3: return "HIGH"
        if len(self.open_ports) > 5: return "MEDIUM"
        return "LOW"

    def generate_report(self):
        print(f"\n{'='*50}")
        print(f"TARGET REPORT: {self.ip}")
        print(f"{'='*50}")
        print(f"Hostname   : {self.hostname}")
        print(f"Risk Level : {self.get_risk_level()}")
        print(f"Open Ports : {self.open_ports}")
        print(f"Vulns Found: {len(self.vulns)}")
        for v in self.vulns:
            print(f"  {v}")

# This exact architecture is used in Metasploit's
# host/vulnerability tracking system
target = Target("192.168.1.1", "webserver.local")
target.add_port(22,  "SSH")
target.add_port(80,  "HTTP")
target.add_vuln(Vulnerability("CVE-2021-44228", "CRITICAL", "Log4Shell RCE"))
target.generate_report()
```

**Real tools using OOP:**

| Tool | OOP Usage |
|------|-----------|
| Metasploit | Module class hierarchy — every exploit is a class |
| Scapy | Packet class with inheritance per protocol |
| Burp Suite | Extension API built entirely on classes |
| theHarvester | Harvester base class with source subclasses |
| Impacket | Protocol implementations as class hierarchies |

---

## 📊 Day Score

| Category | Score |
|----------|-------|
| Exercise 1 — Student class | ✅ Perfect |
| Exercise 2 — BankAccount | ✅ Excellent |
| Exercise 3 — Inheritance | ✅ Excellent |
| Exercise 4 — Polymorphism | ✅ Perfect |
| Exercise 5 — Magic methods | ✅ |
| Debug Fix — 5 errors | ✅ All fixed |
| Mini Project — Hacking Framework | ✅ Excellent |
| Hacker Application | ✅ Professional |
| **Total** | **8.5/10** |

---

## 🔗 Connect

[![Portfolio](https://img.shields.io/badge/Portfolio-000000?style=flat&logo=vercel&logoColor=white)](https://mithleshrana450.github.io/mithleshrana-portfolio/)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2?style=flat&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/mithleshrana450/)
[![GitHub](https://img.shields.io/badge/GitHub-181717?style=flat&logo=github&logoColor=white)](https://github.com/Mithleshrana450)

---

<div align="center">

**[← Previous Day](../day-10-modules-regex/)** • **[🏠 Back to Home](../README.md)** • **[Next Day →](../day-12-socket-programming/)**

*Part of [Python for Ethical Hacking — 4 Month Journey](../README.md)*

</div>
