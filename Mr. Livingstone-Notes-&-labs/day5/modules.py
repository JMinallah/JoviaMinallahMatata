# What are modules?
# Modules are used to organize code into reusable files.

# Inbuilt and external modules
# Inbuilt modules are those that come with Python, such as math, random, and datetime.
# External modules are those that are not included with Python and need to be installed, such as NumPy, Pandas, and Matplotlib.
# Why use modules?
# Modules help to organize code into reusable files, making it easier to maintain and read.
# They also allow us to use code that has already been written by others, saving time and effort.
# Write less, do more.
# Boost productivity.

# Importing modules
# To use a module, we need to import it. We can import a module using the import statement.
# For example, to import the math module, we can use the following code:

# Inbuilt
import math
pie = math.pi
print("The value of pi is: ", pie)

# External
# Steps
# 1. First iinstall the external module using pip, e.g pip install numpy
# 2. Then import the module in your code using the import statement, e.g import numpy as np
# 3. Now you can use the functions and classes provided by the module in your code, e.g np.array([1, 2, 3])

import pandas
# Dataframe example
data = {"Name": ["John", "Jane", "Doe"], 
        "Age": [30, 25, 35]}

print(data)

df = pandas.DataFrame(data)
print(df)

# Importing specific functions from a module
# Example
from math import sqrt
print("The square root of 16 is: ", sqrt(16))

# Importing modules with an alias
# Example
import numpy as np
arr = np.array([1, 2, 3])
print(arr)

# Importing everything from a module
# Example
from math import *

