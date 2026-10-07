# challenge
second = input("Enter seconds: ")
hours = int(second) // 3600
minutes = (int(second) % 3600) // 60
seconds = int(second) % 60


result = f"{hours:02d}:{minutes:02d}:{seconds:02d}"

print(result)