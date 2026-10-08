Seconds = int(input('Please, Enter the number of seconds: '))

Hours =  ( Seconds // 3600 ) # 3600 Seconds in 1 Hour
Minutes =  ( Seconds % 3600 ) // 60 # There are 60 Seconds in a Minute
Remaining_Seconds = Seconds % 60 

print('Hours:', Hours)
print('Minutes:', Minutes)
print('Remaining Seconds:', Remaining_Seconds)

print()

print(f" ⏱ {Hours:02}:{Minutes:02}:{Remaining_Seconds:02}")