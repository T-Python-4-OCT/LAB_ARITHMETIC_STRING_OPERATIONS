seconds=int(input("Enter seconds:"))

hours=seconds // 3600

Minutes= (seconds % 3600)//60

Seconds= seconds % 60 

print("Hours=",hours)
print("Minutes=",Minutes)
print("Seconds=",Seconds)



print(seconds,"seconds=",hours,"hours +",Minutes,"minutes +",Seconds,"Seconds ")

print(f"{hours:02}:{Minutes:02}:{Seconds:02}")
