import random
options=["Rock", "Paper" , "Scissor"]
user_choice=input("Choose rock, paper, or scissor")
computer_choice=random.choice(options)
print("You chose", user_choice)
print("Computer chose", computer_choice)
if user_choice==computer_choice:
    print("It's a tie")
elif user_choice=="Rock" and computer_choice== "Scissor":
    print("Rock crushes scissor. You win.")
elif user_choice=="Paper" and computer_choice== "Rock":
    print("Paper folds rock. You win.") 
elif user_choice=="Scissor" and computer_choice== "Paper":
    print("Scissor cuts paper. You win.")
else:
    print("Oh no! You lose.")
