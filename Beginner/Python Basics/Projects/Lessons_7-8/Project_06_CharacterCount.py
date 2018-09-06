# This project references skills learned from lessons 1-8.

sentence = input("Enter a nice sentence for me to count characters: ")
characterCounts = {}

for i in range(len(sentence)):
    if sentence[i] not in characterCounts:
        characterCounts.setdefault(sentence[i].lower(), 1) # This is to counter capital letters and lowercase letters of the same thing being counted as separate things.
    else:
        j = characterCounts.get(sentence[i], 0)
        j = j + 1
        characterCounts.update({sentence[i] : j})

for k, v in characterCounts.items():
    print(k, v)
