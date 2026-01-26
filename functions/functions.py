

# Functions are defined using the 'def' keyword followed by the function name and parentheses.
"""
def function_name(parameters):
    # function body
    return value
"""
# Function is a reusable block of code that performs a specific task.

# Function without parameters and without return value
def greet(): # Defining a function named 'greet'
    print("Hello, World!") # Function body that prints a greeting message


greet()  # Calling the function to execute its code


# Function with parameters and with no return value
def add(a,b): # Defining a function named 'add' that takes two parameters
    print("The sum is:", a + b) # Function body that prints the sum of the two parameters
add(3, 5)  # Calling the function with arguments 3 and 5

# Function with parameters and with return value

def multiply(x,y): # Defining a function named 'multiply' that takes two parameters
    return x * y  # Function body that returns the product of the two parameters

result = multiply(4, 6)  # Calling the function with arguments 4 and 6
print("The product is:", result)  # Printing the returned value

print(multiply(7, 8))  # Directly printing the returned value from the function call