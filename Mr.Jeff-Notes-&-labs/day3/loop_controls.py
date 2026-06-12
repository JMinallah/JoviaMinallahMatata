#what are loop controls?
#Loop controls are statements that can change the flow of a loop.
#There are three loop control statements in Python: break, continue, and pass.
#break statement is used to exit a loop prematurely.
#continue statement is used to skip the current iteration of a loop and move to the next iteration.
#pass statement is used as a placeholder for code that will be written later.

#example with break statement
for i in range(1, 10):
    if i == 5:
        break #exit the loop when i is 5
    print(i)

#example with continue statement
for i in range(1, 10):
    if i == 5:
        continue #skip the rest of the loop when i is 5
    print(i)

#example with pass statement
for i in range(1, 10):
    if i == 5:
        pass #do nothing when i is 5
    print(i)