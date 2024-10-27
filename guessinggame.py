import random
number = random.randint(1,10)
guesses = 0 
while guesses < 3:
    guess = int(input("Guess a number between 1 and 10:"))
    guesses += 1
    guess == number
    print("you win")
    break
else:
    print("Try again")