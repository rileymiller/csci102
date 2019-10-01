
def main():
    # how to initialize a list
    programming_languages = ["Ruby", "Python", "JavaScript", "C", "C++", "Rust"]
    print(programming_languages)
    # empty list
    empty = []

    # how to append onto a list
    programming_languages.append("C++")
    programming_languages.append("TypeScript")
    programming_languages.append("Perl")

    print(programming_languages)

    # how to modify a list
    programming_languages[3] = "Java"
    print(programming_languages)

    # sort function in lists
    arr = [4, 6, 7, 8, 2, 4,2, 1, 5]
    arr.sort()
    print(arr)

    print()

    # 2D array
    two_d = [ [1,2,3], [2,4,6], [5, 7, 7]]

    # 2D accesses
    print(two_d[0][1])

    # print in a 2D array
    for row in two_d:
        for col in row:
            print(col, end = ', ')
        print()

if __name__ == "__main__":
    main()
