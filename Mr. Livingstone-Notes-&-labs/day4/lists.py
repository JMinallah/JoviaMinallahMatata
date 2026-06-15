# Lists are a type of data structure that can hold multiple values. 
# They are ordered, mutable, and can contain duplicate values.
# Example of a list
fruits = ["apple", "banana", "cherry", "date", "apple"]
print(fruits)
print(type(fruits))

# Accessing list items
print(fruits[0]) #output: apple
print(fruits[1]) #output: banana
print(fruits[-1]) #output: apple

# Adding items to a list
fruits.append("elderberry") #adding item at the end of the list
print(fruits)
fruits.insert(1, "blueberry") #adding item at a specific index
print(fruits)

# Removing items from a list
fruits.remove("banana") #removing item by value
print(fruits)
fruits.pop(2) #removing item by index   
print(fruits)

# Updating items in a list
fruits[0] = "avocado" #updating item at index 0
print(fruits)  

# Slicing a list
print(fruits[1:4]) #output: ['blueberry', 'cherry', 'date']
print(fruits[:3]) #output: ['avocado', 'blueberry', 'cherry']
print(fruits[3:]) #output: ['date', 'elderberry']

# Using a constructor to create a list
numbers = list((1, 2, 3, 4, 5)) #creating a list from a tuple
print(numbers)

#iterating through lists using loops
for number in numbers:
    print(number)
    
# Nested lists
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(matrix)
print(matrix[0]) #output: [1, 2, 3]
print(matrix[1][2]) #output: 6
#accessing nested list items using loops
for row in matrix:
    for item in row:
        print(item)