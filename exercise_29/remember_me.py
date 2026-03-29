from pathlib import Path
import json

def get_stored_user(path):
    """Get stored user info if available."""

    if path.exists():
        contents = path.read_text()
        user_info = json.loads(contents)
        return user_info
    else:
        return None

def get_new_user(path):
    """Prompt for a new user info."""
    username = input("What is your username? ")
    full_name = input("What are your names? ")
    city = input("What city do you live in: ")

    user_info = {
        "username": username,
        "full_name": full_name,
        "city": city
    }
    contents = json.dumps(user_info)
    path.write_text(contents)
    return user_info

def greet_user():
    """Greet the user by user info."""

    path = Path('user.json')
    user_info = get_stored_user(path)

    if user_info:
        stored_user = user_info
        print(f"Welcome back, {stored_user}!")

        correct = input("Is this the correct user? (yes/no): ")

        if correct.lower() == 'yes':
            print(f"Welcome back, {stored_user}!")
        else:
            user_info = get_new_user(path)
            print(f"We'll remember you when you come back, {user_info}!")
    else:
        user_info = get_new_user(path)
        print(f"We'll remember you when you come back, {user_info}!")

greet_user()