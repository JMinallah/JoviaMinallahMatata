# exercise2, demonstrate the concept of data hiding usinf the mobile monye scenario, with methods, withdraw, deposit, and check balance. The balance should be hidden from direct access.
class MobileMoney:
    def __init__(self, initial_balance=0):
        self.__balance = initial_balance  # This is a private attribute

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited: {amount}. New balance: {self.__balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > 0:
            if self.__balance >= amount:
                self.__balance -= amount
                print(f"Withdrew: {amount}. New balance: {self.__balance}")
            else:
                print("Insufficient balance.")
        else:
            print("Withdrawal amount must be positive.")

    def check_balance(self):
        return self.__balance  # This method allows access to the hidden balance
# Example usage
mobile_money = MobileMoney(100)
mobile_money.deposit(50)  # Deposited: 50. New balance: 150
mobile_money.withdraw(30)  # Withdrew: 30. New balance: 120
print(mobile_money.check_balance())  # Output: 120
# Attempting to access the balance directly will result in an AttributeError
# print(mobile_money.__balance)  # This will raise an AttributeError