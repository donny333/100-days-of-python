from silent_auction_art import logo
import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

print(logo)

auction_over = False
bidders_and_bids = {

}

while not auction_over:
    bidder_name = input("What is your name?\n")
    bid = int(input("What is your bid?\n€"))
    bidders_and_bids[bidder_name] = bid
    last_bid = input("Are there more bidders? Type Y or N:\n")
    clear()
    if last_bid.lower() == 'n':
        auction_over = True

winning_bid = 0
winner = {

}

for key in bidders_and_bids:
    if bidders_and_bids[key] > winning_bid:
        winner = {
            key: bidders_and_bids[key]
        }
        winning_bid = bidders_and_bids[key]

clear()
print(f"Winning bid is {winner[next(iter(winner))]}€. And the winner is {next(iter(winner))}.")