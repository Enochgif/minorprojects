import random 
choices = ["rock", "paper", "scissor"]
computer = random.choice(choices)
user = print(input("Enter rock, paper, scissor"))

if user == computer:
    print("Tie!")

elif ( user == "rock" and computer == "scisssors" ) or\
    ( user == "scissors" and computer == "paper" )  or\
    ( user == "paper"and computer == "rock" ):
    print("You win") 
print("Computer Win")