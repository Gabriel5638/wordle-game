"""
Imports the color for the words and randomizes word list
"""

import random
import os
from termcolor import colored
from art import text2art
from words_list import five_words as words


def welcome():
    """Welcome method with artwork"""
    my_art = text2art("Wordle")
    print(my_art)


def instructions():
    """Method to print instrictions"""
    print("Please enter a 5-letter word")
    print("To guess the random hidden word!\n")
    print("Entering more than 5 letter words still counts as a guess.")
    print("Careful words with more or less than 5 letters don't show hints.\n")
    print("Green letters are in the correct placement.")
    print("Red letters are also correct but in the wrong placement.")
    print("You have 10 attempts, good luck.")


def game():
    """Method for the game loop"""
    play_again = 'y'
    while play_again.lower() == 'y':
        os.system('cls' if os.name == 'nt' else 'clear')
        welcome()
        instructions()
        result = main()
        if result[0]:
            print("You guessed the word!")
        else:
            print("You couldn't guess the correct word! It was:")
            print(result[1])

        play_again = input("Do you want to play again? (y/n): ")

    print("Thank you for playing!")


def main():
    """Method to hold the main game functionality"""
    max_chances = 10
    random_word = random.choice(words)
    for _ in range(max_chances):
        user_input = input("Guess: ")
        if len(user_input) != 5:
            print(" Only 5 letter words give hints!")
            continue

        true_check_counter = 0
        color_dict = {}
        for i, letter in enumerate(user_input):
            if letter == random_word[i]:
                color_dict[i] = 'green'
                true_check_counter += 1
            elif letter in random_word:
                color_dict[i] = 'red'
            else:
                color_dict[i] = 'white'

        colored_output = [
            colored(letter, color_dict.get(i, 'white'))
            for i, letter in enumerate(user_input)
        ]
        print('| ' + ' '.join(colored_output) + ' |')

        if true_check_counter == 5:
            return True, random_word

    return False, random_word


game()
