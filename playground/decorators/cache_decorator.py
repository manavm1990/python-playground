import functools
from collections.abc import Callable
from typing import Any


def decorate_cache(
    func: Callable[..., Any],
) -> Callable[..., Any]:
    cache = {}  # dictionary

    @functools.wraps(func)  # decorator to preserve metadata
    # `*args` - positional arguments (e.g. *args)
    # `**kwargs` - keyword arguments (e.g. **object/rest parameters**)
    def wrap(*args: Any, **kwargs: Any) -> Any:
        # Is it in cache?
        key = (args, frozenset(kwargs.items()))

        # If not......
        if key not in cache:
            result = func(*args, **kwargs)
            cache[key] = result
        return cache[key]

    return wrap
