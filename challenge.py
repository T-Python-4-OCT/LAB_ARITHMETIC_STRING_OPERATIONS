total_seconds = int(input("Enter seconds: "))

hours = total_seconds // 3600              
minutes = (total_seconds % 3600) // 60     
seconds = total_seconds % 60
                
print(f"Hours: {hours}")
print(f"Minutes: {minutes}")
print(f"Seconds: {seconds}")

print(str(hours).zfill(2) + ":" + str(minutes).zfill(2) + ":" + str(seconds).zfill(2))