age = 12
if age < 4:
    print("Your admission cost is UGX0.")
elif age < 18:
    print("Your admission cost is UGX25.")
else:
    print("Your admission cost is UGX40.")

# Clean code
if age < 4:
    price = 0
elif age < 18:
    price = 25
else:
    price = 40

print(f"Your admission cost is UGX{price}.")

# Using multiple elif blocks
age = 85
if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age < 65:
    price = 40
else:
    price = 20

print(f"Your admission cost is UGX{price}")

# Omitting the else block
age = 12
if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age < 65:
    price = 40
elif age >= 65:
    price = 20

print(f"Your admission cost is UGX{price}.")

# Testing multiple conditions
