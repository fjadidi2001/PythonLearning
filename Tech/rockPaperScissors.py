import random

userWins = 0
computerWins = 0
options = ["rock", "paper", "scissors"]
while True:
    user_input = input("Type rock or paper or scissors or Q to quit: ").lower()
    if user_input == "q":
        break
    if user_input not in options:
        continue

    random_number = random.randint(0, 2)
    computer_pick = options[random_number]
    print("computer picked", computer_pick)

    if user_input == "rock" and computer_pick == "scissors":
        print("you won")
        userWins += 1

    elif user_input == "paper" and computer_pick == "rock":
        print("you won")
        userWins += 1

    elif user_input == "scissors" and computer_pick == "paper":
        print("you won")
        userWins += 1
    else:
        print("you lost")
        computerWins += 1
print("you won", userWins, "times")
print("the computer won", computerWins, "times")
print("Game over")
