print("Conditions")

x = 2
print(x == 2) # Prints out True
print(x == 3) # Prints out False
print(x < 3) # Prints out True

# Boolean operators
name = "John"
age = 23
if name == "John" and age == 23:
    print("Your name is John, and you are also 23 years old.")

if name == "John" or name == "Rick":
    print("Your name is either John or Rick.")

# The "in" operatior
name = "John"
if name in ["John", "Rick"]:
    print("Your name is either John or Rick.")

statement = False
another_statement = True
if statement is True:
    # do something
    pass
elif another_statement is True: # else if
    # do something else
    pass
else:
    # do another thing
    pass

# example
x = 2
if x == 2:
    print("x equals two!")
else:
    print("x does not equal to two.")

#the "is" operator
x = [1,2,3]
y = [1,2,3]
print(x == y) # prints out True
print(x is y) # prints out False

# The "not" operator
print(not False) # prints out True
print((not False) == (False)) # prints out False

# Exercise
print("Task 1!")

number = 16
second_number = 0
first_array = [1,2,3]
second_array = [1,2]

if number > 15:
    print("1")

if first_array:
    print("2")

if len(second_array) == 2:
    print("3")

if len(first_array) + len(second_array) == 5:
    print("4")

if first_array and first_array[0] == 1:
    print("5")

if not second_number:
    print("6")

print("Task 2!")

number = 79
second_number = 0
first_array = [1,2,3,4,5,6]
second_array = [1,2,3]

if number > 70:
    print("7")

if first_array :
    print("8")

if len(second_array) == 3:
    print("9")

if len(first_array) + len(second_array) == 9:
    print("10")

if first_array and first_array[0] == 1:
    print("11")

if not second_number:
    print("12")

