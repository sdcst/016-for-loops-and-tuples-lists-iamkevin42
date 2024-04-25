#! python3
"""
###### Task 2
Ask the user to enter a name.
Check the name against a tuple that contains a series of names to see if it is a match. Use a for loop this time instead of a single if with multiple
logical operators
(2 points)

inputs:
str name

outputs:
"That name is in the list"
"That name is not in the list"

example:
Enter a name: Grace
That name is not on the list

example:
Enter a name: Lebron
That name is on the list
"""

nameList = ("Lebron","Kobe","Michale","Shaq","Dennis")

for i in nameList:
    a = input("Please enter a name\n")
    if a in nameList:
        print('This name is on the list')
    else:
        print("This name is not on the list")
        break
