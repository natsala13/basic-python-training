number = [(1, 7), (1, 3), (3, 4, 5), (2, 2)]


def last(num1):
    return num1[-1]


def sort_last(number):
    return sorted(number, key=last)


print(sort_last(number))

