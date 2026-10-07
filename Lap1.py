price = 5.75
quantity = 4
tax_rate =8.0

subtotal = price * quantity
tax = subtotal * (tax_rate/100)
total = subtotal + tax

print(f"price of item : ${price:.2f}")
print(f"quantity:{quantity}")
print(f"tax rate:{tax_rate}%")
print()


print(f"subtotal: $ {subtotal:.2f}")
print(f"tax: $ {tax:.2f}")
print(f"total: $ {total:.2f}")

