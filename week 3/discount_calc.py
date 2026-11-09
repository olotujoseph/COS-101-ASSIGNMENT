amount = float(input("Enter purchase amount in Naira: "))

if amount < 0:
    print("Invalid amount. Purchase amount cannot be negative.")

else:
    if amount < 10000:
        rate = 0
    elif amount < 50000:
        rate = 0.05
    else:
        rate = 0.10

    discount = amount * rate
    final_amount = amount - discount

    print(f"Original amount: ₦{amount:.2f}")
    print(f"Discount amount: ₦{discount:.2f}")
    print(f"Final amount payable: ₦{final_amount:.2f}")
