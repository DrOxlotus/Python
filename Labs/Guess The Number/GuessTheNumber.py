# This project references skills learned from lessons 1-4.
from random import randint

# Global Variables
randomNumber = randint(1, 20)
playerGuesses = 0
guessedNumber = 0
#chances = 5
#

print("I'm thinking of a number between 1 and 20: ")
while guessedNumber != randomNumber:
    guessedNumber = int(input("Enter a number: "))
    if (guessedNumber == randomNumber):
        print("YOU WIN! You won after " + str(playerGuesses + 1) + " guess(es).")
    elif guessedNumber > 20 or guessedNumber < 1:
        print("Your guess is out of bounds. This doesn't count toward your guesses.")
    else:
        print("WRONG!")
        playerGuesses = playerGuesses + 1
