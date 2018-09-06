list = ['elephant', 'rat', 'bat', 'cat', 'bird', 'dog']
biggerList = [['elephant', 'bat'], ['pie', 'cake', 'candy'], 'cat', 'dog']

#print(list[2]) (Fetching data using a list INDEX)
#print(biggerList[0]) (Fetching a sublist using a list INDEX)
#print(biggerList[0][0]) (Fetching the first element of the first sublist using sublist INDICES)
#print(biggerList[0:]) (Fetching the entire list using slice notation)
#print(len(biggerList)) (Fetching the length of a list)
"""
Setting the value of the first item in the small list to shark from elephant
list[0] = "shark"
print(list[0])
"""
#print(list + biggerList) (Concatenating two lists together)
#print(list * 2) (Replicating a list and its items)

"""
# Removed all values from the small list
del(list[0:len(list)])
print(list)
"""
"""
Creates a list of desserts instead of an arbitrary number of variables
desserts = []
while True:
    dessertName = input("Enter a dessert: ")
    if dessertName == "":
        break
    else:
        desserts = desserts + [dessertName]

for dessert in desserts:
    print(dessert)
"""

"""
Testing the 'in' keyword to check if a value is in a list.
if "elephant" in list:
    sub = input("Name a new animal: ")
    if sub.lower() == "elephant":
        print("I think you meant 'shark'.")
        sub = "shark"
        list[0] = sub
    else:
        list[0] = sub
    print(list[0])
else:
    print("No")
"""

# What great names these are. :)
#smallSmallList = ['bird']
#aSmallList = aSmallerList = anEvenSmallerList = aSmallerListSmallerThanThat = smallSmallList
#print(aSmallList)
