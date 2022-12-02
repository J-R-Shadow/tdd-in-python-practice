print("Operations")

number = 1 + 2 *3 / 4.0
print(number)

remainder = 11 % 3
print(remainder)

squared = 7 ** 2
cubed = 2 ** 3
print(squared)
print(cubed)

helloworld = "hello" + " " + "world"
print(helloworld)

lotsofhellos = "hello" * 10
print(lotsofhellos)

# Operators with lists
even_numbers = [2, 4, 6, 8]
odd_numbers = [1, 3, 5, 7]
all_numbers = odd_numbers + even_numbers
print(all_numbers)

# Just as in strings, Python supports forming new lists with a repeating sequence using the multplication operator:
print([1, 2, 3] * 3)

print("Task 1!")

x = object()
y = object()

x_list = [x] * 10
y_list = [y] * 10
big_list = x_list + y_list

print("x_list contains %d objects." % len(x_list))
print("y_list contains %d objects." % len(y_list))
print("big_list contains %d objects." % len(big_list))

# Testing code
if x_list.count(x) == 10 and y_list.count(y) == 10:
    print("Almost there...")
if big_list.count(x) == 10 and big_list.count(y) == 10:
    print("Great!")

print("Task 2!")

g = object()
o = object()

g_list = [g] * 30
o_list = [o] * 15
go_list = g_list + o_list

print("g_list contains %d objects." % len(g_list))
print("o_list contains %d objects." % len(o_list))
print("go_list contains %d objects." % len(go_list))

if g_list.count(g) == 30 and o_list.count(o) == 15:
    print("Perfect!")
if go_list.count(g) == 30 and go_list.count(o) == 15:
    print("Nice!")

