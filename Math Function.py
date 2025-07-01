n=int(input("Enter a number: "))
import math
def sqrt(n):
    if n == 0:
        return 0
    else:
        return math.sqrt(n)
print("Square root:", sqrt(n))

def log(n):
    if n == 0:
        return 0
    else:
        return math.log(n)
print("Logarithm:", log(n))


def sinex(n):
    if n == 0:
        return 0
    else:
        return math.sin(n)
print("Sine:", sinex(n))