##
# Purpose: Calculates the divisors (numbers that divide into another number) of whatever number the user inputs.
##
def findDivisors(number, range):
    divisorList = []
    for divisor in range:
        if number % divisor == 0:
            divisorList.append(divisor)
    return divisorList

number = int(input("Please enter a number to divide: "))
divisorRange = list(range(1, (number + 1)))

print("{}".format(number) + " is divisible by the following divisors: {}".format(", ".join(map(str, findDivisors(number, divisorRange)))))
