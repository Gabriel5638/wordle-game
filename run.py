"""
Imports the color for the words.
"""

import random
from termcolor import colored

CHANCES = 0
MAX_CHANCES = 5
TRUE_CHECK = False

words = [
    "tiger",
    "beach",
    "flute",
    "eagle",
    "house",
]

random_words = random.choice(words)
splitted_random_word = [*random_words]

print("\n******Title of game******\n")

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
                    # Print the word in red if it is incorrect
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
