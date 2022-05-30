"""magicians = ["alice", "david", "carolina"]
for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")
    print(f"I can't wait to see your next trick, {magician.title()}.\n")

# 4.1 Pizza's
kind_of_pizza = ["Margarita", "Verona", "Four cheese"]
for pizza in kind_of_pizza:
    print(f"I like {pizza.lower()} pizza!)")
print("\nI really love pizza!")

for value in range(1, 5):
    print(value, "\n")
numbers = list(range(2, 11, 2))
print (numbers)

squares = []
for value in range(1, 11):
    squares.append(value**2)
print(squares)

squares_generator_list = [value**2 for value in range(1, 11)]
print("\n", squares_generator_list)

# 4.3 Counting to 20
for numbers in range(1, 21):
    print(numbers)

# 4.4 Hundred
numbers = list(range(1, 101))
for number in numbers:
    print(number)

# 4.5 Sum hundred
list_of_numbers = []
for value in range(1, 101):
    list_of_numbers.append(value)
print(list_of_numbers)
print("\n", min(list_of_numbers))
print(max(list_of_numbers))
print(sum(list_of_numbers))

# 4.6 Odd numbers
for value in range(1, 21, 2):
    print(value)

# 4.7 Threes
list_of_threes = []
for threes in range(3, 31, 3):
    list_of_threes.append(threes)
print(list_of_threes)

# 4.8 Cubes
list_of_cubes = []
for cubes in range(1, 11):
    list_of_cubes.append(cubes ** 3)
print(list_of_cubes)

#4.9 Cubes generator list
cubes = [number ** 3 for number in range(1, 11)]
print(cubes)

players = ['charles', 'martina', 'michael', 'florence', 'eli']
print("Here are players on my team: ")
for player in players[:3]:
    print(player.title())

my_foods = ['pizza', 'falafel', 'carrot cake']
friends_food = my_foods[:]
my_foods.append('shaurma')
print(my_foods)
print(friends_food)

# 4.10 Slices
list_of_cubes = []
for cubes in range(1, 11):
    list_of_cubes.append(cubes ** 3)
print(list_of_cubes)
print(f"The first three item in the list are: \n{list_of_cubes[:3]}")
print(f"Three item in the middle of the list are: \n{list_of_cubes[4:7]}")
print(f"The last three items of the list are: \n{list_of_cubes[-3:]}")

# 4.11 My pizza/Your pizza
my_pizzas = ["Margarita", "Verona", "Four cheese"]
friend_pizzas = my_pizzas[:]
my_pizzas.append("Pepperoni")
friend_pizzas.append("Polo")

print(f"My favorite pizzas are: ")
for pizza in my_pizzas:
    print("\t", pizza)

print(f"\nMy friends favorite pizzas are: ")
for pizza in friend_pizzas:
    print("\t", pizza)

numbers = []
for number in range(1, 21):
    numbers.append(number)
    print(number)"""

my_pizzas = ["Margarita", "Verona", "Four cheese"]
for pizza in my_pizzas:
    print(my_pizzas)


