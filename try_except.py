"""try:
    print(5/0)
except ZeroDivisionError:
    print('You can\'t divide by zero! ')"""

# division_calculator.py
"""print("Give me two numbers, and i'll divide them.")
print("Enter 'q' to quit.")

while True:
    first_number = input("\n First number: ")
    if first_number == 'q':
        break
    second_number = input("Second number: ")
    if second_number == 'q':
        break
    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print("You can't divide by zero!")
    else:
        print(answer)"""

# 10-6 Adding
"""print("Enter two numbers")
while True:
    try:
        first = int(input("First number: "))
        second = int(input("Second number: "))
        result = first + second
        print(f"{first} + {second} = {result}\n")

    except ValueError:
        print("Enter number, not a string...\n")"""

"""filename1, filename2 = 'cats.txt', 'dogs.txt'

try:
    with open(filename1) as f1:
        print("(Cats.txt)")
        for line in f1:
            print(f"{line.rstrip()}")

    print("\n(Dogs.txt)")
    with open(filename2) as f2:

        for line in f2:
            print(f"{line.rstrip()}")

except FileNotFoundError:
    pass"""

# 10-11 Favorite number
import json


def save_number():
    number = input("Enter number: ")
    filename = 'favorite_number.json'

    with open(filename, 'w') as f:
        json.dump(number, f)
        print(f"Your number {number} has saved.")


def get_number():
    filename = 'favorite_number.json'
    try:
        with open(filename) as f:
            number = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return number


def print_number():
    number = get_number()
    if number:
        print(f"Your number is {number}.")
    else:
        number = save_number()
        print(f"We remember your number {number}")


get_number()
