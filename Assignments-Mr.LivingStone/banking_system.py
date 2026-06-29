# parent account class
class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance
        
    # deposit method
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}. New balance is {self.balance}.")
        else:
            print("Deposit amount must be positive.")
            
    # withdraw method
    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance is {self.balance}.")
        else:
            print("Invalid withdrawal amount.")
# child savings account class
class SavingsAccount(BankAccount):
    def __init__(self, account_number, balance, interest_rate):
        super().__init__(account_number, balance)
        self.interest_rate = interest_rate
        
    # method to override withdraw method to follow savings account rules like interest rate
    def withdraw(self, amount):
        #calculate interest before withdrawal
        interest = self.balance * self.interest_rate
        self.balance += interest
        #call parent withdraw method
        super().withdraw(amount)
    
# child class current account class
class CurrentAccount(BankAccount):
    def __init__(self, account_number, balance, overdraft_limit):
        super().__init__(account_number, balance)
        self.overdraft_limit = overdraft_limit
        
    # method to override withdraw method to allow overdraft
    def withdraw(self, amount):
        if amount > 0 and (self.balance - amount) >= -self.overdraft_limit:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance is {self.balance}.")
        else:
            print("Invalid withdrawal amount or overdraft limit exceeded.")
            
# functionality
def main():
    # create a savings account
    savings_account = SavingsAccount("SA123", 1000, 0.05)
    savings_account.deposit(500)
    savings_account.withdraw(200)
    
    # create a current account
    current_account = CurrentAccount("CA456", 2000, 500)
    current_account.deposit(1000)
    current_account.withdraw(2500)  # should be allowed due to overdraft
    current_account.withdraw(3000)  # should not be allowed due to overdraft limit

if __name__ == "__main__":
    main()