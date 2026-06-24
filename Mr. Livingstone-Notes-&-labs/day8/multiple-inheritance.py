# How is multiple inheritance implemented in Python?
# Multiple inheritance is a feature in Python that allows a class to inherit attributes and methods from more than one parent class. 
# This is achieved by specifying multiple parent classes in the class definition, separated by commas.
# For example,
class Parent1:
    def method1(self):
        return "Method from Parent1"

class Parent2:
    def method2(self):
        return "Method from Parent2"

class Child(Parent1, Parent2):  # Child inherits from both Parent1 and Parent2
    def method3(self):
        return "Method from Child"
    
# Problems of multiple inheritance:
# 1. Diamond Problem: When two parent classes have a method with the same name,
#    and the child class inherits from both, it can lead to ambiguity about which method to call. 
#    Python uses the Method Resolution Order (MRO) to determine the order in which classes are searched for a method. 
#    The MRO follows the C3 linearization algorithm, which ensures a consistent order of method resolution.
#  Linearizaation means that the order of method resolution is determined by the order in which classes are defined and the inheritance hierarchy.
# for instance:
class Parent:
    def method(self):
        return "Method from Parent"

class Class1(Parent):
    def method(self):
        return "Method from Class1"
    
class Class2(Parent):
    def method(self):
        return "Method from Class2"
    
class Child(Class1, Class2):
    child = Child()
    child.method()  # This will call the method from Class1 due to MRO
