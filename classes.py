# dog.py
"""class Dog:
    # simple attempt modeling the dog

    def __init__(self, name, age):
        # initiate atributes name and age

        self.name = name
        self.age = age

    def sit(self):
        # simulate doing command 'sit'
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        # simulate doing command 'sit'
        print(f"{self.name} rolled over")


my_dog = Dog('Willie', 6)
your_dog = Dog('Lucy', 12)

print(f"My dog's name is {my_dog.name}")
print(f"My dog is {my_dog.age} years old")
my_dog.roll_over()

print(f"\nYour dog's name is {your_dog.name}")
print(f"Your dog is {your_dog.age} years old")
your_dog.sit()"""

# 9-1 Restaurant
"""class Restaurant:

    # modeling the restaurant
    def __init__(self, restaurant_name, cuisine_type, restaurant_owner):
        # define the atributives of exemp
        self.name = restaurant_name
        self.cuisine = cuisine_type
        self.owner = restaurant_owner

    def describe_restaurant(self):
        print(f"Restaurant name - {self.name.title()}\n"
              f"Cuisine type - {self.cuisine.title()}")

    def open_restaurant(self):
        print(f"{self.name.title()} is opened from 9:00 to 18:00")

    def restaurant_owner(self):
        print(f"{self.owner} is own {self.name}\n")


my_restaurant = Restaurant('zatoichi', 'japanese', 'Dimchek')
my_restaurant.describe_restaurant()
my_restaurant.restaurant_owner()

pasha_restaurant = Restaurant('troyeshinska shaurma', 'armenian', 'Pashonkus')
pasha_restaurant.describe_restaurant()
pasha_restaurant.restaurant_owner()"""

# 9-3 Users
"""class User:
    def __init__(self, first_name, last_name, age, avatarka):
        # initiate atributes
        self.first = first_name
        self.last = last_name
        self.age = age
        self.ava = avatarka

    def describe_user(self):
        print(f"Users name - {self.first.title()}\n"
              f"Users last name - {self.last.title()}\n"
              f"Users age - {self.age}\n"
              f"Avatarka - {self.ava}\n")

    def greet_user(self):
        print(f"Hello {self.first.title()} {self.last.title()} on our website!\n")

user1 = User('dmitriy', 'truten', 19, 'wojak')
user2 = User('pasha', 'rymarovych', 18, 'himself')
 
user1.describe_user()
user1.greet_user()

user2.describe_user()
user2.greet_user()"""

# car.py
"""class Car:
    # attempt to model car
    def __init__(self, make, model, year):
        # initialyzing atributes that describes car
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 2500

    def get_descriptive_name(self):
        # return formatted name
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        print(f"This car has {self.odometer_reading} kilometres on it")

    def update_odometer(self, kilometrage):
        # set odometers value
        # deny changes if odometer values rolled back
        if kilometrage >= self.odometer_reading:
            self.odometer_reading = kilometrage
        else:
            print("You cant roll back an odometer!")

    def increment_odometer(self, kilometres):
        # add setted value to odometer
        self.odometer_reading += kilometres"""

"""my_new_car = Car('audi', 'r8', 2006)
print(my_new_car.get_descriptive_name())

my_new_car.update_odometer(24_000)
my_new_car.read_odometer()

my_new_car.increment_odometer(1500)
my_new_car.read_odometer()"""

# 9-4 amount of clients
"""class Restaurant:

    # modeling the restaurant
    def __init__(self, restaurant_name, cuisine_type, restaurant_owner):
        # define the atributives of exemp
        self.name = restaurant_name
        self.cuisine = cuisine_type
        self.owner = restaurant_owner
        self.number_served = 20

    def describe_restaurant(self):
        print(f"Restaurant name - {self.name.title()}\n"
              f"Cuisine type - {self.cuisine.title()}")

    def open_restaurant(self):
        print(f"{self.name.title()} is opened from 9:00 to 18:00")

    def restaurant_owner(self):
        print(f"{self.owner} is own {self.name}\n")

    def amount_of_clients(self):
        print(f"In {self.name.title()} restaurant are {self.number_served} clients")

    def set_number_served(self, number_served):
        self.number_served = number_served

    def increment_number_served(self, new_clients):
        print(f"We have {new_clients} new clients!")
        self.number_served += new_clients


my_restaurant = Restaurant('zatoichi', 'japanese', 'Dimchek')
my_restaurant.set_number_served(20)
my_restaurant.amount_of_clients()

my_restaurant.increment_number_served(10)
my_restaurant.amount_of_clients()"""

