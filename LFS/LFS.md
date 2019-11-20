# Large File Systems (LFS)

This is it, our final lab.

Congratz! You've made it! 

Lets put all of that newfound knowledge to good use in a way that you would 
realistically see in your career. For this final culmination of our efforts this
semester we will be working with a large file system created by someone else and 
you are tasked to modify it.

Go to this github link (https://github.com/BloodRaine/zork-py) and fork the repository.
![Forking a Repo](fork.png)

Once you have the repository forked, it should show up on the list of repositories on your account.
Clone the repository onto your computer.

Go ahead and run it to see what it does!

# Zork
If you unfamiliar, ZORK is a text based adventure game that was developed in ancient times 
(relatively). The goal was not so obvious, but simple. Find the treasure and dont get eaten by a monstorous grue.
There were various "rooms" all with interactable objects and connected passages between them. lots of secret puzzles
and fun areas to explore, all while trying your best to avoid typing "kick the bucket" to quickly exit the game.

We've provided you with the code to run the game zork, however, the code is poor and the game is missing some functionality.
First off, there's no grue! Well thats no fun how are we supposed to get eaten in the dark? Also, I dont know if you noticed,
but we can read the leaflet before even opening the mailbox that it's in and picking it up! This is all kinds of wrong.

Lets fix this up.

# Final Lab

For this final lab, we will be re-organizing existing code and adding additional functionality to it.
The existing code all exists in several files that each have their own purpose and functionality.
Looking at the zork.py file, we can see that the Play_Zork function is doing most of the work, 
and its in a bunch of nested for loops. This is generally speaking poor practice to structure code
this kind of code in this way.

# Part A

The goal for starters is strait-forward, functionalize this mess. Each "room" is 
currently contained within an internal while loop structure. Alternatively we can think
of a better way for this game to run. If we keep track of whether the player is alive,
and what room they are currently in, we can send the program into a different function 
for each room. some of this we will want to do in the main.py file and some within the zork.py file.

The main.py should contain the overarching logic to control the game. That is:
1. The current status (alive or dead) if dead exit the game
2. The user input (ask the user what they would like to do)
3. Room number logic (depending on different room numbers, call zork.function_name_of_room_number)
4. A List of the currently held items. Those things can be handy. (You start out with none) 
(this is for extra credit in Part B and isn't necessary if you dont do the extra credit)

The zork.py file should only contain functions, one for each room to be exact. 

Each should be structured to where if we were to just load in the zork.py file, 
we could call Room0(user_input_string, itemList) and get an expected output based upon the 
string that went in. Each of these functions should be updated to contain "OUTPUT" before the 
non "------" statements being printed, and should return a truth value (indicating if the user is living or dead) and  
the roomNumber (to update your room and should the user choose to move around).

For example:
```
def room#(input_string_from_user):
    ...
    return [roomNum, livingStatus] # either the same room num or different if moved
```

NOTE: In order to return multiple values from a function you must return them as a list, tuple, object, or dictionary.

# Part B - Inventory Managment (Extra Credit)
You'll notice there was also an items.py file. This file contains some code to hold all the known items in the game and
three functions, one to pick up an item, one to put an item down, and a function to use an item. Or at least it should.
it doesnt contain everything as we were in the middle of writing it when we realized that the rest of the code needed some serious help.
Thats ok, you can help out here too. After re-writing the code during part A you probably know all of the items in the game.

1. Fill in the lists so that each room list contains the items within that particular room (change the names to match which room is which better and add additional ones or take some away if you should need)
2. Change the print statements to contain the OUTPUT keyword
3. Finish writing the put down function and add the necessary code in zork.py to update the user's inventory
4. Define the useItem function which takes in an itemName and itemList. If the item exists within the list, print the folowing and return True

# Part C - New Room (Extra Credit)
TODO have students create a new room with desired items/functionality within (enter grue!)