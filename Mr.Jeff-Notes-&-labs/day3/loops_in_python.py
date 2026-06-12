#What are loops?
#Loops are used to repeat a block of code multiple times. In Python, there are two main types of loops: for loops and while loops.
#For loops are used to iterate over a sequence (like a list, tuple, or string) or other iterable objects. The syntax for a for loop is:
# for variable in iterable:
#     # code to execute
#While loops are used to repeat a block of code as long as a certain condition is true. The syntax for a while loop is: 
# while condition:
#     # code to execute

#why use loops?
#Loops are useful for performing repetitive tasks without having to write the same code multiple times. They can help make your code more efficient and easier to read. For example, if you want to print "Hello" five times, you could write the code without using loops, but it would be repetitive
#example without using loops
print("Hello")
print("Hello")
print("Hello")
print("Hello")
print("Hello")

#example using a for loop
for i in range(5):
    print("Hello")
    
#example using a while loop
count = 0
while count < 5:
    print("Hello")
    count += 1
    
    
#couunting from 1 to 10 using a for loop
for i in range(1, 11):
    print(i)