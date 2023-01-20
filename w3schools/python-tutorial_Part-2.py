# w3school.com/Python Up to the end of String Formatting {Part 2}

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
