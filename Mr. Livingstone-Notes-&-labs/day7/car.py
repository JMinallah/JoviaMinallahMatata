class Car:
    def __init__(self, brand, year):   # initializing the attributes of the Car class
        self.brand = brand 
        self.year = year
        
    def print_details(self):
        print("Car Details")
        print(f"Brand: {self.brand}")
        print(f"Year: {self.year}")
        print("\n")
# creating objects of the Car class   
car1 = Car("Toyota", 2020)
car2 = Car("Honda", 2021)
# printing the details of the cars objects
car1.print_details()
car2.print_details()