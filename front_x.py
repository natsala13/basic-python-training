list1 = ['mix', 'xyz', 'apple', 'xanadu', 'aardvark']


def front_x(words):
    out1 = []
    out2 = []
    for w in words:
        if w[0] == 'x':
            out1.append(w)
        else:
            out2.append(w)
    return (out1) + (out2)


c = front_x(list1)
print(c)

