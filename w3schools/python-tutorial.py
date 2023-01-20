# w3school.com/Python Up to end of Tuples {Part 1}

print("Hello, world!")
#print("Cheers, mate!")

if 5 > 2:
    print("Five is greater than two!") # Will give Syntax error if skip indent.
# Keep to the same number of indents.

# Python Variables
x = 5
y = 89
z = "Variables are cool."

"""
This is how to write a comment in
more than one line with less #
symbols to make it easier to leave large
comments.
"""
print(x)
print(y)
print(z)

x = 4 # x is now of type int
x = "Sally" # x is now of type string
print(x)

# To specify data types of a variable
x = str(3) # x will be '3'
y = int(3) # x will be 3
z = float(3) # x will be 3.0

# To get the type printed
x = 5
y = "John"
print(type(x))
print(type(y))

x = "John"
# Is the same as 
x = 'John'
# " " are easier to use to avoid trouble when writing with ' 

# Variable names are case sensitive.
a = 4
A = "Sally"
# A will not over write a

# Variables can be short like x and y or more discriptive like name, age, total_volume.
"""
Variable name rules:
    A variable name must start with a letter or the underscore character _
    A variable name cannot start with a number
    A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
    Variable names are case-sensitive (age, Age and AGE are three different variables)
"""
# Good names
myvar = "John"
my_var = "Kim"
_my_var = "Alfie"
myVar = "Catherine"
MYVAR = "Timmothy"
myvar2 = "Bianca"

# Bad names
"""
2myvar = "John"
my-var = "John"
my var = "John"
"""
# camelCase, PascalCase, Snake_Case
myVariableName = "John" # Camel
MyVariableName = "John" # Pascal
my_variable_case = "John" # Snake
# Multi word variable names can be hard to read so use Camel Case, Pascal Case, Snake Case to make it easier.

x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)
# number of variables need to match number of values or will get an error.

x = y = z = "Pineapple"
print(x)
print(y)
print(z)

fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

# Output variables
x = "Python is awesome"
print(x)

x = "Python"
y = "is"
z = "awesome"
print(x, y, z)

x = "Python "
y = "is "
z = "awesome"
print(x + y + z)
# If joined by , spaces get put in. If joined by + have to state spaces.

# With number variables + works as an equation
x = 5
y = 10
print(x + y) # Prints 15
"""
Using print() to add strings and numbers together will end in an error.
    x = 5
    y = "John"
    print(x + y)
"""
x = 5
y = "John"
print(x, y) # prints multiple data types together.

# Global Variables
x = "awesome"

def myfunc():
    print("Python is " + x)

myfunc()

x = "awesome"

def myfunc():
    x = "fantastic" # This variable only prints this within the function.
    print("Python is " + x)

myfunc()

print("Python is " + x)

def myfunc():
    global x
    x = "fantastic"

myfunc()

print("Python is " + x)
# Global changed the overall x variable not just within the function.

x = "awesome"

def myfunc():
    global x
    x = "fantastic"

myfunc()

print("Python is " + x)

"""
Built in data types:
    Text type: str
    Numeric Types: int, float, complex
    Sequence Types: list, tuple, range
    Mapping Type: dict
    Set Types: set, frozenset
    Boolean Type: bool
    Binary Types: bytes, bytearray, memoryview
    None Type: NoneType
"""
x = 5
print(type(x)) # Prints data type of x.

# setting the data type.
x = "Hello World" # str
print(type(x)) 

x = 20 # int
print(type(x)) 

x = 20.5 # float
print(type(x)) 

x = 1j # complex
print(type(x)) 

x = ["apple", "banana", "cherry"] # list
print(type(x)) 

x = ("apple", "banana", "cherry") # tuple
print(type(x)) 

x = range(6) # range
print(type(x)) 

x = {"name" : "John", "age" : 36} # dict
print(type(x)) 

x = {"apple", "banana", "cherry"} # set
print(type(x)) 

x = frozenset({"apple", "banana", "cherry"}) # frozenset
print(type(x))

x = True # bool
print(type(x))

x = b"Hello" # bytes
print(type(x)) 

