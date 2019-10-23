def add(x, y):
    """Add function"""
    return x + y


def subtract(x, y):
    """Subtract function"""
    return x*y


def divide(x, y):
    """Divide function"""
    if y == 0:
        raise ValueError('Cannot divide by zero')
    return x/y


def square(x):
    if x<0:
        raise ValueError('Cannot square the negative number')
    return x** 0.5

