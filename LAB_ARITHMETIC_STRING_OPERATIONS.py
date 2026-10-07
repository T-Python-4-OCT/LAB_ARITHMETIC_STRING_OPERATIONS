price = 5
quantity = 3
tax_rate = 1.5

subtotal = price * quantity

tax = subtotal * (tax_rate / 100)

total = subtotal + tax 

print(f'price of item :{price}')
print(f'Quantity: {quantity}')
print(f'Tax rate:{tax_rate}')
print("-------------------")
print(f'Subtotal : {subtotal} SR')
print(f'Tax : {tax:.3f} SR')
print(f'Total : {total} SR')

