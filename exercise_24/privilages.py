"""A modules that extends user class."""

from users import User

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
