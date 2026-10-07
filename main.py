price = "$10.99"
quantity = 3
tax_rate = "2.07%"
subtotal = float(price.strip('$')) * quantity
tax = subtotal * float(tax_rate.strip('%')) / 100
total = subtotal + tax
print("Price of item:", price)
print("Quantity:", quantity)
print("Tax Rate:", tax_rate,"\n")    
print("Subtotal: ${:.2f}".format(subtotal))
print("Tax: ${:.2f}".format(tax))
print("Total: ${:.2f}".format(total))
