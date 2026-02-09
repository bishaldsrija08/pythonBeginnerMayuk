fruits = ["apple", "banana", "cherry", "kiwi", "mango", "orange", "strawberry", "watermelon"]
newlist = []

for x in fruits:
    if "a" in x or "i" in x:
        newlist.append(x)
print(newlist)