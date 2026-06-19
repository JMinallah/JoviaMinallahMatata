# What are lambda functions?
# These are anonymous functions that can have any number of arguments but only one expression. 
# The expression is evaluated and returned when the function is called.
# Syntax: lambda arguments: expression

# Traditional function definition
def add(x, y):
    return x + y
print(add(5, 3))  # Output: 8

# Lambda function definition
add_lambda = lambda x,y: x + y
print(add_lambda(5, 3))  # Output: 8

# Ex1: Write a lambda function that checks if a number is even
is_even = lambda x: x % 2 == 0
print(is_even(4))  # Output: True

# Practical application of lambda functions with filter() to filter out even numbers from a list
numbers = [1, 2, 3, 4, 5, 26]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  # Output: [2, 4, 26]

# using filter to get numbers greater than 20
greater_than_20 = list(filter(lambda x: x > 20, numbers))
print(greater_than_20)  # Output: [26]

# Ex2: Write a lambda function that uses sorted(), arrange using the length of the words.
words = ["apple", "banana", "kiwi", "grape", "orange"]
sorted_words = sorted(words, key=lambda x: len(x))
print(sorted_words)  # Output: ['kiwi', 'grape', 'apple', 'banana', 'orange']

# Explain the above code
# The sorted function takes a list of words and sorts them based on the length of each word. 
# The key parameter is set to a lambda function that takes each word (x) and returns its length (len(x)). 
# This allows the sorted function to sort the words in ascending order based on their length.
# The arguments for the sorted function are the list of words and the key parameter, which is set to the lambda function.
# is the order of the sorted() function arguments important? 
# Yes, the order of the arguments is important. The first argument is the iterable to be sorted, and the second argument is the key function that determines the sorting criteria. 
# If the order is changed, it may lead to unexpected results or errors.
