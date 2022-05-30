"""current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1"""

# 7.4 Pizza toppings
"""pizza = []
active_topping = True
prompt = "We are making pizza for you"
prompt += "\nWhat topping do you want? (enough/quit) "

while active_topping:
    topping = input(prompt)
    if topping == 'quit':
        break
    elif topping != 'enough':
        pizza.append(topping)
    elif topping == 'enough':
        print(f"\nOk, here is your pizza with: ")
        for toppings in pizza:
            print(f"\t{toppings}")
        active_topping = False"""

# 7.5 Tickets
"""prompt = "How old are you? "
prompt += "Enter you age: "
active_session = True

while active_session:
    age = int(input(prompt))
    if age < 3:
        print(f"Ticket for {age} years old baby is free)")
    elif age >= 3 and age < 12:
        print(f"Ticket for {age} years old cost 10$)")
    elif age >= 12:
        print(f"Ticket for {age} years old cost 15$)")"""

# confirmed_users.py
# Begin from users which you have to check,
# and empty list confirmed users
"""unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []

# check every user, until unconfirmed users wont end
while unconfirmed_users:
    current_user = unconfirmed_users.pop()

    print(f"Verifying user: {current_user.title()}")
    confirmed_users.append(current_user)

# Show every verifyed user
print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())"""

# pets.py
"""pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)

while 'cat' in pets:
    pets.remove('cat')

print(pets)"""

# mountain_poll.py
"""responses = {}

# boolean variable in definition, what shows process questions
polling_active = True

while polling_active:
    # Ask peoples name and answer
    name = input("\nWhat is your name? ")
    response = input("Which mountain would you like to climb someday? ")

    # Save answer in dictionary
    responses[name] = response

    # Another one person
    repeat = input("Would you like to let another person respond? (yes/no) ")

    if repeat == 'no':
        polling_active = False

# Show result
print("\n--- Poll Results ---")
for name, response in responses.items():
    print(f"{name} would like to climb {response}")"""

# 7.8 Cafe
# Creating list with a sandwiches
"""sandwich_orders = ['lvivsky', 'bavarsky', 'beef sandwich', 'cheese sandwich']

# Creating empty list with finished sandwiches
finished_sandwiches = []

# Going through every sandwich
while sandwich_orders:
    # Pop every sandwich one by one from the end
    ready_sandwich = sandwich_orders.pop()
    
    print(f"I made your {ready_sandwich})")
    
    # Append every sandwich to the empty list
    finished_sandwiches.append(ready_sandwich)

print(f"\nHere is your order: ")

# By cycle For going through every sandwich in the list and print it
for sandwich in finished_sandwiches:
    print(f"\t{sandwich}")"""

# 7.9 No pastrami!
# Creating list with a sandwiches
"""sandwich_orders = ['lvivsky', 'bavarsky', 'pastrami', 'beef sandwich',
                   'pastrami', 'cheese sandwich', 'pastrami']

# Creating empty list with finished sandwiches
finished_sandwiches = []

print("In our cafe there is no sandwiches with pastrami... ")

while 'pastrami' in sandwich_orders:
    no_pastrami = sandwich_orders.remove('pastrami')

while sandwich_orders:
    # Pop every sandwich one by one from the end
    ready_sandwich = sandwich_orders.pop()

    print(f"I made your {ready_sandwich})")

    # Append every sandwich to the empty list
    finished_sandwiches.append(ready_sandwich)

print(f"\nHere is your order: ")

# By cycle For going through every sandwich in the list and print it
for sandwich in finished_sandwiches:
    print(f"\t{sandwich}")"""

# 7.10 Perfect vacation
# Creating dictionary with responses
"""vacation = {}

# Creating variable with boolean type
active_responses = True

# main cycle
while active_responses:
    # Asking peoples name and printing
    name = input("\nWhats your name? ")
    print(f"Hello, {name}!")

    # Asking peoples choice and printing
    prompt = "If you can visit to any place on Earth, where would you go? "
    place = input(prompt)

    # Saving their responses in dictionary
    vacation[name] = place

    # Asking other peoples
    repeat = input("Would you like to let another person respond? (yes/no) ")
    if repeat == 'no':
        active_responses = False

print(f"\n--- Poll results ---")
for name, place in vacation.items():
    print(f"{name} would like to visit {place}")"""
