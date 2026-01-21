lines = 5
for i in range( lines, 0, -1):
    for j in range (lines, lines-i, -1):
        print(j, end= " ")
    print()