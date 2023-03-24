prices = [10, 20, 45]
total = 0
for i in prices:
    total += i
print(f'Total:{total}')
print("============================================")
for x in range(4):
    for y in range(3):
        print(f'({x},{y})')

print("============================================")
numbers = [5, 2, 5, 2, 2]
for i in numbers:
    print('x' * i)
print("============================================")
# another solution for format output like F
for j in numbers:
    output = ''
    for count in range(j):
        output += 'x'
    print(output)

print("============================================")
numbers = [1, 1, 1, 1, 5]
for s in numbers:
    o = ''
    for k in range(s):
        o += 'x'
    print(o)
