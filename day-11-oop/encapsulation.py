class BankAccount:
    def __init__(self, balance=0):
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
        else:
            print("Invalid deposit!")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient balance!")

    def get_balance(self):
        return self.__balance

    def transfer(self, other_account, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            other_account.deposit(amount)
        else:
            print("Transfer failed!")


# Example
a1 = BankAccount(1000)
a2 = BankAccount(500)

a1.deposit(200)
a1.withdraw(300)
a1.transfer(a2, 400)

print("A1 Balance:", a1.get_balance())
print("A2 Balance:", a2.get_balance())