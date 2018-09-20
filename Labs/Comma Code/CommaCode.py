# This project references skills learned from lessons 1-7.

# Perhaps not the most elegant way to accomplish the goal, but it works! :thumbs_up:

def DelimitList(list):
    for i in range(len(food)):
        if i < len(food) - 1:
            if i == len(food) - 2:
                print(food[i], end = ", and ")
            else:
                print(food[i], end = ", ")
        else:
            print(food[i])

food = ['goulash', 'steak', 'potatoes',]

DelimitList(food)
