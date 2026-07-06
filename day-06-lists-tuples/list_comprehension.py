# List comprehension:
# Given a list of numbers [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:

# Create new list of only even numbers
# Create new list of squares of odd numbers
# Create new list of numbers greater than 5

numbers = [1,2,3,4,5,6,7,8,9,10]

even_numbers = [i for i in numbers if i % 2 == 0]
print(f"Even numbers: {even_numbers}")

odd_squares = [i ** 2 for i in numbers if i % 2 != 0]
print(f"Odd squares: {odd_squares}")

greater_than_5 = [i for i in numbers if i > 5]
print(f"Greater than 5: {greater_than_5}")
