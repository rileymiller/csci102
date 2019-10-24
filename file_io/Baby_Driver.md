# Baby Driver
In this lab you will be given a massive csv file from https://catalog.data.gov filled with baby names recorded in the year 2011. You will be expected to output the most popular baby name(s) in the corpus.

To Begin:
- Open up "Popular_Baby_Names.csv"
- Parse through the file row by row. 
    - Keep track of the most commonly occuring name (use the csv module and the count field in the file). 
    - One way to approach this is to find the most commonly occuring name(s) by using the `max` function on the count field or by manually keeping track by looping through the corupus. Then, loop through and find the most commonly occuring names. Since there are ties in the document you must keep track of every instance of a the most commonly occuring names.
- Output the names

```
MOST POPULAR
OUTPUT "Jane" 342
OUTPUT "Clara" 342
.
.
.
.
OUTPUT "Jeff" 342
```


Use Popular_Baby_Names_Rubric.csv and excel to find the most common names for Autograder.