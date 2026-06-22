# user class
class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        
# how can i create attributes that don't go in the init block or directly not into a function?
#You can create attributes outside of the `__init__` method by defining them directly in the class body. 
# These attributes will be shared across all instances of the class. Here's an example:
# do i have initialize the outside attributes when creating them in the class body?
# No, you don't have to initialize the attributes when creating them in the class body.

    # user profile attributes
    email = ""
    age = 0
    location = ""
    
    # describe user method
    def describe_user(self):
        print(f"User: {self.first_name} {self.last_name}")
        print(f"Email: {self.email}")
        print(f"Age: {self.age}")
        print(f"Location: {self.location}")
        print("\n")
        
    # greet user method
    def greet_user(self):
        print(f"Hello, {self.first_name} {self.last_name}! Welcome back.")
        
# several instances of the User class
# user1
user1 = User("John", "Doe")
user1.email = "john.doe@example.com"
user1.age = 30
user1.location = "New York"
user1.greet_user()
user1.describe_user()
# user2
user2 = User("Jane", "Smith")
user2.email = "jane.smith@example.com"
user2.age = 25
user2.location = "Los Angeles"
user2.greet_user()
user2.describe_user()

