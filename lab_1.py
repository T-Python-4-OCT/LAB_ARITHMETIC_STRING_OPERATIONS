price = float(input("Enter the price of the item :  \n"))
quantity = int(input("Enter the number of items :   \n"))

tax_rate = 0.075
subtotal = price * quantity
tax = subtotal * tax_rate
total = tax + subtotal

print("Price of item : " + str(price)+"$")
print("quantity : " + str(quantity))
print("tax_rate : 7.5 %")
print("tax: "+ str(round(tax,2)) +"$")
print("subtotal : "+str(round(subtotal,2))+"$")
print("total : "+str(round(total,2))+"$")
