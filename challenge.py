# تحدي: تحويل الثواني إلى ساعات ودقائق وثواني 

seconds = int(input("Enter the number of seconds: "))
hours = seconds // 3600
minutes = (seconds % 3600) // 60
remaining_seconds = seconds % 60

print("Hours:", hours)
print("Minutes:", minutes)
print("Seconds:", remaining_seconds)
print()
print("⏱", str(hours).zfill(2) + ":" + str(minutes).zfill(2) + ":" + str(remaining_seconds).zfill(2))

#MohammedAlnsafi
#تعلمنا من خلال التحدي اضاقة zfill , input 