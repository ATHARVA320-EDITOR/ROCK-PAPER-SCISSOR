import random
print("PLEASE ALWAYS TYPE IS UPPERCASE ONLY, ELSE YOU WILL LOSE.")
options = ["ROCK", "PAPER", "SCISSORS"]
user = input("Choose ROCK, PAPER OR SCISSORS.")
computer = random.choice(options)
print("You chose:", user)
print("Computer chose:", computer)
if user == computer:
    print("It's a tie")
elif user == "ROCK" and computer == "SCISSORS":
    print("Yay, you win")
elif user == "PAPER" and computer == "ROCK":
    print("Yay, you win")
elif user == "SCISSORS" and computer == "PAPER":
    print("Yay, you win")
else:
    print("You lose.")