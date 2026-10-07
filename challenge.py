seconds =int(input("inter the number of seconds ="))
minutes =(  seconds // 60)%60
hours = (seconds // 3600)
Remaining_seconds = ( seconds % 60)





print(f"{hours:02d}:{minutes:02d}:{Remaining_seconds:02d}")