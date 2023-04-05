# Exercise 8: Print the following pattern
# 1
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5
n = 5
for i in range(1, n + 1):
    for j in range(i):
        print(i)
