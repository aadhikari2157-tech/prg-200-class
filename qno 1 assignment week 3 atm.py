balance = float(input("Enter your account balance (NPR): "))
daily_withdrawn = float(input("Amount already withdrawn today (NPR): "))
amount = float(input("Amount to withdraw (NPR): "))

daily_limit = 50000

if amount % 500 != 0:
    print("Invalid amount. Must be a multiple of NPR 500.")
elif amount > balance:
     print("Insufficient balance.")
