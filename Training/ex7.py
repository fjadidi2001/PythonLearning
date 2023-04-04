# Exercise 7: Return the count of a given substring from a string
str_x = str(input("Enter a sentence: "))
str_y = str(input("Enter substring: "))
for i in str_x:
    count = 0
    if str_y in str_x:
        count += 1
    print(count)
