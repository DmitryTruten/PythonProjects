"""cars = car_models = ["audi", "bmw", "mercedes-Benz"]

for car in cars:
    if car == "bmw":
        print(car.upper())
    else:
        print(car.title())

requested_toppings = 'mushrooms'

if requested_toppings != 'anchovies':
    print("Anchovies!")

banned_users = ['petya', 'galya', 'vasya']
user = 'dima'
if user not in banned_users:
    print(f"{user.title()}, you can post something")

# 5.1 If-else:
car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')

print("Is car == 'audi'? I predict False.")
print(car == 'audi')

#5.8 Hello admin!
users = []
if users:
    for user in users:
        if user == 'admin':
            print("Hello admin, sho tu tam")
        else:
            print(f"Hello {user}")
else:
    print("We need to find users")

# 5.10 Checking usernames
current_users = [' PETYA', 'Galya', 'vasya ', ' anya', ' Dima']
new_users = ['pasha', 'vova', 'vlad', 'anya', 'dima']
current_users_normal = []
for current_user in current_users:
    low = current_user.strip().lower()
    current_users_normal.append(low)
print(current_users_normal)

for new_user in new_users:
    if new_user in current_users_normal:
        print(f"{new_user}, please choose another name.")
    else:
        print(f"{new_user} - this username still available")

# 5.11 ordinal numerators
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for number in numbers:
    if number == 1:
        print("1st")
    elif number == 2:
        print("2nd")
    elif number == 3:
        print("3rd")
    else:
        print(f"{number}th")"""
