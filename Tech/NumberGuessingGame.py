import random

topOfRange = input("range: ")
if topOfRange.isdigit():
    topOfRange = int(topOfRange)
    if topOfRange <= 0:
        print('Enter number>0')
        quit()
else:
    print("print integer number")
    quit()
randomNumber = random.randint(0, topOfRange)
guesses = 0
while True:
    guesses += 1
    user_guess = input("make a guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print('enter another guess: ')
        continue
    if user_guess == randomNumber:
        print("you got it")
        break
    elif user_guess > randomNumber:
        print("you were above the number:)")
    else:
        print("you were below the number:)")
print("you got it in" + guesses + "guesses")
