name = input("enter your name:")
m = len(name)
if m < 3:
    print('name must be at least 3 characters')
elif m > 50:
    print('name had 50 characters')
else:
    print("name looks good")
