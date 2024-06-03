import random as ran
import hangman_art
import hangman_words
word_list = hangman_words.word_list

random_word_indent = ran.randint(0, len(word_list) - 1)
chosen_word = word_list[random_word_indent]

blank_letters = []

for letter in chosen_word:
    blank_letters += "_"

lives = 7

print(hangman_art.logo)
print(f"Hey, the answer is {chosen_word}")

guessed_letters = []

while "_" in blank_letters and lives > 0:
    print("".join(blank_letters))
    user_guess = input("Guess a letter: ").lower()
    if len(user_guess) > 1:
        print("You should guess only one letter.")
    elif user_guess in chosen_word:
        for i in range( 0, len(chosen_word)):
            if user_guess == chosen_word[i]:
                blank_letters[i] = user_guess
    elif user_guess in guessed_letters:
        print(f'You already guessed letter "{user_guess}"')
    else:
        lives -= 1
        print(hangman_art.stages[lives])
        guessed_letters += user_guess

if lives > 0:
    print("".join(blank_letters))
    print("You win!")
else:
    print("You lose!")