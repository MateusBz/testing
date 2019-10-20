import math


def circle_area(r):
    if type(r) not in [float, int]:
        raise TypeError('The radius must be a number')
    if r < 0:
        raise ValueError("The radius can't be negative")

    return math.pi*(r**2)

