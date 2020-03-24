def factorial():
    f = 1*2*3*4*5
    return f


def beep(str):
    str = str+'beep'
    return str


def mul_2nums(num1,num2):
    m = num1*num2
    if m>0:
        return m
    else:
        return 0


def main():
    F = factorial()
    print(F)

    str_beep = beep('hello')
    print(str_beep)

    n1 = 3
    n2 = 4
    mu = mul_2nums(n1,n2)
    print(mu)

main()
