# Sorting a list permanently with sort() method
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)
cars.sort(reverse=True)
print(cars)

# Sorting a list temporarily with the sorted() function
print('Here is the original list:')
print(cars)

print('\nHere is the sorted list:')
print(sorted(cars))

print('\nHere is the original list again:')
print(cars,'\n')

# Printing a list in reverse order
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)
cars.reverse()
print(cars)

# Finding the length of a list
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(len(cars))