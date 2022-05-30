import random

player_in_game = True
dealer_in_game = True

# creating whole card deck
card_deck = [2, 3, 4, 5, 6, 7, 8, 9, 10,
             2, 3, 4, 5, 6, 7, 8, 9, 10,
             2, 3, 4, 5, 6, 7, 8, 9, 10,
             2, 3, 4, 5, 6, 7, 8, 9, 10,
             "J", "Q", "K", "A",
             "J", "Q", "K", "A",
             "J", "Q", "K", "A",
             "J", "Q", "K", "A"]

# creating players and dealers hand
player_hand = []
dealer_hand = []


# deal the cards
def deal_the_cards(turn):
    card = random.choice(card_deck)
    turn.append(card)
    card_deck.remove(card)


# calculate the total of each hand
def total(turn):
    total_score = 0
    face = ["J", "Q", "K", "A"]
    for card in turn:
        if card in range(1, 11):
            total_score += card
        elif card in face:
            total_score += 10
        else:
            if total_score > 11:
                total_score += 1
            else:
                total_score += 11
    return total_score


# checking for winner
def open_dealers_hand():
    if len(dealer_hand) == 2:
        return dealer_hand[0]
    elif len(dealer_hand) > 2:
        return dealer_hand[0], dealer_hand[1]


# main loop
for _ in range(2):
    deal_the_cards(dealer_hand)
    deal_the_cards(player_hand)

while player_in_game or dealer_in_game:
    print(f"Dealer has {open_dealers_hand()} and X")
    print(f"You have {player_hand} for a total of {total(player_hand)}")

    if player_in_game:
        hit_or_stay = input("1: Hit\n2: Stay\n")
    if total(dealer_hand) > 16:
        dealer_in_game = False
    else:
        deal_the_cards(dealer_hand)
    if hit_or_stay == '1':
        deal_the_cards(player_hand)
    else:
        player_in_game = False
    if total(player_hand) >= 21:
        break
    elif total(dealer_hand) >= 21:
        break

if total(player_hand) == 21:
    print(f"\nYou\'ve got {total(player_hand)} points "
          f"and dealer have {total(dealer_hand)} points\nBlackJack! You wins!")
elif total(dealer_hand) == 21:
    print(f"\nYou\'ve got {total(player_hand)} points "
          f"and dealer have {total(dealer_hand)} points\nBlackJack! Dealer wins!")
elif total(player_hand) > 21:
    print(f"\nYou\'ve got {total(player_hand)} points "
          f"and dealer have {total(dealer_hand)} points\nYou have hit too much. Dealer wins!")
elif total(dealer_hand) > 21:
    print(f"\nYou\'ve got {total(player_hand)} points "
          f"and dealer have {total(dealer_hand)} points\nDealer hit too much. You wins!")
elif total(player_hand) > 21 and total(dealer_hand) > 21:
    print(f"\nYou\'ve got {total(player_hand)} points "
          f"and dealer have {total(dealer_hand)} points\nBoth hit too much. Draw!")
elif 21 - total(dealer_hand) < 21 - total(player_hand):
    print(f"\nYou\'ve got {total(player_hand)} points "
          f"and dealer have {total(dealer_hand)} points\nDealer got more points than you. Dealer wins!")
elif 21 - total(dealer_hand) > 21 - total(player_hand):
    print(f"\nYou\'ve got {total(player_hand)} points "
          f"and dealer have {total(dealer_hand)} points\nYou have got more points than dealer. You wins!")
