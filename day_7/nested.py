"""
*
* *
* * *
* * * *
* * * * *
"""

lines = 5
for i in range(1, lines+1): # outer loop for number of lines
    for j in range(1, i+1): # inner loop for printing stars
        print("*", end=" ")
    print()
    
"""
* * * * *
* * * *
* * *
* *
*
"""

lines = 5
for i in range(lines, 0, -1): # outer loop for number of lines
    for j in range(1, i+1): # inner loop for printing stars
        print("*", end=" ")
    print() # move to the next line
    
"""
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
"""

lines = 5
for i in range(1, lines+1):
    for j in range(1, i+1):
        print(j, end=" ")
    print()


"""
5 4 3 2 1
5 4 3 2 
5 4 3
5 4
5
"""

lines = 5
for i in range( lines, 0, -1):
    for j in range (lines, lines-i, -1):
        print(j, end= " ")
    print()
    
"""
1 2 3 4 5
1 2 3 4
1 2 3
1 2
1
"""

lines = 5
for i in range(lines, 0, -1):
    for j in range(1, i+1):
        print(j, end=" ")
    print()

"""
1
2 3
4 5 6
7 8 9 10
11 12 13 14 15
"""

lines = 5
count = 1
for i in range(1, lines+1):
    for j in range(1, i+1):
        print(count, end= " ")
        count = count+1
    print()

"""
* * * * *
*       *
*       *
* * * * *
"""

lines= 4

for i in range(1, lines+1):
    for j in range(1, lines+1):
        if i==1 or i==lines or j==1 or j==lines: # condition for border stars [logic is : first row, last row, first column, last column]
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()