# try except

try:
    print(6/0)
except ZeroDivisionError:
    print("You cannot divide by zero!")
finally:    
    print("This will always be executed.")