from silent_auction_art import logo
import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(logo)

clear()

auction_over = False
bidders_and_bids = {

}

while not auction_over:
    bidder_name = input("What is your name?\n")
    bid = int(input("What is your bid?\n"))
    bidders_and_bids[bidder_name] = bid
    last_bid = input("Are there more bidders? Type Y or N:\n")
    if last_bid.lower() == 'n':
        auction_over = True
    clear()
    print(bidders_and_bids)

