__author__ = 'Avitay Geltman'

def multiplication(a,b):
    return a*b

def division(a,b):
    if b != 0:
        return a/b
    else:
        return 'Illegal'

print(multiplication(4,0)) # 0
print(division(4,0)) # illegal
print(multiplication(4,6)) # 24
print(division(30,5)) # 6
