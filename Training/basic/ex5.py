# Exercise 5: Check if the first and last number of a list is the same
n = int(input("Enter number of elements: "))
a = list(map(int,
             input("\nEnter the numbers : ").strip().split()))[:n]

print("\nGiven list: ", a)


def Check_list(a):
    first = a[0]
    last = a[-1]
    if first == last:
        return True
    else:
        return False


print("result is", Check_list(a))