# 9-5 Authorization attempts
"""class User:
    def __init__(self, first_name, last_name, age, avatarka):
        # initiate atributes
        self.first = first_name
        self.last = last_name
        self.age = age
        self.ava = avatarka
        self.login_attempts = 0

    def describe_user(self):
        print(f"Users name - {self.first.title()}\n"
              f"Users last name - {self.last.title()}\n"
              f"Users age - {self.age}\n"
              f"Avatarka - {self.ava}\n")

    def greet_user(self):
        print(f"Hello {self.first.title()} {self.last.title()} on our website!\n")

    def increment_login_attempts(self):
        self.login_attempts += 1
        print(f"Login attempts: {self.login_attempts} times")

    def reset_login_attempts(self):
        self.login_attempts = 0
        print(f"You have reseted login attempts({self.login_attempts})")


user1 = User('dmitriy', 'truten', 19, 'wojak')
user1.describe_user()
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.reset_login_attempts()"""

# electric_car.py
"""class Car:
    # attempt to model car
    def __init__(self, make, model, year):
        # initialyzing atributes that describes car
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        # return formatted name
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        print(f"This car has {self.odometer_reading} kilometres on it")

    def update_odometer(self, kilometrage):
        # set odometers value
        # deny changes if odometer values rolled back
        if kilometrage >= self.odometer_reading:
            self.odometer_reading = kilometrage
        else:
            print("You cant roll back an odometer!")

    def increment_odometer(self, kilometres):
        # add set value to odometer
        self.odometer_reading += kilometres


class Battery:
    # Simple attempt to model accumulator of electrocar

    def __init__(self, battery_size=75):
        # Initialize attributes of accumulator
        self.__battery_size = battery_size

    def describe_battery(self):
        # Print a message about battery size
        print(f"This car has a {self.__battery_size}-kWh battery")

    def uprade_battery(self):
        if self.__battery_size < 100:
            self.__battery_size = 100

    def get_range(self):
        # Print a message about distance
        # which this car can ride through
        # according to battery size
        if self.__battery_size == 75:
            range = 260
        elif self.__battery_size == 100:
            range = 315
        print(f"This car can go about {range} kilometres on a full charge")


class ElectricCar(Car):
    # modeling attribute, that electrocars have
    def __init__(self, make, model, year):
        # start attributes of super class
        # initialize super class attributes, than initialize electrocar attributes
        super().__init__(make, model, year)
        self.battery = Battery()


my_tesla = ElectricCar('tesla', 'model s', 2019)
print(my_tesla.get_descriptive_name())

my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
my_tesla.battery.uprade_battery()

my_tesla.battery.describe_battery()
my_tesla.battery.get_range()"""


class Human:
    default_name = 'Name'
    default_age = 0

    def __init__(self, name=default_name, age=default_age):
        self.name = name
        self.age = age
        self.__money = 0
        self.__house = None

    def info(self):
        print(f"Name - {self.name}")
        print(f"Age - {self.age}")
        print(f"Money - {self.__money}")
        print(f"House - {self.__house}")

    # Статический метод
    @staticmethod
    def default_info():
        print(f"{Human.default_name} "
              f"{Human.default_age}")

    # Приватний метод
    def __make_deal(self, house, price):
        self.__money -= price
        self.__house = house

    def earn_money(self, amount):
        self.__money += amount
        print(f"Earned money - {self.__money}")

    def buy_house(self, house, discount):
        price = house.final_price(discount)
        if self.__money >= price:
            self.__make_deal(house, price)
            print("You bought a house!")
        else:
            print("Not enough money")


class House:
    def __init__(self, area, price):
        self._area = area
        self._price = price

    def final_price(self, discount):
        final_price = self._price * (100 - discount) / 100
        print(f"Final price - {final_price}")
        return final_price


class SmallHouse(House):
    default_area = 40

    def __init__(self, price):
        super().__init__(SmallHouse.default_area, price)


Human.default_info()
dimasik = Human('Dimasik', 19)
dimasik.info()

dacha = SmallHouse(9_000)
dimasik.buy_house(dacha, 3)

dimasik.earn_money(9_000)

dimasik.buy_house(dacha, 5)
dimasik.info()
