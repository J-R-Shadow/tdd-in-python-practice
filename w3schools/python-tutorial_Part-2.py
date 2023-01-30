# w3school.com/Python Up to the end of String Formatting {Part 2} (1199 line)

# Python Sets
myset = {"apple", "banana", "cherry"}

# Set
"""
-Sets are used to store multiple items in a single variable.
-Set is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Tuple, and Dictionary, all with different qualities and usage.
-A set is a collection which is unordered, unchangeable*, and unindexed.
    * Note: Set items are unchangeable, but you can remove items and add new items.
-Sets are written with curly brackets.
"""

thisset = {"mango", "pineapple", "coconut"}
print(thisset)  # Note! sets are unordered, so you cannot be sure in which order the items will appear.

"""
Set Items
    Set items are unordered, unchangeable, and do not allow duplicate values.
Unordered
    Unordered means that the items in a set do not have a defined order.
- Set items can appear in a different order every time you use them, and cannot be referred to by index or key.
Unchangeable
    Set items are unchangeable, meaning that we cannot change the items after the set has been created.
- Once a set is created, you cannot change its items, but you can remove items and add new items.
Duplicates Not Allowed
    Sets cannot have two items with the same value.
"""

thisset = {"mango", "pineapple", "coconut", "mango"}
print(thisset) # Duplicates will be ignored, 'mango' will appear once not twice.

# Get the length of a Set
thisset = {"mango", "pineapple",  "coconut"}
print(len(thisset))

# Set Items - Data Types
set1 = {"apple", "banana", "cherry"} # Strings
set2 = {1, 3, 5, 7, 9} # Integers
set3 = {True, False, True} # Booleans

set4 = {"abc", 34, True, 40, "male"} # Can be mix of all three data types.

myet = {"mango", "pineapple", "coconut"}
print(type(myset)) # Class type 'set'

# Access Set Items
    # You CANNOT access items in a set by referring to an index or a key
    # You CAN loop through the set items using a 'for' loop, or ask if a specified value is present in a set, by using the 'in' keyword.
thisset = {"mango", "pineapple", "coconut"}

for x in thisset:
    print(x)

thisset = {"mango", "pineapple", "coconut"}

print("banana" in thisset) # Prints False
# Once a set is created, you cannot change its items but can add new ones.

# Add Set Items
    # To add one item to a set use the add() method
thisset = {"mango", "pineapple", "coconut"}

thisset.add("papaya")

print(thisset)

# Add Sets
    # To aff items from another set into the current set, use the update() method
thisset = {"mango", "pineapple", "coconut"}
fruit = {"apple", "orange", "peach"}

thisset.update(fruit)
print(thisset)

# Add Any Iterable
    # The object in the update() method does not have to be a set, it can be any iterable object (tuples, lists, dictionaries etc.)
thisset = {"mango", "pineapple", "coconut"}
mylist = ["kiwi", "pomegranate"]

thisset.update(mylist)
print(thisset)

# Remove Set Items
    # To remove an item in a set, use the remove(), or the discard() method.

#remove()
thisset = {"mango", "pineapple", "coconut", "banana"}

thisset.remove("banana") # If item doesn't exist will raise an Error.

print(thisset)

# discard()
thisset = {"apple", "mango", "pineapple", "coconut"}

thisset.discard("apple") # If item doesn't exist will Not raise an Error.

print(thisset)

# pop()
    # You can also use the pop() method to remove an item, but this method will remove a random item, so you cannot be sure what item that gets removed.
    # The return value of the pop() method is the removed item.
thisset = {"mango", "pineapple", "coconut", "banana"}

x = thisset.pop()

print(x)

print(thisset)

# clear()
thisset = {"apple", "banana", "cherry"}

thisset.clear()
print(thisset) # Prints 'set()'

# del
thisset = {"mango", "pineapple", "coconut"}

del thisset
# print(thisset) : will print an Error because name does not exist.

# Loop Sets
thisset = {"mango", "pineapple", "coconut"}

for x in thisset:
    print(x)

