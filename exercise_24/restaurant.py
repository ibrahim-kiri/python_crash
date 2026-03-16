"""A module for representing a restaurant logic"""

class Restaurant:
    """A class respresenting a restaurant"""

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """A method printing restaurant information"""
        print(f"\nThe restaurant name is {self.restaurant_name}")
        print(f"The foods they offer are {self.cuisine_type}")

    def open_restaurant(self):
        """A method that indicates the restaurant is open"""
        print(f"Restaurant {self.restaurant_name} is open and operating!")

    def set_number_served(self, customer):
        "A method to set the number of customers"
        try:
            if customer >= self.number_served:
                self.number_served = customer
            else:
                print("It has served no customer")

            return f"It has served {self.number_served} customers!"
        
        except Exception as e:
            print(f"There is an error {e}")
    
    def increment_number_served(self, customers):
        """A method that increments the number of customers"""
        try:
            if customers >= self.number_served:
                self.number_served += customers
            else:
                print("No customer was served today!")

            return f"The restaurant served {self.number_served} customers today!"
        
        except Exception as e:
            print(f"There is an error {e}")

class Flavors:
    """Class for flavors"""

    def __init__(self, 
                 flavors=['strawberry', 'chocolate']
                ):
        """Initialize flavors attributes"""
        self.flavors = flavors

    def display_flavors(self):
        """A method that displays ice cream flavors"""

        try:
            print(f"Here are the ice cream flavors:")
            for flavor in self.flavors:
                print(f"- {flavor}")

        except Exception as e:
            print(f'There was an error: ({e})')
            


class IceCreamStand(Restaurant):
    """Class inheriting from Restaurant class"""

    def __init__(self, restaurant_name, cuisine_type):
        """Initializes attributes of the parent class"""
        super().__init__(restaurant_name, cuisine_type)
        self.ice_flavors = Flavors()

