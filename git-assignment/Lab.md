# Working with Git

By now you should be familiar with how to create a repo, clone it, and push and pull 
from that repository. 

This week we will be creating our first python project to put on github.

Create a new python file named utility.py

Inside this file lets define a couple of utility functions.
- PrintOutput: copy this from a preivious lab
- LoadFile: a function that takes in a string and reads all the contents and stores it in a list per line. Then returns this list
- UpdateString: This function takes in 2 strings, and an index integer and will change the character at the given index within the first string to be the string and then print the modified string. (remember strings are immutable so s[5] = 'a' will throw an error)
- ScoreFinder: This function will take in 2 lists and a string, the first list is a list of strings and the second is a list of floats. The string is a name. If the name exists in the list of strings, then print the name of that person along with their associated score from the second list
- Union: This function will take in two lists and return a single list containing the union of the two lists (all values of list A and B no duplicates)
- Intersection: This function will take in two lists and return the intersection of the two lists (values only in both A and B)
- NotIn: This function will take in two lists and return a list of all values in the first list that are not in the second list.

In between each function commit your file in git and push it to your repository. At the end you should have 8 or more commits.
The first being when you create the repo and add the utilities.py file and one commit for each function. It is fine to have more than that.

Once you have completed all functions, submit a link to your github repo in the comments of the submission on canvas. 
From there our graders will download your script and test the code.

# Sample Outputs
```
PrintOutput("Hellow World")
>>> OUTPUT Hello World

lines = LoadFile("test.txt")
Print("OUTPUT", lines)
>>> OUTPUT ["Hello there", "I am a test file", "please load me in and pring me out", "Thanks"]

UpdateString("Hello World", "a", 3)
>> OUTPUT Helao World

l1 = ["Mary", "Cody", "Joe", "Jill", "Xai", "Bodo"]
l2 = [5,8,10,6, 10, 4]
ScoreFinder(l1, l2, "jill") % note that upper or lowercase should both work
>>> OUTPUT Jill got a score of 6
ScoreFinder(l1, l2, "Manuel")
>>> OUTPUT Sorry Manuel is not on the scoreboard

l3 = ["Melvin", "Martian", "Baka", "Xai", "Cody"]
print("OUTPUT", Union(l2, l3))
>>> OUTPUT [5,8,10,6, 10, 4, "Melvin", "Martian", "Baka", "Xai", "Cody"]

print("OUTPUT", Intersection(l1, l3))
>>> OUTPUT ["Xai", "Cody"]

print("OUTPUT", NotIn(l3, l1))
>>> OUTPUT ["Melvin", "Martian", "Baka"]
```

In addition to your code, create a README.md that describes what method you used to create each function along with your name and section
commit and push this readme to your github repo as well. Because of fancy git magic, this should now show up on the repository main page
if you open it in github!