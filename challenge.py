seconds = int (input("Entervseconds:"))
hours = seconds//3600
minutes = (seconds%3600) // 60
remaining =seconds % 60
print(f"hours:{hours}")
print(f"minutes:{minutes}")
print(f"remaining:{remaining}")
print (f"{hours:02d}:{minutes:02d}:{remaining:02d}")