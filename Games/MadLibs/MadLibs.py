##
# Purpose: A classic implementation of the MadLibs game!
##

import re

pattern = re.compile(r"{[a-zA-Z\s]+}")

def LoadStory(fileName):
    print("\n" + "You chose, " + fileName + ", what an excellent choice!" + "\n")
    fileDictionary = {
        "A Very Bad Bedtime Story": "bedtime_story.txt"
    }
    with open("stories\\" + fileDictionary[fileName], "r") as file:
        fullStory = file.read()
        modifiedStory = re.split(r"\s+(?=[^()]*(?:\{|$))", fullStory)
        for word in modifiedStory:
            print(word)
            if (re.search(pattern, word)):
                if any(character in [".", ",", ";", "!"] for character in word[len(word)-1]):
                    partOfSpeech = input("Enter a(n) {}: ".format(re.sub(r'[{}]', '', word[0:len(word)-1])))
                    fullStory = fullStory.replace(word[0:len(word)-1], partOfSpeech, 1)
                else:
                    partOfSpeech = input("Enter a(n) {}: ".format(re.sub(r'[{}]', '', word)))
                    fullStory = fullStory.replace(word, partOfSpeech, 1)

        print(fullStory)

choice = ""
while(choice == ""):
    print("Welcome to MadLibs!" + "\n" + """
    1: A Very Bad Bedtime Story
    2: Exit Mad Libs
    """)
    choice = input("What would you like to do? ")
    if choice == "1":
        LoadStory("A Very Bad Bedtime Story")
    elif choice == "2":
        print("\nHave a lovely day!")
        break
    else:
        print("\nThat's not a valid choice; try again!")
