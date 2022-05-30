# greeter.py
"""def get_formatted_name(first_name, last_name):
    # return formatted name
    full_name = f"{first_name} {last_name}"
    return full_name.title()


# endless cycle
while True:
    print("\nPLease tell me your name: ")
    print("enter 'q' at any time to quit\n")
    f_name = input("First name: ")
    if f_name == 'q':
        break
    l_name = input("Last name: ")
    if l_name == 'q':
        break

    formatted_name = get_formatted_name(f_name, l_name)
    print(f"\nHello, {formatted_name}")"""

# 8.2 favorite book
"""def favorite_book(title):
    print(f"One of my favorite books is {title}")

favorite_book('Python Crash Course')"""

# pets.py
"""def describe_pet(pet_name, animal_type='turtle'):
    print(f"\nI have a {animal_type} ")
    print(f"My {animal_type}'s name is {pet_name.title()}")


describe_pet('donatello')"""

# 8.3 - 8.4 T-shirt
"""def make_shirt1(shirt_size, shirt_print):
    print(f"\nSize of this T-shirt is {shirt_size.upper()}")
    print(f"Print on this T-shirt is {shirt_print.title()}")


make_shirt1('xxl', 'randomness')


def make_shirt2(shirt_size, shirt_print):
    print(f"\nSize of this T-shirt is {shirt_size.upper()}")
    print(f"Print on this T-shirt is {shirt_print.title()}")


make_shirt2(shirt_size='xs', shirt_print='workout')


def make_shirt2(shirt_print, shirt_size='l'):
    print(f"\nSize of this T-shirt is {shirt_size.upper()}")
    print(f"Print on this T-shirt is {shirt_print.title()}")


make_shirt2('i love Python')"""

# 8.5 Cities
"""def describe_city(city_name, country_name="ukraine"):
    print(f"{city_name.title()} is in {country_name.title()}")


describe_city('kyiv')
describe_city('tokyo', 'japan')
describe_city('berlin', 'germany')"""

# formatted name.py
"""def get_formatted_name(first_name, last_name='truten', middle_name=""):
    # return formatted name
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()


me = get_formatted_name(first_name='dmitriy')
print(me)

me = get_formatted_name('dmitriy', 'truten', 'vitaliyovych')
print(me)"""

# person.py
"""def build_person(first_name, last_name, age=None):
    # return dictionary with information about person
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person


me = build_person('dmitriy', 'truten', age=19)
print(me)"""

# 8.6 City names
"""def city_country(city_name, country_name):
    # entering names
    names = f"{city_name.title()}, {country_name.title()}"
    print(names)


city_country('kyiv', 'ukraine')
city_country('berlin', 'germany')
city_country('rome', 'italy')"""

# 8.7 Album

"""def make_album(musician_name, album_name, year_album=None):
    album_info = {'musician': musician_name.title(), 'album': album_name.title()}
    if year_album:
        album_info['year_album'] = year_album

    return album_info


while True:
    musician = input("Enter a musician name: ('q' to stop)")
    if musician == 'q':
        break

    album = input("Enter an album name: ('q' to stop)")
    if album == 'q':
        break

    our_album = make_album(musician, album)
    print(f"\n{our_album}")"""

# greet_ users.py
"""def greet_users(names):
    # return simple message for every user in list
    for name in names:
        msg = f"Hello, {name.title()}"
        print(msg)


usernames = ['hannah', 'ty', 'dimchek']
greet_users(usernames)"""

# printing_models.py
def print_models(unprinted_designs, completed_models):
    # simulating print for every model, until last one
    # add every print to completed_models after print
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printing model: {current_design}")
        completed_models.append(current_design)


def show_completed_models(completed_models):
    # show all printed models
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)


"""unprinted_designs = ['phone case', 'robot pendant', 'jojo figurka']
completed_models = []

print_models(unprinted_designs[:], completed_models)
show_completed_models(completed_models)"""

# 8.9 Message
"""def show_messages(text_messages):
    for text in text_messages:
        print(f"{text.title()}")


text_messages = ['hello, hawdyoudo', 'sho tu tam', 'kak ponyat def?']
show_messages(text_messages)"""

# 8.10 Sending messages
"""def show_messages(text_messages):
    for text in text_messages:
        print(f"{text.title()}")


def send_messages(sent_messages):
    for sent in text_messages:
        sent_messages.append(sent)
        print(f"{sent}")


text_messages = ['hello, hawdyoudo', 'sho tu tam', 'kak ponyat def?\n']
sent_messages = []
show_messages(text_messages)
send_messages(sent_messages)"""

# 8.12 Sandwich
"""def ingredients_list(*ingredients):
    print(ingredients)


ingredients_list('kivbasa')
ingredients_list('kivbasa', 'cheese')
ingredients_list('kivbasa', 'cheese', 'ketchup')"""

# 8.13 User profile
"""def build_profile(first, last, **user_info):
    # make a dictionary that have all information about user
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info


user_profile = build_profile('dimchek', 'truten',
                             location='ukraine',
                             field='coding(чючють)',
                             food='vodichka',
                             computer='microwave',
                             english_level="c3")
print(user_profile)"""


# 8.14 Cars
"""def make_car(car_model, car_submodel, **other_info):
    other_info['car_model'] = car_model
    other_info['car_submodel'] = car_submodel
    return other_info


car = make_car('subaru', 'outback', color='blue', tow_package=True)
print(car)"""