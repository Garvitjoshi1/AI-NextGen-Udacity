phone_balance = int(input("Enter your mobile Balance: "))
bank_balance = 1000
if phone_balance < 5:
    phone_balance += 10
    bank_balance -= 10
print("The new phone balance {}, and bank_balance is {}".format(phone_balance, bank_balance))

n = int(input("Enter any number: "))
if n % 2 == 0:
    print("Number", n, " is even.")
else:
    print("Number", n, " is odd.")

season = input('Enter season name: ')
if season == 'spring':
    print('plant the garden!')
elif season == 'summer':
    print('water the garden!')
elif season == 'fall':
    print('harvest the garden!')
elif season == 'winter':
    print('stay indoors!')
else:
    print('unrecognized season')

