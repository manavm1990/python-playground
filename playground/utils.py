import csv
import json
import re
from collections import Counter
from collections.abc import Iterable
from pathlib import Path

import requests


def calculate_tip(base_amt: float, tip_pct: float) -> tuple[str, str]:
    tip_amt = base_amt * (tip_pct / 100)
    total_amt = base_amt + tip_amt
    return f"${tip_amt:.2f}", f"${total_amt:.2f}"  # "$15.00", "$115.00"


def convert_to_uppercase(strings: list) -> list:
    return [string.upper() for string in strings]


def count_words_in_file(filename: str) -> dict:
    # `with` automatically closes the file
    with Path.open(Path(filename)) as file_contents:
        words = re.findall(r"\w+", file_contents.read().lower())
    return dict(Counter(words))  # {'hello': 2, 'world': 1}


def get_files_with_extension(directory_path: str, extension: str) -> list:
    # `str(file)` gives file path as a string instead of extra stuff with Path objects.
    return [str(file) for file in Path(directory_path).rglob(f"*.{extension}")]


def get_html_content(url: str) -> str:
    response = requests.get(url)
    return response.text


def get_second_largest(numbers: list) -> int | None:
    # Remove 🔥 duplicates
    unique_numbers = set(numbers)

    if len(unique_numbers) < 2:
        return None
    sorted_numbers = sorted(unique_numbers)
    return int(sorted_numbers[-2])


def greet(name: str) -> str:
    return "Hello " + name


def greet_all(names: Iterable[str]) -> list:
    return [greet(name) for name in names]


def is_palindrome(s: str) -> bool:
    return (
        s == s[::-1]
    )  # no start, no stop, and `-1` step means "go backwards" ➡️ reverse!


def normalize_id(user_id: int | str) -> str:
    if isinstance(user_id, int):  # Is `user_id` an integer?
        return f"user-{100_000 + user_id}"  # adds 100000 to `user_id` while formatting as a string
    else:
        return user_id


def output_csv_to_json(csv_file_path: str, json_file_path: str) -> None:
    with Path.open(Path(csv_file_path)) as csv_file:
        csv_data = list(csv.DictReader(csv_file))

    with Path.open(Path(json_file_path), "w") as json_file:
        json.dump(csv_data, json_file)


# This 💩 is a GENERATOR EXPRESSION.
def sum_even_numbers(numbers: Iterable[int]) -> int:
    """Given an iterable of integers, return the sum of all even numbers in the iterable."""
    return sum(num for num in numbers if num % 2 == 0)
