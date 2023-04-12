cars = ["Ford", "Volvo", "BMW"]
x = cars[0]  # Access the Elements of an Array
print(x)
cars[0] = "Toyota"
print(cars)
x = len(cars)
print(x)
for x in cars:
    print(x)
cars.append("Honda")
print(cars)
cars.pop(1)
print(cars)
cars.remove("BMW")
print(cars)
