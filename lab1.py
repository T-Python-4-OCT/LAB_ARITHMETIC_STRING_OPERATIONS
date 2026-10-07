price=100.0
quantity=2
tax_rate=0.15
subtotal=price*quantity
tax=subtotal*tax_rate

total=subtotal+tax
print("price of item:",price)
print("quantity:",quantity)
print("tax rate:",tax_rate)
print(f"subtotal: ${subtotal}")
print(f"tax: ${tax}")
print(f"total: ${total}")