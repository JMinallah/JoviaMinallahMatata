# Short summaries on inheritance in python plus examples
# Inheritance is a fundamental concept in object-oriented programming (OOP) that allows a class (called a child or subclass) to inherit attributes and methods from another class (called a parent or superclass). 
# This promotes code reusability and establishes a hierarchical relationship between classes.
# For example,
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "Some sound"
    
# child class
class Dog(Animal): # Dog inherits from Animal
    def speak(self):
        return "Woof!"