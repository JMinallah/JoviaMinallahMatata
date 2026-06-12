#these data structures store data in key-value pairs. They are also called associative arrays or hash maps.
#mutable, unordered, and indexed by keys
#keys must be unique and immutable (strings, numbers, tuples), values can be of any data type and can be duplicated
#dictionaries are defined using curly braces {} with key-value pairs
#example:
my_dict = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}

# print(my_dict["name"])  # Output: Alice
# print(my_dict["age"])   # Output: 30
# print(my_dict["city"])  # Output: New York

b = dict(name="Sarah", age=25)
# print(b)
# # using get method to access values
# print(b.get("age"))

# #adding and updating dictionary items
# b["city"] = "Kampala"  # adding a new key-value pair
# b["age"] = 15   # updating the value of an existing key
# print("==================")
# print("after adding and updating:")
# print(b)

# #removing items from a dictionary
# del my_dict["age"]
# print(my_dict)

# #using pop method to remove an item and return its value
# age = my_dict.pop("city")
# print(age)
# print(my_dict)

#iterating through a dictionary
# for key in b:
#     print(key, b[key])

# print("==================")    
# #using .keys, .values, and .items methods to iterate through a dictionary

# for key in b.keys():
#     print(key)
    
# print("==================")
# for value in b.values():
#     print(value)
    
# print("==================")    
# for key, value in b.items():
#     print(key, value)
    
#nested dictionaries
print("==================")
nested_dict = {
    "person1": {"name": "Alice", "age": 30},
    "person2": {"name": "Bob", "age": 25}
}
print(nested_dict["person1"])  # Output: {'name': 'Alice', 'age': 30}
print(nested_dict["person1"]["name"])  # Output: Alice

#using .items to iterate through a nested dictionary
for person, details in nested_dict.items():
    print(person)
    for key, value in details.items():
        print(f"  {key}: {value}")