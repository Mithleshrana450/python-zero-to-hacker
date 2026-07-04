# Create a recursive function factorial(n) that calculates n!
# factorial(5) = 5 × 4 × 3 × 2 × 1 = 120


def factorial(n):
    if n == 0 or n == 1:   # Base case
        return 1
    else:
        return n * factorial(n - 1)   # Recursive call

    # Example
print(factorial(5))