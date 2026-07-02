# D. Debugging Practice
# Find and fix ALL errors:
age = int(input("Enter age: "))
score = int(input("Enter score: "))

if (age > 18):
    print("Adult")
    if (score > 50):
        print("Passed")
    else:
        print("Failed")
elif (age == 18):
    print("Just turned 18")
else:
    print("Minor")