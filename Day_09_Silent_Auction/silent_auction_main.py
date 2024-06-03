from silent_auction_art import logo
import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

print(logo)