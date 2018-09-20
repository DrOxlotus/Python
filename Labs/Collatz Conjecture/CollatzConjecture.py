# This project references skills learned from lessons 1-4.

def Collatz(number):
    if (number % 2 == 0):
        return (number / 2)
    else:
        return (3 * number) + 1

try:
    userInput = int(input("Enter a number for the Collatz Conjecture: "))
    value = 0
    while value != 1:
        value = Collatz(userInput)
        userInput = value
        print(int(value))
except ValueError:
    print("Invalid input!")
