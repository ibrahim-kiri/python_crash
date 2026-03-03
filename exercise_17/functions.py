def city_country(city_name, country):
    """Function returns a values"""
    combine = f"{city_name}, {country}"
    return combine.title()
cities = city_country('santiage', 'chile')
print(cities)
cities = city_country('california', 'u s a')
print(cities)
cities = city_country('beirut', 'iran')
print(cities)

def make_album(artist_name, album_title, number_songs=None):
    artist = {'name': artist_name, 'album': album_title}
    if number_songs:
        artist['songs'] = number_songs
    return artist
while True:
    print(f"Enter an artists album and name:")
    print("(enter 'q' to quit)")
    a_name = input("Enter artist name: ")
    if a_name == 'q':
        break
    a_album = input("Enter album name: ")
    if a_album == 'q':
        break
    artist_album = make_album(a_name, a_album)
    print(artist_album)
