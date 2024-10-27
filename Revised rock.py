import random
choices = ["rock", "paper", "scissors"]
computer = random.choice(choices)

user = input("Enter rock, paper, or, scissors").lower()

while user not in choices:
    user = input("invalid input. Please enter rock, paper, or scissors").lower()

if user == computer:
    print(f"Both chose{user}. Tie")
elif (user == "scissors" and computer == "paper") or\
 (user == "rock" and computer == "scissors") or\
 (user == "paper" and computer == "rock"):
    print(f"You chose {user}, computer chose {computer}. You win!")
else:
    print(f"You chose {user}, computer chose {computer}. COMPUTER win!")
