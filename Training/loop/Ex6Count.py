
# Exercise 6: Count the total number of digits in a number
num = int(input("Enter your num: "))
count = 0
while num != 0:
    num = num // 10
    count = count + 1
print("Total digits are:", count)
