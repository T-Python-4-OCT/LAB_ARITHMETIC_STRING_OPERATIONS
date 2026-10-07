total_seconds = int(input("Enter seconds: "))

houers = total_seconds // 3600

minutes = (total_seconds % 3600)//60

seconds = total_seconds % 60

print("Hours",houers)
print("Minutes",minutes)
print("Seconds",seconds)

print(f"{houers:02}:{minutes:02}:{seconds:02}")