x = bytearray(5) # bytearray
print(type(x)) 

x = memoryview(bytes(5)) # memoryview
print(type(x))

x = None # NoneType
print(type(x))

# setting the specific data type.
"""    
    x = str("Hello World")
    x = int(20)
    x = float(20.5)
    x = complex(1j)
    x = list(("apple", "banana", "cherry"))
    x = tuple(("apple", "banana", "cherry"))
    x = range(6)
    x = dict(name="John", age=36)
    x = set(("apple", "banana", "cherry"))
    x = frozenset(("apple", "banana", "cherry"))
    x = bool(5)
    x = bytes(5)
    x = bytearray(5)
    x = memoryview(bytes(5))
"""

# Python Numbers
    # int
    # float
    # complex
x = 1 # int
y = 2.8 # float
z = 1j # complex

# to verify number data type.
print(type(x))
print(type(y))
print(type(z))

# int - integer is a whole number, positive or negative without decimals of unlimited length.
x = 1
y = 35656222554887711
z = -3255522

print(type(x))
print(type(y))
print(type(z))

# float - floating point number is a number, positive or negative, containing one or more decimals.
x = 1.10
y = 1.0
z = -35.59

print(type(x))
print(type(y))
print(type(z))

# float can also be scientific numbers with "e" to indicate power of 10.
x = 35e3
y = 12E4
z = -87.7e100

print(type(x))
print(type(y))
print(type(z))

# Complex numbers are written with a "j" as the imaginary part:
x = 3+5j
y = 5j
z = -5j

print(type(x))
print(type(y))
print(type(z))

# Converting types
x = 1 # int
y = 2.8 # float
z = 1j # complex

# Convert from int to float:
a = float(x)

# Convert from float to int:
b = int(y)

# Convert from int to complex:
c = complex(x)

print(type(a))
print(type(b))
print(type(c))
# Cannot convert complex numbers into another number type.
print(a)
print(b)
print(c)

# Random numbers.
import random # Python does not have a random() function. 

print(random.randrange(1, 10))

# Python Casting
"""
Specify a Variable Type
    -int() - constructs an integer number from an integer literal, a float literal (by removing all decimals),
      or a string literal (providing the string represents a whole number)
    -float() - constructs a float number from an integer literal, a float literal or a string literal (providing
      the string represents a float or an integer)
    -str() - constructs a string from a wide variety of data types, including strings, integer literals and float literals
"""
# Examples!
# Integers:
x = int(1) # x will be 1
y = int(2.8) # y will be 2
z = int("3") # z will be 3

# Floats:
x = float(1) # x will be 1.o
y = float(2.8) # y will be 2.8
z = float("3") # z will be 3.0
w = float("4.2") #w will be 4.2

# Strings:
x = str("s1") # x will be 's1'
y = str(2) # y will be '2'
z = str(3.0) # z will be '3.0

# Python Strings
print("Hello")
print('Hello') # Both " " and '' are used for strings.

a = "Hello" # Assigning a string to a variable.
print(a)

