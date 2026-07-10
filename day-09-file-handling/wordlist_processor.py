# Create wordlist.txt
passwords = ["admin", "password123", "hello", "qwerty", "letmein",
             "welcome123", "abc123", "python2025", "secret", "strongpass"]

with open("wordlist.txt", "w") as f:
    f.write("\n".join(passwords))

# Read passwords
with open("wordlist.txt", "r") as f:
    words = f.read().splitlines()

print("Total passwords:", len(words))
print("Longest:", max(words, key=len))
print("Shortest:", min(words, key=len))

# Filter passwords longer than 8 characters
strong = [w for w in words if len(w) > 8]

with open("strong_passwords.txt", "w") as f:
    f.write("\n".join(strong))

print("Strong passwords saved to strong_passwords.txt")