# Generate random number from 1 to 100
# Set difficulty of the game
# Set how many attempts user has
# Create a loop and quit if: there are no attempts left or number is guessed
# Write a conclusion if player won or lost

import random
import art

logo = art.logo

def guess_meter(correct_answer, usr_guess):
    if usr_guess > correct_answer:
        print("Too high!")
    elif usr_guess < correct_answer:
        print("Too low!")


answer = random.randint(1, 100)
attempts = 10

print(logo)

level_choice = input("Choose a difficulty. Type 'easy' or 'hard': ")
if level_choice == 'hard':
    attempts = 5

answer_is_correct = False

while attempts > 0 and not answer_is_correct:
    if attempts > 1:
        print(f"You have {attempts} attempts remaining to guess the number.")
    else:
        print(f"You have {attempts} attempt remaining to guess the number.")

    user_guess = int(input("Make a guess: "))
    if user_guess == answer:
        answer_is_correct = True
    else:
        attempts -= 1
        guess_meter(answer, user_guess)

if attempts > 0:
    print(f"You got it! The answer was {answer}.")
else:
    print("You've run out of guesses.")