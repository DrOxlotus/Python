from random import randint

def SayHello(name):
    print("Hello, " + name + "!")

def Multiply(x, y):
    return (x * y)

def Divide(x, y):
    try:
        return (x / y)
    except ZeroDivisionError:
        print("Error: A divisor cannot equal 0.")

"""
randomNumber1 = randint(1, 10)
randomNumber2 = randint(1, 10)

product = Multiply(randomNumber1, randomNumber2)
if product > 50:
    print(product, " : ", randomNumber1, "*", randomNumber2)
else:
    print("Less than 50.")
"""
"""
def test():
    global value
    value = "test"

value = "global"
test()
print(value)
"""
"""
Divide(4, 2)
Divide(12, 4)
Divide(100, 0)
"""
