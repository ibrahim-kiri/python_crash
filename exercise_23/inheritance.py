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

my_flavor = IceCreamStand('Ibras Inn', 'All foods')
my_flavor.ice_flavors.display_flavors()


class User:
    """Class to create a user"""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.login_attempts = 0

    def describe_user(self):
        """Method that prints summary of a user info"""
        print(f"\nMy name is {self.first_name} {self.last_name}.")
        print(f"I'm {self.age} years old")

    def greet_user(self):
        """Method to print a personalized message"""
        self.name = f"{self.first_name} {self.last_name}"
        print(f"Hi {self.name} your welcome!")

    def increment_login_increments(self, login):
        """
        A method to that increments the value of login attempts
        """
        try:
            if login >= self.login_attempts:
                self.name = f"{self.first_name} {self.last_name}"
                self.login_attempts += login

                print(f"{self.name.title()} has logged in {self.login_attempts} time(s)")
            else:
                print("There was no login attempt!")

        except Exception as e:
            print("There was an error {e}")

    def reset_login_attempts(self, logout):
        """ A method that resets the value of login attempts"""
        try:
            if logout <= self.login_attempts:
                self.name = f"{self.first_name} {self.last_name}"
                self.login_attempts -= logout

                print(f"{self.name.title()} has logged out {self.login_attempts} time(s)")
            else:
                print("There was no logout attempt!")

        except Exception as e:
            print(f"There was an error {e}")


class Privilege:
    """Class for Privileges"""

    def __init__(self, 
                 privileges=['can add post', 'can delete post', 'can ban a user']
                ):
        """Initialize flavors attributes"""
        self.privileges = privileges

    def show_privileges(self):
        """A method that lists thw administrators privileges"""

        try:
            print(f"\nHere are the admin privilages:")
            for privilege in self.privileges:
                print(f"- {privilege}")

        except Exception as e:
            print(f'There was an error: ({e})')


class Admin(User):
    """Class Admin inherits from User"""

    def __init__(self, first_name, last_name, age):
        """Initializes attributes of the parent class"""
        super().__init__(first_name, last_name, age)
        self.admin_privileges = Privilege()

admin_privilage = Admin('Kiringabakwe', 'Ibrahim', 34)
admin_privilage.admin_privileges.show_privileges()


class Car:
    """A simple attempt to represent a car."""

    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    
    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        """Set the odometer reading to the given value."""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading."""
        self.odometer_reading += miles


class Battery:
    """A simple attempt to model a battery for an electric car."""

    def __init__(self, battery_size=40):
        """Initialize the battery's attributes."""
        self.battery_size = battery_size

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-KWh battery.")

    def get_range(self):
        """Print a statement about the range this battery provides."""
        if self.battery_size == 40:
            ranges = 150
        elif self.battery_size == 65:
            ranges = 225

        print(f"\nThis car can go about {ranges} miles on a full charge.")

    def upgrade_battery(self):
        """A method upgrades the battery to 65 kWh"""
        if self.battery_size < 65:
            self.battery_size = 65
            print("Battery upgraded to 65-kwh")
        else:
            print("Battery is already upgraded.")
        
        

class ElectricCar(Car):
    """
    Represent aspects of a car, specific to electric vehicles.
    """

    def __init__(self, make, model, year):
        """
        Initialize attributes of the parent class.
        Then initialize attributes specific to an electric car.
        """
        super().__init__(make, model, year)
        self.battery = Battery()

my_car = ElectricCar('subaru', 'empreza', 2026)
my_car.battery.get_range()
my_car.battery.upgrade_battery()
my_car.battery.get_range()





        

