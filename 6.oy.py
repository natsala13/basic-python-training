def two_numbers(x, y):
    return x/y
x = input('please enter two numbers:\nx=')
y = input('y=')
if int(y) ==0:
    print('Illegal')
else:
    print('your number is:', two_numbers(int(x), int(y)))