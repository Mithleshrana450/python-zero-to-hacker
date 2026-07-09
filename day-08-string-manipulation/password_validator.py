def validate_password(password):
    missing = []

    if len(password) < 8:
        missing.append("at least 8 characters")

    if not any(char.isupper() for char in password):
        missing.append("an uppercase letter")

    if not any(char.isdigit() for char in password):
        missing.append("a digit")

    special_chars = "!@#$%^&*"
    if not any(char in special_chars for char in password):
        missing.append("a special character (!@#$%^&*)")

    if not missing:
        return "Strong"
    else:
        return "Missing: " + ", ".join(missing)

print(validate_password("Password1!"))
# Output: Strong

print(validate_password("password"))
# Output: Missing: an uppercase letter, a digit, a special character (!@#$%^&*)

print(validate_password("Pass12"))
# Output: Missing: at least 8 characters, a special character (!@#$%^&*)