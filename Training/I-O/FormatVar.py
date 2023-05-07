totalMoney = int(input('Enter your total money: '))
quantity = int(input('How many do you want to buy thing?: '))
price = int(input('Enter the price:'))
print(f'I have {totalMoney}$ dollars so I can buy {quantity} football for {price}$ dollars.')

# SOLUTION TWO
quantity = 3
totalMoney = 1000
price = 450
statement1 = "I have {1} dollars so I can buy {0} football for {2:.2f} dollars."
print(statement1.format(quantity, totalMoney, price))