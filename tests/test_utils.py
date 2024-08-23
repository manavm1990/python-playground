import csv
import json
from pathlib import Path

from playground.utils import (
    calculate_tip,
    convert_to_uppercase,
    count_words_in_file,
    get_files_with_extension,
    get_second_largest,
    greet,
    greet_all,
    is_palindrome,
    normalize_id,
    output_csv_to_json,
    sum_even_numbers,
)

names = ["Alice", "Bob", "Charlie"]
numbers = [1, 2, 4, 5, 6, 8, 10, 86, 99]


def test_calculate_tip():
    assert calculate_tip(100.00, 15) == ("$15.00", "$115.00")


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


def test_get_files_with_extension(tmp_path):
    # Arrange: Create a temporary directory with 2️⃣ `txt` files and 1️⃣ `log` file.
    directory = tmp_path / "directory"
    directory.mkdir()  # create directory
    (directory / "file1.txt").touch()
    (directory / "file2.txt").touch()
    (directory / "file3.log").touch()

    # Act: Seek `txt` files.
    result = get_files_with_extension(str(directory), "txt")

    # Assert
    expected_files = ["file1.txt", "file2.txt"]  # Expected files with '.txt' extension
    # Generate expected absolute paths and convert to string
    expected_files_with_paths = [str(directory / file) for file in expected_files]

    assert set(result) == set(expected_files_with_paths)


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


def test_output_csv_to_json(tmp_path):
    # Act
    content = [["name", "age"], ["Alice", 20], ["Bob", 25]]

    csv_tmp = tmp_path / "test.csv"
    json_tmp = tmp_path / "test.json"

    csv_path = Path(str(csv_tmp))
    json_path = Path(str(json_tmp))

    # `'w+'` is for reading the 💩 consistently across platforms
    with csv_path.open("w+", newline="") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerows(content)

    # Act - The JSON file will now be created
    output_csv_to_json(str(csv_tmp), str(json_tmp))

    # Assert
    with json_path.open() as json_file:
        data = json.load(json_file)

    expected_data = [{"name": "Alice", "age": "20"}, {"name": "Bob", "age": "25"}]
    assert data == expected_data


def test_is_palindrome():
    assert is_palindrome("bob")
    assert not is_palindrome("tom")


def test_normalize_id():
    assert normalize_id(1) == "user-100001"
    assert normalize_id(42) == "user-100042"
    assert normalize_id("abc123") == "abc123"


def test_sum_even_numbers():
    assert sum_even_numbers(numbers)
