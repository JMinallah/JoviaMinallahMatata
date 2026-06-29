# parent class vehicle
class Vehicle:
    def __init__(self, registration_number, renta_price):
        self.registration_number = registration_number
        self.rental_price = renta_price
        
    # method to calculate rental cost
    def calculate_rental_cost(self, days):
        return self.rental_price * days
    
    # method to display vehicle information
    def display_info(self):
        print(f"Registration Number: {self.registration_number}")
        print(f"Rental Price: {self.rental_price}")
        
# child class car
class Car(Vehicle):
    def __init__(self, registration_number, rental_price, sitting_capacity):
        super().__init__(registration_number, rental_price)
        self.sitting_capacity = sitting_capacity
    
    # overriding the display_info method to include sitting capacity
    def display_info(self):
        super().display_info()
        print(f"Sitting Capacity: {self.sitting_capacity}")
        
    
# child class motorcycle
class Motorcycle(Vehicle):
    def __init__(self, registration_number, rental_price, engine_capacity):
        super().__init__(registration_number, rental_price)
        self.engine_capacity = engine_capacity
    
    # overriding the display_info method to include engine capacity    
    def display_info(self):
        super().display_info()
        print(f"Engine Capacity: {self.engine_capacity}")
       
# functionality for for the vehicle rental company
def main():
    # creating instances of Car and Motorcycle
    car1 = Car("ABC123", 50, 5)
    motorcycle1 = Motorcycle("XYZ789", 30, 150)
    
    # displaying information for car1
    print("Car Information:")
    car1.display_info()
    print(f"Rental Cost for 3 days: {car1.calculate_rental_cost(3)}\n")
    
    # displaying information for motorcycle1
    print("Motorcycle Information:")
    motorcycle1.display_info()
    print(f"Rental Cost for 2 days: {motorcycle1.calculate_rental_cost(2)}\n")