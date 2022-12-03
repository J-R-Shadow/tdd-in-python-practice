print("Variables and Types")

myint = 7
print(myint)

# To define a floating number we useeither of the two below:
myfloat = 7.0
print(myfloat)

myfloat = float(7)
print(myfloat)

# Strings can be represented with both "_" or '_'
mystring = 'Hello'
print(mystring)

mystring = "Hello"
print(mystring)
# Using " " allows the use of ' without distrupting the string early.
mystring = "Don't worry about using apostrophes."
print(mystring)

one = 1
two = 2
three = one + two
print(three)

hello = "Hello"
world = "world"
helloworld = hello + " " + world
print(helloworld)

a, b = 3, 4
print(a, b)

# Mixing between numbers and strings is not supported
# This will not work:
# one = 1
# two = 2
# hello = "hello"
# print(one + two + hello)

print("Task 1!")
# Exercise
    # The aim of this exercise is to create a string, an integer, and a floating point number.
    # The string should be named mystring and should contain the word "hello". The floating point
    # number should be named myfloat and should contain the number 10.0, and the integer should be 
    # named myint and contain the number 20.

mystring = "hello"
myfloat = 10.0
myint = 20

# Testing code
if mystring == "hello":
    print("String is %s" % mystring)
if isinstance(myfloat, float) and myfloat == 10.0:
    print("Float is %f" % myfloat)
if isinstance(myint, int) and myint == 20:
    print("Integer is %d" % myint)

print("Task 2!")
mystring = "Peekaboo!"
myfloat = float(54)
myint = 62

# Test
if mystring == "Peekaboo!":
    print("This string says %s" % mystring)
if isinstance(myfloat, float) and myfloat == 54.0:
    print("The floating number is %f" % myfloat)
if isinstance(myint, int) and myint == 62:
    print("The Integer is %d" % myint)

