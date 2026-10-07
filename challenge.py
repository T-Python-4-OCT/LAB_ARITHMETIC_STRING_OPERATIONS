#new challenge 


total_seconds = int(input("Enter number of seconds: "))
#claculate hours, minutes and seconds 
hours = total_seconds // 3600
minutes = (total_seconds % 3600) // 60
seconds = total_seconds % 60

print("Hours:", hours)
print("Minutes:", minutes)
print("Seconds:", seconds)

print(f"Time: {hours:02}:{minutes:02}:{seconds:02}")