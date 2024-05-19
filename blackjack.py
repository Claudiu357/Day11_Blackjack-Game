from art import logo
import random
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10]
game_running = True
print(logo)


def deal_cards():
    player_cards = []
    card = random.choice(cards)
    player_cards.append(card)
    card = random.choice(cards)
    player_cards.append(card)
    return player_cards


def calculate_score(someone_cards):
    score = 0
    for card in someone_cards:
        score = score + card
    return score


user_cards = deal_cards()
computer_cards = deal_cards()
print(f"Your cards is:{user_cards}")
print(f"Computer first card is: [{computer_cards[0]},_]")
if calculate_score(user_cards) == 21:
    print("User wins")
    game_running = False
while game_running:
        choice = input("You want to hint another card? Type y or n ")
        if choice == "n":
            while calculate_score(computer_cards) <= calculate_score(user_cards):
                new_card = random.choice(cards)
                if new_card == 11 and calculate_score(computer_cards) + 11 > 21:
                    new_card = 1
                computer_cards.append(new_card)
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
            new_card = random.choice(cards)
            if new_card == 11 and calculate_score(user_cards) + new_card > 21:
                new_card = 1
            user_cards.append(new_card)
            print(f"Your cards is:{user_cards}")
            if calculate_score(user_cards) == 21:
                print("User win")
                game_running = False
            if calculate_score(user_cards) > 21:
                print("User lose")
                game_running = False