# Join Sets
    # There are several ways to join two or more sets in Python.
    # You can use the union() method that returns a new set containing all items from both sets, or the update() method that inserts all the items from one set into another:
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)

set4 = {"d", "e", "f"}
set5 = {4, 5, 6}

set4.update(set5)
print(set4)
# Note: Both union() and update() will exclude any duplicate items.

# Keep ONLY the Duplicates
    # The intersection_update() method will keep only the items that are present in both sets.
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.intersection_update(y)
print(x) # Returns {'apple'}

# The intersection() method will return a new set, that only contains the items that are present in both sets.
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.intersection(y)
print(z)

# Keep All, But NOT the Duplicates
    # The symmetric_difference_update() method will keep only the elements that are NOT present in both sets.
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.symmetric_difference_update(y)

print(x)

# The symmetric_difference() method will return a new set, that contains only the elements that are NOT present in both sets.
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.symmetric_difference(y)
print(z)

# Set Methods
"""
-add()	Adds an element to the set
-clear()	Removes all the elements from the set
-copy()	Returns a copy of the set
-difference()	Returns a set containing the difference between two or more sets
-difference_update()	Removes the items in this set that are also included in another, specified set
-discard()	Remove the specified item
-intersection()	Returns a set, that is the intersection of two other sets
-intersection_update()	Removes the items in this set that are not present in other, specified set(s)
-isdisjoint()	Returns whether two sets have a intersection or not
-issubset()	Returns whether another set contains this set or not
-issuperset()	Returns whether this set contains another set or not
-pop()	Removes an element from the set
-remove()	Removes the specified element
-symmetric_difference()	Returns a set with the symmetric differences of two sets
-symmetric_difference_update()	inserts the symmetric differences from this set and another
-union()	Return a set containing the union of sets
-update()	Update the set with the union of this set and others
"""

# Python Dictionaries
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

# Dictionary
    # Dictionaries are used to store datavalues in key:value pairs.
    # A dictionary is a collection which is ordered*, Changeable and do not allow duplicates.
    # *As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.
    # Dictionaries are written with curly brackets, and have keys and values:
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print(thisdict)

# Dictionary Items
    # Dictionary items are ordered, changeable, and does not allow duplicates.
    # Dictionary items are presented in key:value pairs, and can be reffered to by using the key name:
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print(thisdict["brand"])

# Ordered or Unordered
    # When we say that dictionaries are ordered, it means that the items have a defined order, and that order will not change.
    # Unordered means that the items does not have a defined order, you cannot refer to an item by using an index.

# Changeable
    # Dictionaries are changeable, meaning that we can change, add or remove items after the dictionary has been created.

# Duplicates Not Allowed
    # Dictionaries cannot have two items with the same key:
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964,
    "year": 2020
}
print(thisdict) # "year" will be overwritten from 1964 to 2020

# Dictionary Length
    # To determine how many items a dictionary has, use the len() function:
print(len(thisdict))

# Dictionary Items - Data Types
    # The Values in dictionary items can be of any data type:
thisdict = {
    "brand": "Ford", # str
    "electric": False, # boolean
    "year": 1964, # int
    "colors": ["red", "white", "blue"] # list
}

# Type()
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print(type(thisdict))

# The dict() Constructor
    # It is also possible to use the dict() constructor to make a dictionary.
thisdict = dict(name = "John", age = 36, country = "Norway")
print(thisdict)

# When choosing a collection type, it is useful to understand the properties of
#  that type. Choosing the right type for a particular data set could mean retention
#   of meaning, and, it could mean an increase in efficiency or security.

# Accessing Items
    # You can access the items of a dicionary but referring to its key name, inside square brackets:
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
x = thisdict["model"]

# There is also a method called get() that will give you the same result:
x = thisdict.get("model")

# Get Keys
    # The keys() method will return a list of all the keys in the dictionary.
x = thisdict.keys()

# The list of the keys is a view of the dictionary, meaning that any changes done to the dictionary will be reflected in the keys list.
car = {
    "brand": "Ford",
    "model": "Mustange",
    "year": 1964
}
x = car.keys()

print(x) # Before the change.

car["color"] = "white"

