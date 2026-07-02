# Take units consumed as input. Calculate bill:
#     First 100 units → ₹2 per unit
#     Next 100 units (101-200) → ₹3 per unit
#     Above 200 units → ₹5 per unit
#     Print the total bill.

units = int(input("Enter total consumed units: "))

if units <= 100:
    bill = units * 2
elif units <= 200:
    bill = (100 * 2) + ((units - 100) * 3)
else:
    bill = (100 * 2) + (100 * 3) + ((units - 200) * 5)

    print("Your total electricity bill is: ₹", bill)