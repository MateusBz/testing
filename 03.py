def factorial(n):
    if n == 0:
        return 1
    else:
        temp = 1
        for i in range(2, n + 1):
            temp *= i
        return temp


assert factorial(5) == 120
assert factorial(2) == 2

