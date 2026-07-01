# Day 2 — Operators & Type Casting

## What I Learned
- All 7 types of Python operators: Arithmetic, Comparison, Logical,
  Assignment, Identity, Membership, Bitwise
- Deep dive into type casting: str → int, str → float, int → str, int → bool
- Truthiness concept in Python — why 0, "", None are False
- Floor division `//` vs regular division `/`
- Modulus `%` operator and how it checks even/odd logic
- XOR bitwise operator and its role in encryption
- Assignment shorthand operators: `+=`, `-=`, `*=`, `//=`

## Files
- `arithmetic.py` — All 7 arithmetic operations on user input
- `gst_calculator.py` — Takes price as string input, casts to float, adds 18% GST
- `bool_values.py` — Demonstrates truthiness of 0, 1, "", "hacker", None
- `calculator.py` — Mini calculator taking operator as input from user

## Key Concepts

### Floor Division vs Regular Division
```python
print(17 / 5)    # 3.4  → always returns float
print(17 // 5)   # 3    → always returns int (floors the result)
print(-17 // 5)  # -4   → floors DOWN, not toward zero
```

### Truthiness in Python
Python evaluates values as True or False in conditions.
Empty = False. Non-empty = True.
```python
bool(0)        # False — zero is falsy
bool(1)        # True  — non-zero is truthy
bool("")       # False — empty string is falsy
bool("hacker") # True  — non-empty string is truthy
bool(None)     # False — None is always falsy
```

### XOR — Why Hackers Use It
XOR (`^`) is a bitwise operator that compares bits of two numbers.
It is the foundation of many encryption algorithms because:
- XOR encrypts a value with a key
- XOR with the SAME key decrypts it back
- Simple, fast, reversible
```python
message   = 72     # ASCII value of 'H'
key       = 25
encrypted = message ^ key    # encrypt
decrypted = encrypted ^ key  # decrypt — same operation reverses it
print(decrypted)             # 72 — back to original
```
This exact logic appears in real malware analysis and CTF challenges.

### Type Casting Rules
```python
# input() ALWAYS returns string — cast before math
age   = int(input("Enter age: "))
price = float(input("Enter price: "))

# Can't mix str and int in concatenation
code    = 404
message = "Error: " + str(code)   # must cast int to str first
```

## Mistakes I Made Today
- Used hardcoded values instead of input() in Exercise 3 (GST)
- Used unnecessary parentheses around string values: ("249.99") → "249.99"
- Jumped to 750 in one step in Exercise 4 instead of using multiple operators
- Calculator didn't take operator as input — printed all results at once

## What I Learned From Mistakes
- Always use input() when the requirement says "take from user"
- Parentheses around a single value don't make a tuple — they're just noise
- Exercises are designed to teach a concept — don't shortcut them
- A real calculator takes ONE operation as input and returns ONE result

## Hacker Application
- Port scanners use arithmetic operators to calculate port ranges
- Modulus `%` is used in brute force loop logic
- XOR `^` is the base of encryption/decryption scripts
- Type casting is critical — port numbers, IPs must be correct types
  before being passed into socket connections

## Interview Questions Answered
1. `/` always returns float. `//` always returns int (floor division)
2. `bool("")` returns False — empty string is falsy in Python
3. You cannot concatenate str and int directly — must cast with str()

## Status
✅ Day 2 Complete — Operators, Type Casting, Truthiness, XOR intro
📁 Repo: https://github.com/Mithleshrana450/python-zero-to-hacker