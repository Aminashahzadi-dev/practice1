class InsufficientFundsError(Exception):
    pass


class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            raise InsufficientFundsError(
                f"Balance {self.balance} hai, {amount} nahi nikal sakte"
            )
        self.balance -= amount


acc = BankAccount(1000)
acc.deposit(500)
acc.withdraw(300)
print("Balance:", acc.balance)

try:
    acc.withdraw(5000)
except InsufficientFundsError as e:
    print("Error:", e)
