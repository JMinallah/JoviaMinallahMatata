# What is a function?
# A function is a block of code that performs a specific task. 
# It can take inputs, called parameters, and can return an output. 
# Functions help to organize code, make it reusable, and improve readability. 
# In programming, functions are defined using the `def` keyword followed by the function name and parentheses that may include parameters.

# Why use functions?
# 1. Reusability: Functions allow you to write code once and reuse it multiple times, reducing redundancy.
# 2. Modularity: Functions help break down complex problems into smaller, manageable pieces, making the code easier to understand and maintain.
# 3. Readability: Functions provide a clear structure to the code, making it easier for others (and yourself) to read and understand.
# 4. Testing: Functions can be tested independently, which makes it easier to identify and fix bugs in the code.

# Syntax of a function in Python:
# def function_name(parameters):
#     # code block

# Built-in functions in Python:
# Python provides a wide range of built-in functions that can be used without the need for importing any additional libraries. Some common built-in functions include:
# - print(): Outputs text to the console
# - len(): Returns the length of an object (e.g., string, list, tuple)
# - type(): Returns the type of an object

# Components of a function:
# 1. Function Name: A unique identifier for the function that describes its purpose.
# 2. Parameters: Variables that are passed to the function to provide input data.
# 3. Docstring: A string that describes what the function does, its parameters, and its return value. It is enclosed in triple quotes and is optional but recommended for better code documentation.
# 4. Return Statement: A statement that specifies the value to be returned by the function. If a function does not have a return statement, it returns `None` by default.
# 5. Indentation: The code block within the function must be indented to indicate that it belongs to the function.

# Example 1 of a function that takes parameters and returns a value:
def add_numbers(a, b):
    """This function takes two numbers and returns their sum."""
    return a + b

# Lab1: Greeting function
def greet():
    print("Hello! Welcome to the world of Python programming.")

# calling the greet function
greet()

# Lab2: Square function
def square(number):
    result = number * number
    print(f"The square of {number} is {result}.")
    
# calling the square function
square(5)

# Lab3: Function that takes in 2 inputs annd calculates area of a rectangle
def calculate_area():
    length = float(input("Enter the length of the rectangle: "))
    width = float(input("Enter the width of the rectangle: "))
    area = length * width
    print(f"The area of the rectangle with length {length} and width {width} is {area}.")

# calling the calculate_area function
calculate_area()

# PARAMETERS AND ARGUMENTS
# Parameters are variables that are defined in the function definition and are used to accept input values when the function is called. 
# Arguments, on the other hand, are the actual values that are passed to the function when it is called.
# Example of a function with parameters and arguments:
def greet_user(name):
    print(f"Hello, {name}! Welcome to the world of Python programming.")

# calling the greet_user function with an argument
greet_user("Alice")

# Ex2: Function to display student inputs(name, age, student_number)
def display_details(name, age, student_number):
    print(f"Name: {name}")
    print(f"Age: {age}")
    print(f"Student Number: {student_number}")

# calling the display_details function
display_details("Bob", 20, "S12345")

# Positional and Keyword Arguments
# Positional arguments are passed to a function in the order in which they are defined in the function definition. 
# example with positional arguments:
def introduce(name, age):
    print(f"My name is {name} and I am {age} years old.")
    
# Keyword arguments, on the other hand, are passed to a function using the parameter names, 
# allowing you to specify the values for specific parameters regardless of their order in the function definition.
#example with keyword arguments:
def introduce(name, age):
    print(f"My name is {name} and I am {age} years old.")
    
# defailt parameters
# Default parameters are parameters that have a default value assigned to them in the function definition.
# If a value is not provided for a default parameter when the function is called, the default value will be used. 
# This allows you to call the function without providing values for all parameters
# Example of a function with default parameters:
def greet_user(age, name="Guest"):
    print(f"Hello, {name}! You are {age} years old.")
    
#Return statements
# A return statement is used to specify the value that a function should return when it is called.
# When a return statement is executed, the function terminates and the specified value is returned to the caller. 
# If a function does not have a return statement, it returns `None` by default.
# Example of a function with a return statement:
def add_numbers(a, b):
    return a + b

# Multiple return values
# In Python, a function can return multiple values by separating them with commas in the return statement
# Example of a function that returns multiple values:
def calculate(a, b):
    sum_result = a + b
    difference = a - b
    product = a * b
    return sum_result, difference, product
#calling the calculate function and unpacking the returned values
sum_result, difference, product = calculate(10, 5)

# Scope of variables and types of variables
# The scope of a variable refers to the region of the code where the variable is accessible.
# There are two main types of variables in Python: local variables and global variables.
# Local variables are defined within a function and can only be accessed within that function.
# Example of a local variable:
def my_function():
    local_variable = "I am a local variable."
    print(local_variable)   
# Global variables, on the other hand, are defined outside of any function and can be accessed from anywhere in the code.
# Example of a global variable:
global_variable = "I am a global variable."
def my_function():
    print(global_variable)
    
# Ex4: Write a program to demonstrate the use of local and global variables
# Global variable
x = 10
def my_function():
    # Local variable
    y = 5
    print(f"Inside the function: x = {x}, y = {y}")
my_function()
print(f"Outside the function: x = {x}") # y is not accessible here, will raise an error.
# print(f"Outside the function: y = {y}") # This will raise an error because y is a local variable and cannot be accessed outside the function.