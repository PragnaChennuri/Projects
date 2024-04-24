# This Hangman game challenges the user to guess a word by making guesses within a limited number of attempts. 
# If the user fails to guess the word within the allotted guesses, they lose. However, if they successfully guess the word, 
# they win!

# importing the random for choosing a random word from the list of words in the file
import random
# importing the word_list to be able to choose the words
from word_list import words
# importing the hangman_art to access the ASCII art
from hangman_art import art

# choosing a random word from the list of words
chosen_word = random.choice(words)
# making an empty string to store the correct guesses made by the user
word_t = ""

# looping through the chosen word from above and initializing the empty string with hyphens 
for i in range(0, (len(chosen_word))):
    word_t += "_ "
print(word_t)

# initializing the game by printing the first element in the ASCII art list
print(art[0])
# the total numberof guesses the user can make
wrong_guess_total = 6
# a variable that stores the number of guesses made by each user
guess = 0

# the loop continues until we reach the total number of guesses we can make
while guess < wrong_guess_total:
    # asking the user to input their guess
    user_guess = input("Make your guess: ")
    # making the guess lowercase because all the words in the list are lowercase
    user_guess_lower = user_guess.lower()

    # can't change characters in a sting because they are immutable in python
    # hence changing the string to a list
    word_l = list(word_t)
    
    # checking if the guess made by the user in the list
    if user_guess_lower in chosen_word:
        # if it is we go through the chosen_word variable to figure out the position of the user's guess in the word
        for character in range((len(chosen_word))):
            # once we find the correct position we replace "_" with the correctly guessed character
            if chosen_word[character] == user_guess_lower:
                word_l[character] = user_guess_lower
        # combining the list into a string to be able to see each update on the screen
        word_t = "".join(word_l)
    
    # if the user's guess is not part of the word then
    else:
        # we increment the guess variable to make sure we are within the limit
        guess += 1
        # we then print the respective ASCII art position based on the guess number
        print(art[guess])

    # we print the word to be able to see the updates on the screen
    print(word_t)

    # if the user guessed everything correctly then the following message will get outputted followed by the chosen word
    if chosen_word == word_t:
        print(f"Good job! You made the correct guess, the word is {chosen_word}.")

# if the user is unable to guess the word correctly then we output a message followed by the chosen word
if(guess == 6):
    print(f"Unfortunate! The correct word is {chosen_word}.")
