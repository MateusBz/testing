from class_calc import Calc


def test_add_two_numbers():
    c = Calc()
    assert c.add(4,5) == 9



def test_add_three_numbers():
    c = Calc()
    assert c.add(4, 5 , 6) == 15


def test_subtract_two_numbers():
    c = Calc()
    assert c.sub(10, 7) == 3


def test_multiply_two_numbers():
    c = Calc()
    assert c.multi(10, 7) == 70


def test_multiply_many_numbers():
    c = Calc()
    assert c.multi(1, 2, 3, 4, 5) == 120


def test_divide_two_numbers():
    c = Calc()
    assert c.divide(13, 2) == 6.5


def test_divide_by_zero():
    c = Calc()
    assert c.divide(5, 0) == 'inf'