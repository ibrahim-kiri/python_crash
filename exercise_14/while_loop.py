sandwich_orders = ['pastrami', 'red sandwich', 'orange sandwich', 'pastrami']
finished_sandwiches = []
print("\nSandwich orders has run of pastrami")

while sandwich_orders:
    while 'pastrami' in sandwich_orders:
        sandwich_orders.remove('pastrami')
    current_sandwich = sandwich_orders.pop()
    print(f"I made your {current_sandwich}")
    finished_sandwiches.append(current_sandwich)
print("All the sandwiches that are finished:")
for finished_sandwich in finished_sandwiches:
    print(finished_sandwich.title())

responses = {}
poll_active = True
while poll_active:
    name = input("What is your name: ")
    vacation = input("If you could visit one place in the world, where would you go? ")
    responses[name] = vacation
    repeat = input("Continue yes / no: ")
    if repeat == 'no':
        poll_active = False
for name, vacation in responses.items():
    print(f"{name.title()}: {vacation.title()}")
