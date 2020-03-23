numbers = range(101)
for number in numbers:
    if '7' in str(number):
        print('{} '.format(number))
    elif number % 7 == 0:
        print(number)







