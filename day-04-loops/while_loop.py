# Number guessing game:
#     Set secret = 7. Take number as input in a loop.
#     Keep asking until they guess correctly. Print how many attempts it took.

secret = 7
attempts = 0

while True:
    guessed_number = int(input("Guess the number: "))
    attempts += 1
    if guessed_number == secret:
        print("Correct! You guessed it in", attempts, "attempts")
        break
    else:
        print("Wrong — try again")