
# 📘 Assignment: Hangman Game Challenge

## 🎯 Objective

Build a simple Hangman game in Python. In this assignment, you will practice using strings, loops, conditionals, and user input to create an interactive word-guessing program.

## 📝 Tasks

### 🛠️	Build the Hidden Word Display

#### Description
Create the main game setup for Hangman. Start with a predefined list of words, choose one word for the game, and display the player's progress using underscores for letters that have not been guessed yet.

#### Requirements
Completed program should:

- Store several possible words in a list
- Choose one word for the player to guess
- Show the word as `_ _ _` placeholders at the start
- Update the display after each correct guess
- Keep track of letters the player has already guessed


### 🛠️	Add Guessing Rules and Win/Lose Logic

#### Description
Finish the game by letting the player guess one letter at a time. Check whether each guess is correct, reduce the number of remaining attempts for incorrect guesses, and end the game with a clear message.

#### Requirements
Completed program should:

- Accept single-letter guesses from the user
- Decrease remaining attempts after incorrect guesses
- Prevent repeated guesses from breaking the game
- End with a win message when the word is completed
- End with a lose message when attempts run out
