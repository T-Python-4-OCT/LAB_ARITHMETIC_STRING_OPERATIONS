Price = 2.99
Quantity = 3
Tax_rate = 7.5

Subtotal = Price * Quantity
Tax = Subtotal * (Tax_rate / 100)
Total = Subtotal + Tax

print(f"Price of item: ${Price}")
print(f"Quantity: {Quantity}")
print(f"Tax rate: {Tax_rate}%")

print("Subtotal: $", round(Subtotal, 2))
print("Tax: $", round(Tax, 2))
print("Total: $", round(Total, 2))


