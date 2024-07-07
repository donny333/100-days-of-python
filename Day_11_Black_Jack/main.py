import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
players_cards = []
computers_cards = []

def draw_a_card():
    card_index = random.randint(0, len(cards) - 1)
    return cards[card_index]





print(f"First card: {draw_a_card()}, second card: {draw_a_card()}")

