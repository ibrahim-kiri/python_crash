def get_city_country(city_name, country_name, population=''):
    """Generate a neatly formatted city and country name."""
    if population:
        names = f"{city_name}, {country_name} - {population}"
    else:
        names = f"{city_name}, {country_name}"
    return names.title()