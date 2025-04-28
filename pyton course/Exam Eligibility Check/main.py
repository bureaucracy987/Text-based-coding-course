medical_cause=str(input("Do you have any medical cause, Yes or No:"))
atten=int(input("Enter your attendance of the student:"))
if medical_cause == "Yes":
    print("You are allowed")
else:
    if atten>=75:
        print("You are allowed.")
    else:
        print("You are not allowed.")