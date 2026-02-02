"""
Types of functions:
- Built-in Functions: Predefined functions provided by the programming language.
- User-defined Functions: Functions created by the user to perform specific tasks.
"""

print("I am built in function print()")  # Example of a built-in function
num = input("Enter a number: ")  # Example of a built-in function to take user input
# Converting the input string to an integer using a built-in function
num= int(num)

# converting string to float
num_float = float(num)

# len
name = "Bishal Rijal"
length = len(name)
print("Length of the name is:", length)

# type
its_type = type(num)
print("The type of num is:", its_type)

# 'A' = 65

char = 'B'
print(ascii_value := ord(char))  # Using the walrus operator to assign and print ASCII value