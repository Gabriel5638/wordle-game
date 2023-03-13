import random
from termcolor import colored
chances = 0
max_chances = 5
true_check = False

words = [
            "cat",
            "dog",
            "rat",
            "hat",
            "mat",
    ]

random_words = random.choice(words)
splitted_random_word = ([*random_words])

   print("/n******Title of game******\n")

while chances < max_chances and not true_check:

        user_input = input("Guess: ")
        splitted_input = ([*user_input])
        true_check_counter = 0
         if len(splitted_input) > 5 or len(splitted_input) < 5:
     print("Please enter a word with only 5 letters ")

        else:

       for i in range(len(splitted_input)):
           if i != len(splitted_input) - 1:
           if splitted_input[i] == splitted_random_word[i]:
      # Print the word in green if it is correct
     print(colored(splitted_input[i], 'green'), end=" ")
    true_check_counter += 1
        elif splitted_input[i] in splitted_random_word:
    # Print the word in red if it is incorrect
     print(colored(splitted_input[i], 'red'), end=" ")
         else:
     # Print the word without color if it is not present in the generated word
     print(splitted_input[i], end=" ")
         else:
          if splitted_input[i] == splitted_random_word[i]:
     print(colored(splitted_input[i], 'green'))
        true_check_counter += 1
         elif splitted_input[i] in splitted_random_word:
        print(colored(splitted_input[i], 'red'))
          else:
         print(splitted_input[i])

          if true_check_counter < 4:
    pass
    else:
    true_check = True 
            
      chances += 1 
    

    if true_check:
         print("You guessed the word!")
    else: 
          print("You couldn't guess the correct word! It was", random_words)