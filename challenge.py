total_seconds = int(input("Enter seconds: "))

hours = total_seconds // 3600
minutes = (total_seconds % 3600) // 60
seconds = total_seconds % 60

print(f"Hours: {hours}")
print(f"Minutes: {minutes}")
print(f"Seconds: {seconds}")

# Bonus
print(f"⏱ {hours:02d}:{minutes:02d}:{seconds:02d}")