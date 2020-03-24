__author__ = 'Avitay Geltman'

a = 0
b = 1
print(a, b, end = ' ')

while True:
    c = a + b
    a = b
    b = c
    if c >= 10000:
        break
    else:
        print(c, end=' ')