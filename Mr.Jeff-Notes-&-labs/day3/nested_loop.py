#what's a nested loop?
#A nested loop is a loop inside another loop.
# The inner loop will be executed one time for each iteration of the outer loop.

#Example of a nested loop
# for i in range(1, 4): #outer loop
#     for j in range(1, 4): #inner loop
#         print(f"Outer loop iteration: {i}, Inner loop iteration: {j}")
        
        
#write a loop that produces this pattern:
#1
#12
#123
#1234
#12345

for i in range(1, 6): #outer loop
    for j in range(1, i + 1): #inner loop
        print(j, end='') #print j without a newline
    print() #print a newline after the inner loop is done
        