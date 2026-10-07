seconds=int(input("Enter the number of seconds: "))

minutes=seconds//60
hours=minutes//60
remaining_seconds=seconds%60
print(f"{hours:} hours\n{minutes%60:} minutes\n{remaining_seconds} seconds")


print(f"{hours:02d}:{minutes%60:02d}:{remaining_seconds:02d} ")
