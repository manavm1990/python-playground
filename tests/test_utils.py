from playground.utils import (
    convert_to_uppercase,
    greet,
    greet_all,
    normalize_id,
    sum_even_numbers,
)

names = ["Alice", "Bob", "Charlie"]


def test_convert_to_uppercase():
    result = convert_to_uppercase(names)
    assert result == ["ALICE", "BOB", "CHARLIE"]


def test_greet_all():
    result = greet_all(["Alice", "Bob", "Charlie"])
    assert result == ["Hello Alice", "Hello Bob", "Hello Charlie"]


def test_greeting():
    assert greet("Alice") == "Hello Alice"
    assert greet("Bob") == "Hello Bob"


def test_normalize_id():
    assert normalize_id(1) == "user-100001"
    assert normalize_id(42) == "user-100042"
    assert normalize_id("abc123") == "abc123"


def test_sum_even_numbers():
    assert sum_even_numbers([1, 2, 4, 5, 6, 8, 10, 86, 99])
