"""alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print(f"Original position: {alien_0['x_position']}")

if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3

alien_0['x_position'] = alien_0['x_position'] + x_increment
print(f"New position: {alien_0['x_position']}")

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }
for name, language in favorite_languages.items():
    print(f"{name.title()}'s favorite language is {language.title()},.")
for name in favorite_languages.keys():
    print(name.title())

alien_0 = {'color': 'green', 'speed': 'slow'}
point_value = alien_0.get("points", "No point value assigned")
print(point_value)

# 6.1 Human
human = {
    'first_name': 'Pasha',
    'last_name': 'Rymarovych',
    'age': 18,
    'city': 'Troeschina',
    }
print(f"{human['first_name']}"
      f"\n{human['last_name']}"
      f"\n{human['age']}"
      f"\n{human['city']}")

# 6.3 Glossary
glossary = {
    'data type': 'Can be int, str, float, boolean',
    'integer': 'number',
    'cycle': 'thing that repeat some part of code'
}
print(f"Data type {glossary['data type'].lower()}"
      f"\n Integer is a {glossary['integer'].upper()}"
      f"\n Cycle is a {glossary['cycle'].title()}")

user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi',
}

for key, value in user_0.items():
    print(f"\nKey: {key}")
    print(f"Value: {value}")


friends = ['phil', 'jen']
for name in favorite_languages.keys():
    print(f"Hi {name.title()}")
if name in friends:
    language = favorite_languages[name].title()
    print(f"\t{name.title()}, I see you love {language}")
if 'erin' not in favorite_languages.keys():
    print("Erin, please take our poll")

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }
for name in sorted(favorite_languages.keys()):
    print(f"{name.title()}, thank you for taking poll")

# перебір всіх значень в словнику
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

print("The following languages have been mentioned:")
for language in favorite_languages.values():
    print("\t", language.title())

# 6.4 Glossary 2

glossary = {
    'data type': 'Can be int, str, float, boolean',
    'integer': 'number',
    'cycle': 'thing that repeat some part of code',
    'dictionary': 'is a complicated list, for me))',
    'strip()': 'cool method, i like it',
    'lower().upper()': 'also funny methods'
    }
for key, value in glossary.items():
    print(f"{key.title()} - {value.lower()} ")

# 6.5 Rivers
rivers = {
    'dnipro': 'ukraine',
    'amazonka': 'brazilia',
    'nile': 'egypt'
}
nenka = ['dnipro']
for key in rivers.keys():
    print(key.title())

    if key in nenka:
        x = rivers[key].title()
        print(key.lower())

alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2= {'color': 'red', 'points': 15}

aliens = [alien_0, alien_1, alien_2]
for alien in aliens:
    print(alien)

favorite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell']
}
for name, languages in favorite_languages.items():
    print(f"\n{name.title()}'s favorite languages are:")
    for language in languages:
        print(f"\t{language.title()}")

# 6.7 People
human1 = {
    'first_name': 'Pasha',
    'last_name': 'Rymarovych',
    'age': 18,
    'city': 'Troeschina\n',
}
human2 = {
    'first_name': 'Volodymyr',
    'last_name': 'Tymoshenko',
    'age': 18,
    'city': 'Malyn\n',
}
human3 = {
    'first_name': 'Vlad',
    'last_name': 'Sakun',
    'age': 19,
    'city': 'Poznyaky',
}
people = [human1, human2, human3]
for user in people:
    for key, value in user.items():
        print(f"{key} - {value}")

# 6.9 Favorite places
favorite_places = {
    'dmitriy': ['kyiv', 'zhytomyr', 'cherkasy'],
    'pasha': ['troya', 'prk', 'smth else'],
    'vova': ['malyn', 'kyiv', 'selo']
}
for name, places in favorite_places.items():
    print(f"\n{name.title()}'s favorite places are:")
    for place in places:
        print(f"\t{place.title()}")

# 6.11 Cities
cities = {
    'kyiv': {
        'country': 'ukraine',
        'population': '2_888_470',
        'fact': 'i live here'
    },

    'berlin': {
        'country': 'germany',
        'population': '3_574_830',
        'fact': 'my mom near there'
    },

    'verona': {
        'country': 'italy',
        'population': '257_353',
        'fact': 'its name like my favorite pizza)'
    }
}
for city, city_info in cities.items():
    print(f"{city.title()}:")
    country = city_info['country']
    population = city_info['population']
    fact = city_info['fact']
    print(f"\tCountry - {country.title()}\n"
          f"\tPopulation - {population.title()}\n"
          f"\tFact - {fact.title()}\n")"""

