price=2.99
quantity=3
Tax_rate=7.5
subtotal=price*quantity
tax=subtotal*Tax_rate/100
Total=tax+subtotal




print("Price of item:$",price)
print("Quantity:",quantity)
print("Tax rate:",Tax_rate,"%")


print("$",subtotal)
print("$",round(tax,2))
print("$",round(Total,2))