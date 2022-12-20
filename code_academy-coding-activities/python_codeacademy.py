def main():
    print("Hello World!")

if __name__ == "__main__":
    main()

def main():
    print("This line is printed directly from the main function of the program")
    secondary_function()

def secondary_function():
    print("This line is printed from a secondary function call within the main function")

if __name__ == "__main__":
    main()

seconds = 2500
minutes = seconds / 60 # calculating minutes from seconds

def calculate_minutes(seconds):
    # This function calculates the time in minutes
    # from given seconds.
    minutes = seconds / 60
    return minutes

# This function takes
# one argument, num and
# returns num squared.
def square(num):
    numSquared = num * num
    return numSquared

# Several test cases
# to verify the function
# is working as expected.

print(square(2)) # Prints 4
print(square(5)) # Prints 25
print(square(8)) # Prints 64
print(square(10)) # Prints 100

input("What is your name?")

name = input("What is your name?")

print("Very nice to meet you!")

# To include name given by person
print("Very nice to meet you, ", name, "!")

name = "Barbara"
age = "32"

print("Very nice to meet you! My name is", name, "and I am", age, "years old.")
# can also use concatenate variables.
print("Very nice to meet you my name is" + name, "and I am" + age + "years old.")
# works as long as variables are provided as strings.

# Formatted String Literals
print(f"Very nice to meet you, {name}!")

# for name all in uppercase
print(f"Very nice to meet you, {name.upper()}!")

# str.format()
print("Very nice to meet you, {}!" .format(name))

name = input("What is your name?")
hometown = input("And where are you from?")
    print("Very nice to meet you, {}!" .format(name), f"from {hometown}")

greet_someone()

# Variables
name = "Grace"
name = "Ari" # changes name variable from Grace to Ari.

temperature = 97.5

sum_of_two_number = 4 + 2

# Casting
temperature = str(97.5)
# str() takes a value and converts it to string.

# Printing the Data Type
temperature = str(97.5)
type(temperature) # Prints str

int_value = 4
print(int_value)
print(type(int_value))

print()

float_value = 5.9
print(float_value)
print(type(float_value))

