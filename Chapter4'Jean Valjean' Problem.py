__author__ = 'Avitay Geltman'

number = input('Please enter a 5 digit number\n')

print('You entered the number: ' + number)

print('The digits of this number are: ', end = '')
digits_sum = 0
for i in range(len(number)):
    digits_sum = digits_sum + int(number[i])
    if i != len(number)-1:
        print(number[i], end = ',')
    else:
        print(number[i])

print('The sum of the digits is: ', end = '')
print(digits_sum)
