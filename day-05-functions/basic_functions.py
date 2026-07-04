# Basic calculator function:
#     Create a function calculate(a, b, op).
#     takes two numbers and an operator (+, -, *, /) and returns the result.

def calculate(a, b,op):
    if(op == "+"):
        return a+b
    if(op == "-"):
        return a-b
    if(op == "*"):
        return a*b
    if(op == "/"):
        return a/b
print(calculate(10, 20,"+"))
print(calculate(10, 20,"-"))
print(calculate(10, 20,"*"))
print(calculate(10, 20,"/"))