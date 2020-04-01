def digit_number():
    num_list = []
    while True:
        message = input('please enter a 5 digit number\n')
        if len(message) != 5 or not message.isdigit():
            pass
        else:
            break
    print(f'You entered the number: {message}')
    print('The digits of this number are:', end=" ")

    for n in message:
        print(f'{n}', end=",")

    print('\nThe sum of the digits is:', end=" ")
    out = int(message[0]) + int(message[1]) + int(message[2]) + int(message[3]) + int(message[4])
    print(out)


digit_number()
