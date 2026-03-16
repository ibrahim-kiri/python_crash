"""A module for user management."""

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