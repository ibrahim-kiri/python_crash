# Hello admins
usernames = ['admin', 'jane', 'john', 'cathy', 'rob']

for username in usernames:
    if username == 'admin':
        print(f"Hello admin, would you like to see a status report?")
    else:
        print(f"Hello {username}, thank you for logging in again.")

# No users
usernames = []

if usernames:
    for username in usernames:
        print(username)
else:
    print("We need to find some users!")

# Checking usernames
current_users = ['admin', 'jane', 'john', 'cathy', 'rob']
new_users = ['caro', 'jane', 'bob', 'peter', 'cathy']

for new_user in new_users:
    if new_user in current_users:
        print(f"{new_user}, you will need to enter a new username!")
    else:
        print(f"{new_user}, is available!")

existing_users = [user.lower() for user in current_users]
new_users = ['caro', 'JANE', 'bob', 'peter', 'CATHY']

for new_user in new_users:
    if new_user.lower() in existing_users:
        print(f"{new_user}, should not be accepted!")
    else:
        print(f"{new_user} is available.")

# Ordinal numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for number in numbers:
    if number == 1:
        print(f"{number}st")
    elif number == 2:
        print(f"{number}nd")
    elif number == 3:
        print(f"{number}rd")
    else:
        print(f"{number}th")


