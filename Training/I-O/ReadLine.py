# Exercise 10: Read line number 4 from the following file
from itertools import islice

# print the 15th line
with open('text.txt') as lines:
    for line in islice(lines, 14, 15):
        print(line)

# print each third line until 25
with open('text.txt') as lines:
    for line in islice(lines, 0, 25, 3):
        print(line)