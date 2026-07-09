# Password Strength Analyzer

def analyze_password(password):
    common_passwords = [
        "123456", "password", "123456789", "qwerty", "abc123",
        "111111", "123123", "admin", "welcome", "password123",
        "letmein", "iloveyou"
    ]

    score = 0
    suggestions = []

    # Character checks
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(c in "!@#$%^&*" for c in password)

    # Length check
    length = len(password)

    if length >= 16:
        score += 4
    elif length >= 12:
        score += 3
    elif length >= 8:
        score += 2
        suggestions.append("Use at least 12 characters for better security.")
    else:
        suggestions.append("Password should be at least 8 characters long.")

    # Uppercase
    if has_upper:
        score += 1
    else:
        suggestions.append("Add at least one uppercase letter.")

    # Lowercase
    if has_lower:
        score += 1
    else:
        suggestions.append("Add at least one lowercase letter.")

    # Digit
    if has_digit:
        score += 1
    else:
        suggestions.append("Add at least one number.")

    # Special character
    if has_special:
        score += 1
    else:
        suggestions.append("Add at least one special character (!@#$%^&*).")

    # Bonus points
    if has_upper and has_lower and has_digit and has_special:
        score += 1

    # Common password check
    common = password.lower() in common_passwords
    if common:
        score = max(0, score - 3)
        suggestions.append("Avoid common passwords.")

    # Strength rating
    if score <= 3:
        rating = "Weak"
    elif score <= 6:
        rating = "Medium"
    elif score <= 8:
        rating = "Strong"
    else:
        rating = "Very Strong"

    # Strength bar
    filled = "█" * score
    empty = "░" * (10 - score)
    bar = filled + empty

    # Display results
    print("\n========== PASSWORD ANALYSIS ==========")
    print("Password Length :", length)
    print(f"Strength Score  : {score}/10")
    print("Strength        :", rating)
    print("Strength Bar    :", bar)

    print("\nCharacter Checks")
    print("----------------")
    print("Uppercase :", "✓" if has_upper else "✗")
    print("Lowercase :", "✓" if has_lower else "✗")
    print("Digits    :", "✓" if has_digit else "✗")
    print("Special   :", "✓" if has_special else "✗")

    print("\nCommon Password :", "YES" if common else "NO")

    print("\nSuggestions")
    print("-----------")
    if suggestions:
        for s in suggestions:
            print("- " + s)
    else:
        print("Excellent password! No improvements needed.")


# Main Program
password = input("Enter your password: ")
analyze_password(password)