numbers = []

with open('new_file.txt', 'a+', encoding='utf-8') as f:
    for i in range(0, 5):
        num = float(input('Enter a number: '))
        numbers.append(num)
    f.write(str(numbers))

