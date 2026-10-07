price = 2.99
quantity = 3
tax_rate = 7.5 / 100

print(f"Price: ${price:.2f}")
print(f"Quantity: {quantity}")
print(f"Tax rate: {tax_rate:.1%}")

subtotal = price * quantity
print(f"Subtotal: ${subtotal:.2f}")

tax = tax_rate * subtotal
print(f"Tax: ${tax:.2f}")

total = tax + subtotal
print(f"Total: ${total:.2f}")