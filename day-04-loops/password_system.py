username = "Admin"
password = "hacker123"

for i in range(3):
    a = input("Enter username: ")
    b = input("Enter password: ")

    if a == username and b == password:
        print("Access granted")
        break
    else:
        print("Wrong password, try again")

else:
    print("Account locked")
