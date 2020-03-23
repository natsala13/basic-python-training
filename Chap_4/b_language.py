# Page 58
sentence = input("Please Enter a sentence:\n")
i=0
while i < len(sentence):
    if sentence[i] in 'aeiou':
        sentence = sentence[:i+1] + 'b' + sentence[i] + sentence[i+1:]
        i=i+2
    i=i+1
print(sentence)