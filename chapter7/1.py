def deje(num):
    print('You entered the number :' + num)  # print the number
    n1 = int(num[0])
    n2 = int(num[1])
    n3 = int(num[2])
    n4 = int(num[3])
    n5 = int(num[4])
    print('The digit of this number are:' + num[0]+',' + num[1]+','+num[2]+','+num[3]+','+num[4])
    # print divided number to digits
    print(n1+n2+n3+n4+n5)  # print the sum of the digits

def rigthnumber(num):
    # input a number of 5 digit
    numisdigit = True  # stopping the loop, change when there is right number
    while numisdigit:
        if num.isdigit():  # checking if number or string
            if 9999 < int(num) < 99999:  # checking if 5 digit number
                deje(num)  # calling the print function
                numisdigit = False
            else:
                num = input('Please enter a 5 digit number\n')
        else:
            num = input('Please enter a 5 digit number\n')

def main():
    num = input('Please enter a 5 digit number\n')
    rigthnumber(num)


main()
