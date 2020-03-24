an0 = 0
an1 = 1
fibonacci = True
while fibonacci:
    if an1 > 10000:
        fibonacci = False
        print(an0)
        break
    print(an0)
    print(an1)
    an0 = an0 + an1
    an1 = an1 + an0


