def sandwich(*args):
    """Function accepting a list of items"""
    print("Summary of sandwiches being ordered:")
    for arg in args:
        print(f"- {arg}")
sandwich("pepperoni")
sandwich("pineapple", "mushrooms", "chicken")

def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info
user_profile = build_profile('kiringabakwe', 'ibrahim', location='kampala', field='python')
print(user_profile)

def make_car(manufacturer, model, **car_info):
    """Function that stores information about a car"""
    car_info['manufacturer'] = manufacturer
    car_info['model'] = model
    return car_info
car_profile = make_car('subaru', 'outback', color='blue', tow_package=True)
print(car_profile)
