# 10/29 CSCI 102 Pre-class lecture
**Functions:** This week we will begin covering functions. Functions are used throughout programming and are extremely useful for extractiing functionality throughout a program and for getting rid of repetitive code.

One of the most useful paradigms for understanding and working with functions is the DRY principle (Don't repeat yourself). If you find yourself with redundant logic in your program you may be able to abstract some of that functionality into a function.

### User-defined functions

```
print('hello world')
print('hello world')
print('hello world')
print('hello world')
print('hello world')
```

to: 

```
def printHelloWorld():
    print('hello world')

for i in range(5):
    printHelloWorld()

```

### Parameters
Think of parameters as arguments, what gets passed into a function

Parameter example:

```
def add(foo, bar):
    print(foo + bar)
```

### Return values
One of the more useful attributes of functions is to be able to abstract certain operations into a function and then to return the result of whatever happened inside the function body.

Return example:

```
def add(foo, bar):
    return foo + bar
```

### Dynamic Typing
Python is a **dynamically** typed language which means that it infers the type of data in the program at runtime. Since Python is a dynamically typed language it lends itself to polymorphism nicely. Polymorphism is when you call a function with differently type parameters. 

Programs like Java, C, and C++ are **statically** typed languages which declares the types at compile time.

Dynamic Typing Example:
```
def add(foo, bar):
    return foo + bar

add(3,4)
7
add("yo","sup")
yosup
```

### Function Examples:

```
def get_numbers(num):
    numbers = []
    user_input = input('Enter %s integers:\n' % num)

    i = 0
    for token in user_input.split():
        number = int(token)     # Convert string input into integer
        numbers.append(number)  # Add to numbers list

        print(i, number)
        i += 1

    return numbers
```

### Function Stubs

Sometimes when you're developing a program you may have an idea of what you may like a function to do but you're not quite ready to implement it. In Python to create a function stub (a function that is declared but doesn't do anything) we would use the `pass` keyword. `pass` performs no operation except to act as a placeholder for a required statement.

Pass example:
```
def add(foo, bar):
    pass
```

### Functions are Objects

In Python and other functional languages, functions are first class data types and can be passed to other functions. This is super useful and can drastically improve the readability of your code.

Function as object example:
```
def sub(foo, bar):
    foo - bar

def add(foo, bar):
    foo + bar

add(3, sub(7,4))
```

### Function scoping
Touching back on scoping, variables declared within the scope of a function, can only be used within the function.

Function scoping example:
```
def baz(foo, bar):
    ello = "hi"
    return foo / bar


print(ello) # This will be an error
```






   
