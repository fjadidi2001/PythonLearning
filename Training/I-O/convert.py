# Convert Decimal number to octal using print() output formatting
num = int(input('Enter a number: '))
print(f'this is Decimal number: {num}', 'and convert this number to octal is: %o' % num)
# another solution
Decimal = oct(num)
print(f'this is Decimal number: {num}', f'and convert this number to octal is: {Decimal}')
