import pytest
import calc


@pytest.fixture()
def calc():
    c = calc.Calculator()
    return c


@pytest.mark.parametrize('num1, num2, res', [(5, 10, 15), (0, 0, 0), (-3, -7, -10)])
def test_calc_add_integer(num1, num2, res, calc):
    assert calc.add(num1, num2) == res

# def test_calc_add_integer(c):
#     assert c.add(3, 8) == 11
#     assert c.add(3, 9) == 12
#     assert c.add(11, 11) == 22


def test_calc_add_float(calc):
    assert pytest.approx(calc.add(5.2, 5.2), 0.0001) == 10.4
    assert pytest.approx(calc.add(4.23, -2.1), 0.0001) == 2.13


def test_calc_add_string(calc):
    assert calc.add('abc', 'cd') == 'abccd'
    assert calc.add('', '') == ''

