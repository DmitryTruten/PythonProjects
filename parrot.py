# parrot.py
"""prompt = "\nTell me something and i will repeat it back to you: "
prompt += "\nEnter 'quit' to end the program. "

active = True
while active:
    message = input(prompt)

    while message != 'quit':
        if message != 'quit':
            print(message)"""

# cities.py
"""prompt = "\nPlease enter a city you have visited: "
prompt += "\nEnter 'quit' when you are finished. "

while True:
    city = input(prompt)

    if city == 'quit':
        break
    else:
        print(f"I'd love to go to {city.title()}")"""

# counting.py
current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue

    print(current_number)

