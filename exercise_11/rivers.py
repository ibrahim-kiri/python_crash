rivers = {
    'nile': 'egypt',
    'zambezi': 'zambia',
    'kivu': 'congo',
}
for river, country in rivers.items():
    print(f"The {river.title()} runs through {country.title()}")

rivers = {
    'nile': 'egypt',
    'zambezi': 'zambia',
    'kivu': 'congo',
}
for river in rivers.keys():
    print(river.title())

rivers = {
    'nile': 'egypt',
    'zambezi': 'zambia',
    'kivu': 'congo',
}
for country in rivers.values():
    print(country.title())


favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
}
programmers = ['peter', 'jen', 'sarah', 'edward', 'caro', 'phil']
for name in programmers:
    if name in favorite_languages:
        print(f'{name.title()}, thanks for responding')
    elif name not in favorite_languages:
        print(f'{name.title()}, your invited to take the poll.')

    