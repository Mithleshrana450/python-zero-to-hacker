name = input("Enter your name: ")   # input() always returns a string
age = int(input("Enter your age: "))  # we cast it to int because input() gives string by default

print("Hello", name)
print("You are", age, "years old")
print(type(name))   # shows <class 'str'>
print(type(age))    # shows <class 'int'>