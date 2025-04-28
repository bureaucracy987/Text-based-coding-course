print("Select your vehicle")
print("1. Bike")
print("2. Car")
choice=int(input("Enter your choice:"))
if(choice==1):
    print("Which type of bike?")
    print("1. Scooty")
    print("2. Motorbike")
    choice2=int(input("Enter your choice:"))
    if choice2==1:
     print("You have chosen Scooty.")
    else:
     print("You have chosen Motorbike.")
elif(choice==2):
    print("Which type of car?")
    print("1. Sedan")
    print("2. XUV")
    choice3=int(input("Enter your choice:"))
    if choice3==1:
       print("You have selected Sedan.")
    else:
       print("You have selected XUV.")
else:
   print("Wrong Choice")
     