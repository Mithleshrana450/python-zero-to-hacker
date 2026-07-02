# Create variables:
#     correct_username = "mithu"
#     correct_password = "python123"
#     Take username and password as input. Print "Login successful" or "Invalid credentials".
correct_username = "mithu"
correct_password = "python123"
username = input("Enter username: ")
password = input("Enter password: ")
if(username == correct_username):
    if(password == correct_password):
        print("Login Successful")
    else:
        print("Invalid credentials")
    
else:   
    print("user not found")
