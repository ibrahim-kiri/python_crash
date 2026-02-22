# Pizza toppings
prompt = "\nEnter your pizza topping: "
prompt += "\nType 'quit' to exit: "

active = True
while active:
    message = input(prompt)
    print("We shall add that topping to your pizza")
    if message == 'quit':
        active = False
    else:
        print(message)

# Movie tickets
prompt = "\nEnter your age."
prompt += "\nType '0' to exit: "

active = True
while active:
    age = int(input(prompt))

    if age == 0:
        active = False
    elif age < 3:
        print("Ticket if free")
    elif age <= 12:
        print("Ticket is $10")
    elif age > 12:
        print("Ticket is $15")
        break

# Infinity
while True:
    print("Am a rich great programmer")