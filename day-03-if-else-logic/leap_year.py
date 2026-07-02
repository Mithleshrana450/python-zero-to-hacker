# Take a year as input. Check if it's a leap year:
#     Divisible by 4 AND not divisible by 100 → leap year
#     Divisible by 400 → leap year
#     Everything else → not a leap year

year = int(input("Enter year: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(year, "is a leap year")
else:
    print(year, "is not a leap year")