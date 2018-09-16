##
# Purpose: Allows the user to pick the side of their die, how many times they want to roll, and then outputs each roll and how many times a value occurred.
##
from random import *

def dice_roller(minValue, maxValue, rolls):
    numbers = []
    for _ in range(rolls):
        dieValue = randint(minValue,maxValue)
        numbers.insert(_,dieValue)
        print("You rolled: {}".format(dieValue))

    print("\nUnique values in list: {}".format(len(set(numbers))))
    print("Value occurences in list: {}".format([[v,numbers.count(v)] for v in set(numbers)]))

maxValue = int(input('What is the maximum amount of sides on your die? '))
rolls = int(input('How many times would you like to roll your die? '))
dice_roller(1, maxValue, rolls)
