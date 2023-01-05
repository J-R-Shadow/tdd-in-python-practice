# w3school.com/Python

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

