# Exercise 1: Calculate the multiplication and sum of two numbers
# first solution:
# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))
# result = num1 * num2
# if result < 1000:
#     print(f"the result is: {result}")
# else:
#     print(f"the result is: {num1 + num2}")

# second solution:
def multiplicationOrSum(num1, num2):
    result = num1 * num2
    if result <= 1000:
        print(f"the result is: {result}")
    else:
        print(f"the result is: {num1 + num2}")


multiplicationOrSum(40, 30)
multiplicationOrSum(20, 30)
