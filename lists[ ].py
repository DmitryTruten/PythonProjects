# 3.1 Names

"""names = ["Pasha", "Vova", "Vlad"]
print("\n", names[0], "\n", names[1], "\n", names[2], "\n")

# 3.2 Greetings

greetings = f"Darova {names[0]}, {names[1]}, {names[2]}!"
print(greetings, "\n")

# 3.3 Personal list

car_models = ["audi", "bmw", "mercedes-Benz"]
print(f"I would like to own {car_models[0].title()}\n"
      f"Personally, i don't like {car_models[1].upper()}, besides the {car_models[1].upper()} M3 GTR\n"
      f"{car_models[2].title()} is a pretty well car")

motorcycles = ["honda", "suzuki", "priora"]
motorcycles.append("brychka") #додає один елемент до кінця списку
print(motorcycles, "\n")

motorcycles = ["honda", "suzuki", "priora"]
motorcycles.insert(1, "brychka") #вставляє один елемент в будь-яку частину списку
print(motorcycles, "\n")

motorcycles = ["honda", "suzuki", "priora"]
del motorcycles[0], motorcycles[0] #видаляє елемент без повернення
print(motorcycles, "\n")

motorcycles = ["honda", "suzuki", "priora"]
popped_motorcycles = motorcycles.pop() #видаляє елемент з можливістю використання
print(motorcycles)
print(popped_motorcycles, "\n")

motorcycles = ["honda", "suzuki", "priora"]
first_owned = motorcycles.pop(2)
print(f"The first motorcycle i got was a {first_owned.title()}.")

motorcycles = ["honda", "suzuki", "priora"]
motorcycles.remove("priora") #видаляє елемент з можливістю використання, коли не знаєш його місцезнаходження
print(motorcycles)

# 3.4 Guest list

guest_list = ["pasha", "vova", "vlad"]
cannot_arrive = guest_list.pop(2)
guest_list.insert(0, "vasya")
guest_list.insert(2, "anya")
guest_list.append("dima")
guest_list.append("katya")
guest_list.pop()
guest_list.pop()
guest_list.pop()
guest_list.pop()
del guest_list[1]
del guest_list[0]
print(guest_list)
print(f"{cannot_arrive.title()} will not arrive.")

cars = ["audi", "bmw", "mercedes-Benz", "abarth"]
print("Here is the original list: \n", cars)
print("\nHere is sorted list: \n", sorted(cars)) # сортує список
cars.reverse()
print("\nHere is reversed list: \n", cars)

# 3.8 World traveling

places_original = ["Kyiv", "Paris", "Rome", "Alabama", "Damascus"]
sort_places = sorted(places_original)
reversed_places = sorted(places_original, reverse=True)
places_original.reverse()
places_original.sort()
print(sort_places)
print(reversed_places)
print(places_original)
print(places_original)"""




