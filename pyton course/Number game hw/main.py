import random 
import time
number=random.randint(1,100)
def intro():
    print("May I ask you for your name?")
    global name
    name=input()
    print(name,"we are going to play a game. I will guess a number between 1 to hundred and you have to guess it.")
    if (number%2==0):
     x="even"
    else:
     x="odd"
    print("This is an {} number".format(x))
    time.sleep(.5)
    print("Go ahead, guess!!!")
def pick():
    guessTaken=0
    while (guessTaken<6):
        time.sleep(.25)
        enter=input("Guess:")
        try:
            guess=int(enter)
            if guess>1 and guess<100:
                guessTaken+=1
                if guessTaken<6:
                    if guess<number:
                        print("The number you have entered is too low.")
                    if guess>number:
                        print("The number you have entered is too high.")
                    if guess!=number:
                        time.sleep(.5)
                        print("Try Again")
                    if guess==number:
                        break
            if guess>100 or guess<1:
                print("Silly goose. That isn't the number range.")
                time.sleep(.25)
                print("Please enter a number between 1 to 100")
        except:
            print("I don't think that",enter,"is valid.")  
    if guess == number:
        print("Good job {}! You guessed my number in {} guesses ".format(name,guessTaken))   
    if guess!= number:
        print("Nope. The number I was thinking of was",number)
playagain="yes"
while playagain=="Yes" or playagain=="YES" or playagain=="yes":
    intro()
    pick()
    playagain=input("Do you want to play again?")
     