import functools
from collections.abc import Callable
from typing import Any


def cache_decorator(
    func: Callable[..., Any],
) -> Callable[..., Any]:
    cache = {}  # dictionary

    @functools.wraps(func)  # decorator to preserve metadata
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        # Is it in cache?
        key = (args, frozenset(kwargs.items()))

        # If not......
        if key not in cache:
            result = func(*args, **kwargs)
            cache[key] = result
        return cache[key]

    return wrapper
