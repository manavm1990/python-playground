from typing import Literal


class Rectangle:
    def __init__(self, length: float, width: float) -> None:
        if length <= 0:
            raise ValueError("Length cannot be negative.")
        if width <= 0:
            raise ValueError("Width cannot be negative.")
        self.__length = length
        self.__width = width

    @property
    def length(self) -> float:
        return self.__length

    @length.setter
    def length(self, length: float) -> None:
        if length <= 0:
            raise ValueError("Length cannot be negative.")
        self.__length = length

    @property
    def width(self) -> float:
        return self.__width

    @width.setter
    def width(self, width: float) -> None:
        if width <= 0:
            raise ValueError("Width cannot be negative.")
        self.__width = width

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
        return self.__length * self.__width

    def perimeter(self) -> float:
        return 2 * (self.__length + self.__width)

    def update_dimension(
        self, dimension: Literal["length", "width"], delta: float
    ) -> None:
        self._set_dimension(dimension, delta)

    def __str__(self) -> str:
        return f"Rectangle(length={self.__length}, width={self.__width})"

    def __repr__(self) -> str:
        return f"Rectangle(length={self.__length}, width={self.__width})"

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Rectangle):
            return NotImplemented
        return self.__length == other.__length and self.__width == other.__width
