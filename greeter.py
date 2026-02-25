name = input("Please enter your name: ")
print(f"\nHello, {name}!")

prompt = "If you share your name, we can personalize the messages you see."
prompt += "\nWhat is your first name? "

name = input(prompt)
print(f"\nHello, {name}!")

# Using int() to accept numerical input
age = input("How old are you? ")
print(age)

# Defining a function
def greet_user():
    """Display a simple greeting."""
    print("Hello!")
greet_user()

# Passing information to a function
def greet_user(username):
    """Display a simple greeting."""
    print(f"Hello, {username.title()}!")
greet_user('jesse')