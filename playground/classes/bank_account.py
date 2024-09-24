# playground/bank_account.py
class BankAccount:
    def __init__(
        self, name: str, account_id: int, initial_balance: float = 0.00
    ) -> None:
        self.__name: str = name
        self.__account_id: int = account_id
        self.__balance: float = initial_balance

    @property
    def balance(self) -> float:
        return self.__balance

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str) -> None:
        self.__name = name

    def deposit(self, amount: float) -> float:
        if amount < 0:
            raise ValueError("Deposit amount must be positive")
        self.__balance += amount
        return self.__balance

    def withdraw(self, amount: float) -> float:
        if amount < 0:
            raise ValueError("Withdrawal amount must be positive")
        if amount > self.__balance:
            raise ValueError("Insufficient Funds")
        else:
            self.__balance -= amount
        return self.__balance

    def get_balance(self) -> float:
        return self.__balance

    def __str__(self) -> str:
        return f"BankAccount(balance={self.__balance:.2f})"

    def __repr__(self) -> str:
        return f"BankAccount(initial_balance={self.__balance:.2f})"
