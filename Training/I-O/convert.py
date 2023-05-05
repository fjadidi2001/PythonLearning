# Convert Decimal number to octal using print() output formatting
num = int(input('Enter a number: '))
print(f'this is Decimal number: {num}', 'and convert this number to octal is: %o' % num)
# another solution
Decimal = oct(num)
print(f'this is Decimal number: {num}', f'and convert this number to octal is: {Decimal}')
# another solution

octal = 0
ctr = 0
temp = num  # copying number

# computing octal using while loop
while temp > 0:
    octal += ((temp % 8) * (10 ** ctr))  # Stacking remainders
    temp = int(temp / 8)  # updating dividend
    ctr += 1

print("Binary of {x} is: {y}".format(x=num, y=octal))


def dectoOct(num):
    if num > 0:
        dectoOct(int(num / 8))
        print(num % 8, end='')


print("Octal: ", end='')
dectoOct(num)
