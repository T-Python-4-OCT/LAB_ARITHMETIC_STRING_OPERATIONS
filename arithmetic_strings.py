price=2.99
print("Price of item: $" + str(price))

quantity=3
print("Quantity: " + str(quantity))

tax_rate=7.5
print("Tax rate: " + str(tax_rate) + "%")

sub_total = price * quantity
print("Subtotal: $" + str(sub_total))

tax = sub_total * (tax_rate / 100)
print("Tax: $" + str(round(tax, 2)))

total = sub_total + tax
print("Total: $" + str(round(total, 2)))