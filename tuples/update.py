mytuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")


my_list = list(mytuple)
my_list[1] = "blackcurrant"
my_list.append("grape")
my_list.remove("kiwi")
mytuple = tuple(my_list)
print(mytuple)