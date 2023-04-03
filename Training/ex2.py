# Exercise 2: Print the sum of the current number and the previous number


def get_amount():
    while True:
        amount = input("Enter amount: ")
        try:
            val = int(amount)
            if val >= 0:
                break
            else:
                print("Amount can't be negative, try again")
        except ValueError:
            print("Amount must be a number, try again")
    return val


for i in range(get_amount()):
    current = i

    if current == 0:
        previous = 0
    else:

        previous = i - 1
    print(f"Current Number {current} Previous Number  {previous}  Sum: {current + previous}")
