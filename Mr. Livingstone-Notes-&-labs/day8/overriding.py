# what's overriding?
# overriding is when a subclass provides a specific implementation of a method that is already defined in its superclass. 
# This allows the subclass to modify or extend the behavior of the inherited method.
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
    
# usage
dog = Dog("Buddy")
print(dog.name)  # Output: Buddy
print(dog.speak())  # Output: Woof! (overridden method)