
# TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
# TODO-1: - Create an empty List called display.
# For each letter in the chosen_word, add a "_" to 'display'.


# TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
# TODO-2: - Loop through each position in the chosen_word;
# If the letter at that position matches 'guess' then reveal that letter in the display at that position.


# TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
# TODO-3 - Print 'display' & see the guessed letter in the correct position and every other letter replace with "_".
# Hint - Don't worry about getting the user to guess the next letter. We'll tackle that in step 3.

# TODO-4 - While loop guess again. Stop loop when user guess all letters in chosen_word & 'display' has no ("_").
#  Then you can tell the user they've won.

import random
from hangman_art import stages, logo
from hangman_words import word_list

chosen_word = random.choice(word_list)
word_length = len(chosen_word)
game_over = False
lives = len(stages) - 1

print(f"Solution is {chosen_word}.")
print(logo)

# Creating blanks
display = []
for _ in range(word_length):
    display.append("_")
# print(f"{' '.join(display)}")

already_guessed = ""


while not game_over:
    guess = input("Guess a letter: ").lower()
    # Checking if letter has been already guessed
    if guess not in already_guessed:
        for position in range(word_length):
            letter = chosen_word[position]
            # print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
            if letter in guess:  # if letter == guess:
                display[position] = guess

        # print(f"{' '.join(display)}")

        if guess not in chosen_word:
            print(f"You guessed {guess}, that's not in the word. You lose a life.")
            lives -= 1
            if lives == 0:
                game_over = True
                print("You lose.")
        already_guessed += guess
    else:
        print(f"You've already guessed {guess}")

    print(f"{' '.join(display)}")

    if "_" not in display:
        game_over = True
        print("You win!")

    print(stages[lives])
