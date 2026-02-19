message = input("What kind of rental car would you like: ")
print(f"Let me see if I can find you a {message}")

message = input("How many people are in your dinner group? ")
message = int(message)
if message >= 8:
    print("You'll have to wait for a table.")
else:
    print("Your table is ready.")

number = input("Enter any number: ")
number = int(number)
if number % 10 == 0:
    print(f"{number} is a multiple of 10.")
else:
    print(f"{number} is NOT a multiple of 10.")