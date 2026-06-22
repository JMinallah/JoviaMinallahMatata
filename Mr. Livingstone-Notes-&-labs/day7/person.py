# Create a class Person with attributes name, age, and gender
class Person:
    # Initialize the attributes of the Person class using the __init__() method
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
        
# Create an object of the Person class
person1 = Person("John Doe", 30, "Male")
print(person1.name)  # Output: John Doe
