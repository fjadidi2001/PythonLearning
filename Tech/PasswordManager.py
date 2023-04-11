master_pwd = input("what is the master password? ")


def view():
    pass


def add():
    name = input("Account Name: ")
    pwd = input("Password: ")
    with open('passwords.txt', 'w') as f:




while True:
    mode = input("add/view/q for quit? ").lower()
    if mode == "q":
        break
    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("invalid mode")
        continue
