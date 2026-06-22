# Data Hiding in Python
# In Python, data hiding is achieved through the use of name mangling. 
# This is done by prefixing an attribute with double underscores (__). 
# This makes the attribute private and prevents it from being accessed directly from outside the class.
class MyClass:
    def __init__(self, value):
        self.__hidden_value = value  # This is a private attribute

    def get_hidden_value(self):
        return self.__hidden_value  # This method allows access to the hidden value
# Example usage
obj = MyClass(42)
print(obj.get_hidden_value())  # Output: 42
# Attempting to access the hidden value directly will result in an AttributeError