print(x) # After the change.

# Get Values
    # The values() method will return a list of all the values in the dictionary.
x = thisdict.values()

# the list of the values is a view of the dictionary, meaning that any changes done to the dictionary will be reflected in the values list.
car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

x = car.values()

print(x) # Before the change

car["year"] = 2020

print(x) # After the change

# Get Items
    # The items() method will return each item in a dictionary, as tuples in a list.
x = thisdict.items()

# The returned list is a view of the items of the dictionary, meaning that any changes done to the dictionary will be reflected in the items list.
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.items()

print(x) #before the change

car["year"] = 2020

print(x) #after the change 

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.items()

print(x) #before the change

car["color"] = "red"

print(x) #after the change 

# Check if Key Exists
    # To determine if a specified key is present in a dictionary use the in keyword:
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
if "model" in thisdict:
    print("Yes, 'model' is one of the keys in the thisdict dictionary")

# Change Dictionary Items
    # Change Values
    # You can change the value of a specific item by referring to its key name:
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
thisdict["year"] = 2018

# Update Dictionary
    # The update() method will update the dictionary with the items from the given argument.
    # The argument must be a dictionary, or an iterable object with key:value pairs.
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
thisdict.update({"year": 2020})

# Add Dictionary Items
    # Adding an item value to the dictionary is done by using a new index key and assigning a value to it:
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
thisdict["color"] = "red"
print(thisdict)

# Update Dictionary
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
thisdict.update({"color": "red"})

# Removing Dictionary Items
    # There are several ways to remove items from a dictionary:
# pop()- removes specified key name:
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
thisdict.pop("model")
print(thisdict)

# popitem() - The popitem() method removes the last inserted item 
#  (in versions before 3.7, a random item is removed instead):
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.popitem()
print(thisdict)

# del - The del keyword removes the item with the specified key name:
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict["model"]
print(thisdict)
"""
can also delete a complete dictionary.
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict
print(thisdict) #this will cause an error because "thisdict" no longer exists. 
"""

# The clear() method empties the dictionary:
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.clear()
print(thisdict)

# Loop Dictionaries.
    # You can loop through a dictionary by using a for loop.
    # When looping through a dictionary, the return value are the keys of the dictionary,
    #  but there are methods to return the values as well.
for x in thisdict:
    print(x) # print all key names one by one

for x in thisdict:
    print(thisdict[x]) # print all values in dictionary one by one

for x in thisdict.values():
    print(x) # to also return values of a dictionary

for x in thisdict.keys():
    print(x) # to return the keys of a dictionary

for x, y in thisdict.items():
    print(x, y) # loop through keys and values by using the items() method

# Copy Dictionaries
    # You cannot copy a dctionary simply by typing 'dict2 = dict1' because: 
    #   dict2 will only be a reference to dict1, and changes made in dict1 will automatically be made in dict2.
    # There are ways to make a copy, one way is to use the built-in Dictionary method copy().
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
mydict = thisdict.copy()
print(mydict)

# Another way to make a copy is to use the built-in function dict().
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
mydict = dict(thisdict)
print(mydict)

# Nested Dictionaries
    # A dictionary can contain dictionaries, this is called nested dictionaries.
myfamily = {
    "child1" : {
        "name" : "Emily",
        "year" : 2004
    },
    "child2" : {
        "name" : "Tobias",
        "year" : 2007
    },
    "child3" : {
        "name" : "Linus",
        "year" : 2011
    }
}
# Or, if you want to add three dictionaries into a new dictionary:
child1 = {
    "name" : "Emily",
    "year" : 2004
}
child2 = {
    "name" : "Tobias",
    "year" : 2007
}
child3 = {
    "name" : "Linus",
    "year" : 2011
}
myfamily = {
    "child1" : child1,
    "child2" : child2,
    "child3" : child3
}

# Dictionary Methods
"""
clear()	Removes all the elements from the dictionary
copy()	Returns a copy of the dictionary
fromkeys()	Returns a dictionary with the specified keys and value
get()	Returns the value of the specified key
items()	Returns a list containing a tuple for each key value pair
keys()	Returns a list containing the dictionary's keys
pop()	Removes the element with the specified key
popitem()	Removes the last inserted key-value pair
setdefault()	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
update()	Updates the dictionary with the specified key-value pairs
values()	Returns a list of all the values in the dictionary
"""

