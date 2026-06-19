# ouput the shoe size
Shoes = {
    "brand" : "Nick",
    "color" : "black",
    "size" : 40 
    }
print(Shoes["size"])

#change value from Nick to Adidas
Shoes["brand"] = "Adidas"
print(Shoes["brand"])

# add a new key and value to the dictionary(type: sneakers)
Shoes["type"] = "sneakers"
print(Shoes["type"])

# return all the keys in the dictionary
print(Shoes.keys())

# return all the values in the dictionary
print(Shoes.values())

# check if the key "size" is in the dictionary
print("size" in Shoes)

# Loop through the dictionary.
for key, value in Shoes.items():
    print(key, value)
    
# remove color from the dictionary
del Shoes["color"]
print(Shoes)

#empty the dictionary above
Shoes.clear()
print(Shoes)

# create a dictionary and make a copy of it.
Clothes = {
    "brand" : "Zara",
    "color" : "white",
    "size" : "M"
    }
Clothes_copy = Clothes.copy()
print(Clothes_copy)

# show nested dictionaries.
Nested_dict = {
    "person1" : {
        "name" : "Alice",
        "age" : 30
    },
    "person2" : {
        "name" : "Bob",
        "age" : 25
    }
}
print(Nested_dict)