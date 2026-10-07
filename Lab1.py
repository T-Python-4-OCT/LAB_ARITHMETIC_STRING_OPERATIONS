# سعر القطعة الواحدة، وعدد القطع، ونسبة الضريبة بصيغة عشرية.
price = 2.99
quantity = 3
tax_rate = 0.075

# حساب المجموع قبل الضريبة، ثم قيمة الضريبة، ثم الإجمالي بعد إضافتها.
subtotal = price * quantity
tax = subtotal * tax_rate
total = subtotal + tax

# طباعة معلومات الشراء؛ .2f تعرض المبلغ بمنزلتين عشريتين.
print(f"Price of item: ${price:.2f}")
print(f"Quantity: {quantity}")
# .1% تعرض النسبة المئوية بمنزلة عشرية واحدة.
print(f"Tax rate: {tax_rate:.1%}")
print()
print(f"Subtotal: ${subtotal:.2f}")
print(f"Tax: ${tax:.2f}")
print(f"Total: ${total:.2f}")
