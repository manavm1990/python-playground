import pytest

from playground.rectangle import Rectangle


def test_rectangle_area():
    rectangle = Rectangle(5, 4)
    assert rectangle.area() == 20


def test_rectangle_perimeter():
    rectangle = Rectangle(5, 4)
    assert rectangle.perimeter() == 18


def test_rectangle_negative_length():
    with pytest.raises(ValueError):
        Rectangle(-5, 4)


def test_rectangle_negative_width():
    with pytest.raises(ValueError):
        Rectangle(5, -4)


def test_update_dimension_length_positive():
    rectangle = Rectangle(5, 4)
    rectangle.update_dimension("l", 1)
    assert rectangle.length == 6


def test_update_dimension_length_negative():
    rectangle = Rectangle(6, 4)
    with pytest.raises(ValueError):
        rectangle.update_dimension("l", -7)


def test_update_dimension_width_positive():
    rectangle = Rectangle(5, 4)
    rectangle.update_dimension("w", 2)
    assert rectangle.width == 6


def test_update_dimension_width_negative():
    rectangle = Rectangle(5, 6)
    with pytest.raises(ValueError):
        rectangle.update_dimension("w", -7)
