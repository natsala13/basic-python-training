def user_input():
    """Takes user 5 digit input, makes sure input is valid"""
    num_output = 0
    while num_output < 9999 or num_output > 99999:
        num_input = input("Please enter a 5 digit number:")
        if num_input.isdigit() is True:
            num_output = int(num_input)
    return num_output


def print_digits(number):
    """Prints each digits of a number with a comma"""
    str_number = str(number)
    print("The digits of the number are:", end='')
    for i, num in enumerate(str_number):
        if i < len(str_number)-1:
            print(num + ', ', end='')
        else:
            print(num)
    return 0

def print_sum_digits(number):
    """Prints the digits of a number"""
    str_number = str(number)
    sum = 0
    for i in str_number:
        sum = sum + int(i)
    print("The sum of the digits is: "+str(sum))
    return sum

def main():
    """
    assert(print_sum_digits(0) == 0)
    assert (print_sum_digits(123) == 6)
    assert(print_sum_digits(12345) == 15)
    assert(print_digits(0) == 0)
    assert(print_digits(123) == 0)
    assert(print_digits(-12345) == 0) """

    num = user_input()
    print("You entered the number:" + str(num))
    print_digits(num)
    print_sum_digits(num)


main()