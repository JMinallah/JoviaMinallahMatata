#Control Structures in Python
#Control structures are used to control the flow of a program. They allow you to make decisions and repeat blocks of code based on certain conditions. The main control structures in Python are if statements, for loops, and while loops.

#if statements
#what are if statements?
#If statements are used to make decisions in a program. They allow you to execute a block of code only if a certain condition is true. The syntax for an if statement is:
# if condition:
#     # code to execute 

#example of an if statement
age = int(input("Enter your age: "))
if age >= 18:
    print("You are an adult.")
    
#else statements
#Else statements are used to execute a block of code if the condition in the if statement is false. The syntax for an else statement is:
# if condition:    
#     # code to execute
# else:
#     # code to execute

#example of an if-else statement
age = int(input("Enter your age: "))
if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")
    
#elif statements
#Elif statements are used to check multiple conditions in an if statement. They allow you to execute different blocks of code based on different conditions. The syntax for an elif statement is:
# if condition1:
#     # code to execute
# elif condition2:
#     # code to execute
# else:
#     # code to execute

#example of an if-elif-else statement
age = int(input("Enter your age: "))
if age < 0: 
    print("Invalid age.")
elif age < 18:
    print("You are a minor.")
elif age < 65:
    print("You are an adult.")
else:
    print("You are a senior citizen.")
    

#Lab1Exercise1
# A program that takes in a number and checks if it's positive, negative or a zero
number = float(input("Enter a number: "))
if number > 0:
    print("The number is positive.")
elif number < 0:
    print("The number is negative.")
else:
    print("The number is zero.")
    
#LabExercise2
#Grading system
score = float(input("Enter your score: "))
if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")
else:
    print("Grade: F")