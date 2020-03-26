__author__ = 'Avitay Geltman'

def factorial():
    x = 1
    for i in range(5,0,-1):
        x = x * i
    return x

print(factorial())

def beep(string):
    string += ' beep'
    return string

print(beep('Hello'))

def mul_2nums(a,b):
    if a*b >= 0:
        return a*b
    else:
        return 0

print(mul_2nums(5,3))
print(mul_2nums(5,-3))