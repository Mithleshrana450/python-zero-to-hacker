# Take a number n as input. Calculate sum of all numbers from 1 to n using a loop.
# Input: 5
# Output: Sum = 15  (1+2+3+4+5)

# Take input from user
n = int(input("Enter a number: "))

# Initialize sum
total = 0

# Loop from 1 to n
for i in range(1, n + 1):
    total = total + i

    # Display result
print("Sum =", total)