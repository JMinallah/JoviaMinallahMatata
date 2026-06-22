# using abstraction, create a class Shape with mulitple abstract methods 
# and then create two subclasses Circle and Rectangle that implement these abstract methods.

from abc import ABC, abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass
    
# class Circle that implements the abstract methods of Shape
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

    def perimeter(self):
        return 2 * 3.14 * self.radius
    
# class Rectangle that implements the abstract methods of Shape
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)
    
# creating instances of Circle and Rectangle
circle = Circle(5)
rectangle = Rectangle(4, 6)
# printing area and perimeter of Circle
print("Circle Area:", circle.area())
print("Circle Perimeter:", circle.perimeter())
# printing area and perimeter of Rectangle
print("Rectangle Area:", rectangle.area())
print("Rectangle Perimeter:", rectangle.perimeter())