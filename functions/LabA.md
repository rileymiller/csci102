# Rolling Dice (A Second Time)

Hopefully you remember part A for Lab 8 (http://cs-courses.mines.edu/csci102/Labs/Week08.html)
as you'll be coming back to it again now! Except this time with functions!

For this lab write two functions. 

The first takes in a list and prints out the current index along with the value
at that index 
Note: you'll have to add 1 to the index value as the 0th index will denote a 1 on a die.

For example
when the iterator i is 4, the output should be as follows

```
OUTPUT 4 occured n times
```

where n is the number at the index 4.

So why did we do that? That doesnt have much to do with rolling dice.
Well, time for function two. Promise, it'll all make sense soon.

The second function will take in one integer, that is the number of rolls to make.
Seem familiar? Thats right, in this function we will impliment the same logic from 
our previous Lab, feel free to copy and paste. 
BUT WAIT! (we need a list)
this function should start with an empty list and add 1 to the value at the index 
corresponding to the value rolled on the die. This will construct an array of 
counters for all the possible values on a single die (1-6)
This function will then return the constructed list.
An sample output of this this particular function can be seen here: (remember that this should be random so you may not get the same output)

```
>>> numRolls = 10
>>> rollDice(numRolls)
OUTPUT [1,1,5,2,1,0]
```

Lastly lets put this together.
- Below your function defenitions,
- Have the user input a number of rolls numRolls
- Call function1 (function2(numRolls))
This should auto print all necessary output lines and no additional code should be needed at this point.