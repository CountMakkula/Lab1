Price=float(input("Enter the price of the item: "))
SalesTax=float(input("Enter the sales tax percentage: "))/100
Cost=Price+Price*SalesTax
print(f"Your total is ${Cost:.2f}")