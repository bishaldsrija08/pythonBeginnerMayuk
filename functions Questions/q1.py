# 1. Write a program that takes an integer as input and prints whether it is positive, negative, or zero.

def check(num):
    if num>0:
        return "Positive"
    elif num<0:
        return "Negative"
    else:
        return "Zero"

number = int(input("Enter an integer: "))
result = check(number)
print(f"The number is {result}.")