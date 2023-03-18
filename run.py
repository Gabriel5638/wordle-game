"""
Imports the color,randomizes word list and imports text art for title.
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
    "kempt"
    "quell"
    "roque"
    "phlox"
    "sylph"
    "nymph"
    "pygmy"
    "quate"
    "unapt"
]

LEVELS = {
      "easy": EASY_WORDS,
      "medium": MEDIUM_WORDS,
      "hard": HARD_WORDS,
      "nightmare": NIGHTMARE_WORDS,
}

MAX_CHANCES = 5

def get_word(level):
    word = get_word(level)
    splitt_word = [*word]
    print(text2art("Let's Play Wordle!"))
    print(f"Level: {level}")
    print("Guess a word with 5 letters")
    print("You have 5 chances to guess the correct word")
    chances = 0
    true_check = False

random_words = random.choice(words)
splitted_random_word = [*random_words]

my_art = text2art("Lets Play, Wordle!")
print(my_art)

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
                    # Print the word without color if it is not present
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

# create 3 levels of difficulty.