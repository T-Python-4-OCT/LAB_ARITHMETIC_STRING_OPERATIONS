seconds = int(input("Enter seconds:"))
hours = seconds // 3600
rest = seconds % 3600
min = rest // 60
sec = rest % 60
print ("hours",hours, "minuts", min, "seconds", sec,) 
print (f"{hours:02}:{min:02}:{sec:02}")