class Restaurant:
    """A class respresenting a restaurant"""

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """A method printing restaurant information"""
        print(f"\nThe restaurant name is {self.restaurant_name}")
        print(f"The foods they offer are {self.cuisine_type}")

    def open_restaurant(self):
        """A method that indicates the restaurant is open"""
        print(f"Restaurant {self.restaurant_name} is open and operating!")

restaurant = Restaurant("Ibra's Inn", "All Foods")
print(f"Restaurant name is {restaurant.restaurant_name}.")
print(f"They offer {restaurant.cuisine_type}.")
restaurant.describe_restaurant()
restaurant.open_restaurant()

restaurant_one = Restaurant("Fati's Inn", "French Foods")
restaurant_one.describe_restaurant()

restaurant_two = Restaurant("Aminah's Inn", "Swahili Foods")
restaurant_two.describe_restaurant()


class User:
    """Class to create a user"""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def describe_user(self):
        """Method that prints summary of a user info"""
        print(f"\nMy name is {self.first_name} {self.last_name}.")
        print(f"I'm {self.age} years old")

    def greet_user(self):
        """Method to print a personalized message"""
        self.name = f"{self.first_name} {self.last_name}"
        print(f"Hi {self.name} your welcome!")

user = User('Kiringabakwe', 'Ibrahim', 34)
user.describe_user()
user.greet_user()

user = User('Katusiime', 'Irene', 24)
user.describe_user()
user.greet_user()
        


