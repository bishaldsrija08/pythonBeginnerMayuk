perosn ={
    "name": "Mayuk",
    "age": 22,
    "coutntry": "India",
    "is_married": False,
    "interest": ["coding", "music", "traveling", "music"],
    "name1": "Bishal"
}


perosn.pop("name1")
print(perosn)

del perosn["age"]
print(perosn)

perosn.clear()
print(perosn)