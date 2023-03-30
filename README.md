# Wordle

Wordle is a fun and challenging word-guessing game that will test your vocabulary and deduction skills. The game randomly selects a five-letter word, and you have ten attempts to guess the word correctly. Each time you make a guess, the game will give you hints in the form of colored letters: green letters are in the correct position, and red letters are correct but in the wrong position. Using these clues, you must try to guess the correct word before your ten attempts run out. With a sleek design and user-friendly interface, Wordle is the perfect game for anyone who loves puzzles and word games.

This game was created using Python programming language, and the code was executed in the command terminal. It's a great way to improve your vocabulary and guessing skills while having fun.

The live site can be found here: [Wordle](https://wordle-game-5638.herokuapp.com/)

# Table of Contents

- [User Experience](#user-experience)
- [Features](#features)
- [Design](#design)
- [Inspiration](#inspiration)
- [Technologies](#technologies-used)
- [Testing](#testing)
- [Deployment](#deployment)
- [Credits](#credits)

# User Experience

## User Story

As a user,
- I would like to be able to interact with the game.
- I would like to have a range of words to guess from.
- I would like the rules to be clearly presented to me.
- I would like to be able to replay the game.
- I would like the game to be fun and challenging.

# Features
## Title
![Title](readme-images/wordle-ascii.PNG)

The title screen of the game uses a special kind of text art called ASCII art to display the name of the game in a creative and eye-catching way. 
It is a unique feature that adds a fun and playful element to the overall design of the game.



## Rules section
![Rules-section](readme-images/rules.PNG)

In the rules section, players can find detailed instructions on how to play the game, including the objective, how to make guesses, and how to interpret the feedback provided after each guess. Additionally, the rules outline the limitations of the game, such as the maximum number of guesses allowed and the fact that only five-letter words can be used in the game. The section is designed to provide players with all the information they need to play the game successfully and enjoyably.

## User Interaction
![Guesses](readme-images/guess.PNG)

In Wordle, the user interacts with the game by inputting their guesses and receiving feedback on the correctness of their guess. The user has ten attempts to guess a hidden five-letter word. Each time the user inputs a guess, the game displays the letters that are correct and in the correct position with green letters, and the letters that are correct but in the wrong position with red letters. The user can continue to input guesses until they correctly guess the hidden word or run out of attempts.

## Warning
![Warning](readme-images/warning.PNG)

If the user enters a word with more or less than 5 letters, a message will appear informing the user that only words with 5 letters give hints.
The warning serves as a crucial component of the game design as it reinforces the rules and expectations of the game. It also helps to prevent frustration on the part of the user, as they may become confused or discouraged if they are not informed of why their word was not accepted. Additionally, displaying a clear and concise error message helps to create a more user-friendly experience and improves the overall flow of the game. Overall, the word warning is an essential aspect of the game design that ensures the user can enjoy the game to its fullest potential.

## End Game Prompt
![End](readme-images/prompt.PNG)

After the user runs out of attempts, the game will display a message informing them that they have lost and revealing the hidden word. The user will then be prompted to play again. If the user correctly guesses the hidden word, a message will display congratulating them on their victory and prompting them to play again.


# Design

The design for this game is centered around a simple, yet engaging user experience. The title screen features the name of the game in ASCII text art and a prompt to enter a 5-letter word. Once the game starts, the user is presented with a series of prompts to enter their guesses, with each guess providing feedback on the correctness of the answer. The game mechanics are easy to understand and provide a satisfying challenge for players of all skill levels.

To enhance the user experience, the game features a clean and minimalist design. The colors and typography are carefully chosen to be visually pleasing and easy on the eyes.The end game prompt is designed to be unobtrusive, prompting the user to play again without interrupting the flow of the game.

Overall, the design for this game was focused on providing a fun and challenging experience for users while keeping the user interface simple and intuitive. The result is a game that is both engaging and easy to play, with a design that is both visually appealing and functional.

## Inspiration
This game was inspired by the original wordle game.
The original version was created by Jonathan Feinberg, a software engineer, in 2008. In 2013, Feinberg sold the rights to the game to The New York Times, which launched an online version of the game in 2018. The game quickly became popular, with players around the world trying to guess the secret word with the fewest possible attempts.

The Wordle game has since inspired many similar games and variations, including the version that allows for six attempts and includes a scoring system. This version has gained popularity on social media platforms such as Twitter, where users can share their attempts and scores with their followers. The game's simple yet challenging concept and easy-to-use interface have made it a popular pastime for people of all ages and backgrounds.

## Graphics

The game's graphical limitations stem from its terminal-based design. However, in order to enhance the user experience, ASCII art has been incorporated using the Text 2 Art library.The Termcolor library was also utilized to add visual emphasis to the usable letters in the game.




## Flowchart
<details>
<summary>Game Flowchart, this was the first idea of how the game would work, ended up changing some small things along the way</summary>

![Flowchart](readme-images/flowchart.PNG)
</details>

# Technologies Used

- [Python](https://en.wikipedia.org/wiki/Python_(programming_language)): programming language.
  - Libraries:
    - Random:  A built-in Python library used for generating random numbers and sequences, which was used in this project to select a random word from the list of available words.
    - Os:  Another built-in Python library used for interacting with the operating system. In this project, os was used to clear the terminal screen when the game started.
    - Termcolor:  A Python library for ANSI color formatting of text output. This was used to highlight the usable letters in the guessing system.
    - Art:  A Python library used for creating ASCII art from text strings. In this project, art was used to display the game title in ASCII art.
    - Words_list:  A custom module created for this project that contains a list of five-letter words used in the game.
# Testing

## [PEP8 online check](https://pep8ci.herokuapp.com/)
   ![pep8](readme-images/pep8.PNG)
   ![wordspep](readme-images/pep8-words.PNG)



## Testing Functionality
 The game was tested throughout production when each new function was created. Following deployment, the game was replayed multiple times to see if it had any bugs.
The objective of this test is to ensure that the Wordle game functions as expected and meets the specified requirements.

![Tests](readme-images/tests.PNG)



## Fixed Bugs
- None
## Known Bugs

- None

# Deployment

## Steps to deploy site using Heroku:
- On the Heroku dashboard, select "New" and click "Create new app"
  - Create a unique app name
  - Select your region
  - Click "Create app"
- Go to the settings tab:
  - Scroll down to the config vars section and select "Reveal Config Vars"
  - Add necessary config vars
  - In this case, in the key field enter "PORT" and the value field enter "8000"
  - Click "Add"
  - Scroll down to Buildpacks and click "Add buildpack"
  - Add the necessary buildpacks.
  - In this case, select "python" and click "Save changes"
  - Then, select "node.js" and click "Save changes"
- Go to the Deploy tab:
  - Select GitHub and confirm connection to GitHub account
  - Search for the repository and click "Connect"
  - Scroll down to the deploy options
  - Select automatic deploys if you would like automatic deployment with each new push to the GitHub repository
  - In manual deploy, select which branch to deploy and click "Deploy Branch"
  - Heroku will start building the app
- The link to the app can be found at the top of the page by clicking "Open app"

The live site can be found here: (https://wordle-game-5638.herokuapp.com/)

## Steps to clone site:
- In the GitHub repository, click the "Code" button.
- Select "HTTPS" and copy the URL.
- Open Git Bash and navigate to the repository where you would like to locate the cloned repository.
- Type "git clone" followed by the copied URL.
- Press enter to create the clone.

# Credits
- The code and how I built the game flow itself, was inspired by this [youtube video](https://www.youtube.com/watch?v=04WgY32Nam4)
- The code commenting and the way the code is laid out were done with the help of my mentor.
- The rules were inspired by the original [wordle game](https://www.nytimes.com/games/wordle/index.html)
- This [website](https://www.scaler.com/topics/python/indentation-in-python/) provided me with a much better understanding of indentation.
- This [video](https://www.youtube.com/watch?v=I269TjuEVQA) helped me understand loops.
# Acknowledgements
I am sincerely thankful to my mentor, Marcel, for the information and advice he has provided me, which have been instrumental in my progress and development.