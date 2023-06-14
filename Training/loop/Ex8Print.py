# Exercise 8: Print list in reverse order using a loop
#solution1
list1 = [10, 20, 30, 40, 50]
# reverse list
new_list = reversed(list1)
# iterate reversed list
for list1 in new_list:
    print(item)


#solution2
list1 = [10, 20, 30, 40, 50]
# get list size
# len(list1) -1: because index start with 0
# iterate list in reverse order
# star from last item to first
size = len(list1) - 1
for i in range(size, -1, -1):
    print(list1[i])
