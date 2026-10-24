price , quantity , tax_rate = 2.99 , 3 , 0.075

subtotal = price * quantity
tax = subtotal * tax_rate
total = subtotal + tax

print(f"price of item: ${price}")
print(f"Quantity: {quantity}")
print(f"Tax rate: {tax_rate:.1%}\n")

print(f"Subtotal: ${subtotal}")
print(f"Tax: ${tax:.2}")
print(f"Total: ${total:.2f}")