# What is inheritance?
# Inheritance is a concept that allows a new class (called a child class or subclass) to inherit attributes and methods from an existing class (called a parent class or superclass). 
# This promotes code reusability and establishes a natural hierarchical relationship between classes.
# For example, if you have a parent class called "Animal" with attributes like "name" and "age", and methods like "speak()", 
# you can create a child class called "Dog" that inherits from "Animal". 
# The "Dog" class will automatically have the attributes and methods of the "Animal" class, and you can also add additional attributes or methods specific to the "Dog" class.

# Example of Inheritance in Python
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        print(f"{self.name} makes a sound.")

class Dog(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age)
        self.breed = breed

    def speak(self):
        print(f"{self.name} barks.")

# Creating instances of the classes
animal = Animal("Generic Animal", 5)
dog = Dog("Buddy", 3, "Golden Retriever")

# Calling methods
animal.speak()
dog.speak()