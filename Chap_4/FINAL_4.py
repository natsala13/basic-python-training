input_str = input('Please enter a 5 digit number:')
print('You entered the number :' + input_str)
str_out = 'The digits of this number are: ' + input_str[0] + ',' + input_str[1] + ',' + input_str[2] + ',' + input_str[3] + ',' + input_str[4]
str_sum = 0
for i in input_str:
    str_sum = str_sum + int(i)
print(str_out)
print('The sum of the digits is: ' +str(str_sum))