print("Basic String Operations")

astring = "Hello World!"
astring2 = 'Hello World!'

astring = "Hello World!"
print("single quotes are ' '")

print(len(astring)) # prints out 12

astring = "Hello World!"
print(astring.index("o")) # prints out 4. Did not print five because count starts at 0 not 1.

astring = "Hellow World!"
print(astring.count("l"))

astring = "Hello World!"
print(astring[3:7])
# Prints a slicer of the string starting at index 3 ending at 6. if only one number in brackets it
# will give you the single character at that index. If leaving first number on " :6" will give 
# slice from start to number given. If "6: " slice will be from numver given to end of string.

# You can even put negative numbers inside the brackets. They are an easy way of starting at the
# end of string rather than beginning. "-3" means 3rd character from the end.

astring = "Hello World!"
print(astring[3:7:2])
# Prints the characters of string from 3 to 7 skipping one character. This is extended slice syntax.
# The general form is [start:stop:step].

astring = "Hello World!"
print(astring[3:7])
print(astring[3:7:1])
# Both produce same output.

# There is no function like strrev in C to reverse a string. But with the above mentioned type of 
# slice syntax you can easily reverse a string like this:
astring = "Hello World!"
print(astring[::-1]) 

# This
astring = "Hello World!"
print(astring.upper())
print(astring.lower())
# These make a new string with all letters converted to upper and lower case, respectively.

astring = "Hello World!"
print(astring.startswith("Hello"))
print(astring.endswith("asdfasdfasdf"))
# This is used to determine whether the string starts or ends with something. The first will
# be True and the second will be False.

astring = "Hello World!"
afewwords = astring.split(" ")
# This splits the string into a bunch of strings grouped together in a list. Since this example 
# splits at a space, the first item will be "Hello", and the second will be "World!".

print("Task 1!")

s = "Strings are awesome!" # Length should be 20
print("Length of s = %d" % len(s))

# First a should be index 8.
print("The first occurrence of the letter a = %d" % s.index("a"))

# Number of a's should be 2.
print("The letter 'a' occurs %d times" % s.count("a"))

# Slicing the string into bits.
print("The first five characters are '%s'" % s[:5]) # start to 5
print("The next five characters are '%s'" % s[5:10]) # 5 to 10
print("The thirteenth character is '%s'" % s[12]) # Just number 12
print("The characters with odd index are '%s'" % s[1::2]) # 0-based indexing
print("The last five characters are '%s'" % s[-5:]) # 5th-from-last to end

# Convert everything to uppercase
print("String in uppercase: %s" % s.upper())

# Convert everything to lowercase
print("String in lowercase: %s" % s.lower())

# Check how a string starts
if s.startswith("Str"):
    print("String starts with 'Str'. Good!")

#check how a string ends
if s.endswith("ome!"):
    print("String ends with 'ome!'. Good!")

# Split string into three seperate strings, each containing one word.
print("Split the words of the string: %s" % s.split(" "))

print("Task 2!")

f = "Python Coding is fun and cool."

print("Length of 'f' = %d" % len(f))

print("The first occurance of 'n' = %d" % f.index("n"))

print("The letter 'o' occurs %d times." % f.count("o"))

print("The first five characters are '%s'" % f[:5])
print("The next five characters are '%s'" % f[5:10])
print("The thirteenth character is '%s'" % f[13])
print("The last five characters are '%s'" % f[-5:])

print("String in uppercase: %s" % f.upper())
print("String in lowercase: %s" % f.lower())

if f.startswith("Pyth"):
    print("String starts with 'Pyth'. Great!")

if f.endswith("ool."):
    print("String ends with 'ool.' Good!")

print("Split the words of the string: %s" % f.split(" "))

