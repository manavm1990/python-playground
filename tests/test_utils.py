from playground.utils import (
    convert_to_uppercase,
    count_words_in_file,
    get_second_largest,
    greet,
    greet_all,
    is_palindrome,
    normalize_id,
    sum_even_numbers,
)

names = ["Alice", "Bob", "Charlie"]
numbers = [1, 2, 4, 5, 6, 8, 10, 86, 99]


def test_convert_to_uppercase():
    assert convert_to_uppercase(names) == ["ALICE", "BOB", "CHARLIE"]


def test_count_words_in_file(tmp_path):
    # Arrange
    example_file = tmp_path / "example_file.txt"
    example_file.write_text("Hello, World! Hello")

    # Act
    result = count_words_in_file(str(example_file))

    # Assert
    assert result == {"hello": 2, "world": 1}


def test_get_second_largest():
    assert get_second_largest(numbers) == 86
    assert get_second_largest([2]) is None


def test_greet_all():
    assert greet_all(["Alice", "Bob", "Charlie"]) == [
        "Hello Alice",
        "Hello Bob",
        "Hello Charlie",
    ]


def test_greeting():
    assert greet("Alice") == "Hello Alice"
    assert greet("Bob") == "Hello Bob"


def test_is_palindrome():
    assert is_palindrome("bob")
    assert not is_palindrome("tom")


def test_normalize_id():
    assert normalize_id(1) == "user-100001"
    assert normalize_id(42) == "user-100042"
    assert normalize_id("abc123") == "abc123"


def test_sum_even_numbers():
    assert sum_even_numbers(numbers)
