# accept input string from a user
word = input('Enter word: ')
print("Original String:", word)

# using list slicing
# convert string to list
# pick only even index chars
x = list(word)
print(x)
# x[start:end:step]
for i in x[0::2]:
    print(i)
