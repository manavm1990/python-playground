# log_input_output.py

import functools
from collections.abc import Callable
from typing import Any


def decorate_log_input_output(
    func: Callable[..., Any],
) -> Callable[..., Any]:
    @functools.wraps(func)
    def wrap(*args: Any, **kwargs: Any) -> Any:
        print(f"Input args: {args}, kwargs: {kwargs}")
        result = func(*args, **kwargs)
        print(f"Output: {result}")
        return result

    return wrap
