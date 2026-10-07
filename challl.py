sc=int(input("Enter number of Second :"))
hours= sc // 3600
rem=sc%3600
min=rem//60
sc_rem=rem%60
print("Hours:",hours)
print("Minutes:",min)
print("second:",sc_rem)
