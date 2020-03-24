sentence = 'ani ohev otach'
for c in 'aeiou':
    sentence = sentence.replace(c, f'{c}b{c}')
print(sentence)