# Multiline Strings
a = """Lorem ipsu, dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a) # can also be done with '''_'''
# Line breaks are inserted in the result where they appear in the code.

# Strings are Arrays
    # strings in Python are arrays of bytes representing unicode characters.
    # Python does not have a character data type, a single character is simply a string with a length of 1.
    # Square brackets can be used to access elements of the string.

a = "Hello, world!"
print(a[1]) # will print 'e' as character postition starts at 0

# Looping Through a String
for x in "banana":
    print(x) # Prints out each letter of the string seperately.

# String Length
a = "Hello, World!"
print(len(a)) # Prints 13

# Check String
txt = "The best things in life are free!"
print("free" in txt) # Checks if 'free' is in the text.

txt = "The best things in life are free!"
if "free" in txt:
    print("Yes, 'free' is present.") #prints only if 'free' is in text.

# Can check if a phrase or character is not present in a string.
txt = "The best things in life are free!"
print("expensive" not in txt)

txt = "The best things in life are free!"
if "expensive" not in txt:
    print("No, 'expensive' is NOT present.")

# Python Slicing Strings
b = "Hello, World!"
print(b[2:5]) # to return a range of chracters, specify start & end index, seperate with ':'
#above will print from the first 'l' at character 2 and end at the 5th character of the string.

b = "Hello, World!"
print(b[:5]) # Character from the start of the string to postion of 5, (5th postion won't be included in print result.) print : Hello

b = "Hello, World!"
print(b[2:]) # Prints from 2nd character to end of string. print: 'llo, World!'

b = "Hello, World!"
print(b[-5:-2]) # print : 'orl', this is negative indecing. counting back characters from the end rather than the beginning of string.

# Python Modify Strings
a = "Hello, World!"
print(a.upper()) # Uppercase, prints : 'HELLO, WORLD!'

print(a.lower()) # Lowercase, prints : 'hello, world!'

# Remove Whitespace
a = " Hello, World! "
print(a.strip()) # returns "Hello, World!"

# Replace string
a = "Hello, World!"
print(a.replace("H", "J")) # prints message with H replaced by J.

# Split string
a = "Hello, World!"
print(a.split(",")) # returns ['Hello', 'World!']

# Python String Concatentation
a = "Hello"
b = "World"
c = a + b
print(c) # prints 'HelloWorld'

a = "Hello"
b = "World"
c = a + " " + b
print(c) # prints 'Hello World'

# Python Format Strings
"""
cannot combine strings and numbers like this.
age = 36
txt = "My name is John, I am" + age
print(txt)
"""
# We can using the format() method. this method takes the passed argiments, formats them, places them in the string
    # where the place holders {} are:
age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))

# The format() method takes unlimited number of arguments, placing them into the respective place holders.
quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))

# you can use index numbers {0} to be sure the arguments are placed in the correct place holders
quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))

# Escape Characters
"""
    To insert characters that are illegal in a string, use an escape character.
    An escape character is a backslash \ followed by the character you want to insert.
    An example of an illegal character is a double quote inside a string that is surrounded by double quotes:
    txt = "We are the so-called "Vikings" from the north."
    the example will give an error.
"""

txt = "We are the do-called \"Vikings\" from the north."
print(txt) # \ allows illegal characters to be used.
# Other escape characters:
   # \'	Single Quote	
   # \\	Backslash	
   # \n	New Line	
   # \r	Carriage Return	
   # \t	Tab	
   # \b	Backspace	
   # \f	Form Feed	
   # \ooo	Octal value	
   # \xhh	Hex value

# String Methods
"""
Method & Description
    capitalize()	Converts the first character to upper case
    casefold()	Converts string into lower case
    center()	Returns a centered string
    count()	Returns the number of times a specified value occurs in a string
    encode()	Returns an encoded version of the string
    endswith()	Returns true if the string ends with the specified value
    expandtabs()	Sets the tab size of the string
    find()	Searches the string for a specified value and returns the position of where it was found
    format()	Formats specified values in a string
    format_map()	Formats specified values in a string
    index()	Searches the string for a specified value and returns the position of where it was found
    isalnum()	Returns True if all characters in the string are alphanumeric
    isalpha()	Returns True if all characters in the string are in the alphabet
    isdecimal()	Returns True if all characters in the string are decimals
    isdigit()	Returns True if all characters in the string are digits
    isidentifier()	Returns True if the string is an identifier
    islower()	Returns True if all characters in the string are lower case
    isnumeric()	Returns True if all characters in the string are numeric
    isprintable()	Returns True if all characters in the string are printable
    isspace()	Returns True if all characters in the string are whitespaces
    istitle()	Returns True if the string follows the rules of a title
    isupper()	Returns True if all characters in the string are upper case
    join()	Joins the elements of an iterable to the end of the string
    ljust()	Returns a left justified version of the string
    lower()	Converts a string into lower case
    lstrip()	Returns a left trim version of the string
    maketrans()	Returns a translation table to be used in translations
    partition()	Returns a tuple where the string is parted into three parts
    replace()	Returns a string where a specified value is replaced with a specified value
    rfind()	Searches the string for a specified value and returns the last position of where it was found
    rindex()	Searches the string for a specified value and returns the last position of where it was found
    rjust()	Returns a right justified version of the string
    rpartition()	Returns a tuple where the string is parted into three parts
    rsplit()	Splits the string at the specified separator, and returns a list
    rstrip()	Returns a right trim version of the string
    split()	Splits the string at the specified separator, and returns a list
    splitlines()	Splits the string at line breaks and returns a list
    startswith()	Returns true if the string starts with the specified value
    strip()	Returns a trimmed version of the string
    swapcase()	Swaps cases, lower case becomes upper case and vice versa
    title()	Converts the first character of each word to upper case
    translate()	Returns a translated string
    upper()	Converts a string into upper case
    zfill()	Fills the string with a specified number of 0 values at the beginning
