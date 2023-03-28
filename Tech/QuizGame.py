print("welcome")

name = input("Name: ")
playing = input("Do u wanna play: ")
if playing.lower() != "yes":
    quit()

print('Lets Go')
score = 0
answer = input("List out components of a computer system. ")
if answer.lower() == "cpu and memory and input and output device":
    print('correct!')
    score += 1
else:
    print("incorrect")
answer = input("List out some popular operating system. ")
if answer.lower() == "windows and linux and osx":
    print('correct!')
    score += 1
else:
    print("incorrect")
answer = input("List out some computer processors. ")
if answer.lower() == "intel and amd":
    print('correct!')
    score += 1
else:
    print("incorrect")
answer = input("What is the full form of SDLC?. ")
if answer.lower() == "software development life cycle":
    print('correct!')
    score += 1
else:
    print("incorrect")
print(name + ' got ' + str(score) + " questions correct!")
print(name+" got " + str((score/4)*100) + "%.")
