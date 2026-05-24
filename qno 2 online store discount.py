purchase = float(input("Enter total purchase amount (NPR): "))
is_member = input("Are you a loyalty member? (yes/no): ")
if purchase < 1000:
    discount = 0
elif purchase < 5000:
    discount = 5
elif purchase < 15000:
    discount = 10
else:
    discount = 20
discounted_amount = purchase * (1 - discount / 100)
if is_member.lower() == "yes" and discount > 0:
     final_amount = discounted_amount * (1 - 5 / 100)
    print("Purchase Amount      : NPR", purchase)
    print("Purchase Discount    :", discount, "%")
    print("Loyalty Discount     : 5%")
    print("Final Payable        : NPR", round(final_amount, 2))
else:
    final_amount = discounted_amount
    print("Purchase Amount      : NPR", purchase)
    print("Purchase Discount    :", discount, "%")
    print("Final Payable        : NPR", round(final_amount, 2))
