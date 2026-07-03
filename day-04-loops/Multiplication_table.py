# Multiplication table:
#     Take a number as input. Print its multiplication table from 1 to 10.
#     Input: 5
#     Output:
#         5 x 1 = 5
#         5 x 2 = 10
#         ...
#         5 x 10 = 50

n = int(input("Enter number to print multiplication table of: "))
for i in range(1,11):
    print(n, "X",i, "=",n*i)