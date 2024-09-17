# test_time_it.py

import time

from playground.decorators.time_it import time_it


@time_it
def test_function():
    for _ in range(1000000):
        pass


def test_time_it_decorator(capfd):
    start_time = time.time()
    test_function()
    out, err = capfd.readouterr()
    end_time = time.time()

    # Check that output contains the correct function name
    assert "Function `test_function` executed in" in out

    # Check that the printed execution time is within expected bounds
    execution_time = float(out.split(" ")[-2])
    expected_execution_time = end_time - start_time
    assert (
        abs(execution_time - expected_execution_time) < 0.1
    )  # Allow a small margin for timing inaccuracies
