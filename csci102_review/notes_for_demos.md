### Notes for demo tomorrow
- Demo how you should prompt a user for input
- Explain why array indexes begin at 0, essentially because in C an array points to the location in 
    memory and so _n_ in list[_n_] should not be treated as an index but as an offset from the array's
    head.
- Variables, snake\_case vs. camelCase. How python comes with a style guide.
    - Scoping, most programming languages are lexically scoped where variables defined within
        a code block can only be used within that loop. i.e while loops Variables can be given
        global scope by being declared at the top of a file. Generally this isn't a great practice
        unless a variable is truly global and if so these variables should be declared in all-caps
        (i.e FRAME_WIDTH = 600). Global scope can get you in trouble once we introduce functions and 
        variables are scoped locally to the function block. These global variables can intrude on the
        variables declared within the scope of your function. For this class, if you declare a global
        variable, MAKE SURE you don't try to use that variable within a loop. 
- Strings
    - How to make them s = 'adsfasdas'
    - How to access them (Like lists)
    - How to combine them
        - Make sure to touch on how strings are immutable in python and how concatenations must be
            stored in a new variable.
            Common gotchas:
            ```
                str1 = 'ads'
                str2 = 'adsfasd'
                str1 += str2
                :(
            ```
- Print
    - How to print
    - How to put variables in a print
    - How to new line

- Loops
    - While loops - typically used when you want to break the loop on a condition.
    - for loops - generally when you know how many times you want the loop to run

- Lists
    - How to make (i.e  x = [1,2,3,4])
    - Empty list (i.e x = []) 
    - How to add onto a list (i.e `.append()`)
    - How to modify a list
    - Show some list functions

#### Cool things to show
    - list comprehensions
    - for loop enumeration
