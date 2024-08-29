"""Practice with Functions"""

from random import randint

#
print(randint(10, 25))


# These are parameters
def sum(num1: int, num2: int) -> int:
    """Return the sum of num1 and num2"""
    return num1 + num2


print(sum(num1=20, num2=70))
# The above are arguments


def diceroller(num1: int, num2: int) -> int:
    """random number"""
    return randint(num1, num2)


print(diceroller(1, 6))
