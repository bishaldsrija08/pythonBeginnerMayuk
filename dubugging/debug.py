

enput('Debugging module loaded') # syntax error intentional for testing purposes



# Run time error example

def divide(a,b):
    return a / b

result = divide(10, 0)  # This will raise a ZeroDivisionError
print('Result:', result)


# Logical error example
def calculate_area(length, width):
    return length + width  # Logical error: should be length * width

area = calculate_area(5, 10)
print('Area:', area)  # Incorrect output due to logical error