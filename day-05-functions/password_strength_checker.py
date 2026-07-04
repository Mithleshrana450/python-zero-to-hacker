# Password strength checker:
#     Create a function check_password(password) that returns:

        # "Weak" — less than 6 characters
        # "Medium" — 6 to 10 characters
        # "Strong" — more than 10 characters

def check_password(password):
    if len(password) < 6:
        return "Weak_Password"

    elif len(password) >= 6 and len(password) <= 10:
        return "Medium_Password"

    elif len(password) > 10:
        return "Strong_Password"


print(check_password("12345"))
print(check_password("mypwd12"))
print(check_password("verystrongpassword"))