def div(a, b):
    return a/b


assert div(3, 6) == 0.5, 'Failed'
print('Passed')


assert div(6, 6) == 1, 'Failed'
print('Passed')


assert div(2, 4) == 0.5, 'Failed'
print('Passed')

assert div(15, 3) == 5, 'Failed'
print('Passed')

assert div(6, 0) == 1, 'Failed'
print('Passed')