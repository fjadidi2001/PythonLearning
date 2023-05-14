# Exercise 10: Read line number 4 from the following file

# print the 4th line
# with open('new_file.txt', 'r') as fp:
#     x = fp.readlines()
#     print(x[3])

filePath = "test.txt"
openMode = "r"

with open(filePath, openMode) as f:
    for i, line in enumerate(f):
        print(i, line)