import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

throws = [0, 1, 2]
computer_choice = random.randint(0, 2)
player_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper and 2 for Scissors. "))

if player_choice == 0:
    print(rock)
elif player_choice == 1:
    print(paper)
elif player_choice == 2:
    print(scissors)

print("Computer choice:")

if computer_choice == 0:
    print(rock)
elif computer_choice == 1:
    print(paper)
else:
    print(scissors)

if player_choice < 0 or player_choice > 2:
    print("Invalid number. You lose")
elif player_choice == computer_choice:
    print("Its a draw.")
elif player_choice == 0 and computer_choice == 1:
    print("You lose.")
elif player_choice == 0 and computer_choice == 2:
    print("You win.")
elif player_choice == 1 and computer_choice == 0:
    print("You win.")
elif player_choice == 1 and computer_choice == 2:
    print("You lose.")
elif player_choice == 2 and computer_choice == 0:
    print("You lose.")
elif player_choice == 2 and computer_choice == 1:
    print("You win.")