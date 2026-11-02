seconds= input("Enter the seconds : ")

hour = int(seconds) // 3600
minutes = (int(seconds) % 3600) // 60
seconds = int(seconds) % 60

# print("Hours : ", hour, "\n Minutes : ", minutes, "\n Seconds : ", seconds)

#formatting string
print("Hours :{} \nMinutes : {} \nSeconds : {}".format(hour, minutes, seconds))







