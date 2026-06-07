class BankAccount:
    def __init__(self, name, account_number, balance=0):
        self.name = name
        self.account_number = account_number
        self.balance = balance


    def deposit(self, amount):
        self.balance += amount
        print(f"NPR {amount} deposited into {self.account_number}")
        

