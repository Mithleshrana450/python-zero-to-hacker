# Build an ATM simulator:
#     Enter your PIN: ****
#     Enter amount to withdraw:

#         Rules:
#             - PIN must be 1234
#             - Balance starts at ₹10,000
#             - Cannot withdraw more than balance
#             - Cannot withdraw 0 or negative amount
#             - Print balance after successful withdrawal
pin = input("Enter your PIN: ")

if pin != "1234":
    print("Invalid PIN — access denied")
else:
    amount = int(input("Enter amount to withdraw: "))
    balance = 10000

    if amount <= 0:
        print("Invalid amount")
    elif amount > balance:
        print("Insufficient balance")
    else:
        balance -= amount
        print("Successfully withdrawn ₹", amount)
        print("Remaining balance: ₹", balance)