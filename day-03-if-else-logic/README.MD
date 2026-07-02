# Day 3 — If/Else & Logic Building

## What I Learned
- How Python makes decisions using if/elif/else
- Nested conditions — if inside if inside else
- Logical operators in conditions: and, or, not
- Input validation — always handle invalid inputs
- Slab-based calculation logic (real-world billing systems)
- How to build a basic login authentication system
- Leap year logic using combined conditions

## Files
- `conditions.py` — Positive, Negative, Zero checker
- `login_system.py` — Username and password authentication
- `grade_calculator.py` — Marks to grade converter with validation
- `electricity_bill.py` — Slab-based electricity bill calculator
- `leap_year.py` — Leap year checker using correct logic
- `atm_machine.py` — ATM simulator with PIN and balance logic
- `Debugging.py` — Found and fixed 5 syntax/logic errors

## Key Concepts

### If/Elif/Else Structure
```python
if condition:
    # runs if True
elif another_condition:
    # runs if first was False, this is True
else:
    # runs if ALL above were False
```

### Nested Conditions
```python
if username == correct_username:
    if password == correct_password:
        print("Login Successful")
    else:
        print("Wrong password")   # handles correct user, wrong pass
else:
    print("Username not found")
```

### Slab-Based Calculation (Important)
```python
# Wrong way — multiplies ALL units at slab rate
bill = units * 3   # incorrect for 150 units

# Correct way — each slab calculated separately
if units <= 100:
    bill = units * 2
elif units <= 200:
    bill = (100 * 2) + ((units - 100) * 3)
else:
    bill = (100 * 2) + (100 * 3) + ((units - 200) * 5)
```
This is how real electricity boards in India calculate bills.
BESCOM, MSEDCL, DGVCL all use this exact slab logic.

### Leap Year Logic
```python
year = int(input("Enter year: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(year, "is a leap year")
else:
    print(year, "is not a leap year")
```
Combined conditions using `and`, `or` in one line.

### Input Validation Rule
Always validate user input before processing:
```python
if marks > 100 or marks < 0:
    print("Invalid marks")
elif marks >= 90:
    print("A - Excellent")
```
Never trust raw input — this is critical in cybersecurity too.

## Mistakes I Made Today
- Login system was missing the wrong password case — silent failure
- Grade calculator had redundant conditions like `marks >= 90 and marks <= 100`
  — once inside elif chain, upper bound is already handled
- Electricity bill used flat rate instead of slab-based calculation
- Leap year was missing the else block — printed nothing for non-leap years
- ATM asked amount before PIN — logic order matters in real systems

## What I Learned From Mistakes
- Always handle ALL possible cases — no silent failures
- elif chains already eliminate upper bounds — don't repeat them
- Real-world billing is slab-based, not flat-rate
- Always validate input — negative marks, zero amounts don't make sense
- Order of logic matters — PIN before amount, just like real ATMs

## Debugging Practice
Found and fixed all 5 errors:
1. Missing closing `)` in int(input("Enter age: ")
2. Missing `:` after if condition
3. `Else:` capital E should be `else:`
4. Missing `:` after final else
5. Wrong indentation inside nested blocks

## Interview Questions Answered
1. `=` assigns a value to a variable. `==` compares two values and
   returns True or False. Using = inside a condition is a common bug.
2. Yes — if can exist without else. The block simply does nothing
   if the condition is False.
3. Only the FIRST True elif runs. Python stops checking remaining
   elif blocks once it finds a match.

## Hacker Application
```python
# Port risk classifier — real scanner logic
port = int(input("Enter port number: "))

if port == 22:
    print("SSH — Remote access — HIGH RISK if open to public")
elif port == 80:
    print("HTTP — Web server — check for vulnerabilities")
elif port == 443:
    print("HTTPS — check SSL certificate expiry")
elif port == 21:
    print("FTP — HIGH RISK — usually unencrypted")
elif port == 3306:
    print("MySQL — CRITICAL if exposed publicly")
else:
    print("Unknown port — investigate further")
```
This exact if/elif logic is the core of Nmap's port classification.
You will build the full version in Phase 11.

## Status
✅ Day 3 Complete — If/Else, Nested Conditions, Logic Building
📁 Repo: https://github.com/Mithleshrana450/python-zero-to-hacker