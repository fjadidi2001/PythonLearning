# this program converts your weight from kilos to pounds or verse versa
weight = int(input("Weight: "))
unit = input('(L)bs or (k)g: ')
if unit.upper() == 'L':
    converted = weight * 0.45
    print(f"you are {converted} kilos")
else:
    converted = weight / 0.45
    print(f'you are {converted} pounds')
