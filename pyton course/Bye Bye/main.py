valid=False
while not valid:
    try:
        n=int(input("Enter any number:"))
        while n%2==0:
            print("bye")
            valid=True
    except:
        print("Invalid. Please enter a number")