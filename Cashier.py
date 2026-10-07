
# معلومات المنتج
Price = 2.99
Quantity = 3 
Tax_rate = 0.075

#حساب التكاليف
subtotal = Price * Quantity
tax = subtotal * Tax_rate
total = subtotal + tax

#عرض الفاتورة
print("Price of item: $", round(Price, 2))
print()
print("Quantity:", Quantity)
print()
print("Tax rate:", round(Tax_rate * 100, 2), "%")
print()
print("Subtotal: $", round(subtotal, 2))
print()
print("Tax: $", round(tax, 2))
print()
print("Total: $", round(total, 2))

#MohammedAlnsafi