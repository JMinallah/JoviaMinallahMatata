# Exercise1: Create a class called car with brand, model and price and then make brand public and a display method to show the details of the car. 
# Make model protected and price private and then try to access them outside the class.
class Car:
    def __init__(self, brand, model, price):
        self.brand = brand # public
        self._model = model # protected
        self.__price = price # private
    def display(self):
        return f"Brand(public): {self.brand}, Model(protected): {self._model}, Price(private): {self.__price}"
car1 = Car("Toyota", "Corolla", 20000)
print(car1.brand) # Toyota
print(car1.display()) # Brand(public): Toyota, Model(protected): Corolla, Price(private): 20000