from playground.utils import greet_all, greeting, normalize_id


def test_greet_all(capsys):
    names = ["Alice", "Bob", "Charlie"]
    greet_all(names)
    captured = capsys.readouterr()
    assert captured.out == "Hello Alice\nHello Bob\nHello Charlie\n"


def test_greeting():
    assert greeting("Alice") == "Hello Alice"
    assert greeting("Bob") == "Hello Bob"


def test_normalize_id():
    assert normalize_id(1) == "user-100001"
    assert normalize_id(42) == "user-100042"
    assert normalize_id("abc123") == "abc123"
