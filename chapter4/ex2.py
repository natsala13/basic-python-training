sen = input('Please enter a sentence\n')
i = 0
while i < len(sen):
    if sen[i] in 'aeiou':
        sen = sen[:i+1] + 'b' + sen[i] + sen[i+1:]
        i = i+2
    i = i+1
print(sen)
