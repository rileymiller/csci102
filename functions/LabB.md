# Function Defenitions

The purpose of this lab is to create function defenitions for the five functions 
outilined in fn.py (attach linked file to download, can be renamed) the functions should do the following

1. Output - This function will save you on all your assignemnts in the future! 
This function will take in a string and print that string with the proper "OUTPUT > your output goes here"
format that all of your assignemnts desire! Hint: This should be a 2 liner, just the fn defenition and a print statement.

2. TriangleArea - This function should take in 2 numerical values and compute the area of a 
triangle given that the first input is the height of the triangle and the second value is the width.
Use the Output function above to print your result.

3. FeetToMeters - This function should perform the conversion from the english unit of Feet (input) to Meters.
Use the Output function to print your result! (2 decmal places)

4. PolarCoords - This function should take in two vales (x,y) and convert that point from cartesian coordinates
to the equivalent location in polar coordinates (you can look this conversion up on google if needed)
Be sure to output your degrees in deg not radians and format to 1 decimal place.

5. ListSort - This function should take in a list and sort this list of numbers. (This method uses insertion sort, if you are feeling up to it, try to impliment quicksort)

Note: Do not use any python defined sort method!
You must perform the sort yourself. This should look like some sort of loop with 
conditional checking to see if one value is smaller than the other.

The following pseudocode may help you get going on this function:
```
i ← 1
while i < length(A)
    j ← i
    while j > 0 and A[j-1] > A[j]
        swap A[j] and A[j-1]
        j ← j - 1
    end while
    i ← i + 1
end while
```

There is no need to call these functions as the test script that will be used will run these EXACT function names so 
make sure that the names of the functions area exactly as listed otherwise the script will fail the tests.

You may add code to your file to test whether your functions are working properly (having excess code wont hurt, it just wont be used)

# Sample Outputs
```
>>> PrintOutput("Hello World")
OUTPUT Hello World

>>> TriangleArea(3,4)
OUTPUT 6.0

>>> TriangleArea(4.2,7.8)
OUTPUT 16.38

>>> FeetToMeters(10)
OUTPUT 3.048

>>> PolarCoords(12,5)
OUTPUT r: 13.0, theta: 22.6 degrees

>>> l =[1,5,10,24,4,7,15,67,9,12]
>>> ListSort(l)
OUTPUT The sorted array is: 1, 4, 5, 7, 9, 10, 12, 15, 24, 67
```