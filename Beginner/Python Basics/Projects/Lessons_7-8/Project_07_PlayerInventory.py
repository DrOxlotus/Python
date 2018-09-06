# This project references skills learned from lessons 1-8.
from random import randint

pInventory = {"Ripped Cloth": 200, "Sharp Tooth": 40, "Dull Kris": 1, "Broad Shortsword": 2, "Lightly-Toasted Bread": 20}
loot = ["Snow-Covered Shoelaces", "Rusted Blunderbuss", "Dull Kris", "Yak Fur", "Bent Nail", "Cardinal Ruby", "Ebonweave Cloth", "Dreamsilk", "Primal Diamond", "Steelskin Potion"]

def AddToInventory(inventoryReference, lootReference):
    itemDrops = randint(0, 2)
    i = 0
    while i <= itemDrops:
        lootTable = randint(0, len(loot))
        lootQuantity = randint(1, 10)
        try:
            itemToAdd = loot[lootTable]
            pInventory[itemToAdd] = lootQuantity # This has its own key check; if the key exists, update that key, if not, add the new key and its value.
            i = i + 1
        except IndexError:
            continue
    print("")
    ShowInventory(pInventory)

def TotalItemsInInventory(inventoryReference):
    totalItems = 0
    for k, v in pInventory.items():
        totalItems = totalItems + v

    return totalItems

def ShowInventory(inventoryReference):
    for k, v in pInventory.items():
        print(k + ": " + str(v)) # Very important to cast here, otherwise a TypeError is thrown. (You can't concatenate on an integer.)

    print("Total Items: " + str(TotalItemsInInventory(pInventory)))

ShowInventory(pInventory)
AddToInventory(pInventory, loot)
