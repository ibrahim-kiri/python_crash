from city_functions import get_city_country

def test_city_country():
    """Do names like 'Tehran, Iran' work?"""
    city_country = get_city_country('tehran', 'iran')
    assert city_country == 'Tehran, Iran'

def test_city_country_population():
    """Do names like 'Kampala, Uganda - 30000000' work?"""
    city_country = get_city_country('kampala', 'uganda', 30000000)
    assert city_country == 'Kampala, Uganda - 30000000'