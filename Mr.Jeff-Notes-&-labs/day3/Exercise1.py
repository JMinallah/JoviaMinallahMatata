#Exercise
#write a program that uses a while loop to demonstrate a bank accoutn balance.
#The program should allow a user to deposit and withdraw money until the balance is zero.

balance = 1000  # initial balance

while balance > 0:
    print("Current balance:", balance)
    action = input("Do you want to deposit or withdraw? (d/w): ")
    
    if action == 'd':
        amount = float(input("Enter the amount to deposit: "))
        balance += amount
        print("You deposited:", amount)
        
    elif action == 'w':
        amount = float(input("Enter the amount to withdraw: "))
        if amount > balance:
            print("Insufficient funds. You cannot withdraw more than your current balance.")
        else:
            balance -= amount
            print("You withdrew:", amount)
            
    else:
        print("Invalid action. Please enter 'd' for deposit or 'w' for withdraw.")