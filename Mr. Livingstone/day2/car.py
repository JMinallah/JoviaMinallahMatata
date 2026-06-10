# cars = ["bMw", "AuDi","toyota", "subaru"]

# for car in cars:
#     if (car.lower() == "audi"): #lower() converts to lower case hence true
#         print(car.upper())
#     elif (car == "bmw"):     # false because == is case sensitive
#         print(car.upper())
#     else:
#         print(car.title())
        
#!= ....inequality check
fruits = ["apple", "banana","", "banana", "Banana"]

# for fruit in fruits:    # case sensitive
#     if fruit != "banana":
#         print(fruit.title())
#     else:
#         print("I don't like bananas!")

# for fruit in fruits:    # case sensitive
#     if fruit:
#         print(fruit.title())
        
# age = int(input("Enter your age: "))
# gender = input("Enter your gender (male/female): ").lower()

# if age >= 18 and gender == "male":
#     print("You are eligible for the military service.")
# else:
#     print("You are not eligible for the military service.")

# requested_toppings = ["mushrooms", "extra cheese", "pepperoni"]
# print("mushrooms" in requested_toppings)  # True
# print("olives" in requested_toppings)     # False
# print("extra cheese" not in requested_toppings) # False

print(bool(()))
print(bool({}))
print(bool(""))

A = 10
B = 20
print(A == B)