"""
# Booleans
# Booleans represents on of two values: True or False.

# Boolean Values
print(10 > 9) # will compare two values and print if the statement is true or false.
print(10 == 9)
print(10 < 9)

a = 200
b = 33

if b > a:
    print("b is greater than a")
else:
    print("b is not greater than a")

# Evaluate Values and Variables
# The bool() function allows the evaluation of any value, gives true or false in return,
print(bool("Hello")) # Evaluates string
print(bool(15)) # Evaluates number

x = "Hello"
y = 15

print(bool(x))
print(bool(y))

"""
Most Values are True
Almost any value is evaluated to True if it has some sort of content.

Any string is True, except empty strings.

Any number is True, except 0.

Any list, tuple, set, and dictionary are True, except empty ones.
"""
# The following will return True:
bool("abc")
bool(123)
bool(["apple", "cherry", "banana"])

# Some values are False
"""
In fact, there are not many values that evaluate to False, except empty values,
 such as (), [], {}, "", the number 0, and the value None. And of course the value 
 False evaluates to False.
"""
bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})

"""
One more value, or object in this case, evaluates to False, and that is if you have
 an object that is made from a class with a __len__ function that returns 0 or False:
"""
class myclass():
    def __len__(self):
        return 0
    
myobj = myclass()
print(bool(myobj))

# Functions can Return a Boolean
    # You can create functions that returns a Boolean Value:
def myFunction():
    return True

print(myFunction())

    # You can execute code based on a Boolean answer of a function:
# Print YES! if function returns True, otherwise Print No!:
def myFunction() :
    return True

if myFunction():
    print("YES!")
else:
    print("NO!")

"""
Python also has many built-in functions that return a boolean value,
 like the isinstance() function, which can be used to determine if an object is of a certain data type:
"""
# Check if an object is an integer or not:
x = 200
print(isinstance(x, int))

# Operators

"""
Python divides the operators in the following groups:
    Arithmetic operators   print(10 + 5)
    Assignment operators   x += 3
    Comparison operators   x == y
    Logical operators      x < 5 and x < 10
    Identity operators     x is y
    Membership operators   x not in y
    Bitwise operators      & (and)
For more details go to: https://www.w3schools.com/python/python_operators.asp
"""

# Python Lists
mylist = ["apple", "banana", "cherry"]
#Lists are used to store multiple items in a single variable.
    #Lists are one of 4 built-in data types in Python used to store collections of data,
    # the other 3 are Tuple, Set, and Dictionary, all with different qualities and usage.
        #Lists are created using square brackets:
thislist = ["socks", "trainers", "boots"]
print(thislist)
"""
List Items
    List Items are ordered, changeable, and allow duplicate values.
    List items are indexed, the first item has index [0], the second item had index [1] etc.

Ordered
    When we say that lists are ordered, it means that the items have a defined order, and that order
     will not change.
    If you add new items to a list, the new items will be placed at the end of the list.

Note: There are some list methods that will change the order, but in general: the order of the items will not change.
    
Changeable
    The list is changeable, meaning that we can change, add, and remove items in a list after it has been created.
