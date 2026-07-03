# Real brute force logic structure
passwords = ["admin", "1234", "password", "hacker123", "root"]
correct = "hacker123"
attempts = 0

for pwd in passwords:
    attempts += 1
    if pwd == correct:
        print("Password cracked:", pwd)
        print("Attempts taken:", attempts)
        break
    else:
        print("Password not in wordlist")