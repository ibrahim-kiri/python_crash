# T-Shirt
def make_shirt(size, message):
    print(f"This is {size.title()} size with {message.title()}.")
make_shirt('small', 'i love california')
make_shirt(message='colorado avalanche', size='small')

# Large Shirts
def make_shirt(size='large', message='i love python'):
    print(f"This is {size.title()} size with {message.title()}.")
make_shirt()
make_shirt(size='medium')
make_shirt(size='x-large', message='machine learning guru')

# Cities
def describe_city(name, country='uganda'):
    print(f"{name.title()} is in {country.title()}")
describe_city('mbale')
describe_city('mbarara')
describe_city(name='moshi', country='tanzania')



