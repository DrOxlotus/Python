##
# Purpose: Given two lists, this program will find the values that match in each list, and then count how many times they match.
##
import random

listOne = listTwo = []

for i in range(20):
    listOne.append(random.randint(1,20))
    listTwo.append(random.randint(1,20))

length = 0
setList = [] # List of the same values between the two lists
while length < len(listOne):
    for number in listOne:
        if(listOne[number] == listTwo[number]):
            setList.append(number)
        length = (length + 1)
# Counting the number of occurences of the same value in the new list
print("Value occurences in the list: {}".format([[value, setList.count(value)] for value in set(setList)]))
