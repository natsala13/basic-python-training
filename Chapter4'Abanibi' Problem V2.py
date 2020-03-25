__author__ = 'Avitay Geltman'

# ani ohev otach

x = input('Please enter a sentence\n')
length = len(x)
new_x = ''

for i in range(length):
    if 'a' in x[i] or 'e' in x[i] or 'i' in x[i] or 'o' in x[i] or 'u' in x[i]:
        new_x = new_x + x[i] + 'b' + x[i]
    else:
        new_x = new_x + x[i]

print (new_x)