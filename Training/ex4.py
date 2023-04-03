# Exercise 4: Remove first n characters from a string

word = str(input("Enter you world: "))
remove_chars = int(input("Enter a number: "))
for i in range(len(word)):
    var = word[remove_chars:]
    print(var)
    break
