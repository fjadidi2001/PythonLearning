# Exercise 5: Accept a list of 5 float numbers as an input from the user
number = []
for i in range(0, 5):
    num = float(input('Enter float number: '))
    number.append(num)
print('user list: ', number)
# another solution
for i in range(0, 5):
    print("Enter number at location", i, ":")
    # accept float number from user
    item = float(input())
    # add it to the list
    number.append(item)

print("User List:", number)
