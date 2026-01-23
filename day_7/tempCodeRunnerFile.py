lines= 4

for i in range(1, lines+1):
    for j in range(1, lines+1):
        if i==1 or i==lines or j==1 or j==lines:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()