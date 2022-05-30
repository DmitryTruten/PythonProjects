from random import choice

# 9-6 Ice cream truck
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


class IceCreamStand(Restaurant):
    # modelling ice cream stand

    def __init__(self, restaurant_name, cuisine_type, restaurant_owner):
        # initialize underclass attributes
        super().__init__(restaurant_name, cuisine_type, restaurant_owner)
        self.flavors = ['vanilla', 'strawberry', 'chocolate']

    def print_flavors(self):
        print(f"In our Ice Cream Stand we have next flavors:")
        for flavor in self.flavors:
            print(f"{flavor.title()} flavor")


my_restaurant = IceCreamStand("telezhka", 'morozhka', 'ya')
my_restaurant.print_flavors()"""

# 9-7 Admin
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


class Admin(User):

    # modelling the admin(user with privileges)
    def __init__(self, first_name, last_name, age, avatarka):
        # initialize underclass attributes
        super().__init__(first_name, last_name, age, avatarka)
        self.privileges = Privileges()


class Privileges:
    def __init__(self, privileges=['can add post', 'can delete post', 'can ban default users']):
        self.privileges = privileges

    def show_privileges(self):
        print("Here is admin privileges")
        for privilege in self.privileges:
            print(f"{privilege.title()}")


administrator = Admin('Dimchek', 'Truten', 19, 'himself')
administrator.describe_user()
administrator.privileges.show_privileges()"""

# 9-13 Dices
"""class Dice:
    def __init__(self, sides=6):
        self.sides = sides

    def roll_dice(self):
        print(randint(1, self.sides))


dice = Dice()
for method_call in range(1, 11):
    print(f"The {method_call} roll is:")
    dice.roll_dice()"""


# 9-14 Lottery
class MyLotteryTickets:
    def __init__(self, ticket_list):
        self.ticket_list = ticket_list
        self.my_ticket = []
        self.winner_ticket = []

    def print_winner_ticket(self):
        print(f" Ticket with number {self.ticket_list} is won!")

    def picking_player_ticket(self):
        for number in range(1, 5):
            random_choice = choice(ticket_list)
            self.my_ticket.append(random_choice)

        print(f"Your ticket is {self.my_ticket}")


class WinnerTicket(MyLotteryTickets):
    def __init__(self):
        super().__init__(ticket_list)

    def picking_winner_ticket(self):
        for number in range(1, 6):
            random_choice = choice(ticket_list)
            self.winner_ticket.append(random_choice)
        print(f"Winner ticket is {self.winner_ticket}")

    def picking_player_ticket2(self):
        while self.my_ticket != self.winner_ticket:
            x = input()

            for number in range(1, 5):
                random_choice = choice(ticket_list)
                self.my_ticket.append(random_choice)
            print(f"Your ticket is {self.my_ticket}")

            if self.my_ticket != self.winner_ticket:
                for number1 in range(1, 5):
                    self.my_ticket.pop()
            elif 'a' in self.my_ticket:
                self.print_winner_ticket()


ticket_list = ['a', 'b', 'c',
               '1', '2', '3', '4', '5',
               '6', '7', '8', '9', '10']

tickets = MyLotteryTickets(ticket_list)
winner_tickets = WinnerTicket()
winner_tickets.picking_winner_ticket()
winner_tickets.picking_player_ticket2()
