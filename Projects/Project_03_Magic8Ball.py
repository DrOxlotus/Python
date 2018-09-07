# This project references skills learned from lessons 1-6.
from random import randint

# Global variables
responses = [
    "No.",
    "Don't count on it.",
    "Ask again later.",
    "Outlook... not so good.",
    "Very doubtful.",
    "Without a doubt... just kidding.",
    "Concentrate, and then ask again.",
    "Cannot predict right now.",
    "Yes.",
    "Yes, definitely.",
    "You may rely on it.",
    "Without a doubt.",
    "Outlook... good.",
    "As I see it, yes.",
    "The signs point to... yes.",
    "My sources say... yes.",
]
#
# An alternative of handling this loop's logic would be to fetch the length of the list - 1.
while True:
    try:
        userQuestion = input("Ask your magic 8-Ball a question: ")
        randomResponse = randint(0, len(responses))
        print("Your question was: " + userQuestion + "\n" + "Magic 8-Ball says: " + responses[randomResponse])
    except IndexError:
        continue