"""
# Allow Duplicates
    # Since lists are indexed, lists can have items with the same value:
thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)

# List Length
    #to determin list length use len() function:
clothing = ["shirt", "underwear", "trousers", "socks"]
print(len(clothing))

# List Items - Data Types
    # List items can be of any data type:
list1 = ["apple", "orange", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]

# A list can contain different data types:
list4 = ["abc", 34, True, 40, "male"]

# Type()
    #From Python's perspective, lists are defined as objects with the data type 'list':
    # <class 'list'>
mylist = ["apple", "banana", "cherry"]
print(type(mylist))

# The list() Constructor
    # It's possible to use the list() constructor when creating a new list.
thislist = list(("apple", "orange", "cherry")) # Note the double round-brackets
print(thislist)

"""
Python Collections (Arrays)
    There are four collection data types in the Python programming language:

        List is a collection which is ordered and changeable. Allows duplicate members.
        Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
        Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
        Dictionary is a collection which is ordered** and changeable. No duplicate members.
*Set items are unchangeable, but you can remove and/or add items whenever you like.

**As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.

When choosing a collection type, it is useful to understand the properties of that type. Choosing the right type
 for a particular data set could mean retention of meaning, and, it could mean an increase in efficiency or security.
"""

# Python - Access List Items
    # Access Items
        # List items are indexed and you can access them by referring to the index number:
thislist = ["apple", "banana", "cherry"]
print(thislist[1]) # Prints 'banana'

# Negative Indexing
    # Negative indexing means start from the end
        # -1 refers to the last item, -2 refers to secont to last item etc.
thislist = ["apple", "banana", "cherry"]
print(thislist[-1])

# Range of Indexes
    # You can specify where to start and end the range.
    # When specifying a range, the return value will be a new list with the specified items.
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5]) # Prints ['cherry', 'orange', 'kiwi']

print(thislist[:4]) # Will print ['apple', 'banana', 'cherry', 'orange']

print(thislist[3:]) # Will print ['orange', 'kiwi', 'melon', 'mango']

# Range of Negative Indexes
    # Specify negative indexes if you want to start the search from the end of the list:
print(thislist[-4:-1]) # start at 'orange' but not include 'mango'

# Check if Item Exists
    # To determine if a specfied item is present in a list use the 'in' keyword:
thislist = ["apple", "cherry", "orange"]
if "apple" in thislist:
    print("Yes, 'apple' is in the fruits list")

# Change Item Value
    # To change a specific item, refer to the index number:
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist) # Replaces 'banana' with 'blackcurrant'

# Change a Range of Item Values
    # To change the Value of items within a specific range, define a list with the new values,
        # and refer to the range of index numbers where you want to insert new values:
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist) # Replaces 'banana' and 'cherry'

# If you insert more items than you replace, the new items will be inserted where you specified, and the remaining items will move accordingly:
thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist) # replaces 'banana' and adds 'watermelon'

# If you insert less items than you replace, the new items will be inserted where you specified, and the remaining items will move accordingly:
thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist) # prints ['apple', 'watermelon']

# Insert Items
    # The insert() method inserts an item without replacing any.
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist) # inserts 'watermelon' after 'banana' before 'cherry'

# Add List Items
    # Append Items - add items to the end of a list with append():
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist) # adds 'orange' to end of list

# Insert Items
    # use insert() to insert an item at a specified index
thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist) # inserts 'orange' into the list after 'apple' before 'banana'

# Extend List
    # To append elements from another list to the current list, use the extend() method
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist) # Joins the elements of 'tropical' to the end of 'thislist'

# Add Any Iterable
    # The Extend() method does not have to append lists, you can add any iterable object (tuples, sets, dictionaries etc.).
thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist) # joins 'thistuple' to end of 'thislist'

# Remove List Items
    # To remove specified items use the remove() method
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist) # Removes 'banana'

# Remove specified index
    # pop() method removes a specified index
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist) # removes 'banana'

# if index not specified pop() will remove last item on list.
thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist) # removes 'cherry'

# The del keyword also removes the specified index:
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist) # removes 'apple'

# del can also delete the list completely
thislist = ["apple", "banana", "cherry"]
del thislist

# Clear the List
    # clear() method empties the list but the list remains with no content.
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist) # Prints []

# Loop Lists
    #Loop Through a List using a for loop:
thislist = ["apple", "banana", "cherry"]
for x in thislist:
    print(x) # Prints each item individually till it runs out of items to print

# Loop Through the Index Numbers
    # Use range() and len() to create suitable iterables
thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
    print(thislist[i]) # prints each individual item in order of indexes.
# the iterable created in the above example is [0, 1, 2]

# Using a While Loop
thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
    print(thislist[i])
    i = i + 1

# Looping Usind List Comprehension
    # offers the shorest syntac for looping through lists:
thislist = ["apple", "orange", "cherry"]
[print(x) for x in thislist]

# List Comprehension
    # offers a shorter syntax when you want to create a new list based on values of an existing list.
        # Example:
        # Based on a list of fruits, you want a new list, containing only the fruits with the letter "a" in the name.
# Without List Comprehension
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
    if "a" in x:
        newlist.append(x)

print(newlist)

# With List Comprehension
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]

print(newlist)

# The Syntax
"""
newlist = [expression for item in iterable if condition == True]

