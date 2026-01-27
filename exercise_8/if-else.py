# Alien Colors .1
player = 'john'
alien_color = ['green', 'yellow', 'red']
alien = alien_color[0]
if alien == 'green':
    print(f"{player.title()}, you just earned 5 points")

if 'green' not in alien_color:
    print("")

# Alien Colors .2
player = 'jane'
alien_color = ['green', 'yellow', 'red']
alien = alien_color[0]
if alien == 'green':
    print(f"{player.title()}, you just earned 5 points for shooting the alien")
else:
    print(f"{player.title()}, you just earned 10 points.")

# Alien Clolors .3
player = 'caro'
alien_color = ['green', 'yellow', 'red']
alien = alien_color[0]
if alien == 'green':
    print(f"{player.title()}, you just earned 5 points for shooting the alien")
elif alien == 'yellow':
    print(f"{player.title()}, you just earned 10 points for shooting the alien")
elif alien =='red':
    print(f"{player.title()}, you just earned 15 points for shooting the alien")

alien_color = ['green', 'yellow', 'red']
alien = alien_color[1]
if alien == 'green':
    print(f"{player.title()}, you just earned 5 points for shooting the alien")
elif alien == 'yellow':
    print(f"{player.title()}, you just earned 10 points for shooting the alien")
elif alien =='red':
    print(f"{player.title()}, you just earned 15 points for shooting the alien")

alien_color = ['green', 'yellow', 'red']
alien = alien_color[2]
if alien == 'green':
    print(f"{player.title()}, you just earned 5 points for shooting the alien")
elif alien == 'yellow':
    print(f"{player.title()}, you just earned 10 points for shooting the alien")
elif alien =='red':
    print(f"{player.title()}, you just earned 15 points for shooting the alien")

# Stages of Life
age = 13
if age < 2:
    print('A baby')
elif age <= 4:
    print(' A toddler')
elif age <= 13:
    print('A kid')
elif age <= 20:
    print('A teenager')
elif age <= 65:
    print('An adult')
else:
    print('An elder')

# Favorite Fruit
favorite_fruits = ['mango', 'apple', 'orange']
if 'mango' in favorite_fruits:
    print(f'You really like {favorite_fruits[0]}!')
if 'apple' in favorite_fruits:
    print(f'You really like {favorite_fruits[1]}!')
if 'orange' in favorite_fruits:
    print(f'You really like {favorite_fruits[2]}')