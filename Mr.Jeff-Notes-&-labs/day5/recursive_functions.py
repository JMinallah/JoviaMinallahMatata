# What is recursion and a recursive function?
# Recursion is a programming technique where a function calls itself in order to solve a problem.
# A recursive function is a function that calls itself in order to solve a problem.
# The concept of recursion is based on the idea of breaking down a problem into smaller, more manageable parts until a base case is reached.
# Components of recursive function:
# 1. Base case: This is the condition under which the recursion will stop. It prevents infinite recursion and ensures that the function eventually returns a result.
# 2. Recursive case: This is the part of the function where the function calls itself with modified arguments, moving towards the base case.

# Ex1: Write a recursive function to calculate the factorial of a number.
# 5! = 5 * 4 * 3 * 2 * 1 = 120
def factorial(n):
    if n == 0 or n == 1:
        return 1   # base case: factorial of 0 or 1 is 1
    else:
        return n * factorial(n-1)   #recursive case: n! = n * (n-1)!
    
# counting down numbers using recursion
def countdown(n):
    if n <= 0:
        print("Blast off!")  # base case: when n is 0 or negative, stop recursion
    else:
        print(n)  # print the current number
        countdown(n - 1)  # recursive case: call countdown with n-1
        
# Ex2: Write a recursive function to calculate the nth Fibonacci number.
# What is the Fibonacci sequence?
# The Fibonacci sequence is a series of numbers where each number is the sum of the two preceding ones, usually starting with 0 and 1. 
# The sequence goes: 0, 1, 1, 2, 3, 5, 8, 13, 21, and so on.
def fibonacci(n):
    if n <= 0:
        return 0  # base case: the 0th Fibonacci number is 0
    elif n == 1:
        return 1  # base case: the 1st Fibonacci number is 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)  # recursive case: F(n) = F(n-1) + F(n-2)

# printing the first 10 Fibonacci numbers using recursion
for i in range(10):
    print(fibonacci(i))  # Output: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34
    
# Importance of fibonacci sequence in computer science
# The Fibonacci sequence has several important applications in computer science, including:
# 1. Algorithm design: The Fibonacci sequence is often used in algorithm design and analysis,

# Binary searcch using recursion
def binary_search(arr, target, low, high):
    if low > high:
        return -1  # base case: target not found
    mid = (low + high) // 2
    if arr[mid] == target:
        return mid  # base case: target found
    elif arr[mid] < target:
        return binary_search(arr, target, mid + 1, high)  # recursive case: search in the right half
    else:
        return binary_search(arr, target, low, mid - 1)  # recursive case: search in the left half 
# using the above code
arr = [1, 3, 5, 7, 9, 11, 13, 15]
target = 7
result = binary_search(arr, target, 0, len(arr) - 1)
print(result)  # Output: 3 (index of the target element)