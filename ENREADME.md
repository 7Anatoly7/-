# Game "Field of Wonders"
## Short description
A game for guessing the word on a space theme.

## Detailed description
From a certain list of words, one word is taken that needs to be guessed.
All words consist only of Russian lowercase letters, but in addition to them, you can also enter commands.
The game will continue until you guess the word or want to quit or give up.
If you guess the word, the program displays a victory message and you win the game, otherwise if you leave without guessing the word, the program says goodbye to you, which is considered a loss.

### Game mechanism
First, a random word is selected from the list.
All words consist only of Russian lowercase letters.
Next, the game begins.
During the game, the number of attempts to guess the word is counted.
Letters not found in a word are marked with asterisks, and if a letter is found, then the asterisk is replaced with the letter itself.
If you guess all the letters in a word, the program displays a victory message.
You can also enter not just a letter, but the whole word.
If the word is guessed, then you win, otherwise the program displays a message that you did not guess the word.
If you find a letter in a word, then it cannot be used again, since it has already been guessed.
If you enter any other character, the program displays an invalid input message.
If the first character of the string is an exclamation mark, then a check is made to see if it is a command and if one exists.
The game control commands are listed below.
At the end of the game, the number of attempts spent on guessing the word is displayed.

#### Commands
1. !help - display help
2. !use - show the list of used letters
3. !remain - show the remaining letters of the alphabet
4. !surrender - surrender
5. !exit - exit the game
