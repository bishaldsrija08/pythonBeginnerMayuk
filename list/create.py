

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango", "apple", "banana"]
# thislist = list(("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango", "apple", "banana"))


print(thislist)

# Type
print(type(thislist))

# length
print(len(thislist))

# Access items
print(thislist[0])
print(thislist[1])
print(thislist[2])


# Negative Indexing
print(thislist[-1])

# Range of Indexes
print(thislist[2:5])

# Range of Negative Indexes
print(thislist[-4:-1])

# Check if Item Exists
if "apple" in thislist:
    print("Yes, 'apple' is in the fruits list")

# loop through a list
for x in thislist:
    print(x)

print(thislist[:4])
print(thislist[2:])