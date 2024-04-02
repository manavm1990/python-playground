from collections.abc import Iterable


def greet_all(names: Iterable[str]) -> None:
    for name in names:
        print("Hello " + name)


def greeting(name: str) -> str:
    return "Hello " + name


def normalize_id(user_id: int | str) -> str:
    if isinstance(user_id, int):
        return f"user-{100_000 + user_id}"
    else:
        return user_id
