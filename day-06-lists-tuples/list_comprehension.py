# Create a list of 5 passwords. Add 2 more. Remove one.
# Sort the list. Print final list and total count.

passwords = ["Admin", "123456", "qwerty", "password", "secure"]
passwords.append("123456")
passwords.append("secure123")
passwords.remove("123456")
passwords.sort()
print(f"final list {passwords}")
print(f"total count {len(passwords)}")
