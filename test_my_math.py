import my_math


def test_add():  # test jednostkowy
    assert my_math.add(4, 5) == 20
    assert my_math.add(6, 6) == 12
    assert my_math.add(6, 7) == 13


# test_add()


def test_product():
    assert my_math.product(3, 6) == 18
    assert my_math.product(5, 5) == 25


# test_product()
