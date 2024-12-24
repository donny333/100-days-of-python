import random
import art


cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def draw_a_card():
    card_index = random.randint(0, len(cards) - 1)
    return cards[card_index]


def tot_score(hand):
    score = sum(hand)
    alternative_hand = []
    if score == 21 and len(hand) == 2:
        return 0
    if score > 21 and 11 in hand:
        for i in hand:
            if i == 11:
                alternative_hand.append(1)
            else:
                alternative_hand.append(i)

    if len(alternative_hand) == 0:
        return score
    else:
        return sum(alternative_hand)


def game_info(player_hand, computer_hand):
    print(f"    Your cards: {player_hand}, current score: {sum(player_hand)}")
    print(f"    Computer's first card: {computer_hand[0]}")


def game_final_info(player_hand, computer_hand):
    print(f"    Your final hand: {player_hand}, final score: {tot_score(player_hand)}")
    print(f"    Computer's final hand: {computer_hand}, final score: {tot_score(computer_hand)}")


def game_winnings(player_hand, computer_hand):
    if tot_score(player_hand) == tot_score(computer_hand):
        print("It's a draw 😃")
    elif tot_score(player_hand) == 0:
        print("You got BlackJack. You win 😃")
    elif tot_score(computer_hand) == 0:
        print("Computer got BlackJack. You lose 😭")
    elif tot_score(player_hand) > 21:
        print("You went over. You lose 😭")
    elif tot_score(computer_hand) > 21:
        print("Computer went over. You win 😃")
    elif tot_score(player_hand) > tot_score(computer_hand):
        print("You win 😃")
    elif tot_score(player_hand) < tot_score(computer_hand):
        print("You lost the game 😭")


def game():
    print(art.logo)
    player_hand = [draw_a_card(), draw_a_card()]
    computer_hand = [draw_a_card(), draw_a_card()]

    hit = True
    if tot_score(player_hand) == 0:
        hit = False

    while hit:
        game_info(player_hand, computer_hand)
        another_card = input("Type 'y' to get another card, type 'n' to pass: ")
        if another_card == 'n':
            hit = False
        else:
            player_hand.append(draw_a_card())
        if tot_score(player_hand) > 21:
            hit = False

    does_computer_play = False
    if tot_score(player_hand) < 22:
        does_computer_play = True

    while does_computer_play:
        if tot_score(computer_hand) < 18:
            computer_hand.append(draw_a_card())
        else:
            does_computer_play = False

    game_final_info(player_hand, computer_hand)
    game_winnings(player_hand, computer_hand)


game_on = True
while game_on:
    want_to_play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    if want_to_play != 'y':
        game_on = False
    else:
        print("\n" * 20)
        game()