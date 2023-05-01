# Exercise 6: Display numbers divisible by 5 from a list
n = int(input("Enter number of elements: "))
a = list(map(int,
             input("\nEnter the numbers : ").strip().split()))[:n]

print("\nGiven list is ", a)

for i in a:
    if i % 5 == 0:
        print(i)
