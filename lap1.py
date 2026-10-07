price = 12.50
quantity = 4
tax_rate = 0.15
subtotal = price * quantity
tax = subtotal * tax_rate 
total = subtotal + tax
print(f"Price of item: ${price:.2f}")
print(f"Quantity: {quantity}")
print(f"Tax rate: {tax_rate * 100:.1f}%")
print()
print(f"Subtotal: ${subtotal:.2f}")
print(f"Tax: ${tax:.2f}")
print(f"Total: ${total:.2f}")


