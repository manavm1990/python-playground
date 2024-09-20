# test_fibonacci.py
from playground.fibonacci import generate_fibonacci


def test_generate_fibonacci():
    # Test default limit (100)
    expected = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    result = list(generate_fibonacci())
    assert result == expected, f"Expected {expected}, but got {result}"

    # Test with custom limit
    limit = 10
    expected = [0, 1, 1, 2, 3, 5, 8]
    result = list(generate_fibonacci(limit))
    assert result == expected, f"Expected {expected}, but got {result}"
