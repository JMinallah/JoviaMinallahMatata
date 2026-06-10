# firstName = input("Enter your first name: ")
# lastName = input("Enter your last name: ")
# city = input("Enter your city of residence: ")
# yearOfBirth = int(input("Enter your year of birth: "))

# currentYear = 2026
# age = currentYear - yearOfBirth
# print(f"Hellooo, {firstName} {lastName} from {city}! You are {age} years old.")


print("Welcome to the Secret Number Game!")
print("You have 3 attempts to guess the secret number")
secret_number = 7
guess = ""
number_of_attempts = 3

while guess != secret_number and number_of_attempts > 0: 
    guess = int(input("Enter your guess: "))
    if guess == secret_number:
        print("Congratulations! You've guessed the secret number!")
    else:
        number_of_attempts -= 1
        if number_of_attempts == 0:
            print("Game over! You've used all your attempts. The secret number was", secret_number)
        else:
            print(f"Wrong guess! You have {number_of_attempts} attempts left.")    
        