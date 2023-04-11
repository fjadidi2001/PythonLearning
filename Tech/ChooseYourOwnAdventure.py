name = input("type your name: ")
print("welcome", name, "to this adventure")

answer = input("right or left? ").lower()
if answer == "left":
    answer = input("walk or swim? ").lower()
    if answer == "swim":
        print("lost the game")

    elif answer == "walk":
        print("lost again")
    else:
        print("not a valid option. you lose. hahahah")

elif answer == "right":
    answer = input("cross or back? ").lower()
    if answer == "back":
        print("you lose tht.")

    elif answer == "cross":
        answer = input("yes or no? ").lower()
        if answer == "yes":
            print("you win")
        if answer == "no":
            print("you lose")

    else:
        print("not a valid option. you lose. hahahah")


else:
    print("you lose")
print("bye hater.")
