

def main():
    colors = ["red", "blue", "magenta", "indigo", "pink", "purple"]

    # While loop
    i = 0
    while i < len(colors):
        print(colors[i])
        i += 1

    print()

    # Range-based for loops
    for i in range(len(colors)):
        print(colors[i])

    print()

    # for-in loop
    for color in colors:
        print(color)

    print()

    # What if I need both??
    # enumerate

    for num, color in enumerate(colors, start=1):
        print("Color {}:{}".format(num, color))


if __name__ == "__main__":
    main()




