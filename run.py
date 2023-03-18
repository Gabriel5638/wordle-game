"""
Imports the color, randomizes word list and imports text art for title.
"""

import random
from termcolor import colored
from art import text2art

EASY_WORDS = [
    "tiger",
    "beach",
    "judge",
    "eagle",
    "house",
    "snake",
    "rural",
    "fable",
    "cable",
    "label",
    "dance",
]

MEDIUM_WORDS = [ 
    "grape",
    "blitz",
    "staff",
    "patio",
    "fjord",
    "maple",
    "funny",
    "crypt",
    "pixel",
    "watch",
    "zebra",
    "yacht",
]

HARD_WORDS = [
    "nixie",
    "quick",
    "pizza",
    "juked",
    "zinky",
    "xerus",
    "xenon",
    "whiff",
    "wreck",
    "vizor",
    "venom",
    "vexed",
    "vivid",
]

NIGHTMARE_WORDS = [
    "kempt",
    "quell",
    "roque",
    "phlox",
    "sylph",
    "nymph",
    "pygmy",
    "quate",
    "unapt",
]

LEVELS = {
    "easy": EASY_WORDS,
    "medium": MEDIUM_WORDS,
    "hard": HARD_WORDS,
    "nightmare": NIGHTMARE_WORDS,
}

MAX_CHANCES = 5


def get_word(level):
    words = LEVELS[level]
    word = random.choice(words)
    splitted_word = [*word]
    return splitted_word


def play_wordle(level):
    splitted_word = get_word(level)
    print(text2art("Let's Play Wordle!"))
    print(f"Level: {level}")
    print("Guess a word with 5 letters")
    print("You have 5 chances to guess the correct word")
    chances = 0
    true_check = False

    while chances < MAX_CHANCES and not true_check:
        user_input = input("Guess: ")
        splitted_input = [*user_input]
        true_check_counter = 0

        if len(splitted_input) != 5:
            print("Please enter a word with exactly 5 letters ")
        else:
            for i, letter in enumerate(splitted_input):
                if letter == splitted_word[i]:
                    print(colored(letter, 'green'), end=" ")
                    true_check_counter += 1
                elif letter in splitted_word:
                    print(colored(letter, 'red'), end=" ")
                else:
                    print(letter, end=" ")
            print("")

            if true_check_counter == 5:
                true_check = True

            chances += 1

    if true_check:
        print("You guessed the word!")
    else:
        print("You could not guess the word! it was", ''.join(splitted_word))

def play_nightmare_wordle():
    play_wordle("nightmare")


play_nightmare_wordle()
