# Lab 1 Exercise 1: Create a method overloading and overriding the completes a banking system
# The parent class must be Transaction and the child class can be deposit, withdrawal and Transfer.
# Demonstrate an employer dpositing, witdrawing and transfering funds.

class Transaction:
    def __init__(self, amount):
        self.amount = amount
    def process(self):
        pass    
        

class Deposit(Transaction):
    def process(self):
        return f"Deposited: ${self.amount}"


class Withdrawal(Transaction):
    def process(self):
        return f"Withdrew: ${self.amount}"
    
class Transfer(Transaction):
    def __init__(self, amount, recipient):
        super().__init__(amount)
        self.recipient = recipient

    def process(self):
        return f"Transferred: ${self.amount} to {self.recipient}"
    
# Example usage
if __name__ == "__main__":
    deposit = Deposit(100)
    withdrawal = Withdrawal(50)
    transfer = Transfer(200, "John Doe")

    print(deposit.process())      # Output: Deposited: $100
    print(withdrawal.process())   # Output: Withdrew: $50
    print(transfer.process())      # Output: Transferred: $200 to John Doe
