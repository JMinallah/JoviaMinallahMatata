# restaurant class
class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):  # constructor method to initialize the restaurant name and cuisine type
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        
    def describe_restaurant(self):  # method to describe the restaurant
        print(f"{self.restaurant_name} serves {self.cuisine_type} cuisine.")
        
    def open_restaurant(self):  # method to indicate that the restaurant is open
        print(f"{self.restaurant_name} is now open!")
        
# object of the Restaurant class
restaurant = Restaurant("The Gourmet Kitchen", "Italian")
print(f"Restaurant Name: {restaurant.restaurant_name}")
print(f"Cuisine Type: {restaurant.cuisine_type}")
restaurant.describe_restaurant()
restaurant.open_restaurant()

# 2 more restaurants
restaurant2 = Restaurant("Sushi World", "Japanese")
restaurant3 = Restaurant("Taco Fiesta", "Mexican")
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()