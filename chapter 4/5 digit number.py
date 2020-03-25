number = input('enter a 5 digit number: ')
print('you entered a 5 digits number: ' + number)
print('the digits of this number are: ' + number[0] + ',' + number[1] + ',' + number[2] + ',' + number[3] + ',' + number[4])
sum = 0
for digit in number:
    sum = sum + int(digit)
print('the sum of the digits is: ' + str(sum))

