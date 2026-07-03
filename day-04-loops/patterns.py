# Print this pattern using nested loops:
#     *
#     **
#     ***
#     ****
#     *****

a = int(input("Enter number to print pattern: "))
for i in range(1, a + 1):   # range(1, 6) → 1,2,3,4,5
    for j in range(i):
        print("*", end="")
    print()