import random

topOfRange = input("Type of number: ")
if topOfRange.isdigit():
    topOfRange = int(topOfRange)
    if topOfRange <= 0:
        print('Enter number>0')
        quit()
else:
    print("print a number")
randomNumber = random.randint(0, topOfRange)
print(randomNumber)
