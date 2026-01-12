# Loops => Repetition structures in programming

""" 
initial value, condition, increment/decrement

hello world for 100000 time

initialize = 1
final value = 100000
increase by 1
"""

# for loop syntax => for variable in range(initial value, final value, increment/decrement):

#  WAP to print hello world 1000 times
for i in range(1, 11, 1):
    print("Hello World", i)
    

# WAP to print numbers from 1 to 100
for i in range(1, 101, 1):
    print(i, end=" ")
    
# WAP to print from 100 to 1

for i in range(100, 0, -1):
    print(i, end=" ")
    
# WAP to print even numbers from 1 to 100

for i in range(2, 101, 2):
    print(i, end=" ")

# WAP to print odd numbers from 1 to 100
for i in range (1, 101, 2):
    print(i, end=" ")

# WAP to print multiplication table of 5
for i in range (1, 11, 1):
    print(f"5x{i}={5*i}")

# WAP to print multiplication table of user input number
num = int(input("Enter a number to print its multiplication table: "))

for i in range(1, 11,1):
    print(f"{num}x{i} = {num*i}")
    

# WAP to print sum of first 10 natural numbers
# 1+2+3+4+5+6+7+8+9+10 = 55

sum = 0
for i in range (1, 11,1):
    sum = sum + i
print("Sum of first 10 natural numbers is:", sum)