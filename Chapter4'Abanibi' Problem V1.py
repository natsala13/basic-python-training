__author__ = 'Avitay Geltman'

# ani ohev otach

x = input('Please enter a sentence\n')
length = len(x)
new_x = ''

for i in range(length):
    if x[i] == 'a' or x[i] == 'e' or x[i] == 'i' or x[i] == 'o' or x[i] == 'u':
        new_x = new_x + x[i] + 'b' + x[i]
    else:
        new_x = new_x + x[i]

print (new_x)
