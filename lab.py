# LAB_ARITHMETIC_STRING_OPERATIONS

price = 2.99
print("Price of item: " +"$"+ str(price))

quantity = 3
print("Quantity: " + str(quantity))

tax = 0.075
print("Tax rate: " + str(tax *100) + "%")


total = price * quantity
print("Subtotal: " + "$" + str(total))

print("Tax: " + "$" + str(round(total * tax, 2)))

print("Total: " + "$" + str(round(total * (1 + tax), 2)))