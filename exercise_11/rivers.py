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