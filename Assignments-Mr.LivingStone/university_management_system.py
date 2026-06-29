# parent class of person
class Person:
    def __init__(self, name, ID):
        self.name = name
        self.ID = ID
        
# student class inheriting from person
class Student(Person):
    def __init__(self, name, ID, major):
        super().__init__(name, ID)
        self.major = major
        
# lecturer class inheriting from person
class Lecturer(Person):
    def __init__(self, name, ID, department):
        super().__init__(name, ID)
        self.department = department
        
# main method to demonstrate the functionality
def main():
    # creating a student object
    student1 = Student("Alice", "S123", "Computer Science")
    print(f"Student Name: {student1.name}, ID: {student1.ID}, Major: {student1.major}")