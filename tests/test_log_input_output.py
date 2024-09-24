from playground.decorators.log_input_output import decorate_log_input_output


@decorate_log_input_output
def add_2_nums(a, b=0):
    return a + b


def test_log_input_output_decorator(capfd):
    result = add_2_nums(5, b=10)
    assert result == 15

    # `capfd` - a Pytest fixture for capturing output and errors.
    out, err = capfd.readouterr()
    assert "Input args: (5,), kwargs: {'b': 10}" in out
    assert "Output: 15" in out
