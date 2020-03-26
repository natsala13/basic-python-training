message = input('please enter a 5 digit number\n')
print(f'You entered the number: {message}')
print('The digits of this number are:', end=" ")
for c in message:
    print(f'{c}', end=",")
print('\nThe sum of the digits is:', end= " ")
i = message
out = int(i[0])+ int(i[1]) + int(i[2]) + int(i[3]) + int(i[4])
print(out)


