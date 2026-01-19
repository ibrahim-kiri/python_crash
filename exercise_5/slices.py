players = ['charles', 'martina', 'michael', 'florence', 'eli']
print('-The first three items in the list are:')
print(players[:3])
print('-The items from the middle of the list are:')
print(players[1:-2])
print('-The last three items in the list are:')
print(players[2:])

pizzas = ['italian pizza', 'chicken pizza', 'meat pizza']
friends_pizzas = pizzas[:]
pizzas.append('chinese pizza')
friends_pizzas.append('ugandan pizza')
print('My favorite pizzas are: ')
for pizza in pizzas:
    print(pizza[:])

print('\nMy friends favorite pizzas are: ')
for pizza in friends_pizzas:
    print(pizza[:])
