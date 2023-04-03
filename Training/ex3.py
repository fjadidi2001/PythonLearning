# Exercise 3: Print characters from a string that are present at an even index number
olm = str(input("Enter your string: "))
cal = len(olm)
for i in range(0, cal - 1, 2):
    print(olm[i])


