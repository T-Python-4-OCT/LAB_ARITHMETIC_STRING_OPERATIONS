#LAB_ARITHMETIC_STRING_OPERATIONS
price = 2.99
Quantity = 3
Tax_rate = 0.075

Subtotal = price * Quantity
Tax = Subtotal * Tax_rate
Total = Subtotal + Tax

print ("price of item: $",price)
print ("Quantity:", Quantity)
print ("Tax_rate: 0.075%")
print ()
print ( f"Subtotal: ${Subtotal:.2f}")
print (f"Tax: ${Tax:.2f}")
print (f"total: ${Total:.2f}")

