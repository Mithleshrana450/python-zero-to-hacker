# Print the bool value of these:
#     0, 1, "", "hacker", None — use bool()
#     and explain in a comment why each is True or False.
print(bool(0))        # False - Zero is considered falsy
print(bool(1))        # True - Any non-zero number is considered truthy
print(bool(""))       # False - Empty string is considered falsy
print(bool("hacker")) # True - Non-empty string is considered truthy
print(bool(None))     # False - None is considered falsy