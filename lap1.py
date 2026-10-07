price = 4.99
quantity = 5
tax_rate = 0.15
subtotal = price * quantity
tax = subtotal * tax_rate
total = subtotal + tax
print(f"price of item: ${price:.2f}")
print(f"quantity: {quantity}")
print(f"tax rate: {tax_rate * 100}%")
print(f"\nsubtotal: ${subtotal:.2f}")
print(f"tax ${tax:.2f}")
print(f"total: ${total:.2f}")
