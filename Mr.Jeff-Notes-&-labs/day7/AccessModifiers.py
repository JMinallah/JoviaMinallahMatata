# What are access modifiers in Python?
# These are the keywords that are used to define the accessibility of a class, method, or attribute.
# These are;
# 1. Public -- accessed from anywhere(Symbol: no underscore)
# 2. Protected -- accessed within the class and its subclasses(Symbol: single underscore)
# 3. Private -- accessed within the class only(Symbol: double underscore)

# example of public, private and protected access modifiers in Python
class MyClass:
    def __init__(self):
        self.public_var = "I am a public variable"
        self._protected_var = "I am a protected variable"
        self.__private_var = "I am a private variable"
    def public_method(self):
        return "I am a public method"
    def _protected_method(self):
        return "I am a protected method"
    def __private_method(self):
        return "I am a private method"
    
obj = MyClass()
print(obj.public_var) # I am a public variable
print(obj.public_method()) # I am a public method

# Accessing protected members
print(obj._protected_var) # I am a protected variable
print(obj._protected_method()) # I am a protected method

# Accessing private members
print(obj.__private_var)  # AttributeError: 'MyClass' object has no attribute '__private_var' when accessed directly
print(obj.__private_method()) # AttributeError: 'MyClass' object has no attribute '__private_method' when accessed directly

