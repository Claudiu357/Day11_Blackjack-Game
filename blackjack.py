from art import logo
import random
cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 11]
game_running = True
print(logo)

def deal_cards():
    player_cards = []
    card = random.choice(cards)
    if card == 1:
        card = 11
    player_cards.append(card)
    card = random.choice(cards)
    if card == 1:
        card = 11
    player_cards.append(card)
    return player_cards


def calculate_score(someone_cards):
    score = 0
    for card in someone_cards:
        if card == 1:
            someone_cards[card] = 11
            card = 11
        score = score + card
    return score


user_cards = deal_cards()
computer_cards = deal_cards()
print(f"Your cards is:{user_cards}")
print(f"Computer first card is: [{computer_cards[0]},_]")
while game_running:
    choice = input("You want to hint another card? Type y or n ")
    if choice == "n":
        while calculate_score(computer_cards) <= calculate_score(user_cards):
            computer_cards.append(random.choice(cards))
        if calculate_score(computer_cards) == 21:
            print(f"Computer cards is:{computer_cards} you lose")
        elif calculate_score(user_cards) < calculate_score(computer_cards) < 21:
            print(f"Computer cards is:{computer_cards} you lose")
        elif calculate_score(user_cards) == calculate_score(computer_cards):
            print(f"Draw computer cards is: {computer_cards}")
        else:
            print(f"Computer cards is:{computer_cards} you win")
        game_running = False
    else:
        user_cards.append(random.choice(cards))
        print(f"Your cards is:{user_cards}")
        if calculate_score(user_cards) == 21:
            print("User win")
            game_running = False
        if calculate_score(user_cards) > 21:
            print("User lose")
            game_running = False