# Python - if ... else
    # Conditions and If statements
"""
python supports the usual logical conditions from mathmatics:
    - Equals: a == b
    - Not Equals: a != b
    - Less than: a < b
    - Less than or equal to: a <= b
    - Greater than: a > b
    - Greater than or equal to: a >= b
These conditions can be used in several ways, most commonly in "if statements" and loops.
an "if statement" is written by using the 'if' keyword.
"""
a = 33
b = 200
if b > a:
    print("b is greater than a")

# In this example we use two variable, a and b , which are used as part of the if statement to test wether b is greater than a. As a is 33, and b is 200, we know
#  that 200 is greater than 33, and so we print to screen that "b is greater than a".

# Indentation
"""
Python relies on indention (whitespace at the beginning of a line) to define scope in the code.
Other programming languages use curle-brackets for this purpose.
If statement, without indentation will raise an error:
a = 33
b = 200
if b > a:
print("b is greater than a")
"""
# Elif
    # The 'elif' keyword is Python's way of saying "if the previousconditions were not true, then try this condition".
a = 33
b = 33
if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")
# In the example ais equal to b, so the first condition is not true, but the 'elif' condition is.

# Else
    # The 'else' keyword catches anything which isn't caught by the preceding conditions.
a = 200
b = 33
if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")
else:
    print("a is greater than b")
# In this example a is greater than b, so the first condition is not true, also the 'elif' condition is not true, so we
    # go to the else condtion and print to screen that "a is greater than b".
# You can also have an else without the elif:
a = 200
b = 33
if b > a:
    print("b is greater than a")
else:
    print("b is not greater than a")

# Short Hand If
    # If you have only one statement to execute, you can put it on the dame line as the if statement.
if a > b: print("a is greater than b")

# Short Hand If ... Else
    # If you have only one statement to execute, one for if, and one for else, you can put it all on the same line:
a = 2
b = 330
print("A") if a > b else print("B")
    # This technique is known as Ternary Operators, or Conditional Expressions.
# You can also have multiple else statements on the same line:
a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")

# And
    # The 'and' keyword is a logical operator, and is used to combine conditional statements:
a = 200
b = 33
c = 500
if a > b and c > a:
    print("Both conditions are True")

# Or
    # The 'or' keyword is a logical operator, and is used to combine conditional statemenets:
a = 200
b = 33
c = 500
if a > b or a > c:
    print("At least one of the conditions is True")

# Not
    # The not keyword is a logical operator, and is used to reverse the result of the conditional statement:
a = 33
b = 200
if not a > b:
    print("a is NOT greater than b")

# Nested if
    # You can have if statements inside if statments, this is called nested if statements.
x = 41

if x > 10:
    print("Above ten,")
    if x > 20:
        print("and also above 20!")
    else:
        print("but not above 20.")

# The pass statement
    # if statments cannot be empty, but if you for some reason have an if statement with no content, put in the pass statement to avoid getting an error.
a = 33
b = 200

if b > a:
    pass

# While Loops
# Loops
    # python has two primative loop commands: While and For
#The While Loop
    # With the 'while' loop we can execute a set of statements as long as a condtion is true.
i = 1
while i < 6:
    print(i)
    i += 1  # Remember to increment i or else the loop will continue forever.
# The while loop requires relevant variables to be ready, in this example we need to define an indexing variable, i, which is set to 1.

# The break statement
    # With the break statement we can stop the loop even if the while condition is true:
i = 1
while i < 6:
    print(i)
    if i == 3:
        break
    i += 1

# The continue statement
    # with the continue statement we cn stop the current iteration, and continue with the next:
i = 0
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)

# The else statement
    # With the else statement we can run a block of code once when the condition no longer is true:
i = 1
while i < 6:
    print(i)
    i += 1
else:
    print("i is no longer less than 6")

# For Loops
    