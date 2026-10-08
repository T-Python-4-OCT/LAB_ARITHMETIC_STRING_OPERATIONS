price = 2.99
quantity = 3
tax_rate = 7.5/100
subtotal = price * quantity
tax = subtotal * tax_rate
total = subtotal + tax

print(f"Price of item: ${price}" )
print(f"Quantity: {quantity}")
print(f"Tax rate: {tax_rate * 100}%")
print("\n")
print(f"Subtotal: ${round(subtotal, 2)}")
print(f"Tax: ${round(tax, 2)}")
print(f"Total: ${round(total, 2)}")