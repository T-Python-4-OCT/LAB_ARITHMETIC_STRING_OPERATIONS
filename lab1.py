
price=2.99
print(f"Price: ${price}")

quantity=3
print(f"Quantity: {quantity}")

tax_rate=7.5
print(f"Tax Rate: {tax_rate}%")


print("--------------------")


subtotal=price*quantity
print(f"Subtotal: ${subtotal}")

tax=subtotal*tax_rate/100
print(f"Tax: ${tax:.2}")

total=subtotal+tax
print(f"Total: ${total:.2}")