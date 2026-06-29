# numpy arrays are collections of items of the same data type.
# they are commonly created from python lists or tuples.

# creating a numpy array from a python list
# array = np.array([1,2,3,4,5])

import numpy as np
# one dimensional array from list
array1 = np.array([1,2,3,4,5])
print(array1)

# two dimensional array from list of lists
array2 = np.array([[1,2,3],[4,5,6]])
print(array2)

# one dimensional array from tuple
array3 = np.array((1,2,3,4,5))
print(array3)

# two dimensional array from tuple of tuples
array4 = np.array(((1,2,3),(4,5,6)))
print(array4)