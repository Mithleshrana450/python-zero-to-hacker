<div align="center">

# 🐍 Day 12 — Socket Programming

![Day](https://img.shields.io/badge/Day-12-blue?style=for-the-badge)
![Phase](https://img.shields.io/badge/Phase-2%20Intermediate-orange?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Complete-brightgreen?style=for-the-badge)

> *"Sockets are the foundation of every network tool ever built. Master this and you own the network."*

[← Previous Day](../day-11-oop/) • [🏠 Home](../README.md) • [Next Day →](../day-13-json-api/)

</div>

---

## 📋 Overview

| | |
|---|---|
| 📅 **Date** | July 2026 |
| 🎯 **Goal** | Build real network tools using Python sockets |
| 📦 **Files** | 10 Python files |
| ✅ **Status** | Complete |

---

## 🧠 What I Learned Today

- Socket creation — `AF_INET`, `SOCK_STREAM`, `SOCK_DGRAM`
- TCP vs UDP — connection-based vs connectionless
- `connect()` vs `connect_ex()` — exception vs return code
- `settimeout()` — critical for scanners
- `bind()`, `listen()`, `accept()` — server socket lifecycle
- Banner grabbing — reading service response headers
- HTTP GET request over raw socket
- DNS resolution — `gethostbyname()`, `gethostbyaddr()`
- `getservbyport()` — port to service name lookup
- Threading for fast parallel port scanning
- Thread lock — preventing race conditions
- Complete port scanner with report saving

---

## 📁 File Structure

```
day-12-socket-programming/
│
├── 📄 socket_basics.py        ← socket creation, types, options
├── 📄 port_checker.py         ← is_port_open() function
├── 📄 port_scanner.py         ← input-based port range scanner
├── 📄 banner_grabber.py       ← grab service banners from open ports
├── 📄 server.py               ← TCP server — bind, listen, accept
├── 📄 client.py               ← TCP client — connect, send, receive
├── 📄 dns_resolver.py         ← hostname → IP + port 80 check table
├── 📄 professional_scanner.py ← full scanner: scan + banner + report + time
├── 📄 hacker_application.py   ← OOP threaded port scanner
├── 📄 debugging.py            ← 5 socket errors fixed
└── 📄 README.md
```

---

## 💡 Key Concepts

### Socket Creation
```python
import socket

# TCP socket — reliable, connection-based (most common)
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# UDP socket — fast, connectionless
udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# AF_INET  = IPv4
# AF_INET6 = IPv6
# SOCK_STREAM = TCP
# SOCK_DGRAM  = UDP
```

### connect() vs connect_ex()
```python
# connect() — raises exception if connection fails
try:
    s.connect(("192.168.1.1", 80))
except ConnectionRefusedError:
    print("Port closed")

# connect_ex() — returns error code, no exception
result = s.connect_ex(("192.168.1.1", 80))
if result == 0:
    print("Port OPEN")    # 0 = success
else:
    print("Port CLOSED")  # non-zero = failed
# Use connect_ex() in scanners — cleaner, no exception overhead
```

### Port Checker — Core Scanner Function
```python
import socket

def is_port_open(ip, port, timeout=2):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(timeout)
    result = s.connect_ex((ip, port))
    s.close()
    return result == 0

ip    = socket.gethostbyname("scanme.nmap.org")
ports = [22, 80, 443, 9999]

for port in ports:
    try:
        service = socket.getservbyport(port)
    except:
        service = "Unknown"
    status = "Open" if is_port_open(ip, port) else "Closed"
    print(f"Port {port:<6} {service:<10} {status}")
```

### Banner Grabbing — Service Fingerprinting
```python
import socket

def grab_banner(host, port):
    try:
        s = socket.socket()
        s.settimeout(2)
        s.connect((host, port))

        if port == 80:    # HTTP needs a request first
            s.send(b"GET / HTTP/1.1\r\nHost: " + host.encode() + b"\r\n\r\n")

        banner = s.recv(1024).decode(errors="ignore").strip()
        s.close()
        return banner
    except:
        return "No banner"

# SSH banner reveals version — used in vulnerability matching
print(grab_banner("scanme.nmap.org", 22))
# SSH-2.0-OpenSSH_6.6.1p1 Ubuntu-2ubuntu2.13
```

### TCP Server + Client
```python
# server.py — run first
import socket

server = socket.socket()
server.bind(("localhost", 5000))   # bind to port
server.listen(1)                    # wait for 1 connection
print("Waiting for client...")

conn, addr = server.accept()        # blocks until client connects
print(f"Connected by: {addr}")
message = conn.recv(1024).decode()
print(f"Client says: {message}")
conn.close()
server.close()
```

```python
# client.py — run second
import socket

client = socket.socket()
client.connect(("localhost", 5000))
message = input("Enter message: ")
client.send(message.encode())       # must encode str → bytes
client.close()
```

### Threaded Port Scanner — Fast Scanning
```python
import socket
import threading

open_ports = []
lock = threading.Lock()    # prevent race conditions

def scan_port(ip, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.5)
        if s.connect_ex((ip, port)) == 0:
            with lock:              # thread-safe append
                open_ports.append(port)
        s.close()
    except:
        pass

ip      = "scanme.nmap.org"
threads = []

for port in range(1, 1025):
    t = threading.Thread(target=scan_port, args=(ip, port))
    threads.append(t)
    t.start()

for t in threads:
    t.join()               # wait for all threads to finish

print(f"Open ports: {sorted(open_ports)}")
```

### DNS Resolution
```python
import socket

# Hostname to IP
ip = socket.gethostbyname("google.com")
print("IP:", ip)

# IP to hostname
info = socket.gethostbyaddr("8.8.8.8")
print("Hostname:", info[0])

# Your machine
my_ip = socket.gethostbyname(socket.gethostname())
print("My IP:", my_ip)

# Port to service name
print(socket.getservbyport(22))    # ssh
print(socket.getservbyport(80))    # http
```

---

## 🏋️ Exercises Completed

| # | Exercise | Concept Practiced | Status |
|---|----------|-------------------|--------|
| 1 | `is_port_open()` with service lookup | `connect_ex`, `settimeout`, `getservbyport` | ✅ Perfect |
| 2 | Port range scanner with input | Loop + socket + error handling | ✅ Good |
| 3 | Banner grabber — SSH + HTTP | `recv`, HTTP GET over socket | ✅ Excellent |
| 4 | TCP server + client chat | `bind`, `listen`, `accept`, `send` | ✅ Perfect |
| 5 | DNS resolver table | `gethostbyname`, `connect_ex` | ✅ Excellent |

---

## 🔨 Mini Project — Professional Port Scanner

**What it does:**
Full-featured port scanner — hostname resolution,
custom port range, banner grabbing, report saving, scan timing

```python
import socket, time
from datetime import datetime

target   = input("Enter IP or hostname: ")
ip       = socket.gethostbyname(target)
start_t  = time.time()
report   = open("port_scan_report.txt", "w")

for port in range(start_port, end_port + 1):
    s = socket.socket()
    s.settimeout(1)
    if s.connect_ex((ip, port)) == 0:
        try:
            service = socket.getservbyport(port)
        except:
            service = "Unknown"

        # Banner grab
        try:
            if port == 80:
                s.send(b"GET / HTTP/1.1\r\nHost: " + target.encode() + b"\r\n\r\n")
            banner = s.recv(1024).decode(errors="ignore").strip()
        except:
            banner = "No Banner"

        print(f"Port: {port} | {service} | {banner[:50]}")
        report.write(f"Port: {port}\nService: {service}\nBanner: {banner}\n")
    s.close()

print(f"Scan time: {time.time() - start_t:.2f}s")
report.close()
```

---

## 🐛 Debugging Practice

5 errors found and fixed:

| # | Error | Wrong | Fix |
|---|-------|-------|-----|
| 1 | Missing socket type | `socket(AF_INET)` | `socket(AF_INET, SOCK_STREAM)` |
| 2 | Wrong connect args | `connect("ip", 80)` | `connect(("ip", 80))` — tuple |
| 3 | Wrong timeout type | `settimeout("5")` | `settimeout(5)` — int not string |
| 4 | Missing buffer size | `recv()` | `recv(1024)` |
| 5 | Wrong connect_ex args | `connect_ex("ip", 80)` | `connect_ex(("ip", 80))` — tuple |

```python
# All 5 fixed
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Fix 1
s.connect(("192.168.1.1", 80))                          # Fix 2
s.settimeout(5)                                         # Fix 3
data = s.recv(1024)                                     # Fix 4
result = s.connect_ex(("192.168.1.1", 80))              # Fix 5
```

---

## ❓ Interview Questions

**Q1: Difference between TCP and UDP?**
> TCP is connection-based — establishes a handshake
> before sending data, guarantees delivery and order.
> Used for HTTP, SSH, FTP — where reliability matters.
> UDP is connectionless — sends packets without handshake,
> no guaranteed delivery. Faster, used for DNS, video
> streaming, gaming where speed beats reliability.
> Port scanners use TCP to check if ports accept connections.

**Q2: What does `connect_ex()` return vs `connect()`?**
> `connect()` raises a `ConnectionRefusedError` exception
> if connection fails — requires try/except.
> `connect_ex()` returns an error code instead — 0 means
> success (port open), non-zero means failure (port closed).
> Port scanners use `connect_ex()` because calling
> exceptions thousands of times is slow and messy.

**Q3: Why do we need `settimeout()` in a port scanner?**
> Without timeout, the scanner waits forever for a response
> from filtered or unresponsive ports — it would hang.
> `settimeout(1)` tells the socket to give up after 1 second
> if no response. This is critical for performance —
> scanning 1024 ports without timeout could take hours.

---

## ❌ Mistakes I Made Today

```python
# WRONG — socket_basics.py was left empty
# Always write reference code even for basics

# WRONG — passing string to settimeout
s.settimeout("5")    # TypeError

# CORRECT — must be a number
s.settimeout(5)      # int or float

# WRONG — connect takes string + int as two args
s.connect("192.168.1.1", 80)    # TypeError

# CORRECT — must be a TUPLE
s.connect(("192.168.1.1", 80))  # always tuple

# WRONG — recv with no buffer
data = s.recv()      # TypeError — must specify size

# CORRECT
data = s.recv(1024)  # 1024 bytes buffer
```

---

## 🔐 Hacker Application

```python
import socket
import threading
import time
from datetime import datetime

class PortScanner:
    """OOP threaded port scanner — production quality"""

    def __init__(self, target, start_port=1, end_port=1024, timeout=0.5):
        self.target     = target
        self.start_port = start_port
        self.end_port   = end_port
        self.timeout    = timeout
        self.open_ports = []
        self.lock       = threading.Lock()

    def resolve_target(self):
        try:
            return socket.gethostbyname(self.target)
        except socket.gaierror:
            print(f"[-] Cannot resolve {self.target}")
            return None

    def scan_port(self, ip, port):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(self.timeout)
            if s.connect_ex((ip, port)) == 0:
                try:
                    service = socket.getservbyport(port)
                except:
                    service = "unknown"
                with self.lock:
                    self.open_ports.append((port, service))
            s.close()
        except:
            pass

    def run(self):
        ip = self.resolve_target()
        if not ip: return

        start = time.time()
        threads = [threading.Thread(target=self.scan_port, args=(ip, p))
                   for p in range(self.start_port, self.end_port + 1)]

        for t in threads: t.start()
        for t in threads: t.join()

        print("\n[RESULTS]")
        for port, svc in sorted(self.open_ports):
            print(f"  {port:<6} OPEN   {svc}")
        print(f"\n[*] {len(self.open_ports)} open ports in {time.time()-start:.2f}s")

scanner = PortScanner("scanme.nmap.org", 1, 1024)
scanner.run()
```

**Real tools built on Python sockets:**

| Tool | Socket Usage |
|------|-------------|
| Nmap (Python scripts) | `SOCK_STREAM` connect_ex for port detection |
| Netcat | Raw TCP send/receive |
| Metasploit | Socket-based reverse shell handlers |
| Scapy | Raw sockets for packet crafting |
| theHarvester | Sockets for DNS enumeration |

---

## 📊 Day Score

| Category | Score |
|----------|-------|
| Exercise 1 — Port checker | ✅ Perfect |
| Exercise 2 — Port scanner | ✅ Good |
| Exercise 3 — Banner grabber | ✅ Excellent |
| Exercise 4 — Server + Client | ✅ Perfect |
| Exercise 5 — DNS resolver | ✅ Excellent |
| Mini Project — Pro scanner | ✅ Outstanding |
| Hacker Application — OOP scanner | ✅ Professional |
| Debug Fix — 5 errors | ✅ All fixed |
| Interview Questions | ✅ |
| **Total** | **9/10** |

---

## 🔗 Connect

[![Portfolio](https://img.shields.io/badge/Portfolio-000000?style=flat&logo=vercel&logoColor=white)](https://mithleshrana450.github.io/mithleshrana-portfolio/)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2?style=flat&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/mithleshrana450/)
[![GitHub](https://img.shields.io/badge/GitHub-181717?style=flat&logo=github&logoColor=white)](https://github.com/Mithleshrana450)

---

<div align="center">

**[← Previous Day](../day-11-oop/)** • **[🏠 Back to Home](../README.md)** • **[Next Day →](../day-13-json-api/)**

*Part of [Python for Ethical Hacking — 4 Month Journey](../README.md)*

</div>
