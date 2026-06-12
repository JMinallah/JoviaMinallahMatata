#Write a program for Login Authentication that takes a username and password as input and checks if they match the predefined credentials. If they match, print "Login successful", if the username is correct but the password is wrong, print "Invalid password", and if the username is incorrect, print "Username not found".
#predefined credentials
predefined_username = "admin"
predefined_password = "password123" 

#taking input from the user
username = input("Enter your username: ")
password = input("Enter your password: ")

#checking the credentials
if username == predefined_username:
    if password == predefined_password:
        print("Login successful")
    else:
        print("Invalid password")
else:
    print("Username not found")