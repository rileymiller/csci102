

def main():

    user_input = ''

    while not user_input == 'QUIT':
        user_input = input('Please enter a string: ')
        print('user_input: ', user_input)
    else:
        print('user entered \"QUIT\", exiting')


if __name__ == '__main__':
    main()
