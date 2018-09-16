##
# Purpose: A classic implementation of the Hangman game.
##
from sys import exit
from random import randint

def BuildWordList(fileName):
    wordList = []
    with open('assets\{}'.format(fileName), 'r') as wordFile:
        words = wordFile.read()
        for word in words.split():
            wordList.append(word)

    Start(wordList)

def Search(userInput, word, list):
    list = list
    for value, character in enumerate(word): # Using an enumerate object, which is a tuple, to support the iteration over the string to handle sequencing
        if character == userInput:
            list.insert(value, character)
        else:
            pass
    return list

def Start(wordList):
    index = randint(0, len(wordList))
    word = "schnapps"
    characters = []
    for char in word:
        characters.append(char)

    print("Welcome to Hangman! There are " + str(len(characters)) + " letters in your random word. Good luck!")
    print("If you know the word, enter it as a guess. If you're done, enter 0 and the program will exit.")

    print(word)

    guessAmount = 0
    guessList = []
    while(guessAmount < 8):
        userInput = input("\n" + "[" + str(guessAmount) + "]" + " Enter your guess: ")
        guessAmount = guessAmount + 1
        if userInput == word or guessList == characters:
            print("\n" + "You won!")
            exit(0)
        elif(userInput == "0"):
            print("Thanks for playing!")
            exit(0)
        else:
            guessList = Search(userInput, word, guessList)
    print("\n" + "The correct word was: " + word)
    print("Your correct guesses were: ", end = "") # Don't print a newline
    print(guessList)

BuildWordList("words.txt")
