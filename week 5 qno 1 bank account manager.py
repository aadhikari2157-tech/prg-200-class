class BankAccount:
    def __init__(self, name, account_number, balance=0):
        self.name = name
        self.account_number = account_number
        self.balance = balance


    def deposit(self, amount):
        self.balance += amount
        print(f"NPR {amount} deposited into {self.account_number}")


    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds")
        else:
            self.balance -= amount
            print(f"NPR {amount} withdrawn from {self.account_number}")

    def get_balance(self):
        print(f"{self.name} ({self.account_number}) Balance: NPR {self.balance}")


