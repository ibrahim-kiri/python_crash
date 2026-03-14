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


restaurant = Restaurant('Ibras Inn', 'All Foods')
restaurant.describe_restaurant()
restaurant.open_restaurant()
print(restaurant.set_number_served(22))
print(restaurant.increment_number_served(50))

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

user = User('katusiime', 'irene', 24)
user.describe_user()
user.greet_user()
user.increment_login_increments(1)
user.increment_login_increments(2)
user.increment_login_increments(3)
user.reset_login_attempts(1)
user.reset_login_attempts(2)
user.reset_login_attempts(3)

        

