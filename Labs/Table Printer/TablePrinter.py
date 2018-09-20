##
# Purpose: Prints a list of lists in a beautiful, right-justified format.
##
import sys

data = [["Apples", "Bananas", "Grapes"],
        ["Cakes", "Pies", "Ice Creams", "Cookies"],
        ["Dogs", "Cats", "Birds", "Snakes"],
]

def PrintFormattedTable(table):
    columnWidth = [0] * len(table)
    for i in range(len(table)):
        try:
            length = len(max(data[i], key = len))
            columnWidth[i] = length
        except IndexError:
            continue

    for item in zip(*table):
        print(*item)

PrintFormattedTable(data)
