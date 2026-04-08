from city_functions import get_city_country

print("Enter 'q' at any time to quit.")
while True:
    city_name = input("\nPlease give me a city name: ")
    if city_name == 'q':
        break
    country_name = input("Please give me a country name: ")
    if country_name == 'q':
        break

    city_country = get_city_country(city_name, country_name)
    print(f"\tNeatly formatted city and country name: {city_country}.")