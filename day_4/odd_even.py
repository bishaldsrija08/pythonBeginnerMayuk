"""The modulo operator (%) in Python is used to find the remainder after dividing one number by another. It works with both integers and floating-point numbers and is commonly used in tasks like checking even or odd numbers, repeating patterns, and calculations based on cycles. For Example: 10 % 3 = 1"""

# WAP to check if a number is odd or even
n = int(input("Enter a number: "))

if n % 2 ==0:
    print(f"{n} is an Even number.")
else:
    print(f"{n} is an Odd number.")
