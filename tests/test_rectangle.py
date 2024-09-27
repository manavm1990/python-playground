# tests/test_rectangle.py
import pytest

from playground.classes.rectangle import Rectangle


@pytest.fixture
def rectangle():
    # Initialize a new Rectangle instance for each test.
    return Rectangle(5, 4)


def test_rectangle_area(rectangle):
    assert rectangle.area() == 20


def test_rectangle_perimeter(rectangle):
    assert rectangle.perimeter() == 18


def test_rectangle_negative_length():
    with pytest.raises(ValueError):
        Rectangle(-5, 4)


def test_rectangle_negative_width():
    with pytest.raises(ValueError):
        Rectangle(5, -4)


def test_update_dimension_length_positive(rectangle):
    rectangle.update_dimension("length", 1)
    assert rectangle.length == 6


def test_update_dimension_length_negative(rectangle):
    with pytest.raises(ValueError):
        rectangle.update_dimension("length", -7)


def test_update_dimension_width_positive(rectangle):
    rectangle.update_dimension("width", 2)
    assert rectangle.width == 6


def test_update_dimension_width_negative(rectangle):
    with pytest.raises(ValueError):
        rectangle.update_dimension("width", -7)
