# Day 1 — Variables, Data Types & Input/Output

## What I Learned
- How to create and use variables in Python (Python is dynamically typed — no need to declare type)
- Core data types: `int`, `float`, `str`, `bool`
- How `input()` works — it always returns a string, even for numbers
- Type casting using `int()`, `float()`, `str()` to convert between types
- Using `type()` to check a variable's data type
- Basic `print()` formatting to display output

## Files
- `personal_info_card.py` — Takes user's name, age, and favorite programming language as input, then prints a formatted intro card.

## Key Concept
`input()` always returns a string. If you need a number, you must cast it:
```python
age = int(input("Enter your age: "))
```
Forgetting this is one of the most common beginner bugs — it causes type errors or string concatenation instead of math operations.

## Hacker Application
Ethical hackers use variables constantly to store recon data (IPs, ports, usernames). Type casting matters here too — e.g. a port number entered by a user must be cast to `int` before being used in a socket connection.

## Status
✅ Day 1 complete — Mentorship by Claude