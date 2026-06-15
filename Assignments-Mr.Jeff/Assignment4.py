# Create a menu-driven(GUI) calculator using functions for addition, subtraction, multiplication, and division.
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Division by zero is not allowed."
    return x / y

# Create a simple text-based menu for the calculator
def calculator():
    while True:
        print("\nSimple Calculator")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '5':
            print("Exiting the calculator. Goodbye!")
            break

        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print(f"The result of addition is: {add(num1, num2)}")
        elif choice == '2':
            print(f"The result of subtraction is: {subtract(num1, num2)}")
        elif choice == '3':
            print(f"The result of multiplication is: {multiply(num1, num2)}")
        elif choice == '4':
            print(f"The result of division is: {divide(num1, num2)}")
        else:
            print("Invalid input. Please enter a number between 1 and 5.")