"""
Imports the color for the words and randomizes word list
"""
import random
from termcolor import colored
from art import text2art


def play_wordle():
    """
    Plays a game of Wordle, with 5 max chances.
    """
    chances = 0
    max_chances = 5
    words = [
        "tiger",
        "beach",
        "flute",
        "judge",
        "eagle",
        "house",
        "snake",
        "rural",
        "fable",
        "cable",
        "label",
        "dance",
        "watch",
        "zebra",
        "yacht",
    ]
    random_word = random.choice(words)
    art = text2art("Let's Play, Wordle!")
    print(art)

    while chances < max_chances:
        guess = input("Guess: ")
        if len(guess) != 5:
            print("Please enter a word with only 5 letters ")
            continue

        # Check if the guess is correct
        correct = [g == w for g, w in zip(guess, random_word)]
        if all(correct):
            print("You guessed the word!")
            break

        # Print the result of the guess
        for i, letter in enumerate(guess):
            if correct[i]:
                print(colored(letter, "green"), end=" ")
            elif letter in random_word:
                print(colored(letter, "red"), end=" ")
            else:
                print(letter, end=" ")
        print()

        chances += 1

    if chances >= max_chances:
        print("You couldn't guess the correct word! It was", random_word)

    play_again = input("Do you want to play again? (y/n)").lower()
    if play_again == "y":
        play_wordle()
    else:
        print("Thanks for playing Wordle!")
