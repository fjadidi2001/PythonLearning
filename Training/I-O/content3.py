numbers = []
with open('text.txt', 'r') as fp:
    li = fp.readline()
with open('text.txt', 'w') as fp:
    for i in range(0, 5):
        num = float(input('Enter a number: '))
        numbers.append(num)

