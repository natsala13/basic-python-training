def mul_2nums(x, y):
    return x*y
x = input('please enter two numbers:\nx=')
y = input('y=')
if int(x)*int(y) < 0:
    print('0')
else:
    print('your number is:', mul_2nums(int(x), int(y)))
