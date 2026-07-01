# F. Mini Project — Simple Calculator
# Build a calculator that:
#     Takes two numbers as input from user
#     Takes operator as input (+, -, *, /)
#     Prints the correct result
#     Handles division —
#     if user enters 0 as second number,
#     print "Cannot divide by zero"
#     (use only what you know — print and comparison, no if/else yet — just use bool to show the condition for now)

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
op = input("Enter operator (+, -, *, /): ")

if op == "+":
    print("Result:", a + b)
elif op == "-":
    print("Result:", a - b)
elif op == "*":
    print("Result:", a * b)
elif op == "/":
    if b == 0:
        print("Cannot divide by zero")
    else:
        print("Result:", a / b)
else:
    print("Invalid operator")