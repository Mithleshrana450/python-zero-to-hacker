# Positive, Negative or Zero:
#     Take a number as input.
#     Print whether it is "Positive", "Negative", or "Zero".

number = int(input("Enter the number: "))
if number > 0:
    print("Positive number")
elif number < 0:
    print("Negative number")
else:
    print("Zero")