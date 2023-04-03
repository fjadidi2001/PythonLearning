# using loop
lst = []
n = int(input("Enter number of elements: "))
for i in range(0, n):
    ele = input()
    lst.append(ele)
print(lst)

print("=======================")

# with exception handling (input just int and stop with stop)

try:
    my_list = []
    while True:
        my_list.append(int(input()))

except:
    print(my_list)
print("=======================")
