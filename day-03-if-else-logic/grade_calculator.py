# Grade Calculator:
#     Take marks as input (0-100). Print grade:

#         90-100 → "A — Excellent"
#         80-89 → "B — Good"
#         70-79 → "C — Average"
#         60-69 → "D — Below Average"
#         Below 60 → "F — Failed"

marks = int(input("Enter your marks: "))
if(marks>= 90 and marks <= 100):
    print("A — Excellent")
elif(marks>=80 and marks<=89):
    print("B — Good")
elif(marks>=70 and marks<=79):
    print("C — Average")
elif(marks>=60 and marks<=69):
    print("D — Below Average")
else:
    print("F — Failed")