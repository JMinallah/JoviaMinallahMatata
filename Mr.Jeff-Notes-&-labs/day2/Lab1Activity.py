#match statement is a new feature in Python 3.10 that allows you to match patterns in data structures. It is similar to switch statements in other programming languages. The syntax for a match statement is:
#works like a switch statement in other languages, but it is more powerful and flexible. It can match patterns in data structures, not just simple values. The syntax for a match statement is:
# match variable:
#     case pattern1:
#         # code to execute if pattern1 matches
#     case pattern2:
#         # code to execute if pattern2 matches
#     case _:
#         # code to execute if no pattern matches

#for example, let's say we want to write a program that takes a number corresponding to a day of the week and prints the name of the day. We can use a match statement to do this:
num = int(input("Enter a number corresponding to a day of the week (1-7): "))

match num:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 7:
        print("Sunday")
    case _:
        print("Invalid input! Please enter a number between 1 and 7.")