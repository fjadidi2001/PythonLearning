import random

topOfRange = input("range: ")
if topOfRange.isdigit():
    topOfRange = int(topOfRange)
    if topOfRange <= 0:
        print('Enter number>0 next time.')
        quit()
else:
    print('Enter number>0 next time.')
    quit()

randomNumber = random.randint(0, topOfRange)
print(randomNumber)
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
print("you got it in", guesses, "guesses")


'''
This code is a simple number-guessing game implemented in Python. Here's a breakdown of how it works:

1. **Importing the Random Module**: The code begins by importing the `random` module, which allows the program to generate random numbers.

2. **Getting User Input for Range**: The program prompts the user to enter a range for the random number. The input is stored in the variable `topOfRange`.

3. **Input Validation**:
   - The program checks if the input is a digit using `isdigit()`. If it is, it converts the input from a string to an integer.
   - It then checks if the integer is greater than 0. If not, it prints a message asking for a number greater than 0 and exits the program using `quit()`.
   - If the input is not a digit, it also prints a message and exits.

4. **Generating a Random Number**: A random integer between 0 and the user-defined `topOfRange` is generated using `random.randint(0, topOfRange)`. This number is stored in the variable `randomNumber`.

5. **Guessing Loop**:
   - The program initializes a counter `guesses` to keep track of the number of attempts the user makes to guess the number.
   - It enters an infinite loop (`while True:`) where it continuously prompts the user to make a guess.
   - Each time the user makes a guess, the `guesses` counter is incremented by 1.

6. **Guess Validation**:
   - The program checks if the user's input is a digit. If it is, it converts the input to an integer.
   - If the input is not a digit, it prompts the user to enter another guess and continues to the next iteration of the loop.

7. **Comparing the Guess to the Random Number**:
   - If the user's guess matches `randomNumber`, the program prints "you got it" and breaks out of the loop.
   - If the guess is higher than the random number, it informs the user that they were above the number.
   - If the guess is lower, it informs the user that they were below the number.

8. **Final Output**: After the user guesses the correct number, the program prints how many guesses it took them to get it right.

Overall, this code provides a basic interactive experience where users can guess a randomly generated number, with feedback on whether their guesses are too high or too low.

'''
