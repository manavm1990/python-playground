from typing import Literal


class Rectangle:
    def __init__(self, length, width):
        if length <= 0:
            raise ValueError("Length cannot be negative.")
        if width <= 0:
            raise ValueError("Width cannot be negative.")
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

    def _set_dimension(self, dimension, delta):
        prev_value = getattr(self, dimension)
        new_value = prev_value + delta

        if new_value <= 0:
            raise ValueError(f"Unable to comply. {dimension} cannot be negative.")
        else:
            setattr(self, dimension, new_value)

    def update_dimension(self, dim: Literal["l", "w"], delta: float):
        dimension = "length" if dim == "l" else "width"
        self._set_dimension(dimension, delta)
