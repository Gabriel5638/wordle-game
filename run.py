"""
Imports the color for the words and randomizes word list
"""

import random
import os
from termcolor import colored
from art import text2art
from words_list import five_words as words


CHANCES = 0
MAX_CHANCES = 5
TRUE_CHECK = False

random_words = random.choice(words)
splitted_random_word = [*random_words]


def welcome():
    """Welcome method with artwork"""
    my_art = text2art("Lets Play, Wordle!")
    print(my_art)


def instructions():
    """Method to print instrictions"""
    print("Instructions here")


def game():
    """Method for the game loop"""
    welcome()

    while True:
        instructions()
        main()
        play_again = input("Do you want to play again? (y/n): ")
        if play_again.lower() == "y":
            # Reset game variables
            CHANCES = 0
            MAX_CHANCES = 5
            TRUE_CHECK = False
            TRUE_CHECK_COUNTER = 0
            CHANCES += 1

            # Clear the console screen
            os.system('clear')
            # Continue back to show the instructions
            continue

        print("Thanks for playing!")
        break


def main():
    """Method to hold the main gme functionality"""
    global CHANCES
    global TRUE_CHECK
    while CHANCES < MAX_CHANCES and not TRUE_CHECK:
        user_input = input("Guess: ")
        splitted_input = [*user_input]
        TRUE_CHECK_COUNTER = 0

        if len(splitted_input) > 5 or len(splitted_input) < 5:
            print("Please enter a word with only 5 letters ")
        else:
            for i, word in enumerate(splitted_input):
                if i != len(splitted_input) - 1:
                    if word == splitted_random_word[i]:
                        # Print the word in green if it is correct
                        print(colored(word, 'green'), end=" ")
                        TRUE_CHECK_COUNTER += 1
                    elif word in splitted_random_word:
                        # Print the letter color if letter is correct
                        print(colored(word, 'red'), end=" ")
                    else:
                        # Print the word white color if it is not present
                        print(word, end=" ")
                else:
                    if word == splitted_random_word[i]:
                        print(colored(word, 'green'))
                        TRUE_CHECK_COUNTER += 1
                    elif word in splitted_random_word:
                        print(colored(word, 'red'))
                    else:
                        print(word)

            if TRUE_CHECK_COUNTER < 4:
                pass
            else:
                TRUE_CHECK = True

        CHANCES += 1

    if TRUE_CHECK:
        print("You guessed the word!")
    else:
        print("You couldn't guess the correct word! It was", random_words)


if __name__ == "__main__":
    game()
