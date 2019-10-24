# Steal (Parse) the Declaration of Independence

Nicholas Cage once said the bold phrase, "I'm going to steal the Declaration of Independence." 

In this lab we're going to parse the Declaration of Independence and output the number of occurences of every word in the corpus. This lab is to focus on the fundamental of reading in files using the file I/O functions that Python provides.

To begin:
- Open the "Declaration_of_Independence.txt" file and store it in a variable.
- Parse through the file and count the occurences of each unique word in the document.
- If the word hasn't been found, add it to the list as a tuple where the first argument is the string and the second argument is the number of occurences, 0 in this case (i.e. while parsing the word "America", if "America" hadn't been found yet you would add ("America", 1))
- If the word has been found, find the tuple in the list and increment the number of occurences in the second argument of the tuple (i.e ("America", 2))

After you have finished parsing the document, sort the list in alphabetical order.

Then, output the list with one argument on each line:

```
OUTPUT "America" 4
OUTPUT "the" 54
OUTPUT "Declaration" 3
OUTPUT "a" 123
```