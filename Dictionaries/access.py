perosn ={
    "name": "Mayuk",
    "age": 22,
    "coutntry": "India",
    "is_married": False,
    "interest": ["coding", "music", "traveling", "music"],
    "name1": "Bishal"
}
# Accessing values from the dictionary
print(perosn["name"])
print(perosn["age"])

print(perosn.get("coutntry"))

print(perosn.keys())
print(perosn.values())

print(perosn.items())

if "name" in perosn:
    print("Name is present in the dictionary")