seconds = int(input("Enter seconds: "))

hours = seconds // 3600
minutes = (seconds % 3600) // 60
seconds = seconds % 60

print(f"Hours: {hours}")
print(f"Minutes: {minutes}")
print(f"Seconds: {seconds}")
print(f"{hours:02d}:{minutes:02d}:{seconds:02d}")