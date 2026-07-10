while True:
    try:
        a = float(input("Enter first number: "))
        op = input("Enter operator (+, -, *, /): ")
        b = float(input("Enter second number: "))

        if op == "+":
            print("Result:", a + b)
        elif op == "-":
            print("Result:", a - b)
        elif op == "*":
            print("Result:", a * b)
        elif op == "/":
            print("Result:", a / b)
        else:
            print("Invalid operator!")

    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
    except ValueError:
        print("Error: Please enter valid numbers.")
    except Exception:
        print("Something went wrong.")

    break