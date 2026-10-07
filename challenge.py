seconds = int(input("Enter number of seconds: "))

hours = seconds // 3600
minutes = (seconds % 3600) // 60
seconds = seconds % 60

print("hours:", hours)
print("minutes:", minutes)
print("seconds:", seconds)