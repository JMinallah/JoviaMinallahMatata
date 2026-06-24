# What is polymorphism in python?
# Polymorphism in Python refers to the ability of different objects to be treated as instances of the same class through a common interface. 
# It allows methods to do different things based on the object it is acting upon, even if they share the same name. 
# This is achieved through method overriding and operator overloading.

# What is method overriding?
# method overriding is where a subclass provides a specific implementation of a method that is already defined in its superclass.

# What is method overloading?
# Method overloading is a feature that allows a class to have more than one method with the same name, but with different parameters. 
# However, Python does not support method overloading in the traditional sense.
# Overloading can be achieved in Python by using default arguments or variable-length arguments.

# Approach 1: Method Overriding
class Animal:
    def sound(self):
        return "Some generic animal sound"

class Dog(Animal):
    def sound(self):
        return "Bark"

class Cat(Animal):
    def sound(self):
        return "Meow"

# Approach 2: Operator Overloading
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f"Point({self.x}, {self.y})"
    
# Example usage
if __name__ == "__main__":
    # Method Overriding Example
    animals = [Dog(), Cat(), Animal()]
    for animal in animals:
        print(animal.sound())

    # Operator Overloading Example
    p1 = Point(1, 2)
    p2 = Point(3, 4)
    p3 = p1 + p2
    print(p3)  # Output: Point(4, 6)
    
# Approach 3: Type checking and duck typing
def add(a, b):
    return a + b

# Example usage
if __name__ == "__main__":
    print(add(5, 10))          # Output: 15 (int)
    print(add("Hello, ", "World!"))  # Output: Hello, World! (str)
    print(add([1, 2], [3, 4])) # Output: [1, 2, 3, 4] (list)