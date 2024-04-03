from collections.abc import Iterable


def convert_to_uppercase(strings: list) -> list:
    """Given a list of trings, convert them all to UPPER CASE."""
    return [string.upper() for string in strings]


def greet(name: str) -> str:
    return "Hello " + name


def get_second_largest(numbers: list) -> int | None:
    if len(numbers) < 2:
        return None
    sorted_numbers = sorted(numbers)
    return sorted_numbers[-2]


def greet_all(names: Iterable[str]) -> list:
    return [greet(name) for name in names]


def normalize_id(user_id: int | str) -> str:
    if isinstance(user_id, int):
        return f"user-{100_000 + user_id}"
    else:
        return user_id


def sum_even_numbers(numbers: Iterable[int]) -> int:
    """Given an iterable of integers, return the sum of all even numbers in the iterable."""
    return sum(num for num in numbers if num % 2 == 0)
