words = ['im', 'aba', 'melon', 'catc', 'yay']


def match_ends(list_of_words):
    count = 0
    for w in list_of_words:
        if len(w) >= 2 and (w[0] == w[-1]):
            # count.append(w)
            # print(count)
            count += 1
    return (count)


c = match_ends(words)
print(c)
