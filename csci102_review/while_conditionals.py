

def main():

    user_input = ''

    index = 0
    while not user_input == 'QUIT':
        user_input = input('Please enter a string: ')

        if user_input == 'YIKES':
            continue

        index = index + 1
        print('user_input: ', user_input)
    else:
        print('user entered \"QUIT\", exiting')


if __name__ == '__main__':
    main()
