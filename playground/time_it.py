# time_it.py

import time
from collections.abc import Callable
from typing import Any


def time_it(
    func: Callable[..., Any],
) -> Callable[..., Any]:
    def wrap(*args: Any, **kwargs: Any) -> Any:
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Function `{func.__name__}` executed in {execution_time:.6f} seconds")
        return result

    return wrap
