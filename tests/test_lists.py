print("Lists")

mylist = []
mylist.append(1)
mylist.append(2)
mylist.append(3)
print(mylist[0]) # prints 1
print(mylist[1]) # prints 2
print(mylist[2]) # prints 3

# prints out 1,2,3
for x in mylist:
    print(x)

# following prints an error
    # mylist = [1,2,3]
    # print(mylist[10])

print("Task 1!")
# Exercise
    # Add numbers and strings to the correct lists using the "append" list method.
    # You must add the numbers 1,2, and 3 to the "numbers" list.
    # Add the words 'hello' and 'world' to the strings variable.
    # Also have to fill in the variable second_name using the brackets operator [].

numbers = []
strings = []
names = ["John", "Eric", "Jessica"]

numbers.append(1)
numbers.append(2)
numbers.append(3)

strings.append("hello")
strings.append("world")

second_name = names[1]

print(numbers)
print(strings)
print(names)
print("The second name on the names list is %s" % second_name)

print("Task 2!")

numbers = []
strings = []
names = ["James", "Vincent", "Cedric", "Wilson"]

numbers.append(1)
numbers.append(2)
numbers.append(3)
numbers.append(4)
numbers.append(5)
numbers.append(6)

strings.append("Marco")
strings.append("Polo")

third_name = names [2]

print(numbers)
print(strings)
print(names)
print("The third name on the list is %s" % third_name)
