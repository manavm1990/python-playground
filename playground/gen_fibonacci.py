# fibonacci.py
from collections.abc import Generator


def generate_fibonacci(limit: int = 100) -> Generator[int, None, None]:
    """Generates Fibonacci numbers up to a given limit."""
    a, b = 0, 1
    while a < limit:
        yield a
        a, b = b, a + b
