

def main():


    ## Print out the odd values

    ## Old Way
    old_numbers = []
    for val in range(0,100):
        if val % 2 == 1:
            old_numbers.append(val)

    print(old_numbers, end = '\n\n\n')

    ## New Way
    odd_numbers = [val for val in range(0,100) if val % 2 == 1]
    print(odd_numbers)

if __name__ == "__main__":
    main()

