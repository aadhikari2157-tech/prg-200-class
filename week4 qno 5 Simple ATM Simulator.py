accounts = {
    "A001": {"name": "Ramesh Thapa", "balance": 15000, "pin": "1234"},
    "A002": {"name": "Sunita Karki", "balance": 8500, "pin": "5678"},
    "A003": {"name": "Bikash Rai", "balance": 22000, "pin": "9012"}
}


def atm(account_id, pin, action, amount=0):

    if account_id not in accounts:
        print("Account not found")
        return
    
