##
# Author: Alex Metz (alex.tar.gz@gmail.com)
##

# Import Section
import re # This is the Regular Expression Python library.

def load_story(fileName):
    print("\nYou chose {}. Excellent! Loading story now...\n".format(fileName))
    files = {
        "The Big Bang Theory": "tbbt.txt",
        "Game of Thrones": "got.txt",
        "The Lord of the Rings": "lotr.txt",
        "World of Warcraft": "wow.txt",
        "Overwatch": "ow.txt",
        "Diablo 3": "d3.txt"
    }
    with open('stories\{}'.format(files[fileName]), 'r') as storyFile:
        story=storyFile.read()
        for word in story.split():
            if(re.search(r"\{([A-Za-z0-9_]+)\}", word)):
                if any(x in [".", ",", ";", "!"] for x in word[len(word)-1]):
                    input0 = raw_input("Enter a(n) {}: ".format(re.sub(r'[{}]', '', word[0:len(word)-1])))
                    story = story.replace(word[0:len(word)-1], input0, 1)
                else:
                    input1 = raw_input("Enter a(n) {}: ".format(re.sub(r'[{}]', '', word)))
                    story = story.replace(word, input1, 1) # The 1 is very important; without it every occurence would be replaced with the first match.

        print(story)

choice = ""
while(choice == ""):
    print("""
    1: The Big Bang Theory
    2: Game of Thrones [NYI]
    3: The Lord of the Rings [NYI]
    4: World of Warcraft
    5: Overwatch [NYI]
    6: Diablo 3 [NYI]
    7: Exit Mad Libs
    """)
    choice = raw_input("Which story would you like to load? ")
    if choice == "1":
        load_story("The Big Bang Theory")
    elif choice == "2":
        #load_story("Game of Thrones")
        print("\nNot Yet Implemented. Have a lovely day!")
    elif choice == "3":
        #load_story("Lord of the Rings")
        print("\nNot Yet Implemented. Have a lovely day!")
    elif choice == "4":
        load_story("World of Warcraft")
    elif choice == "5":
        #load_story("Overwatch")
        print("\nNot Yet Implemented. Have a lovely day!")
    elif choice == "6":
        #load_story("Diablo 3")
        print("\nNot Yet Implemented. Have a lovely day!")
    elif choice == "7":
        print("\nHave a lovely day!")
        break
    else:
        print("\nThat's not a valid choice; try again!")
