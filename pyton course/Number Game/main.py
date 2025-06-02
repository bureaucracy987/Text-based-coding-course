import random
playing=True
number=str(random.randint(10,20) )
print("I will generate a number from one to twenty and you have to guess the number one digit at a time.")
while playing:
    guess=input("Give me your best guess.")
    if number==guess:
        print("Hooray you won")
        print("The number was",number)
        break
    else:
        print("You got the number wrong, please try again.")
