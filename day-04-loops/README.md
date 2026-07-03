# Day 4 — Loops (for & while)

## What I Learned
- for loop — iterate over a range or list
- while loop — repeat until condition becomes False
- range() — 3 ways to use: range(n), range(start, stop), range(start, stop, step)
- break — exit loop completely
- continue — skip current iteration, continue loop
- pass — placeholder, does nothing
- for/else — else runs only if loop never hit break
- Nested loops — loop inside a loop for patterns
- while True — standard pattern for input-until-correct

## Files
- `for_loop.py` — sum of numbers, multiplication table
- `while_loop.py` — number guessing game, countdown
- `patterns.py` — star pattern using nested loops
- `password_system.py` — 3 attempt login with for/else
- `port_scanner_sim.py` — simulated port scanner 1-1024


## Key Concepts

### range() — 3 Ways
```python
range(5)          # 0, 1, 2, 3, 4
range(1, 6)       # 1, 2, 3, 4, 5
range(2, 10, 2)   # 2, 4, 6, 8 — step of 2
range(10, 0, -1)  # 10, 9, 8... 1 — countdown
```

### break vs continue
```python
# break — exits loop completely
for i in range(10):
    if i == 5:
        break        # stops — never reaches 6, 7, 8, 9
    print(i)         # prints 0 1 2 3 4

# continue — skips current round, loop keeps going
for i in range(10):
    if i == 5:
        continue     # skips 5, continues to 6, 7, 8, 9
    print(i)         # prints 0 1 2 3 4 6 7 8 9
```

### for/else — Advanced Pattern
```python
# else on a for loop runs ONLY if break was never hit
for i in range(3):
    password = input("Enter password: ")
    if password == "hacker123":
        print("Access granted")
        break
else:
    print("Account locked")   # runs only after 3 failed attempts
```

### while True — Standard Input Loop
```python
# Correct pattern for input-until-correct
while True:
    guess = int(input("Guess: "))
    attempts += 1
    if guess == secret:
        print("Correct in", attempts, "attempts")
        break         # only exit point
    else:
        print("Wrong — try again")
```

### Print Inside vs Outside Loop
```python
# Wrong — prints partial sum every iteration
for i in range(1, n+1):
    total += i
    print("Sum =", total)   # inside loop

# Correct — prints final answer only
for i in range(1, n+1):
    total += i
print("Sum =", total)       # outside loop
```
One indentation level difference = completely different behavior.

### Nested Loops — Pattern Logic
```python
# range must start from 1 to get correct star count
for i in range(1, 6):      # i = 1, 2, 3, 4, 5
    for j in range(i):     # prints i stars per row
        print("*", end="")
    print()                # newline after each row
```

## Mistakes I Made Today
- Print statement was inside loop instead of outside —
  printed running total instead of final sum
- Pattern used range(a) instead of range(1, a+1) —
  caused blank first line and one less star at end
- Guessing game used while(secret == 7) — always True,
  never naturally stops. Correct pattern is while True with break
- Debug fix changed condition instead of adding increment —
  wrong diagnosis of the bug
- range(2, 10, 2) answered as 3,5,7,9 — correct is 2,4,6,8

## What I Learned From Mistakes
- Always check WHERE your print statement is — inside vs outside loop
- range() for patterns must start at 1 not 0
- while True + break is the standard loop-until-correct pattern
- When debugging while loops, first check if increment is missing
- range(start, stop, step) — start is INCLUDED, stop is EXCLUDED

## Debugging Practice
3 errors found and fixed:
1. Missing `:` after for loop → `for i in range(1, 6):`
2. Missing `count += 1` inside while loop → caused infinite loop
3. Missing `:` after if statement → `if i == 5:`

## Interview Questions Answered
1. break exits the loop completely — remaining iterations are cancelled.
   continue skips only the current iteration — loop keeps running.
   break = emergency exit. continue = skip this round.
2. Forgetting increment in while loop makes condition permanently True —
   infinite loop. Must press Ctrl+C to force stop.
3. range(2, 10, 2) generates: 2, 4, 6, 8
   Start=2, Stop=10 (excluded), Step=2

## Hacker Application
```python
# Brute force structure — exact logic used in real tools
passwords = ["admin", "1234", "password", "hacker123"]
correct = "hacker123"
attempts = 0

for pwd in passwords:
    attempts += 1
    if pwd == correct:
        print("Password cracked:", pwd)
        print("Attempts:", attempts)
        break
else:
    print("Password not in wordlist")
```
This is the core logic of Hydra, Medusa, and every
password cracking tool — just with larger wordlists.

```python
# Port scanner core logic
open_ports = [22, 80, 443, 3306, 8080]
count = 0

for port in range(1, 1025):
    if port in open_ports:
        print("Port", port, "OPEN")
        count += 1

print("Scan complete —", count, "open ports found")
```
This exact loop structure is inside Nmap and every
port scanner ever built. You just wrote the foundation.

## Status
✅ Day 4 Complete — for loop, while loop, break, continue, patterns
📁 Repo: https://github.com/Mithleshrana450/python-zero-to-hacker