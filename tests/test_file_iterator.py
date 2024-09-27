# test_file_iterator.py

import pytest

from playground.classes.file_iterator import FileIterator


def test_file_iterator_reads_lines(temp_file):
    file = temp_file("line1\nline2\nline3\n")
    file_iterator = FileIterator(file)
    iterator = iter(file_iterator)

    assert next(iterator) == "line1"
    assert next(iterator) == "line2"
    assert next(iterator) == "line3"

    with pytest.raises(StopIteration):
        next(iterator)


def test_file_iterator_strips_lines(temp_file):
    file = temp_file("  line1  \n  line2  \n  line3  ")
    file_iterator = FileIterator(file)
    iterator = iter(file_iterator)

    assert next(iterator) == "line1"
    assert next(iterator) == "line2"
    assert next(iterator) == "line3"

    with pytest.raises(StopIteration):
        next(iterator)


def test_file_iterator_using_example_file(temp_file):
    file = temp_file("Hello, World! Hello")
    file_iterator = FileIterator(file)
    iterator = iter(file_iterator)

    expected_lines = ["Hello, World! Hello"]
    for expected_line in expected_lines:
        assert next(iterator) == expected_line

    with pytest.raises(StopIteration):
        next(iterator)
