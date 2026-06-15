# Tuples are immutable sequences, typically used to store collections of heterogeneous data. 
# Tuples are defined by enclosing the elements in parentheses `()`.

# Example of a tuple
person = ("John", 30, "Engineer")
print(person)
print(type(person))

# Conversion of list to tuple
my_list = [1, 2, 3, 4, 5]
my_tuple = tuple(my_list)
print(my_tuple)

# Accessing tuple elements
print(person[0])  # Output: John
print(person[1])  # Output: 30
print(person[2])  # Output: Engineer

# Tuples are immutable, so we cannot change their elements after creation.
# However, we can concatenate tuples to create a new tuple.
new_person = person + ("USA",)
print(new_person)

# Tuples can also be unpacked into variables
name, age, profession = person
print(name)       # Output: John
print(age)        # Output: 30
print(profession) # Output: Engineer

# Delete a tuple
del person
# print(person) # This will raise an error since the tuple has been deleted.

# Updating a tuple using a list
person_list = list(person)
person_list[1] = 31  # Update the age
person = tuple(person_list)
print(person)