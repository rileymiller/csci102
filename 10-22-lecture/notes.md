### Notes for 10/22 Lecture

1) how the file system organizes files
    `ls in directory`, talk about directories and files
2) absolute vs. relative paths
    absolute paths stem from file root to current file:
    `/Users/rileymiller/code/csci102/10-22-lecture`
    relative paths are relative to the files current location
    `./notes.md || ../csci102review/loops.py`
3) opening a file for R, W, etc. AND file open error when not in correct directory
```
    'r': open the file for reading
    'w': open the file for writing
    'a': open the file for appending, if the file does not exist then it's created. Contents of an existing file are overwritten
```
4) steps for reading a file
```
    f = open("myfile.txt")
    file = open("myfile.txt", "r")
    content = f.read() # returns ths file contents as a string
    f.readlines() # returns a list of strings
    for line in content:
        print(line)
    f.close()
```
5) steps for writing a file
```
    f = open('myfile.txt', 'w')  # Open file
    f.write('Example string:\n  test...')  # Write string
    f.close()  # Close the file

    import os

    # Open a file with default line-buffering.
    f = open('myfile.txt', 'w')

    # No newline character, so not written to disk immediately
    f.write('Write me to a file, please!')

    # Force output buffer to be written to disk
    f.flush()
    os.fsync(f.fileno())
```
6) the with statement (stress scoping idea)
```
with open('myfile.txt', 'r') as myfile:
    # Statement-1
    # Statement-2
    # ...
    # Statement-N

    print('Opening myfile.txt')

# Open a file for reading and appending
with open('myfile.txt', 'r+') as f:
    # Read in two integers
    num1 = int(f.readline())
    num2 = int(f.readline())

    product = num1 * num2

    # Write back result on own line
    f.write('\n')
    f.write(str(product))

# No need to call f.close() - f closed automatically 
print('Closed myfile.txt')

```
7) format of CSV files (and how they can be loaded into Excel, Google spreadsheet, etc.)
CSV: comma separated values, a simple text based file format that uses commas to separate fields.
```
name,hw1,hw2,midterm,final
Petr Little,9,8,85,78
Sam Tarley,10,10,99,100
Joff King,4,2,55,61
```
8) the CSV module
The Python standard library csv module can be used to help read and write files in the csv format. To read a file using the csv module, a program must first create a reader object, passing a file object created via open. The reader object is an iterable – iterating over the reader using a for loop returns each row of the csv file as a list of strings, where each item in the list is a field from the row.
```
import csv

with open('grades.csv', 'r') as csvfile:
    grades_reader = csv.reader(csvfile, delimiter=',')

    row_num = 1
    for row in grades_reader:
        print('Row #%d:' % row_num, row)
        row_num += 1


    import csv

row1 = ['100', '50', '29']
row2 = ['76', '32', '330']

with open('gradeswr.csv', 'w') as csvfile:
    grades_writer = csv.writer(csvfile)

    grades_writer.writerow(row1)
    grades_writer.writerow(row2)

    grades_writer.writerows([row1, row2])
```
