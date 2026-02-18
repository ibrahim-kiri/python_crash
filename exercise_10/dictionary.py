# Person
person = {
    'first_name': 'kats',
    'last_name': 'lyn',
    'age': 23,
    'city': 'fort_portal'
}
print(person)

# Favorite numbers
favorite_numbers = {
    'john': [2, 3],
    'jane': [4, 5],
    'caro': [6, 7],
    'peter': [8, 9],
    'rob': [1, 10],
}
for name, numbers in favorite_numbers.items():
    print(f"{name.title()}: {numbers}")

# Glossary
glossary = {
    'variable': 'stores values in memory',
    'loops': 'iterates through values',
    'dictionary': 'stores key-value pairs',
}

print(f"variable: {glossary.get('variable', 'No glossary')}")
print(f"loops: {glossary.get('loops', 'No glossary')}")
print(f"dictionary: {glossary.get('dictionary', 'No glossary')}")

person = {
    'first_name': 'kats',
    'last_name': 'lyn',
    'age': 23,
    'city': 'fort_portal'
}
person_2 = {
    'first_name': 'toby',
    'last_name': 'moby',
    'age': 30,
    'city': 'kampala'
}
person_3 = {
    'first_name': 'pete',
    'last_name': 'lori',
    'age': 27,
    'city': 'kasese'
}
people = [person, person_2, person_3]
for peoples in people:
    print(peoples)

pet_1 = {
    'animal': 'cat',
    'owner': 'jasmine'
}
pet_2 = {
    'animal': 'dog',
    'owner': 'rob'
}
pets = [pet_1, pet_2]
for pet in pets:
    print(pet)

favorite_places = {
    'lyn': ['canada', 'tokyo', 'london'],
    'kate': ['new york', 'brasilia', 'haiti'],
    'john': ['maldives', 'malaysia', 'zanzibar'],
}
for name, place in favorite_places.items():
    print(f"{name.title()}: {place}")

cities = {
    'kampala': {
        'country': 'uganda',
        'population': '5200054',
        'fact': 'Hospitable'
    },
    'nairobi': {
        'country': 'kenya',
        'population': '6580014',
        'fact': 'Developmental'
    },
    'dodoma': {
        'country': 'tanzania',
        'population': '8420003',
        'fact': 'Lovable'
    }
}
cities['kampala']['location'] = 'central'
cities['nairobi']['location'] = 'central'
cities['dodoma']['location'] = 'central'

for city, info in cities.items():
    print(f"\nCity: {city.title()}")
    country = info['country']
    population = info['population']
    location = info['location']
    fact = info['fact']

    print(f"\tCountry: {country.title()}")
    print(f"\tPopulation: {population}")
    print(f"\tLocation: {location.title()}")
    print(f"\tFact: {fact.title()}")