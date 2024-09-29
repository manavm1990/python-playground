# tests/test_utils.py
import csv
import json
from pathlib import Path
from unittest.mock import patch

import pytest

from playground.utils import (
    calculate_tip,
    convert_to_uppercase,
    count_words_in_file,
    get_files_with_extension,
    get_html_content,
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


@pytest.fixture
def csv_and_json_paths(tmp_path):
    csv_tmp = tmp_path / "test.csv"
    json_tmp = tmp_path / "test.json"

    csv_path = Path(str(csv_tmp))
    json_path = Path(str(json_tmp))

    return csv_path, json_path


@pytest.fixture
def example_file(tmp_path):
    file = tmp_path / "example_file.txt"
    file.write_text("Hello, World! Hello")
    return file


@pytest.fixture
def example_directory(tmp_path):
    directory = tmp_path / "directory"
    directory.mkdir()
    (directory / "file1.txt").touch()
    (directory / "file2.txt").touch()
    (directory / "file3.log").touch()
    return directory


@pytest.fixture
def url_and_html():
    test_url = "https://example.com"
    test_html = "<html><body>Example</body></html>"
    return test_url, test_html


def test_calculate_tip():
    assert calculate_tip(100.00, 15) == ("$15.00", "$115.00")


def test_convert_to_uppercase():
    assert convert_to_uppercase(names) == ["ALICE", "BOB", "CHARLIE"]


def test_count_words_in_file(example_file):
    result = count_words_in_file(str(example_file))
    assert result == {"hello": 2, "world": 1}


def test_get_html_content(url_and_html):
    test_url, test_html = url_and_html

    with patch("requests.get") as mock_get:
        mock_get.return_value.text = test_html

        response = get_html_content(test_url)

        assert response == test_html


def test_get_files_with_extension(example_directory):
    result = get_files_with_extension(str(example_directory), "txt")
    expected_files = ["file1.txt", "file2.txt"]
    expected_files_with_paths = [
        str(example_directory / file) for file in expected_files
    ]
    assert set(result) == set(expected_files_with_paths)


def test_get_second_largest():
    assert get_second_largest(numbers) == 86
    assert get_second_largest([2]) is None


def test_greet_all():
    assert greet_all(names) == ["Hello Alice", "Hello Bob", "Hello Charlie"]


def test_greeting():
    assert greet("Alice") == "Hello Alice"
    assert greet("Bob") == "Hello Bob"


def test_output_csv_to_json(csv_and_json_paths):
    csv_path, json_path = csv_and_json_paths
    content = [["name", "age"], ["Alice", 20], ["Bob", 25]]

    with csv_path.open("w+", newline="") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerows(content)

    output_csv_to_json(str(csv_path), str(json_path))

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
