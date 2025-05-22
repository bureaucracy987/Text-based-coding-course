Time=float(input("Enter the time(in 24 hours format):"))
if Time>8 and Time<12:
 print("Time to do your chores.")
elif Time>12 and Time<14:
 print("Its time to have lunch.")
elif Time>14 and Time<21:
 print("Its time to do your evening chores")
elif Time>21 and Time<22:
 print("Its time to have dinner.")
elif Time>22 and Time<6:
 print("Its time to sleep")
else:
 print("ERROR!!!")
