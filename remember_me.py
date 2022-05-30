"""import json

username = input("What is your name? ")

filename = 'username.json'
with open(filename, 'w') as f:
    json.dump(username, f)
    print(f"We will remember you, {username})")"""

import json

"""Load username if it already saved
Otherwise ask username and save it"""


def get_stored_username():
    """Get username if it exists"""
    filename = 'username.json'
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username


def get_new_username():
    """Ask username"""
    username = input("What is your name? ")
    filename = 'username.json'
    with open(filename, 'w') as f:
        json.dump(username.title(), f)

    return username


def greet_user():
    """Greet user by name"""
    username = get_stored_username()
    question = f"Is your name - {username}? (yes/no) "
    answer = input(question)

    if answer == 'yes':
        print(f"Welcome back, {username}")

    else:
        username = get_new_username()
        print(f"We will remember you, {username}")


greet_user()
