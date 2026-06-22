# What is abstraction in python?
# Abstraction is a concept that allows us to hide the internal implementation details of a class and only expose the necessary functionalities to the user. 
# It helps in reducing complexity and increasing efficiency by providing a clear interface for interacting with objects.
# Example of application of abstraction:

from abc import ABC, abstractmethod
class Vehicle(ABC):  #  ABC is a built-in module in Python that provides the infrastructure for defining abstract base classes.
    @abstractmethod
    def start_engine(self):
        pass

    @abstractmethod
    def stop_engine(self):
        pass
# steps for creating an abstract class:
# 1. Import the ABC module from the abc library.
# 2. Create a class that inherits from ABC.
# 3. Use the @abstractmethod decorator to define abstract methods in the class.
# 4. Implement the abstract methods in the subclasses that inherit from the abstract class.