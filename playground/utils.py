import re
from collections import Counter
from collections.abc import Iterable
from pathlib import Path


def convert_to_uppercase(strings: list) -> list:
    """Given a list of trings, convert them all to UPPER CASE."""
    return [string.upper() for string in strings]


def count_words_in_file(filename: str) -> dict:
    # `with` automatically closes the file
    with Path.open(Path(filename)) as file_contents:
        words = re.findall(r"\w+", file_contents.read().lower())
    return dict(Counter(words))


def greet(name: str) -> str:
    return "Hello " + name


def get_second_largest(numbers: list) -> int | None:
    if len(numbers) < 2:
        return None
    sorted_numbers = sorted(numbers)
    return sorted_numbers[-2]


def greet_all(names: Iterable[str]) -> list:
    return [greet(name) for name in names]


def is_palindrome(s: str) -> bool:
    return s == s[::-1]


def normalize_id(user_id: int | str) -> str:
    if isinstance(user_id, int):
        return f"user-{100_000 + user_id}"
    else:
        return user_id


def sum_even_numbers(numbers: Iterable[int]) -> int:
    """Given an iterable of integers, return the sum of all even numbers in the iterable."""
    return sum(num for num in numbers if num % 2 == 0)
