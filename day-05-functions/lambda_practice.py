# Lambda to return the square of a number
square = lambda x: x * x

# Lambda to check if a number is even
is_even = lambda x: x % 2 == 0

# Lambda to convert a string to uppercase
to_upper = lambda s: s.upper()

# Example
print(square(5))          # 25
print(is_even(8))         # True
print(is_even(7))         # False
print(to_upper("hello"))  # HELLO