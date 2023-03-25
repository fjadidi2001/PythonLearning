command = ""
started = False
while True:
    command = input("> ").lower()
    if command == "start":
        if started:
            print("car already started")
        else:
            started = True
            print("car started...")
    elif command == "stop":
        if not started:
            print("car is already stopped!")
        else:
            started = False
            print("car stopped.")
    elif command == "help":

        print('''
start - to start the car
stop - to stop the car
quit - to exit
        ''')
    elif command == "quit":
        break
    else:
        print("sorry, i dont understand that ")
