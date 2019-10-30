# Unit Tests

In computer programming, unit testing is a software testing method by which individual 
units of source code, sets of one or more computer program modules together with 
associated control data, usage procedures, and operating procedures, are tested 
to determine whether they are fit for use. (Wikipedia on Unit Testing)

Essentially unit tests are programs that test correctness of expected output.

In this assignement we will create a series of unit tests to ensure that 
an output is as expected. Typically testing is done using assert statements,
however we are going to substitute conditions for the time being.

All tests should return True or False as a string whether the condition is true or false, 
thus your output lines will look something like.

```
OUTPUT TRUE
OUTPUT FALSE
OUTPUT TRUE
OUTPUT TRUE
OUTPUT FALSE
```

These tests are as follows
1. Multiplication - this test function will take in 3 values, the 
initial operands a and b, and the "output" that was recieved from the multiplication
method used. This function should determine if the 3rd value is indeed the 
product of the two numbers a and b.

2. Bounds Checking - given 3 integers, a lower and upper bound and the length of a list, ensure that 
the bounds do not exceed the bounds for the list. (not less than 0 and not greater than the last index of the list)

3. Decimal Points - this test should take in a float number and determine if the 
number of places after the decimal is actually 3 or not. Assume that only float numbers with 
decimal values will be sent into this function. Hint: You can split a string on the decimal 
then get the length.

4. List Sort - this test will check if a list is actually sorted or not. It will take in a list
and check sortedness (is that a word?) of the list. It'll only be valid if all values are sorted.

5. reversed list - given the original list and a "reversed" list determine whether 
the "reversed" list is trully the reverse of the initial list

6. num O's - given a 2D list of X's and O's ensure that only 5 O's 
exist within the 2D list.


# Sample Output
```
>>> printOutput(mult(3,5,15))
OUTPUT True
>>> printOutput(mult(3,5,10))
OUTPUT False

>>> printOutput(boundsCheck(3,10,15))
OUTPUT True
>>> printOutput(boundsCheck(-1,10,15))
OUTPUT False
>>> printOutput(boundsCheck(2,20,15))
OUTPUT False

>>> printOutput(decimalPoints(3.175))
OUTPUT True
>>> printOutput(decimalPoints(3.1))
OUTPUT False
>>> printOutput(decimalPoints(3.175897))
OUTPUT False

printOutput(isSorted([1,2,3,4,5]))
OUTPUT True
>>> printOutput(isSorted([5,4,3,2,1]))
OUTPUT False

printOutput(reversed([1,2,3,4,5], [1,2,3,4,5]))
OUTPUT False
>>> printOutput(reversed([1,2,3,4,5], [5,4,3,2,1]))
OUTPUT True
>>> printOutput(reversed([1,2,3,4,5], [5,4,4,4,4]))
OUTPUT False

>>> l = [['x','o','x','o','x'], ['x','x','x','x','x','x'], ['x','x','o','x','x'], ['x','o','o','x','x']]
>>> printOutput(numOs(l))
OUTPUT True
>>> l = [['x','o','x','o','o'], ['x','o','x','x','o','x'], ['x','x','o','x','x'], ['x','o','o'], ['o']]
>>> printOutput(numOs(l))
OUTPUT False
```