n = int(input("Enter number of elements: "))
a = list(map(int,
             input("\nEnter the numbers : ").strip().split()))[:n]

print("\nGiven list is ", a)

for i in a:
    print("Div by 5", i)
