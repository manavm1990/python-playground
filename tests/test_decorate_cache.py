from playground.decorators.cache import decorate_cache


@decorate_cache
def no_args_function():
    return "no_args"


@decorate_cache
def add(a, b):
    return a + b


@decorate_cache
def subtract(a, b=0):
    return a - b


@decorate_cache
def multiply(a, b):
    return a * b


@decorate_cache
def concat(*args, **kwargs):
    return "".join(str(arg) for arg in args) + "".join(
        f"{key}={value}" for key, value in kwargs.items()
    )


def test_cache_for_function_without_arguments():
    result_first_call = no_args_function()
    result_second_call = no_args_function()
    assert result_first_call == result_second_call
    assert result_first_call is result_second_call


def test_cache_for_function_with_positional_arguments():
    result_first_call = add(1, 2)
    result_second_call = add(1, 2)
    assert result_first_call == result_second_call
    assert result_first_call is result_second_call


def test_cache_for_function_with_keyword_arguments():
    result_first_call = subtract(a=5, b=3)
    result_second_call = subtract(a=5, b=3)
    assert result_first_call == result_second_call
    assert result_first_call is result_second_call

    result_first_call_default = subtract(5)
    result_second_call_default = subtract(5)
    assert result_first_call_default == result_second_call_default
    assert result_first_call_default is result_second_call_default


def test_cache_with_different_arguments():
    result_first_call = multiply(2, 3)
    result_second_call = multiply(3, 2)
    assert result_first_call == 6
    assert result_second_call == 6
    assert (
        result_first_call == result_second_call
    )  # Both should yield the correct result


def test_cache_with_any_arguments():
    result_first_call = concat("a", "b", c="d")
    result_second_call = concat("a", "b", c="d")
    assert result_first_call == result_second_call
    assert result_first_call is result_second_call

    result_diff_call = concat("a", "b", d="e")
    assert result_first_call != result_diff_call
