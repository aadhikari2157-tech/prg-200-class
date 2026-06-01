inventory = {
    "rice": {"price": 120, "stock": 20},
    "milk": {"price": 90, "stock": 10},
    "bread": {"price": 60, "stock": 15},
    "eggs": {"price": 15, "stock": 30}
}

cart = {
    "rice": 2,
    "milk": 3,
    "eggs": 12
}

def process_order(inventory, cart):
    total = 0

    print("---- Bill ----")

    for item, qty in cart.items():
        if item in inventory: