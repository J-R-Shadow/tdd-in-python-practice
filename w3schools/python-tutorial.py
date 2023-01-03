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

