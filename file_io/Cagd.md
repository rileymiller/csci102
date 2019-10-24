# Cag'd
In rememberance of our favorite memeable National Treasure character we're going to practice our file I/O by reading and writing to files.


When writing to the file we will convert every `&` to a `%`, every `%` to an `&`, and every `/` to a `~`.
To begin:
- Open "caged.txt"
- Parse the file, character by character
    - If the character is `&`, `%`, or `~`, convert to the correct character.
- Write converted file to a new file called "caged_convert.txt"

Output: Should be a Nicholas Cage ASCII art with the correct conversions. Beware, the outputted file will be diffed with the inputted file and you will receive 0 credit if you try to output the inputted file.