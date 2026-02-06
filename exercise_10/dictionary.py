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
    'john': 5,
    'jane': 8,
    'caro': 2,
    'peter': 3,
    'rob': 6,
}
print(favorite_numbers)

# Glossary
glossary = {
    'variable': 'stores values in memory',
    'loops': 'iterates through values',
    'dictionary': 'stores key-value pairs',
}

print(f"variable: {glossary.get('variable', 'No glossary')}")
print(f"loops: {glossary.get('loops', 'No glossary')}")
print(f"dictionary: {glossary.get('dictionary', 'No glossary')}")