import math

import pytest

import circle


def test_area():
    assert pytest.approx(circle.circle_are(1), 0.001) == math.pi
    assert pytest.approx(circle.circle_are(2), 0.001) == math.pi*(2 **2)
    assert pytest.approx(circle.circle_are(2.2), 0.001) == math.pi*(2.2 **2)


def test_area_exception():
    with pytest.raises(ValueError):
        circle.circle_are(-3)


def test_area_type_exception():
    with pytest.raises(TypeError):
        circle.circle_are('asf')