The return value is a new list, leaving the old list unchanged.
"""

# Condition
    # The condition is like a filter that only accepts the items that valuate to True.
newlist = [x for x in fruits if x != "apple"]
# The condition if x != "apple"  will return True for all elements other than "apple", making the new list contain all
    #  fruits except "apple".

# The condition is optional and can be omitted:
    # with no if statement:
newlist = [x for x in fruits]

# Iterable
    # The iterable can be any iterable object, like a list, tuple, set etc.
newlist = [x for x in range(10)]
# below is the same example but with a condition
newlist = [x for x in range(10) if x < 5]
# condition is accepting only numbers lower than 5

# Expression
    # The expression is the current item in the iteration, but it is also the outcome, which you can manipulate before it
        #  ends up like a list item in the new list:
newlist = [x.upper() for x in fruits]
# You can set the outcome to whatever you like:
newlist = ['hello' for x in fruits]

# The expression can also contain conditions, not like a filter, but as a way to manipulate the outcome:
newlist = [x if x != "banana" else "orange" for x in fruits]

# The expression in the example above says:
    # "Return the item if it is not banana, if it is banana return orange".

# Sort Lists
    #Sort List Alphanumerically
        # objects in lists have a sort() method that will sort the list alphanumerically, ascending, by default:
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)

numbers1 = [100, 50, 65, 82, 23]
numbers1.sort()
print(numbers1)

# Sort Descending
fruit1 = ["orange", "mango", "kiwi", "pineapple", "banana"]
fruit1.sort(reverse = True)
print(fruit1)

numbers1 = [100, 50, 65, 82, 23]
numbers1.sort(reverse = True)
print(numbers1)

# Customize Sort Function
    # you can also customise your own function using key = function
        # The function will return a number that will be used to sort the list (the lowest number first):
def myfunc(n):
    return abs(n - 50)

numbers1 = [100, 50, 65, 82, 23]
numbers1.sort(key = myfunc)
print(numbers1)

# Case Insensitive Sort
    #By default the sort() method is case sensitive, resulting in all capital letters being sorted before lower case letters:
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print(thislist)

# Luckily we can use built-in functions as key functions when sorting a list.
    # So if you want a case-insensitive sort function, use str.lower as a key function:
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist)

# Reverse Order
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)

# Copy Lists

# copy() function
thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)

# Join Lists
"""
Join Two Lists
there are several ways to join, or concatenate, two or more lists in python.
one of the easiest ways is the + operator.
"""
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)

# another way is by appending all of list4 and list5.
list4 = ["d", "f", "g"]
list5 = [4, 5, 6]

for x in list5 :
    list4.append(x)

print(list4)

# Extending lists by the extend() method.
list6 = ["h", "i", "j"]
list7 = [7, 8, 9]
list6.extend(list7)
print(list6)

# List Methods
"""
append()	Adds an element at the end of the list
clear()	Removes all the elements from the list
copy()	Returns a copy of the list
count()	Returns the number of elements with the specified value
extend()	Add the elements of a list (or any iterable), to the end of the current list
index()	Returns the index of the first element with the specified value
insert()	Adds an element at the specified position
pop()	Removes the element at the specified position
remove()	Removes the item with the specified value
reverse()	Reverses the order of the list
sort()	Sorts the list
"""

# Python Tuples
mytuple = ("apple", "banana", "cherry")

# Tuple
    # Tuples are used to store multiple items in a single variable.
    # Tuple is one of 4 built in data types in Python.
    # A Tuple is a colletion which is ordered and unchangeable.

thistuple = ("apple", "banana", "cherry")
print(thistuple)

# Tuple Items
    # Tuple Items are ordered, unchangeable, and allow suplicate values.
    # Tuple Items are indexed, the first item has index of [0] etc.

# Ordered
    # when we say that tuples are ordered, it means that the items have a defined order and that order will not change.

# Unchangeable
    # Tuples are unchangeable, meaning that we cannot change, add or remove items aftr the tuple has been created.

# Allow Duplicates
    # Since tuples are indexed, they can have items with the same value:
        # Example:
thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)

# Tuple Length
thistuple = ("apple", "banana", "cherry")
print(len(thistuple))

# Create Tuple with One Item
thistuple = ("apple",)
print(type(thistuple))

#NOT a tuple
thistuple = ("apple")
print(type(thistuple))

# Tuple Items - Data Types
    # Tuple items can be of any data type:
tuple1 = ("apple", "banana", "cherry") # String
tuple2 = (1, 5, 7, 9, 3) # integer
tuple3 = (True, False, False) # Boolean

    # Tuple can contain different data types:
tuple4 = ("abc", 34, True, 40, "male")

# type()
    # From Python's perspective, tuples are defined as objects with the data type 'tuple':
    # <class 'tuple'> 
mytuple = ("apple", "banana", "cherry")
print(type(mytuple))

# The tuple() Constructor
    # It is also possible to use the tuple() constructor to make a tuple.
thistuple = tuple(("apple", "banana", "cherry")) # note the double round brackets.
print(thistuple)

# Python Collections (Arrays)
"""
There are four collection data types in the Python programming language:

    List is a collection which is ordered and changeable. Allows duplicate members.
    Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
    Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
    Dictionary is a collection which is ordered** and changeable. No duplicate members.

