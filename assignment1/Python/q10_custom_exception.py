class InvalidBalanceError(Exception):
    def __init__(self, message):
        super().__init__(message)

class BankAccount:
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0 :
            raise InvalidBalanceError(f"Invalid amount for deposit : {amount}")
        else :
            self.balance += amount
            print(f"Amount deposited :{amount}, Current balance : {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            raise InvalidBalanceError("Insufficient amount")
        else :
            self.balance -= amount
            print(f"Amount withdrawan :{amount}, Current balance : {self.balance}")

try:
    account = BankAccount("Venkatasai", 500)
    account.deposit(200)
    account.withdraw(600)
    #account.deposit(-100)
    account.withdraw(800)

except InvalidBalanceError as e:
    print("Error:", e)