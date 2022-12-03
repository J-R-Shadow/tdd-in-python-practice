print("String Formatting")

# This prints out "Hello, John!"
name = "John"
print("Hello, %s!" % name)

# This prints put "John is 23 years old."
name = "John"
age = 23
print("%s is %d years old." % (name, age))

# This prints out: A list: [1,2,3]
mylist = [1,2,3]
print("A list: %s" % mylist)

# List of basic argument specifiers:
# %s - String (or any object with a string representaion, like numbers.)
# %d - Integers
# %f - Floating point numbers
# %.<number of digits>f - Floating point numbers with a fixed amount of digits to the right of the dot.
# %x/%X - Integers in hex representaion (lowercase/uppercase)

print("Task 1!")
# Exercise
    # you need to write a format string which prints out the datausing the following syntax: Hello John Doe.
    # Your current balance is $53.44.
        # data = ("John", "Doe", 53.44)
        # format_string = "Hello"

        #print(format_string % data)

data = ("John", "Doe", 53.44)
format_string = "Hello, %s %s. Your current balance is $%s."

print(format_string % data)

print("Task 2!")

data = ("James", "Shadow", 44.39)
format_String = "Hello, %s %s. Your current balance is $%s."

print(format_string % data)