*Set items are unchangeable, but you can remove and/or add items whenever you like.

**As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.

When choosing a collection type, it is useful to understand the properties of that type. Choosing the right type
 for a particular data set could mean retention of meaning, and, it could mean an increase in efficiency or security.
"""

# Python - Access Tuple Items
    # Access Tuple Items
    # You can access tuple items by referring to the index number, inside square brackets []:
thistuple = ("apple", "banana", "cherry")
print(thistuple[1])

# Negative Indexing
    # Negative indexing means start from the end.
thistuple = ("apple", "banana", "cherry")
print(thistuple[-1])

# Range of Indexes
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])

print(thistuple[-4:-1]) # Range of Negative indexes.

if "apple" in thistuple:
    print("Yes, 'apple' is in fruits tuple.") # check if item exists.

# Update Tuples
    # Tuples are unchangeable, but there are some work arounds.
# Change Tuple Values
    # you can convert a tuple to a list, edit list, turn it back into tuple.
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)

# Add items

thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)

# Add tuple to tuple
thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y

print(thistuple)

# Remove items
thistuple =("apple", "banana", "cherry")
y = list(thistuple)
y.remove("banana")
thistuple = tuple(y)

# Or delete tuple completely
thistuple = ("apple", "banana", "cherry")
del thistuple
# print(thistuple) will result in error because tuple no longer exists.

# Unpack Tuples
    # Unpacking a Tuple
fruits = ("apple", "banana", "cherry") # this is packing a tuple

# But we are also allowed to extract the values back into variables. this is called 'unpacking':
fruits = ("apple", "banana", "cherry")
(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)

# Using Asterisk*
    # If the number of variables is less than the number of values, you can add an * to the variable name and the values
    #  will be assigned to the variable as a list:
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green, yellow, *red) = fruits

print(green)
print(yellow)
print(red)

# If the asterisk is added to another variable name than the last, Python will assign values to the variable until the number
#  of values left matches the number of variables left.
fruits = ("apple", "mango", "papaya", "pineapple", "cherry")
(green, *tropic, red) = fruits

print(green)
print(tropic)
print(red)

# Loop Tuples