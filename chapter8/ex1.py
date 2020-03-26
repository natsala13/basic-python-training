with open(r'C:\Users\ilsli\basic-python-training\bla.txt') as txt1:
    with open(r'C:\Users\ilsli\basic-python-training\empty.txt', 'w') as txt2:
        for line in txt1:
            txt2.write(line)
