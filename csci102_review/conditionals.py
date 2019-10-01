

def main():
    x = 4
    y = 2

    print("x == y", x == y)
    print('x != y', x != y)
    print('x < y', x < y)
    print('x <= y', x <= y)
    print('x > y' , x > y)


    if x == 2 and y == 4:
        print('foo')
    elif not x == 2 or not y == 4:
        print('bar')
    else:
        print('baz')

if __name__ == '__main__':
    main()
