from typing import Literal


class Rectangle:
    def __init__(self, length: float, width: float) -> None:
        if length <= 0:
            raise ValueError("Length cannot be negative.")
        if width <= 0:
            raise ValueError("Width cannot be negative.")
        self.length = length
        self.width = width

    def _set_dimension(
        self, dimension: Literal["length", "width"], delta: float
    ) -> None:
        prev_value = getattr(self, dimension)
        new_value = prev_value + delta

        if new_value <= 0:
            raise ValueError(f"Unable to comply. {dimension} cannot be negative.")
        else:
            setattr(self, dimension, new_value)

    def area(self) -> float:
        return self.length * self.width

    def perimeter(self) -> float:
        return 2 * (self.length + self.width)

    def update_dimension(
        self, dimension: Literal["length", "width"], delta: float
    ) -> None:
        self._set_dimension(dimension, delta)
