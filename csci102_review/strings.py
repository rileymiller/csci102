

def main():
    s = 'I pledge allegience to the flag....'

    print(s)

    print('s[2:]', s[2:])

    t = 'of the United States of America...'

    # concatenation
    s += t
    print(s)

    # string immutable
    s[3] = 'W'

if __name__ == '__main__':
    main()
